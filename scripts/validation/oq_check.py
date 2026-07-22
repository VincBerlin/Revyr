#!/usr/bin/env python3
"""Verify every OQ-ID denotes exactly one decision across the four artifacts."""
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(os.environ.get("REVYR_REPO") or Path(__file__).resolve().parent.parent.parent)
FILES = [
    "docs/decisions/open-questions.md",
    "docs/canvas/revyr-endurance-platform.canvas.md",
    "docs/prd/revyr-endurance-platform.prd.md",
    "docs/vision/revyr-endurance-platform.vision.md",
]

# Ordered topic classifier: first match wins. Keys are lowercase substrings.
TOPICS = [
    ("A0-PROXY-PFAD", ("ablageort", "deployt")),
    ("PRODUKTNAME", ("marke", "name")),
    ("OWNER-DRI", ("owner", "dri")),
    ("GESCHAEFTSMODELL", ("geschäftsmodell", "monetarisierung", "preislogik")),
    ("HEALTH-CLAIMS", ("claims", "health-formulierungen")),
    ("MODERATION", ("moderations-sla",)),
    ("RETENTION", ("retention",)),
    ("SPIELWERTE", ("effort", "bahngold", "spielwerte")),
    ("OS-GERAETE", ("ios", "geräteversionen", "referenzgeräte")),
    ("KARTEN-ROUTING", ("karten", "routinganbieter")),
    ("BACKEND", ("backend",)),
]

ROW = re.compile(r"^\|\s*(OQ-\d+)\s*\|\s*([^|]+?)\s*\|")


def classify(text: str) -> str:
    low = text.lower()
    for topic, keys in TOPICS:
        if any(k in low for k in keys):
            return topic
    return "UNCLASSIFIED"


meanings = defaultdict(set)
rows = []
for rel in FILES:
    for lineno, line in enumerate(
        (REPO / rel).read_text(encoding="utf-8").splitlines(), 1
    ):
        m = ROW.match(line.strip())
        if not m:
            continue
        oq, desc = m.group(1), m.group(2)
        topic = classify(desc)
        meanings[oq].add(topic)
        rows.append((oq, topic, rel, lineno))

rows.sort()
for oq, topic, rel, lineno in rows:
    print(f"{oq}  {topic:<18} {rel}:{lineno}")

print()
conflicts = {oq: t for oq, t in meanings.items() if len(t) > 1}
unclassified = [r for r in rows if r[1] == "UNCLASSIFIED"]

# An ID may denote only one decision; a decision may be denoted by only one ID.
topic_owner = defaultdict(set)
for oq, topics in meanings.items():
    for t in topics:
        topic_owner[t].add(oq)
dupes = {t: ids for t, ids in topic_owner.items() if len(ids) > 1}

if conflicts:
    print("FAIL: OQ-ID with more than one meaning:")
    for oq, t in sorted(conflicts.items()):
        print(f"  {oq} -> {sorted(t)}")
if dupes:
    print("FAIL: decision denoted by more than one OQ-ID:")
    for t, ids in sorted(dupes.items()):
        print(f"  {t} -> {sorted(ids)}")
if unclassified:
    print("FAIL: unclassified rows:")
    for r in unclassified:
        print(f"  {r}")

if conflicts or dupes or unclassified:
    sys.exit(1)
print(f"PASS: {len(meanings)} OQ-IDs, {len(rows)} references, 1:1 ID<->decision.")
