#!/usr/bin/env python3
"""Structural verification of the canvas file. No literals derived from counts."""
import re, sys, json, os

_REPO = os.environ.get("REVYR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(_REPO, "docs/canvas/revyr-endurance-platform.canvas.md")
REG = os.path.join(_REPO, "docs/ID-REGISTRY.md")
lines = open(P, encoding="utf-8").read().split("\n")

def cells(line):
    s = line.strip()
    return [c.strip() for c in s.strip("|").split("|")]

# --- 1. table integrity: every contiguous pipe block has uniform column count,
#        a separator row, and no blank line inside the body.
problems = []
i = 0
tables = []
while i < len(lines):
    if lines[i].strip().startswith("|"):
        start = i
        block = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            block.append((i + 1, lines[i]))
            i += 1
        tables.append((start + 1, block))
    else:
        i += 1

for start, block in tables:
    widths = {}
    for ln, raw in block:
        widths.setdefault(len(cells(raw)), []).append(ln)
    if len(widths) > 1:
        problems.append(f"TABLE@{start}: uneven column counts {dict((k, v[:4]) for k, v in widths.items())}")
    if len(block) >= 2 and not re.match(r'^\|[\s:\-|]+\|$', block[1][1].strip()):
        problems.append(f"TABLE@{start}: second row is not a separator: {block[1][1][:60]}")

# --- 2. blank line immediately followed by a pipe row that is NOT a header
#        (i.e. a body row orphaned out of its table)
for n in range(1, len(lines) - 1):
    if lines[n].strip() == "" and lines[n + 1].strip().startswith("|"):
        # next non-blank after the pipe run must eventually contain a separator
        if n + 2 < len(lines) and not re.match(r'^\|[\s:\-|]+\|$', lines[n + 2].strip()):
            problems.append(f"L{n+2}: pipe row after blank line without separator row -> orphaned table body?")

# --- 3. deprecated IDs must not appear as ACTIVE definition rows.
#        Active definition rows = rows whose FIRST cell is exactly an ID (no ~~).
deprecated = set()
for raw in open(REG, encoding="utf-8"):
    if raw.strip().startswith("|"):
        c = cells(raw)
        if len(c) >= 9 and re.fullmatch(r'(CAN|REQ|AC|EV|TRC|VIS)-\d{3}', c[0]) and "deprecated" in c[4]:
            deprecated.add(c[0])

# Definition tables only: header must be the atomic-item header.
DEF_HEADER = ["ID", "Aussage", "Source Type", "Source", "Herkunft", "Befund / Hinweis"]
def_rows = []          # (line, cells) inside definition tables
for start, block in tables:
    if cells(block[0][1]) != DEF_HEADER:
        continue
    for ln, raw in block[2:]:
        def_rows.append((ln, cells(raw)))

active_rows = {}
for ln, c in def_rows:
    if c and re.fullmatch(r'(CAN|REQ|AC|EV|TRC|VIS)-\d{3}', c[0]):
        active_rows.setdefault(c[0], []).append(ln)
print(f"# definition rows: {len(def_rows)}, distinct active IDs: {len(active_rows)}")

for did in sorted(deprecated):
    if did in active_rows:
        problems.append(f"DEPRECATED {did} appears as an un-struck definition row at {active_rows[did]}")

# --- 4. duplicate active definition rows for the same ID in the atomic tables
for k, v in sorted(active_rows.items()):
    if len(v) > 1:
        problems.append(f"DUPLICATE active row for {k} at {v}")

# --- 5. canonical wordings must be present verbatim (from the user decision)
canon = {
 "A/CAN-099": "Die mobile Anwendung und ihre nutzbaren Web-Auskopplungen müssen für Menschen mit unterschiedlichen visuellen, motorischen und assistiven Anforderungen bedienbar sein. Dazu gehören WCAG 2.2 AA, Screenreader-Unterstützung, skalierbare Schrift, ausreichende Bedienflächen, nachvollziehbare Fokusführung und die Regel, dass Farbe niemals der einzige Informationsträger ist.",
 "B/CAN-141": "Die Anwendung verwendet ein tokenbasiertes, überwiegend monochromes Designsystem. Farbe wird nur eingesetzt, wenn sie eine definierte fachliche Bedeutung besitzt: Health-Status, Team- und Revieridentität, Sportplatz-Gold sowie bestätigte Feiermomente. Run und Bike werden nicht ausschließlich durch Farbe unterschieden.",
 "C/CAN-139": "Nutzer behalten Kontrolle über ihre aufgezeichneten Aktivitäten und können eine abgeschlossene Run- oder Bike-Aktivität als standardkonforme GPX-Datei exportieren, ohne sie veröffentlichen oder mit anderen Nutzern teilen zu müssen.",
 "CAN-138": "Nutzer können lokal gespeicherte Run- und Bike-Aktivitäten in einem Verlauf anzeigen und eine ausgewählte Aktivität mit Route, Dauer, Distanz und sportartspezifischer Kernmetrik in einer Detailansicht öffnen.",
 "CAN-142": "Nutzer können eine gespeicherte Route erneut als Grundlage einer geplanten Run- oder Bike-Aktivität verwenden.",
 "CAN-143": "Nutzer können fachlich vergleichbare Aktivitäten auf derselben oder hinreichend ähnlichen Strecke anhand sportartspezifischer Kennzahlen miteinander vergleichen.",
}
body = "\n".join(lines)
for k, t in canon.items():
    if t not in body:
        problems.append(f"CANONICAL WORDING MISSING verbatim: {k}")

# --- 6. the generic colour clause must live in CAN-099 only, not CAN-141
def def_row(idv):
    for ln, c in def_rows:
        if c and c[0] == idv:
            return c
    return []
c99, c141 = def_row("CAN-099"), def_row("CAN-141")
if not c99 or "Farbe niemals der einzige Informationsträger" not in c99[1]:
    problems.append("CAN-099 Aussage does not carry the canonical colour clause")
# CAN-141 may MENTION the removal in the Befund cell, but must not state it in its Aussage cell
if c141 and re.search(r'Farbe (ist )?nie(mals)? de[rn] einzige', c141[1]):
    problems.append("CAN-141 Aussage still states the generic colour clause")
# and the Befund cell must record WHERE it went
if c141 and "CAN-099" not in c141[5]:
    problems.append("CAN-141 Befund does not point at the canonical carrier CAN-099")

# --- 7. no stale count literals bound to a count
for pat, why in [(r'\bzehn reservierte\b', "stale 'zehn reservierte'"),
                 (r'CAN-138 … CAN-140', "range spans a deprecated ID"),
                 (r'CAN-138 bis CAN-141 standen nie', "stale range")]:
    for n, l in enumerate(lines, 1):
        if re.search(pat, l) and "überholt" not in l and "frühere Stand" not in l:
            problems.append(f"L{n}: {why}: {l.strip()[:80]}")

print(json.dumps({"tables": len(tables), "problems": problems}, ensure_ascii=False, indent=2))
sys.exit(1 if problems else 0)
