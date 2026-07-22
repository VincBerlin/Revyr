#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
blocking_model.py — DIE EINZIGE Implementierung des C16-Blocking-Modells.

Jeder Validator und jeder Generator IMPORTIERT aus diesem Modul. Es gibt keine
zweite Fassung der Formel, keinen kopierten Ausdruck, keine ID-spezifische
Sonderbehandlung.

Vorgeschichte (Nutzerentscheidung 2026-07-19, C16):
Das frühere Feld `blocking_scope` mischte Release-Gates mit Taetigkeiten.
Die woertliche Lesart der letzten Formelklausel verglich einen Gate-Bezeichner
(A0, B, C) mit einer Taetigkeitsliste (field-test, release, …). Beide
Vokabulare sind DISJUNKT — die Klausel lieferte fuer jeden gegateten Eintrag
`false` und liess `blocking` still absinken. `blocking_scope` ist deshalb
ersatzlos entfallen und durch zwei getrennte Felder ersetzt.

Kanonische Formel (Registry §3.1):

    blocking = status NOT IN [resolved]
               OR resolution_status != accepted
               OR evidence_status IN [failed, blocked]
               OR current_gate IN blocked_gates
               OR current_activity IN blocked_activities

WORTLAUT-ANGLEICHUNG (Nutzerentscheidung 2026-07-20, Punkt 6):
Der Bericht zitierte die erste Klausel als `status == open`, die normativen
Quellen schreiben `status != resolved`. Fuer die beiden GUELTIGEN Werte
(`open`, `resolved`) sind beide Fassungen aequivalent — fuer einen FEHLENDEN
oder unbekannten `status` NICHT:

    status = MISSING  ->  `== open`      liefert false  (blocking sinkt still ab)
    status = MISSING  ->  `!= resolved`  liefert true   (fail-closed)

Genau dieser Fall trat bei NFR-008 auf. Die Implementierung folgt jetzt dem
normativen Wortlaut und ist fail-closed: was nicht nachweislich `resolved` ist,
blockiert. Ein fehlender Statuswert ist ein Befund, kein Freibrief.

Registry §3.1 praezisiert: bei `evidence_status IN [planned, pending]` entsteht
ein aktueller Blocker NUR ueber die beiden letzten Klauseln. `planned`/`pending`
allein blockiert nichts.

HARTE REGEL: `current_gate` wird AUSSCHLIESSLICH gegen `blocked_gates`
geprueft, `current_activity` AUSSCHLIESSLICH gegen `blocked_activities`.
Ein Gate-Bezeichner in `blocked_activities` (oder umgekehrt) ist ein FEHLER,
kein Sonderfall — `check_vocabulary()` meldet ihn, `derive_blocking()`
verweigert die Ableitung.
"""

import re

# ---------------------------------------------------------------------------
# Abschliessende, DISJUNKTE Wertebereiche (Registry §3.1, Zeilen 120–121)
# ---------------------------------------------------------------------------

GATES = frozenset({"P0", "A0", "A1", "A2", "B", "C", "D", "E"})

ACTIVITIES = frozenset({
    "documentation", "planning", "implementation", "field-test", "release",
    "store-submission", "database-schema-finalization", "account-release",
    "competition-release", "territory-release",
})

# Die Disjunktheit ist die Voraussetzung des gesamten Modells und wird beim
# Import geprueft — nicht behauptet.
_OVERLAP = GATES & ACTIVITIES
if _OVERLAP:
    raise AssertionError(
        "GATES und ACTIVITIES sind nicht disjunkt: %s. Das C16-Modell setzt "
        "Disjunktheit voraus." % sorted(_OVERLAP))

STATUS_VALUES = frozenset({"open", "resolved"})
RESOLUTION_VALUES = frozenset({"undecided", "decision-documented", "accepted"})

# Evidence-Status-Semantik (Nutzerentscheidung, projektweit):
#   not-planned : es existiert noch kein Messkonzept
#   planned     : Metrik, Berechnung und zustaendiges Gate sind definiert,
#                 Instrumentierung fehlt
#   pending     : Instrumentierung implementiert, Messdaten/Messfenster fehlen
#   verified    : Zielwert mit ausreichender, dokumentierter Evidenz geprueft
EVIDENCE_VALUES = frozenset({"not-required", "not-planned", "planned",
                             "pending", "verified", "failed", "blocked"})

EVIDENCE_SEMANTICS = {
    "not-planned": "es existiert noch kein Messkonzept",
    "planned": ("Metrik, Berechnung und zustaendiges Gate sind definiert, "
                "Instrumentierung fehlt"),
    "pending": ("Instrumentierung implementiert, aber Messdaten/Messfenster "
                "fehlen noch"),
    "verified": "Zielwert mit ausreichender, dokumentierter Evidenz geprueft",
    "not-required": "ausdruecklich kein Nachweis noetig",
    "failed": "Nachweis erbracht und nicht bestanden",
    "blocked": "Nachweis kann nicht gefuehrt werden",
}

# Die laufende Taetigkeit dieses Dokumentenlaufs.
CURRENT_ACTIVITY = "documentation"

# Spaltenkopf der Statusmodell-Tabellen (Registry §6.11.1, decision-log.md).
CONTRA_AXIS_COLUMNS = ["id", "status", "resolution_status", "evidence_status",
                       "blocking", "blocked_gates", "blocked_activities",
                       "evidence_gate", "decision_reference",
                       "evidence_reference"]

GATELESS = {"", "-", "—", "–", "n/a", "missing"}

# Sechs Ergebnisklassen. Ohne sie kollabieren "entschieden, Nachweis steht aus"
# und "gar nicht entschieden" auf denselben Fehlschlag.
OUTCOME_DECISION_OPEN = "1-designentscheidung-offen"
OUTCOME_EVIDENCE_PENDING = "2-entschieden-evidence-ausstehend"
OUTCOME_EVIDENCE_FAILED = "3-entschieden-evidence-fehlgeschlagen"
OUTCOME_COMPLETE = "4-vollstaendig"
OUTCOME_NOT_BLOCKING = "5-nicht-blockierend-fuers-aktuelle-gate"
OUTCOME_BLOCKING = "6-blockierend-fuers-aktuelle-gate"

FORMULA_TEXT = (
    "blocking = status NOT IN [resolved] "
    "OR resolution_status != accepted "
    "OR evidence_status IN [failed, blocked] "
    "OR current_gate IN blocked_gates "
    "OR current_activity IN blocked_activities"
)

# Die frueher im Bericht zitierte Fassung. Sie wird GEFUEHRT, damit die
# Angleichung nachpruefbar ist — und weil eine Pruefung sonst nicht feststellen
# kann, ob ein Dokument noch den Altwortlaut traegt.
FORMULA_TEXT_SUPERSEDED = "blocking = status == open"
FORMULA_DIVERGENCE_NOTE = (
    "`status == open` und `status != resolved` sind fuer die gueltigen Werte "
    "aequivalent und fuer einen FEHLENDEN status nicht: die Altfassung liefert "
    "false (blocking sinkt still ab), die kanonische Fassung true (fail-closed). "
    "Der Unterschied ist genau der NFR-Fall."
)

MODEL_PROVENANCE = {
    "module": "scratchpad/blocking_model.py",
    "single_implementation": True,
    "formula": FORMULA_TEXT,
    "gates": sorted(GATES),
    "activities": sorted(ACTIVITIES),
    "vocabularies_disjoint": True,
    "gate_vs_activity_comparison": "verboten und beim Ableiten unterbunden",
    "importers": ["validate_intake.py", "validate_trace.py", "check_prd.py",
                  "gen_intake.py", "selftest_validator.py"],
    "replaces": "blocking_scope (ersatzlos entfallen, C16)",
}


class VocabularyViolation(ValueError):
    """Ein Gate steht in blocked_activities oder eine Taetigkeit in
    blocked_gates. Das ist ein Datendefekt, kein auswertbarer Zustand."""


# ---------------------------------------------------------------------------
# Normalisierung
# ---------------------------------------------------------------------------

def clean(cell):
    """Entfernt Markdown-Auszeichnung; laesst den Sachwert unveraendert."""
    return re.sub(r"[`*~]", "", str(cell)).strip()


def parse_list_cell(cell):
    """`[A0]`, `[C, D]`, `[]`, `—`, `— (leer)`, "`A0`", "`C`, `D`"
    -> Liste von Rohwerten.

    Die beiden Statusmodell-Tabellen schreiben dieselbe Liste unterschiedlich
    (Registry mit Klammern, Ledger ohne). Das ist eine Schreibweise, kein
    Sachunterschied — deshalb hier normalisiert, NICHT im Vergleich verdeckt.
    """
    v = clean(cell)
    v = re.sub(r"\(\s*leer\s*\)", "", v, flags=re.I).strip()
    if v.lower() in GATELESS:
        return []
    if v.startswith("[") and v.endswith("]"):
        v = v[1:-1]
    return [x.strip() for x in v.split(",") if x.strip()]


def parse_bool_cell(cell):
    """Der Ledger schreibt `blocking` als Prosa ("**true** — `A0` ∈ …").
    Ein eindeutig fuehrendes true/false wird uebernommen; enthaelt die Zelle
    BEIDE Werte, ist sie nicht maschinell vergleichbar und liefert None.
    Das wird als Befund ausgewiesen, nicht auf einen Wert geraten.
    """
    v = clean(cell).lower()
    has_true = re.search(r"\btrue\b", v) is not None
    has_false = re.search(r"\bfalse\b", v) is not None
    if has_true and has_false:
        return None
    if has_true:
        return True
    if has_false:
        return False
    return None


def normalize_status_token(value):
    """Der Ledger schreibt "`resolved` (Entscheidung …) — Achsen …".
    Die Achse `status` ist das FUEHRENDE Token."""
    v = clean(value).lower()
    m = re.match(r"^(open|resolved)\b", v)
    if m:
        return m.group(1)
    return v.split("(")[0].split("—")[0].strip() or "MISSING"


# ---------------------------------------------------------------------------
# Vokabularpruefung — der C16-Kern
# ---------------------------------------------------------------------------

def check_vocabulary(entry):
    """Liefert eine Liste von Befunden. Leer = sauber.

    Geprueft wird beides:
      (a) jeder Wert liegt im JEWEILS eigenen Wertebereich, und
      (b) kein Wert liegt im Wertebereich des ANDEREN Feldes.
    (b) ist der eigentliche C16-Defekt: erst er macht einen
    Gate-vs-Taetigkeit-Vergleich ueberhaupt moeglich.
    """
    out = []
    for field, own, other, other_name in (
            ("blocked_gates", GATES, ACTIVITIES, "blocked_activities"),
            ("blocked_activities", ACTIVITIES, GATES, "blocked_gates")):
        for v in entry.get(field, []):
            if v in other:
                out.append({"id": entry.get("id"), "feld": field, "wert": v,
                            "problem": "Wert gehoert in das Vokabular von `%s` "
                                       "— Gate-vs-Taetigkeit-Vermischung (C16)"
                                       % other_name})
            elif v not in own:
                out.append({"id": entry.get("id"), "feld": field, "wert": v,
                            "problem": "Wert liegt ausserhalb des abschliessenden "
                                       "Wertebereichs von `%s`" % field})
    gate = clean(entry.get("evidence_gate", ""))
    if gate.lower() not in GATELESS and gate not in GATES:
        out.append({"id": entry.get("id"), "feld": "evidence_gate", "wert": gate,
                    "problem": "evidence_gate ist kein Gate-Bezeichner"})
    return out


# ---------------------------------------------------------------------------
# DIE kanonische Ableitung
# ---------------------------------------------------------------------------

def derive_blocking(entry, current_gate=None, current_activity=CURRENT_ACTIVITY,
                    strict=True):
    """Kanonische Blocking-Ableitung. EINZIGE Implementierung im Projekt.

    entry: dict mit status, resolution_status, evidence_status,
           blocked_gates (Liste), blocked_activities (Liste), evidence_gate.

    current_gate=None  -> Auswertung am EIGENEN `evidence_gate` des Eintrags
                          (die in Registry §6.11.1 verwendete Konvention).
                          Ein gateloser Eintrag (`—`) hat keine auswertbare
                          Gate-Klausel; sie ist dann schlicht False — sie wird
                          NICHT durch eine Taetigkeit ersetzt.
    current_activity   -> die gerade gepruefte Taetigkeit.

    Rueckgabe: (blocking: bool, reasons: list[str]).
    Jede ausgeloeste Klausel wird benannt, damit die Ableitung nachvollziehbar
    bleibt und nicht als blosse Behauptung dasteht.

    strict=True: bei Vokabularverstoessen wird VocabularyViolation geworfen,
    statt eine Vermischung stillschweigend auszuwerten.
    """
    viol = check_vocabulary(entry)
    if viol and strict:
        raise VocabularyViolation(
            "Vokabularverstoss, Ableitung verweigert: %s" % viol)

    status = clean(entry.get("status", "")).lower()
    resolution = clean(entry.get("resolution_status", "")).lower()
    evidence = clean(entry.get("evidence_status", "")).lower()
    gates = list(entry.get("blocked_gates", []))
    acts = list(entry.get("blocked_activities", []))
    own_gate = clean(entry.get("evidence_gate", ""))

    reasons = []

    # Klausel 1 — normativer Wortlaut, fail-closed.
    # NICHT `status == open`: das liefert fuer einen fehlenden Wert false und
    # laesst blocking still absinken (Nutzerentscheidung 2026-07-20, Punkt 6).
    if status not in ("resolved",):
        reasons.append("status NOT IN [resolved] (%s)" % (status or "MISSING"))
    # Klausel 2
    if resolution != "accepted":
        reasons.append("resolution_status != accepted (%s)" % (resolution or "MISSING"))
    # Klausel 3
    if evidence in ("failed", "blocked"):
        reasons.append("evidence_status IN [failed, blocked] (%s)" % evidence)

    # Klausel 4 — NUR gegen blocked_gates.
    gate = own_gate if current_gate is None else clean(current_gate)
    if gate.lower() in GATELESS:
        reasons_gate_note = ("kein auswertbares Gate (evidence_gate = '%s') — "
                             "Gate-Klausel liefert false und wird NICHT durch "
                             "eine Taetigkeit ersetzt" % (own_gate or "—"))
    else:
        reasons_gate_note = None
        if gate in gates:
            reasons.append("current_gate '%s' IN blocked_gates %s" % (gate, gates))

    # Klausel 5 — NUR gegen blocked_activities.
    act = clean(current_activity) if current_activity else ""
    if act and act in acts:
        reasons.append("current_activity '%s' IN blocked_activities %s" % (act, acts))

    if reasons_gate_note:
        reasons.append("(Hinweis: %s)" % reasons_gate_note)

    # Der Hinweis ist kein Grund. Nur echte Klauseln zaehlen.
    effective = [r for r in reasons if not r.startswith("(Hinweis:")]
    return bool(effective), reasons


def classify(entry, blocking):
    """Die sechs Ergebnisklassen, mechanisch getrennt."""
    status = clean(entry.get("status", "")).lower()
    resolution = clean(entry.get("resolution_status", "")).lower()
    evidence = clean(entry.get("evidence_status", "")).lower()
    if status != "resolved" or resolution != "accepted":
        return OUTCOME_DECISION_OPEN
    if evidence in ("failed", "blocked"):
        return OUTCOME_EVIDENCE_FAILED
    if evidence == "verified":
        return OUTCOME_COMPLETE
    if evidence == "not-required":
        return OUTCOME_BLOCKING if blocking else OUTCOME_COMPLETE
    if evidence in ("planned", "pending", "not-planned"):
        return OUTCOME_BLOCKING if blocking else OUTCOME_EVIDENCE_PENDING
    return OUTCOME_DECISION_OPEN


# ---------------------------------------------------------------------------
# EIN Parser fuer beide Statusmodell-Tabellen (Registry §6.11.1, decision-log)
# ---------------------------------------------------------------------------

def _header_cells(line):
    return [re.sub(r"[`*]", "", c).strip().lower()
            for c in line.strip().strip("|").split("|")]


def parse_axis_tables(text, prefixes=None):
    """Liest JEDE Statusmodell-Tabelle, unabhaengig vom ID-Praefix.

    BEFUND (Nutzerentscheidung 2026-07-20, Punkt 4): Der Achsenparser war auf
    `CONTRA-\\d{3}` festgenagelt. Damit wurden ausschliesslich die sechs
    CONTRA-Eintraege nachgerechnet; jedes `blocking` an einer anderen ID —
    zuletzt acht von vierzehn — stand ungeprueft im Dokument. Ein Feld, das
    niemand nachrechnet, ist keine Ableitung, sondern eine Behauptung.

    prefixes=None -> alle Praefixe. Sonst eine Menge zugelassener Praefixe.

    Rueckgabe: {id: achsen-dict}. Ein Eintrag OHNE `status`-Spalte erhaelt
    status="" — und faellt damit in der kanonischen Formel fail-closed auf
    blocking=true. Das ist beabsichtigt und der Grund fuer die Wortlaut-
    angleichung.
    """
    out = {}
    header = None
    prev = None
    id_re = re.compile(r"^([A-Z]+)-\d{3}$")
    for lineno, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if not s.startswith("|"):
            header = None
            prev = None
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and all(set(c) <= set("-: ") and c for c in cells):
            head = [re.sub(r"\s*\(.*\)$", "", c).strip() for c in (prev or [])]
            # Eine Achsentabelle erkennt man an ihren Achsen, nicht an ihrer
            # Spaltenzahl: `id` + `blocking` + mindestens eine weitere Achse.
            header = head if ("id" in head and "blocking" in head
                              and set(head) & {"status", "resolution_status",
                                               "evidence_status"}) else None
            prev = None
            continue
        prev = _header_cells(line)
        if not header:
            continue
        eid = clean(cells[0])
        m = id_re.match(eid)
        if not m:
            continue
        if prefixes is not None and m.group(1) not in prefixes:
            continue
        col = {name: cells[i] for i, name in enumerate(header) if i < len(cells)}
        out[eid] = {
            "id": eid,
            "prefix": m.group(1),
            "status": normalize_status_token(col.get("status", "")) if "status" in col else "",
            "resolution_status": clean(col.get("resolution_status", "")).lower(),
            "evidence_status": clean(col.get("evidence_status", "")).lower(),
            "blocking_recorded": parse_bool_cell(col.get("blocking", "")),
            "blocking_verbatim": clean(col.get("blocking", "")),
            "blocked_gates": parse_list_cell(col.get("blocked_gates", "")),
            "blocked_activities": parse_list_cell(col.get("blocked_activities", "")),
            "evidence_gate": clean(col.get("evidence_gate", "")),
            "decision_reference": clean(col.get("decision_reference", "")),
            "evidence_reference": clean(col.get("evidence_reference", "")),
            "header_order": header,
            "axes_present": sorted(set(header) & set(CONTRA_AXIS_COLUMNS)),
            "axes_missing": sorted(set(CONTRA_AXIS_COLUMNS) - set(header)),
            "lineno": lineno,
        }
    return out


def parse_contra_axes(text):
    """Liest die Statusmodell-Tabelle je CONTRA-ID — SPALTENNAMENBASIERT.

    BEFUND, der diese Fassung erzwungen hat: Registry §6.11.1 und
    docs/decisions/decision-log.md fuehren dieselben zehn Felder in
    UNTERSCHIEDLICHER Spaltenreihenfolge (Registry: … blocking, blocked_gates,
    blocked_activities, evidence_gate …; Ledger: … blocked_gates,
    blocked_activities, evidence_gate, blocking …). Ein positionsbasierter
    Parser las den Ledger deshalb gar nicht — die Vorfassung ergab dort 0
    Zeilen und liess C6c/C6d/C16 auf einer LEEREN Menge bestehen. Ein Pass auf
    der leeren Menge belegt nichts.

    Die Spaltenreihenfolge ist kein Sachunterschied; sie wird getrennt als
    Befund ausgewiesen (`header_order`), nicht stillschweigend geglaettet.
    """
    out = {}
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
            head = [re.sub(r"\s*\(.*\)$", "", c).strip() for c in (prev or [])]
            header = head if set(head) == set(CONTRA_AXIS_COLUMNS) else None
            prev = None
            continue
        prev = _header_cells(line)
        if not header:
            continue
        cid = clean(cells[0])
        if not re.match(r"^CONTRA-\d{3}$", cid):
            continue
        col = {name: cells[i] for i, name in enumerate(header) if i < len(cells)}
        out[cid] = {
            "id": cid,
            "status": clean(col.get("status", "")).lower(),
            "resolution_status": clean(col.get("resolution_status", "")).lower(),
            "evidence_status": clean(col.get("evidence_status", "")).lower(),
            "blocking_recorded": parse_bool_cell(col.get("blocking", "")),
            "blocking_verbatim": clean(col.get("blocking", "")),
            "blocked_gates": parse_list_cell(col.get("blocked_gates", "")),
            "blocked_activities": parse_list_cell(col.get("blocked_activities", "")),
            "evidence_gate": clean(col.get("evidence_gate", "")),
            "decision_reference": clean(col.get("decision_reference", "")),
            "evidence_reference": clean(col.get("evidence_reference", "")),
            "header_order": header,
            "lineno": lineno,
        }
    return out


# Eine Zeile, die den ABGESCHAFFTEN Vergleich als Vergangenheit, Fehler oder
# Gegenannahme beschreibt, IST nicht der Vergleich. Genau diese Unterscheidung
# fehlte in der ersten Fassung: sie schlug an den Saetzen an, die den Defekt
# dokumentieren — also an der Fehlerbeschreibung statt am Fehler.
# Die Ausnahme ist eng: der Marker muss in DERSELBEN Zeile stehen.
HISTORICAL_MARKERS = (
    "hätte", "haette", "wäre", "waere", "früher", "frueher", "vorher",
    "bisher", "alt-", "altfassung", "vorfassung", "entfallen", "ersetzt",
    "defekt", "gelautet", "historisch", "nicht mehr", "abgeschafft",
    "verboten", "unzulässig", "unzulaessig", "wörtliche lesart",
    "woertliche lesart",
)


def _is_historical(line):
    low = line.lower()
    return any(mk in low for mk in HISTORICAL_MARKERS)


def scan_gate_vs_activity_comparisons(text):
    """Findet Stellen, an denen ein Dokument ein Gate gegen eine
    Taetigkeitsliste (oder umgekehrt) vergleicht — die C16-Vermischung im
    FLIESSTEXT, nicht nur in der Tabelle.

    Gesucht wird `X ∈ [...]` / `X in [...]` und die Feldzuweisungen
    `blocked_gates = [...]` / `blocked_activities = [...]`.

    Zeilen, die den Vergleich ausdruecklich als abgeschafft, falsch oder
    kontrafaktisch beschreiben, sind KEIN Verstoss (siehe HISTORICAL_MARKERS).
    """
    findings = []
    for lineno, line in enumerate(text.split("\n"), 1):
        if _is_historical(line):
            continue
        for m in re.finditer(r"`?blocked_gates`?\s*(?:=|:)?\s*`?\[([^\]]*)\]", line):
            for v in [x.strip().strip("`") for x in m.group(1).split(",") if x.strip()]:
                if v in ACTIVITIES or v not in GATES:
                    findings.append({"line": lineno, "feld": "blocked_gates",
                                     "wert": v, "text": line.strip()[:160]})
        for m in re.finditer(r"`?blocked_activities`?\s*(?:=|:)?\s*`?\[([^\]]*)\]", line):
            for v in [x.strip().strip("`") for x in m.group(1).split(",") if x.strip()]:
                if v in GATES or v not in ACTIVITIES:
                    findings.append({"line": lineno, "feld": "blocked_activities",
                                     "wert": v, "text": line.strip()[:160]})
        # `A0 ∈ [field-test, release]` — Gate gegen Taetigkeiten
        for m in re.finditer(r"`?([A-Z][A-Za-z0-9]{0,2})`?\s*(?:∈|\bin\b)\s*`?\[([^\]]*)\]",
                             line):
            left, rhs = m.group(1), [x.strip().strip("`")
                                     for x in m.group(2).split(",") if x.strip()]
            if left in GATES and any(v in ACTIVITIES for v in rhs):
                findings.append({"line": lineno, "feld": "vergleich",
                                 "wert": "%s ∈ %s" % (left, rhs),
                                 "problem": "Gate gegen Taetigkeitsliste verglichen",
                                 "text": line.strip()[:160]})
    return findings
