#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueft docs/prd/... gegen die Registry.

REPARATUREN dieses Laufs (Nutzerentscheidung 2026-07-20):

(1) FELDWERTE statt Feldnamen. Die Vorfassung prueft `if feld in body` — sie
    stellte damit fest, dass das WORT `signal` irgendwo im Abschnitt vorkommt.
    Ein leeres, ein auf `—` gesetztes oder ein voellig fremdes Feld bestand
    diese Pruefung. "Messfeld gefuellt" war eine Aussage ueber Zeichenketten,
    nicht ueber Inhalte. Jetzt wird die Feldtabelle geparst und der WERT
    geprueft: nicht leer, kein Nullwert, und fuer die Achsenfelder aus dem
    zugehoerigen Vokabular.

(2) GRUNDGESAMTHEIT aus der Registry. Die Vorfassung fuehrte eine abgetippte
    Liste, in der REQ-040 stand — inzwischen deprecatet. Der Validator
    verlangte also einen Messmodell-Abschnitt fuer eine ID, die es nicht mehr
    geben darf, und meldete FAIL gegen ein korrektes Dokument. Die Liste wird
    jetzt abgeleitet: alle aktiven REQ-IDs mit Messmodell-Abschnitt.

(3) KEIN Zahlliteral. Die Vorfassung suchte woertlich nach einer Altzahl und
    band sich damit selbst an einen ueberholten Stand. Die Zahlen kommen aus
    der Registry-Historie.

(4) BLOCKING fuer ALLE Eintraege nachgerechnet, nicht nur fuer CONTRA-IDs.

(5) EIN Parser. Registry-Lesen aus registry_model — die frueher hier
    definierte Fassung ("erste Zelle, die wie ein Status aussieht") kannte die
    Kopfzeile nicht und konnte Statuswerte aus fremden Tabellen uebernehmen.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blocking_model as BM      # noqa: E402
import registry_model as RM      # noqa: E402
from validate_trace import scan_count_literals  # noqa: E402  (EINE Fassung)

# Repo-Pfad ueberschreibbar (argv[1]), damit die Negativkontrolle gegen eine
# PRAEPARIERTE Kopie laufen kann. Ein Selbsttest, der nur die echten Dateien
# sehen kann, belegt nichts.
DEFAULT_REPO = "/Users/vincentschnetzer/Documents/Run&Bike"
REPO = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_REPO
PRD = os.path.join(REPO, "docs/prd/revyr-endurance-platform.prd.md")

prd = open(PRD, encoding="utf-8").read()
reg = RM.load(REPO)

# Werte, die ein Feld als NICHT gefuellt ausweisen. `MISSING`/`BLOCKER` zaehlen
# ausdruecklich als GEFUELLT-UND-BEGRUENDET: ein sichtbarer Befund ist eine
# Aussage, eine leere Zelle ist keine.
NULLISH = {"", "-", "—", "–", "n/a", "na", "tbd", "todo", "?", "…", "..."}

MEASUREMENT_FIELDS = ["measurement_type", "signal", "target_or_pass_condition",
                      "measurement_window", "evidence_source", "source_type",
                      "owner", "release_gate", "rationale"]

# Achsenfelder mit abschliessendem Wertebereich. Fuer sie genuegt "nicht leer"
# nicht — der FUEHRENDE Wert muss aus dem Vokabular stammen.
VOCAB_FIELDS = {
    "source_type": {"EXPLICIT", "ASSUMPTION", "MISSING", "INFERRED"},
    "release_gate": set(BM.GATES) | {"MISSING"},
}

fail = []


def check(cond, msg):
    print(("PASS  " if cond else "FAIL  ") + msg)
    if not cond:
        fail.append(msg)


def parse_field_table(body):
    """| Feld | Wert |-Tabelle eines Messmodell-Abschnitts."""
    out = {}
    for line in body.split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) != 2:
            continue
        key = BM.clean(cells[0]).lower()
        if key in ("feld", "field", "") or set(key) <= set("-: "):
            continue
        out[key] = cells[1]
    return out


def value_is_filled(raw):
    v = BM.clean(raw)
    return bool(v) and v.lower() not in NULLISH


def leading_vocab_value(raw, vocab):
    """Erstes Token des Werts, sofern es im Vokabular liegt.

    `GATE-A0` und `A0` sind DASSELBE Gate in zwei Schreibweisen. Das PRD
    schreibt durchgaengig die lange Form. Die Vorfassung dieser Pruefung
    verlangte die kurze und meldete daraufhin fast jedes Requirement als
    Vokabularverstoss — eine Schreibweise als Sachverhalt gelesen. Das
    Praefix wird deshalb normalisiert, NICHT der Wert nachgesehen.
    """
    v = BM.clean(raw).upper()
    want = {x.upper() for x in vocab}
    for token in re.findall(r"[A-Z][A-Z_0-9\-]*", v):
        for cand in (token, re.sub(r"^GATE-", "", token)):
            if cand in want:
                return cand
    return None


# ---------------------------------------------------------------------------
# 1. ID-Bestand
# ---------------------------------------------------------------------------
for pref in RM.MANAGED_PREFIXES:
    c = reg.counts(pref)
    if c:
        print("### %-7s %s" % (pref, "  ".join("%s=%d" % kv for kv in sorted(c.items()))))
print()

n_req = reg.count("REQ")
n_ac = reg.count("AC")
n_ev = reg.count("EV")

for pref in ("REQ", "AC", "EV", "USER", "NFR"):
    missing = [i for i in reg.active(pref) if i not in prd]
    check(not missing, "%s: alle aktiven Registry-IDs im PRD (fehlend: %s)"
          % (pref, missing))

# --- deprecatete IDs: SPALTENBASIERT, nicht markerbasiert -----------------
#
# BEFUND/FIX: Die Vorfassung entschied ueber eine Liste von Stichwoertern in
# derselben Zeile ("deprecat", "historisch", "ersetzt", …). Genau diese
# Konstruktion ist der wiederkehrende Defekt dieses Projekts: sie ist blind
# fuer jede Formulierung, die niemand vorher aufgeschrieben hat. Sie meldete
# hier sechs Verstoesse gegen ein KORREKTES Dokument — beanstandet wurden
# u. a. die Bestandstabelle (deren SPALTE "deprecated" heisst, ohne dass das
# Wort in der Zeile steht), die Migrationstabelle (`− REQ-040 | 2026-07-20`)
# und ein Fliesstext ueber die Teilung.
#
# Die tragende Frage ist nicht, ob ein Stichwort danebensteht, sondern ob die
# Alt-ID als GUELTIGER ANKER verwendet wird. Deshalb spaltenbasiert — dieselbe
# Regel, die C3c in validate_intake.py anwendet. Zwei Werkzeuge, eine Regel.
# MUSTERBASIERT statt Aufzaehlung. Eine feste Liste von Spaltennamen ist
# dieselbe Falle wie eine feste Liste von Stichwoertern: sie kennt genau die
# Schreibweisen, die jemand vorher aufgeschrieben hat. Die Negativkontrolle hat
# das prompt vorgefuehrt — `Requirement ID` fehlte in der Aufzaehlung, und ein
# eingeschleuster toter Anker blieb unentdeckt.
ANCHOR_COLUMN_RE = re.compile(
    r"^(?:canvas|vision|requirement|req|ac|acceptance|evidence|ev|trace|trc|"
    r"risk|risiko|user|nfr)\b"
    r"(?:[\s\-]*(?:id|item|criterion|kriterium|anker|link|ids))?"
    r"(?:\s*\(.*\))?$", re.I)


def is_anchor_column(name):
    return bool(ANCHOR_COLUMN_RE.match(BM.clean(name).strip()))


def anchor_occurrences(text, idv):
    """Fundstellen, an denen `idv` als LEBENDER Anker in einer Tabellenspalte
    steht. Provenienz-, Migrations- und Bestandsspalten zaehlen nicht."""
    out = []
    header = None
    prev = None
    for lineno, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if not s.startswith("|"):
            header = None
            prev = None
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and all(set(c) <= set("-: ") and c for c in cells):
            header = [BM.clean(c).lower() for c in (prev or [])]
            prev = None
            continue
        prev = cells
        if not header:
            continue
        # Eine durchgestrichene Zeile ist als aufgehoben ausgewiesen.
        if cells and "~~" in cells[0]:
            continue
        for i, cell in enumerate(cells):
            if i >= len(header) or idv not in cell:
                continue
            if not is_anchor_column(header[i]):
                continue
            if "~~" in cell or "deprecat" in cell.lower():
                continue
            out.append({"zeile": lineno, "spalte": header[i],
                        "text": cell[:120]})
    return out


for pref in ("REQ", "AC", "EV", "USER", "NFR"):
    for d in reg.deprecated(pref):
        occ_total = sum(1 for l in prd.splitlines() if d in l)
        live = anchor_occurrences(prd, d)
        check(not live,
              "%s: %s steht im PRD an keiner Ankerstelle (%d Fundstellen gesamt, "
              "%d davon in einer Ankerspalte: %s)"
              % (pref, d, occ_total, len(live), live[:3]))

# --- Bestandstabelle: WERTE vergleichen, nicht Formulierungen suchen ------
#
# Die Vorfassung suchte nach dem Satz "41 aktive AC". Das PRD fuehrt den Stand
# als TABELLE — sachlich besser und von der Vorfassung nicht erkannt. Jetzt
# wird die Tabelle geparst und Zelle gegen Registry gerechnet.
INV_HEADER_START = ["präfix", "aktiv", "deprecated"]
inv = {}
header = None
prev = None
for line in prd.split("\n"):
    s = line.strip()
    if not s.startswith("|"):
        header = None
        prev = None
        continue
    cells = [c.strip() for c in s.strip("|").split("|")]
    if cells and all(set(c) <= set("-: ") and c for c in cells):
        head = [BM.clean(c).lower() for c in (prev or [])]
        header = head if head[:3] == INV_HEADER_START else None
        prev = None
        continue
    prev = cells
    if not header:
        continue
    pref = BM.clean(cells[0])
    if pref in RM.MANAGED_PREFIXES:
        inv[pref] = {header[i]: BM.clean(c) for i, c in enumerate(cells)
                     if i < len(header)}

check(bool(inv), "Bestandstabelle im PRD gefunden (%d Praefixe)" % len(inv))
inv_bad = []
for pref, row in sorted(inv.items()):
    for col, status in (("aktiv", "active"), ("deprecated", "deprecated"),
                        ("reserviert", "reserved")):
        if col not in row:
            continue
        m = re.match(r"(\d+)", row[col])
        if not m:
            continue
        if int(m.group(1)) != reg.count(pref, status):
            inv_bad.append({"praefix": pref, "spalte": col, "prd": m.group(1),
                            "registry": reg.count(pref, status)})
check(not inv_bad, "Bestandstabelle stimmt zellenweise mit der Registry ueberein "
                   "(Abweichungen: %s)" % inv_bad)
check(n_ac >= n_req and n_ev >= n_req,
      "Invariante AC(%d)>=REQ(%d) und EV(%d)>=REQ(%d)" % (n_ac, n_req, n_ev, n_req))

# ---------------------------------------------------------------------------
# 2. Ueberholte Zaehlstaende im PRD — abgeleitet, nicht abgetippt
# ---------------------------------------------------------------------------
current = {str(reg.count(p)) for p in RM.Registry.COUNT_FAMILY}
stale = sorted(reg.forbidden_count_literals() - current, key=int)
live = []
for lineno, l in enumerate(prd.splitlines(), 1):
    # ID-Token zuerst entfernen: die Ziffern in CAN-123 oder REQ-039 sind Teil
    # eines Bezeichners, keine Zaehlung. Ohne diesen Schritt meldet die
    # Pruefung jede Canvas-Referenz als "ueberholte Gesamtzahl" — ein
    # Fehlalarm, der die echten Treffer unter sich begraebt.
    l_ids = RM.ID_RE.sub("", l)
    # Ebenso Ordnungszahlen: "Registry §8 Punkt 39" verweist auf einen
    # Listenpunkt. Eine Zahl, die einen Punkt BENENNT, zaehlt nichts.
    l_ids = re.sub(r"(?:Punkt|Nr\.?|§|Zeile|Zeilen|Schritt|Regel|Bedingung)\s*"
                   r"[\d.,\s–—-]*\d", " ", l_ids)
    for s in stale:
        if not re.search(r"(?<!\d)" + s + r"(?!\d)", l_ids):
            continue
        # Eine ueberholte Zahl DARF vorkommen, wenn sie ausdruecklich als
        # historisch, als Rechenschritt oder als Defektbeschreibung auftritt.
        if re.search(r"\d{4}-\d{2}-\d{2}|historisch|hartkodiert|Stand 20|"
                     r"vor dem Auftau|erwartet|Alt-|damals|frueher|früher|"
                     r"^\|\s*[-+]", l.strip()):
            continue
        live.append({"zeile": lineno, "zahl": s, "text": l.strip()[:110]})
check(not live, "keine lebende ueberholte Gesamtzahl im PRD "
                "(geprueft: %s; Treffer: %s)" % (stale, live))

# ---------------------------------------------------------------------------
# 3. C16 — blocking_scope, Vokabulare, Formelwortlaut
# ---------------------------------------------------------------------------
bs = [l.strip() for l in prd.splitlines() if "blocking_scope" in l]
ok = all(re.search(r"entfallen|ersetzt|Alt-Wert|GESCHLOSSEN|lebt am|mischte|"
                   r"alte Formel", l) for l in bs)
check(ok, "blocking_scope nur in der Entfallens-Dokumentation (%d Zeilen)" % len(bs))

viol = []
for m in re.finditer(r"blocked_gates`?[:|]?\s*\|?\s*`?\[([^\]]*)\]", prd):
    for v in [x.strip() for x in m.group(1).split(",") if x.strip()]:
        if v in BM.ACTIVITIES or v not in BM.GATES:
            viol.append(("gates", v))
for m in re.finditer(r"blocked_activities`?[:|]?\s*\|?\s*`?\[([^\]]*)\]", prd):
    for v in [x.strip() for x in m.group(1).split(",") if x.strip()]:
        if v in BM.GATES or v not in BM.ACTIVITIES:
            viol.append(("activities", v))
check(not viol, "Gate-/Taetigkeitsvokabulare disjunkt und abgeschlossen "
                "(Verstoesse: %s)" % viol)

# Formelwortlaut: die aufgehobene Fassung darf nur als aufgehoben dastehen.
old_formula = [i for i, l in enumerate(prd.splitlines(), 1)
               if BM.FORMULA_TEXT_SUPERSEDED in l and not BM._is_historical(l)]
check(not old_formula,
      "Blocking-Formel im geltenden Wortlaut `status != resolved` "
      "(Altfassung als geltend in Zeilen: %s). %s"
      % (old_formula, BM.FORMULA_DIVERGENCE_NOTE))

# ---------------------------------------------------------------------------
# 4. blocking NACHRECHNEN — jeder Eintrag mit Achsen, nicht nur CONTRA-
# ---------------------------------------------------------------------------
reg_text = open(reg.path, encoding="utf-8").read()
axes = {}
for name, text in (("ID-REGISTRY.md", reg_text), ("prd.md", prd)):
    for eid, ax in BM.parse_axis_tables(text).items():
        axes.setdefault(eid, (name, ax))
check(bool(axes), "Statusmodell-Tabellen gelesen (%d Eintraege mit blocking-Achse: %s)"
      % (len(axes), sorted({e.split("-")[0] for e in axes})))

unchecked = []
for eid, (src, ax) in sorted(axes.items()):
    v = BM.check_vocabulary(ax)
    check(not v, "%s: keine Gate-vs-Taetigkeit-Vermischung" % eid)
    if v:
        continue
    derived, reasons = BM.derive_blocking(ax)
    rec = ax["blocking_recorded"]
    if rec is None:
        unchecked.append({"id": eid, "quelle": src,
                          "wert": ax["blocking_verbatim"][:60]})
        continue
    check(derived == rec,
          "%s (%s): blocking abgeleitet=%s == eingetragen=%s (Klauseln: %s)"
          % (eid, src, derived, rec, reasons))
check(not unchecked,
      "0 blocking-Werte ohne maschinelle Nachrechnung (%d ungeprueft: %s)"
      % (len(unchecked), unchecked))

# Kein Praefix ausserhalb des zugelassenen Geltungsbereichs traegt blocking.
BLOCKING_SCOPE_PREFIXES = {"OQ", "CONTRA"}
out_of_scope = sorted(e for e in axes if e.split("-")[0] not in BLOCKING_SCOPE_PREFIXES)
check(not out_of_scope,
      "blocking bleibt auf %s beschraenkt (ausserhalb: %s)"
      % (sorted(BLOCKING_SCOPE_PREFIXES), out_of_scope))

# ---------------------------------------------------------------------------
# 5. Messmodell — FELDWERTE, Grundgesamtheit abgeleitet
# ---------------------------------------------------------------------------
blocks = {}
heads = list(re.finditer(r"^###\s+(REQ-\d{3})\s*[—–-]\s*(.+)$", prd, re.M))
for i, h in enumerate(heads):
    end = heads[i + 1].start() if i + 1 < len(heads) else len(prd)
    blocks[h.group(1)] = prd[h.end():end]

active_req = reg.active("REQ")
with_block = [r for r in active_req if r in blocks]
check(len(with_block) == len(active_req),
      "Messmodell-Abschnitt fuer jedes aktive Requirement "
      "(fehlend: %s)" % sorted(set(active_req) - set(with_block)))

dep_blocks = [r for r in reg.deprecated("REQ") if r in blocks]
check(not dep_blocks,
      "kein Messmodell-Abschnitt fuer deprecatete Requirements (gefunden: %s)"
      % dep_blocks)

empty_fields = []
bad_vocab = []
for rid in sorted(with_block):
    fields = parse_field_table(blocks[rid])
    for f in MEASUREMENT_FIELDS:
        if f not in fields:
            empty_fields.append({"id": rid, "feld": f, "problem": "Feld fehlt"})
        elif not value_is_filled(fields[f]):
            empty_fields.append({"id": rid, "feld": f, "problem": "Wert leer/Nullwert",
                                 "wert": BM.clean(fields[f])[:40]})
    for f, vocab in VOCAB_FIELDS.items():
        if f in fields and value_is_filled(fields[f]):
            if leading_vocab_value(fields[f], vocab) is None:
                bad_vocab.append({"id": rid, "feld": f,
                                  "wert": BM.clean(fields[f])[:60],
                                  "problem": "kein Wert aus %s" % sorted(vocab)})
check(not empty_fields,
      "%d Messmodell-Abschnitte: alle %d Felder mit echtem WERT belegt "
      "(nicht nur Feldname vorhanden). Verstoesse: %d"
      % (len(with_block), len(MEASUREMENT_FIELDS), len(empty_fields)))
for e in empty_fields[:20]:
    print("        -", e)
check(not bad_vocab,
      "Achsenfelder tragen einen Wert aus ihrem Vokabular (Verstoesse: %d)"
      % len(bad_vocab))
for e in bad_vocab[:20]:
    print("        -", e)

# ---------------------------------------------------------------------------
# 6. Personas
# ---------------------------------------------------------------------------
for u in reg.active("USER"):
    check(u in prd, "%s im PRD angelegt" % u)
req9 = blocks.get("REQ-009", "")
req11 = blocks.get("REQ-011", "")
check("USER-004" in req9, "REQ-009: Persona-Verknuepfung hergestellt")
check("USER-004" in req11 and "NICHT" in req11,
      "REQ-011: Persona-Verknuepfung geprueft und begruendet abgelehnt")

# ---------------------------------------------------------------------------
# 7. Selbstpruefung des Werkzeugs
# ---------------------------------------------------------------------------
lits = scan_count_literals([os.path.abspath(__file__)], reg.forbidden_count_literals())
check(not lits, "check_prd.py fuehrt keine Gesamtzahl als Literal (%s)" % lits)

print("\n=== FAILURES: %d ===" % len(fail))
for f in fail:
    print("  -", f)
sys.exit(1 if fail else 0)
