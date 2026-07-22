import re, os
_REPO = os.environ.get("REVYR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
rep = open(os.path.join(_REPO, 'docs/validation/validation-report.md'), encoding='utf-8').read()
reg = open(os.path.join(_REPO, 'docs/ID-REGISTRY.md'), encoding='utf-8').read().split('\n')

# open points from registry section 8
open_pts = []
for l in reg[1520:1567]:
    m = re.match(r'^\|\s*(\d+)\s*\|(.*)$', l)
    if not m:
        continue
    n, rest = int(m.group(1)), m.group(2)
    closed = rest.strip().startswith('~~') or 'GESCHLOSSEN' in rest
    if not closed:
        open_pts.append(n)
print('offene §8-Punkte:', len(open_pts), open_pts)

# points explicitly named in report section 4 (table rows "| N | ..." and prose "Punkt N")
named = set()
for m in re.finditer(r'^\|\s*(\d+)\s*\|', rep, re.M):
    named.add(int(m.group(1)))
for m in re.finditer(r'Punkte?\s+(\d+)', rep):
    named.add(int(m.group(1)))
for m in re.finditer(r'(?:^|[\s(])(\d+)\s*\(Teil', rep):
    named.add(int(m.group(1)))
# section 4.4 / 4.5 enumerations
for blk in re.findall(r'Acht Punkte: (.*?)\.\n', rep, re.S) + re.findall(r'Punkte (7, 9.*?) —', rep, re.S):
    for m in re.finditer(r'\b(\d{1,2})\b', blk):
        named.add(int(m.group(1)))

missing = [p for p in open_pts if p not in named]
print('nie im Bericht zugeordnet:', missing)
