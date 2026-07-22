#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_intake.py — Intake-/Schema-Validator fuer das REVYR-Dokumentenpaket.

WICHTIG: Dieses Werkzeug wurde in diesem Lauf NEU verfasst. Es ist KEIN
vorbestehender Standard und war vorher im Repository nicht vorhanden
(vgl. docs/ID-REGISTRY.md §8 Punkt 13 und §9).

Es prueft mechanisch, was sonst nur behauptet wuerde. Es repariert nichts.
Ein Fehlschlag ist ein Befund, kein Anlass, die Pruefung abzuschwaechen.

Kanonische ID-Quelle: docs/ID-REGISTRY.md (ab Phase 2 eingefroren).
Der Validator vergibt, benennt und deprecated KEINE ID.

Aufruf:
    python3 validate_intake.py --repo "/Users/.../Run&Bike" [--json out.json]
"""

import argparse
import io
import json
import os
import re
import sys
import tokenize
from collections import defaultdict

# DIE kanonische Blocking-Implementierung. Es gibt keine zweite. Formel,
# Wertebereiche, Vokabularpruefung, Achsenparser und Ergebnisklassen kommen
# ausschliesslich von hier — validate_trace.py, check_prd.py, gen_intake.py
# und selftest_validator.py importieren dasselbe Modul.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blocking_model as BM  # noqa: E402

# ---------------------------------------------------------------------------
# Konfiguration
# ---------------------------------------------------------------------------

# BEFUND: Die Registry verwaltet seit dem Auftau-Schritt 2 auch `USER-` und
# `NFR-` (§5). Der Validator kannte nur die urspruenglichen zehn Praefixe und
# meldete deshalb JEDE Persona-Referenz als "nicht in der Registry" — ein
# Fehlalarm des Werkzeugs gegen einen korrekten Dokumentenstand.
MANAGED_PREFIXES = ["VIS", "CAN", "REQ", "AC", "TRC", "EV", "RISK", "ASM", "OQ",
                    "CONTRA", "USER", "NFR"]

# Von der Aufgabenstellung ausdruecklich verlangte Referenzpruefung:
REQUIRED_REF_PREFIXES = ["OQ", "REQ", "CAN", "AC", "TRC", "EV"]

# Registry-Entscheidung §4: Template-Platzhalter, keine echten Items.
TEMPLATE_PLACEHOLDERS = {"REQ-000", "AC-000", "EV-000"}

REGISTRY = "docs/ID-REGISTRY.md"
PRD = "docs/prd/revyr-endurance-platform.prd.md"
TRACE = "docs/traceability.md"
DECISION_LOG = "docs/decisions/decision-log.md"

# ---------------------------------------------------------------------------
# KANONISCHES STATUSMODELL fuer OQ- und CONTRA- (Registry §3.1)
# Diese Konstanten sind die EINZIGE Definition. gen_intake.py importiert sie
# aus diesem Modul, damit Validator und Generator nicht auseinanderlaufen
# koennen. Zwei unabhaengige Prueflaeufe kamen zuvor auf 2 bzw. 3 Divergenzen,
# weil jeder seine eigene, ungeschriebene Definition benutzte.
# ---------------------------------------------------------------------------

STATUS_VALUES = BM.STATUS_VALUES
RESOLUTION_VALUES = BM.RESOLUTION_VALUES
EVIDENCE_VALUES = BM.EVIDENCE_VALUES

# Registry §3.1: ausdruecklich unzulaessig als `status`-Wert.
FORBIDDEN_STATUS_VALUES = {"design-resolved", "evidence-pending", "pending",
                           "closed", "mitigated"}

# Registry §3: zulaessige `status`-Werte je Praefix.
ALLOWED_STATUS_BY_PREFIX = {
    "OQ": STATUS_VALUES,
    "CONTRA": STATUS_VALUES,
}
ALLOWED_STATUS_DEFAULT = {"active", "deprecated", "reserved", "template-placeholder"}

# C16 (Nutzerentscheidung 2026-07-19): `blocking_scope` ist ERSATZLOS entfallen.
# An seiner Stelle stehen zwei disjunkte Felder mit je abschliessendem
# Wertebereich. Beide kommen aus blocking_model.py — hier wird nichts kopiert.
GATES = BM.GATES
ACTIVITIES = BM.ACTIVITIES
CURRENT_ACTIVITY = BM.CURRENT_ACTIVITY
CONTRA_AXIS_COLUMNS = BM.CONTRA_AXIS_COLUMNS

OUTCOME_DECISION_OPEN = BM.OUTCOME_DECISION_OPEN
OUTCOME_EVIDENCE_PENDING = BM.OUTCOME_EVIDENCE_PENDING
OUTCOME_EVIDENCE_FAILED = BM.OUTCOME_EVIDENCE_FAILED
OUTCOME_COMPLETE = BM.OUTCOME_COMPLETE
OUTCOME_NOT_BLOCKING = BM.OUTCOME_NOT_BLOCKING
OUTCOME_BLOCKING = BM.OUTCOME_BLOCKING

# Die Registry ist die Datei, DIE Deprecation definiert. Ihre eigenen
# Deprecation- und Migrationstabellen sind daher keine Regelverstoesse.
DEPRECATED_REF_EXEMPT = {REGISTRY}

# Pflichtfelder je Requirement (Aufgabenstellung).
REQUIRED_REQ_FIELDS = [
    "measurement_type",
    "signal",                  # oder control_evidence
    "target_or_pass_condition",
    "owner",
    "release_gate",
]
SIGNAL_ALIASES = {"signal", "control_evidence", "signal_or_control_evidence",
                  "signal / control evidence", "signal_oder_control_evidence"}

# Werte, die ohne Begruendung ein unbegruendeter Nullwert waeren.
NULLISH = {"", "-", "--", "—", "–", "n/a", "na", "none", "null", "tbd", "tba",
           "?", "??", "keine", "keiner", "keines", "offen", "unklar"}

# Marker, die einen Nullwert ausdruecklich begruenden.
JUSTIFY_MARKERS = ["MISSING", "ASSUMPTION", "BLOCKER", "OPEN QUESTION",
                   "OPEN-QUESTION", "OFFENE FRAGE", "EVIDENCE-PENDING",
                   "PENDING", "OWNER-BLOCKER"]

# Pauschale Ausreden, die die Aufgabenstellung ausdruecklich verbietet.
BLANKET_PHRASES = ["nicht relevant", "nicht anwendbar", "spaeter", "später",
                   "n. a.", "entfaellt ohne begruendung"]


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


# Facetten-Kennungen des abgeschafften Ad-hoc-Raums: -a, -b, -c, -p1, -v1 … -v5.
# Suffixform: EIN Kleinbuchstabe, optional Ziffern, danach Wortgrenze.
FACET_SUFFIX = re.compile(r"-([a-z]\d*)(?![A-Za-z0-9_])")


def is_facet_at(text, end):
    """True, wenn direkt hinter einer ID-Nennung eine Facetten-Kennung steht.

    Ein Bindestrich, dem ein Grossbuchstabe, eine Ziffer oder ein Sonderzeichen
    folgt (CAN-003-Nachfolgeklausel, CAN-009-/VIS-006-Signal), ist KEINE Facette,
    sondern deutsche Wortbildung um eine echte Referenz herum.
    """
    return FACET_SUFFIX.match(text, end) is not None


def id_ref_regex(prefix):
    """Erfasst JEDE Nennung einer ID dieses Praefixes.

    BEFUND/FIX: Die Vorfassung trug den Lookahead `(?![0-9-])`. Er war gegen
    Facetten-Kennungen (CAN-009-a) gedacht, verwarf aber JEDE ID, auf die ein
    Bindestrich folgt — also auch echte Referenzen in deutscher Kompositumform
    (CAN-003-Nachfolgeklausel, CAN-009-/VIS-006-Signal). Diese Fundstellen wurden
    nicht klassifiziert, sondern waren fuer den Validator unsichtbar; C3a/C3b/C3c/C3d
    liefen ueber eine unvollstaendige Grundgesamtheit.
    Jetzt wird alles erfasst; Facette vs. echte Referenz entscheidet is_facet_at().
    `(?!\\d)` bleibt: eine vierstellige Zahl ist keine dreistellige ID.
    """
    return re.compile(r"(?<![A-Za-z0-9_-])" + prefix + r"-(\d{3})(?!\d)")


# ---------------------------------------------------------------------------
# Einlesen
# ---------------------------------------------------------------------------

def read(repo, rel):
    p = os.path.join(repo, rel)
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def collect_scanned_files(repo):
    """Alle Dokumente, die auf ID-Referenzen geprueft werden."""
    files = []
    docs = os.path.join(repo, "docs")
    for root, _dirs, names in os.walk(docs):
        for n in sorted(names):
            if n.endswith(".md"):
                files.append(os.path.relpath(os.path.join(root, n), repo))
    for extra in ("README.md", "intake-package.json"):
        if os.path.isfile(os.path.join(repo, extra)):
            files.append(extra)
    return sorted(files)


# ---------------------------------------------------------------------------
# Registry parsen
# ---------------------------------------------------------------------------

# Kopfzeile der kanonischen ID-Definitionstabellen (Registry §3).
REGISTRY_DEF_HEADER = ["id", "type", "title", "canonical_file", "status",
                       "created_at", "deprecated_at", "replacement_id", "notes"]


def _header_cells(line):
    s = line.strip()
    if not s.startswith("|"):
        return None
    return [c.strip().strip("*` ").lower() for c in s.strip("|").split("|")]


def parse_registry(text):
    """Liest die ID-Definitionszeilen der Registry.

    BEFUND/FIX (2026-07-19): Die Vorfassung akzeptierte JEDE Tabellenzeile mit
    >= 9 Spalten, deren erste Zelle wie eine ID aussieht — ohne die Kopfzeile zu
    pruefen. Seit Registry §6.11.1 existiert eine zweite, ebenfalls 9-spaltige
    Tabelle (das Statusmodell je CONTRA-ID) mit voellig anderer Spaltenbedeutung.
    Deren Zeilen wurden als ID-DEFINITIONEN eingelesen; Spalte 5 ist dort
    `blocking`, nicht `status`. Ergebnis war der Phantombestand
    "CONTRA false=1, resolved=6, true=5" (12 statt 6 Contradictions) und
    drei frei erfundene Statusdivergenzen in C6b.
    Jetzt wird nur gelesen, was unter der kanonischen Kopfzeile steht.
    """
    entries = []
    id_col = re.compile(r"^([A-Z]+)-(\d{3})$")
    in_def_table = False
    prev_cells = None
    for lineno, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if not s.startswith("|"):
            in_def_table = False
            prev_cells = None
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and all(set(c) <= set("-: ") and c for c in cells):
            # Trennzeile: die Zeile darueber war die Kopfzeile.
            in_def_table = (prev_cells == REGISTRY_DEF_HEADER)
            prev_cells = None
            continue
        prev_cells = _header_cells(line)
        if not in_def_table:
            continue
        if len(cells) < 9:
            continue
        m = id_col.match(cells[0].strip("*` "))
        if not m:
            continue
        if m.group(1) not in MANAGED_PREFIXES:
            continue
        entries.append({
            "id": cells[0].strip("*` "),
            "prefix": m.group(1),
            "type": cells[1],
            "title": cells[2],
            "canonical_file": cells[3].strip("`"),
            "status": cells[4].strip("`* "),
            "created_at": cells[5],
            "deprecated_at": cells[6],
            "replacement_id": cells[7],
            "notes": cells[8],
            "lineno": lineno,
        })
    return entries


# ---------------------------------------------------------------------------
# PRD-Messmodell parsen
# ---------------------------------------------------------------------------

def parse_prd_blocks(text):
    """### REQ-0xx — Titel  +  | feld | wert | Tabelle."""
    blocks = {}
    heads = list(re.finditer(r"^###\s+(REQ-\d{3})\s*[—–-]\s*(.+)$", text, re.M))
    for i, h in enumerate(heads):
        start = h.end()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[start:end]
        fields = {}
        for line in body.split("\n"):
            s = line.strip()
            if not s.startswith("|"):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) != 2:
                continue
            key = norm(cells[0]).lower().strip("*` ")
            if key in ("feld", "field", "---", ""):
                continue
            if set(key) <= set("-: "):
                continue
            fields[key] = cells[1]
        blocks[h.group(1)] = {
            "title": norm(h.group(2)),
            "fields": fields,
            "body": body,
            "lineno": text[:h.start()].count("\n") + 1,
        }
    return blocks


# ---------------------------------------------------------------------------
# Traceability parsen
# ---------------------------------------------------------------------------

def parse_trace_matrix(text):
    """Kernmatrix: | TRC-xxx | REQ-xxx — ... | VIS | CAN | AC | EV | ... |

    BEFUND/FIX (dieser Lauf): Die Vorfassung verlangte die Zelle WOERTLICH als
    `TRC-\\d{3}` und verwarf jede Zeile mit Markdown-Auszeichnung. Damit war sie
    blind fuer genau die fuenf Zeilen, um die es geht:
    `**TRC-037**` … `**TRC-040**` (die vier neuen) und `~~TRC-014~~` (die
    deprecatete). Der Validator meldete daraufhin REQ-037…040 als "keine Zeile
    in der Kernmatrix" und AC-037…041 / EV-037…042 als "nicht verknuepft" —
    VIER FALSCHE BEFUNDKLASSEN gegen ein korrektes Dokument. Ein zweites
    Werkzeug (validate_trace.py) kam parallel auf eine andere Zeilenzahl; die
    Werkzeuge widersprachen einander.

    Es wurde das WERKZEUG geaendert, nicht das Dokument: die Zeilen sind da.
    Dieselbe Fehlerklasse wie der frueher Bindestrich-blinde ID-Tokenizer —
    eine Pruefung, die ihren Gegenstand nicht sieht, ist keine bestandene
    Pruefung, sondern eine blinde.
    """
    rows = []
    for lineno, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 6:
            continue
        raw = cells[0]
        trc_m = re.match(r"^(?:\*\*|~~)*\s*(TRC-\d{3})\s*(?:\*\*|~~)*$", raw)
        if not trc_m:
            continue
        trc = trc_m.group(1)
        # `~~TRC-014~~` ist als deprecated GEFUEHRT und zaehlt nicht als aktive
        # Zeile — geloescht werden darf sie nicht, mitgezaehlt aber auch nicht.
        deprecated = "~~" in raw
        req = re.search(r"(?<![A-Za-z0-9_-])REQ-(\d{3})(?![0-9-])", cells[1])
        # BEFUND/FIX: Die Vorfassung nahm mit re.search NUR DEN ERSTEN Treffer
        # je Spalte. REQ-019 traegt aber ZWEI ACs (AC-019 funktional, AC-041
        # Messkriterium) und ZWEI EVs (EV-019, EV-041) — genau die Aufteilung,
        # die in diesem Lauf beschlossen wurde. AC-041 und EV-041 galten
        # dadurch als "in der Kernmatrix nicht verknuepft", obwohl sie in der
        # Zeile stehen. Jetzt werden ALLE Treffer der Spalte gelesen.
        acs_in_row = re.findall(r"(?<![A-Za-z0-9_-])AC-\d{3}(?!\d)", cells[4])
        evs_in_row = re.findall(r"(?<![A-Za-z0-9_-])EV-\d{3}(?!\d)", cells[5])
        rows.append({
            "trc": trc,
            "deprecated": deprecated,
            "req": "REQ-" + req.group(1) if req else None,
            "ac": acs_in_row[0] if acs_in_row else None,
            "ev": evs_in_row[0] if evs_in_row else None,
            "acs": acs_in_row,
            "evs": evs_in_row,
            "cells": cells,
            "lineno": lineno,
        })
    # Nur die erste (Kern-)Matrix: Duplikate nach TRC-ID entfernen,
    # spaetere Wiederholungen derselben TRC-ID sind Detailbloecke.
    seen, uniq = set(), []
    for r in rows:
        if r["trc"] in seen:
            continue
        seen.add(r["trc"])
        uniq.append(r)
    return uniq


# ---------------------------------------------------------------------------
# CONTRA-Achsen: Statusmodell parsen und `blocking` ABLEITEN
# ---------------------------------------------------------------------------

def _clean(cell):
    return re.sub(r"[`*]", "", norm(cell)).strip()


# ---------------------------------------------------------------------------
# C16: EINE Implementierung, importiert — keine Kopie, keine Variante.
#
# Vorher lagen hier DREI Fassungen der Blocking-Logik im Projekt:
#   validate_intake.derive_blocking()  (Konvention)
#   validate_intake.derive_blocking_literal()  (woertliche Lesart)
#   check_prd.py, inline, mit einem je-ID-hartkodierten Erwartungs-Dict
# Sie konnten auseinanderlaufen und sind genau deshalb auseinandergelaufen.
# Jetzt gibt es nur noch blocking_model.derive_blocking().
# ---------------------------------------------------------------------------

_clean = BM.clean
parse_contra_axes = BM.parse_contra_axes
derive_blocking = BM.derive_blocking
classify_contra = BM.classify


# Kopfzeilen, die eine zweispaltige Tabelle als Feld/Wert-Tabelle ausweisen.
FIELD_TABLE_HEADERS = {"feld", "field"}


def parse_field_tables(text, scoped=True):
    """Zeilen aus Feld/Wert-Tabellen.

    scoped=True  -> NUR Tabellen mit Kopfzeile `| Feld | Wert |` (bzw. Field/Value).
                    Das ist das Format der Messmodell-Bloecke in PRD und
                    Traceability. Andere zweispaltige Tabellen sind Vergleichs-
                    oder Aufzaehlungstabellen und haben keine Feldsemantik;
                    eine leere Zelle darin ist kein Nullwert.
    scoped=False -> jede zweispaltige Zeile (roher, unscharfer Erstlauf).
    """
    out = []
    lines = text.split("\n")
    in_field_table = False
    for idx, line in enumerate(lines):
        lineno = idx + 1
        s = line.strip()
        if not s.startswith("|"):
            in_field_table = False
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) != 2:
            in_field_table = False
            continue
        key = norm(cells[0]).strip("*` ")
        if set(key) <= set("-: ") and key:
            continue                      # Trennzeile |---|---|
        if key.lower() in FIELD_TABLE_HEADERS:
            in_field_table = True         # Kopfzeile erkannt
            continue
        if not key:
            continue
        if scoped and not in_field_table:
            continue
        out.append((lineno, key, cells[1]))
    return out


# ---------------------------------------------------------------------------
# Pruefungen
# ---------------------------------------------------------------------------

class Result(object):
    def __init__(self):
        self.checks = []

    def add(self, cid, name, passed, actual, findings=None, note=None):
        self.checks.append({
            "id": cid,
            "name": name,
            "status": "PASS" if passed else "FAIL",
            "actual": actual,
            "findings": findings or [],
            "note": note,
        })


def is_justified(value):
    up = value.upper()
    return any(mk in up for mk in JUSTIFY_MARKERS)


def check_req_fields(res, reg_by_id, prd_blocks):
    active_reqs = sorted(e["id"] for e in reg_by_id
                         if e["prefix"] == "REQ" and e["status"] == "active")
    findings = []
    complete = 0
    owner_blockers = []
    for rid in active_reqs:
        blk = prd_blocks.get(rid)
        if not blk:
            findings.append({"id": rid, "problem": "kein Messmodell-Block im PRD"})
            continue
        f = blk["fields"]
        missing = []
        # signal ODER control evidence
        if not any(norm(f.get(k, "")) for k in SIGNAL_ALIASES if k in f):
            if not norm(f.get("signal", "")):
                missing.append("signal|control_evidence")
        for key in ("measurement_type", "target_or_pass_condition",
                    "owner", "release_gate"):
            if not norm(f.get(key, "")):
                missing.append(key)
        owner = norm(f.get("owner", ""))
        if owner and owner.lower() in NULLISH:
            missing.append("owner (leerer Platzhalter)")
        elif owner and is_justified(owner):
            owner_blockers.append(rid)
        if missing:
            findings.append({"id": rid, "problem": "fehlende Felder: " + ", ".join(missing)})
        else:
            complete += 1
    # KEINE hartkodierte Gesamtzahl. Die Grundgesamtheit ist die Menge der
    # aktiven REQ-IDs aus docs/ID-REGISTRY.md. Frueher stand hier
    # `complete == 36` — dieselbe Pruefung waere nach jeder legitimen
    # Erweiterung des ID-Bestands fehlgeschlagen, ohne dass etwas defekt ist.
    n_active = len(active_reqs)
    res.add("C1",
            "%d/%d REQs (Anzahl aus der Registry abgeleitet) mit "
            "measurement_type, signal|control_evidence, target_or_pass_condition, "
            "owner-oder-sichtbarem-Owner-Blocker, release_gate"
            % (n_active, n_active),
            n_active > 0 and complete == n_active and not findings,
            "%d/%d REQs vollstaendig; davon %d mit sichtbarem Owner-Blocker statt DRI"
            % (complete, n_active, len(owner_blockers)),
            findings,
            note="Grundgesamtheit aus %s abgeleitet (status = active), nicht "
                 "abgetippt. n > 0 ist Bestehensbedingung." % REGISTRY)
    return owner_blockers


def check_null_values(res, repo, files):
    findings = []
    checked = 0
    raw_hits = 0
    for rel in files:
        if not rel.endswith(".md"):
            continue
        text = read(repo, rel)
        # Roher Erstlauf-Zaehler zur Offenlegung (siehe Bericht).
        for _ln, _k, v in parse_field_tables(text, scoped=False):
            if norm(v).strip("*` ").lower() in NULLISH and not is_justified(v):
                raw_hits += 1
        for lineno, key, value in parse_field_tables(text, scoped=True):
            checked += 1
            v = norm(value).strip("*` ")
            low = v.lower()
            if low in NULLISH and not is_justified(v):
                findings.append({"file": rel, "line": lineno, "field": key,
                                 "value": v, "problem": "leerer/nullwertiger Feldwert ohne Begruendung"})
                continue
            for ph in BLANKET_PHRASES:
                if low == ph or low.startswith(ph + ".") or low == ph + ".":
                    findings.append({"file": rel, "line": lineno, "field": key,
                                     "value": v,
                                     "problem": "pauschale Nichtanwendbarkeit ohne "
                                                "requirement-spezifische Begruendung"})
                    break
    res.add("C2", "0 unbegruendete Nullwerte in Feld/Wert-Tabellen",
            not findings,
            "%d Feldwerte in `| Feld | Wert |`-Tabellen geprueft, %d unbegruendete Nullwerte"
            % (checked, len(findings)),
            findings,
            note="Ungescopter Erstlauf ueber ALLE zweispaltigen Zeilen ergab %d Treffer; "
                 "davon sind %d Fehlalarme aus zweispaltigen Vergleichstabellen ohne "
                 "Feldsemantik (Architektur §16 Zulaessig/Nicht-zulaessig-Liste, "
                 "linke Spalte laenger als rechte). Beide Zahlen sind offengelegt."
                 % (raw_hits, raw_hits - len(findings)))


# Marker, die eine Zeile als Migrations-/Provenienzdokumentation ausweisen.
# Registry-Regel 1 verlangt, den deprecateten Eintrag zu ERHALTEN; Regel 7 verlangt
# ausdruecklich Alias-/Migrationstabellen. Solche Zeilen sind daher keine
# Regelverstoesse, sondern die von der Registry geforderte Dokumentation.
MIGRATION_MARKERS = ["~~", "deprecated", "Herkunft", "Alt-ID", "Alt-Item", "entfallen",
                     "ersetzt", "Ersetzt", "abgeloest", "abgelöst", "Sammelblock",
                     "nicht mehr referenzierbar", "Migration", "Nachfolger",
                     "Legacy", "KOLLISION", "Facette"]

# Marker, die eine reservierte ID korrekt als offenen Punkt kennzeichnen
# (statt sie als erfuellte Verknuepfung zu zaehlen).
RESERVED_OK_MARKERS = ["MISSING", "BLOCKER", "reserved", "reserviert", "offen",
                       "OPEN QUESTION", "Nutzerentscheidung"]


# Spalten-/Feldnamen, in denen eine ID als ERFUELLTE Verknuepfung gilt.
# Nur hier ist eine deprecatete oder reservierte ID ein Regelverstoss.
# Provenienz- ("Herkunft"), Migrations-, Befund- und Prosakontexte sind es nicht:
# dort wird die ID BESCHRIEBEN, nicht als gueltiger Anker VERWENDET.
LINK_COLUMN_MARKERS = ["canvas item", "vision item", "acceptance criterion",
                       "acceptance", "evidence", "requirement", "risiko", "risk",
                       "trace id", "verknuepfung", "verknüpfung", "anker",
                       "primaer", "primär"]
PROVENANCE_COLUMN_MARKERS = ["herkunft", "alt-", "legacy", "ursprung", "quelle",
                             "ersetzt", "nachfolg", "migration", "fundstelle",
                             "facette", "bisher", "sammelblock"]


def is_link_column(colname):
    c = (colname or "").lower()
    if any(m in c for m in PROVENANCE_COLUMN_MARKERS):
        return False
    return any(m in c for m in LINK_COLUMN_MARKERS)


def split_row(line):
    s = line.strip()
    if not s.startswith("|"):
        return None
    return [c.strip() for c in s.strip("|").split("|")]


def build_column_map(lines):
    """Ordnet jeder Tabellenzeile ihre Kopfzeilen-Zellen zu.

    Rueckgabe: dict lineno -> list[str] (Spaltennamen) oder None fuer Prosa.
    Bei `| Feld | Wert |`-Tabellen wird stattdessen der Feldname der Zeile
    selbst als Spaltenname der Wertspalte verwendet.
    """
    colmap = {}
    header = None
    prev = None
    for idx, line in enumerate(lines):
        lineno = idx + 1
        cells = split_row(line)
        if cells is None:
            header, prev = None, None
            continue
        if cells and all(set(c) <= set("-: ") and c for c in cells):
            header = prev            # Zeile darueber war die Kopfzeile
            colmap[lineno] = None
            prev = cells
            continue
        if header is None:
            prev = cells
            colmap[lineno] = None
            continue
        if len(header) == 2 and header[0].strip("*` ").lower() in FIELD_TABLE_HEADERS:
            # Feld/Wert-Tabelle: Feldname der Zeile benennt die Wertspalte
            colmap[lineno] = [cells[0], cells[0]] if len(cells) >= 2 else None
        else:
            colmap[lineno] = header
        prev = cells
    return colmap


# EIN gemeinsames Vokabular fuer "hier wird UEBER die ID gesprochen, sie wird
# nicht als Anker VERWENDET". Dieselbe Liste traegt C14 (ein Kommentar, der den
# Defekt beschreibt, ist nicht der Defekt), C16 (kontrafaktische Beschreibung
# des Alt-Vergleichs) und C3c. Drei getrennte Listen waeren derselbe Fehler wie
# drei getrennte Blocking-Formeln.
#
# `deprecat` bewusst als STAMM: die Artefakte schreiben "deprecated",
# "deprecatete", "deprecateten". Ein Marker "deprecated" traf die deutschen
# Beugungsformen nicht — dieselbe Fehlerklasse wie der frueher
# Bindestrich-blinde Tokenizer.
PROVENANCE_MARKERS = tuple(sorted(set(BM.HISTORICAL_MARKERS) | {
    "nachfolger", "ersetzt", "ersetzung", "vorher", "früher", "frueher",
    "deprecat", "abgelöst", "abgeloest", "statt", "herkunft", "alt-",
    "altfassung", "migration", "war ", "abgeleitet", "nachgezogen",
    "nannte", "umgedeutet", "beinahe-treffer",
}))


# Aussagen, die eine ID als abgeloest AUSWEISEN. Sie verwenden die ID nicht als
# Anker, sondern sprechen ueber sie.
DEPRECATION_PREDICATES = ("deprecated", "ersetzt", "abgelöst", "abgeloest",
                          "nicht mehr", "keine aktive", "entfällt", "entfaellt",
                          "validierungsfehler", "migrationstabelle",
                          "nachfolger", "zählt in", "zaehlt in")


def _sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+|\s+·\s+|\n", text) if s.strip()]


def _is_provenance_annotation(cell, ref):
    """True, wenn `ref` in dieser Zelle nur als Herkunfts- oder
    Abloesungsangabe vorkommt, nicht als Anker.

    Zwei Formen, beide ENG gefasst:
      (a) die ID steht in einer Klammer-/Kursivgruppe MIT Provenienzmarker;
      (b) JEDER Satz, der die ID enthaelt, sagt etwas UEBER ihre Abloesung
          ("Ersetzt das deprecatete EV-014", "REQ-014 ist keine aktive
          Anforderung mehr", "Neue Referenzen auf REQ-014 sind ein
          Validierungsfehler").

    Eine nackte deprecatete ID in einer Verknuepfungsspalte erfuellt weder (a)
    noch (b) und bleibt ein Verstoss — dafuer gibt es eine Negativkontrolle.
    Dieselbe Beweisfuehrung wie bei C14 (ein Kommentar, der den Defekt
    beschreibt, ist nicht der Defekt) und C16 (HISTORICAL_MARKERS).
    """
    rx = re.compile(r"(?<![A-Za-z0-9_-])" + re.escape(ref) + r"(?!\d)")
    # (a) Klammer-/Kursivgruppe
    for m in re.finditer(r"\(([^()]*)\)|\*\(([^()]*)\)\*|\*([^*]+)\*", cell):
        group = next((g for g in m.groups() if g), "")
        if ref not in group:
            continue
        if any(mk in group.lower() for mk in PROVENANCE_MARKERS):
            outside = cell[:m.start()] + cell[m.end():]
            if not rx.search(outside):
                return True
    # (b) satzweise Abloesungsaussage
    hits = [s for s in _sentences(cell) if rx.search(s)]
    if hits and all(any(mk in s.lower() for mk in
                        DEPRECATION_PREDICATES + PROVENANCE_MARKERS)
                    for s in hits):
        return True
    return False


def classify_occurrence(line, lineno, colmap, ref):
    """Mechanische Klassifikation: 'live' nur, wenn die ID in einer
    Verknuepfungsspalte steht. Sonst 'context'."""
    cells = split_row(line)
    if cells is None:
        return "context"                     # Prosa: Beschreibung, kein Anker
    header = colmap.get(lineno)
    if not header:
        return "context"
    # Gleicher Fix wie in id_ref_regex(): der fruehere Lookahead `(?![0-9-])` fand
    # eine ID in Kompositumform in KEINER Zelle wieder und stufte sie damit still
    # auf "context" herunter, auch wenn sie in einer Verknuepfungsspalte stand.
    rx = re.compile(r"(?<![A-Za-z0-9_-])" + re.escape(ref) + r"(?!\d)")
    for i, cell in enumerate(cells):
        if not any(not is_facet_at(cell, m.end()) for m in rx.finditer(cell)):
            continue
        # BEFUND/FIX: `~~REQ-014~~` ist die Deprecation-Auszeichnung selbst.
        # Eine durchgestrichene ID ist per Definition kein aktiver Anker; sie
        # als solchen zu melden beanstandet die Deprecation-Kennzeichnung.
        if re.search(r"~~[^~]*" + re.escape(ref) + r"[^~]*~~", cell):
            continue
        # BEFUND/FIX: Auch INNERHALB einer Verknuepfungsspalte steht Provenienz.
        # `**REQ-037 — Accessibility** *(neu 2026-07-19, Nachfolger 1/2 von
        # REQ-014)*` verankert REQ-037; REQ-014 ist dort die Herkunftsangabe.
        # Die Vorfassung stufte die ganze Zelle als Anker ein und beanstandete
        # damit die Herkunftsangabe, die die Ablösung gerade belegt.
        # ENG GEFASST: nur wenn die ID in einer Klammer ODER Kursivgruppe steht
        # UND diese Gruppe einen Provenienzmarker traegt. Eine nackte
        # deprecatete ID in einer Verknuepfungsspalte bleibt ein Verstoss
        # (Negativkontrolle C3c in selftest_validator.py).
        if _is_provenance_annotation(cell, ref):
            continue
        colname = header[i] if i < len(header) else ""
        if is_link_column(colname):
            return "live"
    return "context"


# Kanonische Nicht-Erfuellungsmarker aus dem Statusmodell des Projekts. KEIN
# freies Prosa-Vokabular: `MISSING`, `BLOCKER` und `reserved` sind die drei
# Werte, mit denen die Artefakte einen noch nicht eingeloesten Anker
# auszeichnen.
_UNFULFILLED_IN_CELL = re.compile(
    r"\bMISSING\b|\bBLOCKER\b|\breserved\b|z[äa]hlt\s+nicht|noch\s+nicht", re.I)


def classify_reserved_occurrence(line, lineno, colmap, ref):
    """Wie classify_occurrence — aber fuer RESERVIERTE IDs.

    BEFUND/FIX (2026-07-20): C3d heisst "reservierte IDs werden nirgends als
    ERFUELLTE Verknuepfung gezaehlt", und sein Hinweistext behauptete, die
    Fundstellen seien danach unterschieden, ob sie "korrekt als MISSING/BLOCKER
    gekennzeichnet" sind. Der Code tat das NICHT: er benutzte dieselbe
    Klassifikation wie fuer deprecatete IDs, die allein auf die Spalte sieht.
    Zellen wie `**VIS-012 — reserved, Inhalt MISSING → BLOCKER**` wurden damit
    als erfuellte Verknuepfung gemeldet — obwohl die Zelle das Gegenteil sagt.
    Der Hinweistext beschrieb eine Pruefung, die es nicht gab; die Zahl
    "korrekt gekennzeichnet" entstand als Nebenprodukt der Spaltenlage.

    Jetzt wird die behauptete Pruefung tatsaechlich ausgefuehrt: eine
    reservierte ID in einer Verknuepfungsspalte ist nur dann `live`, wenn die
    ZELLE sie nicht zugleich als unerfuellt ausweist. Der Marker muss in
    derselben Zelle stehen — eine Fussnote weiter unten entlastet nichts.
    """
    if classify_occurrence(line, lineno, colmap, ref) != "live":
        return "context"
    cells = split_row(line) or []
    rx = re.compile(r"(?<![A-Za-z0-9_-])" + re.escape(ref) + r"(?!\d)")
    for cell in cells:
        if rx.search(cell) and _UNFULFILLED_IN_CELL.search(cell):
            return "context"
    return "live"


def check_references(res, repo, files, reg_index):
    # Reservierte CAN-IDs zur Laufzeit, damit kein Hinweistext eine Menge
    # behauptet, die die Registry nicht fuehrt.
    reserved_can_ids = sorted(
        rid for rid, ents in reg_index.items()
        if rid.startswith("CAN-") and ents and ents[0]["status"] == "reserved")
    unknown, deprecated_refs, reserved_refs, facet_refs = [], [], [], []
    counts = defaultdict(int)
    regexes = {p: id_ref_regex(p) for p in MANAGED_PREFIXES}
    for rel in files:
        text = read(repo, rel)
        lines = text.split("\n")
        colmap = build_column_map(lines)
        for lineno, line in enumerate(lines, 1):
            for p in MANAGED_PREFIXES:
                for m in regexes[p].finditer(line):
                    ref = "%s-%s" % (p, m.group(1))
                    if is_facet_at(line, m.end()):
                        # Kennung des abgeschafften Facettenraums (CAN-009-a).
                        # Sie nennt NICHT die Basis-ID und wird deshalb nicht als
                        # deren Referenz gezaehlt — aber sie wird erfasst und
                        # ausgewiesen, nicht stillschweigend verworfen.
                        facet_refs.append({
                            "file": rel, "line": lineno,
                            "facet": line[m.start():FACET_SUFFIX.match(line, m.end()).end()],
                            "base": ref,
                            "kind": classify_occurrence(line, lineno, colmap, ref)})
                        continue
                    counts[p] += 1
                    if ref in TEMPLATE_PLACEHOLDERS:
                        continue          # Registry §4: Platzhalter, kein Fehlalarm
                    ents = reg_index.get(ref)
                    if not ents:
                        unknown.append({"file": rel, "line": lineno, "id": ref})
                        continue
                    statuses = set(e["status"] for e in ents)
                    if statuses == {"deprecated"} and rel not in DEPRECATED_REF_EXEMPT:
                        deprecated_refs.append({
                            "file": rel, "line": lineno, "id": ref,
                            "kind": classify_occurrence(line, lineno, colmap, ref),
                            "text": norm(line)[:160]})
                    if "reserved" in statuses and "active" not in statuses:
                        reserved_refs.append({
                            "file": rel, "line": lineno, "id": ref,
                            "kind": classify_reserved_occurrence(
                                line, lineno, colmap, ref),
                            "text": norm(line)[:160]})

    req_unknown = [u for u in unknown if u["id"].split("-")[0] in REQUIRED_REF_PREFIXES]
    res.add("C3a",
            "0 ungueltige Referenzen (OQ, REQ, CAN, AC, TRC, EV) gegen docs/ID-REGISTRY.md",
            not req_unknown,
            "%d Referenzen der geforderten Praefixe geprueft, %d unbekannt"
            % (sum(counts[p] for p in REQUIRED_REF_PREFIXES), len(req_unknown)),
            req_unknown)
    facet_live = [f for f in facet_refs if f["kind"] == "live"]
    res.add("C3b",
            "0 ungueltige Referenzen ueber alle %d verwalteten Praefixe"
            % len(MANAGED_PREFIXES),
            not unknown,
            "%d Referenzen geprueft, %d unbekannt" % (sum(counts.values()), len(unknown)),
            unknown,
            note="Zusaetzlich erfasst und getrennt gefuehrt: %d Fundstellen des "
                 "abgeschafften Facettenraums (z. B. CAN-009-a), davon %d in einer "
                 "Verknuepfungsspalte. Sie zaehlen NICHT als Referenz der Basis-ID. "
                 "Die Vorfassung des Tokenizers verwarf sie zusammen mit echten "
                 "Referenzen in Kompositumform unsichtbar."
                 % (len(facet_refs), len(facet_live)))
    dep_live = [d for d in deprecated_refs if d["kind"] == "live"]
    dep_ctx = [d for d in deprecated_refs if d["kind"] == "context"]
    res.add("C3c",
            "0 AKTIVE Verknuepfungen auf deprecatete IDs (Registry-Regel 3). "
            "Migrations-/Provenienzzeilen zaehlen nicht als Verstoss, weil Registry-Regel 1 "
            "den Alt-Eintrag zu erhalten und Regel 7 eine Alias-Tabelle zu fuehren verlangt. "
            "docs/ID-REGISTRY.md selbst ausgenommen, weil sie Deprecation definiert.",
            not dep_live,
            "%d Fundstellen deprecateter IDs gesamt: %d Migrations-/Provenienzkontext, "
            "%d aktive Verknuepfung" % (len(deprecated_refs), len(dep_ctx), len(dep_live)),
            dep_live,
            note="Der ungescopte Erstlauf meldete alle %d Fundstellen als Verstoss. "
                 "Die Klassifikation ist mechanisch und spaltenbasiert: 'live' nur, wenn "
                 "die ID in einer Verknuepfungsspalte steht (Canvas Item, Vision Item, "
                 "Acceptance Criterion, Evidence, Risiko, Trace ID). Provenienzspalten "
                 "('Herkunft'), Migrationstabellen und Prosa beschreiben die Alt-ID, "
                 "verwenden sie aber nicht als gueltigen Anker. "
                 "Negativkontrolle: siehe selftest_validator.py."
                 % len(deprecated_refs))
    rsv_live = [d for d in reserved_refs if d["kind"] == "live"]
    rsv_ctx = [d for d in reserved_refs if d["kind"] == "context"]
    res.add("C3d",
            "Reservierte IDs werden nirgends als ERFUELLTE Verknuepfung gezaehlt "
            "(Registry: 'darf noch nicht als erfuellte Referenz gezaehlt werden')",
            not rsv_live,
            "%d Fundstellen reservierter IDs gesamt: %d korrekt als MISSING/BLOCKER "
            "gekennzeichnet, %d ohne solche Kennzeichnung"
            % (len(reserved_refs), len(rsv_ctx), len(rsv_live)),
            rsv_live,
            # BEFUND/FIX: Hier stand eine abgetippte Menge reservierter CAN-IDs.
            # Sie war ueberholt — die Registry fuehrt weniger reservierte
            # Canvas-Items, als der Hinweis behauptete, und der Wortlaut wurde
            # aus diesem Hinweis woertlich in weitere Artefakte uebernommen.
            # Jetzt zur Laufzeit aus der Registry.
            note="Die %d reservierten CAN-IDs (%s) bleiben "
                 "inhaltlich MISSING und sind ein offener BLOCKER, unabhaengig davon, "
                 "dass sie korrekt gekennzeichnet referenziert werden."
                 % (len(reserved_can_ids), ", ".join(reserved_can_ids)))
    return dict(counts), len(deprecated_refs), len(reserved_refs)


def check_duplicate_ids(res, entries):
    by_id = defaultdict(list)
    for e in entries:
        by_id[e["id"]].append(e)
    findings = []
    for rid, ents in sorted(by_id.items()):
        actives = [e for e in ents if e["status"] == "active"]
        if len(actives) > 1:
            files = set(e["canonical_file"] for e in actives)
            findings.append({"id": rid, "problem":
                             "%d aktive Eintraege in %d canonical_file(s): %s"
                             % (len(actives), len(files), ", ".join(sorted(files))),
                             "lines": [e["lineno"] for e in actives]})
    res.add("C4", "0 doppelte IDs (keine ID zweimal 'active' mit unterschiedlicher canonical_file)",
            not findings,
            "%d eindeutige IDs registriert, %d Duplikate" % (len(by_id), len(findings)),
            findings)


def check_coverage(res, entries, trace_rows, prd_blocks, reg_index):
    active = lambda p: sorted(e["id"] for e in entries
                              if e["prefix"] == p and e["status"] == "active")
    reqs, acs, evs, trcs = active("REQ"), active("AC"), active("EV"), active("TRC")

    # Deprecatete Kernmatrix-Zeilen (`~~TRC-014~~`) werden GEFUEHRT, aber nicht
    # als aktive Zeilen gewertet. Sie tragen bewusst `—` in den Verknuepfungs-
    # spalten; sie als verwaist oder als Kopplungsbruch zu melden waere ein
    # Fehlalarm gegen die Registry-Regel, deprecatete IDs nicht zu loeschen.
    dep_rows = [r for r in trace_rows if r.get("deprecated")]
    trace_rows = [r for r in trace_rows if not r.get("deprecated")]

    # verwaiste Traceability-Zeilen
    orphan = []
    for r in trace_rows:
        if r["trc"] not in reg_index:
            orphan.append({"trc": r["trc"], "line": r["lineno"],
                           "problem": "TRC-ID nicht in der Registry"})
        elif r["req"] is None:
            orphan.append({"trc": r["trc"], "line": r["lineno"],
                           "problem": "Zeile nennt kein Requirement"})
        elif r["req"] not in reqs:
            orphan.append({"trc": r["trc"], "line": r["lineno"],
                           "problem": "verweist auf unbekanntes Requirement %s" % r["req"]})
    res.add("C5a", "0 verwaiste Traceability-Zeilen", not orphan,
            "%d aktive Kernmatrix-Zeilen geprueft, %d verwaist; zusaetzlich %d "
            "deprecatete Zeile(n) gefuehrt und bewusst nicht mitgezaehlt: %s"
            % (len(trace_rows), len(orphan), len(dep_rows),
               ", ".join(r["trc"] for r in dep_rows) or "keine"),
            orphan)

    # REQs ohne Traceability
    traced = set(r["req"] for r in trace_rows if r["req"])
    untraced = [{"id": q, "problem": "keine Zeile in der Kernmatrix"}
                for q in reqs if q not in traced]
    res.add("C5b", "0 REQs ohne Traceability", not untraced,
            "%d/%d REQs in der Kernmatrix" % (len(traced & set(reqs)), len(reqs)),
            untraced)

    # AC ohne Requirement
    ac_orphan = []
    for a in acs:
        ent = reg_index[a][0]
        m = re.search(r"(?<![A-Za-z0-9_-])REQ-(\d{3})(?![0-9-])",
                      ent["notes"] + " " + ent["title"])
        if not m:
            ac_orphan.append({"id": a, "problem": "kein Requirement-Bezug in der Registry"})
        elif "REQ-" + m.group(1) not in reqs:
            ac_orphan.append({"id": a, "problem": "Bezug auf unbekanntes REQ-%s" % m.group(1)})
        elif a not in {x for r in trace_rows for x in r.get("acs", [])}:
            ac_orphan.append({"id": a, "problem": "in der Kernmatrix nicht verknuepft"})
    res.add("C5c", "0 AC ohne Requirement", not ac_orphan,
            "%d AC geprueft, %d ohne Requirement-Bezug" % (len(acs), len(ac_orphan)),
            ac_orphan)

    # EV ohne Bezug
    ev_orphan = []
    for v in evs:
        ent = reg_index[v][0]
        m = re.search(r"(?<![A-Za-z0-9_-])REQ-(\d{3})(?![0-9-])",
                      ent["notes"] + " " + ent["title"])
        if not m:
            ev_orphan.append({"id": v, "problem": "kein Requirement-Bezug in der Registry"})
        elif "REQ-" + m.group(1) not in reqs:
            ev_orphan.append({"id": v, "problem": "Bezug auf unbekanntes REQ-%s" % m.group(1)})
        elif v not in {x for r in trace_rows for x in r.get("evs", [])}:
            # BEFUND/FIX: Ein Nachweis kann an einem WIDERSPRUCH haengen statt
            # an einer Requirement-Zeile. EV-042 gehoert zu CONTRA-005 (mit
            # REQ-017/REQ-027) und hat deshalb korrekt keine eigene
            # Kernmatrix-Zeile; docs/traceability.md weist das ausdruecklich
            # als richtig aus. Die Vorfassung verlangte pauschal eine
            # Matrixzeile und meldete den dokumentierten Normalfall als Defekt.
            # Der Check heisst "ohne BEZUG", nicht "ohne Matrixzeile".
            ref_text = ent["notes"] + " " + ent["title"]
            contra_refs = [c for c in re.findall(r"CONTRA-\d{3}", ref_text)
                           if c in reg_index]
            if not contra_refs:
                ev_orphan.append({"id": v, "problem":
                                  "in der Kernmatrix nicht verknuepft und kein "
                                  "Widerspruchsbezug"})
    res.add("C5d", "0 EV ohne Bezug", not ev_orphan,
            "%d EV geprueft, %d ohne Bezug" % (len(evs), len(ev_orphan)),
            ev_orphan)

    # 1:1-Kopplung REQ <-> AC <-> EV
    #
    # BEFUND/FIX (2026-07-20): Die Vorfassung prueft NUMERISCHE GLEICHHEIT —
    # REQ-0nn muesse an AC-0nn und EV-0nn haengen. Das war nie die Anforderung,
    # sondern eine Beobachtung aus der Zeit, als die drei Raeume im Gleichschritt
    # wuchsen. Seit AC-041 (Aufteilung von AC-019) und EV-041/EV-042 laufen die
    # Nummernkreise auseinander; die Registry weist das ausdruecklich als
    # RICHTIG aus (AC = REQ+1, EV = REQ+2). Die Pruefung meldete daraufhin
    # REQ-041 -> AC-042/EV-043 als Defekt: ein korrekter Dokumentenstand,
    # beanstandet von einer Pruefung, die eine Zufaelligkeit fuer eine Regel
    # hielt.
    #
    # Die tragende Aussage ist die BIJEKTION: jedes Requirement hat genau ein
    # AC und genau ein EV, und kein AC/EV haengt an zwei Requirements. Das wird
    # jetzt geprueft — die Nummer ist dabei belanglos.
    mismatch = []
    ac_owner, ev_owner = {}, {}
    for r in trace_rows:
        if not r["req"]:
            continue
        if not r["ac"]:
            mismatch.append({"trc": r["trc"], "req": r["req"],
                             "problem": "kein Acceptance Criterion verknuepft"})
        if not r["ev"]:
            mismatch.append({"trc": r["trc"], "req": r["req"],
                             "problem": "kein Evidence-Eintrag verknuepft"})
        for val, owner, kind in ((r["ac"], ac_owner, "AC"), (r["ev"], ev_owner, "EV")):
            if not val:
                continue
            if val in owner and owner[val] != r["req"]:
                mismatch.append({"trc": r["trc"], "problem":
                                 "%s %s haengt an zwei Requirements: %s und %s"
                                 % (kind, val, owner[val], r["req"])})
            owner[val] = r["req"]
    res.add("C5e",
            "1:1-Kopplung REQ <-> AC <-> EV in der Kernmatrix (Bijektion, "
            "NICHT Nummerngleichheit — die Nummernkreise laufen belegt auseinander)",
            not mismatch,
            "%d Requirement-Zeilen geprueft, %d Abweichungen; %d AC und %d EV "
            "eindeutig zugeordnet"
            % (len([r for r in trace_rows if r["req"]]), len(mismatch),
               len(ac_owner), len(ev_owner)),
            mismatch,
            note="Nummerngleichheit war eine Beobachtung, keine Anforderung. "
                 "AC-041 (Aufteilung von AC-019) und EV-041/EV-042 machen sie "
                 "unmoeglich; die Registry weist das als richtig aus.")

    # PRD-Bloecke ohne Registry-REQ
    stray = [{"id": k, "problem": "Messmodell-Block ohne aktiven Registry-Eintrag"}
             for k in sorted(prd_blocks) if k not in reqs]
    res.add("C5f", "0 Messmodell-Bloecke ohne Registry-Requirement", not stray,
            "%d PRD-Bloecke, %d ohne Registry-Eintrag" % (len(prd_blocks), len(stray)),
            stray)


# ---------------------------------------------------------------------------
# C6b — KANONISCHE DEFINITION (verbindlich fuer Validator UND Generator)
# ---------------------------------------------------------------------------
C6B_DEFINITION = {
    "grundgesamtheit": "ALLE in docs/ID-REGISTRY.md unter der kanonischen "
                       "ID-Definitionskopfzeile gefuehrten CONTRA-IDs — sowohl "
                       "status=open als auch status=resolved. Keine ID wird "
                       "ausgeschlossen, auch CONTRA-006 nicht.",
    "verglichene_achse": "AUSSCHLIESSLICH das kanonische Feld `status` "
                         "(open|resolved) aus Registry §6.11 gegen den "
                         "Statuswert der Widerspruchstabelle in "
                         "docs/decisions/decision-log.md.",
    "nicht_verglichen": "evidence_status, resolution_status, blocking, "
                        "blocked_gates und blocked_activities sind EIGENE "
                        "Achsen und erzeugen KEINE "
                        "C6b-Divergenz. Ein `resolved` mit `evidence_status = "
                        "pending` ist kein Widerspruch, sondern der Normalfall. "
                        "Der Achsengleichlauf wird getrennt in C6c geprueft.",
    "contra_006": "CONTRA-006 ist Teil der Grundgesamtheit und wird gezaehlt "
                  "wie jede andere ID. Es zaehlt als Divergenz genau dann, "
                  "wenn seine `status`-Werte auseinanderfallen — nicht deshalb, "
                  "weil seine Evidence aussteht. Die frueheren Zaehlstaende 2 "
                  "und 3 unterschieden sich genau hier: der eine Pruefer "
                  "verglich nur `status`, der andere zaehlte den unzulaessigen "
                  "Mischwert DESIGN-RESOLVED/EVIDENCE-PENDING mit.",
    "getrennte_ausweisung": "open und resolved werden getrennt ausgewiesen.",
    "blocking": "blocking wird NIE aus einer Tabelle uebernommen und NIE je ID "
                "hartkodiert, sondern nach der kanonischen C16-Formel aus "
                "status, resolution_status, evidence_status, blocked_gates, "
                "blocked_activities, dem geprueften Gate und der geprueften "
                "Taetigkeit abgeleitet — durch die EINZIGE Implementierung in "
                "blocking_model.derive_blocking().",
}

# Normalisierung des Ledger-Statuswerts auf die Achse `status`.
# Der Ledger schreibt "`resolved` (Entscheidung Nutzer 2026-07-19) — Achsen ...".
# Die Vorfassung pruefte `.startswith("resolved")` auf dem ROHSTRING und sah
# wegen des fuehrenden Backticks drei Divergenzen, die keine waren.
def normalize_status_token(value):
    v = _clean(value).lower()
    m = re.match(r"^(open|resolved)\b", v)
    if m:
        return m.group(1)
    for bad in FORBIDDEN_STATUS_VALUES:
        if v.startswith(bad):
            return bad
    return v.split("(")[0].split("—")[0].strip() or "MISSING"


def parse_ledger_status(ledger_text):
    """Statuswert je CONTRA-ID aus der Widerspruchstabelle des Ledgers."""
    rows = {}
    in_table = False
    prev = None
    for line in ledger_text.split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            in_table = False
            prev = None
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and all(set(c) <= set("-: ") and c for c in cells):
            in_table = bool(prev) and prev[0] == "id" and prev[-1] == "status"
            prev = None
            continue
        prev = _header_cells(line)
        if not in_table:
            continue
        cid = _clean(cells[0])
        if re.match(r"^CONTRA-\d{3}$", cid):
            rows[cid] = cells[-1]
    return rows


def check_contradictions(res, entries, ledger_text, reg_text, repo, files):
    contras = [e for e in entries if e["prefix"] == "CONTRA"]
    ledger_rows = parse_ledger_status(ledger_text)
    reg_axes = parse_contra_axes(reg_text)
    led_axes = parse_contra_axes(ledger_text)

    # ---- C6a: Ledger-Eintrag vorhanden ----
    missing_entry = [{"id": e["id"], "registry_status": e["status"],
                      "problem": "kein Ledger-Eintrag in %s" % DECISION_LOG}
                     for e in contras if e["id"] not in ledger_rows]
    res.add("C6a", "0 ungeloeste Contradictions ohne Ledger-Eintrag",
            not missing_entry,
            "%d Contradictions, %d ohne Ledger-Eintrag"
            % (len(contras), len(missing_entry)),
            missing_entry)

    # ---- C6b: Statusgleichlauf, kanonisch definiert ----
    divergence = []
    by_status = defaultdict(list)
    for e in contras:
        reg_st = normalize_status_token(e["status"])
        by_status[reg_st].append(e["id"])
        raw = ledger_rows.get(e["id"])
        if raw is None:
            continue                      # bereits von C6a gemeldet
        led_st = normalize_status_token(raw)
        if reg_st != led_st:
            divergence.append({"id": e["id"], "registry_status": reg_st,
                               "ledger_status": led_st,
                               "ledger_raw": _clean(raw)[:120],
                               "problem": "Statusdivergenz auf der Achse `status`"})
    res.add("C6b",
            "Statusgleichlauf Registry <-> Widerspruchs-Ledger auf der Achse "
            "`status` (kanonische Definition, siehe C6B_DEFINITION)",
            not divergence,
            "%d Contradictions in der Grundgesamtheit (open=%d, resolved=%d), "
            "%d Statusdivergenzen; CONTRA-006 ist enthalten und divergiert %s"
            % (len(contras), len(by_status.get("open", [])),
               len(by_status.get("resolved", [])), len(divergence),
               "ja" if any(d["id"] == "CONTRA-006" for d in divergence) else "nicht"),
            divergence,
            note="Kanonische Definition: " + json.dumps(C6B_DEFINITION, ensure_ascii=False))

    # ---- C6c: Achsengleichlauf Registry §6.11.1 <-> Ledger-Statusmodell ----
    # BEFUND: Die beiden Tabellen fuehren dieselben zehn Felder in
    # UNTERSCHIEDLICHER Spaltenreihenfolge. Der frueher positionsbasierte Parser
    # las den Ledger deshalb ueberhaupt nicht (0 Zeilen) — C6c, C6d und C16
    # bestanden auf der LEEREN Menge. Ein Pass auf der leeren Menge belegt
    # nichts. Der Parser ist jetzt spaltennamenbasiert; die abweichende
    # Reihenfolge wird als eigener Befund ausgewiesen, nicht weggeglaettet.
    axis_div = []
    AXIS_FIELDS = ("status", "resolution_status", "evidence_status",
                   "blocked_gates", "blocked_activities", "evidence_gate")
    for cid in sorted(set(reg_axes) | set(led_axes)):
        r, l = reg_axes.get(cid), led_axes.get(cid)
        if r is None or l is None:
            axis_div.append({"id": cid, "problem":
                             "Statusmodell-Zeile fehlt in %s"
                             % (DECISION_LOG if l is None else REGISTRY)})
            continue
        for k in AXIS_FIELDS:
            if r[k] != l[k]:
                axis_div.append({"id": cid, "feld": k, "registry": r[k],
                                 "ledger": l[k], "problem": "Achsendivergenz"})
        # `blocking` getrennt: der Ledger schreibt es als Prosa.
        if r["blocking_recorded"] is not None and l["blocking_recorded"] is not None:
            if r["blocking_recorded"] != l["blocking_recorded"]:
                axis_div.append({"id": cid, "feld": "blocking",
                                 "registry": r["blocking_recorded"],
                                 "ledger": l["blocking_recorded"],
                                 "problem": "Achsendivergenz"})
    prosa = sorted(cid for cid, ax in led_axes.items()
                   if ax["blocking_recorded"] is None)
    order_note = ""
    orders = {json.dumps(ax["header_order"], ensure_ascii=False)
              for ax in list(reg_axes.values())[:1] + list(led_axes.values())[:1]}
    if len(orders) > 1:
        order_note = ("BEFUND: Registry und Ledger fuehren dieselben Felder in "
                      "unterschiedlicher SPALTENREIHENFOLGE. Sachlich kein "
                      "Unterschied, aber der Grund, warum ein positionsbasierter "
                      "Parser den Ledger vorher gar nicht las. ")
    res.add("C6c",
            "Achsengleichlauf Registry §6.11.1 <-> decision-log.md "
            "(status, resolution_status, evidence_status, blocked_gates, "
            "blocked_activities, evidence_gate, blocking)",
            not axis_div,
            "%d CONTRA-IDs mit Statusmodell in beiden Dateien, %d Achsendivergenzen"
            % (len(set(reg_axes) & set(led_axes)), len(axis_div)),
            axis_div,
            note=order_note + ("`blocking` ist im Ledger fuer %s als Prosa "
                               "notiert (enthaelt true UND false) und dort nicht "
                               "maschinell vergleichbar; es wird NICHT auf einen "
                               "Wert geraten. Die Sachaussage ist ueber die "
                               "uebrigen Achsen vollstaendig geprueft."
                               % (", ".join(prosa) or "keine ID")))

    # ---- C6d: blocking ABGELEITET statt uebernommen ----
    mismatch, outcomes = [], {}
    for cid in sorted(reg_axes):
        ax = reg_axes[cid]
        try:
            derived, reasons = derive_blocking(ax)
        except BM.VocabularyViolation as exc:
            # Ein Vokabularverstoss macht die Ableitung unzulaessig. Er wird
            # als Befund gemeldet — der Lauf darf daran nicht abbrechen, sonst
            # verschwindet mit dem Absturz auch C16.
            mismatch.append({"id": cid, "problem": "blocking nicht ableitbar: %s"
                             % exc})
            derived, reasons = True, [str(exc)]
        outcomes[cid] = {"blocking_derived": derived,
                         "reasons": reasons,
                         "outcome": classify_contra(ax, derived),
                         "evidence_gate": ax["evidence_gate"],
                         "blocked_gates": ax["blocked_gates"],
                         "blocked_activities": ax["blocked_activities"],
                         "evidence_status": ax["evidence_status"]}
        recorded = ax["blocking_recorded"]
        if recorded is None:
            mismatch.append({"id": cid, "eingetragen": ax["blocking_verbatim"][:80],
                             "abgeleitet": str(derived).lower(),
                             "problem": "eingetragener blocking-Wert ist nicht "
                                        "eindeutig (true UND false in derselben Zelle)"})
        elif derived != recorded:
            mismatch.append({"id": cid, "eingetragen": str(recorded).lower(),
                             "abgeleitet": str(derived).lower(),
                             "klauseln": reasons,
                             "problem": "eingetragener blocking-Wert weicht von "
                                        "der kanonischen Ableitung ab"})
    klassen = defaultdict(int)
    for v in outcomes.values():
        klassen[v["outcome"]] += 1
    res.add("C6d",
            "`blocking` ist aus den Achsen ABGELEITET und stimmt mit dem "
            "eingetragenen Wert ueberein (eine einzige Implementierung, "
            "keine ID-spezifische Sonderregel)",
            not mismatch and len(reg_axes) > 0,
            "%d CONTRA-IDs abgeleitet, %d Abweichungen; Ergebnisklassen: %s"
            % (len(reg_axes), len(mismatch),
               ", ".join("%s=%d" % (k, klassen[k]) for k in sorted(klassen))
               or "keine"),
            mismatch,
            note="Ableitung aus %s. Grundgesamtheit > 0 ist Bestehensbedingung: "
                 "ein Pass auf der leeren Menge belegt nichts. Ergebnisklassen "
                 "je ID: %s"
                 % (BM.MODEL_PROVENANCE["module"],
                    json.dumps({k: v["outcome"] for k, v in sorted(outcomes.items())},
                               ensure_ascii=False)))

    # ---- C6e: keine unzulaessigen Statuswerte ----
    bad_status = []
    for e in contras:
        v = _clean(e["status"]).lower()
        if v in FORBIDDEN_STATUS_VALUES or v not in STATUS_VALUES:
            bad_status.append({"id": e["id"], "wert": e["status"], "datei": REGISTRY,
                               "problem": "unzulaessiger `status`-Wert (Registry §3.1)"})
    for cid, raw in sorted(ledger_rows.items()):
        v = normalize_status_token(raw)
        if v not in STATUS_VALUES:
            bad_status.append({"id": cid, "wert": v, "datei": DECISION_LOG,
                               "problem": "unzulaessiger `status`-Wert (Registry §3.1)"})
    for src, axes in ((REGISTRY, reg_axes), (DECISION_LOG, led_axes)):
        for cid, ax in sorted(axes.items()):
            if ax["status"] not in STATUS_VALUES:
                bad_status.append({"id": cid, "wert": ax["status"], "datei": src,
                                   "problem": "unzulaessiger `status`-Wert"})
            if ax["resolution_status"] not in RESOLUTION_VALUES:
                bad_status.append({"id": cid, "wert": ax["resolution_status"],
                                   "datei": src,
                                   "problem": "unzulaessiger `resolution_status`-Wert"})
            if ax["evidence_status"] not in EVIDENCE_VALUES:
                bad_status.append({"id": cid, "wert": ax["evidence_status"],
                                   "datei": src,
                                   "problem": "unzulaessiger `evidence_status`-Wert"})
    res.add("C6e",
            "0 ungueltige Registry-Statuswerte (DESIGN-RESOLVED, EVIDENCE-PENDING, "
            "pending, closed, mitigated sind als `status` unzulaessig)",
            not bad_status,
            "%d CONTRA-Statuswerte in Registry, Ledger und beiden Statusmodell-"
            "Tabellen geprueft, %d unzulaessig"
            % (len(contras) + len(ledger_rows) + 3 * (len(reg_axes) + len(led_axes)),
               len(bad_status)),
            bad_status,
            note="Der frueher offene Wertebereich von `blocking_scope` ist "
                 "gegenstandslos: das Feld ist entfallen. Die vier strittigen "
                 "Werte (competition-release, territory-release, "
                 "database-schema-finalization, account-release) sind regulaere "
                 "Mitglieder von `blocked_activities`. Geprueft wird das in C16.")

    # ---- C16: 0 Gate-vs-Taetigkeit-Vergleiche ----
    # Der Check hat seine Frage GEWECHSELT, weil die Nutzerentscheidung den
    # Defekt behoben hat. Frueher: "existiert eine Abbildung Gate -> Taetigkeit?"
    # (sie existierte nicht, und sie zu erfinden war verboten). Jetzt: die
    # Abbildung wird nicht mehr gebraucht, weil die Vokabulare getrennt sind —
    # geprueft wird, dass NIRGENDS mehr ein Gate gegen eine Taetigkeit
    # verglichen wird und dass kein Wert im falschen Feld steht.
    c16 = []
    for src, axes in ((REGISTRY, reg_axes), (DECISION_LOG, led_axes)):
        for cid, ax in sorted(axes.items()):
            for v in BM.check_vocabulary(ax):
                v["datei"] = src
                c16.append(v)
    for rel in files:
        if not rel.endswith(".md"):
            continue
        for f in BM.scan_gate_vs_activity_comparisons(read(repo, rel)):
            f["datei"] = rel
            c16.append(f)
    # Das lebende Feld `blocking_scope` ist selbst ein C16-Verstoss.
    for rel in files:
        if not rel.endswith(".md"):
            continue
        for lineno, line in enumerate(read(repo, rel).split("\n"), 1):
            if BM._is_historical(line):
                continue          # beschreibt die Abschaffung, ist sie nicht
            if re.search(r"\|\s*`?blocking_scope`?\s*\|", line) or \
               re.search(r"`blocking_scope`?\s*(?:=|:)\s*\[", line):
                c16.append({"datei": rel, "line": lineno, "feld": "blocking_scope",
                            "problem": "abgeschafftes Feld `blocking_scope` wird "
                                       "noch als Feld verwendet (C16)",
                            "text": norm(line)[:140]})
    res.add("C16",
            "0 Gate-vs-Taetigkeit-Vergleiche: `current_gate` wird ausschliesslich "
            "gegen `blocked_gates` geprueft, `current_activity` ausschliesslich "
            "gegen `blocked_activities`; kein Wert steht im falschen Feld",
            not c16,
            "%d CONTRA-Statusmodellzeilen und %d Markdown-Dateien geprueft, "
            "%d Vermischungen; Vokabulare disjunkt: %s"
            % (len(reg_axes) + len(led_axes),
               len([f for f in files if f.endswith(".md")]), len(c16),
               "ja" if not (GATES & ACTIVITIES) else "NEIN"),
            c16,
            note="`blocking_scope` ist ersatzlos entfallen (C16, Nutzer"
                 "entscheidung 2026-07-19). Eine Abbildung Gate -> Taetigkeit "
                 "wird nicht mehr gebraucht und wurde NICHT erfunden — der "
                 "Defekt ist durch Trennung der Vokabulare behoben, nicht durch "
                 "eine ergaenzte Tabelle. Formel: " + BM.FORMULA_TEXT)

    return contras, ledger_rows, reg_axes, outcomes


def check_research_plans(res, prd_blocks):
    """Jede RESEARCH_HYPOTHESIS braucht einen Forschungsplan; ohne ihn waere
    'measurement_type = RESEARCH_HYPOTHESIS' eine leere Etikettierung."""
    rh, missing = [], []
    for rid in sorted(prd_blocks):
        mt = norm(prd_blocks[rid]["fields"].get("measurement_type", ""))
        if "RESEARCH_HYPOTHESIS" not in mt:
            continue
        rh.append(rid)
        if "**research_plan**" not in prd_blocks[rid]["body"]:
            missing.append({"id": rid, "problem": "RESEARCH_HYPOTHESIS ohne research_plan"})
    res.add("C8", "Jede RESEARCH_HYPOTHESIS traegt einen Forschungsplan",
            not missing,
            "%d RESEARCH_HYPOTHESIS-REQs, %d ohne Forschungsplan" % (len(rh), len(missing)),
            missing)


# ---------------------------------------------------------------------------
# NFR-Audit, Herkunft/Nachweis-Trennung, Vererbung, Vision-Anker
# ---------------------------------------------------------------------------

def parse_nfr_blocks(text):
    """### NFR-00x — Titel  +  | Feld | Wert |-Tabelle.

    ZWEI BEFUNDE/FIXES (2026-07-20):

    (a) BLOCKGRENZE. Die Vorfassung liess einen Block bis zum naechsten
        NFR-Kopf laufen — und den letzten bis zum DATEIENDE. Der letzte
        NFR-008-Abschnitt verschluckte dadurch den halben Rest des PRD samt
        fremder Feld/Wert-Tabellen. So kam NFR-008 zu einem `source_type`
        "ASSUMPTION FUER DAS REQUIREMENT", der in seinem Abschnitt gar nicht
        steht: ein Wert aus einer voellig anderen Tabelle, syntaktisch
        gueltig und sachlich falsch. Die Grenze ist jetzt die naechste
        `###`-Ueberschrift GLEICH WELCHER ID.

    (b) ERSTE STATT LETZTE. Das PRD fuehrt drei Ueberschriften `### NFR-008 —`
        (Definition, Entscheidung 2026-07-19, Runde 4 2026-07-20). Die
        Vorfassung liess die LETZTE gewinnen — also einen Kommentarabschnitt
        ohne Messfelder. Der Validator meldete daraufhin `evidence_status` und
        die Mess-/Kontrollmethode als fehlend, obwohl beide im
        Definitionsabschnitt stehen. Kanonisch ist die ERSTE Ueberschrift;
        spaetere sind Entscheidungs- und Kommentarabschnitte und werden als
        `weitere_abschnitte` gefuehrt, nicht verrechnet.
    """
    blocks = {}
    heads = list(re.finditer(r"^###\s+(NFR-\d{3})\s*[—–-]\s*(.+)$", text, re.M))
    all_heads = [m.start() for m in re.finditer(r"^###\s+", text, re.M)]
    for i, h in enumerate(heads):
        nxt = [p for p in all_heads if p > h.start()]
        end = nxt[0] if nxt else len(text)
        body = text[h.end():end]
        fields = {}
        for line in body.split("\n"):
            s = line.strip()
            if not s.startswith("|"):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) != 2:
                continue
            key = norm(cells[0]).lower().strip("*` ")
            if key in ("feld", "field", "") or set(key) <= set("-: "):
                continue
            fields[key] = cells[1]
        nid = h.group(1)
        entry = {"title": norm(h.group(2)), "fields": fields, "body": body,
                 "lineno": text[:h.start()].count("\n") + 1}
        if nid in blocks:
            blocks[nid].setdefault("weitere_abschnitte", []).append(
                {"title": entry["title"], "lineno": entry["lineno"]})
            continue                      # ERSTE gewinnt, nicht letzte
        blocks[nid] = entry
    return blocks


# Feldnamen, die eine Mess- oder Kontrollmethode benennen.
NFR_METHOD_KEYS = ["testmethode", "mess-/kontrollmethode", "kontrollmethode",
                   "messmethode", "pruefverfahren"]
NFR_REQUIRED = {
    "source_type": ["source_type"],
    "evidence_status": ["evidence_status"],
    "mess-/kontrollmethode": NFR_METHOD_KEYS,
    "owner": ["owner"],
    "release_gate": ["release_gate"],
}


def _first(fields, keys):
    for k in keys:
        if k in fields:
            return fields[k]
    return None


def _leading_token(value, vocabulary):
    """Fuehrender Achsenwert eines Feldes, z. B. `pending` aus
    '**`pending`** fuer die pruefbaren Klauseln — …'. Gibt None zurueck, wenn
    das Feld mit keinem zulaessigen Wert des Vokabulars beginnt."""
    v = _clean(value).strip().lower()
    for tok in sorted(vocabulary, key=len, reverse=True):
        if re.match(r"^%s\b" % re.escape(tok), v):
            return tok
    return None


# Felder, deren Wert einem geschlossenen Vokabular folgen MUSS. Ein beliebiger
# Fliesstext genuegt hier nicht — sonst zaehlt "— nicht `pending`." als
# vorhandener Achsenwert, und die Pruefung waere stumpf.
NFR_VOCABULARY = {
    "source_type": {"explicit", "assumption", "missing", "blocker", "contradiction"},
    "evidence_status": EVIDENCE_VALUES,
}


def check_nfrs(res, nfr_blocks):
    findings, complete = [], 0
    owner_blockers = []
    for nid in sorted(nfr_blocks):
        f = nfr_blocks[nid]["fields"]
        missing = []
        for label, keys in NFR_REQUIRED.items():
            val = _first(f, keys)
            if val is None:
                missing.append("%s (Feld fehlt)" % label)
                continue
            v = _clean(val)
            if not v or (v.lower() in NULLISH and not is_justified(v)):
                missing.append("%s (leer/unbegruendet)" % label)
                continue
            if label in NFR_VOCABULARY:
                # BEFUND aus der Negativkontrolle: die Vorfassung akzeptierte
                # JEDEN nichtleeren Text. Ein geleertes evidence_status-Feld,
                # dessen Resttext zufaellig lang genug war, lief als
                # "vorhanden" durch. Jetzt muss der FUEHRENDE Wert aus dem
                # Vokabular stammen.
                if _leading_token(v, NFR_VOCABULARY[label]) is None:
                    missing.append("%s (kein gueltiger Achsenwert am Feldanfang: %r)"
                                   % (label, v[:40]))
        owner = _clean(_first(f, ["owner"]) or "")
        if owner and is_justified(owner):
            owner_blockers.append(nid)
        if missing:
            findings.append({"id": nid, "problem": ", ".join(missing)})
        else:
            complete += 1
    res.add("C9",
            "8/8 NFRs mit source_type, evidence_status, Mess-/Kontrollmethode, "
            "Owner-oder-sichtbarem-Owner-Blocker und Release Gate",
            complete == 8 and len(nfr_blocks) == 8 and not findings,
            "%d/%d NFR-Bloecke vollstaendig; davon %d mit sichtbarem "
            "OWNER-BLOCKER statt DRI" % (complete, len(nfr_blocks), len(owner_blockers)),
            findings,
            note="Ein ausdruecklich als MISSING/BLOCKER gekennzeichneter Wert gilt "
                 "als vorhanden-und-begruendet, NICHT als erfuellt. NFR-008 traegt "
                 "release_gate = MISSING: das ist ein sichtbarer Befund, keine "
                 "stille Luecke.")
    return owner_blockers


# Formulierungen, mit denen ein Artefakt selbst einraeumt, dass keine Quelle
# existiert. Steht so etwas neben source_type = EXPLICIT, ist das ein Defekt.
NO_SOURCE_MARKERS = ["keine gefunden", "keine quelle", "kein artefakt nennt",
                     "ohne quellenangabe", "ohne quelle", "nicht empirisch belegt",
                     "missing"]
# Belege, die die Beweislatte fuer EXPLICIT tragen koennen.
SOURCE_EVIDENCE = re.compile(
    r"(user-confirmed|CONFIRMED|DEC-\d{3}|SRC-\d{3}|CAN-\d{3})")


def _source_type_head(value):
    v = _clean(value)
    return re.split(r"[—–(]", v)[0].strip().upper()


def check_source_types(res, prd_blocks, nfr_blocks):
    """C10 — 0 unbelegte Zielwerte mit source_type EXPLICIT.
    C11 — 0 Verwechslungen zwischen Herkunft und Nachweis.
    C12 — 0 automatische Source-Type-Vererbungen."""
    unbacked, confusion, inherited = [], [], []
    checked_explicit = 0

    def source_field(fields):
        for k in ("quelle des zielwerts", "quelle", "source"):
            if k in fields:
                return fields[k]
        return None

    items = ([(k, v, "REQ") for k, v in sorted(prd_blocks.items())] +
             [(k, v, "NFR") for k, v in sorted(nfr_blocks.items())])

    for iid, blk, kind in items:
        f = blk["fields"]
        st_raw = f.get("source_type")
        if st_raw is None:
            continue
        head = _source_type_head(st_raw)
        st_clean = _clean(st_raw)
        low = st_clean.lower()

        # --- C11: Achsen nicht vermischen ---
        if head.lower() in EVIDENCE_VALUES or head.lower() in FORBIDDEN_STATUS_VALUES:
            confusion.append({"id": iid, "feld": "source_type", "wert": head,
                              "problem": "Nachweis-Wert im Herkunftsfeld "
                                         "(source_type traegt einen evidence_status)"})
        ev_raw = f.get("evidence_status")
        if ev_raw is not None:
            ev_head = _clean(ev_raw)
            ev_head = re.split(r"[—–(]", ev_head)[0].strip().lower()
            if ev_head in ("explicit", "assumption", "contradiction"):
                confusion.append({"id": iid, "feld": "evidence_status",
                                  "wert": ev_head,
                                  "problem": "Herkunfts-Wert im Nachweisfeld"})
            elif ev_head and ev_head not in EVIDENCE_VALUES and not is_justified(ev_head):
                confusion.append({"id": iid, "feld": "evidence_status",
                                  "wert": ev_head,
                                  "problem": "unzulaessiger evidence_status-Wert"})

        if head != "EXPLICIT":
            continue
        checked_explicit += 1

        # --- C10: EXPLICIT braucht einen Beleg ---
        # BEFUND aus der Negativkontrolle: die Vorfassung setzte hier ein
        # `continue`. Eine Zeile, die C10 verletzt, wurde dadurch von C12 GAR
        # NICHT MEHR GEPRUEFT — der schwerere Befund verdeckte den leichteren.
        # C10 und C12 werden jetzt unabhaengig voneinander ausgewertet.
        src = source_field(f)
        haystack = "%s %s" % (st_clean, _clean(src) if src else "")
        if not SOURCE_EVIDENCE.search(haystack):
            unbacked.append({"id": iid, "kind": kind,
                             "source_type": head,
                             "quelle": (_clean(src)[:120] if src
                                        else "FELD 'Quelle des Zielwerts' FEHLT"),
                             "problem": "source_type EXPLICIT ohne jeden Beleg "
                                        "(weder user-confirmed noch DEC-/SRC-/CAN-Bezug)"})
        elif src is not None:
            s_low = _clean(src).lower()
            if any(m in s_low for m in NO_SOURCE_MARKERS) and "gefunden —" not in s_low \
               and "gefunden -" not in s_low:
                unbacked.append({"id": iid, "kind": kind,
                                 "quelle": _clean(src)[:120],
                                 "problem": "source_type EXPLICIT, waehrend das "
                                            "Quellenfeld selbst 'keine Quelle' sagt"})

        # --- C12: keine automatische Vererbung ---
        # Ein quantitativer Zielwert wird NICHT dadurch EXPLICIT, dass eine
        # qualitative Vision-/Canvas-Absicht in dieselbe Richtung zeigt.
        # Mechanisch: EXPLICIT, dessen Beleg AUSSCHLIESSLICH aus VIS-/CAN-Items
        # ohne bestaetigte Entscheidung (DEC-/SRC-/user-confirmed/CONFIRMED)
        # besteht, ist eine stille Hochstufung.
        strong = re.search(r"(user-confirmed|CONFIRMED|DEC-\d{3}|SRC-\d{3})", haystack)
        weak = re.search(r"(VIS-\d{3}|CAN-\d{3})", haystack)
        if weak and not strong:
            inherited.append({"id": iid, "kind": kind,
                              "beleg": _clean(haystack)[:140],
                              "problem": "EXPLICIT allein aus einer qualitativen "
                                         "VIS-/CAN-Absicht abgeleitet — "
                                         "automatische Source-Type-Vererbung"})

    res.add("C10", "0 unbelegte Zielwerte mit source_type EXPLICIT",
            not unbacked,
            "%d EXPLICIT-Zeilen in PRD-Requirements und NFR-Bloecken geprueft, "
            "%d ohne Beleg" % (checked_explicit, len(unbacked)),
            unbacked,
            note="Beweislatte (PRD): (a) Nutzer hat den Wert bestaetigt, "
                 "(b) belegte Nutzerquelle, (c) konkret zitierte externe Regel. "
                 "Mechanisch geprueft wird das Vorhandensein eines Belegbezugs "
                 "(user-confirmed | CONFIRMED | DEC- | SRC- | CAN-) im Feld "
                 "`source_type` oder `Quelle des Zielwerts`.")
    res.add("C11",
            "0 Verwechslungen zwischen Herkunft (source_type) und Nachweis "
            "(evidence_status)",
            not confusion,
            "%d Requirement- und NFR-Bloecke auf Achsenvermischung geprueft, "
            "%d Verwechslungen" % (len(items), len(confusion)),
            confusion)
    res.add("C12", "0 automatische Source-Type-Vererbungen",
            not inherited,
            "%d EXPLICIT-Zeilen geprueft, %d allein aus einer qualitativen "
            "VIS-/CAN-Absicht hochgestuft" % (checked_explicit, len(inherited)),
            inherited)


def check_hardcoded_blocking(res, tool_files):
    """C14 — das Pruefwerkzeug selbst darf `blocking` nicht je ID verdrahten.
    Registry §3.1: 'Ein Pruefwerkzeug, das blocking fuer eine bestimmte ID fest
    verdrahtet, ist selbst der Defekt.'"""
    findings = []
    pat = re.compile(
        r"""(?ix)
        (?:blocking[^\n]{0,80}(?:==|!=|\bis\b)[^\n]{0,20}["']CONTRA-\d{3}["']
        | ["']?id["']?\s*(?:==|!=)\s*["']CONTRA-\d{3}["'][^\n]{0,80}blocking
        | blocking["']?\s*:\s*[^\n,]{0,40}["']CONTRA-\d{3}["']
        | ["']CONTRA-\d{3}["'][^\n]{0,60}blocking\s*=)
        """)
    for path in tool_files:
        if not os.path.isfile(path):
            continue
        for lineno, line in enumerate(open(path, encoding="utf-8"), 1):
            if line.lstrip().startswith("#"):
                continue          # Kommentare beschreiben den Defekt, sind keiner
            if pat.search(line):
                findings.append({"file": os.path.basename(path), "line": lineno,
                                 "text": norm(line)[:140],
                                 "problem": "hartkodierter Blocking-Sonderfall "
                                            "fuer eine einzelne CONTRA-ID"})
    res.add("C14",
            "0 hartkodierte Blocking-Sonderfaelle im Pruefwerkzeug "
            "(Registry §3.1: blocking ist abgeleitet, nie je ID verdrahtet)",
            not findings,
            "%d Werkzeugdateien geprueft, %d hartkodierte Sonderfaelle"
            % (len(tool_files), len(findings)),
            findings)


# Formulierungen, mit denen ein Artefakt einen Vision-Anker als fachlich
# unpassend AUSWEIST. Daraus wird die Menge der dokumentiert falschen Paare
# abgeleitet — sie ist nicht im Validator abgetippt.
#
# Jeder Marker traegt eine RICHTUNG. Das ist der Kern der Praezision:
#   "before" — der Marker qualifiziert die zuletzt genannte ID
#              ("VIS-009 … — fachlich falsch")
#   "after"  — der Marker leitet die ID ein
#              ("hing an VIS-009", "Ersetzt VIS-009")
# Ohne Richtung greift die Beanstandung auf die daneben stehende KORREKTE ID
# ueber; genau so meldete die Vorfassung REQ-014 -> VIS-011 als Fehlanker.
WRONG_ANCHOR_MARKERS = {
    "fachlich falsch": "before",
    "fachlich unpassend": "before",
    "semantisch falsch": "before",
    "null überschneidung": "before",
    "null ueberschneidung": "before",
    "haben keine gemeinsame aussage": "before",
    "hing an": "after",
    "hängte": "after",
    "haengte": "after",
    "ersetzt vis-": "after",
}


# Der beanstandete Anker steht dicht am Beanstandungswort. Diese Naehe ist die
# Regel — nicht "das erste VIS-Item in der Zeile".
WRONG_ANCHOR_WINDOW = 60


def collect_documented_wrong_anchors(repo, files):
    """Liest aus den Artefakten selbst, welche REQ->VIS-Paare dort als fachlich
    falsch ausgewiesen sind. Kein Paar ist im Validator hartkodiert.

    BEFUND/FIX: Die Vorfassung nahm das ERSTE VIS-Item der Zeile. Damit meldete
    sie `docs/ID-REGISTRY.md:905` ("VIS-011 … vergeben, weil REQ-014 an einem
    semantisch falschen Anker hing") als Fehlanker REQ-014 -> VIS-011 — also
    ausgerechnet den KORRIGIERTEN Anker als den falschen. Das war ein
    Fehlalarm meines Prueflaufs, kein Dokumentdefekt. Jetzt zaehlt nur ein
    VIS-Item, das innerhalb von %d Zeichen um das Beanstandungswort steht;
    zusaetzlich wird eine Anlage-Formulierung ("vergeben", "angelegt", "neu")
    zwischen ID und Beanstandungswort ausgeschlossen.
    """ % WRONG_ANCHOR_WINDOW
    pairs = {}
    vis_rx = re.compile(r"(?<![A-Za-z0-9_-])VIS-(\d{3})")
    for rel in files:
        if not rel.endswith(".md"):
            continue
        for lineno, line in enumerate(read(repo, rel).split("\n"), 1):
            low = line.lower()
            reqs = re.findall(r"(?<![A-Za-z0-9_-])REQ-(\d{3})", line)
            if len(reqs) != 1:
                continue
            hits = [(m.start(), m.end(), m.group(1)) for m in vis_rx.finditer(line)]
            if not hits:
                continue
            for mk, direction in WRONG_ANCHOR_MARKERS.items():
                pos = low.find(mk)
                while pos >= 0:
                    end = pos + len(mk)
                    if direction == "before":
                        cand = [h for h in hits if h[1] <= end
                                and pos - h[1] <= WRONG_ANCHOR_WINDOW]
                        pick = cand[-1] if cand else None   # naechste davor
                    else:
                        cand = [h for h in hits if h[1] >= pos
                                and h[0] - pos <= WRONG_ANCHOR_WINDOW]
                        pick = cand[0] if cand else None    # naechste danach
                    if pick:
                        pairs.setdefault(("REQ-" + reqs[0], "VIS-" + pick[2]),
                                         []).append({"file": rel, "line": lineno,
                                                     "marker": mk,
                                                     "richtung": direction,
                                                     "text": norm(line)[:160]})
                    pos = low.find(mk, end)
    return pairs


def parse_prd_vision_anchors(text):
    """`Canvas: … · Vision: VIS-xxx` am Ende jedes Requirement-Blocks."""
    anchors = {}
    heads = list(re.finditer(r"^###\s+(REQ-\d{3})\s*[—–-]", text, re.M))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[h.end():end]
        m = re.search(r"^Canvas:.*$", body, re.M)
        if not m:
            continue
        vis_part = m.group(0).split("Vision:", 1)
        ids = re.findall(r"(?<![A-Za-z0-9_-])VIS-(\d{3})",
                         vis_part[1] if len(vis_part) > 1 else "")
        anchors[h.group(1)] = ["VIS-" + x for x in ids]
    return anchors


def check_vision_links(res, repo, files, prd_text, trace_rows, reg_index):
    """C15 — 0 semantisch falsche Vision-Verknuepfungen.
    Die als falsch bekannten Paare werden aus den Artefakten GELESEN, nicht
    im Validator gefuehrt. REQ-014 wird zusaetzlich namentlich nachgewiesen."""
    wrong = collect_documented_wrong_anchors(repo, files)
    anchors = parse_prd_vision_anchors(prd_text)

    # Traceability-Kernmatrix: Spalte 2 traegt das Vision Item.
    #
    # BEFUND/FIX (2026-07-20): Die Vorfassung sammelte JEDE VIS-ID aus der
    # Zelle. Eine Zelle, die mit `**MISSING — BLOCKER**` beginnt und danach
    # erklaert, WELCHER Anker entfernt wurde, meldete damit genau den
    # entfernten Anker als "weiterhin aktiven Link" — die Pruefung beanstandete
    # die Dokumentation der Entfernung. Bei TRC-032 stand die Entfernung und
    # ihre Beanstandung in derselben Zelle.
    #
    # STRUKTURELL, nicht vokabularbasiert: entscheidend ist die FUEHRENDE
    # Aussage der Zelle. Sagt sie `MISSING`/`BLOCKER`, behauptet die Zelle
    # keinen Anker; jede darin genannte VIS-ID ist Herkunft. Eine Zelle, die
    # eine ID nennt UND einen Anker behauptet, bleibt ein Verstoss.
    trace_anchor = {}
    for r in trace_rows:
        if not r["req"] or len(r["cells"]) < 3:
            continue
        cell = r["cells"][2]
        lead = re.sub(r"[`*~\s]", "", cell)[:16].upper()
        if lead.startswith("MISSING") or lead.startswith("BLOCKER"):
            trace_anchor[r["req"]] = []
            continue
        trace_anchor[r["req"]] = ["VIS-" + x for x in re.findall(
            r"(?<![A-Za-z0-9_-])VIS-(\d{3})", cell)]

    findings = []
    for (rid, vid), where in sorted(wrong.items()):
        live = []
        if vid in anchors.get(rid, []):
            live.append("%s (PRD-Ankerzeile)" % PRD)
        if vid in trace_anchor.get(rid, []):
            live.append("%s (Kernmatrix)" % TRACE)
        if live:
            findings.append({"req": rid, "vis": vid, "aktiv_in": live,
                             "dokumentiert_als_falsch_in": where[0],
                             "problem": "Vision-Anker ist in den Artefakten als "
                                        "fachlich falsch ausgewiesen, steht aber "
                                        "weiterhin als aktiver Link"})

    # Gezielte Nachpruefung REQ-014 — nicht als Sonderregel, sondern als
    # benannter Nachweis, dass der Check den real eingetretenen Fall trifft.
    req14 = {"prd_anker": anchors.get("REQ-014", []),
             "kernmatrix_anker": trace_anchor.get("REQ-014", []),
             "als_falsch_dokumentiert": sorted(
                 v for (r, v) in wrong if r == "REQ-014")}
    # Anker, die als ERFUELLT zaehlen: aktiv in der Registry und nicht als
    # unbestaetigt gekennzeichnet.
    unconfirmed = []
    for rid, vids in sorted(anchors.items()):
        for vid in vids:
            ents = reg_index.get(vid, [])
            if not ents:
                unconfirmed.append({"req": rid, "vis": vid,
                                    "problem": "VIS-ID nicht in der Registry"})
    res.add("C15",
            "0 semantisch falsche Vision-Verknuepfungen (dokumentiert falsche "
            "REQ->VIS-Paare stehen nirgends mehr als aktiver Link)",
            not findings and not unconfirmed,
            "%d in den Artefakten dokumentierte Fehlanker geprueft, %d davon noch "
            "aktiv; %d REQs mit Vision-Anker; REQ-014 gezielt nachgeprueft: %s"
            % (len(wrong), len(findings), len(anchors), json.dumps(req14, ensure_ascii=False)),
            findings + unconfirmed,
            note="Die Paarliste ist NICHT im Validator abgetippt. Sie wird aus "
                 "Saetzen der Artefakte selbst gewonnen ('fachlich falsch', "
                 "'fachlich unpassend', 'hing an', 'ersetzt VIS-', …). Ein neu "
                 "dokumentierter Fehlanker wird dadurch automatisch mitgeprueft. "
                 "Hinweis: VIS-011 ist `ASSUMPTION` und unbestaetigt und zaehlt "
                 "nach Registry §8 Punkt 15 NICHT als erfuellter Anker — das ist "
                 "ein eigener, offener Befund und kein C15-Verstoss.")


# ---------------------------------------------------------------------------
# Pruefungen, die in diesem Lauf ergaenzt wurden (Auftau-Schritt 2, C17..C27).
#
# Grundsatz fuer alle: die ID ist der GEGENSTAND der Pruefung und darf benannt
# werden; das ERGEBNIS wird nie hartkodiert. Jede ID wird gegen die Registry
# aufgeloest — existiert sie dort nicht, ist das ein Befund und kein Anlass,
# den Check zu ueberspringen.
# ---------------------------------------------------------------------------

CANVAS = "docs/canvas/revyr-endurance-platform.canvas.md"


def registry_entry(reg_index, rid):
    ents = reg_index.get(rid, [])
    return ents[0] if ents else None


def canvas_statements(repo, rid):
    """ALLE Aussage-Zellen (Spalte 2) zu einem Canvas-Item.

    Diese Trennung ist der Kern von C18 und C23: die Anmerkungsspalte
    BESCHREIBT die Abgrenzung ("der Designsystem-Anteil ist nach CAN-141
    ausgelagert", "ausdruecklich NICHT enthalten: …"). Wer sie mitliest,
    beanstandet die Abgrenzung selbst als Vermischung.

    BEFUND/FIX: Die Vorfassung nahm die ERSTE Trefferzeile. Das ist im Canvas
    die Uebersichtstabelle mit einer 55-Zeichen-Kurzfassung, nicht die
    eigentliche Item-Aussage weiter unten. Der Check prueft also die
    Zusammenfassung und haette eine Vermischung in der echten Aussage nie
    gesehen — die Negativkontrolle hat genau das aufgedeckt. Jetzt werden
    ALLE Aussage-Zellen geprueft.
    """
    out = []
    for lineno, line in enumerate(read(repo, CANVAS).split("\n"), 1):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 2 and _clean(cells[0]) == rid:
            out.append((lineno, cells[1]))
    return out


def collect_evidence_status_claims(repo, files, subject):
    """Alle `evidence_status`-Werte, die in einer Zeile MIT `subject` stehen.
    Genommen wird das Token direkt hinter `evidence_status`."""
    out = []
    rx = re.compile(r"evidence[_ ]status`?\s*[:=]?\s*\**`?([a-z-]+)`?\**", re.I)
    for rel in files:
        if not rel.endswith(".md"):
            continue
        for lineno, line in enumerate(read(repo, rel).split("\n"), 1):
            if subject not in line:
                continue
            for m in rx.finditer(line):
                v = m.group(1).lower()
                if v in EVIDENCE_VALUES:
                    out.append({"datei": rel, "line": lineno, "wert": v,
                                "text": norm(line)[:160]})
    return out


def check_canvas_and_requirement_split(res, repo, files, reg_index, prd_text,
                                       trace_rows):
    prd_blocks = parse_prd_blocks(prd_text)

    # ---- C17: CAN-130 evidence_status = planned, keine Widersprueche ----
    e130 = registry_entry(reg_index, "CAN-130")
    claims = collect_evidence_status_claims(repo, files, "CAN-130")
    values = sorted({c["wert"] for c in claims})
    bad = [c for c in claims if c["wert"] != "planned"]
    f17 = list(bad)
    if e130 is None:
        f17.append({"id": "CAN-130", "problem": "nicht in der Registry"})
    elif e130["status"] != "active":
        f17.append({"id": "CAN-130", "status": e130["status"],
                    "problem": "Inhalt ist entschieden, Status muesste `active` sein"})
    if not claims:
        f17.append({"id": "CAN-130", "problem": "kein einziger evidence_status-Wert "
                                                "gefunden — nicht nachweisbar `planned`"})
    res.add("C17",
            "CAN-130 traegt `evidence_status = planned` und 0 widerspruechliche "
            "CAN-130-Evidence-Statuswerte im gesamten Dokumentenbestand",
            not f17,
            "%d evidence_status-Angaben zu CAN-130 gefunden, Wertemenge %s, "
            "%d widerspruechlich"
            % (len(claims), values or "leer", len(bad)),
            f17,
            note="Semantik (projektweit): planned = Metrik, Berechnung und "
                 "zustaendiges Gate sind definiert, Instrumentierung fehlt. "
                 "`planned` ist deshalb KEIN Nachweis — `empirical_result` "
                 "bleibt MISSING. Grundgesamtheit > 0 ist Bestehensbedingung.")

    # ---- C18: CAN-099 ausschliesslich Accessibility ----
    st99_all = canvas_statements(repo, "CAN-099")
    # Begriffe der GESTALTUNGSSPRACHE. Nicht darunter: "Farbe" — der Satz
    # "Farbe ist niemals der einzige Informationstraeger" ist eine
    # Accessibility-Schranke und gehoert genau hierher.
    DESIGN_TERMS = ["monochrom", "designsystem", "design-system", "tokenbasiert",
                    "design-token", "sportplatz-gold", "teamfarbe", "revieridentit",
                    "feiermoment", "gestaltungssprache"]
    ACCESS_TERMS = ["wcag", "screenreader", "kontrast", "fokus", "dynamic type",
                    "font scaling", "voiceover", "talkback", "bedienfl"]
    f18 = []
    if not st99_all:
        f18.append({"id": "CAN-099", "problem": "keine Canvas-Zeile gefunden"})
    for lineno, st in st99_all:
        low = st.lower()
        for term in DESIGN_TERMS:
            if term in low:
                f18.append({"id": "CAN-099", "line": lineno, "begriff": term,
                            "problem": "Designsystem-Anteil in der AUSSAGE von "
                                       "CAN-099 — CAN-099 ist ausschliesslich "
                                       "Accessibility"})
    if st99_all and not any(any(a in st.lower() for a in ACCESS_TERMS)
                            for _, st in st99_all):
        f18.append({"id": "CAN-099", "problem": "keine Aussage nennt ein "
                                                "Accessibility-Merkmal"})
    res.add("C18",
            "CAN-099 enthaelt ausschliesslich Accessibility (kein "
            "Designsystem-Anteil in der Item-Aussage)",
            not f18,
            "%d Aussage-Zellen zu CAN-099 geprueft (Zeilen %s) gegen %d "
            "Gestaltungs- und %d Accessibility-Begriffe, %d Verstoesse"
            % (len(st99_all), [l for l, _ in st99_all], len(DESIGN_TERMS),
               len(ACCESS_TERMS), len(f18)),
            f18,
            note="Geprueft wird die AUSSAGE-Spalte, nicht die Anmerkungsspalte. "
                 "Die Anmerkung beschreibt die Abgrenzung ('Designsystem-Anteil "
                 "nach CAN-141 ausgelagert') — sie mitzulesen wuerde die "
                 "Abgrenzung selbst als Vermischung beanstanden. `Farbe` ist "
                 "bewusst KEIN verbotener Begriff: 'Farbe ist niemals der "
                 "einzige Informationstraeger' ist eine Accessibility-Schranke.")

    # ---- C19: eigenes Canvas-Item fuer das monochrome Designsystem ----
    design_items = []
    for line in read(repo, CANVAS).split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 2 or not re.match(r"^\**CAN-\d{3}\**$", cells[0].strip()):
            continue
        low = cells[1].lower()
        if "monochrom" in low and ("designsystem" in low or "tokenbasiert" in low):
            design_items.append(_clean(cells[0]))
    # BEFUND/FIX: nach ID deduplizieren. Dasselbe Item steht sowohl in der
    # Uebersichtstabelle als auch in der Haupttabelle des Canvas. Die
    # Vorfassung zaehlte ZEILEN und meldete ein einziges Item als "2 Items" —
    # ein Fehlalarm. Geprueft ist die Anzahl unterscheidbarer ITEMS.
    design_items = sorted(set(design_items))
    f19 = []
    if not design_items:
        f19.append({"problem": "kein Canvas-Item, dessen AUSSAGE ein monochromes, "
                               "tokenbasiertes Designsystem formuliert"})
    for cid in design_items:
        e = registry_entry(reg_index, cid)
        if e is None:
            f19.append({"id": cid, "problem": "nicht in der Registry"})
        elif e["status"] != "active":
            f19.append({"id": cid, "status": e["status"],
                        "problem": "Designsystem-Item ist nicht aktiv"})
        if cid in ("CAN-099",):
            f19.append({"id": cid, "problem": "das Designsystem darf nicht im "
                                              "Accessibility-Item stehen"})
    res.add("C19",
            "Das monochrome tokenbasierte Designsystem hat ein EIGENES "
            "Canvas-Item (nicht mit Accessibility in einem Item vermischt)",
            not f19 and len(design_items) == 1,
            "%d Canvas-Item(s) mit Designsystem-Aussage gefunden: %s"
            % (len(design_items), design_items or "keines"),
            f19)

    # ---- C20: getrennte Requirements UND getrennte ACs ----
    def reqs_matching(*terms):
        out = []
        for rid, blk in prd_blocks.items():
            low = (blk["title"] or "").lower()
            if any(t in low for t in terms):
                out.append(rid)
        return sorted(out)

    acc_reqs = reqs_matching("accessibility", "zugänglich", "zugaenglich")
    des_reqs = reqs_matching("designsystem", "design-system")
    f20 = []
    if not acc_reqs:
        f20.append({"problem": "kein Requirement mit Accessibility-Titel"})
    if not des_reqs:
        f20.append({"problem": "kein Requirement mit Designsystem-Titel"})
    overlap = sorted(set(acc_reqs) & set(des_reqs))
    if overlap:
        f20.append({"ids": overlap, "problem": "ein Requirement traegt BEIDE "
                                               "Gegenstaende — nicht getrennt"})
    # Zugehoerige ACs aus der Kernmatrix; sie muessen ebenfalls verschieden sein.
    ac_by_req = {}
    for r in trace_rows:
        if not r.get("req") or r.get("deprecated"):
            continue
        # Die AC-Spalte kann mehrere ACs tragen (REQ-019: AC-019 + AC-041).
        # Gelesen wird die ZELLE, nicht der vorextrahierte Einzeltreffer.
        cell = r["cells"][4] if len(r["cells"]) > 4 else ""
        ac_by_req[r["req"]] = sorted(set(re.findall(r"AC-\d{3}", cell)))
    acc_acs = sorted({a for rid in acc_reqs for a in ac_by_req.get(rid, [])})
    des_acs = sorted({a for rid in des_reqs for a in ac_by_req.get(rid, [])})
    for rid in acc_reqs + des_reqs:
        if not ac_by_req.get(rid):
            f20.append({"id": rid, "problem": "kein AC in der Kernmatrix verknuepft"})
    shared = sorted(set(acc_acs) & set(des_acs))
    if shared:
        f20.append({"ids": shared, "problem": "Accessibility und Designsystem "
                                              "teilen sich ein AC"})
    res.add("C20",
            "Accessibility und Designsystem haben GETRENNTE Requirements und "
            "GETRENNTE Acceptance Criteria",
            not f20,
            "Accessibility-REQ %s mit AC %s; Designsystem-REQ %s mit AC %s"
            % (acc_reqs or "keine", acc_acs or "keine",
               des_reqs or "keine", des_acs or "keine"),
            f20)

    # ---- C21: GPX-Export hat eine eigene Functional Requirement ----
    gpx_reqs = sorted(rid for rid, blk in prd_blocks.items()
                      if "gpx" in (blk["title"] or "").lower())
    f21 = []
    if not gpx_reqs:
        f21.append({"problem": "kein Requirement, dessen TITEL den GPX-Export "
                               "benennt — der Export haette keine eigene "
                               "Functional Requirement"})
    for rid in gpx_reqs:
        e = registry_entry(reg_index, rid)
        if e is None:
            f21.append({"id": rid, "problem": "nicht in der Registry"})
        elif e["status"] != "active":
            f21.append({"id": rid, "status": e["status"], "problem": "nicht aktiv"})
        mt = re.sub(r"[`*]", "", norm(prd_blocks[rid]["fields"].get(
            "measurement_type", ""))).strip()
        if not mt:
            f21.append({"id": rid, "problem": "kein measurement_type"})
    res.add("C21",
            "Der GPX-Export hat eine EIGENE Functional Requirement (nicht nur "
            "eine Teilklausel eines anderen Requirements)",
            not f21 and len(gpx_reqs) == 1,
            "%d Requirement(s) mit GPX-Export im Titel: %s"
            % (len(gpx_reqs), gpx_reqs or "keines"),
            f21)

    # ---- C22: REQ-034 ist NUR sekundaerer Anker fuer den GPX-Export ----
    f22 = []
    for rid in gpx_reqs:
        body = prd_blocks[rid]["body"]
        anchor_line = ""
        for line in body.split("\n"):
            if line.strip().startswith("Canvas:"):
                anchor_line = line
                break
        if not anchor_line:
            f22.append({"id": rid, "problem": "keine Ankerzeile gefunden"})
            continue
        if "REQ-034" not in anchor_line:
            f22.append({"id": rid, "problem": "REQ-034 steht nicht in der "
                                              "Ankerzeile — Sekundaerbezug fehlt"})
            continue
        # "sekundaer" muss VOR REQ-034 stehen; steht es dahinter oder gar nicht,
        # ist REQ-034 als primaerer Anker gefuehrt.
        i = anchor_line.index("REQ-034")
        prefix = anchor_line[:i].lower()
        if "sekund" not in prefix:
            f22.append({"id": rid, "ankerzeile": norm(anchor_line)[:160],
                        "problem": "REQ-034 ist nicht als `sekundär` "
                                   "gekennzeichnet"})
        # BEFUND/FIX: Die Vorfassung suchte `primär … REQ-034` ohne die
        # Verneinung zu lesen und schlug deshalb ausgerechnet an dem Satz an,
        # der das Gegenteil sagt: "REQ-034 ist sekundär, NICHT primär".
        # Dieselbe Fehlerklasse wie der Bindestrich-blinde Tokenizer: die
        # Pruefung las die Zeichen, nicht die Aussage. Jetzt wird die
        # Verneinung im unmittelbaren Umfeld ausgewertet.
        for m in re.finditer(r"prim[äa]r", body, re.I):
            window = body[max(0, m.start() - 60):m.end() + 60]
            if "REQ-034" not in window:
                continue
            if re.search(r"\bnicht\b|\bkein\b|sekund", window, re.I):
                continue          # verneint oder ausdruecklich als sekundaer
            f22.append({"id": rid, "stelle": norm(window)[:160],
                        "problem": "REQ-034 wird als primaerer Anker gefuehrt"})
    res.add("C22",
            "REQ-034 ist fuer den GPX-Export NUR sekundaerer Anker, nicht "
            "primaerer",
            not f22 and bool(gpx_reqs),
            "%d GPX-Requirement(s) geprueft, %d Verstoesse"
            % (len(gpx_reqs), len(f22)),
            f22)

    # ---- C23: CAN-022 ausschliesslich Datenqualitaetsproblem ----
    st22_all = canvas_statements(repo, "CAN-022")
    CONVENIENCE_TERMS = ["telefon mitführen", "telefon mitfuehren", "ohne telefon",
                         "komfort", "bequem", "convenience"]
    QUALITY_TERMS = ["trainingssignal", "herzfrequenz", "kadenz", "sensor",
                     "vollständig", "vollstaendig", "zuverlässig", "zuverlaessig"]
    f23 = []
    if not st22_all:
        f23.append({"id": "CAN-022", "problem": "keine Canvas-Zeile gefunden"})
    for lineno, st in st22_all:
        low = st.lower()
        for term in CONVENIENCE_TERMS:
            if term in low:
                f23.append({"id": "CAN-022", "line": lineno, "begriff": term,
                            "problem": "Komfort-/Convenience-Aussage in der "
                                       "AUSSAGE von CAN-022 — vermischt mit dem "
                                       "Datenqualitaetsproblem"})
    if st22_all and not any(any(q in st.lower() for q in QUALITY_TERMS)
                            for _, st in st22_all):
        f23.append({"id": "CAN-022", "problem": "keine Aussage nennt ein "
                                                "Datenqualitaetsmerkmal"})
    res.add("C23",
            "CAN-022 enthaelt ausschliesslich das Datenqualitaetsproblem "
            "(der Komfortaspekt ist NICHT eingemischt)",
            not f23,
            "%d Aussage-Zellen zu CAN-022 geprueft (Zeilen %s), %d Verstoesse"
            % (len(st22_all), [l for l, _ in st22_all], len(f23)),
            f23,
            note="Der Komfortaspekt 'Nutzer muessen zusaetzlich das Telefon "
                 "mitfuehren' ist laut Nutzerentscheidung eine SEPARATE "
                 "moegliche Aussage und hat bewusst KEINE CAN-ID. Dass die "
                 "Anmerkungsspalte ihn als ausgeschlossen benennt, ist die "
                 "Abgrenzung — deshalb wird nur die Aussage-Spalte geprueft.")

    # ---- C24: die neue USER-ID ist registry-gueltig ----
    # Die ID wird NICHT abgetippt, sondern aus der Registry gewonnen: Personas,
    # die im Auftau-Schritt 2 angelegt wurden.
    personas = [e for e in reg_index.values() for e in e
                if e["prefix"] == "USER"]
    new_personas = sorted({e["id"] for e in personas
                           if e["created_at"].strip() == "2026-07-19"})
    f24 = []
    if not personas:
        f24.append({"problem": "kein USER-Praefix in der Registry gefuehrt — die "
                               "Persona-Vergabe waere ungeregelt"})
    if not new_personas:
        f24.append({"problem": "keine im Auftau-Schritt 2 angelegte Persona "
                               "gefunden"})
    for pid in new_personas:
        e = registry_entry(reg_index, pid)
        if e["status"] != "active":
            f24.append({"id": pid, "status": e["status"], "problem": "nicht aktiv"})
        if not norm(e["title"]):
            f24.append({"id": pid, "problem": "kein Titel"})
        if not e["canonical_file"]:
            f24.append({"id": pid, "problem": "keine canonical_file"})
    # Keine Wiederverwendung einer geloeschten/deprecateten Persona-ID.
    for e in personas:
        if e["status"] == "deprecated" and e["id"] in new_personas:
            f24.append({"id": e["id"], "problem": "deprecatete ID wiederverwendet"})
    res.add("C24",
            "Die neu vergebene USER-ID ist registry-gueltig (registriert, aktiv, "
            "mit Titel und canonical_file; keine wiederverwendete ID)",
            not f24,
            "%d Personas in der Registry, davon neu am 2026-07-19: %s"
            % (len({e["id"] for e in personas}), new_personas or "keine"),
            f24,
            note="Die ID wird aus der Registry GEWONNEN, nicht im Validator "
                 "abgetippt. Eine Beispiel-ID aus einer Anweisung wird nie "
                 "ungeprueft uebernommen.")

    # ---- C25: REQ-032 mit der Persona UND CAN-022 verknuepft ----
    f25 = []
    blk32 = prd_blocks.get("REQ-032")
    if blk32 is None:
        f25.append({"id": "REQ-032", "problem": "kein PRD-Block"})
    else:
        # BEFUND/FIX: Die Vorfassung durchsuchte den GESAMTEN Requirement-Block.
        # USER-004 und CAN-022 kommen dort auch im Fliesstext vor; das Entfernen
        # der eigentlichen VERKNUEPFUNG blieb deshalb unbemerkt. Die
        # Negativkontrolle hat das aufgedeckt. Geprueft wird jetzt die
        # Ankerzeile — dort steht die Verknuepfung.
        body = ""
        for line in blk32["body"].split("\n"):
            if line.strip().startswith("Canvas:"):
                body = line
                break
        if not body:
            f25.append({"id": "REQ-032", "problem": "keine Ankerzeile gefunden"})
        found_personas = sorted(set(re.findall(r"USER-\d{3}", body)))
        if not (set(found_personas) & set(new_personas)):
            f25.append({"id": "REQ-032", "gefunden": found_personas,
                        "erwartet_aus_registry": new_personas,
                        "problem": "REQ-032 ist nicht mit der neuen Persona "
                                   "verknuepft"})
        if "CAN-022" not in body:
            f25.append({"id": "REQ-032", "problem": "REQ-032 nennt CAN-022 nicht"})
        for pid in found_personas:
            if registry_entry(reg_index, pid) is None:
                f25.append({"id": "REQ-032", "ref": pid,
                            "problem": "verknuepfte USER-ID ist nicht registriert"})
    trace32 = next((r for r in trace_rows if r.get("req") == "REQ-032"), None)
    if trace32 is not None and "CAN-022" not in " ".join(trace32["cells"]):
        f25.append({"id": "TRC-032", "problem": "Kernmatrix-Zeile nennt CAN-022 nicht"})
    res.add("C25",
            "REQ-032 ist mit der neuen Persona UND mit CAN-022 verknuepft",
            not f25,
            "REQ-032 geprueft gegen Persona %s und CAN-022; %d Verstoesse"
            % (new_personas or "keine", len(f25)),
            f25)


def check_hardcoded_counts(res, repo, tool_files, n_active_req):
    """C26 — keine hartkodierte Gesamtzahl der REQ-Familie im Werkzeug.

    DREI Reparaturen gegenueber der Vorfassung:

    (a) Die Verbotsmenge ist ABGELEITET, nicht abgetippt. Vorher stand die
        Alt-Zahl als Literal im Validator — die Pruefung gegen hartkodierte
        Zahlen fuehrte selbst eine hartkodierte Zahl. Jetzt kommt die Menge
        aus der Registry-Historie (`created_at`/`deprecated_at`): jeder
        Zaehlstand, der je galt, ohne dass eine dieser Zahlen im Quelltext
        steht.

    (b) Es werden NUMBER- **und** STRING-Token geprueft. Die Vorfassung sah
        nur NUMBER — und war deshalb blind fuer ihre eigene Uebertretung, denn
        eine Zahl in Anfuehrungszeichen ist ein STRING. Eine Pruefung, die
        ihren eigenen Verstoss nicht sieht, hat nichts belegt.

    (c) Slice-/Index-Positionen sind ausgenommen: eine Textbreite ist keine
        Zaehlung. Die Vorfassung meldete eine Zeichenkettenkuerzung als
        "hartkodierte Requirement-Gesamtzahl" — ein Fehlalarm gegen korrekten
        Code. Die Ausnahme ist eng und hat eine Negativkontrolle.

    Die EINE Implementierung liegt in validate_trace.scan_count_literals;
    dieses Modul ruft sie auf, statt sie zu wiederholen.
    """
    from validate_trace import scan_count_literals
    import registry_model as RM
    forbidden = RM.load(repo).forbidden_count_literals()
    findings = scan_count_literals(tool_files, forbidden)
    res.add("C26",
            "0 hartkodierte Gesamtzahlen der REQ-Familie im Pruefwerkzeug "
            "(weder ein frueherer noch der aktuelle Stand, als NUMBER oder "
            "als STRING)",
            not findings,
            "%d Werkzeugdateien tokenisiert, %d verbotene Zaehlstaende "
            "(aus der Registry-Historie abgeleitet, nicht im Code genannt), "
            "%d Treffer"
            % (len(tool_files), len(forbidden), len(findings)),
            findings,
            note="Die Anzahl aktiver Requirements wird zur Laufzeit aus %s "
                 "abgeleitet: aktuell %d. Keine Pruefung besteht oder faellt "
                 "wegen einer Konstante. Verbotene Zaehlstaende in diesem Lauf: "
                 "%s." % (REGISTRY, n_active_req,
                          " ".join(sorted(forbidden, key=int))))


def check_non_vision_anchors(res, repo, files, prd_text, trace_rows, reg_index):
    """C27 — 0 semantisch falsche Canvas-, User-, Requirement- oder AC-Anker.

    C15 deckt die Vision-Achse ab. Dieselbe Beweisfuehrung wird hier auf die
    vier uebrigen Ankerarten angewandt: die als falsch AUSGEWIESENEN Paare
    werden aus den Artefakten GELESEN, nicht im Validator gefuehrt.
    """
    prd_blocks = parse_prd_blocks(prd_text)
    PREFIXES = ("CAN", "USER", "REQ", "AC")
    wrong = {}
    for rel in files:
        if not rel.endswith(".md"):
            continue
        for lineno, line in enumerate(read(repo, rel).split("\n"), 1):
            low = line.lower()
            reqs = re.findall(r"(?<![A-Za-z0-9_-])REQ-(\d{3})", line)
            if len(reqs) != 1:
                continue
            for pref in PREFIXES:
                hits = [(m.start(), m.end(), m.group(1)) for m in
                        re.finditer(r"(?<![A-Za-z0-9_-])%s-(\d{3})" % pref, line)]
                if not hits:
                    continue
                for mk, direction in WRONG_ANCHOR_MARKERS.items():
                    if mk.startswith("ersetzt vis-"):
                        continue          # vision-spezifisch, gehoert zu C15
                    pos = low.find(mk)
                    while pos >= 0:
                        end = pos + len(mk)
                        if direction == "before":
                            cand = [h for h in hits if h[1] <= end
                                    and pos - h[1] <= WRONG_ANCHOR_WINDOW]
                            pick = cand[-1] if cand else None
                        else:
                            cand = [h for h in hits if h[1] >= pos
                                    and h[0] - pos <= WRONG_ANCHOR_WINDOW]
                            pick = cand[0] if cand else None
                        if pick and not ("REQ" == pref and pick[2] == reqs[0]):
                            wrong.setdefault(
                                ("REQ-" + reqs[0], "%s-%s" % (pref, pick[2])),
                                []).append({"file": rel, "line": lineno,
                                            "marker": mk, "richtung": direction,
                                            "text": norm(line)[:160]})
                        pos = low.find(mk, end)

    # Aktive Anker je Requirement: PRD-Ankerzeile + VERKNUEPFUNGSSPALTEN der
    # Kernmatrix.
    #
    # BEFUND/FIX: Die Vorfassung las ALLE Zellen der Matrixzeile, also auch die
    # Titel- und Anmerkungsspalten. Dort steht Provenienz ("Nachfolger 1/2 von
    # REQ-014"), und Provenienz ist kein Anker. Der Check meldete daraufhin
    # REQ-037 und REQ-038 als "Anker auf eine deprecatete ID" — ausgerechnet
    # wegen des Satzes, der die Ablösung DOKUMENTIERT. Ein Check, der die
    # ordnungsgemaesse Deprecation-Dokumentation beanstandet, prueft nicht die
    # Sache, sondern die Zeichen.
    LINK_COLS = (2, 3, 4, 5)          # VIS | CAN | AC | EV
    active = defaultdict(set)
    dep_ids = {e["id"] for ents in reg_index.values() for e in ents
               if e["status"] == "deprecated"}
    for rid, blk in prd_blocks.items():
        if rid in dep_ids:
            continue                  # deprecatete REQs tragen keine Anker mehr
        for line in blk["body"].split("\n"):
            if line.strip().startswith("Canvas:"):
                for pref in PREFIXES:
                    for m in re.finditer(r"(?<![A-Za-z0-9_-])%s-\d{3}" % pref, line):
                        active[rid].add(m.group(0))
    for r in trace_rows:
        if not r.get("req") or r.get("deprecated") or r["req"] in dep_ids:
            continue
        joined = " ".join(r["cells"][i] for i in LINK_COLS if i < len(r["cells"]))
        for pref in PREFIXES:
            for m in re.finditer(r"(?<![A-Za-z0-9_-])%s-\d{3}" % pref, joined):
                active[r["req"]].add(m.group(0))

    findings = []
    for (rid, aid), where in sorted(wrong.items()):
        if aid in active.get(rid, set()):
            findings.append({"req": rid, "anker": aid,
                             "dokumentiert_als_falsch_in": where[0],
                             "problem": "Anker ist in den Artefakten als fachlich "
                                        "falsch ausgewiesen, steht aber weiterhin "
                                        "als aktiver Link"})
    # Zusaetzlich: aktive Anker, die in der Registry gar nicht existieren.
    for rid, aids in sorted(active.items()):
        for aid in sorted(aids):
            if aid in TEMPLATE_PLACEHOLDERS:
                continue
            e = registry_entry(reg_index, aid)
            if e is None:
                findings.append({"req": rid, "anker": aid,
                                 "problem": "Anker-ID ist nicht in der Registry"})
            elif e["status"] == "deprecated":
                findings.append({"req": rid, "anker": aid,
                                 "problem": "Anker verweist auf eine deprecatete ID"})
    res.add("C27",
            "0 semantisch falsche Canvas-, User-, Requirement- oder AC-Anker "
            "(dokumentiert falsche Paare stehen nirgends mehr als aktiver Link; "
            "kein Anker zeigt auf eine unbekannte oder deprecatete ID)",
            not findings,
            "%d dokumentierte Fehlanker-Paare aus den Artefakten gelesen, "
            "%d Requirements mit Ankern, %d Verstoesse"
            % (len(wrong), len(active), len(findings)),
            findings,
            note="Die Paarliste ist NICHT im Validator abgetippt; sie stammt aus "
                 "denselben Beanstandungsmarkern wie C15. Die Vision-Achse "
                 "verbleibt in C15, damit sich beide Checks nicht gegenseitig "
                 "verdecken.")


def check_runtime_criteria(res):
    """Kriterien, die laufenden Code voraussetzen — im reinen Dokumentenlauf
    nicht pruefbar. Sie werden NICHT stillschweigend als bestanden gefuehrt."""
    res.add("C7", "Reale Testausfuehrung gegen laufenden Code "
                  "(wired-in-prod, Evidence-Class, true-line-status)",
            False,
            "NICHT PRUEFBAR — es existiert kein Code, kein mobile/, kein infra/. "
            "Implementierungscode ist in diesem Lauf ausdruecklich verboten. "
            "Kein Pass moeglich; als NICHT ERFUELLT gefuehrt, nicht als bestanden.",
            [{"problem": "Kriterium erfordert Ausfuehrung; Dokumentenlauf kann es nicht bestehen"}])


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--json", default=None)
    ap.add_argument("--tools-dir", default=None,
                    help="Verzeichnis der zu pruefenden Werkzeugdateien (C14). "
                         "Default: das Verzeichnis dieses Validators. Die "
                         "Negativkontrolle setzt hier eine STAGED KOPIE ein, "
                         "damit sie die echten Werkzeuge nicht veraendert.")
    args = ap.parse_args()
    repo = args.repo

    reg_text = read(repo, REGISTRY)
    entries = parse_registry(reg_text)
    reg_index = defaultdict(list)
    for e in entries:
        reg_index[e["id"]].append(e)

    prd_text = read(repo, PRD)
    prd_blocks = parse_prd_blocks(prd_text)
    nfr_blocks = parse_nfr_blocks(prd_text)
    trace_rows = parse_trace_matrix(read(repo, TRACE))
    ledger_text = read(repo, DECISION_LOG)
    files = collect_scanned_files(repo)
    here = args.tools_dir or os.path.dirname(os.path.abspath(__file__))
    # NUR die Produktivwerkzeuge. selftest_validator.py ist bewusst
    # ausgenommen: seine Aufgabe IST es, den Defekt woertlich zu enthalten
    # (Fixture fuer C14). Wuerde er mitgeprueft, meldete C14 die eigene
    # Negativkontrolle als Verstoss — ein Fehlalarm, der die Kontrolle
    # unbrauchbar macht. Die Ausnahme ist eng und hier begruendet.
    tool_files = [os.path.join(here, n) for n in
                  ("validate_intake.py", "gen_intake.py", "blocking_model.py")]

    # ERWEITERUNG 2026-07-20: C26 prueft die GESAMTE aktive Validatorkette.
    # Die Vorfassung tokenisierte drei Dateien — validate_trace.py und
    # check_prd.py gehoerten nicht dazu, und genau in ihnen sassen das
    # Zahlliteral und die Altzahl-Suche. Ein Verbot, das die Dateien nicht
    # ansieht, in denen der Verstoss steht, ist kein Verbot.
    # selftest_validator.py bleibt fuer C14 ausgenommen (es MUSS den Defekt
    # woertlich enthalten), wird fuer C26 aber mitgeprueft: seine Fixtures
    # duerfen die Zahlen ableiten statt sie abzutippen.
    count_tool_files = [os.path.join(here, n) for n in
                        ("validate_intake.py", "gen_intake.py", "blocking_model.py",
                         "registry_model.py", "validate_trace.py", "check_prd.py",
                         "selftest_validator.py", "validate_schema.py",
                         "oq_check.py")]
    count_tool_files = [p for p in count_tool_files if os.path.isfile(p)]

    # Die Anzahl aktiver Requirements wird ABGELEITET, nirgends abgetippt.
    n_active_req = len([e for e in entries
                        if e["prefix"] == "REQ" and e["status"] == "active"])

    res = Result()
    owner_blockers = check_req_fields(res, entries, prd_blocks)
    check_null_values(res, repo, files)
    ref_counts, dep_total, rsv_total = check_references(res, repo, files, reg_index)
    check_duplicate_ids(res, entries)
    check_coverage(res, entries, trace_rows, prd_blocks, reg_index)
    contras, ledger_rows, reg_axes, outcomes = check_contradictions(
        res, entries, ledger_text, reg_text, repo, files)
    check_research_plans(res, prd_blocks)
    nfr_owner_blockers = check_nfrs(res, nfr_blocks)
    check_source_types(res, prd_blocks, nfr_blocks)
    check_hardcoded_blocking(res, tool_files)
    check_vision_links(res, repo, files, prd_text, trace_rows, reg_index)
    check_canvas_and_requirement_split(res, repo, files, reg_index, prd_text,
                                       trace_rows)
    check_hardcoded_counts(res, repo, count_tool_files, n_active_req)
    check_non_vision_anchors(res, repo, files, prd_text, trace_rows, reg_index)
    check_runtime_criteria(res)

    # ---- Ausgabe ----
    print("=" * 78)
    print("INTAKE-VALIDIERUNG — revyr-endurance-platform")
    print("Validator: NEU in diesem Lauf verfasst, kein vorbestehender Standard.")
    print("Repo: %s" % repo)
    print("Geprueft: %d Dateien | Registry-Eintraege: %d | PRD-Bloecke: %d | "
          "NFR-Bloecke: %d | TRC-Zeilen: %d"
          % (len(files), len(entries), len(prd_blocks), len(nfr_blocks),
             len(trace_rows)))
    print("=" * 78)

    counts = defaultdict(lambda: defaultdict(int))
    for e in entries:
        counts[e["prefix"]][e["status"]] += 1
    print("\n-- ID-Bestand laut Registry --")
    for p in MANAGED_PREFIXES:
        st = counts[p]
        print("  %-7s %s" % (p, ", ".join("%s=%d" % (k, v) for k, v in sorted(st.items()))))

    print("\n-- Pruefergebnisse --")
    failed = 0
    for c in res.checks:
        if c["status"] == "FAIL":
            failed += 1
        print("\n[%s] %s — %s" % (c["status"], c["id"], c["name"]))
        print("      Ergebnis: %s" % c["actual"])
        if c.get("note"):
            print("      Hinweis:  %s" % c["note"])
        for f in c["findings"][:25]:
            print("        - %s" % json.dumps(f, ensure_ascii=False))
        if len(c["findings"]) > 25:
            print("        ... %d weitere" % (len(c["findings"]) - 25))

    print("\n" + "=" * 78)
    print("BESTANDEN: %d/%d   FEHLGESCHLAGEN: %d"
          % (len(res.checks) - failed, len(res.checks), failed))
    print("GESAMT: %s" % ("ALLE PRUEFUNGEN BESTANDEN" if failed == 0
                          else "NICHT BESTANDEN — %d Kriterien nicht erfuellt" % failed))
    # Die Anzahl kommt aus der Registry. Der frueher hier ausgeschriebene Wert
    # war ueberholt und wurde von hier aus in weitere Artefakte kopiert.
    reserved_can_ids = sorted(e["id"] for e in entries
                              if e["prefix"] == "CAN" and e["status"] == "reserved")
    print("Gesamtstatus: BLOCKED_TRACEABILITY — die %d reservierten Canvas-Items"
          % len(reserved_can_ids))
    print("(%s) sind vom" % ", ".join(reserved_can_ids))
    print("Nutzer nicht bestaetigt. Hoechstmoeglicher Status danach:")
    print("READY_FOR_USER_CONFIRMATION. READY_FOR_AGILETEAM_PLANNING ist")
    print("ausgeschlossen und wird von keinem Agenten gesetzt.")
    print("=" * 78)

    if args.json:
        payload = {
            "validator": "validate_intake.py (in diesem Lauf neu verfasst)",
            "repo": repo,
            "files_scanned": files,
            "id_counts": {p: dict(counts[p]) for p in MANAGED_PREFIXES},
            "reference_counts": ref_counts,
            "owner_blocker_reqs": owner_blockers,
            "owner_blocker_nfrs": nfr_owner_blockers,
            "c6b_definition": C6B_DEFINITION,
            "contra_axes": reg_axes,
            "contra_outcomes": outcomes,
            "checks": res.checks,
            "passed": len(res.checks) - failed,
            "failed": failed,
            "overall": "PASS" if failed == 0 else "FAIL",
        }
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
        print("JSON geschrieben: %s" % args.json)

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
