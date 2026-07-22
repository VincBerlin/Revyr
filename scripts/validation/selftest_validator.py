#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Negativkontrolle fuer validate_intake.py.

Zweck: nachweisen, dass die Pruefungen ueberhaupt FEHLSCHLAGEN koennen.
Eine Pruefung, die auf jedem Eingabewert PASS liefert, belegt nichts.
Jeder Fall injiziert genau einen Defekt in eine Kopie der echten Artefakte
und erwartet, dass der zugehoerige Check auf FAIL springt.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
VALIDATOR = os.path.join(HERE, "validate_intake.py")
REPO = "/Users/vincentschnetzer/Documents/Run&Bike"

PRD = "docs/prd/revyr-endurance-platform.prd.md"
TRACE = "docs/traceability.md"
REG = "docs/ID-REGISTRY.md"
LOG = "docs/decisions/decision-log.md"
CANVAS = "docs/canvas/revyr-endurance-platform.canvas.md"


TOOLS = ("validate_intake.py", "gen_intake.py", "blocking_model.py",
         "selftest_validator.py", "registry_model.py", "validate_trace.py",
         "check_prd.py")


def stage():
    """Kopiert Artefakte UND Werkzeugdateien. Die Werkzeugkopie liegt in
    <tmp>/tools und wird dem Validator per --tools-dir uebergeben, damit die
    C14-Injektion die echten Skripte im Scratchpad nicht anfasst."""
    tmp = tempfile.mkdtemp(prefix="revyr-selftest-")
    shutil.copytree(os.path.join(REPO, "docs"), os.path.join(tmp, "docs"))
    for f in ("README.md", "intake-package.json"):
        src = os.path.join(REPO, f)
        if os.path.isfile(src):
            shutil.copy(src, os.path.join(tmp, f))
    os.makedirs(os.path.join(tmp, "tools"))
    for f in TOOLS:
        shutil.copy(os.path.join(HERE, f), os.path.join(tmp, "tools", f))
    return tmp


def patch_tool(tmp, name, old, new):
    p = os.path.join(tmp, "tools", name)
    t = open(p, encoding="utf-8").read()
    assert old in t, "Werkzeug-Anker nicht gefunden in %s: %r" % (name, old[:60])
    open(p, "w", encoding="utf-8").write(t.replace(old, new, 1))


def patch(tmp, rel, old, new, count=1):
    p = os.path.join(tmp, rel)
    t = open(p, encoding="utf-8").read()
    assert old in t, "Fixture-Anker nicht gefunden in %s: %r" % (rel, old[:60])
    open(p, "w", encoding="utf-8").write(t.replace(old, new, count))


def run(tmp):
    """Fuehrt den Validator aus und liefert je Check Status UND Befundzahl.

    Die Befundzahl ist noetig, weil einige Checks auf den ECHTEN Artefakten
    berechtigt FAIL sind (es gibt reale Defekte). Fuer sie ist "PASS -> FAIL"
    als Schaerfenachweis nicht verfuegbar; stattdessen muss die Injektion die
    Zahl der Befunde ERHOEHEN. Ohne diese zweite Messgroesse waeren genau die
    Checks ungeprueft, die gerade etwas finden.
    """
    out_json = os.path.join(tmp, "selftest-result.json")
    r = subprocess.run([sys.executable, VALIDATOR, "--repo", tmp,
                        "--tools-dir", os.path.join(tmp, "tools"),
                        "--json", out_json],
                       capture_output=True, text=True)
    checks = {}
    if os.path.isfile(out_json):
        for c in json.load(open(out_json, encoding="utf-8"))["checks"]:
            checks[c["id"]] = {"status": c["status"],
                               "n": len(c.get("findings") or [])}
    return {"text": r.stdout + r.stderr, "checks": checks}


def status_of(res, cid):
    return res["checks"].get(cid, {}).get("status", "ABSENT")


def findings_of(res, cid):
    return res["checks"].get(cid, {}).get("n", -1)


CASES = []


def case(name, cid, expect="FAIL"):
    """expect='FAIL': der injizierte Defekt MUSS den Check kippen.
    expect='PASS': Gegenprobe — die Injektion ist KEIN Defekt, der Check muss
    stehenbleiben (schuetzt vor einer Reparatur, die ins Gegenteil ueberschiesst).
    """
    def deco(fn):
        CASES.append((name, cid, fn, expect))
        return fn
    return deco


@case("C1: Pflichtfeld release_gate aus REQ-001 entfernt", "C1")
def c1(tmp):
    patch(tmp, PRD, "| release_gate | GATE-A0 |", "| release_gate |  |")


@case("C2: Feldwert durch unbegruendeten Bindestrich ersetzt", "C2")
def c2(tmp):
    patch(tmp, TRACE, "| Source Type | EXPLICIT |", "| Source Type | — |")


@case("C3a: Referenz auf nicht registrierte REQ-999", "C3a")
def c3a(tmp):
    patch(tmp, TRACE, "| Risiko | RISK-005 |",
          "| Risiko | RISK-005 |\n| Requirement | REQ-999 |")


@case("C3c: deprecatete CAN-005 in einer Verknuepfungsspalte", "C3c")
def c3c(tmp):
    patch(tmp, TRACE, "| Canvas Item (atomar) | CAN-047, CAN-028, CAN-013 |",
          "| Canvas Item (atomar) | CAN-005 |")


@case("C3a: nicht registrierte REQ-999 in deutscher Kompositumform", "C3a")
def c3a_compound(tmp):
    # Negativkontrolle GENAU fuer den real eingetretenen Fehlermodus:
    # der fruehere Lookahead `(?![0-9-])` verwarf jede ID, auf die ein Bindestrich
    # folgt. Eine ECHTE Referenz in Kompositumform war damit unsichtbar — nicht
    # geprueft, sondern nicht gesehen. Die uebrigen Faelle injizieren nur
    # freistehende IDs und konnten diesen Fehler nicht aufdecken.
    patch(tmp, TRACE, "| Risiko | RISK-005 |",
          "| Risiko | RISK-005 |\n| Requirement | REQ-999-Nachfolgeklausel |")


@case("C3c: deprecatete CAN-005 in Kompositumform in einer Verknuepfungsspalte", "C3c")
def c3c_compound(tmp):
    # Zweite Haelfte desselben Fehlermodus: die ID steht in einer
    # Verknuepfungsspalte, aber als Wortbestandteil. Der alte Tokenizer fand sie
    # nicht; classify_occurrence() haette sie zusaetzlich auf "context"
    # heruntergestuft, selbst wenn der Tokenizer sie gefunden haette.
    patch(tmp, TRACE, "| Canvas Item (atomar) | CAN-047, CAN-028, CAN-013 |",
          "| Canvas Item (atomar) | CAN-005-Nachfolgeklausel |")


@case("Facette CAN-009-a bleibt Facette und wird NICHT zum Verstoss", "C3c",
      expect="PASS")
def c3c_facet_stays_clean(tmp):
    # Gegenprobe zur Reparatur: der Fix darf nicht ins andere Extrem kippen.
    # Eine Facetten-Kennung in einer Verknuepfungsspalte nennt die deprecatete
    # Basis-ID NICHT und darf C3c deshalb nicht kippen.
    patch(tmp, TRACE, "| Canvas Item (atomar) | CAN-049, CAN-101, CAN-108, CAN-028 |",
          "| Canvas Item (atomar) | CAN-009-a |")


@case("C3d: reservierte CAN-016 als erfuellter Anker", "C3d")
def c3d(tmp):
    patch(tmp, TRACE, "| Canvas Item (atomar) | CAN-048, CAN-028, CAN-013, CAN-100 |",
          "| Canvas Item (atomar) | CAN-016 |")


@case("C4: REQ-001 ein zweites Mal aktiv in anderer canonical_file", "C4")
def c4(tmp):
    p = os.path.join(tmp, REG)
    t = open(p, encoding="utf-8").read()
    t = t.replace(
        "| REQ-002 | requirement |",
        "| REQ-001 | requirement | Doppelbelegung | `docs/vision/revyr-endurance-platform.vision.md` "
        "| active | 2026-07-18 | — | — | injizierter Defekt |\n| REQ-002 | requirement |", 1)
    open(p, "w", encoding="utf-8").write(t)


@case("C5b: Traceability-Zeile fuer REQ-036 geloescht", "C5b")
def c5b(tmp):
    p = os.path.join(tmp, TRACE)
    lines = open(p, encoding="utf-8").read().split("\n")
    out = [l for l in lines if not l.startswith("| TRC-036 | REQ-036")]
    open(p, "w", encoding="utf-8").write("\n".join(out))


@case("C5e: AC/EV-Kopplung in TRC-003 verdreht", "C5e")
def c5e(tmp):
    patch(tmp, TRACE, "| AC-003 | EV-003 |", "| AC-004 | EV-004 |")


@case("C6a: Ledger-Zeile fuer CONTRA-006 geloescht", "C6a")
def c6a(tmp):
    p = os.path.join(tmp, LOG)
    lines = open(p, encoding="utf-8").read().split("\n")
    out = [l for l in lines if not l.strip().startswith("| CONTRA-006 |")]
    open(p, "w", encoding="utf-8").write("\n".join(out))


# ---------------------------------------------------------------------------
# Negativkontrollen fuer die in diesem Lauf ergaenzten Pruefungen.
# Eine Pruefung ohne injizierten Defekt ist nicht nachweislich scharf.
# ---------------------------------------------------------------------------

@case("C6b: Registry-`status` von CONTRA-004 auf `open` zurueckgedreht", "C6b")
def c6b_status_divergence(tmp):
    # Genau der Zustand, der C6b vor dem Auftauen der Registry auf FAIL hielt:
    # Registry `open`, Ledger `resolved`. Die Achse `status` divergiert.
    patch(tmp, REG,
          "| CONTRA-004 | contradiction |", "| CONTRA-004 | contradiction |")
    p = os.path.join(tmp, REG)
    t = open(p, encoding="utf-8").read()
    i = t.index("| CONTRA-004 | contradiction |")
    j = t.index("\n", i)
    row = t[i:j].replace("| resolved | 2026-07-19 |", "| open | 2026-07-19 |", 1)
    open(p, "w", encoding="utf-8").write(t[:i] + row + t[j:])


@case("C6b: CONTRA-006 mit `evidence_status = pending` kippt C6b NICHT", "C6b",
      expect="PASS")
def c6b_evidence_is_not_divergence(tmp):
    # Gegenprobe zur kanonischen Definition: die Evidence-Achse darf keine
    # Statusdivergenz erzeugen. Genau hier kamen zwei Pruefer auf 2 vs. 3.
    patch(tmp, LOG,
          "| CONTRA-006 | resolved | accepted | pending |",
          "| CONTRA-006 | resolved | accepted | planned |")


@case("C6c: evidence_status von CONTRA-005 im Ledger abweichend gesetzt", "C6c")
def c6c(tmp):
    patch(tmp, LOG,
          "| CONTRA-005 | resolved | accepted | pending |",
          "| CONTRA-005 | resolved | accepted | planned |")


@case("C6d: blocking von CONTRA-001 auf `true` gesetzt, ohne dass eine "
      "Klausel greift", "C6d")
def c6d(tmp):
    # Eingetragener Wert weicht von der Ableitung ab -> die Ableitung muss
    # widersprechen, nicht den Tabellenwert uebernehmen.
    patch(tmp, REG,
          "| CONTRA-001 | resolved | accepted | not-required | **false** | `[]` | `[]` |",
          "| CONTRA-001 | resolved | accepted | not-required | **true** | `[]` | `[]` |")


@case("C6d: evidence_status `failed` erzwingt blocking=true", "C6d")
def c6d_failed(tmp):
    # Ergebnisklasse (3) entschieden/Evidence fehlgeschlagen. Der eingetragene
    # blocking-Wert `false` muss dadurch falsch werden.
    patch(tmp, REG,
          "| CONTRA-001 | resolved | accepted | not-required | **false** | `[]` | `[]` |",
          "| CONTRA-001 | resolved | accepted | failed | **false** | `[]` | `[]` |")


@case("C6d: Gate aus blocked_gates entfernt -> blocking muss auf false fallen",
      "C6d")
def c6d_gate_removed(tmp):
    # Beweist, dass die Gate-Klausel WIRKT und nicht bloss mitgeschrieben wird.
    # Ohne `A0` in blocked_gates greift keine Klausel mehr; der eingetragene
    # Wert **true** wird dadurch falsch.
    patch(tmp, REG,
          "| CONTRA-006 | resolved | accepted | pending | **true** | `[A0]` |",
          "| CONTRA-006 | resolved | accepted | pending | **true** | `[]` |")


@case("C6e: unzulaessiger Mischwert DESIGN-RESOLVED im `status` von CONTRA-006",
      "C6e")
def c6e(tmp):
    patch(tmp, REG,
          "| CONTRA-006 | resolved | accepted | pending |",
          "| CONTRA-006 | DESIGN-RESOLVED | accepted | pending |")


@case("C9: Feld `owner` aus dem NFR-004-Block entfernt", "C9")
def c9(tmp):
    patch(tmp, PRD,
          "| `owner` | **MISSING — OWNER-BLOCKER** (OQ-002). Zusätzlich blockierend "
          "für die Messung: OQ-003",
          "| `owner` |  | (OQ-002). Zusätzlich blockierend "
          "für die Messung: OQ-003")


@case("C9: `evidence_status` aus dem NFR-001-Block geleert", "C9")
def c9_evidence(tmp):
    # BEFUND/FIX an der Kontrolle selbst: Der Fall zielte auf NFR-008, das
    # C9 ohnehin schon meldet. Die Injektion erzeugte deshalb KEINEN neuen
    # Befund und die Kontrolle war stumpf — sie belegte nichts. Jetzt trifft
    # sie ein NFR, das aktuell sauber ist; damit muss ein Befund HINZUKOMMEN.
    patch(tmp, PRD,
          "| `evidence_status` | **`pending`** — kein Code, kein Build, keine Messung.",
          "| `evidence_status` |  |")


@case("C10: NFR-001 auf EXPLICIT hochgestuft, Quelle bleibt 'KEINE GEFUNDEN'", "C10")
def c10(tmp):
    patch(tmp, PRD,
          "| `source_type` | **ASSUMPTION** (vorher EXPLICIT) — festgelegt durch "
          "Nutzerentscheidung 2026-07-19 |",
          "| `source_type` | **EXPLICIT** |")


@case("C11: `source_type` von NFR-003 traegt einen evidence_status-Wert", "C11")
def c11(tmp):
    # NFR-003 und NFR-005 tragen beide woertlich '**ASSUMPTION** (vorher
    # EXPLICIT)'; count=1 trifft das erste Vorkommen (NFR-003).
    patch(tmp, PRD,
          "| `source_type` | **ASSUMPTION** (vorher EXPLICIT) |",
          "| `source_type` | **pending** |")


@case("C11: `evidence_status` von NFR-001 traegt einen Herkunftswert", "C11")
def c11_reverse(tmp):
    patch(tmp, PRD,
          "| `evidence_status` | **`pending`** — kein Code, kein Build, keine Messung.",
          "| `evidence_status` | **ASSUMPTION** — kein Code, kein Build, keine Messung.")


@case("C12: EXPLICIT allein aus einer qualitativen VIS-Absicht abgeleitet", "C12")
def c12(tmp):
    # Genau die verbotene automatische Vererbung: VIS-003 ist eine qualitative
    # Absicht ("verlaessliches Tracking") und macht 3 % nicht EXPLICIT.
    patch(tmp, PRD,
          "| `source_type` | **ASSUMPTION** (vorher EXPLICIT) — festgelegt durch "
          "Nutzerentscheidung 2026-07-19 |",
          "| `source_type` | **EXPLICIT** — abgeleitet aus VIS-003 |")


@case("C14: hartkodierter Blocking-Sonderfall wieder in gen_intake.py eingesetzt",
      "C14")
def c14(tmp):
    # Woertlich der Defekt aus der Vorfassung. Injiziert wird in die STAGED
    # KOPIE unter <tmp>/tools; die echten Skripte im Scratchpad bleiben
    # unangetastet.
    patch_tool(tmp, "gen_intake.py",
               'item["blocking"] = derived',
               'item["blocking"] = e["id"] == "CONTRA-006"')


@case("C15: REQ-037 an den dokumentiert falschen Anker VIS-009 gehaengt", "C15")
def c15(tmp):
    # Zweiteilig, weil C15 die Fehlanker-Paare aus den ARTEFAKTEN liest:
    # (1) das Paar REQ-037 -> VIS-009 wird als fachlich falsch dokumentiert,
    # (2) genau dieser Anker wird trotzdem aktiv gesetzt. Ohne (1) gaebe es
    # nichts zu beanstanden — die erste Fassung dieser Kontrolle war deshalb
    # stumpf und belegte nichts.
    patch(tmp, PRD,
          "Canvas: **CAN-099** (kanonischer Accessibility-Anker) · "
          "NFR: **NFR-005** · Vision: **VIS-011** (Accessibility Boundary)",
          "REQ-037 hing an VIS-009 — fachlich falsch.\n\n"
          "Canvas: **CAN-099** (kanonischer Accessibility-Anker) · "
          "NFR: **NFR-005** · Vision: **VIS-009** (Privacy Boundary)")


@case("C15: korrekter Anker VIS-011 kippt C15 NICHT", "C15", expect="PASS")
def c15_counterproof(tmp):
    # Gegenprobe: der Check darf nicht jeden Anker beanstanden, nur den in den
    # Artefakten als falsch AUSGEWIESENEN. Ohne diese Probe waere ein Check,
    # der immer FAIL liefert, von einem scharfen nicht zu unterscheiden.
    patch(tmp, TRACE,
          "| **TRC-037** | **REQ-037 — Accessibility**",
          "| **TRC-037** | **REQ-037 — Accessibility**")




# ---------------------------------------------------------------------------
# Negativkontrollen fuer die in DIESEM Lauf ergaenzten Pruefungen (C16..C27).
# Eine Pruefung ohne injizierten Defekt ist nicht nachweislich scharf.
# ---------------------------------------------------------------------------

@case("C16: Taetigkeitsbezeichner in `blocked_gates` eingesetzt "
      "(Gate-vs-Taetigkeit-Vermischung)", "C16")
def c16_activity_in_gates(tmp):
    # Genau der Defekt, den C16 verhindern soll: ein Wert aus dem
    # Taetigkeitsvokabular steht im Gate-Feld.
    patch(tmp, REG,
          "| CONTRA-005 | resolved | accepted | pending | **true** | `[B]` |",
          "| CONTRA-005 | resolved | accepted | pending | **true** | `[release]` |")


@case("C16: Gate-Bezeichner in `blocked_activities` eingesetzt", "C16")
def c16_gate_in_activities(tmp):
    patch(tmp, REG,
          "| `[database-schema-finalization, account-release]` |",
          "| `[A0, account-release]` |")


@case("C16: kontrafaktische Beschreibung des Alt-Defekts kippt C16 NICHT",
      "C16", expect="PASS")
def c16_description_is_not_defect(tmp):
    # Gegenprobe. Die Registry BESCHREIBT den abgeschafften Vergleich
    # ("haette ... gelautet: ist A0 in [implementation, release]?"). Eine
    # Fehlerbeschreibung ist nicht der Fehler — sonst waere die Dokumentation
    # des Defekts selbst ein Verstoss und nicht mehr schreibbar.
    patch(tmp, REG,
          "#### 6.11.1 Statusmodell je CONTRA-ID (Felder nach §3.1)",
          "Frueher haette die Klausel gelautet: ist `A0` in "
          "`[field-test, release]`? Das ist entfallen.\n\n"
          "#### 6.11.1 Statusmodell je CONTRA-ID (Felder nach §3.1)")


@case("C17: CAN-130 traegt an einer Stelle `evidence_status verified`", "C17")
def c17(tmp):
    # `planned` -> `verified` waere die Behauptung eines erbrachten Nachweises.
    # BEFUND an der Kontrolle selbst: die erste Fundstelle dieses Textes in
    # traceability.md steht auf einer Zeile OHNE CAN-130 — die Injektion lag
    # ausserhalb des Pruefgegenstands und belegte nichts. Jetzt wird gezielt
    # die CAN-130-Zeile getroffen.
    patch(tmp, TRACE,
          "`source_type` **EXPLICIT**, `evidence_status` **planned**",
          "`source_type` **EXPLICIT**, `evidence_status` **verified**")


@case("C17: zweiter, abweichender CAN-130-Statuswert im Ledger", "C17")
def c17_conflict(tmp):
    p = os.path.join(tmp, "docs/EVIDENCE-LEDGER.md")
    t = open(p, encoding="utf-8").read()
    open(p, "w", encoding="utf-8").write(
        t + "\n\nCAN-130: `evidence_status` **pending**.\n")


@case("C18: Designsystem-Satz in die AUSSAGE von CAN-099 eingemischt", "C18")
def c18(tmp):
    patch(tmp, CANVAS,
          "Farbe niemals der einzige Informationsträger ist. |",
          "Farbe niemals der einzige Informationsträger ist. Die Anwendung "
          "verwendet ein tokenbasiertes, monochromes Designsystem. |")


@case("C18: die ABGRENZUNG in der Anmerkungsspalte kippt C18 NICHT", "C18",
      expect="PASS")
def c18_note_is_not_content(tmp):
    # Gegenprobe: Die Anmerkung sagt "der Designsystem-Anteil ist nach CAN-141
    # ausgelagert". Wer sie als Inhalt liest, beanstandet die Abgrenzung selbst.
    patch(tmp, CANVAS,
          "**CAN-099 ist AUSSCHLIESSLICH Accessibility**",
          "**CAN-099 ist AUSSCHLIESSLICH Accessibility** "
          "(monochromes Designsystem: siehe CAN-141)")


@case("C19: eigenes Designsystem-Item CAN-141 aus dem Canvas entfernt", "C19")
def c19(tmp):
    p = os.path.join(tmp, CANVAS)
    lines = open(p, encoding="utf-8").read().split("\n")
    out = [l for l in lines
           if not (l.strip().startswith("| CAN-141 |")
                   and "monochrom" in l.lower())]
    open(p, "w", encoding="utf-8").write("\n".join(out))


@case("C20: Designsystem-Requirement traegt zusaetzlich Accessibility im Titel",
      "C20")
def c20(tmp):
    patch(tmp, PRD,
          "### REQ-038 — Monochromes tokenbasiertes Designsystem",
          "### REQ-038 — Monochromes tokenbasiertes Designsystem und Accessibility")


@case("C21: GPX-Requirement in eine Teilklausel zurueckgebaut "
      "(kein eigener Titel mehr)", "C21")
def c21(tmp):
    patch(tmp, PRD,
          "### REQ-039 — GPX-Export abgeschlossener Aktivitäten",
          "### REQ-039 — Export abgeschlossener Aktivitäten")


@case("C22: `sekundär` vor REQ-034 in der Ankerzeile entfernt", "C22")
def c22(tmp):
    patch(tmp, PRD,
          "· sekundär: **REQ-034**",
          "· **REQ-034**")


@case("C22: der Satz 'REQ-034 ist sekundär, nicht primär' kippt C22 NICHT",
      "C22", expect="PASS")
def c22_negation(tmp):
    # Gegenprobe fuer den real eingetretenen Fehlalarm: die Vorfassung suchte
    # `primär … REQ-034` ohne die Verneinung zu lesen und schlug ausgerechnet
    # an dem Satz an, der das Gegenteil sagt.
    patch(tmp, PRD,
          "**REQ-034 ist sekundär, nicht primär**",
          "**REQ-034 ist sekundär, nicht primär** — und ausdrücklich nicht "
          "primärer Anker.")


@case("C23: Komfortaspekt in die AUSSAGE von CAN-022 eingemischt", "C23")
def c23(tmp):
    patch(tmp, CANVAS,
          "weniger vollständig und weniger zuverlässig. |",
          "weniger vollständig und weniger zuverlässig. Außerdem müssen Nutzer "
          "zusätzlich das Telefon mitführen. |")


@case("C23: der Ausschluss in der Anmerkungsspalte kippt C23 NICHT", "C23",
      expect="PASS")
def c23_exclusion_is_not_content(tmp):
    # Gegenprobe: Die Anmerkung benennt den Komfortaspekt, um ihn
    # AUSZUSCHLIESSEN. Das ist die Abgrenzung, nicht die Vermischung.
    patch(tmp, CANVAS,
          "**Ausdrücklich NICHT enthalten:**",
          "**Ausdrücklich NICHT enthalten (Komfort, Telefon mitführen):**")


@case("C24: die neue Persona in der Registry auf `reserved` zurueckgesetzt",
      "C24")
def c24(tmp):
    p = os.path.join(tmp, REG)
    t = open(p, encoding="utf-8").read()
    i = t.index("| USER-004 | persona |")
    j = t.index("\n", i)
    row = t[i:j].replace("| active | 2026-07-19 |", "| reserved | 2026-07-19 |", 1)
    open(p, "w", encoding="utf-8").write(t[:i] + row + t[j:])


@case("C25: Persona-Verknuepfung aus dem REQ-032-Block entfernt", "C25")
def c25(tmp):
    patch(tmp, PRD,
          "Canvas: **CAN-022** (Problem), CAN-069, CAN-052, CAN-137 · "
          "Vision: **MISSING** · Persona: **USER-004** (primär)",
          "Canvas: **CAN-022** (Problem), CAN-069, CAN-052, CAN-137 · "
          "Vision: **MISSING**")


@case("C25: CAN-022-Bezug aus dem REQ-032-Block entfernt", "C25")
def c25_canvas(tmp):
    patch(tmp, PRD,
          "Canvas: **CAN-022** (Problem), CAN-069, CAN-052, CAN-137",
          "Canvas: CAN-069, CAN-052, CAN-137")


@case("C26: Requirement-Gesamtzahl als Literal ins Werkzeug zurueckgeschrieben",
      "C26")
def c26(tmp):
    # Woertlich der Defekt aus der Vorfassung: eine Gesamtzahl als Literal im
    # Vergleich. Die Zahl wird AUS DER REGISTRY geholt, nicht abgetippt —
    # sonst traege diese Negativkontrolle selbst genau das Literal, dessen
    # Abwesenheit sie nachweisen soll.
    sys.path.insert(0, HERE)
    import registry_model as RM
    n = RM.load(REPO).count("REQ")
    patch_tool(tmp, "validate_intake.py",
               "n_active > 0 and complete == n_active and not findings",
               "n_active > 0 and complete == %d and not findings" % n)


@case("C27: aktiver Anker auf eine deprecatete CAN-ID in einer "
      "Verknuepfungsspalte", "C27")
def c27(tmp):
    # Nackte deprecatete CAN-005 in der Vision-/Canvas-Verknuepfungsspalte der
    # TRC-040-Zeile — ohne Klammer, ohne Provenienzmarker. Sie darf von der
    # Provenienzregel NICHT entschuldigt werden.
    patch(tmp, TRACE, "**VIS-003** — ungeprüfte ASSUMPTION",
          "**VIS-003**, CAN-005 — ungeprüfte ASSUMPTION")


@case("C3c: Provenienzangabe in Klammern kippt C3c NICHT", "C3c", expect="PASS")
def c3c_provenance_stays_clean(tmp):
    # Gegenprobe zur Provenienzregel: `*(Nachfolger 1/2 von REQ-014)*` in einer
    # Verknuepfungsspalte ist Herkunft, kein Anker. Ohne diese Probe waere die
    # Regel nicht von einem Freibrief zu unterscheiden.
    patch(tmp, TRACE,
          "**REQ-042 — Vergleich fachlich vergleichbarer Aktivitäten** "
          "*(neu 2026-07-20, Nachfolger 2/2 von REQ-040)*",
          "**REQ-042 — Vergleich fachlich vergleichbarer Aktivitäten** "
          "*(neu 2026-07-20, Nachfolger 2/2 von REQ-040, ersetzt zugleich eine "
          "Teilklausel von REQ-014)*")


@case("C5d: EV-042 der Widerspruchsbezug entzogen", "C5d")
def c5d_contra_ev(tmp):
    # Gegenprobe zur Ausnahme fuer widerspruchsgebundene Nachweise: ohne
    # CONTRA-Bezug ist EV-042 tatsaechlich bezugslos und muss auffallen.
    p = os.path.join(tmp, REG)
    t = open(p, encoding="utf-8").read()
    i = t.index("| EV-042 | evidence |")
    j = t.index("\n", i)
    open(p, "w", encoding="utf-8").write(
        t[:i] + t[i:j].replace("CONTRA-005", "der Widerspruch") + t[j:])



@case("C9: evidence_status aus dem NFR-008-DEFINITIONSabschnitt entfernt", "C9")
def c9_definition_block(tmp):
    # Kontrolle zur Blockgrenzen-Reparatur: der kanonische Abschnitt ist der
    # ERSTE `### NFR-008 —`. Wird dort ein Pflichtfeld entfernt, MUSS C9
    # kippen. Die Vorfassung las statt dessen den letzten Abschnitt und haette
    # diesen Eingriff nicht bemerkt.
    p = os.path.join(tmp, PRD)
    t = open(p, encoding="utf-8").read()
    i = t.index("### NFR-008 — Wartbarkeit")
    j = t.index("| `evidence_status` |", i)
    k = t.index("\n", j)
    open(p, "w", encoding="utf-8").write(t[:j] + "| `evidence_status` |  |" + t[k:])


@case("C9: Feld/Wert-Tabelle NACH dem NFR-Abschnitt faellt nicht mehr hinein "
      "(Gegenprobe zur Blockgrenze)", "C9", expect="PASS")
def c9_boundary_does_not_leak(tmp):
    # Gegenprobe: eine fremde Tabelle hinter einer eigenen Ueberschrift darf
    # NICHT als NFR-Feld gelesen werden. Genau so kam NFR-008 zu einem
    # source_type, der in seinem Abschnitt nie stand.
    p = os.path.join(tmp, PRD)
    t = open(p, encoding="utf-8").read()
    i = t.index("### NFR-008 — Runde 4")
    j = t.index("\n\n", i)
    open(p, "w", encoding="utf-8").write(
        t[:j] + "\n\n### Fremder Abschnitt\n\n| Feld | Wert |\n|---|---|\n"
        "| source_type | VOELLIG FALSCHER WERT |\n" + t[j:])


# ===========================================================================
# ZWEITE HARNISCH-EBENE: validate_trace.py und check_prd.py
#
# Bis zu diesem Lauf pruefte die Negativkontrolle AUSSCHLIESSLICH
# validate_intake.py. Die beiden anderen Validatoren hatten keine einzige
# Schaerfenprobe — und genau in ihnen sassen der Scratchpad-Cache, das
# Zahlliteral und die Feldnamen-statt-Feldwert-Pruefung. Ein Werkzeug ohne
# Negativkontrolle ist ein Werkzeug, dessen PASS nichts bedeutet.
# ===========================================================================

TRACE_CASES = []
PRD_CASES = []


def run_tool(tool, tmp):
    """Fuehrt validate_trace.py oder check_prd.py gegen eine Kopie aus.
    Liefert (returncode, ausgabe)."""
    r = subprocess.run([sys.executable, os.path.join(tmp, "tools", tool), tmp],
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def tool_case(tool, name, needle, expect="FAIL"):
    """needle: Textbaustein, der in der Ausgabe erscheinen MUSS, damit der
    Nachweis der richtige ist. Ein blosser Rueckgabewert != 0 belegt nicht,
    dass die GEMEINTE Pruefung angeschlagen hat — er koennte von einer
    beliebigen anderen stammen. Genau diese Verwechslung soll die
    Negativkontrolle ausschliessen."""
    def deco(fn):
        (TRACE_CASES if tool == "validate_trace.py" else PRD_CASES).append(
            (name, needle, fn, expect, tool))
        return fn
    return deco


# --- validate_trace.py -----------------------------------------------------

@tool_case("validate_trace.py",
           "Registry wird zur LAUFZEIT gelesen: neue REQ-ID in der Registry "
           "muss sofort als fehlende Kernmatrix-Zeile auffallen",
           "keine Zeile fuer REQ-")
def t_runtime_registry(tmp):
    # Der Beweis gegen den Cache-Defekt: die Registry wird waehrend des Laufs
    # geaendert. Ein Werkzeug, das derived.json liest, bemerkt davon NICHTS
    # und meldet weiter PASS. Genau so entstand der Fehlalarm gegen REQ-041.
    p = os.path.join(tmp, REG)
    t = open(p, encoding="utf-8").read()
    i = t.index("| REQ-042 |")
    j = t.index("\n", i)
    row = t[i:j].replace("REQ-042", "REQ-043", 1)
    open(p, "w", encoding="utf-8").write(t[:j] + "\n" + row + t[j:])


@tool_case("validate_trace.py",
           "Zahlliteral als STRING ins Werkzeug zurueckgeschrieben",
           "Zahlliteral im Validator")
def t_count_literal_string(tmp):
    # Die Vorfassung sah nur NUMBER-Token und war fuer genau diesen Fall blind.
    # Der Wert wird NICHT abgetippt, sondern aus der Registry geholt — sonst
    # traege diese Kontrolle selbst das verbotene Literal.
    sys.path.insert(0, HERE)
    import registry_model as RM
    n = str(RM.load(REPO).count("REQ"))
    patch_tool(tmp, "validate_trace.py",
               'GATES = BM.GATES',
               'ERWARTETE_ANZAHL = "%s"\nGATES = BM.GATES' % n)


@tool_case("validate_trace.py",
           "Slice-Breite bleibt erlaubt (Gegenprobe zur Ausnahme)",
           "FAILS: 0", expect="PASS")
def t_slice_is_not_a_count(tmp):
    # Gegenprobe: die Ausnahme fuer Slice-Positionen darf nicht ins Gegenteil
    # umschlagen und JEDE Zahl entschuldigen — hier muss sie GREIFEN.
    sys.path.insert(0, HERE)
    import registry_model as RM
    n = str(RM.load(REPO).count("REQ"))
    patch_tool(tmp, "validate_trace.py",
               "    print(\"Registry gelesen: %s\" % reg.path)",
               "    _probe = str(reg.path)[:%s]\n"
               "    print(\"Registry gelesen: %%s\" %% reg.path)" % n)


@tool_case("validate_trace.py",
           "true-line-Invariante in der §5-Tabelle verletzt",
           "true-line-status")
def t_true_line(tmp):
    patch(tmp, TRACE,
          "| REQ-001 | docs/vision/revyr-endurance-platform.vision.md#VIS-008 "
          "| VC-001 (Inhalt MISSING) | pending-watcher |",
          "| REQ-001 | docs/vision/revyr-endurance-platform.vision.md#VIS-008 "
          "| VC-001 (Inhalt MISSING) | verified |")


@tool_case("validate_trace.py",
           "§5-Pruefung greift NICHT auf fremde Tabellen ueber (Gegenprobe zur "
           "Kopfzeilenbindung)", "FAILS: 0", expect="PASS")
def t_header_binding(tmp):
    # In §4 wird eine weitere Zeile der Form "REQ-xxx | **MISSING …" ergaenzt.
    # Die formbasierte Vorfassung haette sie als §5-Zeile gelesen und drei
    # true-line-Verstoesse gemeldet. Die kopfzeilengebundene Fassung nicht.
    patch(tmp, TRACE,
          "| REQ-039 | **MISSING — BLOCKER (2026-07-20).** CAN-013 **entfernt**.",
          "| REQ-039 | **MISSING — Zusatzzeile ohne §5-Kopfzeile.** |\n"
          "| REQ-039 | **MISSING — BLOCKER (2026-07-20).** CAN-013 **entfernt**.")


@tool_case("validate_trace.py",
           "aufgehobener Blocking-Formelwortlaut als geltende Regel eingefuegt",
           "aufgehobenen Formelwortlaut")
def t_old_formula(tmp):
    patch(tmp, TRACE, "\n## ", "\n\nEs gilt: blocking = status == open.\n\n## ", 1)


# --- check_prd.py ----------------------------------------------------------

@tool_case("check_prd.py",
           "Messfeld GELEERT — Feldname bleibt stehen (der Defekt, den die "
           "Vorfassung nicht sehen konnte)", "Wert leer/Nullwert")
def p_empty_field_value(tmp):
    # DIE zentrale Kontrolle fuer Aufgabe 1: die Vorfassung prueft `feld in
    # body` und haette diesen Eingriff bestanden — der Feldname steht ja noch
    # da. Nur eine WERT-Pruefung faellt hier um.
    p = os.path.join(tmp, PRD)
    t = open(p, encoding="utf-8").read()
    i = t.index("### REQ-001 —")
    j = t.index("| signal |", i)
    k = t.index("\n", j)
    open(p, "w", encoding="utf-8").write(t[:j] + "| signal | — |" + t[k:])


@tool_case("check_prd.py",
           "Achsenfeld traegt einen Wert ausserhalb seines Vokabulars",
           "kein Wert aus")
def p_bad_vocab(tmp):
    p = os.path.join(tmp, PRD)
    t = open(p, encoding="utf-8").read()
    i = t.index("### REQ-001 —")
    j = t.index("| release_gate |", i)
    k = t.index("\n", j)
    open(p, "w", encoding="utf-8").write(
        t[:j] + "| release_gate | demnaechst |" + t[k:])


@tool_case("check_prd.py",
           "Bestandstabelle nennt eine Zahl, die die Registry nicht hergibt",
           "Bestandstabelle stimmt zellenweise")
def p_inventory_mismatch(tmp):
    patch(tmp, PRD, "| NFR | **8** | 0 | 0 | 0 |", "| NFR | **9** | 0 | 0 | 0 |")


@tool_case("check_prd.py",
           "deprecatete ID als aktiver Anker in einer Ankerspalte",
           "steht im PRD an keiner Ankerstelle")
def p_dead_anchor(tmp):
    patch(tmp, PRD, "| AC-025 | REQ-025 |", "| AC-025 | REQ-014 |")


@tool_case("check_prd.py",
           "Migrations- und Bestandszeilen kippen die Ankerpruefung NICHT "
           "(Gegenprobe zur Spaltenbindung)", "FAILURES: 0", expect="PASS")
def p_provenance_stays_clean(tmp):
    # Die markerbasierte Vorfassung meldete genau solche Zeilen als Verstoss.
    sys.path.insert(0, HERE)
    import registry_model as RM
    reg = RM.load(REPO)
    row = "| REQ | **%d** | %d (%s) | 0 | 1 (`REQ-000`) |" % (
        reg.count("REQ"), reg.count("REQ", "deprecated"),
        ", ".join(reg.deprecated("REQ")))
    extra = "| TRC | **%d** | %d (%s) | 0 | 0 |" % (
        reg.count("TRC"), reg.count("TRC", "deprecated"),
        ", ".join(reg.deprecated("TRC")))
    patch(tmp, PRD, row, row + "\n" + extra)


@tool_case("check_prd.py",
           "blocking-Wert eingetragen, den die Formel nicht hergibt",
           "blocking abgeleitet")
def p_blocking_mismatch(tmp):
    # Trifft die Nachrechnung ALLER Eintraege mit Achsen (Aufgabe 1, letzter
    # Punkt) — nicht nur die Feststellung, dass ein Feld existiert.
    # Die ACHSENZEILE, nicht die Definitionszeile — beide beginnen mit
    # "| CONTRA-004 |". Die erste Fassung dieser Kontrolle traf die
    # Definitionszeile und belegte deshalb nichts.
    p = os.path.join(tmp, REG)
    t = open(p, encoding="utf-8").read()
    i = t.index("| CONTRA-004 | resolved | accepted |")
    j = t.index("\n", i)
    open(p, "w", encoding="utf-8").write(
        t[:i] + t[i:j].replace("**true**", "**false**", 1) + t[j:])


@tool_case("check_prd.py",
           "FEHLENDER status blockiert fail-closed (`!= resolved`, nicht "
           "`== open`)", "blocking abgeleitet")
def p_missing_status_is_blocking(tmp):
    # DER Fall, um dessentwillen der Formelwortlaut angeglichen wurde. Mit
    # `status == open` liefert ein leerer Statuswert false und blocking sinkt
    # still ab; mit `status != resolved` bleibt er true.
    p = os.path.join(tmp, REG)
    t = open(p, encoding="utf-8").read()
    i = t.index("| CONTRA-001 | resolved | accepted |")
    j = t.index("\n", i)
    open(p, "w", encoding="utf-8").write(
        t[:i] + t[i:j].replace("| resolved | accepted |", "|  | accepted |", 1)
        + t[j:])


def run_tool_cases():
    print("=" * 78)
    print("NEGATIVKONTROLLE — validate_trace.py und check_prd.py")
    print("=" * 78)
    ok = True
    n_ok = 0
    cases = TRACE_CASES + PRD_CASES
    for name, needle, fn, expect, tool in cases:
        tmp = stage()
        try:
            fn(tmp)
            rc, out = run_tool(tool, tmp)
        finally:
            shutil.rmtree(tmp)
        hit = needle in out
        good = (hit and rc != 0) if expect == "FAIL" else (hit and rc == 0)
        ok = ok and good
        n_ok += 1 if good else 0
        print("[%s] %-20s %s\n        rc=%d  Nachweistext %s"
              % ("OK" if good else "SCHWACH", tool, name, rc,
                 "gefunden" if hit else "NICHT gefunden — Kontrolle belegt nichts"))
    print("SCHARF: %d/%d Werkzeug-Negativkontrollen" % (n_ok, len(cases)))
    return ok


def main():
    # Kontrolle 0: unveraenderter Stand als Bezugsmessung.
    base = stage()
    base_res = run(base)
    shutil.rmtree(base)

    print("=" * 78)
    print("NEGATIVKONTROLLE — kann validate_intake.py ueberhaupt fehlschlagen?")
    print("=" * 78)
    print("Nachweisregel je Fall:")
    print("  expect=FAIL, Check unveraendert PASS  -> muss auf FAIL kippen")
    print("  expect=FAIL, Check unveraendert FAIL  -> muss MEHR Befunde melden")
    print("  expect=PASS                           -> darf sich NICHT verschlechtern")
    print("=" * 78)
    ok = True
    n_ok = 0
    for name, cid, fn, expect in CASES:
        before = status_of(base_res, cid)
        before_n = findings_of(base_res, cid)
        tmp = stage()
        try:
            fn(tmp)
            res = run(tmp)
            after = status_of(res, cid)
            after_n = findings_of(res, cid)
        finally:
            shutil.rmtree(tmp)

        if expect == "FAIL":
            if before == "PASS":
                good = (after == "FAIL")
                how = "PASS->FAIL"
            elif before == "FAIL":
                good = (after == "FAIL" and after_n > before_n)
                how = "Befunde %d->%d" % (before_n, after_n)
            else:
                good = False
                how = "Check nicht vorhanden"
        else:                       # expect == "PASS": keine Verschlechterung
            good = (after == before and after_n <= before_n)
            how = "%s(%d)->%s(%d)" % (before, before_n, after, after_n)

        ok = ok and good
        n_ok += 1 if good else 0
        print("[%s] %-6s %s\n        unveraendert=%s(%d) -> nach Injektion=%s(%d) "
              "[erwartet %s | %s]"
              % ("OK" if good else "SCHWACH", cid, name, before, before_n,
                 after, after_n, expect, how))
    print("=" * 78)
    print("SCHARF: %d/%d Negativkontrollen (validate_intake.py)" % (n_ok, len(CASES)))
    print("=" * 78)
    ok_tools = run_tool_cases()
    print("=" * 78)
    print("ERGEBNIS: %s" % ("alle Pruefungen sind scharf (jede reagiert auf ihren Defekt)"
                            if (ok and ok_tools)
                            else "MINDESTENS EINE PRUEFUNG IST STUMPF"))
    print("=" * 78)
    return 0 if (ok and ok_tools) else 1


if __name__ == "__main__":
    sys.exit(main())
