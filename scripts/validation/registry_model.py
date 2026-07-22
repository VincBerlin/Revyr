#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
registry_model.py — DER EINZIGE Registry-Parser des Projekts.

Vorgeschichte (Befund dieses Laufs):
Es existierten DREI Parser fuer dieselbe Datei:
  * validate_intake.py:parse_registry() — kopfzeilengebunden, korrekt
  * derive_counts.py:load()            — abschnittsueberschriftgebunden,
                                          las das Statusmodell teilweise mit
  * check_prd.py:registry_rows()       — "erste Zelle, die wie ein Status
                                          aussieht", ohne Kopfzeilenpruefung
Zusaetzlich las validate_trace.py ueberhaupt nicht die Registry, sondern einen
Scratchpad-Cache (derived.json). Der Cache war vom Stand vor Runde 4; der
Validator meldete daraufhin REQ-041/042, AC-043, EV-044, CAN-142/143 und
VIS-014 als "erfundene IDs" — ein Fehlalarm gegen einen korrekten Dokumenten-
stand, erzeugt allein durch eine veraltete Zwischendatei.

Konsequenz: EIN Parser, zur LAUFZEIT aus docs/ID-REGISTRY.md. Kein Cache.
Es gibt keine zweite Fassung, keine kopierte Regex, keine Zahl als Literal.
"""

import os
import re

REGISTRY_REL = "docs/ID-REGISTRY.md"
DEFAULT_REPO = "/Users/vincentschnetzer/Documents/Run&Bike"

# Kopfzeile der kanonischen ID-Definitionstabellen (Registry §3).
DEF_HEADER = ["id", "type", "title", "canonical_file", "status",
              "created_at", "deprecated_at", "replacement_id", "notes"]

MANAGED_PREFIXES = ["VIS", "CAN", "REQ", "AC", "TRC", "EV", "RISK", "ASM", "OQ",
                    "CONTRA", "USER", "NFR"]

# Registry-Entscheidung §4: Template-Platzhalter, keine echten Items.
TEMPLATE_PLACEHOLDERS = {"REQ-000", "AC-000", "EV-000"}

ID_RE = re.compile(r"\b((?:%s)-\d{3})\b" % "|".join(MANAGED_PREFIXES))


def registry_path(repo=None):
    return os.path.join(repo or DEFAULT_REPO, REGISTRY_REL)


def _header_cells(line):
    s = line.strip()
    if not s.startswith("|"):
        return None
    return [c.strip().strip("*` ").lower() for c in s.strip("|").split("|")]


def parse_definitions(text):
    """Alle ID-Definitionszeilen unter der kanonischen Kopfzeile.

    Kopfzeilengebunden — nicht spaltenzahlgebunden. Registry §6.11.1 fuehrt
    eine zweite, ebenfalls neunspaltige Tabelle (Statusmodell je CONTRA-ID),
    deren Spalte 5 `blocking` heisst und nicht `status`. Ein spaltenzahl-
    basierter Parser las sie als Definitionen und erfand damit Statuswerte.
    """
    entries = []
    in_def = False
    prev = None
    id_col = re.compile(r"^([A-Z]+)-(\d{3})$")
    for lineno, line in enumerate(text.split("\n"), 1):
        s = line.strip()
        if not s.startswith("|"):
            in_def = False
            prev = None
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and all(set(c) <= set("-: ") and c for c in cells):
            in_def = (prev == DEF_HEADER)
            prev = None
            continue
        prev = _header_cells(line)
        if not in_def or len(cells) < len(DEF_HEADER):
            continue
        m = id_col.match(cells[0].strip("*` ~"))
        if not m or m.group(1) not in MANAGED_PREFIXES:
            continue
        entries.append({
            "id": cells[0].strip("*` ~"),
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


class Registry(object):
    """Abgeleiteter ID-Bestand. Jede Zahl ist eine Ableitung, kein Literal."""

    def __init__(self, text, path=None):
        self.text = text
        self.path = path
        self.entries = parse_definitions(text)
        self.by_id = {}
        self.duplicates = []
        for e in self.entries:
            if e["id"] in self.by_id:
                self.duplicates.append((e["id"], self.by_id[e["id"]]["lineno"],
                                        e["lineno"]))
            else:
                self.by_id[e["id"]] = e
        # Existenzmenge: JEDE in der Registry ueberhaupt vergebene ID. Fuer die
        # Frage "existiert diese ID?" ist die Definitionstabelle nicht
        # massgeblich, sondern die Vergabe (Migrations- und Nachfolgerspalten).
        self.all_ids = frozenset(ID_RE.findall(text))

    # -- Grundabfragen ----------------------------------------------------
    def ids(self, prefix, status=None):
        return sorted(e["id"] for e in self.by_id.values()
                      if e["prefix"] == prefix
                      and (status is None or e["status"] == status))

    def status_of(self, idv):
        e = self.by_id.get(idv)
        return e["status"] if e else None

    def active(self, prefix):
        return self.ids(prefix, "active")

    def deprecated(self, prefix):
        return self.ids(prefix, "deprecated")

    def reserved(self, prefix):
        return self.ids(prefix, "reserved")

    def count(self, prefix, status="active"):
        """DIE Zahl. Abgeleitet, nie hartkodiert, nie als Literal erwartet
        oder verboten (Nutzerentscheidung 2026-07-20, Punkt 5)."""
        return len(self.ids(prefix, status))

    def counts(self, prefix):
        out = {}
        for e in self.by_id.values():
            if e["prefix"] == prefix:
                out[e["status"]] = out.get(e["status"], 0) + 1
        return out

    def exists(self, idv):
        return idv in self.all_ids

    # -- Zaehlstaende ueber die Zeit --------------------------------------
    @staticmethod
    def _date(cell):
        v = re.sub(r"[`*~]", "", str(cell)).strip()
        m = re.match(r"(\d{4}-\d{2}-\d{2})", v)
        return m.group(1) if m else None

    def count_history(self, prefix):
        """Zaehlstand aktiver IDs je Stichtag — ABGELEITET aus `created_at`
        und `deprecated_at` der Definitionstabelle.

        Das ist der Schluessel zu Punkt 5 der Nutzerentscheidung: die Zahlen,
        die kein Werkzeug erwarten oder verbieten darf, sind exakt die
        historischen Zaehlstaende. Sie werden hier GERECHNET. Damit steht
        keine von ihnen als Literal im Code — der Validator kennt sie, ohne
        sie zu nennen.
        """
        ent = [e for e in self.by_id.values() if e["prefix"] == prefix
               and e["status"] in ("active", "deprecated")]
        days = sorted({d for e in ent
                       for d in (self._date(e["created_at"]),
                                 self._date(e["deprecated_at"])) if d})
        out = []
        for d in days:
            n = 0
            for e in ent:
                born = self._date(e["created_at"])
                died = self._date(e["deprecated_at"])
                if born and born <= d and not (died and died <= d):
                    n += 1
            out.append((d, n))
        return out

    # -- Zahlliterale, die kein Werkzeug fuehren darf ----------------------
    #
    # Grundgesamtheit: die REQ-Familie. Ihre Zaehlstaende liegen weit oberhalb
    # gewoehnlicher Programmkonstanten; kleine Zaehlstaende (VIS, NFR) sind als
    # Verbotsliterale ungeeignet, weil sie sich nicht von Schleifengrenzen
    # unterscheiden lassen. Die Untergrenze wird aus den Daten genommen, nicht
    # gesetzt.
    COUNT_FAMILY = ("REQ", "AC", "EV", "TRC")

    def forbidden_count_literals(self):
        """Jede Zahl, die je als Gesamtzahl der REQ-Familie galt oder gilt.

        Enthaelt automatisch die beiden vom Nutzer benannten Altzahlen und die
        aktuellen Staende — ohne dass eine davon im Quelltext steht.
        """
        bad = set()
        for p in self.COUNT_FAMILY:
            for _day, n in self.count_history(p):
                bad.add(str(n))
            bad.add(str(self.count(p, "active")))
        floor = min(int(x) for x in bad) if bad else None
        # CAN/VIS nur, soweit sie oberhalb derselben Groessenordnung liegen.
        for p in ("CAN", "VIS"):
            for _day, n in self.count_history(p):
                if floor is not None and n >= floor:
                    bad.add(str(n))
        return bad


_CACHE = {}


def load(repo=None, force=False):
    """Liest die Registry ZUR LAUFZEIT. Kein Zwischenstand auf Platte.

    Der Prozess-lokale Cache ist an mtime gebunden und ueberlebt den Lauf
    nicht — er ist eine Leseoptimierung, keine Zwischendatei.
    """
    path = registry_path(repo)
    key = (path, os.path.getmtime(path))
    if force or key not in _CACHE:
        _CACHE.clear()
        with open(path, encoding="utf-8") as fh:
            _CACHE[key] = Registry(fh.read(), path)
    return _CACHE[key]


if __name__ == "__main__":
    import json
    import sys
    r = load(sys.argv[1] if len(sys.argv) > 1 else None)
    print("Registry:", r.path)
    print("Duplikate:", r.duplicates)
    print(json.dumps({p: r.counts(p) for p in MANAGED_PREFIXES}, indent=1))
    print("vergebene IDs gesamt:", len(r.all_ids))
    for p in Registry.COUNT_FAMILY:
        print("Historie %-4s %s" % (p, r.count_history(p)))
    print("verbotene Zahlliterale (abgeleitet):",
          " ".join(sorted(r.forbidden_count_literals(), key=int)))
