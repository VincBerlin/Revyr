#!/usr/bin/env python3
"""Validiert docs/traceability.md gegen die eingefrorene Registry.

Grundsatz: Schlaegt eine Pruefung fehl, ist das ein BEFUND. Widerspricht die
Pruefung dem Dokumenttext, wird der TEXT geaendert, nicht die Pruefung.

REPARATUREN dieses Laufs (Nutzerentscheidung 2026-07-20):

(a) LAUFZEIT statt CACHE. Die Vorfassung las den Scratchpad-Cache
    `derived.json` — einen Stand von VOR Runde 4. Sie meldete daraufhin
    REQ-041/042, AC-043, EV-044, CAN-142/143 und VIS-014 als "erfundene IDs"
    und die Verteilungssummen als falsch: rund drei Dutzend FAILS gegen ein
    KORREKTES Dokument, samt und sonders erzeugt von einer veralteten
    Zwischendatei. Jetzt wird `docs/ID-REGISTRY.md` bei jedem Lauf gelesen.

(b) KEINE Zahlliterale — auch nicht in Prosa. Die Vorfassung fuehrte die
    verbotene Altzahl als STRING (`forbidden = {...}`) und band das Werkzeug
    damit selbst an einen Altstand. Zugleich sah ihre eigene Pruefung diesen
    Verstoss nicht: sie betrachtete nur `tokenize.NUMBER`, und eine Zahl in
    Anfuehrungszeichen ist ein `tokenize.STRING`. Die Pruefung war blind fuer
    ihre eigene Uebertretung. Jetzt werden die verbotenen Zahlen aus der
    Registry-Historie ABGELEITET (`created_at`/`deprecated_at`), und geprueft
    werden NUMBER- **und** STRING-Token. Beim ersten Lauf der neuen Fassung hat
    sie prompt diesen Erklaertext beanstandet, in dem die Altzahlen noch
    ausgeschrieben standen — der Text wurde geaendert, nicht die Pruefung.

(c) SPALTENKOEPFE statt Zeilenform. §5 und die Achsentabellen werden ueber
    ihre Kopfzeile gefunden. Formbasiertes Raten las fremde Tabellen mit.

(d) EIN Parser. Registry-Lesen kommt aus registry_model, Blocking aus
    blocking_model. Dieses Werkzeug definiert weder Parser noch Formel selbst.
"""
import ast
import collections
import io
import os
import re
import sys
import tokenize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blocking_model as BM      # noqa: E402
import registry_model as RM      # noqa: E402

# Der Repo-Pfad ist ueberschreibbar, damit die Negativkontrolle das Werkzeug
# gegen eine PRAEPARIERTE Kopie laufen lassen kann. Ohne das laeuft jeder
# Selbsttest gegen dieselben echten Dateien und belegt nichts.
DEFAULT_REPO = "/Users/vincentschnetzer/Documents/Run&Bike"

GATES = BM.GATES
ACTIVITIES = BM.ACTIVITIES

fails, warns = [], []


def scan_count_literals(paths, forbidden):
    """Zahlliterale UND Zahlen in Zeichenketten.

    Die Vorfassung sah nur NUMBER-Token. Genau dadurch blieb ihre eigene
    Verbotsmenge unentdeckt: sie fuehrte die Altzahl in Anfuehrungszeichen,
    also als STRING. Beide Tokenarten werden jetzt geprueft.

    AUSNAHME, eng und begruendet: ein NUMBER-Token in einer Slice-/Index-
    Position (`text[:N]`, `xs[N]`) ist eine Textbreite, keine Zaehlung. Es kann
    keine Pruefung bestehen oder scheitern lassen. Die Ausnahme gilt NICHT fuer
    Vergleiche, Zuweisungen oder Mengenliterale — dort ist dieselbe Zahl ein
    Befund. Negativkontrolle in selftest_validator.py.
    """
    out = []
    for path in paths:
        if not os.path.isfile(path):
            continue
        with open(path, "rb") as fh:
            try:
                toks = list(tokenize.tokenize(fh.readline))
            except tokenize.TokenError as exc:
                out.append({"file": os.path.basename(path),
                            "problem": "nicht tokenisierbar: %s" % exc})
                continue
        for i, tok in enumerate(toks):
            if tok.type == tokenize.NUMBER and tok.string in forbidden:
                prev = next((t for t in reversed(toks[:i])
                             if t.type not in (tokenize.NL, tokenize.NEWLINE,
                                               tokenize.INDENT, tokenize.DEDENT,
                                               tokenize.COMMENT)), None)
                nxt = next((t for t in toks[i + 1:]
                            if t.type not in (tokenize.NL, tokenize.NEWLINE,
                                              tokenize.COMMENT)), None)
                in_slice = (prev is not None and prev.string in ("[", ":")
                            and nxt is not None and nxt.string in ("]", ":"))
                if in_slice:
                    continue
                out.append({"file": os.path.basename(path), "line": tok.start[0],
                            "literal": tok.string, "art": "NUMBER",
                            "problem": "hartkodierte Gesamtzahl der REQ-Familie"})
            elif tok.type == tokenize.STRING:
                try:
                    val = ast.literal_eval(tok.string)
                except Exception:
                    continue
                if not isinstance(val, str):
                    continue
                # Regex-Quantoren (`{0,80}`, `{2,3}`) sind Musterbreiten, keine
                # Zaehlungen. Ohne diese Ausnahme meldet die Pruefung jedes
                # laengenbegrenzte Suchmuster als hartkodierte Gesamtzahl —
                # ein Fehlalarm gegen korrekten Code.
                probe = re.sub(r"\{\s*\d+\s*(?:,\s*\d+\s*)?\}", " ", val)
                for hit in set(re.findall(r"(?<!\d)(\d{2,3})(?!\d)", probe)):
                    if hit in forbidden:
                        out.append({"file": os.path.basename(path),
                                    "line": tok.start[0], "literal": hit,
                                    "art": "STRING",
                                    "problem": "Gesamtzahl der REQ-Familie in "
                                               "einer Zeichenkette — von einer "
                                               "reinen NUMBER-Pruefung nicht "
                                               "sichtbar"})
    return out


TRUE_LINE_COLUMNS = {"req-id", "vision-link", "value-check-id", "true-line-status",
                     "wired-in-prod?", "evidence-class", "evidence-class-required"}


def parse_true_line_table(text):
    """§5-Tabelle SPALTENKOPFGEBUNDEN lesen. {REQ-ID: {spalte: wert}}."""
    out = {}
    header = None
    prev = None
    for line in text.split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            header = None
            prev = None
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and all(set(c) <= set("-: ") and c for c in cells):
            head = [BM.clean(c).lower() for c in (prev or [])]
            header = head if set(head) == TRUE_LINE_COLUMNS else None
            prev = None
            continue
        prev = cells
        if not header:
            continue
        rid = BM.clean(cells[0])
        if not re.fullmatch(r"REQ-\d{3}", rid):
            continue
        out[rid] = {name: cells[i] for i, name in enumerate(header) if i < len(cells)}
    return out


def main(repo=None):
    repo = repo or (sys.argv[1] if len(sys.argv) > 1 else DEFAULT_REPO)
    doc = os.path.join(repo, "docs/traceability.md")
    txt = open(doc, encoding="utf-8").read()
    reg = RM.load(repo)                      # LAUFZEIT, kein Cache
    active_req = set(reg.active("REQ"))
    n = len(active_req)

    # --- 1. Zahl aktiver Requirements: abgeleitet, nicht hartkodiert
    m = re.search(r"Aus der Registry geparst am \d{4}-\d{2}-\d{2}: (\d+)", txt)
    if not m:
        fails.append("§0.0: abgeleitete Zahl nicht gefunden")
    elif int(m.group(1)) != n:
        fails.append("§0.0 nennt %s, Registry liefert %d" % (m.group(1), n))

    # --- 2. Kernmatrix: je aktive REQ genau eine Zeile
    rows = {}
    dep_rows = []
    for l in txt.split("\n"):
        mm = re.match(r"\|\s*(?:\*\*)?(?:~~)?(TRC-\d{3})", l)
        if not mm:
            continue
        if "~~" in l.split("|")[1]:
            dep_rows.append(mm.group(1))
            continue
        rows[mm.group(1)] = [c.strip() for c in l.strip().strip("|").split("|")]
    if len(rows) != n:
        fails.append("Kernmatrix hat %d aktive Zeilen, erwartet %d" % (len(rows), n))
    for t in rows:
        r = "REQ-" + t.split("-")[1]
        if r not in active_req:
            fails.append("Kernmatrix fuehrt %s zu %s, das nicht aktiv ist" % (t, r))
    for r in sorted(active_req):
        if "TRC-" + r.split("-")[1] not in rows:
            fails.append("Kernmatrix: keine Zeile fuer %s" % r)

    # --- 3. Deprecatete IDs werden gefuehrt, nicht geloescht.
    # Die Liste wird aus der Registry GELESEN. Die Vorfassung tippte fuenf IDs
    # ab und war damit blind fuer jede spaeter deprecatete ID — u. a. fuer die
    # gesamte Runde-4-Menge (REQ-040, AC-040, EV-040, TRC-040, CAN-140).
    #
    # GELTUNGSBEREICH, eng gefasst: nur die Matrixfamilien. Die Kernmatrix ist
    # zeilenweise nach Requirement aufgebaut; eine dort fehlende Alt-ID macht
    # die Migration unauffindbar. CAN- ist bewusst AUSGENOMMEN: die
    # traceability fuehrt Canvas-Items als Anker, nicht als Bestandsliste, und
    # eine Praesenzpflicht fuer jedes deprecatete Canvas-Item waere eine
    # erfundene Anforderung. Ob eine erwaehnte Alt-CAN-ID noch als AKTIVER
    # Anker dasteht, prueft C3c in validate_intake.py — das ist die Frage,
    # auf die es ankommt.
    for pref in ("REQ", "AC", "EV", "TRC"):
        for did in reg.deprecated(pref):
            if did not in txt:
                fails.append("%s ist deprecated und muss GEFUEHRT werden, fehlt aber"
                             % did)
    for did in reg.deprecated("TRC"):
        if did not in dep_rows:
            fails.append("%s nicht als deprecatete Kernmatrix-Zeile gefuehrt" % did)

    # --- 4. true-line-Invarianten fuer ALLE aktiven Requirements
    #
    # BEFUND/FIX: Die Vorfassung erkannte die §5-Tabelle an der FORM ihrer
    # Zeilen ("REQ-xxx | docs/vision… oder **MISSING…"). Diese Form haben auch
    # die Canvas-Ankertabellen in §4.1/§4.2, seit dort Anker als **MISSING
    # ausgewiesen sind. Der Validator las acht fremde Zeilen mit, zaehlte
    # REQ-037/038/041 dreifach und meldete an ihnen true-line-Verstoesse, die
    # es nicht gab — eine Pruefung, die ihren Gegenstand nicht trennscharf
    # trifft, meldet Fehler gegen ein korrektes Dokument.
    # Jetzt spaltenkopfgebunden: dieselbe Konsequenz wie beim Achsenparser.
    tl = parse_true_line_table(txt)
    tl_active = {k: v for k, v in tl.items() if reg.status_of(k) == "active"}
    tl_dep = {k: v for k, v in tl.items() if reg.status_of(k) == "deprecated"}
    tl_alien = {k: v for k, v in tl.items()
                if k not in tl_active and k not in tl_dep}
    if len(tl_active) != n:
        fails.append("§5-Tabelle hat %d aktive Zeilen, erwartet %d"
                     % (len(tl_active), n))
    if tl_alien:
        fails.append("§5 fuehrt Zeilen zu IDs, die die Registry weder aktiv noch "
                     "deprecated kennt: %s" % sorted(tl_alien))
    for rid in sorted(active_req):
        if rid not in tl_active:
            fails.append("§5: keine true-line-Zeile fuer %s" % rid)
    # Die Invarianten gelten fuer AKTIVE Requirements. Eine deprecatete Zeile
    # traegt keinen true-line-Status, sondern einen Migrationsvermerk; sie auf
    # `pending-watcher` zu pruefen hiesse, einen Wert dort zu verlangen, wo das
    # Modell ausdruecklich keinen vorsieht.
    for rid, row in sorted(tl_active.items()):
        for col, want in (("true-line-status", "pending-watcher"),
                          ("wired-in-prod?", "no"),
                          ("evidence-class", "none")):
            got = BM.clean(row.get(col, ""))
            if got != want:
                fails.append("§5 %s: %s = %r, erwartet %r" % (rid, col, got, want))
    for rid, row in sorted(tl_dep.items()):
        if BM.clean(row.get("true-line-status", "")) == "pending-watcher":
            fails.append("§5 %s ist deprecated, traegt aber einen lebenden "
                         "true-line-Status" % rid)

    # --- 5. Kein verbotenes Verdikt / keine Selbstbestaetigung
    for bad in ["READY_FOR_AGILETEAM_PLANNING**", "= verified", "user-confirmed`",
                "true-line-status` = pass"]:
        ctx = txt[max(0, txt.index(bad) - 140):txt.index(bad) + 140] if bad in txt else ""
        neg = any(w in ctx for w in ("nicht", "kein", "keinem", "keiner", "keine"))
        if bad in txt and not neg:
            warns.append("Pruefen: '%s' erscheint im Text" % bad)
    if "BLOCKED_TRACEABILITY" not in txt:
        fails.append("Gesamtstatus BLOCKED_TRACEABILITY fehlt")

    # --- 6. C16: kein lebendes blocking_scope-Feld
    for i, l in enumerate(txt.split("\n"), 1):
        if re.search(r"\|\s*`?blocking_scope`?\s*[|/]", l) or \
           re.search(r"`blocking_scope[:=] ", l):
            fails.append("Zeile %d: blocking_scope wird noch als Feld verwendet" % i)

    # --- 7. C16: Vokabulare disjunkt und abschliessend
    for kind, vocab in (("blocked_gates", GATES), ("blocked_activities", ACTIVITIES)):
        for mm in re.finditer(r"`?" + kind + r"`?\s*[:|]?\s*`?\[([^\]]*)\]", txt):
            for v in [x.strip().strip("`") for x in mm.group(1).split(",") if x.strip()]:
                if v not in vocab:
                    fails.append("%s: unzulaessiger Wert '%s'" % (kind, v))
    if GATES & ACTIVITIES:
        fails.append("Vokabulare nicht disjunkt")

    # --- 7b. Blocking-Formel im Wortlaut: die Altfassung darf nicht als
    # geltende Regel dastehen. Sie darf als AUFGEHOBENE Fassung vorkommen.
    for i, l in enumerate(txt.split("\n"), 1):
        if BM.FORMULA_TEXT_SUPERSEDED in l and not BM._is_historical(l):
            fails.append("Zeile %d fuehrt den aufgehobenen Formelwortlaut als "
                         "geltend (%s)" % (i, BM.FORMULA_DIVERGENCE_NOTE))

    # --- 7c. blocking wird NACHGERECHNET — fuer JEDEN Eintrag mit Achsen,
    # nicht nur fuer CONTRA-IDs (Nutzerentscheidung Punkt 4).
    for eid, ax in sorted(BM.parse_axis_tables(txt).items()):
        viol = BM.check_vocabulary(ax)
        if viol:
            fails.append("%s: Vokabularverstoss %s" % (eid, viol))
            continue
        derived, reasons = BM.derive_blocking(ax)
        rec = ax["blocking_recorded"]
        if rec is not None and derived != rec:
            fails.append("%s: eingetragenes blocking=%s, abgeleitet %s (%s)"
                         % (eid, rec, derived, reasons))

    # --- 8. Alle referenzierten IDs existieren in der Registry
    for mm in RM.ID_RE.finditer(txt):
        i = mm.group(1)
        if i in RM.TEMPLATE_PLACEHOLDERS:
            continue
        if not reg.exists(i):
            fails.append("Erfundene/unbekannte ID: %s" % i)

    # --- 9. Verteilungen summieren auf n
    for label, pat in (("MeasType", 6), ("SourceType", 8)):
        cnt = collections.Counter(
            re.sub(r"[*`~]", "", r[pat]).split(" (")[0].strip() for r in rows.values())
        if sum(cnt.values()) != n:
            fails.append("%s-Summe %d != %d" % (label, sum(cnt.values()), n))
    mt_row = collections.Counter(re.sub(r"[*`~]", "", r[6]).strip() for r in rows.values())
    for typ, cnt in mt_row.items():
        mm = re.search(r"\| " + typ + r" \| (\d+) \|", txt)
        if mm and int(mm.group(1)) != cnt:
            fails.append("§2 nennt %s=%s, Kernmatrix zaehlt %d" % (typ, mm.group(1), cnt))

    # --- 10. Keine Pruefung haengt an einer hartkodierten Requirement-Zahl.
    forbidden = reg.forbidden_count_literals()
    for f in scan_count_literals([os.path.abspath(__file__)], forbidden):
        fails.append("Zahlliteral im Validator: %s" % f)

    print("Registry gelesen: %s" % reg.path)
    print("aktive Requirements (aus Registry abgeleitet): %d" % n)
    print("Kernmatrix aktiv: %d | deprecated gefuehrt: %s" % (len(rows), dep_rows))
    print("§5-Zeilen: %d aktiv, %d deprecated" % (len(tl_active), len(tl_dep)))
    print("verbotene Zahlliterale (abgeleitet, nicht genannt): %s"
          % " ".join(sorted(forbidden, key=int)))
    print("\nFAILS: %d" % len(fails))
    for f in fails:
        print("  FAIL", f)
    print("WARNS: %d" % len(warns))
    for w in warns:
        print("  warn", w)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
