# Validation Report — revyr-endurance-platform

Datum: **2026-07-20 (Runde 5, konsolidiert)** — ersetzt die Fassung vom 2026-07-20 (Runde 4)
⚠️ **Nachtrag 2026-07-20 (Runde 6): siehe §0.** Der dort protokollierte Validatorlauf ist der
jüngste. Die Kopfzahlen dieses Abschnitts und die Abschnitte §1–§9 samt Anhang beschreiben den
Stand der **Runde 5** und bleiben als Historie unverändert stehen.
Feature Slug: `revyr-endurance-platform`
Modus: PLUMBLINE_INTAKE_VALIDATION (reiner Dokumentenlauf, kein Code)
Readiness-Level: **BLOCKED_TRACEABILITY**
true-line-status: `pending-watcher` — dieser Bericht stellt **kein** Plumbline-Watcher-Verdikt aus.
wired-in-prod: `no` · evidence-class: `none` · self-certified: `false`
User Confirmation: **nicht erteilt.** Kein Agent bestätigt im Namen des Nutzers.

> **Dieser Bericht gilt NICHT als erfolgreich.** Von **38** mechanisch geprüften Kriterien sind
> **6 nicht erfüllt**: `C2`, `C3c`, `C3d`, `C7`, `C8`, `C12` (**32/38 bestanden**).
> Gegenüber dem Lauf vom 2026-07-19 ist die Zahl der Fehlschläge **gestiegen** (5 → 6).
> Es wurde nichts repariert — `C2` fällt neu, weil in dieser Runde ein neues Dokument entstand.
>
> **Gesamtstatus `BLOCKED_TRACEABILITY`.** `READY_FOR_AGILETEAM_PLANNING` wird ausdrücklich
> **nicht** erreicht, nicht beantragt und ist aus diesem Zustand nicht erreichbar.

Alle Zahlen sind zur Laufzeit aus `docs/ID-REGISTRY.md` **abgeleitet**, keine ist abgetippt.

---

## 0. Validatorlauf vom 2026-07-20 (Runde 6) — echte Ausgabe, nachgetragen

> **Historienhinweis.** Die Abschnitte **§1 bis §9 und der Anhang** dokumentieren den Stand der
> **Runde 5**. Sie bleiben unverändert stehen. Dieser Abschnitt §0 hält den **danach** gefahrenen
> Lauf fest. Wo beide auseinandergehen, gilt für den Werkzeugstand §0 und für die inhaltliche
> Bewertung weiterhin §1–§9, solange deren Aussagen nicht ausdrücklich hier widerrufen sind.
> **Nichts in diesem Abschnitt ist eine Freigabe oder ein Gate-Verdikt.** Gesamtstatus bleibt
> `BLOCKED_TRACEABILITY`.

**Kommando:** `scripts/validation/run_all.sh` · **Exit-Code: 1** · Python 3.14.2 ·
Repo `/Users/vincentschnetzer/Documents/Run&Bike`.

⚠️ **Die Kette wurde in dieser Sitzung zweimal gefahren, und sie hat zweimal Verschiedenes
gemessen.** Zwischen beiden Läufen hat sich der **Dokumentenbestand** geändert (§0.9). Beide
Ergebnisse sind unten geführt; maßgeblich für den Ist-Stand ist **Lauf 2**. Der Unterschied wird
nicht eingeebnet, weil er selbst ein Befund ist: **die Kette ist nicht gegen einen sich
verändernden Bestand stabil, und ohne Versionskontrolle ist kein Lauf nachträglich rekonstruierbar**
(`docs/EVIDENCE-LEDGER.md:102`: „das Repository steht nicht unter Versionskontrolle (am 2026-07-20
gemessen: kein `.git`-Verzeichnis)").
Erstmals aus dem **Repository** ausführbar — die Werkzeuge liegen seit Runde 6 unter
`scripts/validation/` statt im Scratchpad (`docs/SOURCE-MAP.md:4`: „**Runde 6**: Quellen und
Validatorkette ins Repository überführt (§1.6)"). Die Feststellung in **§9.1**, jedes
Validatorergebnis sei außerhalb der damaligen Session nicht reproduzierbar, ist damit für den
Ablageort überholt. **Registry §8 Punkt 13 und Punkt 33 werden dadurch nicht geschlossen** — dieser
Lauf stuft sie nicht herab und nicht hoch.

### 0.1 Werkzeugebene — Zusammenfassung des Laufs

```
ZUSAMMENFASSUNG: PASS=6  FAIL=4  INFO/SKIP=1
FEHLGESCHLAGEN: validate_intake.py verify.py verify_canvas.py oq_check.py
```

| Werkzeug | Ergebnis dieses Laufs | gegenüber Runde 5 |
|---|---|---|
| `registry_model.py` | PASS (rc=0) | in §-Anhang der Runde 5 nicht geführt |
| `validate_schema.py` | PASS — konform; `NICHT GEPRUEFTE SCHLUESSELWOERTER: ['x_schema_change_log']` | unverändert |
| `validate_intake.py` | **FAIL** — `BESTANDEN: 32/38   FEHLGESCHLAGEN: 6` → `C2`, `C3c`, `C3d`, `C7`, `C8`, `C12` (beide Läufe) | **Kriterienmenge identisch**; C2 mit **mehr** Fundstellen (§0.3) |
| `validate_trace.py` | PASS — `FAILS: 0` / `WARNS: 0` | unverändert |
| `check_prd.py` | PASS — `=== FAILURES: 0 ===` | unverändert |
| `xcheck.py` | PASS — alle vier Abweichungslisten leer | unverändert |
| `verify.py` | **FAIL** — `FAILS: 1` | Fehlschlag unverändert, **gezählte Verteilung geändert** (§0.4) |
| `verify_canvas.py` | **FAIL** — **3** Probleme | Runde 5: **1** Problem → **verschlechtert** (§0.5) |
| `oq_check.py` | **FAIL** — `UNCLASSIFIED -> ['OQ-012'…'OQ-016']` | unverändert, gleiche Ursache |
| `AUDIT_points.py` | INFO — `offene §8-Punkte: 0 []` | Runde 5: **37** → **Werkzeugartefakt** (§0.6) |
| `selftest_validator.py` | PASS — `SCHARF: 13/13 Werkzeug-Negativkontrollen` | unverändert |

### 0.2 Die Kernzahl ist unverändert — sie ist nicht besser geworden

Der Vergleichsstand lautete **38 Prüfungen, 32 bestanden, 6 nicht bestanden (C2, C3c, C3d, C7, C8,
C12)**. Dieser Lauf liefert **dieselbe Zahl und dieselbe Menge**. Keine der sechs Prüfungen ist
repariert, keine ist neu hinzugekommen. **Auf der Kriterienebene hat sich nichts geändert.**

Geändert hat sich der Bestand **unterhalb** der Kriterienebene — und zwar in drei Fällen zum
Schlechteren. Das ist der eigentliche Befund dieses Laufs: eine gleichbleibende Kopfzahl verdeckt
zusätzliche Fundstellen.

### 0.3 C2 — dieselbe Prüfung, **9 statt 5** Fundstellen (in zwei Schritten gewachsen)

| Stand | geprüfte Feldwerte | unbegründete Nullwerte |
|---|---:|---:|
| Runde 5 (Anhang) | nicht ausgewiesen | **5** |
| Lauf 1 dieser Sitzung | 1587 | **7** |
| **Lauf 2 dieser Sitzung (maßgeblich)** | **1606** | **9** |

Wortlaut aus Lauf 2: „*1606 Feldwerte in `| Feld | Wert |`-Tabellen geprueft, **9** unbegruendete
Nullwerte*". Die Runde-5-Fassung führte fünf (§5, Zeile P0, und Anhang: „5 Nullwerte ohne
Begründung, `2026-07-20-p0-spikes.md:390–394`").

**Die fünf bekannten Fundstellen** in `docs/plans/2026-07-20-p0-spikes.md:390–394` bestehen
unverändert fort. Keine ist behoben.

**Zwei kamen in Lauf 1 hinzu** — in einer Datei, die die Runde-5-Fassung an keiner Stelle nennt
(`docs/plans/2026-07-20-p0-spikes-startbericht.md:3`: „Datum: 2026-07-20 (Runde 6)"):

| Fundstelle | Feld | Wert |
|---|---|---|
| `docs/plans/2026-07-20-p0-spikes-startbericht.md:65` | `blocked_activities` | `—` |
| `docs/plans/2026-07-20-p0-spikes-startbericht.md:87` | `blocked_activities` | `—` |

Wortlaut der Zeile 65: „`| `blocked_activities` | — |`". Zeile 87 ist gleichlautend.

**Zwei weitere kamen zwischen Lauf 1 und Lauf 2 hinzu** — durch einen Eintrag in
`docs/EVIDENCE-LEDGER.md`, der während dieser Sitzung entstanden ist (§0.9):

| Fundstelle | Feld | Wert |
|---|---|---|
| `docs/EVIDENCE-LEDGER.md:100` | `Acceptance Criteria` | `**keine**` |
| `docs/EVIDENCE-LEDGER.md:115` | `evidence-class` | `**none**` |

**Ursache in allen vier Fällen: neue Dokumente wiederholen den bekannten Defekt.** Es ist dieselbe
Fehlerform, die Runde 5 unter C2 bereits beanstandet hatte — ein nullwertiger Feldwert ohne
Begründung. Bezeichnend ist der Kontrast **innerhalb derselben Tabelle**: `EVIDENCE-LEDGER.md:99`
(„`| Requirement IDs | **keine** — governance-/tooling-bezogen, an kein REQ gebunden |`") und `:101`
(„`| Evidence IDs | **keine — BLOCKER.** …`") tragen ihre Begründung mit und werden **nicht**
beanstandet; die Zeilen 100 und 115 tragen den bloßen Wert.

**Nicht wegdefiniert:** dass `—` sachlich „keine blockierten Tätigkeiten" und `none` sachlich „keine
Nachweisklasse" bedeuten mag, ist keine Begründung im Sinne von C2. C2 verlangt die Begründung
**im Dokument**, und die Nachbarzeilen zeigen, dass das Format dafür existiert und benutzt wird.

### 0.4 `verify.py` — Fehlschlag unverändert, gezählte Verteilung verschoben

Ausgabe dieses Laufs:

```
core-matrix row status: {'linked': 27, 'not-linked': 2, 'broken': 8, 'linked-partial': 3} total 40
FAILS: 1
  - D status tally counted={'linked': 27, 'not-linked': 2, 'broken': 8, 'linked-partial': 3} claimed={'linked': 31, 'broken': 6, 'not-linked': 1, 'linked-partial': 2}
```

§5.2 hielt für Runde 5 fest: „gezählt `{linked 28, broken 8, linked-partial 3, not-linked 1}`".
**Eine Zeile ist von `linked` nach `not-linked` gewandert.** Das `claimed`-Literal im Werkzeug ist
unverändert `{linked 31, broken 6, not-linked 1, linked-partial 2}` — der in §5.2 diagnostizierte
Werkzeugdefekt (hartkodiertes Literal) besteht fort und ist **nicht** korrigiert worden.

**Die Verschiebung ist ein Dokumentvorgang, kein Werkzeugvorgang, und sie ist im Dokument
ausgewiesen.** `docs/traceability.md:238` trägt am Zeilenende wörtlich:
„`| **not-linked** *(Runde 6, 2026-07-20; vorher `linked`)* |`".
Begründet ist die Herabstufung in `docs/traceability.md:471`: „**Vision-Anker — Quellenprüfung
Runde 6 (2026-07-20), Herabstufung `linked` → `not-linked`** … **Der Qualifizierer „verlässlich"
steht in keiner der vier Quellen.**"

Die beiden `not-linked`-Zeilen dieses Laufs sind **TRC-004** (`docs/traceability.md:238`) und
**TRC-037** (`docs/traceability.md:271`). Die Differenz zum `claimed`-Literal ist damit **größer**
geworden, nicht kleiner.

### 0.5 `verify_canvas.py` — von **1** auf **3** Probleme, darunter eine neue Fehlerklasse

```json
{
  "tables": 22,
  "problems": [
    "TABLE@224: uneven column counts {6: [224, 225, 226, 227], 10: [230], 8: [251]}",
    "TABLE@328: uneven column counts {6: [328, 329, 330, 331], 9: [338]}",
    "CANONICAL WORDING MISSING verbatim: A/CAN-099"
  ]
}
```

**Problem 1 und 2 sind die bekannte Falschmeldung an verschobenen Zeilennummern.** §5.2 diagnostizierte
für `TABLE@187` maskierte Pipes, die der Spaltenzähler nicht honoriert. Nachgemessen: Zeile 230
enthält 4, Zeile 251 enthält 2, Zeile 338 enthält 3 maskierte Pipes (`\|`); `verify_canvas.cells()`
trennt auf dem rohen `|`. **Gleiche Ursache, zwei Fundorte statt einem** — die Canvas-Datei ist
gewachsen und trägt den Defekt nun in zwei Tabellen.

**Problem 3 ist neu und gehört einer anderen Klasse an.** Es ist **keine** Formatierungsfalschmeldung.
Der Prüfschritt 5 von `verify_canvas.py` hält den vom Nutzer gesetzten kanonischen Wortlaut A als
eingefrorenes Literal und findet ihn im Canvas nicht mehr wörtlich. Gemessene Abweichung —
**eine einzige Textstelle**, im Literal vorhanden, im Dokument entfernt:

| | Wortlaut |
|---|---|
| Werkzeugliteral (`verify_canvas.py`, Schlüssel `A/CAN-099`) | „Die mobile Anwendung **und ihre nutzbaren Web-Auskopplungen** müssen für Menschen …" |
| `docs/canvas/revyr-endurance-platform.canvas.md` (Aussage-Zelle CAN-099) | „Die mobile Anwendung **muss** für Menschen …" — ohne die Erstreckung, Numerus angepasst |

Der Rest des Satzes ist zeichengleich.

**Ursache, nicht umgedeutet:** die Streichung ist ein **beauftragter und protokollierter**
Dokumentvorgang. `docs/decisions/decision-log.md:20` (DEC-014) führt sie wörtlich: „**CAN-099**
„mobile Anwendung und ihre Web-Auskopplungen … Bedienflächen … Fokusführung … motorische
Anforderungen" → nur „mobile Anwendung … WCAG 2.2 AA, Screenreader, skalierbare Schrift,
Farbregel"; Web-Auskopplungen entfernt". Die ausführliche Begründung steht in
`docs/traceability.md:1494` („**(a) Web-Erstreckung entfernt.** … **Keine der vier Quellen
erstreckt die Accessibility-Pflicht auf Web-Artefakte.**"). Sie setzt den Befund aus **§3, Punkt 1**
dieses Berichts um.

**Was hier ausdrücklich NICHT behauptet wird.** Der Fehlschlag wird **nicht** als „erledigt, weil
begründet" gewertet — §9.2 hält fest: „Eine Diagnose hebt einen Fehlschlag nicht auf." Offen bleibt
eine Sachfrage, die dieser Lauf **nicht entscheidet**: der gestrichene Wortlaut ist als
**Nutzerentscheidung 2026-07-20, kanonischer Wortlaut A** ausgewiesen
(`docs/canvas/revyr-endurance-platform.canvas.md`, Herkunftsspalte CAN-099). Dokument und
eingefrorenes Literal stehen damit auseinander. **Welche der beiden Fassungen die vom Nutzer
bestätigte ist, ist aus den Artefakten nicht entscheidbar und wird hier nicht entschieden** —
Owner Nutzer. Das Werkzeug wurde **nicht** angepasst (Freeze, §9.2: „Ein Fehlschlag ist ein Befund
und wird am Dokument behoben, nicht am Werkzeug").

### 0.6 `AUDIT_points.py` — die Meldung „0 offene §8-Punkte" ist ein Werkzeugartefakt

Ausgabe dieses Laufs: „`offene §8-Punkte: 0 []`" und „`nie im Bericht zugeordnet: []`".
Der Anhang der Runde 5 führte „**37 offene §8-Punkte**; nie zugeordnet: 22, 23, 26, 27, 30, 41, 44".

**Das ist keine Verbesserung und kein geschlossener Punkt.** `scripts/validation/AUDIT_points.py`
liest ein **hartkodiertes Zeilenfenster**:

```python
for l in reg[1520:1567]:
```

Das entspricht den Dateizeilen **1521–1567** von `docs/ID-REGISTRY.md`. Der Abschnitt §8 beginnt
dort inzwischen bei Zeile **1629** („`## 8. Offene Punkte, BLOCKER und MISSING`") und endet vor
Zeile 1687; die Datei umfasst 1962 Zeilen. Im Fenster 1521–1567 steht heute die Migrationstabelle
(Zeile 1521: „`| TRC-040 | traceability-row | 2026-07-20 | **TRC-041, TRC-042** | …`"). **Das
Werkzeug misst §8 nicht mehr, sondern eine andere Stelle der Datei; die 0 ist die Zahl der Treffer
im falschen Fenster.**

**Nachmessung über die tatsächlichen §8-Grenzen (1629–1686), mit derselben Abschlussregel des
Werkzeugs** (`~~` am Zeilenanfang oder „GESCHLOSSEN"): **51 nummerierte Zeilen, davon 44 offen** —
Punkte 1, 6–13, 15, 17–34, 36–51. **Diese 44 ist eine hier durchgeführte Messung, keine
Werkzeugausgabe**; sie wird nicht als Werkzeugergebnis geführt und ersetzt keinen Zählstand.
Festzuhalten ist allein: der Bestand offener §8-Punkte ist gegenüber den 37 der Runde 5
**gestiegen**, nicht auf null gefallen.

`AUDIT_points.py` läuft in `run_all.sh` als **INFO** und kippt deshalb kein Verdikt. Das Werkzeug
wurde **nicht** korrigiert (Freeze). Der Defekt — ein hartkodiertes Zeilenfenster auf eine
wachsende Datei — ist derselben Bauform zuzurechnen, die **C26** im Prüfwerkzeug verbietet, und
wird hier als **offener Werkzeugdefekt** ausgewiesen.

### 0.7 Beobachtung ohne Verdikt — zwei Werkzeuge zählen ASM verschieden

Im selben Lauf meldet `validate_intake.py` „`ASM     active=7, deprecated=7`", während
`registry_model.py` und `check_prd.py` „`ASM active=7 deprecated=4`" führen. `registry_model.py`
weist zugleich aus: „`Duplikate: [('ASM-001', 1067, 1071), ('ASM-002', 1068, 1072), ('ASM-003',
1069, 1073)]`" — `docs/ID-REGISTRY.md` führt ASM-001, ASM-002 und ASM-003 je zweimal, einmal mit
`canonical_file` PRD und einmal Vision (Zeilen 1067–1073), jeweils mit dem Vermerk „KOLLISION".
Das eine Werkzeug zählt **Zeilen**, das andere **eindeutige IDs**.

**Kein Verdikt.** Ob dieser Unterschied neu ist, ist **nicht entscheidbar** — der Runde-5-Bericht
führt für ASM keinen Zählstand (§5.1 nennt REQ, AC, EV, TRC, CAN, VIS, OQ und die Präfixzahl, ASM
nicht). Als Beobachtung ausgewiesen, nicht als Fehlschlag gewertet, nichts nachgezogen.

### 0.8 C7 — unverändert strukturell unerreichbar

`validate_intake.py` meldet wörtlich: „*NICHT PRUEFBAR — es existiert kein Code, kein mobile/, kein
infra/. Implementierungscode ist in diesem Lauf ausdruecklich verboten. Kein Pass moeglich; als
NICHT ERFUELLT gefuehrt, nicht als bestanden.*"

**Nicht umgedeutet, nicht ausgeklammert, nicht als „nicht anwendbar" geführt.** C7 erfordert
laufenden Code; es existiert keiner. Das Kriterium bleibt **nicht erfüllt** und zählt in den 6
Fehlschlägen mit. Es wird auch künftig in keinem Dokumentenlauf bestehen.

### 0.9 Der Bestand hat sich **während** der Prüfung geändert — offengelegt, nicht geglättet

Zwischen Lauf 1 und Lauf 2 ist `docs/EVIDENCE-LEDGER.md` gewachsen und trägt seither den Eintrag
`docs/EVIDENCE-LEDGER.md:87`: „`## [2026-07-20] Governance / Werkzeugkette — Überführung der Quellen
und Validatoren ins Repository`". Seine Feld/Wert-Tabelle beginnt bei `:97`.

**Gemessen, nicht schlussgefolgert.** Die Differenz der geprüften Feldwerte beträgt
1606 − 1587 = **19**. Der neue Ledger-Eintrag steuert in den Zeilen 96–120 genau **19** gescopte
Feldzeilen bei; die zwischen den Läufen ebenfalls erweiterte Datei
`docs/validation/validation-report.md` (dieser Abschnitt §0) steuert **0** bei — ihre Tabellen
tragen nicht den Kopf `| Feld | Wert |` und werden von C2 nicht erfasst. Die Zunahme ist damit
**vollständig** dem Ledger-Eintrag zugeordnet; die Fortschreibung dieses Berichts hat **keinen**
Befund erzeugt.

**Was das über die Kette aussagt — drei Punkte, keiner davon beschönigt:**

1. **Kein Werkzeug der Kette schreibt in das Repository.** `selftest_validator.py` legt seine
   Fixtures in einem Temporärverzeichnis an (`tempfile.mkdtemp(prefix="revyr-selftest-")`, Kopie
   nach `<tmp>/docs`) und mutiert ausschließlich Kopien; das einzige schreibende Werkzeug,
   `gen_intake.py`, ist in `run_all.sh` nicht enthalten. **Die Änderung stammt nicht aus dem Lauf.**
2. **Wer den Eintrag geschrieben hat, ist aus den Artefakten nicht entscheidbar** und wird hier
   **nicht** vermutet. Festgehalten wird allein die Messung.
3. **Kein Lauf dieser Kette ist nachträglich rekonstruierbar.** Ohne Versionskontrolle existiert
   kein Stand, gegen den ein früheres Ergebnis reproduziert werden könnte — der Ledger-Eintrag
   stellt das für sich selbst fest (`:102`: „das Repository steht nicht unter Versionskontrolle").
   Ein Validatorergebnis ohne festhaltbaren Eingabestand ist ein **Momentwert**, keine Prüfung mit
   Beweiswert. Das ist ein **eigener offener Punkt**, der durch die Überführung der Werkzeuge ins
   Repository (§0, Kopf) **nicht** miterledigt ist.

### 0.10 Gesamtbild dieses Laufs

Auf der Kriterienebene **unverändert** (32/38, dieselben sechs Fehlschläge). Unterhalb davon
**in drei Punkten schlechter**: C2 von 5 auf **9** Fundstellen, `verify_canvas.py` von 1 auf 3
Probleme mit einer neuen Fehlerklasse, `verify.py` mit einer zusätzlich herabgestuften
Traceability-Zeile. Dazu ein **neu sichtbar gewordener Werkzeugdefekt** (`AUDIT_points.py`), der
einen gestiegenen Bestand offener §8-Punkte als null ausgibt, und ein **Bestand, der sich während
der Prüfung selbst verändert hat** (§0.9).

**Nichts wurde repariert. Nichts wurde hochgestuft. Keine ID vergeben. Kein Werkzeug geändert.
Keine Quelldatei geändert.** Gesamtstatus bleibt **`BLOCKED_TRACEABILITY`**.

---

## 1. Ergebnis der Quellenprüfung

### 1.1 Die vier Quelldokumente — Fundorte und selbst berechnete Prüfsummen

Alle vier existieren. Sie liegen **außerhalb** des Repositorys und wurden ausschließlich
**gelesen** — nicht kopiert, nicht verändert. Prüfsummen mit `shasum -a 256` selbst berechnet und
gegen die Briefing-Präfixe bestätigt.

| ID | Datei (kanonisch) | Bytes | mtime | sha256 (Präfix) |
|---|---|---:|---|---|
| SRC-001 | `/Users/vincentschnetzer/Desktop/docs/REVYR-Vision-Canvas-PRD.md` | 24585 | 2026-07-18 02:52 | `d0a6adf4e1f2be84…` |
| SRC-002 | `/Users/vincentschnetzer/Desktop/docs/REVYR-Plan-PRD.md` | 10525 | 2026-07-16 23:51 | `37e090aafac7a3c7…` |
| SRC-003 | `/Users/vincentschnetzer/Desktop/docs/superpowers/plans/2026-07-10-REVYR-GESAMTPLAN-FINAL.md` | 61117 | 2026-07-18 02:52 | `c3ceb46fa52c4875…` |
| SRC-004 | `/Users/vincentschnetzer/Desktop/docs/superpowers/plans/2026-07-10-tracking-and-planned-routes.md` | 78355 | 2026-07-10 03:19 | `dc18a97d9fe22996…` |

**Nebenstände** (ältere, inhaltlich **verschiedene** Fassungen, abweichende SHA-256) für
SRC-001…SRC-003 unter `/Users/vincentschnetzer/Downloads/`. SRC-004 hat keine Nebenkopie.
**Alle Prüfungen ausschließlich gegen den Desktop-Stand** (neuer und größer).

**Gemeldet, nicht beauftragt, keine ID vergeben:**
`/Users/vincentschnetzer/Downloads/RUNNING_CYCLING_APP_KONZEPT_CHAT_ZUSAMMENFASSUNG.md`
(29451 B, `00f898fa9c1a3a71…`) — das Konzeptdokument, auf das SRC-003/SRC-004 mit `§`-Verweisen
zeigen (§2, §14–17, §20, §27–28, §33, §36). Ein erheblicher Teil dieser Verweise ist **nur** damit
auflösbar.

**Ursache des früher gemeldeten Befunds „vier von fünf Quellen fehlen": ein Pfadfehler.**
`CLAUDE.md` nennt repo-relative Pfade, die nicht existieren. Es fehlte nie ein Dokument.

### 1.2 Zellenprüfung — 131 geprüft, 0 ungeprüft

| Verdikt | Anzahl | Canvas | PRD | Vision |
|---|---:|---:|---:|---:|
| **BELEGT** | 109 | 77 | 24 | 8 |
| **TEILBELEGT** | 17 | 8 | 7 | 2 |
| **UNBELEGT** | 5 | 5 | 0 | 0 |
| **UNGEPRÜFT** | **0** | 0 | 0 | 0 |
| Summe | **131** | 90 | 31 | 10 |

**Nicht Teil dieser Grundgesamtheit:** die **85** `EXPLICIT`-Zellen **ohne** SRC-Angabe. Sie sind
nicht prüfbar, weil sie nichts benennen, wogegen zu prüfen wäre. Sie bleiben unverändert
**BLOCKER** — und sie sind die größte offene Belegposition des Bestands.

### 1.3 Offene Beobachtung, nicht glattgebügelt

SRC-001/SRC-003 tragen im **Text** `2026-07-16`, die Desktop-Dateien mtime `2026-07-18`, die
**Dateinamen** `2026-07-10`. Ein mtime ist **kein** Autorendatum — ob fortgeschrieben oder nur
kopiert wurde, ist aus den Dateien **nicht entscheidbar**. Als offene Beobachtung ausgewiesen,
weder als Widerspruch behauptet noch wegerklärt.

---

## 2. Was herabgestuft wurde — und was ausdrücklich NICHT hochgestuft wurde

### 2.1 Herabgestuft

**Fünf Canvas-Zellen sind UNBELEGT** — die Aussage kommt in **keiner** der vier Quellen vor:

| Zelle | Befund |
|---|---|
| CAN-041 „Apple Fitness" | Die Wettbewerberliste der Quellen ist abschließend: Whoop, Garmin, Strava |
| CAN-042 „Google/Fitbit" | „Fitbit" nirgends; „Google" nur als Auth / Play Store / Kartenanbieter |
| CAN-046 „Lokale Event-Plattformen" | nirgends. SRC-003 führt lokale Events als **eigenes Feature** (Plan 14) |
| CAN-110 „Private/gesperrte Sportanlagen" | nirgends. SRC-003 Risiko 23 ist OSM-**Datenqualität** — ein anderes Risiko |
| CAN-112 „Integrationstests" | Begriff nirgends. SRC-003 §9 zählt die Nachweisarten abschließend auf |

Vier von fünf liegen in **Wettbewerbsumfeld** und **Nachweisarten** — genau dort, wo
Branchenvorwissen leicht als Quellenaussage durchgeht.

**Weitere Herabstufungen dieser Runde** (Ankerebene, siehe §4): fünf Zeilen der manuellen
Ankerreview (TRC-020, TRC-030, TRC-033 auf `trägt-teilweise`; TRC-007, TRC-019 auf
`kein-Anker-vorhanden`), sowie die Zeilenstatus REQ-007 und REQ-019 von `linked`/`linked-partial`
auf **`broken`**.

### 2.2 Ausdrücklich NICHT hochgestuft

- **Keine** der 109 BELEGT-Zellen wurde hochgestuft. Belegt heißt geprüft, nicht befördert.
- **Kein** Status wurde auf `linked`, `user-confirmed` oder `verified` gesetzt.
- **Die 13 Herabstufungen, deren Prämisse entfallen ist, wurden NICHT zurückgenommen.**
  Mindestens 13 Blocker sind mit „SRC-001/SRC-003 nicht auffindbar" begründet
  (`prd.md:921/922/926/958/1076/1213/1263/1613`, `traceability.md:270/526`, `vision.md:63/153`,
  `ID-REGISTRY.md:1131–1133`). Diese Prämisse ist **widerlegt** — die betroffenen Anker
  (CAN-075, VIS-009, CAN-114, CAN-123, USER-001…003) sind sämtlich BELEGT. **Das kehrt die
  Herabstufungen nicht um:** die meisten stehen auf einem **zweiten Bein** („analytische
  Nullschwelle"), das unberührt bleibt. Sie sind von ihren Ownern **neu zu bewerten**, nicht
  automatisch zu heben.
- **CAN-113** ist nicht schwach belegt, sondern **falsch adressiert** („Referenzstrecken" steht in
  SRC-001/SRC-002, nicht im beanspruchten SRC-003). Quellenwechsel, **keine** inhaltliche
  Herabstufung.
- **CAN-051** trägt eine Quelle, die seinen Kern nicht deckt (siehe §3, REQ-007).

---

## 3. Anker REQ-037/038/039 und die Klärungen dieser Runde

### 3.1 Die drei Anker — dreimal „trägt", mit drei verschiedenen Lücken

| | Verdikt | Belegt | Nicht belegt |
|---|---|---|---|
| **REQ-037 ← CAN-099** | **trägt** | WCAG AA (SRC-001 §3.5 · SRC-003 §2.4 · SRC-002 §10) · VoiceOver/TalkBack **namentlich** (SRC-003 §2.4) · Dynamic Type · „Farben nie einziger Informationsträger" | Fassung **2.2** · **Web-Auskopplungen** · Bedienflächen · Fokusführung |
| **REQ-038 ← CAN-141** | **trägt am deutlichsten** | SRC-003 §2 „konsequent monochrom" · SRC-001 M-04 „**Design-Tokens**" · SRC-003 §2.1 „Bedeutungsfarben (**einzige Ausnahmen**)" | zwei Abweichungen (s.u.) |
| **REQ-039 ← CAN-139** | **trägt** | SRC-001 T-06 · SRC-003 Plan 2.8 · SRC-002 §3 · „**Portabilität**" wörtlich in SRC-003 §8 | „standardkonform" (keine Formatversion genannt) |

Alle drei sind **direkt** verankert. Keine Brücke, kein Zwischenglied.

**Vier Befunde, die nicht geglättet wurden:**

1. **CAN-099 nennt drei Pflichten, die in keiner Quelle stehen.** Volltextsuche über alle vier
   Dokumente nach *Bedienfläche · touch/tap target · Fokus · motorisch*: **null Treffer.** Dazu die
   Erstreckung auf **Web-Auskopplungen** — SRC-003 §2.1 erstreckt nur die **Farbmisch-Regel**
   dorthin, §2.4 (Accessibility) nicht; SRC-001 §2 führt „kein Web-Client" als **Nicht-Ziel**. Die
   Kette „Farbregel gilt für Web → Accessibility auch" wurde **nicht gebaut**. Heute folgenlos,
   weil nicht in AC-037 — beim nächsten AC-Nachzug würden sie still zur Pflicht.
2. **CAN-141 ist schwächer als seine Quelle.** SRC-003 §2.1: Run/Bike „unterscheidet sich durch
   Ikonografie + Typo-Akzent, **nicht durch Farbe**". CAN-141 verbietet nur die *ausschließliche*
   Farbunterscheidung. **Nicht verschärft.** Dazu: die Quellen führen **fünf** Bedeutungsfarben
   (Team · Einzel-Revier · **Gold** · Health · Feier), CAN-141 **vier** — und AC-038 nennt die
   Vierer-Liste „abschließend".
3. **Die OPEN-QUESTION-Prämisse zur Fremd-App (§8 Punkt 36) ist enger als notiert.** Sie gilt
   **nur für den CAN-139-Wortlaut**: SRC-001 T-06 und SRC-003 Plan 2.8 führen beide wörtlich
   „**Fremd-App öffnet Datei**" — als Akzeptanzkriterium. AC-039 (d) und EV-039 geben damit die
   Quelle wieder. Offen bleibt allein die Wortlautfrage. Weder AC gestrichen noch Text ergänzt.
4. **„Ohne veröffentlichen/teilen" ist TEILBELEGT.** Die Quellen **beschreiben eine Architektur**,
   in der die Klausel gilt (SRC-001 §2 „alles lokal, ohne Account"), **fordern sie aber nirgends**.
   Aus „es gibt keinen Feed" folgt nicht „der Export darf nie einen voraussetzen".

**`canvas-problem` — nicht dreimal dieselbe Antwort.** REQ-038 → **MISSING (begründet)**, weil
SRC-003 §2 die Sache selbst als **Designprinzip** typisiert. REQ-039 → **MISSING (begründet)**, aber
schwächer: die Quelle schweigt zum Problem, statt es auszuschließen. REQ-037 → **MISSING, BLOCKER,
bleibt** — hier wurde die angebotene Nichtanwendbarkeit **verweigert**: Zugänglichkeit adressiert
unmittelbar eine Nutzergruppe, die das Produkt sonst nicht benutzen kann. CAN-099 **benennt die
Gruppe selbst**; ein Constraint, der seine Zielgruppe nennt, belegt die Existenz des Problems und
ersetzt sie nicht.

### 3.2 REQ-007 und REQ-019 — beide Anker entfernt, beide BLOCKER

**REQ-019.** Die erschlossene Brücke „Feed → Entdeckungsfläche → Zugang" ist **entfernt**. Die
Vision-Ebene beider Quellen wurde **vollständig** geprüft (SRC-001 §1.1–§1.4, SRC-003 §1.1–§1.3):
**keine Stelle nennt Routenempfehlung oder Feed.** Das Wort „Entdeckungsfläche" steht in **keiner**
Quelle — es *war* die Brücke. Nächstbeste Kandidaten einzeln verworfen: SRC-001 §1.1 „mit den
**Sportlern** deiner Umgebung" und §1.3 „lokale Ausdauersportler **finden**" (Personen, nicht
Strecken); SRC-003 §1.1 „Verbinden, **Folgen**" (Follow-Graph); SRC-003 §1.3 „Runner/Jogger: …
**Strecken entdecken**" — der stärkste Kandidat und dennoch kein Beleg, weil er ein
**Zielgruppen-Bedürfnis** benennt, nicht dass Strecken von anderen empfohlen werden.
Der Inhalt ist belegt, aber **eine Ebene tiefer**: SRC-001 §2.5 Social Loop („Follower übernehmen
die Route mit einem Tipp") — und SRC-001 §2 ist mit „**TEIL 2 — PRODUCT CANVAS**" überschrieben.
CAN-058 ist damit belegt; ein **Vision**-Anker entsteht daraus nicht.
Status `linked-partial` → **`broken`**.

**REQ-007.** Die frühere Begründung „aus dem Wortlaut nicht entscheidbar" ist entfallen — die
Quellen **entscheiden** die Frage: „Fortschritt" wird durchgehend **longitudinal** gebraucht
(SRC-001 §1.2 „Spürbaren Fortschritt — Punkte, Ränge, Avatare, Seasons"; §2.1; §3.3 „ob sie sich
**verbessert**"; SRC-003 §1.1). Die **aktivitätsinterne Restdistanz** erscheint **ausschließlich
funktional** (SRC-001 T-02, SRC-003 §9 GATE A) — nie auf Vision-Ebene.
Status `linked` → **`broken`**. Konsistenzgrund: für REQ-006, die Planungshälfte desselben Modus B,
ist VIS-003 aus genau diesem Grund bereits entfernt.

**Neuer Befund:** **CAN-051** („echte routebezogene Restdistanz", `EXPLICIT | SRC-001/SRC-003`) ist
damit **falsch verankert**. SRC-004 spezifiziert wörtlich `Math.max(0, plannedMeters -
coveredMeters)` mit Test `'subtracts covered from planned'` — also genau die Subtraktion, von der
REQ-007 bewusst abweicht. Quelle auf SRC-005/DEC-004 umstellen → **BLOCKER, Owner Canvas.**

**ID-Bedarf (BLOCKER, Registry eingefroren, keine Nummer genannt):** zwei VIS-IDs — routenbezogener
Fortschritt, Routenempfehlung/Feed. Für beide ist, anders als bei REQ-038/039/041, **nicht einmal
eine ID reserviert.**

### 3.3 Die leeren VIS-Platzhalter — drei verschiedene Ergebnisse

Kein Item gefüllt, keine ID vergeben.

- **VIS-012 — belegbar, Wortlaut vorgeschlagen, Status unbestätigt.** SRC-003 führt „**2.
  Design-System**" als eigenen Hauptabschnitt: *„Designprinzip: ‚Farbe muss man sich verdienen.'
  Die App ist konsequent monochrom …"*, bestätigt in §11. Produktweites Prinzip, kein Feature.
  ⚠️ **Sachkorrektur einer früheren Fassung:** „§2 samt **abschließender** Farbliste" ist falsch.
  §2 nennt **drei** Bedeutungsfarben; abschließend ist **§2.1** („einzige Ausnahmen") mit **fünf**
  — inklusive **Gold**. Wer §2 als abschließend zitiert, verliert zwei.
- **VIS-013 — zitierbar, aber Ebenensprung.** Einziger Beleg: SRC-003 §8 **Store-Readiness-Matrix**,
  „GPX-Export erfüllt Portabilität". Das Wort „Portabilität" kommt in allen vier Quellen **genau
  einmal** vor — in einer Compliance-Matrix. Das ist eine Compliance-Anforderung, keine
  Produktzusage. **Kein Wortlaut vorgeschlagen.** BLOCKER, Owner Nutzer.
- **VIS-014 — nicht belegbar.** Nur funktional (SRC-001 T-05 „Routen speichern/wiederverwenden")
  plus eine Zielgruppen-Beobachtung (SRC-003 §1.3 „feste Stammstrecken") — eine Eigenschaft der
  **Zielgruppe**, keine Zusage des **Produkts**. BLOCKER, Owner Nutzer.

Der Blocker für VIS-012/VIS-013 wechselt damit die **Art**: von „inhaltlich nicht ableitbar" zu
„**noch nicht entschieden**".

### 3.4 OQ-002, OQ-003, OQ-004

- **OQ-002 (Owner/DRI) — MISSING bestätigt.** Keine Quelle nennt Person, Rolle oder Organisation.
  ⚠️ Die einzigen `owner`-Treffer in den Quellen sind **Datenbank-Spaltennamen** in SRC-003 §5.3
  (`owner_team_id`, `owner_id`, `owner_type`) — ausdrücklich als Fehlleistungsfalle vermerkt.
- **OQ-003 (Referenzgeräte / Minimum-OS) — MISSING bestätigt, aber nicht leer.** Die Quellen
  **fordern** Referenzgeräte (SRC-001 §3.5; SRC-003 §9 Ledger-Pflichtzeile „Echtes Gerät ✅
  **Modell + OS**"), **benennen** aber weder Modell noch Mindest-OS. In allen vier Dokumenten kommt
  **keine** iOS-/Android-Versionsnummer, **kein** SDK-Level und **kein** Gerätemodell vor.
  **Kein Gerät geraten.**
- **OQ-004 (Karten-/Routinganbieter) — TEILWEISE BELEGT, enger als der Titel.** Vier Quellenstellen
  stimmen überein: Startanbieter **entschieden** (react-native-maps + OpenRouteService), Kriterien
  („Google-Preise, ORS-Limits"), Alternativen („Mapbox, MapLibre+OSM"). Offen ist allein der
  **finale Kosten-ADR**. **Nicht geschlossen** — Nutzerentscheidung.
  ⚠️ **Terminabweichung, nicht geglättet:** alle vier Quellen datieren den ADR **„vor Stufe B" /
  „vor v2.0"**. **Keine Quelle nennt A0 oder A2.** Die Vorziehung auf „vor A0" ist eine
  **projektinterne Ableitung** aus der Proxy-Entscheidung vom 2026-07-19. Beide Termine stehen
  nebeneinander; welcher gilt, ist Nutzerentscheidung.

---

## 4. Manuelle Ankerreview — Verteilung und offene Zeilen

Ankersemantik wird **ausschließlich** über diese Tabelle geführt. Es wurde **kein** neuer
Semantikvalidator gebaut. Quelle: `scratchpad/semantic-review.md` (40 Datenzeilen, 7 Spalten,
maschinell auf Struktur geprüft; jede Reviewer-Zelle trägt den Vermerk *agentgeneriert / keine
menschliche Freigabe*).

| Status | Anzahl | Anteil | Vorfassung |
|---|---:|---:|---:|
| `trägt` | **2** | 5,0 % | 5 |
| `trägt-teilweise` | **23** | 57,5 % | 20 |
| `trägt-nicht` | **7** | 17,5 % | 9 |
| `kein-Anker-vorhanden` | **8** | 20,0 % | 6 |
| **Summe** | **40** | 100 % | 40 |

**Nur 2 von 40 Zeilen sind beidseitig eindeutig belegt.** Eine reine Existenzprüfung hätte
**40/40 PASS** gemeldet — das ist der Grund, warum diese Review manuell und nicht maschinell
geführt wird.

**Alle 7 `trägt-nicht`:**
Vision (3, sämtlich VIS-008 — Metriktrennung gegen einen fremden Gegenstand):
**TRC-024** (Anti-Cheat; geteilt ist nur das Wort „Fairness" — Gegenprobe über VIS-001…011: kein
Item nennt Betrug, Manipulation, Verifikation → **kein Ersatz, BLOCKER**),
**TRC-026** (Team-Territory; Ersatz VIS-004+VIS-005 vorhanden, ohne neue ID reparierbar),
**TRC-028** (Einzel-Reviere; Ersatz VIS-004, reparierbar).
Canvas (4, durchweg Rollenfehler in der Primärspalte):
**TRC-010** und **TRC-012** (Erfolgssignale CAN-126/CAN-125; Ersatz CAN-052),
**TRC-013** (CAN-124 „W4-Retention"; gesamte Ankermenge ohne Capability-Item → **BLOCKER**),
**TRC-029** (CAN-107 ist ein **Risiko**, RISK-018 → **kein Ersatz, BLOCKER**).

**Alle 8 `kein-Anker-vorhanden`** — sämtlich Vision-Spalte, sämtlich BLOCKER, sämtlich als
sichtbare Lücke die richtige Behandlung: **TRC-006** (Routenplanung), **TRC-007** (routenbezogener
Fortschritt), **TRC-019** (Routenempfehlungen/Feed), **TRC-031** (Sturzerkennung), **TRC-032**
(Wearables) — diese fünf **ohne reservierte VIS-ID** —, sowie **TRC-038** (VIS-012), **TRC-039**
(VIS-013), **TRC-041** (VIS-014), je `reserved` mit Inhalt MISSING.

**Offengelegte Gewichtungsregel** statt stillschweigender Anwendung: *eine unbelegte Klausel stuft
herab, wenn das zugehörige AC sie prüft.* Sie ist diskriminierend, kein Rettungsinstrument — sie
hält zwei Zeilen (TRC-002, TRC-015) und stuft drei herab (TRC-020, TRC-030, TRC-033).

**Querschnitt.** Der wiederkehrende Defekt zeigte eine **dritte Form**: nicht der falsche und nicht
der erschlossene Anker, sondern die **zusammenfassende Wertung** — „nahezu satzgleich", „wortgleich
im tragenden Attribut". Beide Formulierungen sind wahr und verdecken trotzdem, dass die Hälfte der
Klauseln unbelegt ist. Zweithäufigster Fehler: **inkonsistente Anwendung eigener Maßstäbe**,
dreimal nachgewiesen (TRC-020/021, TRC-030/031, TRC-033/011) — in **allen drei Fällen war die
günstigere Bewertung die falsche.**

---

## 5. Aktive Blocker nach Gate

**Zerlegungsregel:** jeder Blocker wird **genau einmal** gezählt, am **frühesten** Gate, das er
blockiert. Ein Blocker, der A0 und B blockiert, steht unter A0. Quellen dieser Zerlegung:
`docs/ID-REGISTRY.md` §8 (37 offene Punkte), `docs/decisions/open-questions.md` (15 offene OQ),
**`docs/SOURCE-MAP.md` §2/§5** und die sechs fehlgeschlagenen Validatorkriterien.
**Die vorige Fassung hatte `docs/SOURCE-MAP.md` sowie OQ-003/OQ-004 ausgelassen — sie sind hier
vollständig enthalten.**

| Gate | Anzahl | Blocker |
|---|---:|---|
| **P0** | **6** *(vorher 7 — Runde 6 hat einen Blocker geschlossen, siehe §5.3)* | OQ-002 Owner/DRI (*„vor P0 Start"*, betrifft alle 40 REQ + 8 NFR) · CAN-016…CAN-021 inhaltlich MISSING (§8 #1 — **der genannte Grund für `BLOCKED_TRACEABILITY`**, 14 REQ mit `canvas-problem = MISSING`) · **Entscheidungstranche 2 (2026-07-19) ohne SRC-ID** (SOURCE-MAP §2.1) · **Entscheidungstranche 3 (2026-07-20) ohne SRC-ID** (SOURCE-MAP §2.2; CAN-099/139/141 wurden auf ihrer Grundlage auf `EXPLICIT` gehoben) · ~~**Repository hat keinen ausführbaren Validator und keine gemeinsame Blocking-Implementierung** (§8 #13 + #33)~~ **RESOLVED Runde 6 2026-07-20** — `scripts/validation/run_all.sh` läuft repo-relativ, Exit-Code identisch zum dokumentierten Erwartungslauf, `blocking_model.py` importierbar aus der Kette · **C2**: 5 unbegründete Nullwerte in `docs/plans/2026-07-20-p0-spikes.md:390–394` · §8 #30/#44 Dokument-Nachzüge Auftau-Schritt 2 und Runde 4 |
| **A0** | **8** | **OQ-003 Referenzgeräte + Minimum-OS** (*„vor A0 Feldtest"*) · **OQ-004 Karten-/Routinganbieter** (projektintern vor A0 gebucht; **Quellen sagen „vor Stufe B"** — Divergenz offen) · **P02-a**: `raw` als vierter `quality`-Wert nirgends dokumentiert, **keine OQ-ID → BLOCKER** · **P03-a**: „ohne Datenverlust" ohne Bezugsgröße (Nullschwelle auf *Aktivitäten*, Journaling-Intervall MISSING), **keine OQ-ID → BLOCKER** · CONTRA-006 A0-lokal ↔ serverseitiger Routing-Proxy (§8 #8) · §8 #17 `decision_reference` nennt einen ADR, der nicht existiert · §8 #10 Architektur §9 überholt (Proxy/Public Key) · REQ-004/REQ-005: PRD und Traceability nennen **unterschiedliche** Canvas-Anker |
| **A1** | **1** | OQ-006 Claims-Whitelist (*„vor A1 Public Beta"*) — bis dahin bleibt Health-Copy intern |
| **A2** | **13** | OQ-001 Produktname · OQ-015 Vergleichbarkeitsdefinition (REQ-042) · OQ-016 Referenz-Fremdanwendung (REQ-039) · §8 #37 REQ-037/038/039 ohne `canvas-problem`-Anker · §8 #19 **VIS-012** · §8 #20 **VIS-013** · §8 #38 **VIS-014** · §8 #15 VIS-011 unbestätigt (REQ-037) · §8 #36 CAN-139-Wortlaut ↔ AC-039 (d) · §8 #24 Wortlautbestätigung Runde 3 · §8 #43 Wortlautbestätigung Runde 4 · **C8** REQ-042 `RESEARCH_HYPOTHESIS` ohne `research_plan` · **C12** REQ-038 `EXPLICIT` ohne tragenden Beleg |
| **B** | **6** | OQ-005 Backend · OQ-009 Retention (*vor B/D*) · OQ-010 Moderations-SLA (*vor B Public*) · OQ-012 Telemetrie CAN-130 · OQ-014 Stichprobenregel CAN-130 · **REQ-019 ohne tragenden Vision-Anker** (§8 #41; REQ-019 ist Stufe **B**) |
| **C** | **2** | OQ-007 Geschäftsmodell · OQ-008 Effort-/Territory-/Bahngold-Startwerte (*vor C/D*) |
| **D** | **0** | — kein Blocker, der **erstmals** bei D greift (OQ-008/OQ-009 sind bei C bzw. B gezählt) |
| **E** | **1** | §8 #21 kein Vision-Item für REQ-032 (Wearables, Stufe **E**), keine reservierte VIS-ID |
| **Gate-übergreifend / ohne Gate** | **12** *(vorher 14 — Runde 6 hat zwei Blocker geschlossen, siehe §5.3)* | **C7** (erfordert laufenden Code — bei **jedem** Gate offen) · **OQ-013 NFR-008: Gate MISSING — kein Gate referenziert NFR-008** · **85 `EXPLICIT`-Zellen ohne Quellenangabe** (SOURCE-MAP) · **5 UNBELEGTE Canvas-Zellen** (CAN-041/042/046/110/112) · CAN-113 falsch adressiert · CAN-051 Quelle deckt Kern nicht · 13 Herabstufungen mit entfallener Prämisse, neu zu bewerten · Datumsdiskrepanz · ~~zwei Fassungen von SRC-001…003~~ **RESOLVED Runde 6 2026-07-20** — `docs/sources/` hält die Desktop-Fassung als kanonisch mit SHA-256-Hashes in `scripts/validation/HASHES.md`; Downloads-Fassung ausdrücklich als älterer Nebenstand nicht kopiert · ~~`CLAUDE.md` nennt nicht existierende Pfade~~ **RESOLVED CONTRA-001** (frühere Runde) — nun auf die vier Plumbline-Kernartefakte ausgerichtet · **A0/A1/A2 kommen in keiner Quelle vor** · §8 #12 VC-001…VC-036 ohne Definitionsdatei · §8 #11 Präfixaufnahme · 7 §8-Punkte nie einem Berichtsabschnitt zugeordnet (22, 23, 26, 27, 30, 41, 44) |
| **Summe** | **49** *(vorher 52 — 3 Blocker in Runde 6/CONTRA-001 geschlossen; Details §5.3)* | ohne Doppelzählung |

### 5.3 Runde-6-Schließungen (2026-07-20) — drei Blocker

Die Schließungen sind mechanisch nachweisbar; keine hebt einen NUTZERentscheidungsblocker auf.
Reales Belegniveau, nicht Wortlaut: `real-boundary` für Werkzeuge und Quellen im repo-eigenen Sinn
(reproduzierbar aus einem Klon, byte-identisch zu den Originalen).

| Blocker (vorher) | Was ihn schließt | Nachweis |
|---|---|---|
| „Repository hat keinen ausführbaren Validator" (§8 #13 + #33, P0) | `scripts/validation/run_all.sh` mit 11 Werkzeugen; `blocking_model.py` importierbar; `selftest_validator.py` 13/13 scharf | Lauf Runde 6: **`ZUSAMMENFASSUNG: PASS=6 FAIL=4 INFO/SKIP=1`**, Exit `1` — Zeile für Zeile identisch mit dem in `scripts/validation/README.md` dokumentierten Erwartungslauf. Keine Validatorlogik geändert. |
| „zwei Fassungen von SRC-001…003" (Gate-übergreifend) | `docs/sources/SRC-001…004` mit SHA-256, Desktop-Kanonik in `docs/SOURCE-MAP.md` §1.1 fixiert, Downloads-Fassung ausdrücklich als älterer Nebenstand nicht kopiert (`scripts/validation/HASHES.md` §1.1 „Nicht kopiert, bewusst") | Hash-Vergleich: SRC-001 `d0a6adf4…74f0d3`, SRC-002 `37e090aa…d16542`, SRC-003 `c3ceb46f…e3764d`, SRC-004 `dc18a97d…7bc25f`. Original = Repo-Kopie = Soll-Hash aus §1.1 — „identisch (3/3)". |
| „`CLAUDE.md` nennt nicht existierende Pfade" (Gate-übergreifend) | CONTRA-001-Fix früherer Runde: Dokumenten-Hierarchie zeigt auf `docs/canvas/…canvas.md`, `docs/prd/…prd.md`, `docs/vision/…vision.md`, `docs/traceability.md` — alle existieren. | 4 explizit benannte Pfade in `CLAUDE.md` § „Document Hierarchy" alle auflösbar. |

**Was ausdrücklich NICHT geschlossen wurde:** die drei Werkzeugdefekte aus §5.2 (`verify.py`,
`verify_canvas.py`, `oq_check.py`) bleiben offen; der P0-Blocker **§8 #30/#44
Dokument-Nachzüge** bleibt offen (er ist eine Reihe von Nachzügen, nicht Werkzeugfähigkeit);
alle fünf **N1…N5-Nutzerentscheidungen** aus §6 bleiben stehen. Die Runde-6-Schließungen
reduzieren die Blockerzahl **von 52 auf 49**, ohne einen einzigen Nutzerentscheidungspunkt zu
berühren.

### 5.1 Zwei SOURCE-MAP-Blocker gegen meine eigenen Dateien — beide durch Messung widerlegt

Beide sind an mich adressiert. Ich lege die Messung offen und **schließe sie nicht selbst**;
`docs/SOURCE-MAP.md` gehört einem anderen Owner.

1. **„`validation-report.md` führt `blocking_scope` weiterhin als lebendes Feld samt der alten,
   defekten Formel" (SOURCE-MAP §5) — trifft nicht zu.** `blocking_scope` kommt im Bericht an
   **zwei** Stellen vor, beide als **Reparaturprotokoll**: M18 dokumentiert die Entfernung, und
   sein Subjekt ist **`nfr-audit.json`**, nicht dieser Bericht; §8-Punkt 32 dokumentiert
   „0 Verwendungen als Feld". Eine feldförmige Zeile existiert nicht (maschinell geprüft). Die
   einzige genannte Formel ist die **korrigierte**: `status NOT IN [resolved]`, fail-closed.
   Der Befund liest eine Zeile, die die Behauptung nicht trägt — **dieselbe Defektklasse**, die
   dieser Bericht dokumentiert.
2. **„`intake-package.json` divergiert mit Runde 4 in *jeder* Zeile" (SOURCE-MAP §5) — trifft
   nicht zu.** Gemessen gegen die registry-abgeleiteten Zählstände: REQ 40 ✓ · AC 41 ✓ · EV 42 ✓ ·
   TRC 40 ✓ · CAN 123 ✓ · VIS 11 ✓ · OQ 16 (15 offen, 1 resolved) ✓ · 12 verwaltete Präfixe ✓.
   **Null Divergenzen.** Was tatsächlich veraltet war, war der `validation`-Block (`33/5` statt
   `32/6`) — das habe ich in dieser Runde korrigiert (§9).

### 5.2 Drei Werkzeugbefunde, die NICHT als bestanden gewertet wurden

Sie sind **nicht** korrigiert worden (Freeze) und gelten weiter als offen:

| Werkzeug | Ausgabe | Diagnose |
|---|---|---|
| `verify.py` | `FAILS 1` — gezählt `{linked 28, broken 8, linked-partial 3, not-linked 1}` gegen `claimed {linked 31, broken 6, not-linked 1, linked-partial 2}` | Das **Dokument ist aktuell**; das `claim` ist ein **hartkodiertes Literal im Werkzeug** und veraltet. Werkzeugdefekt — und exakt die Bauform, die C26 im Prüfwerkzeug verbietet |
| `verify_canvas.py` | `TABLE@187 uneven column counts {6:[187–190], 8:[214]}` | Zeile 214 (CAN-139) enthält **maskierte Pipes** (`\|`) in einem Zitat; der Spaltenzähler honoriert die Maskierung nicht. Markdown-seitig ist die Tabelle korrekt — **Falschmeldung** |
| `oq_check.py` | `FAIL: decision denoted by more than one OQ-ID: UNCLASSIFIED -> [OQ-012…OQ-016]` | Der Themenklassifikator kennt die fünf in Runde 3/4 angelegten OQ-IDs nicht; alle fünf fallen in denselben Sammelwert. Der Folgebefund ist daraus **abgeleitet** und deshalb **nicht belastbar** |

---

## 6. Verbleibende echte Nutzerentscheidungen — fünf

Alles andere ist Nachzugsarbeit eines Owners und braucht **keine** Nutzerentscheidung.

| # | Entscheidung | Warum nur der Nutzer | Blockiert |
|---|---|---|---|
| **N1** | **Owner/DRI benennen** (OQ-002) | organisatorisch, aus keiner Quelle ableitbar | **P0-Abnahme** insgesamt: 40 REQ, 8 NFR, beide Spikes |
| **N2** | **Inhalt von CAN-016…CAN-021 bestätigen oder verwerfen** | sechs Problemaussagen, die niemand außer dem Nutzer setzen darf | der **genannte Grund** für `BLOCKED_TRACEABILITY`; 14 REQ mit `canvas-problem = MISSING` |
| **N3** | **SRC-IDs für die Entscheidungstranchen 2 und 3 vergeben** | Provenienz von Nutzerentscheidungen; Registry eingefroren, keine ID darf erfunden werden | die `EXPLICIT`-Einstufung von CAN-099/139/141 und ~50 Freitextstellen „Nutzerentscheidung 2026-07-19/20" |
| **N4** | **Referenzgeräte + Minimum-OS festlegen** (OQ-003) | keine Quelle nennt Modell, Version oder SDK-Level; **nichts wird geraten** | **A0-Feldtest**; beide P0-Spikes sind baubar, aber nur **eingeschränkt abnehmbar** (`real-boundary-smoke`) |
| **N5** | **VIS-Lücken entscheiden**: Wortlaut für VIS-012/VIS-013/VIS-014 **und** zwei bisher **nicht reservierte** VIS-IDs für REQ-007 und REQ-019 | Vision-Aussagen sind Produktzusagen; VIS-013 wäre sonst ein Ebenensprung aus einer Compliance-Matrix | TRC-007, TRC-019, TRC-038, TRC-039, TRC-041 |

**Bewusst nicht in dieser Liste:** OQ-004. Startanbieter, Kriterien und Alternativen sind belegt;
offen ist nur der finale Kosten-ADR — und der ist **vor Stufe B** fällig, nicht vor P0. Er als
sechste Entscheidung zu führen hieße, die Termindivergenz zugunsten der strengeren Lesart still
zu entscheiden.

---

## 7. Sind Vision und Canvas bestätigungsfähig?

### Canvas: **nein** — Änderung gegenüber der Vorfassung. Vision: **nein**.

**Die Vorfassung führte „Canvas: ja, mit einem benannten Vorbehalt". Das ist nicht mehr haltbar.**
Zum Zeitpunkt jener Aussage war die Quellenprüfung nicht durchgeführt. Sie hat seither **fünf
UNBELEGTE Zellen** ergeben (CAN-041, CAN-042, CAN-046, CAN-110, CAN-112) — Aussagen, die in
**keiner** der vier Quellen vorkommen und die **noch nicht herabgestuft** sind. Dazu **CAN-113**
(falsch adressiert) und **CAN-051** (Quelle deckt den Kern nicht). Ein Canvas mit sieben
belegmängelbehafteten Zellen ist nicht bestätigungsfähig, und ein „Ja mit Vorbehalt" würde genau
diese sieben unter dem Vorbehalt verschwinden lassen.

**Canvas — Begründung im Einzelnen:**
- 77 von 90 geprüften Zellen stehen **wortnah** in SRC-001/SRC-003 — die Belegbasis ist tragfähig.
- Aber: **6 reservierte Items (CAN-016…021) sind inhaltlich leer** und vom Nutzer unbestätigt.
- **5 Zellen sind UNBELEGT**, 2 weitere falsch bequellt — Herabstufung erforderlich, in dieser
  Runde ausdrücklich **nicht** vorgenommen (fremdes Eigentum).
- **85 `EXPLICIT`-Zellen nennen überhaupt keine Quelle** und sind damit **nicht prüfbar**.
- Die dritte Entscheidungstranche, auf der CAN-099/139/141 als `EXPLICIT` stehen, hat **keine
  SRC-ID** — der Beleg ist kein referenzierbares Artefakt.

**Vision — Begründung im Einzelnen (deutlicher Fall):**
- Von 40 Traceability-Zeilen haben **8 keinen Vision-Anker**, davon **5 ohne reservierte ID**.
- **VIS-011** ist `ASSUMPTION` und unbestätigt — zählt nach §8 #15 **nicht** als erfüllter Anker.
- **VIS-012, VIS-013, VIS-014** sind `reserved` mit Inhalt **MISSING**.
- Nur **11** aktive Vision-Items tragen **40** Requirements — und die manuelle Review weist nur
  **2 von 40** Zeilen als beidseitig eindeutig belegt aus.
- **VIS-013** wäre, so wie er heute belegbar ist, ein **Ebenensprung** aus einer
  Store-Compliance-Matrix in eine Produktzusage.

---

## 8. Kann P0 beginnen — und mit welchen Tasks?

### **Bauen: ja, zwei Tasks. Abnehmen: nein — für keinen von beiden.**

Diese Trennung ist der Kern der Antwort. Wer sie zusammenzieht, bekommt entweder ein falsches
„nein" (Arbeit steht still, obwohl sie laufen könnte) oder ein falsches „ja" (Ergebnisse gelten
als abgenommen, obwohl niemand sie abnehmen darf).

| Task | Bauen? | Abnehmen? | Einschränkung |
|---|---|---|---|
| **P0-02** TrackPointV1 (REQ-004 / AC-004 / EV-004, GATE-A0) | **ja**, als **technischer Spike** | **nein** | kein Owner (N1) · Referenzgeräte MISSING (N4) → EV-004 `real-boundary-smoke` nicht erreichbar · **P02-a** offen: `raw` als vierter `quality`-Wert nirgends dokumentiert, **keine OQ-ID** |
| **P0-03** Lokale Persistenz (REQ-005 / AC-005 / EV-005, GATE-A0) | **ja**, als **technischer Spike** | **nein**, und **eine Hälfte ist strukturell blockiert** | wie oben, zusätzlich: **OQ-009 (Retention) → EV-042 `blocked`** macht die zweite Hälfte der Task-Acceptance („Identität und historische Aggregate im Schema getrennt", CONTRA-005) **nicht abnehmbar** · **P03-a** offen: „ohne Datenverlust" hat keine Bezugsgröße |

**P0-01 kann nicht beginnen** — der Delivery Plan legt für P0-01 bereits offen, dass die
Task-Acceptance den geforderten Nachweis nicht abdeckt; dieselbe Lücke besteht bei **P0-02**
(**P02-b**: „Schema + Fixtures + Serialisierungstest" deckt den von AC-004 geforderten
**deterministischen Filter** nicht ab).

**Was P0-03 ausdrücklich NICHT tun darf:** ein Schema **finalisieren**. Die Zeitpunktregel lautet
„vor Schema-Finalisierung", und OQ-009 ist offen. **Wegwerfschema erlaubt, Finalisierung nicht.**
Wer P0-03 danach als erledigt führte, ließe die blockierte Hälfte über die lieferbare gelten — die
Fehlerform, wegen der CAN-140/EV-040 überhaupt geteilt wurden.

**Auftrags-/Plan-Abweichung, weder übernommen noch gestrichen:** der Auftrag nennt für P0-03 nur
REQ-005, der Delivery Plan **REQ-005 + REQ-017 + REQ-027** — und die beiden zusätzlichen tragen
genau die blockierte Acceptance-Hälfte.

**MISSING, nicht geraten:** Verwurfsquote · Journaling-Intervall · Chunk-Größe ·
Schreiblatenz-Ziel · Referenzstrecke und Wiederholungszahl (NFR-001) · Begründung des
30-Minuten-Fensters · Ort für das Tunnel-Fixture.

**Reihenfolge, wenn der Nutzer starten will:** N1 und N4 zuerst — sie allein verwandeln „bauen,
aber nicht abnehmen" in „bauen und abnehmen". N2, N3 und N5 blockieren die **Bestätigung** von
Canvas und Vision, nicht den **Bau** der beiden Spikes.

---

## 9. Freeze-Vermerk

**Gültig ab Abschluss dieser Runde (2026-07-20).** Kanonischer Ort:
`docs/ID-REGISTRY.md` §13 — dort ohne jede ID-Änderung eingetragen.

**Eingefroren sind:**
- das **Metamodell** — Achsen und Vokabulare (`source_type`, `measurement_type`,
  `evidence_status`, `item_type`, Release-Stufen), die Blocking-Formel
  `status NOT IN [resolved]` (fail-closed), die Beschränkung von `blocking` auf `OQ-`/`CONTRA-`,
  die Zählregel §10.2;
- die **Validatorkette** — `validate_intake.py`, `validate_trace.py`, `check_prd.py`,
  `validate_schema.py`, `selftest_validator.py`, `verify.py`, `verify_canvas.py`, `xcheck.py`,
  `oq_check.py`, `blocking_model.py`, `intake-package.schema.json`;
- die **Ankersemantik** — sie wird **nicht** weiter maschinell geführt, sondern ausschließlich
  **review-geführt** (§4). Es wurde **kein** neuer Semantikvalidator gebaut.

### ⚠️ 9.1 Die Werkzeuge sind KEINE Repository-Dateien — offener Punkt, kein gelöster

`blocking_model.py` und **sämtliche** genannten Werkzeuge liegen im **Scratchpad** dieser Session:

```
/private/tmp/claude-501/-Users-vincentschnetzer-Documents-Run-Bike/
    5ad02448-3a52-4a17-affc-d652ef4b5345/scratchpad/
```

Unbeschönigt:

- **Ein Freeze ändert daran nichts.** Eingefroren wird ein Stand, kein Ablageort.
- **Außerhalb dieser Session sind sie nicht verfügbar.** Jedes in diesem Bericht genannte
  Validatorergebnis ist dann **nicht reproduzierbar** — weder für den Nutzer noch für einen
  späteren Agenten.
- **Registry §8 Punkt 13** („kein ausführbarer Validator für die Regeln in Abschnitt 2") und
  **§8 Punkt 33** („keine gemeinsame Implementierung der kanonischen Blocking-Funktion") bleiben
  **OFFEN**. Die Scratchpad-Werkzeuge schließen sie **nicht**. Sie sind deshalb in §5 als
  **P0-Blocker** geführt und nicht als erledigt verbucht.
- **Registry §9** beschreibt weiterhin einen **Soll**-, keinen Ist-Zustand des Repositorys.

Die Überführung ins Repository ist ein **eigener, ausdrücklich zu beauftragender Schritt**. In
dieser Runde **nicht erfolgt und nicht begonnen** — kein Verzeichnis angelegt, keine Datei kopiert.

### 9.2 Was ein Auftauen erfordern würde

Nur durch ausdrückliche Nutzerentscheidung, und nur bei einem dieser Anlässe:
1. eine **neue oder geänderte SRC-Quelle** (inkl. Aufnahme des Konzeptdokuments als Quelle);
2. eine **neue ID-Klasse** oder ein **neues Achsenvokabular**;
3. eine **Nutzerentscheidung, die eine bestehende Achse umdefiniert**;
4. die **Überführung der Werkzeuge ins Repository** (§9.1) — selbst ein Eingriff in den Stand.

**Ausdrücklich kein Auftaugrund: ein fehlgeschlagener Check.** Ein Fehlschlag ist ein **Befund**
und wird am **Dokument** behoben, nicht am **Werkzeug**. Die drei bekannten Werkzeug-Falschmeldungen
(§5.2) sind deshalb bewusst **nicht** korrigiert worden.

### 9.3 Letzte Änderung vor dem Freeze — offengelegt

`intake-package.schema.json` wurde **additiv** erweitert (`validation.run_date`, `.run_scope`,
`.delta_to_previous_run`, `.failed_check_diagnosis`, `.other_validators`, root `tooling_freeze`),
damit `intake-package.json` die **echte** Ausgabe des Laufs vom 2026-07-20 tragen kann. Ohne diese
Erweiterung wäre die Datei nur dadurch schemakonform geblieben, dass sie den veralteten Stand
`33/5` weitergeführt hätte. **Keine Regel gelockert, kein Feld entfernt, kein Pflichtfeld optional
gemacht.** Protokolliert in `x_schema_change_log`.

**Nicht eingefroren:** Dokumentinhalte, Blocker-Auflösungen, ID-Vergabe durch den Nutzer, manuelle
Ankerreview.

---

## Anhang — echte Validatorausgabe, Lauf vom 2026-07-20

| Werkzeug | Ergebnis |
|---|---|
| `validate_intake.py` | **BESTANDEN 32/38 · FEHLGESCHLAGEN 6** → `C2`, `C3c`, `C3d`, `C7`, `C8`, `C12` |
| `validate_trace.py` | **FAILS 0 · WARNS 0** (40 aktive REQ abgeleitet; TRC-014/TRC-040 deprecated) |
| `check_prd.py` | **FAILURES 0** (alle CONTRA-`blocking`-Werte maschinell nachgerechnet) |
| `selftest_validator.py` | **13/13 Werkzeug-Negativkontrollen scharf** |
| `xcheck.py` | **0 Divergenzen** (Registry 123 aktive CAN == Canvas 123 Definitionszeilen) |
| `validate_schema.py` | **konform** — zu einem in diesem Lauf **selbst verfassten** Schema. **Kein Standardnachweis.** |
| `verify.py` | **FAILS 1** — D-Tally gegen hartkodiertes Literal (§5.2) |
| `verify_canvas.py` | **1 Problem** — `TABLE@187`, maskierte Pipes (§5.2) |
| `oq_check.py` | **FAIL** — Klassifikator kennt OQ-012…OQ-016 nicht (§5.2) |
| `AUDIT_points.py` | **37 offene §8-Punkte**; nie zugeordnet: 22, 23, 26, 27, 30, 41, 44 |

**Nicht erfüllte Kriterien im Klartext:**

| ID | Art | Owner | Befund |
|---|---|---|---|
| **C2** | Dokumentdefekt (**neu**) | Spike-Plan | 5 Nullwerte ohne Begründung, `2026-07-20-p0-spikes.md:390–394` |
| **C3c** | Werkzeug-Limitation | Traceability | `traceability.md:1588` nennt TRC-040 in **Prosa**; Ankerwert der Zelle ist VIS-003 |
| **C3d** | Werkzeug-Limitation | Traceability | `traceability.md:480` nennt VIS-014 als **Begründung**, nicht als erfüllten Anker |
| **C7** | strukturell unerreichbar | — | erfordert laufenden Code; **ein Dokumentenlauf kann dieses Kriterium nicht bestehen** |
| **C8** | Dokumentdefekt | PRD | REQ-042 `RESEARCH_HYPOTHESIS` ohne `research_plan` |
| **C12** | Dokumentdefekt (bestritten) | PRD / Canvas | REQ-038 `EXPLICIT` allein aus qualitativer Ankerabsicht. Der PRD-Text behauptet „belegt, nicht hochgestuft" — **die Prüfung gilt, nicht der Text** |

**Weder C3c noch C3d wurden als bestanden gewertet**, obwohl beide als Werkzeug-Limitation
diagnostiziert sind. Eine Diagnose hebt einen Fehlschlag nicht auf.

---

**Gesamtstatus: `BLOCKED_TRACEABILITY`** · `true-line-status` `pending-watcher` ·
`wired-in-prod` `no` · `evidence-class` `none` · `self-certified` `false`.
Kein Code, kein Verzeichnis, keine AWS-Ressource, keine ID vergeben, keine Quelldatei kopiert oder
verändert, keine fremde Datei geändert.
