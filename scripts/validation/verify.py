# -*- coding: utf-8 -*-
import io, re, sys, collections, os

_REPO = os.environ.get("REVYR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(_REPO, "docs/traceability.md")
R = os.path.join(_REPO, "docs/ID-REGISTRY.md")
lines = io.open(P, encoding="utf-8").read().split("\n")
fails = []

# --- A: table structure (column uniformity + no blank line inside a table body)
def cells(l):
    # escaped pipes (\|) are cell CONTENT, not separators
    s = l.strip().replace("\\|", "\x00")
    return s.count("|") - 1

i = 0
tables = 0
while i < len(lines):
    if lines[i].strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-|]+\|$", lines[i+1].strip()):
        tables += 1
        head = i
        n = cells(lines[i])
        j = i + 2
        while j < len(lines) and lines[j].strip().startswith("|"):
            if cells(lines[j]) != n:
                fails.append("A col-mismatch line %d (head %d): %d vs %d" % (j+1, head+1, cells(lines[j]), n))
            j += 1
        # blank line immediately followed by another row => blank inside body
        if j < len(lines) and lines[j].strip() == "":
            k = j + 1
            if k < len(lines) and lines[k].strip().startswith("|") and not (k+1 < len(lines) and re.match(r"^\|[\s:\-|]+\|$", lines[k+1].strip())):
                fails.append("A blank-line-inside-table at line %d" % (j+1))
        i = j
    else:
        i += 1

# --- B: registry-derived counts
reg = io.open(R, encoding="utf-8").read().split("\n")
defrow = re.compile(r"^\|\s*([A-Z]+)-(\d+)\s*\|[^|]*\|[^|]*\|\s*`([^`]+)`\s*\|\s*\*{0,2}([a-z\-]+)\*{0,2}\s*\|")
counts = collections.defaultdict(collections.Counter)
for l in reg:
    m = defrow.match(l)
    if m:
        counts[m.group(1)][m.group(4)] += 1

exp = {
    "REQ": ("active", 40), "TRC": ("active", 40), "AC": ("active", 41), "EV": ("active", 42),
    "VIS": ("active", 11), "CAN": ("active", 123),
}
derived = {}
for p, (st, want) in exp.items():
    got = counts[p][st]
    derived[p] = got
    if got != want:
        fails.append("B count %s active: registry=%d, doc claims=%d" % (p, got, want))

# --- C: no deprecated ID used as a live link in the core matrix / §5 table
dep = set()
for l in reg:
    m = defrow.match(l)
    if m and m.group(4) == "deprecated":
        dep.add("%s-%s" % (m.group(1), m.group(2)))
# core matrix rows
core = [l for l in lines if re.match(r"^\|\s*\**TRC-\d+", l)]
for l in core:
    if l.strip().startswith("| ~~"):
        continue
    for d in dep:
        for m in re.finditer(r"(?<![\w-])" + re.escape(d) + r"(?![\d-])", l):
            ctx = l[max(0, m.start()-40):m.start()]
            # migration provenance is explicitly permitted (Registry rule 3 forbids the
            # REFERENCE, not the migration record) -- see traceability section 8.1
            if re.search(r"Nachfolger[^|]*von\s*$|deprecated[^|]*\u2192\s*$|statt\s*$", ctx):
                continue
            fails.append("C deprecated %s in live core-matrix row: %s" % (d, l[:70]))

# --- D: row-status tally in core matrix vs claimed
stat = collections.Counter()
for l in core:
    if l.strip().startswith("| ~~"):
        continue
    last = l.rstrip().rstrip("|").split("|")[-1]
    for s in ("linked-partial", "not-linked", "broken", "linked"):
        if s in last:
            stat[s] += 1
            break
    else:
        fails.append("D no status in row: %s" % l[:70])
tot = sum(stat.values())
claim = {"linked": 31, "broken": 6, "not-linked": 1, "linked-partial": 2}
if dict(stat) != claim:
    fails.append("D status tally counted=%s claimed=%s" % (dict(stat), claim))
if tot != derived["REQ"]:
    fails.append("D core-matrix active rows=%d != registry REQ active=%d" % (tot, derived["REQ"]))

# --- E: forbidden chain gone
for i, l in enumerate(lines):
    if "Vorstufe von Verst" in l:
        if not any(k in l for k in ("verboten", "entfernt", "AUFGEHOBEN", "Kette")):
            fails.append("E forbidden chain still used as anchor, line %d" % (i+1))

# --- F: VIS-008 no longer anchors REQ-019..022
for l in core:
    if re.search(r"REQ-0(19|20|21|22)\b", l) and "VIS-008" in l:
        for m in re.finditer(r"VIS-008", l):
            ctx = l[max(0, m.start()-30):m.start()]
            if "statt " in ctx:   # migration note, not an anchor
                continue
            fails.append("F VIS-008 still anchors community REQ: %s" % l[:70])

# --- G: no literal 36/39 used as expectation or prohibition
for i, l in enumerate(lines):
    if re.search(r"\b(36|39)\b", l):
        if not any(k in l for k in ("Altstand", "kein g", "verboten", "nicht 36", "weder 36", "Weder 36", "VC-0", "VC-036", "vorher", "gestiegen", "von 3 auf 6", "von 5 auf 9", "35 / 40", "REQ-039", "CAN-139", "EV-039", "AC-039", "TRC-039", "VIS-", "§")):
            fails.append("G bare count literal line %d: %s" % (i+1, l[:90]))

print("tables scanned:", tables)
print("registry-derived active:", dict((k, derived[k]) for k in sorted(derived)))
print("core-matrix row status:", dict(stat), "total", tot)
print("FAILS:", len(fails))
for f in fails:
    print("  -", f)
