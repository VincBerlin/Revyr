# Äquivalenzbeweis — Original vs. Repo-Kopie

Stand: 2026-07-20. Gesamtstatus bleibt `BLOCKED_TRACEABILITY`. Dieses Dokument ist
**kein** Gate-Verdikt und **keine** Freigabe.

## Was bewiesen wird — und was ausdrücklich nicht

Bewiesen wird **ausschließlich**: fünf Werkzeuge, deren Repo-Pfad-Literal durch eine
Auflösung aus dem Skriptort ersetzt wurde, erzeugen auf **diesem** Rechner, gegen
**diesen** Repo-Stand, byte-genau dieselbe Ausgabe wie das jeweilige Original.

**Nicht** bewiesen wird, dass die Werkzeuge korrekt prüfen. Drei von ihnen melden
aktenkundige Falschbefunde (siehe `README.md`, „Bekannte Werkzeugdefekte"). Die
Äquivalenz zeigt, dass die Repo-Kopie **denselben Defekt** unverändert reproduziert —
das ist der Zweck, nicht ein Mangel des Beweises.

## Geänderte Werkzeuge

| Werkzeug | Geändert |
|---|---|
| `xcheck.py` | Pfad-Literal → `_REPO` aus `__file__` bzw. `REVYR_REPO` |
| `verify.py` | dito |
| `verify_canvas.py` | dito |
| `oq_check.py` | dito (`Path(...)` statt `os.path`, weil das Original `pathlib` nutzt) |
| `AUDIT_points.py` | dito |

Prüflogik, Schwellwerte, Ausgabetexte und Reihenfolge wurden **nicht** angefasst. Die
vollständigen Diffs stehen unten.

## Vergleichskommando (tatsächlich verwendet)

```bash
SP=/private/tmp/claude-501/-Users-vincentschnetzer-Documents-Run-Bike/5ad02448-3a52-4a17-affc-d652ef4b5345/scratchpad
V="/Users/vincentschnetzer/Documents/Run&Bike/scripts/validation"
W=/private/tmp/.../equiv2
for f in xcheck.py verify.py verify_canvas.py oq_check.py AUDIT_points.py; do
  python3 "$SP/$f" >"$W/$f.orig.out" 2>"$W/$f.orig.err"; ro=$?
  python3 "$V/$f"  >"$W/$f.copy.out" 2>"$W/$f.copy.err"; rc=$?
  cmp -s "$W/$f.orig.out" "$W/$f.copy.out" && echo SAME || echo DIFF   # stdout
  cmp -s "$W/$f.orig.err" "$W/$f.copy.err" && echo SAME || echo DIFF   # stderr
done
```

`cmp -s` vergleicht **byte-genau**, nicht zeilen- oder textnormalisiert.

## Ergebnis

| Werkzeug | stdout | stderr | rc Original | rc Kopie | SHA-256 stdout (16) orig | SHA-256 stdout (16) Kopie | stdout Bytes | stderr Bytes |
|---|---|---|---:|---:|---|---|---:|---:|
| `xcheck.py` | **SAME** | **SAME** | 0 | 0 | `cf87fad337b0152b` | `cf87fad337b0152b` | 312 | 0 |
| `verify.py` | **SAME** | **SAME** | 0 | 0 | `3b9707fd29b2a900` | `3b9707fd29b2a900` | 385 | 0 |
| `verify_canvas.py` | **SAME** | **SAME** | 1 | 1 | `07a873bb6c62557f` | `07a873bb6c62557f` | 163 | 0 |
| `oq_check.py` | **SAME** | **SAME** | 1 | 1 | `871e30aea35129c9` | `871e30aea35129c9` | 4916 | 0 |
| `AUDIT_points.py` | **SAME** | **SAME** | 0 | 0 | `0873130973a4cb7d` | `0873130973a4cb7d` | 321 | 0 |

**Keine Abweichung in stdout, stderr oder Exit-Code.** Es gab nichts zu beschönigen;
hätte es eine Abweichung gegeben, stünde sie hier wörtlich.

Der Exit-Code war nicht Teil des Auftrags, wurde aber miterhoben, weil eine gleiche
Ausgabe bei ungleichem Exit-Code die Gleichwertigkeit widerlegt hätte.

## Geltungsgrenze des Beweises

Original und Kopie lösen hier auf **denselben** Repo-Pfad auf: das Original per
Literal, die Kopie per Skriptort. Die Äquivalenz ist damit an genau diesem Ort
gemessen. Sie sagt **nichts** darüber, ob die Werkzeuge anderswo gleich liefen — das
ist gerade der Unterschied, den die Änderung herstellt, und er lässt sich per
Definition nicht durch Gleichheit belegen. Dass die Auflösung aus einem anderen
Verzeichnis greift, ist separat gemessen (`README.md`, Abschnitt „Lauf aus einem Klon").

## Vollständige Diffs

```diff
--- xcheck.py (Original)
+++ xcheck.py (Repo-Kopie)
-import re, json
-REG="/Users/vincentschnetzer/Documents/Run&Bike/docs/ID-REGISTRY.md"
-CAN="/Users/vincentschnetzer/Documents/Run&Bike/docs/canvas/revyr-endurance-platform.canvas.md"
+import re, json, os
+_REPO = os.environ.get("REVYR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
+REG=os.path.join(_REPO, "docs/ID-REGISTRY.md")
+CAN=os.path.join(_REPO, "docs/canvas/revyr-endurance-platform.canvas.md")

--- verify.py (Original)
+++ verify.py (Repo-Kopie)
-import io, re, sys, collections
+import io, re, sys, collections, os
-P = "/Users/vincentschnetzer/Documents/Run&Bike/docs/traceability.md"
-R = "/Users/vincentschnetzer/Documents/Run&Bike/docs/ID-REGISTRY.md"
+_REPO = os.environ.get("REVYR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
+P = os.path.join(_REPO, "docs/traceability.md")
+R = os.path.join(_REPO, "docs/ID-REGISTRY.md")

--- verify_canvas.py (Original)
+++ verify_canvas.py (Repo-Kopie)
-import re, sys, json
+import re, sys, json, os
-P = "/Users/vincentschnetzer/Documents/Run&Bike/docs/canvas/revyr-endurance-platform.canvas.md"
-REG = "/Users/vincentschnetzer/Documents/Run&Bike/docs/ID-REGISTRY.md"
+_REPO = os.environ.get("REVYR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
+P = os.path.join(_REPO, "docs/canvas/revyr-endurance-platform.canvas.md")
+REG = os.path.join(_REPO, "docs/ID-REGISTRY.md")

--- oq_check.py (Original)
+++ oq_check.py (Repo-Kopie)
+import os
 import re
 import sys
-REPO = Path("/Users/vincentschnetzer/Documents/Run&Bike")
+REPO = Path(os.environ.get("REVYR_REPO") or Path(__file__).resolve().parent.parent.parent)

--- AUDIT_points.py (Original)
+++ AUDIT_points.py (Repo-Kopie)
-import re
-rep = open('/Users/vincentschnetzer/Documents/Run&Bike/docs/validation/validation-report.md', encoding='utf-8').read()
-reg = open('/Users/vincentschnetzer/Documents/Run&Bike/docs/ID-REGISTRY.md', encoding='utf-8').read().split('\n')
+import re, os
+_REPO = os.environ.get("REVYR_REPO") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
+rep = open(os.path.join(_REPO, 'docs/validation/validation-report.md'), encoding='utf-8').read()
+reg = open(os.path.join(_REPO, 'docs/ID-REGISTRY.md'), encoding='utf-8').read().split('\n')
```

## Auflösungsregel

`scripts/validation/<tool>.py` → `dirname` dreimal → Repo-Wurzel. Vorrang hat die
Umgebungsvariable `REVYR_REPO`, falls gesetzt und nicht leer.

Ein Nebeneffekt, offen benannt statt verschwiegen: `oq_check.py` steht in der Liste
`count_tool_files` von `validate_intake.py` (C26, Suche nach verbotenen Zahlliteralen).
Die eingefügte Zeile enthält **keine** Ziffer, C26 bleibt davon unberührt. Nachgewiesen
dadurch, dass `validate_intake.py` vor und nach der Änderung dieselben sechs
fehlgeschlagenen Kriterien meldet.
