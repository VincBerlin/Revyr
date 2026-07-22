# Traceability Matrix

Feature Slug: `revyr-endurance-platform`
Status: linked – **READY_FOR_USER_CONFIRMATION** (nicht bestätigt)
Gesamtstatus des Vorhabens: **BLOCKED_TRACEABILITY** (unverändert)
Stand: 2026-07-20 (Nachzug auf den ID-Bestand nach **Runde 4**: Ersetzung der belegten semantisch
falschen Anker, Teilung von REQ-040, kanonische Trennung EV-008/EV-039)

## 0. Geltung, ID-Disziplin und was diese Datei *nicht* tut

- **Kanonische ID-Quelle ist `docs/ID-REGISTRY.md`.** Diese Matrix referenziert ausschließlich
  dort registrierte IDs. Sie vergibt, benennt und deprecated **keine** ID. Die Registry ist ab
  Phase 2 eingefroren; wo eine benötigte ID fehlt, steht hier ein **BLOCKER**, keine erfundene ID.
- **Alle Messfelder** (`Measurement Type`, `Signal / Control Evidence`, `Target / Pass Condition`,
  `Measurement Window`, `Evidence Source`, `Source Type`, `Owner`, `Release Gate`, `Rationale`,
  `Research Plan`) stammen unverändert aus dem Messmodell und — für die am 2026-07-19 neu
  hinzugekommenen Requirements — **wörtlich aus der `canonical_file` `docs/prd/…prd.md`**.
  Kein Wert wurde ergänzt, gerundet oder geschätzt.
- **Diese Matrix bestätigt nichts.** Sie setzt keinen Status auf `user-confirmed` oder
  `READY_FOR_AGILETEAM_PLANNING` und gibt kein Plumbline-Watcher-Verdikt ab.
- `true-line-status` steht bei **allen aktiven Requirements** auf `pending-watcher`,
  `wired-in-prod?` bei allen auf `no`, `evidence-class` bei allen auf `none` — es existiert kein
  Code und kein `mobile/`-Verzeichnis. Das gilt ausdrücklich auch für die vier am 2026-07-19 neu
  hinzugekommenen Requirements.
- **Kein Nullwert ohne Begründung.** Wo ein Feld leer bliebe, steht `MISSING`, `ASSUMPTION`,
  `BLOCKER` oder `OPEN QUESTION` mit requirement-spezifischer Begründung. Pauschales
  „nicht relevant“ oder „später“ kommt nicht vor.

### 0.0 Zählregel — keine hartkodierte Anzahl

Die Zahl aktiver Requirements ist **abgeleitet**, nicht festgeschrieben (Registry Regel 11,
§10.1). Sie wird aus `docs/ID-REGISTRY.md` §6.4 gewonnen:

```
aktive_requirements = |{ e ∈ Registry : praefix(e.id) = "REQ"
                                    ∧ e.status = "active"
                                    ∧ e.status ≠ "template-placeholder" }|
```

**Aus der Registry geparst am 2026-07-20: 40.** Ausgeschlossen sind `REQ-000`
(`template-placeholder`, Registry §4) sowie `REQ-014` und `REQ-040` (`deprecated`). Herleitung:
REQ-001…REQ-042 sind vergeben (42 IDs), davon zwei deprecatet → 40. Ableitungsweg und Datum
stehen hier, weil Registry §10.2 Bindung 4 sie verlangt.

⚠️ **Weder 36 noch 39 ist ein gültiger Erwartungswert — und keine der beiden Zahlen darf
verboten werden.** Registry §10.2 Bindung 2 stellt ausdrücklich fest, dass ein *Verbot* eines
Literals ein Werkzeug genauso an einen Zählstand bindet wie seine *Erwartung*. Die Vorfassung
dieses Abschnitts verbot „36" und band die Datei damit an einen Altstand — das ist korrigiert.
Keine Prüfung dieser Datei darf eine feste Anzahl erwarten **oder** ausschließen; jede solche
Prüfung ist zu korrigieren, **nicht die Daten**.

Dasselbe gilt für die implizite 1:1-Beziehung REQ ↔ AC ↔ EV: **41 aktive AC und 42 aktive EV
gegen 40 REQ sind korrekt**, weil REQ-019 seit dem 2026-07-19 zwei Acceptance Criteria (AC-019
funktional, AC-041 Messkriterium) und zwei Evidences (EV-019, EV-041) trägt und EV-042 an
CONTRA-005/REQ-017/REQ-027 hängt (Registry §6.5.1, §10). **TRC bleibt 1:1 zu REQ (40).**

**Bekannter Folgebefund, hier nicht geglättet:** die Spalte `value-check-id` (§5) führt
`VC-001`…`VC-036` und bildet damit einen **Altstand** ab. Für REQ-037, REQ-038, REQ-039, REQ-041
und REQ-042 existiert **keine VC-ID** — sie wird hier **nicht erfunden** (`VC-` ist nicht
registry-verwaltet, Registry §5.2, und die IDs haben ohnehin keine Definitionsdatei). Die Lücke
ist durch die Teilung von REQ-040 in Runde 4 um einen Fall **größer** geworden, nicht kleiner.
Siehe §5 und §6.6.

### Ablösung der Ad-hoc-Facetten-IDs

Die frühere Fassung dieser Datei führte eigene Facetten-Kennungen (`CAN-001-a`, `CAN-003-v1`, …),
die in keiner Registry standen. Sie sind gemäß `docs/ID-REGISTRY.md` §7.2 vollständig durch
atomare CAN-IDs ersetzt und werden hier **nicht mehr verwendet**:

| Facette (entfallen) | Atomare CAN-ID |
|---|---|
| `CAN-001-a` | CAN-013 |
| `CAN-001-b` | CAN-014 |
| `CAN-001-c` | CAN-015 |
| `CAN-003-p1` | CAN-028 |
| `CAN-003-v1` … `CAN-003-v5` | CAN-029 … CAN-033 |
| `CAN-009-a` | CAN-124 |
| `CAN-009-b` | CAN-125, CAN-126 |
| `CAN-009-c` | CAN-127, CAN-128, CAN-129 |

Ebenso sind die Sammelblock-IDs `CAN-001` … `CAN-012` (deprecated) aus allen Spalten entfernt.
Die Zuordnung `CAN-002 → USER-001/002/003` ist durch die atomaren Zielnutzer-Items
CAN-023, CAN-024, CAN-026 und CAN-027 ersetzt; CAN-025 bleibt ein BLOCKER (siehe §6).

### 0.1 Korrekturprotokoll dieses Nachzugs (2026-07-19)

Dieser Schritt vergibt **keine** ID. Die Registry ist eingefroren; alle unten verwendeten IDs
sind dort bereits registriert. Geändert wurden ausschließlich Felder dieser Datei:

| # | Was | Vorher | Nachher | Registry-Beleg |
|---|---|---|---|---|
| 1 | **Vision-Anker REQ-014** — die zentrale Korrektur dieses Schritts | VIS-009 (Privacy Boundary) — **fachlich falsch**, null Überschneidung mit Accessibility | **VIS-011 (Accessibility Boundary)**, mit Vorbehalt (siehe unten) | `ID-REGISTRY.md` §6.1 (VIS-011, `active`), §6.1.1 (Prüfung VIS-001…VIS-010) |
| 2 | CONTRA-004/005/006 Statusfelder | Mischwerte in Überschriften (`RESOLVED (Entscheidung)`, `DESIGN-RESOLVED / EVIDENCE-PENDING`) | zwei getrennte Achsen `status` + `evidence_status` nach §3.1, `blocking` abgeleitet | `ID-REGISTRY.md` §3.1, §6.11.1 |
| 3 | REQ-027 `Evidence Needed` / `Evidence Source` | „Unveränderlichkeitsprüfung" (durch DEC-012 ersetzte Formulierung) | neuer EV-027-Titel, **wörtlich** aus der `canonical_file` `prd.md:293` | `ID-REGISTRY.md` §6.6 (EV-027) |
| 4 | NFR-Klassifikation | acht NFRs pauschal `EXPLICIT` (aus dem PRD übernommen) | je NFR getrennte Achsen `source_type` / `evidence_status`, neu §6.7 | keine — `NFR-` war zu diesem Zeitpunkt **nicht** registry-verwaltet; seit dem Auftau-Schritt 2 ist es das (Registry §5.1, §6.13). Korrigiert in §6.6. |

### 0.2 Korrekturprotokoll des ID-Bestands-Nachzugs (2026-07-19, dieser Schritt)

Dieser Schritt vergibt **keine** ID. Alle unten verwendeten IDs stammen aus der eingefrorenen
Registry bzw. aus `scratchpad/id-migration.json`. Geändert wurden ausschließlich Felder dieser
Datei:

| # | Was | Vorher | Nachher | Registry-Beleg |
|---|---|---|---|---|
| 1 | **Zählregel** | „alle 36 Requirements“, an mehreren Stellen hartkodiert (Kopf, §2, §5, §6.2, §8, §10) | abgeleitet aus Registry §6.4, Stand **39**; die 36 ist als Erwartungswert ausdrücklich verboten (§0.0). Verbliebene Nennungen der Zahl 36 beschreiben ausschließlich den **Altstand** oder sind Teil der ID `VC-036`. | Registry Regel 11, §10.1 |
| 2 | **REQ-014 / AC-014 / EV-014 / TRC-014** | aktive Zeilen der Kernmatrix und des Messmodells | **als `deprecated` geführt, nicht gelöscht**; Nachfolger REQ-037/REQ-038 mit vollständigen Pflichtfeldern | Registry §6.4, §6.5, §6.6, §6.7, §7.4.1 |
| 3 | **REQ-008** | „Verlauf, Wiederverwendung und Export“, Canvas-Anker CAN-050/CAN-030, Source Type EXPLICIT | **verengt** auf „Verlauf und Detailansicht“; Canvas-Anker **CAN-138**; Source Type **ASSUMPTION**; GPX → REQ-039, Vergleich → REQ-040 | Registry §6.4 (REQ-008), §7.4.3 |
| 4 | **CAN-071** | in §3 und §6.1 als reservierter Canvas-BLOCKER von REQ-008 geführt | **deprecated**; BLOCKER geschlossen, Nachfolger CAN-138/139/140 | Registry §6.3, §7.4.1 |
| 5 | **CAN-022, CAN-099, CAN-130** | `reserved`, Inhalt MISSING, als BLOCKER gezählt (REQ-032, REQ-014, REQ-019) | **`active`**, inhaltlich entschieden; die drei Canvas-BLOCKER sind geschlossen | Registry §7.4.3, §6.3.2 |
| 6 | **AC-019** | eine AC, die funktionale Prüfung und Kennzahl vermischte | **zwei IDs**: AC-019 (funktional) und **AC-041** (Messkriterium), mit getrennten Evidences EV-019/EV-041 | Registry §6.5.1 |
| 7 | **REQ-032 Persona** | „CAN-025 hat im PRD keine USER-ID“ — BLOCKER | **USER-004** vergeben und primär verankert; ID-Frage geschlossen, Bestätigung offen | Registry §6.12 |
| 8 | **`blocking_scope`** (C16) | ein Feld, das Gates und Tätigkeiten mischte — 20 Vorkommen in dieser Datei | ersatzlos entfallen → **`blocked_gates` + `blocked_activities`**, disjunkte abschließende Wertebereiche, eine kanonische Formel | Registry §3.1, §6.11.1 |
| 9 | **NFR-008** | „verwaist“ — im ganzen Repository nur in seiner eigenen Definitionszeile | **definiert statt deprecatet**; Verwaisung aufgelöst, Messdefinition ist **OQ-013** | Registry §6.13.1 |

**Was dieser Schritt ausdrücklich NICHT tut.** `true-line-status` bleibt bei **allen aktiven**
Requirements `pending-watcher`, `wired-in-prod?` bei allen `no`, `evidence-class` bei allen
`none` — einschließlich REQ-037…REQ-040. Es existiert kein Code. Kein Feld wurde auf
`user-confirmed` oder `verified` gesetzt; es wird kein Plumbline-Watcher-Verdikt ausgestellt.
Der Gesamtstatus bleibt `BLOCKED_TRACEABILITY`, bis der Nutzer die offenen Canvas- und
Vision-Items bestätigt hat.

### 0.3 Korrekturprotokoll Runde 4 (2026-07-20, dieser Schritt)

Dieser Schritt vergibt **keine** ID und deprecatet **keine**. Alle verwendeten IDs stammen aus der
eingefrorenen Registry (§7.5, §6.3.3). Geändert wurden ausschließlich Felder dieser Datei.

| # | Was | Vorher | Nachher | Registry-Beleg |
|---|---|---|---|---|
| 1 | **Vision-Anker REQ-019, REQ-020, REQ-021, REQ-022** | alle vier an **VIS-008** (Fairness Boundary) — trägt ausschließlich getrennte Run-/Bike-Metriken und **keine** Community-Aussage | REQ-019 → **VIS-003**, REQ-020 → **VIS-004**, REQ-021 → **VIS-004**, REQ-022 → **VIS-003**; jede Verknüpfung einzeln begründet, VIS-004 bei REQ-022 geprüft und **verworfen** | §6.6 (TRC-019…022), §7.5.3 |
| 2 | **Canvas-Primäranker REQ-019, REQ-020, REQ-022** | **Erfolgssignale** in der Spalte „Canvas Item (primär, atomar)" (CAN-130, CAN-127, CAN-128) | **Capabilities** CAN-058, CAN-060, CAN-067. Die Erfolgssignale stehen weiter in §4.2, wo sie hingehören | §6.6 (TRC-019…022) |
| 3 | **Verbotene Schlusskette** „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" | trug **fünf** Anker: `:1488`/`:1546` (REQ-037), `:1489`/`:1547` (REQ-038), `:1490` (REQ-039), zusätzlich `:1491` (REQ-040) | alle entfernt; die betroffenen Felder stehen auf **MISSING** bzw. **MISSING (begründet)**. **Kein CAN-Item umgedeutet, keine Problem-ID erfunden** | §7.5.5, §8 Punkt 37 |
| 4 | **CAN-050 bei REQ-008** | REQ-008 führte CAN-050 als Canvas-Anker, obwohl die Registry es **REQ-006** zuordnet | aus dem REQ-008-Kontext **entfernt**; Anker ist **CAN-138**. Dass CAN-050 selbst ein Composite ist, bleibt ein eigener BLOCKER und wird **nicht** vorweggenommen | §7.5.5 (`:465`), §8 Punkt 39 |
| 5 | **EV-008 / EV-039** | EV-008 trug im Feld `Evidence Needed` einen Sammeltext ohne Ausschluss des GPX-Anteils | kanonisch getrennt, in **beide** Richtungen ausgeschrieben: EV-008 **ausschließlich** Verlauf und Detailansicht, EV-039 **ausschließlich** GPX-Kompatibilität und Export | §6.7 (EV-008, EV-039), §7.5.3 |
| 6 | **REQ-040 / TRC-040 / AC-040 / EV-040 / CAN-140** | eine Zeile, ein Composite aus Wiederverwendung und Vergleich | **deprecated**, ersetzt durch **TRC-041** (REQ-041/AC-042/EV-043/CAN-142) und **TRC-042** (REQ-042/AC-043/EV-044/CAN-143). Beide Zeilen neu ausformuliert, **unterschiedlich blockiert** | §7.5.1, §7.5.2 |
| 7 | **Zählstände** | „39" als abgeleiteter Stand, „36" als **Verbots**literal | Ableitung auf **40**; **weder** 36 **noch** 39 wird erwartet oder verboten | §10.1, §10.2 Bindung 2 |
| 8 | **Fünf Zweifelsfälle einzeln geprüft** | REQ-032→CAN-029, REQ-009→CAN-013, REQ-004→VIS-007 + CAN-100, REQ-031→VIS-007, REQ-039→CAN-030 | Ergebnis je Fall in §6.5.1 — **zwei tragen, drei tragen nicht**. Zusätzlich registry-beauftragt geprüft: REQ-006 ↔ VIS-003 (§8 Punkt 40) | §8 Punkte 40, 43 |

**Was dieser Schritt ausdrücklich NICHT tut.** `true-line-status` bleibt bei **allen aktiven**
Requirements `pending-watcher`, `wired-in-prod?` `no`, `evidence-class` `none` — REQ-041 und
REQ-042 eingeschlossen. Es existiert kein Code. Kein Feld wurde auf `user-confirmed` oder
`verified` gesetzt, kein Plumbline-Watcher-Verdikt ausgestellt, kein Metamodell erweitert. Der
Gesamtstatus bleibt **BLOCKED_TRACEABILITY**.

**Warum die VIS-009-Verknüpfung entfernt und nicht nur kommentiert wurde.** Die Vorfassung ließ
VIS-009 bewusst als Link stehen und vermerkte den Befund daneben (§6.5, Zeile 4). Das ist die
schlechtere Lösung: ein semantisch falscher Anker, der syntaktisch gültig ist und sich plausibel
liest, wird bei jeder späteren maschinellen Prüfung als *erfüllte* Vision-Referenz gezählt — der
Befund im Fließtext daneben wird nicht mitgelesen. Die Zeile „Fehlende Vision-Links | 0" in §8
war genau deshalb irreführend. VIS-011 behebt die Ursache; der Vorbehalt steht jetzt **im Feld
selbst**, nicht in einer Fußnote.

### 0.4 Korrekturprotokoll Runde 5 (2026-07-20) — **Quellenprüfung**

Dieser Schritt vergibt **keine** ID und deprecatet **keine**. Er stuft ausschließlich **herab**;
kein Anker wurde hochgestuft, kein Status auf `linked`, `user-confirmed` oder `verified` gesetzt.

**Was sich geändert hat, ist der Prüfstand, nicht das Produkt.** Die vier Quelldokumente
(SRC-001 … SRC-004) liegen außerhalb des Repositorys und waren bis zum 2026-07-20 nicht lesbar;
`CLAUDE.md` nennt repo-relative Pfade, die nicht existieren. Mehrere Befunde der Runden 1–4
beruhten auf dieser Lücke — teils als „nicht auffindbar", teils als „nicht entscheidbar".
**Beides waren Aussagen über den Prüfstand, formuliert wie Aussagen über den Text.**

| # | Was | Vorher | Nachher | Quellenbeleg |
|---|---|---|---|---|
| 1 | **Vision-Anker REQ-019** | `linked-partial`, VIS-003 „trägt die Feed-/Zugangs-Hälfte" | **VIS-003 entfernt**, `broken`. Die tragende Lesart lief über das Zwischenglied „Feed = Entdeckungsfläche für den Zugang zu Trainingspartnern" — **eine Ableitung, kein Beleg**. Das Wort „Entdeckungsfläche" steht in keiner Quelle | SRC-001 Teil 1 §1.1–§1.4, SRC-003 §1.1–§1.3 vollständig geprüft: keine Vision-Aussage zu Empfehlung oder Feed. Inhalt steht in SRC-001 **§2.5** (Canvas) und SRC-003 **§4.2** (Spezifikation) |
| 2 | **Vision-Anker REQ-007** | `linked`, VIS-003, daneben eine OPEN QUESTION „nicht entscheidbar" | **VIS-003 entfernt**, `broken`. Die Quellen entscheiden die Frage: „Fortschritt" ist durchgehend longitudinal | SRC-001 §1.2, §2.1, §3.3; SRC-003 §1.1. Aktivitätsinterne Restdistanz nur funktional: SRC-001 **T-02**, SRC-003 §9 GATE A |
| 3 | **TRC-021, TRC-022** | `linked` trotz im eigenen Feld dokumentierter Teildeckung | beide **`linked-partial`**. VIS-004 trägt bei REQ-021 nur „lokale Teams", nicht Wachstum; VIS-003 trägt bei REQ-022 nur die gemeinsame Aktivität, nicht **Events** | Wachstum: SRC-003 §1.2 (USP-Ebene). Events: SRC-001 **L-05**, SRC-003 Plan 14 (funktionale Ebene) |
| 4 | **Ausschlussliste §8** | „31 / 40, nicht gezählt (neun)" — **TRC-007 fehlte** | **28 / 40, nicht gezählt (zwölf)**; Zeilenstatus linked 28 / broken 8 / not-linked 1 / linked-partial 3. Die Zahl der erfüllten Anker ist jetzt deckungsgleich mit `linked` — als stehende Gegenprobe ausgeschrieben | — |

**Was dieser Schritt ausdrücklich NICHT tut.** Er füllt **kein** reserviertes Vision-Item, vergibt
**keine** VIS-ID und nennt für die zwei neu erkannten Lücken **keine Nummer**. `true-line-status`
bleibt bei allen 40 aktiven Requirements `pending-watcher`, `wired-in-prod?` `no`,
`evidence-class` `none`. Der Gesamtstatus bleibt **BLOCKED_TRACEABILITY**.

**Warum REQ-021 und REQ-022 ihre Anker behalten, REQ-007 und REQ-019 nicht.** Der Unterschied ist
nicht graduell: bei REQ-021 und REQ-022 trägt eine Hälfte des Requirements eine **wörtliche**
Klausel des Vision-Items („lokale Teams", „Zugang zu lokalen Trainingspartnern"). Bei REQ-007 und
REQ-019 trug **keine** Hälfte wörtlich — die Verbindung entstand erst durch ein eingefügtes
Zwischenglied. **`linked-partial` setzt eine getragene Hälfte voraus; wo die tragende Lesart selbst
eine Brücke war, ist der Status `broken`.**

### 0.5 Korrekturprotokoll Runde 6 (2026-07-20) — **Nutzerauftrag-Nachzug**

Dieser Schritt vergibt **keine** ID, deprecatet **keine** und deutet **kein** Item um. Er stuft
ausschließlich **herab** oder legt offen; kein Anker wurde hochgestuft, kein Status auf `linked`,
`user-confirmed` oder `verified` gesetzt.

**Neue Prüfgrundlage: die Quellen liegen jetzt im Repository.** Nutzerauftrag Punkt 1 hat
SRC-001 … SRC-004 nach `docs/sources/` überführt. Alle Belege dieses Schritts sind deshalb
erstmals **repo-relativ** zitierbar und nachprüfbar; die Runden 1–5 mussten auf externe Pfade
verweisen. Sämtliche unten genannten Abwesenheitsbefunde sind gegen die Repo-Kopien neu erhoben,
nicht aus den Vorrunden übernommen.

| # | Was | Vorher | Nachher | Beleg |
|---|---|---|---|---|
| 1 | **Zeilenstatus TRC-004** | `linked`; das Vision-Feld behauptete „**Keine Schlusskette, sondern dieselbe Aussage.**" | **`not-linked`.** Die im Feld benannte tragende Klausel „Nutzer benötigen **verlässliches Tracking**" ist auf **Bedürfnisebene** unbelegt; der Anker VIS-003 bleibt stehen, zählt aber nach Registry §8 Punkt 15 **nicht** als erfüllt. Behauptung gestrichen, Befund an ihre Stelle gesetzt | Volltextsuche „verlässlich" über `docs/sources/SRC-001…SRC-004`: **0 Treffer**. Nächstliegend `SRC-001-REVYR-Vision-Canvas-PRD.md:250` „Distanzabweichung < 3 %" und `:252` „Kein Datenverlust bei App-Kill/Absturz während Tracking" — beides **NFR-Ebene**, keine Bedürfnisaussage |
| 2 | **REQ-007, `Target / Pass Condition`** | „(CAN-051 hält fest, dass die Subtraktion ausdrücklich verboten ist)" — ein als `EXPLICIT` geführtes Canvas-Item trug eine Pass/Fail-Bedingung | Berufung auf CAN-051 als **Autorität** entfernt; stattdessen offengelegt, dass die einzige Quelle, die den Rechenweg festlegt, **das Gegenteil** spezifiziert und der Traeger `proposed` ist. Die Anforderung selbst bleibt **inhaltlich unverändert** (Nutzerauftrag Punkt 4) | `docs/sources/SRC-004-tracking-and-planned-routes.md:416-417` „`return Math.max(0, plannedMeters - coveredMeters);`" und `:382` „`it('subtracts covered from planned', …)`"; `docs/decisions/decision-log.md:10` führt DEC-004 als `proposed` |
| 3 | **REQ-007, `Source Type`** | MISSING | **MISSING — unverändert.** Nutzerauftrag Punkt 4 („bis zur Nutzerbestätigung ASSUMPTION") betrifft die **Anforderungsherkunft**; das Feld dieser Datei führt die **Zielwertherkunft**. Eine Angleichung wäre eine stille Hochstufung und wurde **nicht** vollzogen; die Abgrenzung ist im Feld ergänzt | §1 Legende („Die **Pass-Bedingung** steht wörtlich …"), §2 „`EXPLICIT` gilt dort für den **Zielwert**, nicht für die Anforderung" und „MISSING-Schwellen". Korridor-, Hysterese- und Latenzwerte: Volltextsuche „Korridor", „Hysterese" über alle vier Quellen **0 Treffer** |
| 4 | **REQ-037: CAN-099-Wortlaut und `Signal / Control Evidence`** | „Die mobile Anwendung **und ihre nutzbaren Web-Auskopplungen** müssen …" bzw. „… der mobilen App **und aller nutzbaren Web-Auskopplungen** …" | **Web-Erstreckung entfernt** (Nutzerauftrag Punkt 3). Die nicht belegten Accessibility-Details (Fassung 2.2, Bedienflächen, Fokusführung, motorisch/assistiv) **bleiben im Text stehen** und sind als ASSUMPTION gekennzeichnet — ebenfalls Nutzerauftrag Punkt 3 | Alle vier „Web-Auskopplung"-Fundstellen liegen in `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md:83`, `:484`, `:711`, `:735` und betreffen **ausnahmslos** die CSS-Farbmischregel. Der einzige Accessibility-Abschnitt aller vier Quellen (`SRC-003:100`) nennt Web **nicht** |
| 5 | **REQ-024: Ankerbelastung durch CAN-109** | Rationale und `evidence-class-required` stützten sich unkommentiert auf CAN-109 | CAN-109 ist nach Nutzerauftrag Punkt 2 auf **ASSUMPTION** zurückgestuft (Owner Canvas). Die Mindestklasse `production-verified` und die getrennte Messung beider Fehlerrichtungen **bleiben unverändert** — eine Absenkung wäre eine Erleichterung der Prüfhürde. Die Abhängigkeit ist offengelegt | „False Positive", „Appeal", „Einspruch", „Confidence": Volltextsuche über alle vier Quellen **0 Treffer**. Das Risikoregister `SRC-003:690-717` enthält **keine** Zeile zur Anti-Cheat-Fehlklassifikation |
| 6 | **REQ-033: „Privacy-Review"** | in `Signal`, `Measurement Window` und Forschungsplan Stufe 3 als Kontrollnachweis und Gate-E-Vorbedingung geführt | Wortlaut **unverändert** (Messfelder sind wörtlich aus der `canonical_file`), Befund **offengelegt**: ein querschnittlicher Privacy-Review je Funktionsgruppe ist in keiner Quelle belegt | „Privacy-Review", „Privacy Matrix", „Datenschutz": Volltextsuche über `docs/sources/` **0 Treffer**. Wortnah belegt ist nur eine **datenklassengebundene** Einzelprüfung: `SRC-003:629` „eigene Privacy-Prüfung" (Task 17.4, Zyklus) und `SRC-003:715` „DSGVO-Prüfung in 10.2" (serverseitige Gesundheitsdaten) |
| 7 | **Zählstände §8** | Zeilenstatus linked 28 / broken 8 / not-linked 1 / linked-partial 3; Vision-Anker erfüllt 28 / 40 | **linked 27 / broken 8 / not-linked 2 / linked-partial 3 — Summe 40**; Vision-Anker erfüllt **27 / 40**, nicht gezählt **dreizehn**. Folge ausschließlich von Zeile 1 | §8, aus der Kernmatrix gezählt, nicht fortgeschrieben |

**Was dieser Schritt ausdrücklich NICHT tut.** `true-line-status` bleibt bei **allen aktiven**
Requirements `pending-watcher`, `wired-in-prod?` `no`, `evidence-class` `none`. Es existiert kein
Code. Kein Feld wurde auf `user-confirmed` oder `verified` gesetzt, kein Plumbline-Watcher-Verdikt
ausgestellt, kein Metamodell erweitert, keine Zeile entblockt. Der Gesamtstatus bleibt
**BLOCKED_TRACEABILITY**.

⚠️ **Die Gegenprüfung der zugrunde liegenden Befunde ist in allen fünf Fällen nicht durchgelaufen**
(`haelt_stand = false` in jeder Linse). Die Befunde sind deshalb **nicht** blind übernommen worden.
Wo die Einwände einander widersprechen — bei CAN-119 zeigen die drei Linsen in **drei verschiedene
Richtungen** — ist der Wortlaut **unverändert** geblieben und nur der Befund offengelegt. Wo ein
Einwand den Befund abschwächt, ist die **schwächere** Fassung umgesetzt: die Folgenlinse verlangte
für TRC-004 `broken`, umgesetzt ist `not-linked`, weil der Anker VIS-003 **vorhanden** bleibt und
`broken` ein fehlendes Kettenglied behauptet hätte. Jede dieser Abweichungen steht am Requirement
selbst, nicht nur hier.

⚠️ **Bekannte Werkzeug-Falschmeldung, hier nicht geglättet.** `scripts/validation/verify.py` prüft
den Zeilenstatus gegen ein **hartkodiertes** Literal (`claim = {"linked": 31, …}`) und meldet
deshalb einen Fehlschlag. Das ist ein Werkzeug-Befund, kein Dokumentdefekt; er ist in
`docs/validation/validation-report.md` §5.2 offengelegt. **Die Zahlen dieser Datei sind gezählt,
das Literal des Werkzeugs ist es nicht** — nach Registry §13.3 wird der Befund am Dokument behoben,
nicht am Werkzeug, und das Werkzeug ist eingefroren.

---

## 1. Kernmatrix

Eine Zeile je Requirement. `Canvas Item` nennt den **primären** atomaren Anker; die vollständige
Ankermenge steht in §3 je Requirement.

| Trace ID | Requirement | Vision Item | Canvas Item (primär, atomar) | Acceptance Criterion | Evidence | Measurement Type | Release Gate | Source Type | Status |
|---|---|---|---|---|---|---|---|---|---|
| TRC-001 | REQ-001 — Sportmodus als zentrale Konfiguration | VIS-008 | CAN-047 | AC-001 | EV-001 | OPERATIONAL_QUALITY | GATE-A0 | **ASSUMPTION** | linked |
| TRC-002 | REQ-002 — Foreground-Tracking | VIS-003 | CAN-048 | AC-002 | EV-002 | OPERATIONAL_QUALITY | GATE-A0 | **ASSUMPTION** | linked |
| TRC-003 | REQ-003 — Background, Pause und Recovery | VIS-005 | CAN-049 | AC-003 | EV-003 | OPERATIONAL_QUALITY | GATE-A0 | **ASSUMPTION** | linked |
| TRC-004 | REQ-004 — Erweitertes GPS-Datenmodell und Filter | **VIS-003** *(2026-07-20: VIS-007 entfernt, siehe §6.5.1 Fall 3; **Runde 6**: Anker bleibt, zählt aber nicht als erfüllt — die tragende Klausel „verlässliches Tracking" ist auf Bedürfnisebene unbelegt, §6.1.1)* | **CAN-028** *(2026-07-20: CAN-100 ist ein **Risiko**-Item und steht jetzt in der Risiko-Zeile, §3)* | AC-004 | EV-004 | OPERATIONAL_QUALITY | GATE-A0 | **ASSUMPTION** | **not-linked** *(Runde 6, 2026-07-20; vorher `linked`)* |
| TRC-005 | REQ-005 — Robuste lokale Aktivitätsspeicherung | VIS-005 | CAN-131 | AC-005 | EV-005 | OPERATIONAL_QUALITY | GATE-A0 | **ASSUMPTION** | linked |
| TRC-006 | REQ-006 — Routenplanung | **MISSING — BLOCKER** *(VIS-003 am 2026-07-20 als nicht tragend entfernt; Prüfung registry-beauftragt, §8 Punkt 40 der Registry, Ergebnis in §6.5.1 Fall 6)* | CAN-050 *(zugleich als Composite ein eigener BLOCKER, §6.1.2)* | AC-006 | EV-006 | OPERATIONAL_QUALITY | GATE-A0 | **ASSUMPTION** | **broken** |
| TRC-007 | REQ-007 — Routenbezogener Fortschritt | **MISSING — BLOCKER** *(2026-07-20: VIS-003 entfernt, Quellenprüfung §6.1.1)* | CAN-051 | AC-007 | EV-007 | OPERATIONAL_QUALITY | GATE-A0 | MISSING | **broken** |
| TRC-008 | REQ-008 — Verlauf und Detailansicht *(verengt 2026-07-19)* | VIS-003 | **CAN-138** | AC-008 | EV-008 | OPERATIONAL_QUALITY | GATE-A0 | **ASSUMPTION** | linked |
| TRC-009 | REQ-009 — Herzfrequenzquellen | VIS-007 | CAN-052 | AC-009 | EV-009 | OPERATIONAL_QUALITY | GATE-A1 | **ASSUMPTION** | linked |
| TRC-010 | REQ-010 — Erklärbarer Belastungs-Score mit Confidence | VIS-007 | CAN-126 | AC-010 | EV-010 | PRODUCT_OUTCOME | GATE-A1 | ASSUMPTION | linked |
| TRC-011 | REQ-011 — HF-Zonen und optionale Ansage | VIS-007 | CAN-052 | AC-011 | EV-011 | OPERATIONAL_QUALITY | GATE-A1 | **ASSUMPTION** | linked |
| TRC-012 | REQ-012 — Stimmungs-Check-in und Korrelation | VIS-003 | CAN-125 | AC-012 | EV-012 | RESEARCH_HYPOTHESIS | GATE-A1 | ASSUMPTION | linked |
| TRC-013 | REQ-013 — Health-Home und Steigerungshinweis | VIS-007 | CAN-124 | AC-013 | EV-013 | PRODUCT_OUTCOME | GATE-A1 | ASSUMPTION | linked |
| ~~TRC-014~~ | ~~REQ-014 — Designsystem und Accessibility~~ | — | — | — | — | — | — | — | **deprecated 2026-07-19 → TRC-037, TRC-038** (Registry §6.6). Zeile bleibt als Migrationsbeleg stehen, ist aber **keine** aktive Verknüpfung; sie referenzierte drei deprecatete IDs plus das deprecatete Sammelblock-Item CAN-007 plus den als falsch erkannten Vision-Anker VIS-009 und war in **keinem** Feld mehr gültig. |
| TRC-015 | REQ-015 — Verdiente Avatar-Progression | VIS-004 | CAN-055 | AC-015 | EV-015 | COMPLIANCE_CONTROL | GATE-A2 (PRD Release A2-B-C; erstmalige Abnahme mit GATE-A2, danach fortlaufend bis GATE-C) | **ASSUMPTION** | linked |
| TRC-016 | REQ-016 — Recaps, Erfolgskarten und Live-Status | VIS-004 | CAN-054 | AC-016 | EV-016 | COMPLIANCE_CONTROL | GATE-A2 | MISSING | linked |
| TRC-017 | REQ-017 — Accounts, Auth und Datenmigration | VIS-005 | CAN-056 | AC-017 | EV-017 | COMPLIANCE_CONTROL | GATE-B | MISSING | linked |
| TRC-018 | REQ-018 — Privacy, Sichtbarkeit und Moderation | VIS-009 | CAN-057 | AC-018 | EV-018 | COMPLIANCE_CONTROL | GATE-B | **ASSUMPTION** | linked |
| TRC-019 | REQ-019 — Routenempfehlungen und Feed | **MISSING — BLOCKER** *(2026-07-20: VIS-003 entfernt, Quellenprüfung §6.1.1)* | **CAN-058** *(Capability; CAN-130 ist das Erfolgssignal und steht in §4.2)* | **AC-019** (funktional) · **AC-041** (Messkriterium) | **EV-019** (funktional) · **EV-041** (Kennzahl, `planned`) | PRODUCT_OUTCOME | GATE-B | ASSUMPTION (Anforderung) · **EXPLICIT** (Zielwert, CAN-130) | **broken** |
| TRC-020 | REQ-020 — Teamgründung und Beitritt | **VIS-004** *(2026-07-20 statt VIS-008)* | **CAN-060** *(Capability; CAN-127 ist das Erfolgssignal und steht in §4.2)* | AC-020 | EV-020 | PRODUCT_OUTCOME | GATE-C | ASSUMPTION | linked |
| TRC-021 | REQ-021 — Aktive Mitglieder und Teamwachstum | **VIS-004** *(2026-07-20 statt VIS-008; trägt nur die **Team-Hälfte**, §6.1.1)* | CAN-060 | AC-021 | EV-021 | RESEARCH_HYPOTHESIS | GATE-C | MISSING | **linked-partial** |
| TRC-022 | REQ-022 — Gemeinsame Aktivitäten und Events | **VIS-003** *(2026-07-20 statt VIS-008; VIS-004 einzeln geprüft und **verworfen**, §3; trägt nur die **Aktivitäts-Hälfte**, §6.1.1)* | **CAN-067** *(Capability; CAN-128 ist das Erfolgssignal und steht in §4.2)* | AC-022 | EV-022 | PRODUCT_OUTCOME | GATE-C (PRD Release C-D) | ASSUMPTION | **linked-partial** |
| TRC-023 | REQ-023 — Effort-Normalisierung | VIS-008 | CAN-062 | AC-023 | EV-023 | RESEARCH_HYPOTHESIS | GATE-C | MISSING | linked |
| TRC-024 | REQ-024 — Anti-Cheat mit Confidence-Stufen | VIS-008 | CAN-063 | AC-024 | EV-024 | RESEARCH_HYPOTHESIS | GATE-C | MISSING | linked |
| TRC-025 | REQ-025 — Challenges, Rankings und idempotente Rewards | VIS-004 | CAN-061 | AC-025 | EV-025 | OPERATIONAL_QUALITY | GATE-C | **ASSUMPTION** | linked |
| TRC-026 | REQ-026 — Team-Territory | VIS-008 | CAN-064 | AC-026 | EV-026 | RESEARCH_HYPOTHESIS | GATE-D | MISSING | linked |
| TRC-027 | REQ-027 — Seasons und nach Finalisierung fachlich unveränderbare Historie | VIS-004 | CAN-066 | AC-027 | EV-027 | OPERATIONAL_QUALITY | GATE-D | MISSING | linked |
| TRC-028 | REQ-028 — Deterministische Einzel-Reviere | VIS-008 | CAN-065 | AC-028 | EV-028 | RESEARCH_HYPOTHESIS | GATE-D | MISSING | linked |
| TRC-029 | REQ-029 — Sportplatz-Challenges und Bahngold-Score | VIS-004 | CAN-107 | AC-029 | EV-029 | RESEARCH_HYPOTHESIS | GATE-D | MISSING | linked |
| TRC-030 | REQ-030 — Live-Map und Beschützer-Modus | VIS-009 | CAN-068 | AC-030 | EV-030 | COMPLIANCE_CONTROL | GATE-D | **ASSUMPTION** | linked |
| TRC-031 | REQ-031 — Sturzerkennung als Assistenz | **MISSING — BLOCKER** *(VIS-007 am 2026-07-20 als nicht tragend entfernt; keine reservierte VIS-ID, §6.5.1 Fall 4)* | CAN-068 | AC-031 | EV-031 | RESEARCH_HYPOTHESIS | GATE-D | MISSING | **broken** |
| TRC-032 | REQ-032 — Wearables und Bike-Sensorik | **MISSING — BLOCKER** (kein VIS-Item trägt „vollständige und erklärbare Trainingsdaten“; VIS-005 war der bisherige, fachlich unpassende Anker — §6.5 Zeile 5) | **CAN-022** (Problem) | AC-032 | EV-032 | OPERATIONAL_QUALITY | GATE-E | MISSING | **broken** |
| TRC-033 | REQ-033 — Coach, Recovery, Wetter und Zyklus unter Claims-Gate | VIS-007 | CAN-070 | AC-033 | EV-033 | RESEARCH_HYPOTHESIS | GATE-E | MISSING | linked |
| TRC-034 | REQ-034 — Security, Datenschutz und Datenminimierung | VIS-009 | CAN-084 | AC-034 | EV-034 | COMPLIANCE_CONTROL | GATE-A0 (Bundle-Scan, Secret- und Proxy-Kontrollen ab A0) und fortlaufend bis GATE-E | EXPLICIT | linked |
| TRC-035 | REQ-035 — Evidence Ledger und Definition of Done | VIS-010 | CAN-123 | AC-035 | EV-035 | COMPLIANCE_CONTROL | GATE-A0 bis GATE-E (PRD Release A0-E), wirksam bereits ab P0 | **ASSUMPTION** | linked |
| TRC-036 | REQ-036 — Store- und Release-Gates | VIS-010 | CAN-083 | AC-036 | EV-036 | COMPLIANCE_CONTROL | GATE-A0 bis GATE-E (PRD Release A0-E); jede Stufe ist ihr eigener Pruefpunkt | **ASSUMPTION** | linked |
| **TRC-037** | **REQ-037 — Accessibility** *(neu 2026-07-19, Nachfolger 1/2 von REQ-014)* | **VIS-011** (unbestätigt, zählt **nicht** als erfüllter Anker — §6.5 Zeile 4) | **CAN-099** | AC-037 | EV-037 | COMPLIANCE_CONTROL | GATE-A0 (Accessibility-Basis) bis GATE-A2 (vollständiger WCAG-2.2-AA-Audit) | **ASSUMPTION** | **not-linked** |
| **TRC-038** | **REQ-038 — Monochromes tokenbasiertes Designsystem** *(neu 2026-07-19, Nachfolger 2/2 von REQ-014)* | **VIS-012 — reserved, Inhalt MISSING → BLOCKER** | **CAN-141** | AC-038 | EV-038 | COMPLIANCE_CONTROL | GATE-A0 bis GATE-A2, erstmalige Abnahme mit GATE-A0 | **EXPLICIT** | **broken** |
| **TRC-039** | **REQ-039 — GPX-Export abgeschlossener Aktivitäten** *(neu 2026-07-19)* | **VIS-013 — reserved, Inhalt MISSING → BLOCKER** | **CAN-139** | AC-039 | EV-039 | OPERATIONAL_QUALITY | GATE-A2, spätestens vor öffentlichem v1.0-Release | **ASSUMPTION** | **broken** |
| ~~TRC-040~~ | ~~REQ-040 — Streckenwiederverwendung und Aktivitätsvergleich~~ | — | — | — | — | — | — | — | **deprecated 2026-07-20 → TRC-041, TRC-042** (Registry §7.5.1). Zeile bleibt als Migrationsbeleg stehen, ist aber **keine** aktive Verknüpfung; sie referenzierte nach der Teilung **vier** deprecatete IDs (CAN-140, REQ-040, AC-040, EV-040) und ihr einziger Vision-Anker galt nur für **eine** der beiden Hälften. |
| **TRC-041** | **REQ-041 — Wiederverwendung einer gespeicherten Route** *(neu 2026-07-20, Nachfolger 1/2 von REQ-040)* | **VIS-014 — reserved, Inhalt MISSING → BLOCKER** | **CAN-142** | AC-042 | EV-043 | OPERATIONAL_QUALITY | GATE-A2 | **ASSUMPTION** | **broken** |
| **TRC-042** | **REQ-042 — Vergleich fachlich vergleichbarer Aktivitäten** *(neu 2026-07-20, Nachfolger 2/2 von REQ-040)* | **VIS-003** — ungeprüfte ASSUMPTION des Traceability-Owners, hier **nicht** hochgestuft, siehe §3 | **CAN-143** | AC-043 | EV-044 | OPERATIONAL_QUALITY | GATE-A2 | **ASSUMPTION** | **linked-partial** |

**Zeilenstatus-Werte.** `linked` = alle fünf Kettenglieder vorhanden und fachlich tragfähig ·
`linked-partial` = Anker vorhanden, deckt das Requirement aber **nachweislich nur teilweise** ·
`not-linked` = Anker vorhanden und fachlich passend, aber `source_type = ASSUMPTION` und
unbestätigt, zählt deshalb nach Registry §8 Punkt 15 **nicht** als erfüllt · `broken` = ein
Kettenglied fehlt (Inhalt MISSING). **`broken` wird bewusst geführt, statt die Zeile an ein
unpassendes Item zu hängen** — genau letzteres war der Defekt VIS-009 ↔ REQ-014.

### Legende `Source Type`

| Wert | Bedeutung in dieser Matrix |
|---|---|
| EXPLICIT | Die Pass-Bedingung steht wörtlich in einem Artefakt **und** ihre Herkunft ist belegt: `CONFIRMED`-Canvas-Item, `user-confirmed`-Entscheidung (`DEC-`), `SRC-006` oder eine **konkret zitierte** verbindliche externe Regel. |
| ASSUMPTION | Ein Zielwert existiert, ist aber **nicht belegt oder nicht empirisch validiert**. Er darf nicht als bestätigte Produktwahrheit gelesen werden. |
| MISSING | Die entscheidende quantitative Schwelle existiert in **keinem** Artefakt. Es wurde kein plausibler Wert eingesetzt. |

---

## 2. Messmodell — Verteilung und Begründung der Klassen

**Basis: die aus der Registry abgeleitete Zahl aktiver Requirements (§0.0).** Alle vier
Verteilungen summieren sich auf diese Zahl; REQ-014 und REQ-040 sind als `deprecated` in
**keiner** Zeile mehr enthalten.

| Measurement Type | Anzahl | Requirements |
|---|---:|---|
| OPERATIONAL_QUALITY | 16 | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-011, REQ-025, REQ-027, REQ-032, REQ-039, **REQ-041**, **REQ-042** |
| COMPLIANCE_CONTROL | 10 | REQ-015, REQ-016, REQ-017, REQ-018, REQ-030, REQ-034, REQ-035, REQ-036, REQ-037, REQ-038 |
| RESEARCH_HYPOTHESIS | 9 | REQ-012, REQ-021, REQ-023, REQ-024, REQ-026, REQ-028, REQ-029, REQ-031, REQ-033 |
| PRODUCT_OUTCOME | 5 | REQ-010, REQ-013, REQ-019, REQ-020, REQ-022 |
| **Summe** | **40** | entspricht der aus `docs/ID-REGISTRY.md` §6.4 abgeleiteten Zahl (§0.0) |

| Source Type | Anzahl | Requirements |
|---|---:|---|
| EXPLICIT | 2 | REQ-034 (klauselbeschränkt), REQ-038 |
| ASSUMPTION | 25 | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006, REQ-008, REQ-009, REQ-010, REQ-011, REQ-012, REQ-013, REQ-015, REQ-018, REQ-019, REQ-020, REQ-022, REQ-025, REQ-030, REQ-035, REQ-036, REQ-037, REQ-039, **REQ-041**, **REQ-042** |
| MISSING | 13 | REQ-007, REQ-016, REQ-017, REQ-021, REQ-023, REQ-024, REQ-026, REQ-027, REQ-028, REQ-029, REQ-031, REQ-032, REQ-033 |
| **Summe** | **40** | |

⚠️ **Die `EXPLICIT`-Zahl ist in Runde 4 NICHT gestiegen, obwohl drei Canvas-Items auf `EXPLICIT`
gesetzt wurden** (CAN-099, CAN-139, CAN-141 — Registry §7.5.3). Der Source Type eines
Requirements folgt **nicht** automatisch dem seines Canvas-Ankers: REQ-039 hängt an CAN-139
(`EXPLICIT`), bleibt aber `ASSUMPTION`, weil der **Anforderungstext** unbestätigt ist und weder
GPX-Formatversion noch Referenzanwendung benannt sind. Eine automatische Vererbung hätte hier
eine Höherstufung ohne neuen Beleg erzeugt.

### 2.1 Nachgezogen: das `source_type`-Nachaudit des PRD

⚠️ **Diese Matrix führte bis zum 2026-07-19 `EXPLICIT` bei 17 Requirements** und stand damit im
Widerspruch zur kanonischen Datei. `docs/prd/…prd.md` hat alle 17 einzeln gegen dieselbe
Beweislatte geprüft, die für die NFRs gilt, und **16 auf `ASSUMPTION` herabgestuft**; nur REQ-034
hält, klauselbeschränkt. Die Werte sind hier **übernommen, nicht neu bewertet** — das PRD ist die
`canonical_file` für `source_type`. Der Widerspruch wird damit aufgelöst und nicht durch eine
Fußnote überdeckt.

Die drei tragenden Gründe des Nachaudits (Volltext: `prd.md`, „Nachaudit der 17
`EXPLICIT`-Zeilen"):

1. **Verkettung auf herabgestufte NFRs** — REQ-002, REQ-003, REQ-004, REQ-005 und das damalige
   REQ-014 (heute **REQ-037**) beziehen ihre Pass-Bedingung wörtlich aus NFR-001/002/003/005.
   Diese vier NFRs sind auf `ASSUMPTION` herabgestuft; ein abgeleiteter Wert kann nicht stärker
   belegt sein als seine Quelle. **REQ-038 fällt ausdrücklich nicht darunter** — es hängt an
   CAN-141, nicht an NFR-005.
2. **Analytische Nullschwelle ≠ belegte Herkunft** — bei REQ-001, REQ-008, REQ-009, REQ-011,
   REQ-015, REQ-018, REQ-025, REQ-030, REQ-035 und REQ-036 folgt die 0-/100-%-Schranke logisch
   aus dem Requirement und ist deshalb **keine gewählte Zahl**. Belegbedürftig und **unbelegt**
   bleibt die Anforderung selbst: sie stützt sich auf SRC-001/SRC-003, die laut
   `docs/SOURCE-MAP.md` **nicht auffindbar** sind.
3. **Genannt ≠ zitiert** — REQ-036 beruft sich auf Store-Policies, ohne Klausel, Fassung oder
   Datum zu nennen.

**REQ-038 ist die zweite `EXPLICIT`-Zeile und keine Hochstufung zur Statistikpflege.** Sie hält,
weil CAN-141 `source_type EXPLICIT` trägt: das monochrome Designsystem mit den vier zulässigen
Farbbedeutungen ist eine ausdrückliche Nutzerangabe vom 2026-07-19. **Nicht mitgezogen:**
REQ-037, obwohl aus derselben Entscheidung — dort fehlt weiterhin die zitierte **Rechtsgrundlage**
für die Verbindlichkeit von WCAG 2.2 AA.

**ASSUMPTION-Zielwerte aus VIS-006 (6).** REQ-010, REQ-012, REQ-013, REQ-019, REQ-020, REQ-022
stützen sich auf VIS-006-Zielwerte, die in keinem Artefakt empirisch hinterlegt sind. Sie
erscheinen ausdrücklich **nicht** als validierte Produktwahrheit. **Teilpräzisierung bei
REQ-019:** der Zielwert „> 1,0" ist seit dem 2026-07-19 über **CAN-130** `EXPLICIT` und
vollständig definiert — insbesondere ist jetzt bestimmt, **was der Nenner ist**. `EXPLICIT` gilt
dort für den **Zielwert**, nicht für die Anforderung, und **Definition ist kein Nachweis**:
`evidence_status` **planned**, `empirical_result` **MISSING**.

**MISSING-Schwellen (13).** REQ-007, REQ-016, REQ-017, REQ-021, REQ-023, REQ-024, REQ-026,
REQ-027, REQ-028, REQ-029, REQ-031, REQ-032, REQ-033 — in keinem Fall wurde ein Wert geraten.
Die Zahl ist durch den Auftau-Schritt 2 **unverändert**: keines der vier neuen Requirements
trägt `MISSING`, und keines der 13 wurde durch die Migration belegt.

**RESEARCH_HYPOTHESIS (9).** Jedes dieser Requirements trägt in §3 einen vollständigen
Forschungsplan (Hypothese, Plan, Fixtures/reale Testdaten, Entscheidungsschwelle, Konsequenz bei
unzureichender Evidenz). Kein produktiver Rollout vor bestandenem Gate; nicht validierte
Startwerte bleiben ASSUMPTION. **REQ-042 zählt hier ausdrücklich nicht mit:** das Requirement
misst Funktionsqualität (OPERATIONAL_QUALITY), aber seine **Vergleichslogik** bleibt
`RESEARCH_HYPOTHESIS` bzw. MISSING, solange OQ-015 offen ist. Beides wird getrennt geführt.
**REQ-041 ist davon unberührt** — es ist vollständig spezifizierbar und trägt keine offene
Untersuchungsfrage; genau das war der operative Grund für die Teilung von REQ-040.

**Owner.** OQ-002 (finaler Repository-Owner/DRI) ist offen. Deshalb trägt **jedes aktive**
Requirement einen sichtbaren OWNER-BLOCKER statt eines stillen Nullwerts — die vier neuen
eingeschlossen. Wo ein Register eine Rolle nennt, ist sie als Owner *der offenen Frage*
gekennzeichnet, nie als REQ-Owner.

---

## 3. Requirement-Detail: Messmodell, Verknüpfung, Risiko, offene Entscheidung

### REQ-001 — Sportmodus als zentrale Konfiguration

| Feld | Wert |
|---|---|
| Trace ID | TRC-001 |
| Vision Item | VIS-008 — Fairness Boundary: Run und Bike besitzen getrennte Metriken, Ziele und interne Wertungen; sportübergreifender  |
| Canvas Item (atomar) | CAN-047, CAN-028, CAN-013 |
| Acceptance Criterion | AC-001 — Zu REQ-001 — Then: Alle sportabhängigen Metriken, Schwellen, Labels und Routingprofile wechseln konsistent; Run zeigt Pace, Bike… |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Konsistenzrate der sportabhaengigen Konfiguration: Anteil der Screens, Metriken, Schwellen und Routingprofile, die beim Wechsel Run <-> Bike vollstaendig auf das jeweilige SportConfig-Objekt umschalten (Run zeigt Pace, Bike zeigt Geschwindigkeit). Run und Bike werden getrennt durchlaufen. Zusaetzlich statisch: Anzahl sportabhaengiger Konstanten ausserhalb der Konfigurationsobjekte. |
| Target / Pass Condition | AC-001 als Pass/Fail mit 100-%-Abdeckung: alle sportabhaengigen Metriken, Schwellen, Labels und Routingprofile wechseln konsistent; 0 sportspezifische Werte hart codiert in Screens. Kein Nutzungs- oder Engagement-Zielwert - REQ-001 ist eine Architektur-/Korrektheitsschranke, kein Nutzerverhalten. |
| Measurement Window | Je Gate-A0-Abnahme und bei jeder Versionsaenderung eines SportConfig-Objekts; Screen-Checkliste einmal je Plattform (iOS, Android) und je Sportart. |
| Evidence Needed | EV-001 — Konfigurations-Unit-Tests und Screen-Checkliste für iOS/Android. |
| Evidence Source | EV-001 (Konfigurations-Unit-Tests und Screen-Checkliste fuer iOS/Android); Mindestklasse laut docs/traceability.md: real-boundary-smoke, weil die Sportumschaltung eine UI-Eigenschaft auf realen Geraeten ist. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 (finaler Repository-Owner/DRI) ist offen; PRD-Kopfzeile 'Owner' = MISSING. Default bei Nichtaufloesung laut docs/decisions/open-questions.md: 'Umsetzung bleibt organisatorisch unzugeordnet'. Dokumentierte Rollenreferenz nur zur gekoppelten Frage OQ-003 ('Engineering/QA') - das ist der Owner der Frage, nicht der REQ-Owner. |
| Release Gate | GATE-A0 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — Sportumschaltung ist eine UI-Eigenschaft; die Screen-Checkliste (EV-001) muss auf realem iOS und Android laufen. |
| Risiko | RISK-005 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-003 |
| Rationale | Der Erfolg von REQ-001 ist an keiner Nutzerreaktion ablesbar, sondern an der technischen Konsistenz zwischen Sportmodus und Ausgabe. Ein Engagement-KPI waere hier ein Kategorienfehler. Run/Bike-Trennung ist zwingend, weil genau die Verwechslung der sportspezifischen Kernmetrik (RISK-005: 'Bike zeigt falsche Laufmetriken') der Fehlerfall ist, den das REQ verhindern soll. |

---

### REQ-002 — Foreground-Tracking

| Feld | Wert |
|---|---|
| Trace ID | TRC-002 |
| Vision Item | VIS-003 — User Need: Nutzer benötigen verlässliches Tracking, verständliche statt abstrakte Health-Auswertung, konkrete  ⚠️ **Zitat des Altstands (Runde 6, 2026-07-20):** VIS-003 wird nach Nutzerauftrag Punkt 2 verengt; die Qualifizierer „verlässlich" und „sicher" sind in keiner der vier Quellen belegt und werden als ASSUMPTION-Rest getrennt geführt. **Der Wortlaut wird hier nicht nachgezogen**, weil er wörtlich aus dem Vision-Item stammt und dessen Fassung dem Vision-Owner obliegt. Diese Zeile stützt sich **nicht** auf einen der beiden Qualifizierer — anders als REQ-004, siehe §6.1.1. |
| Canvas Item (atomar) | CAN-048, CAN-028, CAN-013, CAN-100 |
| Acceptance Criterion | AC-002 — Zu REQ-002 — Then: Die Route und Live-Metriken aktualisieren sich fortlaufend und die Aktivität kann kontrolliert beendet werden. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Getrennt fuer Run und Bike und je Plattform: Distanzabweichung gegen die Referenzstrecke nach Filter, GPS-Punktqualitaet (Anteil Punkte oberhalb der Genauigkeitsschwelle), Aktualisierungsluecken der Live-Metrik und Live-Karte, Anteil gestarteter Aktivitaeten, die technisch abbrechen statt vom Nutzer beendet zu werden. |
| Target / Pass Condition | NFR-001: < 3 % Distanzabweichung auf definierter Referenzstrecke nach Filter, getrennt nachgewiesen fuer Run und Bike und je Plattform. AC-002 als Pass/Fail: Route und Live-Metriken aktualisieren fortlaufend, die Aktivitaet ist kontrolliert beendbar. Fuer die Rate technisch abgebrochener Sessions nennt kein Artefakt einen Zielwert: MISSING - der Wert wird gemessen und dokumentiert, aber nicht mit einer erfundenen Schwelle bewertet. |
| Measurement Window | Je Referenzstreckenlauf; mindestens ein Lauf je Sportart und je Plattform vor Gate A0; Wiederholung bei jeder Aenderung an Sampling, Filter oder Location-Provider. |
| Evidence Needed | EV-002 — Gerätetest je Sport und Plattform auf Referenzstrecke. |
| Evidence Source | EV-002 (Geraetetest je Sport und Plattform auf Referenzstrecke); Mindestklasse laut docs/traceability.md: production-verified. RISK-002 (GPS-Drift) ist die zugehoerige offene Risikoposition. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Zusaetzlich blockierend fuer die Messung selbst: OQ-003 (Minimum iOS/Android und Referenzgeraete, Owner der Frage 'Engineering/QA') ist MISSING - ohne Referenzgeraete ist NFR-001 nicht reproduzierbar messbar. |
| Release Gate | GATE-A0 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | production-verified — GPS, Karte, UI und NFR-001 (< 3 % auf Referenzstrecke) sind nur im realen Feld je Sport und Plattform nachweisbar. |
| Risiko | RISK-002, RISK-003 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-003 |
| Rationale | Foreground-Tracking ist die technische Grundzusage des Produkts; gemessen wird Datenqualitaet, nicht Nutzerverhalten. Run und Bike muessen getrennt gemessen werden, weil Sampling, Geschwindigkeitsbereich und damit die Driftwirkung sportspezifisch sind. Ein Aktivitaets-Abschluss-KPI als Produktziel gehoert zu REQ-013 (Wiedernutzung), nicht hierher. |
| Befund | Erzeugt die Risiken CAN-100 (GPS-Drift) und CAN-101 (Batterieverbrauch) als Kernfläche (NFR-001, NFR-002). Register: RISK-002, RISK-003. |

---

### REQ-003 — Background, Pause und Recovery

| Feld | Wert |
|---|---|
| Trace ID | TRC-003 |
| Vision Item | VIS-005 — Project Goal: Zuerst einen belastbaren Health-Tracker etablieren; danach Accounts, Community, Teams und erst n |
| Canvas Item (atomar) | CAN-049, CAN-101, CAN-108, CAN-028 |
| Acceptance Criterion | AC-003 — Zu REQ-003 — Then: Die Aktivität bleibt lückenlos, Pausenzeit verfälscht keine Metrik und die Session ist wiederherstellbar. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Recovery-Rate nach App-Kill und Absturz, Background-Vollstaendigkeit (Anteil erwarteter GPS-Punkte bei gesperrtem Bildschirm und im Hintergrund), Trefferquote und Falschausloesung der sportabhaengigen Auto-Pause getrennt fuer Run und Bike, Batterieverbrauch pro Stunde. |
| Target / Pass Condition | NFR-003 als binaeres Pass/Fail: kein Datenverlust bei App-Kill oder Absturz; Session-Recovery gelingt in 100 % der 30-Minuten-Kill-Tests je Plattform und je Sportart. AC-003: Pausenzeit verfaelscht keine Metrik. NFR-002 nennt ein Batterieziel < 10 % pro Stunde, das die Quelle selbst als 'Ziel' mit Pflicht zur Messwertdokumentation fuehrt und das fuer dieses Produkt nicht empirisch belegt ist. Fuer die Auto-Pause-Falschausloesungsrate existiert kein dokumentierter Schwellwert: MISSING. |
| Measurement Window | 30 Minuten je Kill-/Background-Test, je Plattform und je Sportart (EV-003); Batteriemessung ueber eine zusammenhaengende Stunde (NFR-002); Wiederholung vor jedem Gate ab A0. |
| Evidence Needed | EV-003 — 30-Minuten-Kill-/Background-Test je Plattform und Sport. |
| Evidence Source | EV-003 (30-Minuten-Kill-/Background-Test je Plattform und Sport); Mindestklasse production-verified - Background-Execution und OS-Scheduler-Verhalten sind mit keinem Fake beweisbar. RISK-001 (OS drosselt/beendet Background-GPS) und RISK-003 (Batterie) sind offen. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. OQ-003 (Referenzgeraete) ist ebenfalls MISSING und ohne Geraetefestlegung ist der Batteriemesswert nicht vergleichbar. |
| Release Gate | GATE-A0 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | production-verified — Background-Execution, App-Kill und OS-Scheduler-Verhalten sind mit keinem Fake beweisbar. |
| Risiko | RISK-001, RISK-003, RISK-010 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-003 |
| Rationale | Zuverlaessigkeit im Hintergrund ist reine Betriebsqualitaet. Getrennte Run-/Bike-Messung ist zwingend, weil Auto-Pause an sportabhaengigen Geschwindigkeitsschwellen haengt: eine Bike-Rollphase und ein Run-Stillstand sind unterschiedliche Zustaende. Das Batterieziel wird bewusst als hedged Zielwert der Quelle zitiert und nicht als validierter Messwert dargestellt. |
| Befund | Verschärft CAN-101 (Batterieverbrauch) und CAN-108 (Store-Ablehnung): dauerhafte Background-Location ist ein Hauptablehnungsgrund beider Stores. Register: RISK-001, RISK-003, RISK-010. |

---

### REQ-004 — Erweitertes GPS-Datenmodell und Filter

| Feld | Wert |
|---|---|
| Trace ID | TRC-004 |
| Vision Item | **VIS-003 — User Need**, tragende Klausel: „Nutzer benötigen **verlässliches Tracking** …". Ein ungefilterter, driftbehafteter GPS-Track ist kein verlässliches Tracking; REQ-004 ist die Bedingung, unter der diese Klausel überhaupt einlösbar ist, und seine Pass-Bedingung zahlt direkt auf NFR-001 (Distanzabweichung) ein. ⚠️ **Der Zusatz „wörtlich" und der Schlusssatz „Keine Schlusskette, sondern dieselbe Aussage" sind am 2026-07-20 (Runde 6) gestrichen** — die Klausel ist auf Bedürfnisebene nicht belegt; siehe nächste Zeile. Der Anker bleibt stehen, **zählt aber nicht als erfüllt**. |
| Vision-Anker — Quellenprüfung Runde 6 (2026-07-20), **Herabstufung `linked` → `not-linked`** | **Der Qualifizierer „verlässlich" steht in keiner der vier Quellen.** Volltextsuche über `docs/sources/SRC-001…SRC-004`: **0 Treffer**. Belegt ist auf Bedürfnisebene ausschließlich „tracken" **ohne** Qualifizierer (`docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md:64` „**Runner/Jogger:** tracken, Leistung verstehen, …"). Die Qualitätsforderung erscheint ausschließlich auf **NFR-Ebene**: `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md:250` „\| **Genauigkeit** \| Distanzabweichung < 3 % auf bekannter Referenzstrecke (nach GPS-Filter) \|" und `:252` „\| **Zuverlässigkeit** \| Kein Datenverlust bei App-Kill/Absturz während Tracking (Recovery-Pflicht); …". **Der Schritt „Produktqualitätsanforderung ⇒ der Nutzer benötigt diese Qualität" ist ein Ebenensprung und damit ein Zwischenglied** — genau die Ableitungsform, die in Runde 5 bei REQ-007 und REQ-019 verworfen wurde. Verschärfend: `SRC-001:18` stellt fest „Bestehende Apps zeichnen das auf — mehr nicht", behauptet also gerade **kein** Zuverlässigkeitsdefizit als Nutzerproblem. **Warum `not-linked` und nicht `broken`:** VIS-003 ist **vorhanden** und fachlich passend für REQ-004; unbelegt ist der Beleggrad der tragenden Klausel, nicht ihre Existenz. `broken` behauptet ein **fehlendes** Kettenglied und wäre hier falsch. Die Lage ist die von **REQ-037/VIS-011**: Anker vorhanden und passend, aber ASSUMPTION und unbestätigt → zählt nach Registry §8 Punkt 15 nicht als erfüllt. ⚠️ **Abweichung von der Gegenprüfung, offengelegt:** die Folgenlinse verlangte `broken` mit Verweis auf TRC-006/007/019. Dort war der Anker **entfernt**; hier bleibt er. Die Abweichung ist bewusst und milder als der Befund. **Kein VIS-Item umgedeutet, keine VIS-ID vergeben, kein Anker entfernt.** Die endgültige Einstufung hängt an der Nutzerentscheidung über den ASSUMPTION-Rest von VIS-003 (Nutzerauftrag Punkt 2) und liegt **nicht** bei diesem Owner. |
| Vision-Anker — durchgeführte Prüfung (2026-07-20) | **VIS-007 entfernt, nicht kommentiert.** VIS-007 verlangt, dass **Score und Empfehlungen** Datenbasis, Gründe und Unsicherheit erklären. REQ-004 erzeugt weder Score noch Empfehlung — es liegt auf **Gate A0**, vor jeder Health-Ausgabe. Die naheliegende Brücke („REQ-004 klassifiziert Punkte als *unsicher*, VIS-007 verlangt Unsicherheit zu erklären") verwechselt die **Qualitätsmarke eines einzelnen GPS-Punkts** mit der **Unsicherheit einer Health-Aussage**. **Entscheidend für die Konsistenz:** §3 begründet bei **REQ-032** die Ablehnung von VIS-007 wörtlich damit, es betreffe „die **Erklärbarkeit der Health-Auswertung**, nicht die **Vollständigkeit** der Signale". Dieselbe Begründung schließt REQ-004 aus — es ist ebenfalls ein Signalqualitäts-Requirement. Den Anker bei REQ-032 zu verwerfen und bei REQ-004 zu behalten wäre ein Widerspruch in derselben Datei. |
| Canvas Item (atomar) | **CAN-028** (Value Promise „Verlässliches Tracking" — primärer Anker), CAN-113 (Evidence-Annahme „Referenzstrecken"). **CAN-100 am 2026-07-20 aus dieser Zeile entfernt** — es ist ein **Risiko**-Item und steht jetzt in der Zeile „Risiko"; siehe §6.1.2. |
| Acceptance Criterion | AC-004 — Zu REQ-004 — Then: Akzeptierte, verworfene und unsichere Punkte sind deterministisch und nachvollziehbar klassifiziert. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Klassifikationsverteilung des Filters ueber reale Drift-, Tunnel-, Sprung- und Hochgeschwindigkeits-Aufzeichnungen (akzeptiert / verworfen / unsicher), Reproduzierbarkeit bei wiederholtem Lauf ueber dieselbe Fixture, Restfehler in der Distanz nach Filter, Vollstaendigkeit der Pflichtfelder je Trackpunkt (Position, Zeit, Genauigkeit, verfuegbare Bewegungsmetadaten). Run-Fixtures (Drift im Stand, niedrige Geschwindigkeit) und Bike-Fixtures (hohe Geschwindigkeit, lange Geraden) werden getrennt gefuehrt. |
| Target / Pass Condition | AC-004 als Pass/Fail: die Klassifikation ist deterministisch - identische Eingabe erzeugt zu 100 % identische Ausgabe - und jede Entscheidung ist auf eine benannte Regel zurueckfuehrbar. Der Restfehler nach Filter zahlt auf NFR-001 (< 3 %) ein. Ein Zielwert fuer eine zulaessige Verwurfsquote existiert in keinem Artefakt: MISSING; er wird nicht geraten, sondern dokumentiert. |
| Measurement Window | Je Fixture-Suite-Lauf in CI (bei jedem Commit an der Filterlogik); Neuaufnahme realer Fixtures vor jedem Gate ab A0. |
| Evidence Needed | EV-004 — Drift-, Tunnel-, Sprung- und Hochgeschwindigkeits-Fixtures. |
| Evidence Source | EV-004 (Drift-, Tunnel-, Sprung- und Hochgeschwindigkeits-Fixtures); Mindestklasse real-boundary-smoke: die Fixtures muessen aus realen Aufzeichnungen stammen, sonst prueft der Test nur sich selbst (docs/traceability.md). Hinweis: das PRD fuehrt REQ-004 selbst mit Source Type ASSUMPTION (Herkunft SRC-005) - das betrifft die Herkunft des Requirements, nicht die hier gesetzte Pruefbedingung. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. |
| Release Gate | GATE-A0 |
| Status | **not-linked** *(geändert 2026-07-20 Runde 6: der Vision-Anker VIS-003 bleibt, seine tragende Klausel ist auf Bedürfnisebene unbelegt; die Vorfassung führte `linked`)* · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — Filterlogik ist rein, aber die Fixtures müssen aus realen Drift-/Tunnel-Aufzeichnungen stammen, sonst prüft der Test nur sich selbst. **Unverändert Runde 6:** die Mindestklasse hängt an der Fixture-Herkunft, nicht am Vision-Anker; sie wird durch die Herabstufung **nicht** abgesenkt. |
| Risiko | **CAN-100 (GPS-Drift verfälscht Distanz und Route), Register RISK-002** — REQ-004 **mindert** dieses Risiko, es erzeugt es nicht; `canvas-risk-status` bleibt deshalb `aligned`. *Bis zum 2026-07-20 stand CAN-100 als **primärer** Canvas-Anker in der Kernmatrix — ein Risiko-Item in der Spalte für den primären atomaren Anker.* |
| Offene Entscheidung | offene Fragen: OQ-002 · **BLOCKER (neu 2026-07-20): REQ-004 hat kein atomares Capability-Item.** Seine drei Anker waren ein **Risiko** (CAN-100), ein **Wertversprechen** (CAN-028) und eine **Evidence-Annahme** (CAN-113) — keines davon sagt zu, dass das Produkt ein GPS-Datenmodell mit deterministischem Filter *hat*. Die Capability-Gruppe CAN-047…CAN-070 und CAN-138/139/142/143 führt kein solches Item; **CAN-048** („Robustes Foreground-Tracking") trägt laut Registry REQ-002 und wird hier **nicht** mitbenutzt. Siehe §6.1.2 — **nicht** in §6.1 mitgezählt, weil §6.1 ausschließlich fehlende Problem-Anker führt. · **Schwacher Problem-Anker, offengelegt:** CAN-013 („Tracker liefern Daten ohne verständliche Bedeutung") beschreibt fehlende **Bedeutung** vorhandener Daten; REQ-004 behandelt **falsche** Daten. Der Anker bleibt bis zur Nutzerentscheidung stehen und wird in §4.1 als schwach gekennzeichnet, **nicht** stillschweigend als tragfähig geführt. |
| Rationale | Datenqualitaet des GPS-Modells ist technische Qualitaet und die Vorbedingung fuer jede spaetere Aussage (Distanz, Score, Territory). Determinismus ist ein pruefbares Pass/Fail; eine Verwurfsquote als Ziel zu setzen waere ein erfundener Wert, weil sie von Strecke und Geraet abhaengt. |

---

### REQ-005 — Robuste lokale Aktivitätsspeicherung

| Feld | Wert |
|---|---|
| Trace ID | TRC-005 |
| Vision Item | VIS-005 — Project Goal: Zuerst einen belastbaren Health-Tracker etablieren; danach Accounts, Community, Teams und erst n |
| Canvas Item (atomar) | CAN-131, CAN-028 |
| Acceptance Criterion | AC-005 — Zu REQ-005 — Then: Keine Aktivität geht verloren und Migrationen sowie Indexe bleiben konsistent. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Datenverlustrate ueber Schreib-, Kill- und Migrationszyklen, Anteil erfolgreicher Schema-Migrationen ueber das Fixture-Set, Transaktionsintegritaet (Anzahl halb geschriebener oder verwaister Sessions), Schreiblatenz bei langen Tracks. |
| Target / Pass Condition | AC-005 und NFR-003 als Pass/Fail mit Schwelle 0: 0 verlorene Aktivitaeten ueber Kill- und Migrations-Fixtures, 0 inkonsistente Indexe nach Migration, jede Migration ist idempotent wiederholbar. Kein Prozentziel - die geforderte Schwelle ist ausdruecklich null Verlust. |
| Measurement Window | Je CI-Lauf der Repository- und Migrations-Tests; zusaetzlich ein Kill-Test gegen die echte lokale Datenbank auf dem Geraet vor jedem Gate ab A0. |
| Evidence Needed | EV-005 — SQLite-Repository-Tests, Kill-Test und Migrations-Fixtures. |
| Evidence Source | EV-005 (SQLite-Repository-Tests, Kill-Test und Migrations-Fixtures); Mindestklasse real-boundary-smoke - Kill-Test und Migration muessen gegen die echte lokale DB auf dem Geraet laufen. ASM-102 (SQLite statt AsyncStorage) ist eine offene Annahme, die durch einen technischen Spike zu bestaetigen ist. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. |
| Release Gate | GATE-A0 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — Kill-Test und Migration müssen gegen die echte lokale DB auf dem Gerät laufen. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002 |
| Rationale | Persistenz ist Betriebszuverlaessigkeit mit einer harten Nullschwelle; jedes Prozentziel waere hier schwaecher als die Anforderung selbst. Sportspezifische Trennung ist requirement-spezifisch nicht anwendbar: die Speicherung ist sportneutral, sie speichert dieselbe Trackpunkt-Struktur fuer Run und Bike; sportabhaengig sind nur die daraus abgeleiteten Metriken (REQ-001). |

---

### REQ-006 — Routenplanung

| Feld | Wert |
|---|---|
| Trace ID | TRC-006 |
| Vision Item | **MISSING — BLOCKER.** Kein VIS-Item trägt die Aussage „eine Route vor der Aktivität planen". **VIS-003 ist am 2026-07-20 als Anker entfernt worden**, nicht nur kommentiert. |
| Vision-Anker — durchgeführte Prüfung (2026-07-20) | **VIS-003 entfernt. Prüfung von der Registry ausdrücklich beauftragt** (§8 Punkt 40: „Er ist nach dem Muster §6.1.1 zu prüfen — **nicht** zu übernehmen, weil er existiert", Owner: Traceability-Owner, Phase 2/3). **Ergebnis: VIS-003 trägt REQ-006 nicht.** VIS-003 nennt vier Bedürfnisse — verlässliches Tracking, verständliche Health-Auswertung, konkrete Fortschrittssignale, sicherer Zugang zu lokalen Trainingspartnern. **Eine Route vor dem Start zu planen ist keines davon.** Es ist Vorbereitung, nicht Aufzeichnung, nicht Auswertung, nicht Fortschritt, nicht Zugang. **Der ausschlaggebende Konsistenzgrund:** dieselbe Lesart ist am 2026-07-20 für **REQ-041** (Wiederverwendung einer gespeicherten Route) ausdrücklich verworfen worden, und dafür wurde eigens **VIS-014** reserviert. VIS-003 bei REQ-041 zu verwerfen und bei REQ-006 zu behalten hieße, dieselbe Aussage in zwei Zeilen gegensätzlich zu bewerten. **Es wird kein anderes VIS-Item umgedeutet und keine VIS-ID erfunden.** Anders als bei REQ-038/039/041 ist für die **Routenplanung** nicht einmal eine VIS-ID reserviert — dieselbe Lage wie bei REQ-032 und REQ-031. |
| Canvas Item (atomar) | CAN-050, CAN-091, CAN-092, CAN-093, CAN-094, CAN-095, CAN-096, CAN-097, CAN-089. **Befund 2026-07-20:** CAN-050 („Routenplanung **und** gespeicherte Routen") ist selbst ein Composite und wird deshalb in Registry §8 Punkt 39 als BLOCKER geführt. Es bleibt hier der Anker — die Atomisierung ist eine Nutzerentscheidung und wird **nicht** vorweggenommen. |
| Acceptance Criterion | AC-006 — Zu REQ-006 — Then: Eine plausible Route beziehungsweise ein Ziel mit Distanz und Fehlermeldungen wird angezeigt. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Routing-Erfolgsrate und Routing-Latenz je Sportprofil (der Proxy uebersetzt run -> foot-walking und ride -> cycling-regular, CAN-094), API-Timeout- und Fehlerrate des Routing-Proxys, Anteil Planungen, die ohne verstaendliche Fehlermeldung scheitern, Abweichung zwischen geplanter Zieldistanz und tatsaechlicher Routenlaenge. Run und Bike getrennt, weil beide Profile unterschiedliche Wegenetze nutzen. |
| Target / Pass Condition | AC-006 als Pass/Fail ueber zehn reale Routenszenarien je Sport (EV-006): jedes Szenario liefert entweder eine plausible Route mit Distanz oder eine verstaendliche Fehlermeldung. Zusaetzliche harte Kontrolle aus CAN-092 und NFR-007: der Bundle-Scan zeigt 0 Routing-Provider-Keys im App-Bundle. Zielwerte fuer Erfolgsrate, Latenz und Timeout-Rate sind MISSING: OQ-004 (Anbieter und Kostenlimits) ist offen, ohne Anbieter ist kein Latenzziel ableitbar. |
| Measurement Window | Zehn reale Routenszenarien je Sportart vor Gate A0; Erfolgs-, Fehler- und Latenzwerte fortlaufend je Proxy-Aufruf erhoben und je Gate ausgewertet. |
| Evidence Needed | EV-006 — Routing-Service-Tests und zehn reale Routenszenarien je Sport. |
| Evidence Source | EV-006 (Routing-Service-Tests und zehn reale Routenszenarien je Sport); Mindestklasse real-boundary-smoke - ein gemockter Routing-Response verdeckt genau den NFR-007-Pfad (docs/traceability.md). Ergaenzend: Proxy-Integrationstest und Bundle-Scan aus ASM-103. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Dokumentierte Rollenreferenz zur gekoppelten offenen Frage OQ-004 ('Engineering/Product') - das ist der Owner der Frage, nicht der REQ-Owner. |
| Release Gate | GATE-A0 |
| Status | **broken** (Vision-Anker MISSING seit 2026-07-20) · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | blocked |
| evidence-class-required | real-boundary-smoke — Netzwerk plus echter Routing-Provider über den A0-Proxy; ein gemockter Routing-Response verdeckt genau den NFR-007-Pfad. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-004, OQ-005, OQ-011 · **Canvas-BLOCKER:** CAN-019 (Planungs- und Orientierungsproblem vor der Aktivitaet) ist reserviert und inhaltlich MISSING. REQ-006 hat damit keinen atomaren Canvas-Problembezug, sondern nur Capability- und Constraint-Anker. Zaehlt laut Canvas nicht als erfuellte Canvas-Referenz. |
| Rationale | Routenplanung wird als Betriebsqualitaet gemessen (Erfolgsrate, Latenz, Fehlerverhalten), nicht als Nutzungsquote; die Uebernahme geplanter Routen durch andere Nutzer ist REQ-019 und liegt erst ab Gate B vor. Statusnachzug: docs/traceability.md fuehrt REQ-006 als 'blocked' unter anderem wegen OQ-011 - OQ-011 ist durch die Nutzerentscheidung vom 2026-07-19 (Ablageort infra/routing-proxy/) entschieden, docs/decisions/open-questions.md fuehrt ihn noch offen. Der Rest der Blockade (OQ-004, OQ-005) besteht fort. |
| Befund | Die Nutzerentscheidung „A0-Routing über serverseitigen Proxy“ zieht OQ-005 (Backend) und OQ-004 (Karten-/Routinganbieter, Kostenlimits) auf **vor A0** vor. CAN-131 beschreibt A0 als lokale Stufe. **OQ-011 (Ablageort) ist seit 2026-07-19 resolved** — `infra/routing-proxy/`, abgebildet in CAN-097 — und blockiert nicht länger; `docs/decisions/open-questions.md` führt ihn noch als offen (Nachzug Phase 3). Verbleibend blockierend: OQ-004 und OQ-005. Sekundär: CAN-019 (Problembezug) ist reserved, kein Erfolgssignal. |

---

### REQ-007 — Routenbezogener Fortschritt

| Feld | Wert |
|---|---|
| Trace ID | TRC-007 |
| Vision Item | **MISSING — BLOCKER.** Kein VIS-Item trägt die Aussage „Fortschritt entlang einer geplanten Strecke". **VIS-003 ist am 2026-07-20 als Anker entfernt worden**, nicht nur kommentiert. |
| Vision-Anker — durchgeführte Quellenprüfung (2026-07-20, Runde 5) | **Die Vorfassung führte hier eine OPEN QUESTION mit der Begründung, die Lesart von „Fortschritt" sei „aus dem Wortlaut nicht entscheidbar". Diese Begründung ist entfallen:** die vier Quelldokumente sind seit dem 2026-07-20 lesbar, und sie entscheiden die Frage. **Wortlaut in den Quellen — „Fortschritt" wird durchgehend longitudinal gebraucht:** SRC-001 §1.2 Mission 2: „**Spürbaren Fortschritt** — Punkte, Ränge, Avatare, Seasons: Erfolge, die man fühlt und feiert"; SRC-001 §2.1: „Motivation stirbt an drei Stellen: **Ich verstehe meinen Fortschritt nicht** · …"; SRC-001 §3.3 (Persona Lena): „will verstehen, **ob sie sich verbessert**"; SRC-003 §1.1 Priorität 2: „Challenges & Spiel — **Fortschritt**, Seasons, Areale als Motivationsmaschine". **Keine dieser Stellen meint den Fortschritt innerhalb einer laufenden Aktivität.** Die aktivitätsinterne Restdistanz erscheint in den Quellen ausschließlich auf **funktionaler** Ebene: SRC-001 T-02 „Modus B: Route per Wegpunkte planen oder km-Ziel; **geplante vs. verbleibende km**" (Teil 3 PRD) und SRC-003 §9 GATE A „**verbleibende km korrekt**" (Gate-Kriterium) — **nie auf Vision-Ebene. Ergebnis: VIS-003 trägt REQ-007 nicht.** Konsistenzgrund: für **REQ-006** (Routenplanung) ist VIS-003 am 2026-07-20 aus genau diesem Grund entfernt worden. REQ-006 und REQ-007 sind die Planungs- und die Durchführungshälfte desselben Modus B; VIS-003 bei einer zu verwerfen und bei der anderen zu behalten wäre dieselbe Aussage in zwei Zeilen gegensätzlich bewertet. **Kein VIS-Item umgedeutet, keine VIS-ID erfunden** — für routenbezogene Navigation ist, anders als bei REQ-038/039/041, **nicht einmal eine VIS-ID reserviert.** ID-Bedarf an den Registry-Owner gemeldet. |
| Canvas Item (atomar) | CAN-051, CAN-028. **CAN-100 (Risiko-Item)** steht in der Zeile „Risiko"/„Befund", nicht mehr in der Ankerliste — dieselbe Rollenkorrektur wie bei REQ-004. |
| Acceptance Criterion | AC-007 — Zu REQ-007 — Then: Fortschritt bleibt monoton plausibel, Restdistanz folgt der Route und Off-Route-Zustand wird sichtbar. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Off-Route-Genauigkeit unter realem GPS-Rauschen: Anteil korrekt erkannter Abweichungen, Falschausloesungsrate bei Routentreue, Erkennungslatenz bei Richtungsumkehr und bei Schleifen, Monotonie der Restdistanz entlang der geplanten Geometrie. Run und Bike getrennt: bei Bike bedeutet dieselbe Erkennungslatenz eine deutlich groessere zurueckgelegte Fehlstrecke. ⚠️ **Offengelegt Runde 6 (2026-07-20), Wortlaut unverändert:** die Begriffe „Richtungsumkehr", „Monotonie" und „Projektion" stammen aus **keiner** der vier Quellen (Volltextsuche über `docs/sources/`: je **0 Treffer**), ebenso „Korridor" und „Hysterese" in der Pass-Bedingung. `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md:496` nennt „Route verlassen" **einmal**, dort aber als Audio-Ansage in „Plan 5 (optional vor v1.0)"; `docs/sources/SRC-004-tracking-and-planned-routes.md:2423` führt „off-route detection" ausdrücklich unter „**Deferred to Later Plans**". Ein A0-MUSS ist damit nicht gedeckt. **Das Signal bleibt stehen** (Nutzerauftrag Punkt 4), ist aber als ASSUMPTION zu lesen, nicht als belegte Anforderung. |
| Target / Pass Condition | AC-007 als Pass/Fail: die Restdistanz folgt der geplanten Polyline und ist nicht Gesamtdistanz minus gelaufene Distanz; der Fortschritt bleibt monoton plausibel; der Off-Route-Zustand wird sichtbar. Numerische Schwellen fuer Off-Route-Korridor, Hysterese und maximale Erkennungslatenz existieren in keinem Artefakt: MISSING - vom DRI vor Gate A0 zu entscheiden, hier wird kein Wert geraten. ⚠️ **Nachzug Runde 6 (2026-07-20):** die Vorfassung berief sich hier auf „(CAN-051 hält fest, dass die Subtraktion ausdrücklich verboten ist)" und machte damit ein als `EXPLICIT` geführtes Canvas-Item zur Autorität einer Pass/Fail-Bedingung. **Die Berufung ist entfernt.** CAN-051 wird nach Nutzerauftrag Punkt 2 zurückgestuft (Owner Canvas). Die Bedingung selbst bleibt **unverändert bestehen** — Nutzerauftrag Punkt 4 erhält REQ-007 ausdrücklich als route-aware Verbesserung —, ihre Herkunft ist jetzt offengelegt statt gewaschen: sie ist eine **bewusste Abweichung** von der einzigen Quelle, die den Rechenweg festlegt. `docs/sources/SRC-004-tracking-and-planned-routes.md:416-417` spezifiziert „`return Math.max(0, plannedMeters - coveredMeters);`", `:382` prüft sie als Sollverhalten („`it('subtracts covered from planned', …)`"), `:2360` verdrahtet sie gegen die zurückgelegte Gesamtdistanz. SRC-001, SRC-002 und SRC-003 sagen zum Rechenweg **nichts**. Träger der Abweichung ist allein DEC-004 — und der steht in `docs/decisions/decision-log.md:10` auf `proposed`, nicht `user-confirmed`. **Bis zur Nutzerbestätigung ist die Pass-Bedingung keine belegte Produktwahrheit.** |
| Measurement Window | Je Abweichungs-Testfahrt/-lauf auf der Referenzstrecke, je Sportart und Plattform, vor Gate A0; Polyline-Projektions-Fixtures bei jedem CI-Lauf. |
| Evidence Needed | EV-007 — Polyline-Projektions-Fixtures und reale Abweichungstests. |
| Evidence Source | EV-007 (Polyline-Projektions-Fixtures und reale Abweichungstests); Mindestklasse real-boundary-smoke - die Projektion ist rein, die Off-Route-Erkennung haelt aber nur unter realem GPS-Rauschen. RISK-006 (Routenrest bei Abweichungen falsch) ist offen. |
| Source Type | **MISSING — unverändert (Runde 6 geprüft, nicht geändert).** ⚠️ **Abgrenzung zu Nutzerauftrag Punkt 4, ausdrücklich offengelegt.** Der Auftrag lautet, REQ-007 „bis zur Nutzerbestätigung ASSUMPTION" zu führen. Das ist **hier nicht umgesetzt**, weil dieses Feld etwas anderes bezeichnet als das gleichnamige Feld der `canonical_file`: §1 Legende und §2 bestimmen `Source Type` in dieser Matrix als Herkunft der **Pass-Bedingung / des Zielwerts** („`EXPLICIT` gilt dort für den **Zielwert**, nicht für die Anforderung"), und REQ-007 steht deshalb in der Liste der **MISSING-Schwellen**. Der Zielwert — Korridorbreite, Hysterese, Erkennungslatenz — existiert in **keinem** Artefakt und in keiner der vier Quellen (Volltextsuche „Korridor", „Hysterese" über `docs/sources/`: **0 Treffer**). Ihn auf `ASSUMPTION` zu setzen hieße zu behaupten, es gebe eine Quelle für Werte, die niemand geschrieben hat — eine **stille Hochstufung**. `docs/prd/revyr-endurance-platform.prd.md:181` führt REQ-007 mit `ASSUMPTION` / Quelle `SRC-005`; das betrifft die **Anforderungsherkunft** und steht zu diesem Wert **nicht** im Widerspruch. **Verbleibender echter Defekt, hier gemeldet statt geglättet:** die beiden Achsen tragen dasselbe Feldlabel. Die Matrix führt an anderer Stelle bereits den eindeutigen Namen `target_source_type` (REQ-019). Eine projektweite Umbenennung ist ein **Metamodell-Eingriff** und liegt beim Registry-Owner, nicht hier. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Die fehlenden Korridor-/Hysteresewerte brauchen genau diesen DRI. |
| Release Gate | GATE-A0 |
| Status | **broken** (Vision-Anker MISSING seit 2026-07-20) · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | real-boundary-smoke — Projektion ist rein, Off-Route-Erkennung hält aber nur unter realem GPS-Rauschen. |
| Risiko | RISK-006 |
| Offene Entscheidung | offene Fragen: OQ-002 · **Canvas-BLOCKER:** CAN-019 (Planungs- und Orientierungsproblem) ist reserviert und inhaltlich MISSING - kein atomarer Canvas-Problembezug fuer REQ-007. |
| Rationale | Routenbezogener Fortschritt ist eine Genauigkeitseigenschaft und wird als solche gemessen. Der entscheidende Zielwert (Korridorbreite und Latenz) fehlt in allen Artefakten, deshalb source_type MISSING statt einer plausibel klingenden Zahl. Sportgetrennte Messung ist zwingend, weil Geschwindigkeit direkt in die tolerierbare Latenz eingeht. |
| Befund | CAN-100 (GPS-Drift): Off-Route- und Falschrichtungserkennung erzeugt bei Drift Fehlzustände direkt im Live-UI. Register: RISK-006. |

---

### REQ-008 — Verlauf und Detailansicht

> **Verengt am 2026-07-19, nicht deprecated.** GPX-Export → **REQ-039**, Streckenwiederverwendung
> → **REQ-041**, Streckenvergleich → **REQ-042**. Es bleibt dieselbe Anforderung, auf ihren
> atomaren Kern reduziert; deshalb keine neue ID (Registry §6.4, §7.4.3).
> Alttitel: „Verlauf, Wiederverwendung und Export“.
>
> ⚠️ **Nachzug 2026-07-20:** die Verweisziele lauteten bis dahin „REQ-040“. REQ-040 ist seit dem
> 2026-07-20 **deprecated**; wer der Kette REQ-008 → REQ-040 mechanisch folgt, landet auf einer
> deprecateten ID. Die **wirksame** Nachfolgemenge von REQ-008s abgetrennten Klauseln ist
> **REQ-039, REQ-041, REQ-042** (Registry §6.3, Hinweis zur transitiven Nachfolge).

| Feld | Wert |
|---|---|
| Trace ID | TRC-008 |
| Vision Item | VIS-003 — User Need: Nutzer benötigen verlässliches Tracking, verständliche statt abstrakte Health-Auswertung, konkrete  ⚠️ **Zitat des Altstands (Runde 6, 2026-07-20):** VIS-003 wird nach Nutzerauftrag Punkt 2 verengt; die Qualifizierer „verlässlich" und „sicher" sind in keiner der vier Quellen belegt und werden als ASSUMPTION-Rest getrennt geführt. **Der Wortlaut wird hier nicht nachgezogen**, weil er wörtlich aus dem Vision-Item stammt und dessen Fassung dem Vision-Owner obliegt. Diese Zeile stützt sich **nicht** auf einen der beiden Qualifizierer — anders als REQ-004, siehe §6.1.1. |
| Canvas Item (atomar) | **CAN-138** (Verlauf und Detailansicht lokal gespeicherter Run- und Bike-Aktivitäten), CAN-030. **CAN-050 am 2026-07-20 entfernt** — siehe nächste Zeile. |
| CAN-050 — warum die Verknüpfung entfernt wurde (2026-07-20) | Die Registry ordnet **CAN-050 („Routenplanung und gespeicherte Routen") ausdrücklich REQ-006 zu** (§6.3: „Trägt REQ-006"). REQ-008 führte es dennoch als Anker — eine ID mit **zwei Bedeutungen in zwei Requirement-Kontexten**, belegt in Registry §7.5.5 (`traceability.md:465`) und §8 Punkt 39. **Warum der Fehler plausibel las:** beide Requirements handeln von „gespeicherten Dingen, die man wiederfindet". Sie sind trotzdem verschieden — CAN-050 meint eine **geplante Route** (Artefakt **vor** der Aktivität, Gate A0, REQ-006), REQ-008 meint eine **aufgezeichnete Aktivität** (Artefakt **nach** der Aktivität). Genau diese Verwechslung ist die wiederkehrende Defektklasse. **Nicht vorweggenommen:** dass CAN-050 selbst ein Composite ist (Planung + gespeicherte Routen), bleibt ein eigener BLOCKER für den Nutzer (§6.1.2) und wird hier **nicht** durch eine eigenmächtige Aufteilung erledigt. |
| Acceptance Criterion | AC-008 — Zu REQ-008 — Then: Verlauf und Detailansicht liefern die korrekten sportbezogenen Daten und die aufgezeichnete Route. **Verengt 2026-07-19:** die Klausel „und exportierbar“ liegt jetzt bei AC-039, der Vergleich bei **AC-043** *(nachgezogen 2026-07-20: AC-040 ist deprecated)*. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | **Getrennt für Run und Bike:** Ladefehlerrate und Ladezeit von Verlauf und Detailansicht bei wachsender Datenmenge; Anteil regulär abgeschlossener Aktivitäten, die nach einem App-Neustart im Verlauf erscheinen; Anteil Detailansichten, die den korrekten Track laden; Vollständigkeit und **Sportrichtigkeit** der Kernmetrik (Run: Pace; Bike: Geschwindigkeit); Anzahl beschädigter oder unbekannter Aktivitätsdatensätze, die zu einem unkontrollierten Zustand statt zu einem kontrollierten Fehler führen. |
| Target / Pass Condition | AC-008 als Pass/Fail mit Nullschwellen, **Run und Bike getrennt nachgewiesen**: (a) 100 % der regulär abgeschlossenen Aktivitäten erscheinen **nach Neustart** im Verlauf · (b) die Detailansicht lädt in 100 % der Fälle den korrekten Track · (c) **Run zeigt Pace**, (d) **Bike zeigt Geschwindigkeit** — 0 Verwechslungen · (e) **0 Aktivitäten gehen nach regulärem Abschluss verloren** · (f) beschädigte oder unbekannte Aktivitätsdaten führen in 100 % der Fälle zu einem **kontrollierten Zustand**. Eine Nutzungs- oder Wiederverwendungsquote wird **nicht** gesetzt — ein solcher Zielwert wäre erfunden. |
| Measurement Window | Je Gate-A0-Abnahme und bei jeder Änderung an Datenmodell oder Detailansicht; **je Sportart und je Plattform (iOS, Android) mindestens ein vollständiger Durchlauf einschließlich App-Neustart**. |
| Evidence Needed | **EV-008** — Repository- und UI-Test für **Verlauf und Detailansicht**, **je Sportart getrennt** (Run zeigt Pace, Bike zeigt Geschwindigkeit); Neustart-Test auf Persistenz; Negativtest auf beschädigte oder unbekannte Aktivitätsdaten. *Wortlaut am 2026-07-20 an die `canonical_file` und die Registry §6.7 angeglichen.* |
| EV-008 ↔ EV-039 — kanonische Trennung (verbindlich, 2026-07-20) | **EV-008 ist AUSSCHLIESSLICH Evidence für Verlauf und Detailansicht.** Es enthält **keinen** GPX-, Export-, Portabilitäts- oder Fremd-App-Nachweis. **EV-039 ist AUSSCHLIESSLICH der GPX-Kompatibilitäts- und Exportnachweis** und enthält **keinen** Verlaufs- oder Detailansichts-Nachweis. Die Trennung ist bewusst in **beide** Richtungen ausgeschrieben: eine einseitige Formulierung lässt die Gegenrichtung offen, und genau dort entstand die Doppelführung. **Herkunft des Defekts:** die Überlappung lief **nicht** über das PRD — das hatte den GPX-Anteil bereits am 2026-07-19 ausgelagert — sondern über die veraltete EV-008-Definition der **Registry**, die nach Registry §1 bei jeder Prüfung gewonnen hätte. **Prüfregel: Wer einen GPX-Nachweis unter EV-008 findet oder einen Verlaufs-Nachweis unter EV-039, hat einen Validierungsfehler gefunden — keine Redundanz.** |
| Evidence Source | EV-008; Mindestklasse `real-boundary-smoke` — Persistenz über einen echten Prozessneustart ist mit keinem Fake beweisbar. |
| Source Type | **ASSUMPTION** — zwei unabhängig tragende Gründe: (1) die Pass-Bedingungen sind analytische 0-/100-%-Schranken, belegbedürftig und unbelegt bleibt die Anforderung selbst (sie trug `EXPLICIT` über SRC-001/SRC-003, laut `docs/SOURCE-MAP.md` **nicht auffindbar**); (2) der **verengte Wortlaut** stammt aus der Nutzerentscheidung vom 2026-07-19 und ist nicht ausdrücklich als Anforderungstext bestätigt. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. |
| Release Gate | GATE-A0 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — Persistenz über einen echten Prozessneustart ist mit keinem Fake beweisbar. **Geändert 2026-07-19:** die frühere Begründung („GPX muss in einem echten Fremdsystem geöffnet werden“) gehört seit der Verengung zu **REQ-039**, nicht mehr hierher. Die Klasse bleibt dieselbe, der Grund ist ein anderer. |
| Risiko | RISK-005 — „Bike zeigt falsche Laufmetriken“ wird genau in der Detailansicht sichtbar. **Ergänzt 2026-07-19:** die Vorfassung führte hier „kein Registereintrag referenziert“; durch die Verengung auf die sportrichtige Kernmetrik ist RISK-005 jetzt der einschlägige Registereintrag. |
| Offene Entscheidung | offene Fragen: OQ-002 · **Canvas-BLOCKER geschlossen (2026-07-19):** ~~CAN-071 ist reserviert und inhaltlich MISSING~~ → CAN-071 ist **deprecated** und durch atomare Items ersetzt; REQ-008 hat mit **CAN-138** erstmals einen vollständig passenden atomaren Capability-Anker. **Transitiver Hinweis:** die wirksame Nachfolgemenge von CAN-071 ist **CAN-138, CAN-139, CAN-142, CAN-143** — CAN-140 ist seit dem 2026-07-20 selbst deprecated. · **BLOCKER, der bleibt:** CAN-138 trägt `source_type ASSUMPTION`, solange der Wortlaut nicht ausdrücklich nutzerbestätigt ist — der Anker ist damit *vorhanden*, aber nicht *belegt*. |
| Rationale | Der prüfbare Kern ist **Verfügbarkeit und Korrektheit der lokal gespeicherten Historie**, nicht Nutzerverhalten. Die Run-/Bike-Trennung ist hier **nicht dekorativ**, sondern der eigentliche Fehlerfall: RISK-005 wird in der Detailansicht sichtbar, weil dort die sportartspezifische Kernmetrik ausgegeben wird. Der naheliegende Produktoutcome — Wiederverwendung gespeicherter Routen — liegt seit dem 2026-07-20 bei **REQ-041**, der Vergleich bei **REQ-042**; beides wird hier nicht mehr mitgemessen. |

---

### REQ-009 — Herzfrequenzquellen

| Feld | Wert |
|---|---|
| Trace ID | TRC-009 |
| Vision Item | VIS-007 — Health-first Boundary: Health-Ausgaben sind Orientierung, keine Diagnose. Score und Empfehlungen müssen Datenb |
| Canvas Item (atomar) | CAN-052 (Capability, primär), CAN-086 (Constraint), **CAN-022** (Problem — **ersetzt CAN-013 am 2026-07-20**, siehe nächste Zeile) |
| Canvas-Problem — durchgeführte Einzelprüfung (2026-07-20) | **CAN-013 trägt nicht, CAN-022 trägt.** **CAN-013** („Bestehende Tracker liefern Daten **ohne verständliche Bedeutung**") beschreibt Daten, die **vorhanden** sind und **nicht interpretiert** werden. REQ-009 handelt vom Gegenteil: die Herzfrequenz ist **gar nicht da**, solange keine Quelle angebunden ist. Fehlende Daten sind keine bedeutungslosen Daten. CAN-013 wurde hier als **Universal-Problemanker** benutzt — dieselbe Defektklasse, die Registry §8 Punkt 37 für REQ-037/038/039 festhält. **CAN-022** dagegen nennt die tragende Aussage **wörtlich**: „Ohne Anbindung bereits genutzter **Sportuhren** und **externer Sensoren** fehlen oder verschlechtern sich zentrale Trainingssignale wie **Herzfrequenz**, Kadenz, …". REQ-009 ist exakt die Anbindung von HF-Quellen einschließlich BLE-Sensoren; „Sportuhr" deckt zugleich den HealthKit-/Health-Connect-Pfad, weil eine Sportuhr genau dorthin schreibt. **Kein Item umgedeutet — der Treffer steht im Wortlaut.** ⚠️ **Offengelegte Abweichung, nicht geglättet:** die Registry führt CAN-022 mit **Release Gate E**, REQ-009 liegt auf **Gate A1**. Ob ein Problem-Item überhaupt ein Gate trägt (oder es nur von seinem primären Requirement REQ-032 erbt), ist im Metamodell nicht geregelt. Die Registry ist eingefroren; das Gate wird hier **nicht** geändert. **OPEN QUESTION** für den Nutzer. |
| Persona | **USER-004** (sekundär, neben USER-001 und USER-002) — **verknüpft nach semantischer Einzelprüfung.** REQ-009 liest Herzfrequenz aus HealthKit, Health Connect und **unterstützten BLE-Sensoren**; USER-004 ist über genau diesen Gerätebesitz definiert. Das ist eine **unmittelbare Deckung**, keine bloß thematische Nähe. `source_type` **ASSUMPTION** — die Persona ist unbestätigt (Registry §6.12). |
| Acceptance Criterion | AC-009 — Zu REQ-009 — Then: Live-/Verlaufs-HF und Quelle werden korrekt dargestellt; fehlende HF blockiert Tracking nicht. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Anteil Aktivitaeten mit korrekt gekennzeichneter HF-Quelle (HealthKit, Health Connect oder BLE), HF-Datenlueckenrate je Quelle, Verbindungsabbruchrate je BLE-Sensor, Anteil Aktivitaeten in denen fehlende HF das Tracking blockiert. Getrennt erhoben fuer die Run-typischen Quellen (Watch/HealthKit/Health Connect) und die Bike-typische BLE-Brustgurt-/Sensorstrecke. |
| Target / Pass Condition | AC-009 als Pass/Fail: Quelle und Datenluecken sind in 100 % der aufgezeichneten Aktivitaeten sichtbar gekennzeichnet; fehlende HF blockiert das Tracking in 0 % der Faelle. Ein Zielwert fuer die zulaessige Lueckenrate je Quelle existiert in keinem Artefakt: MISSING - die Lueckenrate wird gemessen und dokumentiert (EV-009), aber nicht mit einer erfundenen Schwelle bewertet. |
| Measurement Window | Je Aktivitaet erhoben; Abnahme je Gate A1 mit mindestens einem echten Geraetetest je Plattform und je Quelle (HealthKit, Health Connect, BLE-Gurt). |
| Evidence Needed | EV-009 — Echte Geräte und BLE-Gurt je Plattform. |
| Evidence Source | EV-009 (echte Geraete und BLE-Gurt je Plattform); Mindestklasse production-verified - reale Luecken- und Quellensemantik entsteht nur am realen Geraet. CAN-086 (Health-Berechtigungen brauchen belastbare Begruendung) und RISK-010 (Store-Ablehnung) sind einschlaegig. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. OQ-003 (Referenzgeraete) ist MISSING und begrenzt die Aussagekraft der Geraetematrix. |
| Release Gate | GATE-A1 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | production-verified — HealthKit, Health Connect und BLE-Gurt liefern nur am realen Gerät reale Lücken- und Quellensemantik. |
| Risiko | RISK-009, RISK-010 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-003 · **Canvas-BLOCKER geschlossen (2026-07-19):** ~~CAN-025 ('Ambitionierte Ausdauersportler:innen') hat im PRD keine USER-ID~~ → **USER-004** ist vergeben und im PRD eingetragen (Registry §6.12, `prd.md:50`). · **BLOCKER, der bleibt:** USER-004 trägt `source_type ASSUMPTION` und ist als Persona **unbestätigt**; bis zur Nutzerbestätigung trägt REQ-009 damit einen *benannten*, aber nicht *belegten* Zielgruppenanker. |
| Rationale | HF-Anbindung ist Datenerfassungsqualitaet: messbar sind Quellenkennzeichnung, Luecken und Verbindungsstabilitaet - nicht Nutzerverhalten. Die Trennung nach Sportart folgt der realen Hardwarelage: Bike-Sensorik laeuft ueber BLE, Run typischerweise ueber Watch/Health-Plattform. Nebenbefund: docs/traceability.md vermerkt bei REQ-009 die 'ambitionierte' Persona als im PRD MISSING (CAN-025) - das bleibt ein offener Zielgruppenbezug, kein Messproblem. |
| Befund | CAN-108 (Store-Ablehnung) und CAN-086 (Health-Berechtigungen): HealthKit-/Health-Connect-Zugriff unterliegt eigenen Policy- und Zweckbindungsregeln. Register: RISK-009, RISK-010. |

---

### REQ-010 — Erklärbarer Belastungs-Score mit Confidence

| Feld | Wert |
|---|---|
| Trace ID | TRC-010 |
| Vision Item | VIS-007 — Health-first Boundary: Health-Ausgaben sind Orientierung, keine Diagnose. Score und Empfehlungen müssen Datenb |
| Vision Item (ergänzend, aus dem Messmodell) | VIS-006 |
| Canvas Item (atomar) | CAN-126, CAN-052, CAN-029, CAN-102 |
| Acceptance Criterion | AC-010 — Zu REQ-010 — Then: Nutzer sehen Score, konkrete Gründe, Datenbasis, fehlende Signale und die Unsicherheit der Aussage. |
| Measurement Type | **PRODUCT_OUTCOME** |
| Signal / Control Evidence | Nutzung der Health-Erklaerung: Anteil abgeschlossener Aktivitaeten, bei denen das Warum-Sheet zum Belastungs-Score geoeffnet wird (CAN-126). Als Kontextgroesse daneben der Anteil Scores, die mit reduzierter Confidence (Fallback ohne Herzfrequenz) ausgegeben werden, damit eine niedrige Erklaerungsnutzung nicht mit fehlender Datenbasis verwechselt wird. Run und Bike getrennt ausgewiesen, weil die HF-Verfuegbarkeit und damit die Confidence-Verteilung sportspezifisch ist. |
| Target / Pass Condition | VIS-006 Zeile A: Oeffnungsrate der Score-Erklaerung > 25 %. ASSUMPTION - dieser Wert ist ein gesetztes Produktziel ohne empirische Grundlage und darf nicht als validierte Produktwahrheit dargestellt werden. Daneben als harte Kontrolle aus AC-010: der Score nennt in 100 % der Faelle Gruende, Datenbasis, fehlende Signale und Unsicherheit; ohne Herzfrequenz wird ein klar begrenzter Fallback ausgewiesen. |
| Measurement Window | Signal je Aktivitaet erhoben, ausgewertet ueber eine rollierende 28-Tage-Kohorte ab Gate A1. Das 28-Tage-Fenster ist aus dem Vier-Wochen-Bezug von CAN-124/VIS-006 abgeleitet; fuer die Oeffnungsrate selbst nennt kein Artefakt ein Fenster - das Fenster ist damit ASSUMPTION. |
| Evidence Needed | EV-010 — Formeltests mit/ohne HF und UI-Test des Warum-Sheets. |
| Evidence Source | EV-010 (Formeltests mit und ohne HF, UI-Test des Warum-Sheets); Mindestklasse real-boundary-smoke. MESSLUECKE: kein Requirement und kein NFR beschreibt eine Telemetrie-/Analytics-Erhebung. Ohne sie ist die Oeffnungsrate nicht erhebbar, zugleich fordern CAN-095 (local-first) und REQ-034 (Datensparsamkeit) Zurueckhaltung. Diese Luecke ist eine OPEN QUESTION fuer den DRI und beruehrt OQ-005. |
| Source Type | ASSUMPTION |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Dokumentierte Rollenreferenz zur gekoppelten Frage OQ-006 (Claims-Whitelist, 'Product/Legal') - das ist der Owner der Frage, nicht der REQ-Owner. |
| Release Gate | GATE-A1 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | real-boundary-smoke — Formel ist rein, aber Eingangsdaten kommen aus der Health-Grenze und das Warum-Sheet ist UI. |
| Risiko | RISK-008 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-005, OQ-006 |
| Rationale | Der Produktwert von REQ-010 ist genau, dass die Erklaerung genutzt wird - das ist ein echtes Nutzersignal und in der Aufgabenstellung ausdruecklich als PRODUCT_OUTCOME genannt ('Nutzung der Health-Erklaerung'). Der Zielwert stammt aus VIS-006, ist aber nirgends empirisch hinterlegt und deshalb ASSUMPTION. RISK-008 (Score wird als medizinische Aussage verstanden) macht die Erklaerkontrolle zur zwingenden Nebenbedingung. |
| Befund | CAN-102 (falsche Health-Claims): primäre Claim-Fläche. OQ-006 (Claims-Whitelist) ist offen und laut Canvas „vor A1 Public Beta“ fällig. Register: RISK-008. |

---

### REQ-011 — HF-Zonen und optionale Ansage

| Feld | Wert |
|---|---|
| Trace ID | TRC-011 |
| Vision Item | VIS-007 — Health-first Boundary: Health-Ausgaben sind Orientierung, keine Diagnose. Score und Empfehlungen müssen Datenb |
| Canvas Item (atomar) | CAN-052, CAN-102 |
| Acceptance Criterion | AC-011 — Zu REQ-011 — Then: Zonen und Hinweise reagieren korrekt; Deaktivierung verhindert jede Ansage. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Korrektheit der Zonenberechnung gegen Zonen-Fixtures fuer geschaetzte und manuell korrigierte Werte, Anzahl ausgeloester Live-Zonenhinweise bei deaktivierter Einstellung, Ansage- und Anzeigelatenz am realen Geraet mit Kopfhoerer, Anteil Aktivitaeten ohne verwertbare Zoneneinstufung. Run und Bike getrennt, weil Belastungsverteilung und damit Zonenverweildauer sportspezifisch sind. |
| Target / Pass Condition | AC-011 als Pass/Fail: Zonen reagieren korrekt auf geschaetzte und manuell korrigierte Werte; die Deaktivierung verhindert jede Ansage - 0 Ansagen in 100 % der Deaktivierungstests. Ein Genauigkeitsziel fuer die Zonenschaetzung existiert in keinem Artefakt: MISSING. Die verwendete Schaetzformel ist zusaetzlich an OQ-006 gebunden, weil eine Zonenempfehlung eine Health-Aussage ist. |
| Measurement Window | Je CI-Lauf der Zonen-Unit-Tests; Geraetetest mit Kopfhoerer je Plattform vor Gate A1; Wiederholung bei jeder Aenderung der Schaetzformel oder der Ansagelogik. |
| Evidence Needed | EV-011 — Zonen-Unit-Tests und Kopfhörer-Gerätetest. |
| Evidence Source | EV-011 (Zonen-Unit-Tests und Kopfhoerer-Geraetetest); Mindestklasse real-boundary-smoke - Audio-Ansage und vollstaendige Deaktivierung sind nur ueber echte Kopfhoerer am Geraet pruefbar. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Dokumentierte Rollenreferenz zur gekoppelten Frage OQ-006 ('Product/Legal'). |
| Release Gate | GATE-A1 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | real-boundary-smoke — Audio-Ansage und vollständige Deaktivierung sind nur über echte Kopfhörer am Gerät prüfbar. |
| Risiko | RISK-008 |
| Persona | **keine Verknüpfung mit USER-004** — Ergebnis der semantischen Einzelprüfung, nicht ein Übersehen. Gegenstand von REQ-011 sind **Zonenberechnung, Korrektur und Abschaltbarkeit**: quellenneutral und **ohne externen Sensor vollständig erfüllbar**. Der Bezug zu USER-004 besteht nur **mittelbar** über die Datenabhängigkeit von REQ-009, und eine mittelbare Abhängigkeit ist **kein Zielgruppenanker** — sonst wäre jede Anforderung, die Herzfrequenz berührt, an USER-004 zu hängen. Genau diese Universalverknüpfung ist ausgeschlossen (`prd.md:56`). |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-006 · **Früherer Canvas-BLOCKER entfernt, nicht ersetzt (2026-07-19):** die Vorfassung führte hier „Zielgruppenbezug offen: CAN-025 hat im PRD keine USER-ID“. Der Vermerk ist **in beiden Richtungen unzutreffend** — die USER-ID existiert inzwischen (USER-004), **und** REQ-011 braucht sie gar nicht. Er ist deshalb **gestrichen** und ausdrücklich **nicht** durch eine USER-004-Verknüpfung ersetzt worden. |
| Rationale | Der prüfbare Kern ist die deterministische Zonenberechnung und die vollständige Abschaltbarkeit — eine Betriebs- und Korrektheitseigenschaft mit Nullschwelle. Eine Nutzungsquote für Zonenhinweise wäre ein erfundener Engagement-KPI; für Zonen oder Audio-Ansage existiert kein Signal. **Nebenbefund entfallen:** der frühere Verweis „wie REQ-009: die ‚ambitionierte' Persona (CAN-025) fehlt im PRD“ ist überholt und wurde nicht stehen gelassen, weil er dieser Datei jetzt widerspräche. |
| Befund | CAN-102 über Zonenempfehlung und Live-Ansage; hängt ebenfalls an OQ-006. Register: RISK-008. |

---

### REQ-012 — Stimmungs-Check-in und Korrelation

| Feld | Wert |
|---|---|
| Trace ID | TRC-012 |
| Vision Item | VIS-003 — User Need: Nutzer benötigen verlässliches Tracking, verständliche statt abstrakte Health-Auswertung, konkrete  ⚠️ **Zitat des Altstands (Runde 6, 2026-07-20):** VIS-003 wird nach Nutzerauftrag Punkt 2 verengt; die Qualifizierer „verlässlich" und „sicher" sind in keiner der vier Quellen belegt und werden als ASSUMPTION-Rest getrennt geführt. **Der Wortlaut wird hier nicht nachgezogen**, weil er wörtlich aus dem Vision-Item stammt und dessen Fassung dem Vision-Owner obliegt. Diese Zeile stützt sich **nicht** auf einen der beiden Qualifizierer — anders als REQ-004, siehe §6.1.1. |
| Vision Item (ergänzend, aus dem Messmodell) | VIS-006, VIS-007 |
| Canvas Item (atomar) | CAN-125, CAN-052, CAN-029, CAN-102 |
| Acceptance Criterion | AC-012 — Zu REQ-012 — Then: Der Check-in dauert unter zwei Sekunden und Trends werden ohne Kausalitätsbehauptung angezeigt. |
| Measurement Type | **RESEARCH_HYPOTHESIS** |
| Signal / Control Evidence | Zwei getrennte Signale. (a) Datenerhebung: Quote der Stimmungs-Check-ins nach einer Aktivitaet (CAN-125) und die gemessene Check-in-Dauer am Geraet. (b) Forschung: Staerke, Stabilitaet und Unsicherheit der Korrelation zwischen Stimmungs-Check-in und Belastungs-/Trainingsmerkmalen ueber den erhobenen Korpus, ausgewertet getrennt fuer Run und Bike, weil Belastungsprofil und Aktivitaetsdauer je Sportart systematisch abweichen. |
| Target / Pass Condition | (a) VIS-006 Zeile A: Check-in-Quote > 50 % - ASSUMPTION, gesetztes Produktziel ohne empirische Grundlage. AC-012 setzt zwei explizite Schranken: der Check-in dauert unter zwei Sekunden (Geraetemessung) und Trends werden erst ab mindestens vier Wochen Daten gezeigt, ohne Kausalitaetsbehauptung. (b) Die Entscheidungsschwelle fuer die Anzeige einer Korrelation ist MISSING: kein Artefakt nennt Mindest-Effektstaerke, Mindestfallzahl oder Signifikanzkriterium. Ohne diese Schwelle darf keine Korrelation ausgespielt werden. |
| Measurement Window | Check-in-Quote und -Dauer je Aktivitaet, ausgewertet ueber eine rollierende 28-Tage-Kohorte. Korrelationsauswertung fruehestens ueber ein Vier-Wochen-Fenster je Nutzer (AC-012), danach rollierend; laengere Fenster sind nicht festgelegt (MISSING). |
| Evidence Needed | EV-012 — Zeitmessung, Fixture-Korrelation und Copy-Review. |
| Evidence Source | EV-012 (Zeitmessung, Fixture-Korrelation und Copy-Review); Mindestklasse real-boundary-smoke - die Zwei-Sekunden-Schranke ist eine Geraetemessung, keine Fixture-Aussage. Gleiche MESSLUECKE wie REQ-010: keine dokumentierte Telemetrie-Erhebung; Stimmungsdaten sind zudem eine besonders sensible Kategorie (REQ-034, CAN-088). |
| Source Type | ASSUMPTION |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Fuer die Claim-Formulierung der Trendanzeige zusaetzlich OQ-006 ('Product/Legal') offen. |
| Release Gate | GATE-A1 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | real-boundary-smoke — Die Zwei-Sekunden-Schranke aus AC-012 ist eine Gerätemessung, keine Fixture-Aussage. |
| Risiko | RISK-008 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-006 |
| Rationale | Der Check-in selbst ist eine einfache Funktion, die auszuwertende Korrelation zwischen Stimmung und Belastung ist dagegen eine unvalidierte Health-Korrelation - in der Aufgabenstellung ausdruecklich der RESEARCH_HYPOTHESIS zugeordnet. Die Check-in-Quote ist hier nicht das Erfolgsziel, sondern die Datenvoraussetzung der Untersuchung; sie wird trotzdem mit ihrem VIS-006-Wert und ASSUMPTION-Markierung mitgefuehrt, damit das Produktsignal nicht verlorengeht. |
| Befund | CAN-102 (Korrelation) und Stimmungsdaten als besonders sensible Kategorie; AC-012 verlangt Darstellung ohne Kausalitätsbehauptung. Register: RISK-008. |

**Forschungsplan (RESEARCH_HYPOTHESIS)**

| Feld | Inhalt |
|---|---|
| Hypothese | Zwischen dem Stimmungs-Check-in nach einer Aktivitaet und Belastungs-/Trainingsmerkmalen besteht ein Zusammenhang, der stabil genug ist, um ihn dem Nutzer als Trend zu zeigen - ohne Kausalitaetsbehauptung. |
| Plan | Stufe 1: Check-in-Erfassung ohne jede Trenddarstellung, Messung von Quote und Dauer. Stufe 2: Auswertung auf einem Korpus mit mindestens vier Wochen je Nutzer, getrennt nach Run und Bike, mit vorab festgelegtem Auswertungsverfahren und ausgewiesener Unsicherheit. Stufe 3: Copy-Review gegen die Claims-Whitelist (OQ-006), bevor irgendein Trend sichtbar wird. |
| Fixtures / reale Testdaten | Reale Check-in-Verlaeufe ueber mindestens vier Wochen je Nutzer plus die zugehoerigen Aktivitaets- und Belastungsdaten; Fixture-Korrelationen (EV-012) nur zur Verifikation der Auswertungslogik, nicht als Evidenz fuer den Zusammenhang selbst. |
| Entscheidungsschwelle | MISSING - kein Artefakt beziffert Mindestfallzahl, Mindest-Effektstaerke oder Unsicherheitsgrenze. Vom DRI gemeinsam mit OQ-006 vor Gate A1 zu entscheiden. |
| Konsequenz bei unzureichender Evidenz | Der Check-in bleibt als reine Erfassung ohne Trend- oder Korrelationsanzeige bestehen. Kein produktiver Rollout der Korrelationsdarstellung vor bestandenem Gate. |

---

### REQ-013 — Health-Home und Steigerungshinweis

| Feld | Wert |
|---|---|
| Trace ID | TRC-013 |
| Vision Item | VIS-007 — Health-first Boundary: Health-Ausgaben sind Orientierung, keine Diagnose. Score und Empfehlungen müssen Datenb |
| Vision Item (ergänzend, aus dem Messmodell) | VIS-006 |
| Canvas Item (atomar) | CAN-124, CAN-126, CAN-029, CAN-102, CAN-072 |
| Acceptance Criterion | AC-013 — Zu REQ-013 — Then: Aktivitäten, Belastung und Trend sind korrekt; Hinweise verwenden freigegebene Orientierungssprache. |
| Measurement Type | **PRODUCT_OUTCOME** |
| Signal / Control Evidence | Wiedernutzung und Nutzung der Health-Erklaerung am Health-Home: W4-Retention aktiver Tracker-Nutzer (CAN-124) und Oeffnungsrate der Erklaerung zum Wochenzustand (CAN-126). Als Gegenprobe der Anteil Wochen, in denen der Steigerungshinweis ausgeloest wurde, damit Uebersteuerung (Hinweis in fast jeder Woche) sichtbar wird. Run und Bike getrennt ausgewiesen, weil Wochenvolumen und Belastungsverlauf sportspezifisch sind. |
| Target / Pass Condition | VIS-006 Zeile A: W4-Retention > 30 % und Oeffnen der Score-Erklaerung > 25 %. ASSUMPTION - beide Werte sind gesetzte Produktziele ohne empirische Grundlage. AC-013 als begleitende Kontrolle: Aktivitaeten, Belastung und Trend sind korrekt und Hinweise verwenden freigegebene Orientierungssprache. Die Schwelle, ab der 'deutlich erhoehte Belastung' einen Hinweis ausloest, ist in keinem Artefakt beziffert: MISSING; sie ist zusaetzlich an OQ-006 gebunden, weil der Hinweistext eine Health-Aussage ist. |
| Measurement Window | W4-Retention: 28 Tage ab erster Aktivitaet, rollierende Kohorte. Hinweisausloesung und Wochenzustand: je Kalenderwoche, mit Vier-Wochen-Vergleichsfenster (AC-013). |
| Evidence Needed | EV-013 — Wochen-Fixtures und Claims-Lint. |
| Evidence Source | EV-013 (Wochen-Fixtures und Claims-Lint); Mindestklasse real-boundary-smoke - Home-Rendering und freigegebene Claim-Sprache muessen am Geraet sichtbar geprueft werden. Gleiche MESSLUECKE wie REQ-010: keine dokumentierte Telemetrie-Erhebung fuer Retention; Konflikt mit CAN-095 (local-first) und REQ-034. |
| Source Type | ASSUMPTION |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. OQ-006 (Claims-Whitelist, 'Product/Legal') ist ebenfalls offen und blockiert den Hinweistext. |
| Release Gate | GATE-A1 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | real-boundary-smoke — Home-Rendering und freigegebene Claim-Sprache müssen am Gerät sichtbar geprüft werden. |
| Risiko | RISK-008 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-006 |
| Rationale | REQ-013 ist der Ort, an dem sich der Kernnutzen des Trackers im Nutzerverhalten zeigen soll - Wiedernutzung und Nutzung der Erklaerung. Deshalb PRODUCT_OUTCOME. Die Zielwerte sind aus VIS-006 uebernommen und als ASSUMPTION markiert. Die unbezifferte Ausloeseschwelle wird ausdruecklich als MISSING gefuehrt statt sie zu erfinden; sie ist die schaerfste Claim-Flaeche des Produkts (docs/traceability.md, Befund REQ-013, unmittelbar an der Grenze CAN-072 'kein Medizinprodukt'). |
| Befund | Schärfste Claim-Fläche: aktiver Hinweis bei erhöhter Belastung, unmittelbar an der Non-Goal-Grenze CAN-072 („kein Medizinprodukt“). Hängt an OQ-006. Register: RISK-008. |

---

### ~~REQ-014~~ — Designsystem und Accessibility · **DEPRECATED 2026-07-19**

> **Nicht gelöscht, sondern als `deprecated` geführt.** REQ-014 war ein **Composite** aus zwei
> unabhängig prüfbaren Anforderungen mit verschiedenen Prüfverfahren, Nachweisen und Gates. Es
> wird ausdrücklich **nicht umgedeutet** — kein stilles Verengen auf eine der beiden Hälften.
> Ersetzt durch **REQ-037** (Accessibility) und **REQ-038** (Monochromes Designsystem), je mit
> eigener AC- und EV-ID. Folge: **AC-014, EV-014 und TRC-014 sind ebenfalls deprecated.**
> Registry §6.4, §7.4.1. **Neue Referenzen auf REQ-014 sind ein Validierungsfehler.**

| Feld | Wert |
|---|---|
| Status | **deprecated** · `deprecated_at` 2026-07-19 · `replacement_id` **REQ-037, REQ-038** |
| Trace ID | ~~TRC-014~~ → TRC-037, TRC-038 |
| Acceptance Criterion | ~~AC-014~~ → AC-037, AC-038 |
| Evidence | ~~EV-014~~ → EV-037, EV-038 |
| Warum zerlegt | Zugänglichkeit (WCAG, Screenreader, Dynamic Type) und Gestaltungssprache (tokenbasiert, monochrom, Farbe nur mit fachlicher Bedeutung) können **unabhängig voneinander bestehen oder fallen**. Sie haben verschiedene Prüfverfahren (Audit/Screenreader-Durchlauf gegen Token-Inventar), verschiedene Nachweise und verschiedene Belegquellen (NFR-005 gegen CAN-141). |
| Aufteilung der Klausel „Farbe ist nie der einzige Träger“ | Sie wirkt in **beiden** Nachfolgern mit **unterschiedlicher Prüfrichtung**: in AC-037 (d) als Zugänglichkeitsschranke („geht Information verloren?“), in AC-038 (a)/(b) als Gestaltungsregel („wo darf Farbe überhaupt stehen?“). Das ist keine Doppelung, sondern der Grund für die Zerlegung. |
| Aufteilung von EV-014 | „Token-Review“ → **EV-038** · „Accessibility- und Screenreader-Check“ → **EV-037**. Zwei Nachweisverfahren, die in einer ID vermischt waren. |
| Vision-Anker der Nachfolger | REQ-037 → **VIS-011** (ASSUMPTION, unbestätigt — `not-linked`) · REQ-038 → **VIS-012 reserved, Inhalt MISSING** (`broken`). Der frühere Anker **VIS-009 (Privacy Boundary)** war fachlich falsch und ist am 2026-07-19 entfernt worden (§0.1); er wird **nicht** auf einen der Nachfolger vererbt. |
| Canvas-Anker der Nachfolger | REQ-037 → **CAN-099** (`active`, ausschließlich Accessibility) · REQ-038 → **CAN-141** (`active`, Designsystem). Beide früheren Canvas-BLOCKER sind damit geschlossen; der bisherige Anker CAN-013 (Problem-Item) trägt die Anforderung nicht und wird nicht vererbt. |
| `true-line-status` / `wired-in-prod?` / `evidence-class` | **entfällt** — REQ-014 ist keine aktive Anforderung mehr und zählt in **keiner** Abdeckungszählung dieser Datei mit (§8). |
| Messfelder | **bewusst nicht fortgeschrieben.** Sie stehen vollständig bei REQ-037 und REQ-038. Ein Messmodell für eine deprecatete ID weiterzupflegen, würde die Composite-Anforderung faktisch am Leben erhalten. |

### REQ-015 — Verdiente Avatar-Progression

| Feld | Wert |
|---|---|
| Trace ID | TRC-015 |
| Vision Item | VIS-004 — Product Value: Die Plattform verbindet erklärbare Trainingsbelastung, verdiente Progression, lokale Teams und  |
| Canvas Item (atomar) | CAN-055, CAN-075, CAN-034 |
| Acceptance Criterion | AC-015 — Zu REQ-015 — Then: Das Item wird genau einmal freigeschaltet; ohne Leistung oder Kauf ist es nicht verfügbar. |
| Measurement Type | **COMPLIANCE_CONTROL** |
| Signal / Control Evidence | Kontrollierter Nachweis: Anzahl leistungsbezogener Items, Teamkleidungs- und Season-Objekte, die auf einem anderen Weg als ueber eine definierte, verifizierte reale Leistung erreichbar sind; Anzahl Kaufpfade im Item-Katalog; Anzahl Doppel-Unlocks unter Wiederholung und Nebenlaeufigkeit; Anteil Unlock-Kriterien mit dokumentiertem, verifizierbarem Leistungsnachweis. |
| Target / Pass Condition | AC-015 als Pass/Fail mit Nullschwelle: jedes Item wird genau einmal freigeschaltet; 0 Kaufpfade und 0 Umgehungspfade fuer leistungsbezogene Items. Deckt zugleich das Non-Goal CAN-075 (kein Verkauf von Leistungsstatus, Boosts oder Spielvorteilen) und die Store-IAP-Pruefung ab. Ein Progressions- oder Engagement-Zielwert wird nicht gesetzt: docs/traceability.md haelt fuer REQ-015 ausdruecklich fest, dass CAN-009 und VIS-006 kein Progressionssignal fuehren - ein solcher Wert waere erfunden. |
| Measurement Window | Vor Gate A2 und danach bei jeder Aenderung des Item-Katalogs oder der Unlock-Kriterien; Idempotenz-Fixtures bei jedem CI-Lauf. |
| Evidence Needed | EV-015 — Idempotenz- und Unlock-Fixtures. |
| Evidence Source | EV-015 (Idempotenz- und Unlock-Fixtures); Mindestklasse real-boundary-smoke - Idempotenz ist Domainlogik, die Nicht-Verfuegbarkeit ohne Leistung ist jedoch eine UI-Aussage (docs/traceability.md). |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. |
| Release Gate | GATE-A2 (PRD Release A2-B-C; erstmalige Abnahme mit GATE-A2, danach fortlaufend bis GATE-C) |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — Idempotenz ist Domainlogik, die Nicht-Verfügbarkeit ohne Leistung ist jedoch eine UI-Aussage. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002 · **Canvas-BLOCKER:** CAN-016 (Fortschritts- und Motivationsproblem) ist reserviert und inhaltlich MISSING - REQ-015 hat keinen atomaren Canvas-Problembezug; Fortschritt erscheint nur als Wertversprechen (CAN-030/CAN-034), nicht als Problem. |
| Rationale | Der harte, verletzbare Kern von REQ-015 ist eine Schranke ('nicht kaufbar', 'genau einmal'), kein Nutzerverhalten - deshalb COMPLIANCE_CONTROL mit Nullschwelle. Requirement-spezifische Nichtanwendbarkeit eines Nutzersignals: die Wirkung verdienter Progression auf Nutzerverhalten hat in Canvas und Vision keinerlei Signal; ein erfundenes Freischaltungs- oder Nutzungsziel wuerde genau den Anreiz erzeugen, den CAN-075 verbietet. Sportspezifische Trennung ist nicht anwendbar, weil Unlock-Idempotenz und Kaufpfad-Freiheit sportneutrale Eigenschaften des Katalogs sind; sportabhaengig sind allenfalls die Leistungskriterien selbst, die dann je Sportart als eigene Unlock-Definition gepruefte werden. |

---

### REQ-016 — Recaps, Erfolgskarten und Live-Status

| Feld | Wert |
|---|---|
| Trace ID | TRC-016 |
| Vision Item | VIS-004 — Product Value: Die Plattform verbindet erklärbare Trainingsbelastung, verdiente Progression, lokale Teams und  |
| Vision Item (ergänzend, aus dem Messmodell) | VIS-009 |
| Canvas Item (atomar) | CAN-054, CAN-105, CAN-030 |
| Acceptance Criterion | AC-016 — Zu REQ-016 — Then: Metriken sind korrekt, exportierbar und sensible Standortdaten sind reduziert. |
| Measurement Type | **COMPLIANCE_CONTROL** |
| Signal / Control Evidence | Kontrollierter Nachweis: Anzahl erzeugter Erfolgskarten, Recaps und Live-/Lockscreen-Status, in denen Start- oder Endpunkt rekonstruierbar bleibt; Uebereinstimmung der ausgewiesenen Metriken mit der gespeicherten Aktivitaet; Store-Konformitaet der Live-Aktivitaetsanzeige je Plattform. |
| Target / Pass Condition | AC-016 als Pass/Fail: Metriken stimmen mit der gespeicherten Aktivitaet ueberein und sensible Standortdaten sind reduziert - 0 rekonstruierbare Start-/Endpunkte im Privacy-Snapshot-Test. BEFUND: die Reduktionsregel selbst (Radius, Zeitversatz, Zuschnitt) ist in keinem Artefakt spezifiziert - MISSING; docs/traceability.md haelt fuer REQ-016 bereits fest, dass das REQ die Minderung nennt, aber die Reduktionsregel nicht spezifiziert. Ohne sie ist der Test nicht abschliessend definiert. Eine Teilen- oder Nutzungsquote wird nicht gesetzt; sie waere erfunden (kein CAN-009-/VIS-006-Signal fuer Recaps und Erfolgskarten). |
| Measurement Window | Vor Gate A2 und bei jeder Aenderung des Karten-, Widget- oder Erfolgskarten-Renderings; je Plattform. |
| Evidence Needed | EV-016 — Bildexport-, Widget- und Privacy-Snapshot-Test. |
| Evidence Source | EV-016 (Bildexport-, Widget- und Privacy-Snapshot-Test); Mindestklasse real-boundary-smoke - Widgets und Live-Aktivitaeten sind OS-Integrationen und nur am realen Geraet darstellbar. Einschlaegiges Risiko: CAN-105 / RISK-015 (Standortmissbrauch). |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Die fehlende Reduktionsregel braucht genau diesen DRI, ergaenzt um OQ-009 (Datenretention fuer GPS/Live). |
| Release Gate | GATE-A2 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | real-boundary-smoke — Widgets und Live-Aktivitäten sind OS-Integrationen und nur am realen Gerät darstellbar. |
| Risiko | RISK-015 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-009 · **Canvas-BLOCKER:** CAN-016 (Fortschritts- und Motivationsproblem) ist reserviert und inhaltlich MISSING - REQ-016 hat keinen atomaren Canvas-Problembezug. |
| Rationale | Die bindende, verletzbare Klausel des REQ steht im Requirement selbst ('ohne sensible Start-/Endpunkte offenzulegen') und ist ein Datenschutz-Kontrollnachweis - deshalb COMPLIANCE_CONTROL. Requirement-spezifische Nichtanwendbarkeit eines Nutzersignals: fuer Recaps, Erfolgskarten und Live-Status existiert in Canvas und Vision kein Erfolgssignal; eine Teilenquote als Ziel waere ein erfundener Engagement-KPI. source_type ist MISSING, weil die entscheidende Pruefgroesse - der zulaessige Grad der Standortreduktion - nirgends beziffert ist. |
| Befund | CAN-105 (Standortmissbrauch): teilbare Erfolgskarten und Lockscreen-Status exponieren Standortkontext; das REQ nennt die Minderung, aber die Reduktionsregel ist nicht spezifiziert. Register: RISK-015. |

---

### REQ-017 — Accounts, Auth und Datenmigration

| Feld | Wert |
|---|---|
| Trace ID | TRC-017 |
| Vision Item | VIS-005 — Project Goal: Zuerst einen belastbaren Health-Tracker etablieren; danach Accounts, Community, Teams und erst n |
| Vision Item (ergänzend, aus dem Messmodell) | VIS-009 |
| Canvas Item (atomar) | CAN-056, CAN-084, CAN-088, CAN-014 |
| Acceptance Criterion | AC-017 — Zu REQ-017 — Then: Daten migrieren/synchronisieren deterministisch; Löschung entfernt alle personenbezogenen Daten gemäß Retenti… |
| Measurement Type | **COMPLIANCE_CONTROL** |
| Signal / Control Evidence | Kontrollierter Nachweis: Anzahl personenbezogener Datensaetze, die nach einer vollstaendigen In-App-Accountloeschung verbleiben; Anteil verlustfrei migrierter lokaler Aktivitaeten; Determinismus des Offline-Sync (identischer Konfliktfall erzeugt identisches Ergebnis); Erfolgsrate von E-Mail-, Apple- und Google-Auth gegen die echten Identitaetsanbieter. |
| Target / Pass Condition | AC-017 als Pass/Fail: die Loeschung entfernt alle personenbezogenen Daten gemaess Retention-Regeln; 100 % der lokalen Aktivitaeten migrieren deterministisch, 0 Datenverlust. OFFENER WIDERSPRUCH: REQ-027 verlangt unveraenderliche Historie (Snapshots, Trophaeen, Vereinsheim, Zeitreise); welche Historiendaten eine vollstaendige Loeschung ueberleben duerfen, ist ungeklaert (docs/traceability.md, Befund REQ-027). Bis zur Entscheidung ist die Pass-Bedingung nicht vollstaendig pruefbar. Die Retentionsfristen selbst sind MISSING (OQ-009). |
| Measurement Window | Vor Gate B und danach bei jeder Aenderung von Auth, Sync oder Datenmodell; Loeschungsnachweis je Plattform und je Auth-Anbieter. |
| Evidence Needed | EV-017 — E2E-Flow, Offline-Test und Löschungsnachweis. |
| Evidence Source | EV-017 (E2E-Flow, Offline-Test und Loeschungsnachweis); Mindestklasse production-verified - Apple-/Google-Sign-in und der Loeschungsnachweis sind nur gegen echte IdP- und Backend-Endpunkte belegbar. Store-Relevanz: In-App-Accountloeschung ist Policy-Voraussetzung (REQ-036, CAN-083). |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Zusaetzlich offen: OQ-005 (Backend, 'Engineering') und OQ-009 (Datenretention, 'Privacy/Product') - ohne Retentionsfristen ist 'vollstaendig geloescht' nicht definierbar. |
| Release Gate | GATE-B |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | production-verified — Apple-/Google-Sign-in und der Löschungsnachweis sind nur gegen echte IdP- und Backend-Endpunkte belegbar. |
| Risiko | RISK-012, RISK-015 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-005, OQ-009 |
| Rationale | Accounts, Migration und Loeschung sind Datenschutz- und Store-Kontrollen mit Pass/Fail-Charakter; ein Anmelde- oder Konversionsziel waere ein erfundener Engagement-KPI (docs/traceability.md: kein Signal fuer Accounts/Migration). source_type MISSING, weil die entscheidende Groesse - was 'vollstaendig geloescht' konkret umfasst - durch fehlende Retentionsregeln und den offenen Widerspruch zu REQ-027 nicht bestimmt ist. Sportspezifische Trennung ist requirement-spezifisch nicht anwendbar: Auth, Sync und Loeschung wirken auf denselben Datenbestand unabhaengig von der Sportart; sportabhaengig sind nur die migrierten Inhalte, deren Vollstaendigkeit je Sportart stichprobenartig zu belegen ist. |
| Befund | Accounts und Sync lassen Standort- und Health-Daten erstmals das Gerät verlassen; verschärft CAN-105. Hängt an OQ-005 (Backend; fristgerecht „vor Stufe B“). Register: RISK-012, RISK-015. |

---

### REQ-018 — Privacy, Sichtbarkeit und Moderation

| Feld | Wert |
|---|---|
| Trace ID | TRC-018 |
| Vision Item | VIS-009 — Privacy Boundary: Profile sind standardmäßig privat; Live-Standort ist pro Aktivität Opt-in, zeitlich begrenzt |
| Canvas Item (atomar) | CAN-057, CAN-059, CAN-037, CAN-014 |
| Acceptance Criterion | AC-018 — Zu REQ-018 — Then: Nur erlaubte Daten sind sichtbar; Blockierung wirkt beidseitig sofort und Meldungen sind bearbeitbar. |
| Measurement Type | **COMPLIANCE_CONTROL** |
| Signal / Control Evidence | Kontrollierter Nachweis gegen die Sichtbarkeitsmatrix: Anteil Matrixzellen, fuer die ein automatisierter Test die tatsaechliche Sichtbarkeit belegt; Wirksamkeit des Blockierens (beidseitig, sofort) im Zwei-Account-Test; Anteil Meldungen, die bearbeitbar in der Moderationsqueue ankommen; Anzahl Profile, die entgegen dem Default oeffentlich sind. |
| Target / Pass Condition | AC-018 als Pass/Fail mit 100-%-Abdeckung der Sichtbarkeitsmatrix: nur erlaubte Daten sind sichtbar, Blockierung wirkt beidseitig sofort, jede Meldung ist bearbeitbar, Profile sind standardmaessig privat (0 Abweichungen vom Default). Ein Moderations-SLA ist MISSING (OQ-010) - ohne ihn bleibt 'bearbeitbar' zeitlich unbestimmt. |
| Measurement Window | Vor Gate B und danach bei jeder Aenderung der Sichtbarkeitsregeln, der RLS-Policies oder der Moderationsfluesse. |
| Evidence Needed | EV-018 — Sichtbarkeits-Matrix, Zwei-Account- und Moderationstest. |
| Evidence Source | EV-018 (Sichtbarkeits-Matrix, Zwei-Account- und Moderationstest); Mindestklasse production-verified - eine Sichtbarkeitsmatrix ist nur gegen echte Backend-Policies/RLS widerlegbar, ein Mock bestaetigt nur die eigene Annahme (docs/traceability.md). RISK-021 (Moderationsaufwand skaliert nicht) ist offen. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Dokumentierte Rollenreferenz zur gekoppelten Frage OQ-010 (Moderations-SLA und Betrieb, 'Operations'). |
| Release Gate | GATE-B |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | production-verified — Eine Sichtbarkeitsmatrix ist nur gegen echte Backend-Policies/RLS widerlegbar; ein Mock bestätigt nur die eigene Annahme. |
| Risiko | RISK-021 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-010 |
| Rationale | Privacy, Sichtbarkeit und Moderation sind klassische kontrollierte Nachweise mit 100-%-Abdeckungsanspruch. Requirement-spezifische Nichtanwendbarkeit eines Nutzersignals: eine Nutzungsquote von Privacy-Einstellungen wuerde die Wirksamkeit der Regeln weder belegen noch widerlegen - entscheidend ist, dass die Matrix haelt, auch wenn niemand sie bewusst nutzt. Sportspezifische Trennung ist nicht anwendbar: Sichtbarkeit und Blockierung gelten identisch fuer Run- und Bike-Inhalte, weil die Regeln am Nutzer und nicht an der Sportart haengen. |

---

### REQ-019 — Routenempfehlungen und Feed

| Feld | Wert |
|---|---|
| Trace ID | TRC-019 |
| Vision Item | **MISSING — BLOCKER.** Kein VIS-Item trägt die Aussage „Routenempfehlung" oder „Feed". **VIS-008 wurde am 2026-07-20 entfernt, VIS-003 am selben Tag in Runde 5 ebenfalls** — beide Anker sind fort, keiner ist ersetzt. |
| Vision-Anker — Prüfung Runde 4 (2026-07-20), unverändert gültig | **VIS-008 entfernt.** VIS-008 ist die *Fairness Boundary* („Run und Bike besitzen getrennte Metriken, Ziele und interne Wertungen; sportübergreifender Effort nur mit simulierten und versionierten Faktoren") und trägt **ausschließlich** eine Aussage über sportgetrennte Wertung — **keine** Community-, Feed- oder Empfehlungsaussage. Der Anker war syntaktisch gültig, las sich plausibel und trug die falsche Bedeutung: dieselbe Defektklasse wie VIS-009 ↔ REQ-014. |
| Vision-Anker — durchgeführte Quellenprüfung (2026-07-20, Runde 5) | **VIS-003 entfernt.** Die Vorfassung hängte REQ-019 über die Kette „VIS-003 nennt *sicheren Zugang zu lokalen Trainingspartnern* → ein Feed ist die *Entdeckungsfläche* für diesen Zugang → also trägt VIS-003" an. **Das ist eine Ableitung über ein Zwischenglied und damit kein Beleg** — formal dieselbe verbotene Kette wie „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" (Registry §6.1.1). Das Wort „Entdeckungsfläche" steht in **keiner** Quelle; es war die Brücke selbst. **Prüfung der Vision-Ebene beider Quellen, vollständig:** SRC-001 **Teil 1 — VISION** besteht aus §1.1 Vision Statement, §1.2 Mission, §1.3 Fünf-Jahres-Bild, §1.4 Werte & Leitplanken; SRC-003 §1 Produktidentität aus §1.1 Was REVYR ist, §1.2 USPs (acht), §1.3 Zielgruppen. **Keine dieser Stellen nennt eine Routenempfehlung oder einen Feed.** Nächstliegende Kandidaten, einzeln geprüft und **verworfen**: SRC-001 §1.1 „dich mit den **Sportlern** deiner Umgebung verbindet" und §1.3 „über die sich lokale Ausdauersportler **finden**, messen und treffen" — beide handeln vom Finden **von Personen**, nicht von Strecken; SRC-003 §1.1 Priorität 3 „Social & Live — Verbinden, **Folgen**, Live-Map …" — der Follow-Graph, nicht der Empfehlungs-Feed; SRC-003 §1.3 „Runner/Jogger: … **Strecken entdecken** …" — der **stärkste** Kandidat und trotzdem kein Beleg: er benennt ein Bedürfnis der Zielgruppe, **nicht**, dass Strecken von anderen Nutzern empfohlen werden oder dass ein Feed existiert; dieselbe Formulierung wäre durch REQ-006 (Routenplanung) oder die Neue-Strecke-Erkennung erfüllt. **Wo der Inhalt tatsächlich steht — und warum das nicht hilft:** SRC-001 §2.5 *Social Loop* beschreibt REQ-019 nahezu wörtlich („Aktivität → neue Strecke erkannt → **Empfehlung** … posten → **Follower übernehmen die Route mit einem Tipp** …"), SRC-003 §4.2 *Routen & Empfehlungen* spezifiziert ihn vollständig. **Beide liegen auf Canvas- bzw. Systemspezifikations-Ebene, nicht auf Vision-Ebene** — SRC-001 §2 ist ausdrücklich mit „TEIL 2 — PRODUCT CANVAS" überschrieben. Der Canvas-Anker **CAN-058** ist damit belegt und bleibt; ein Vision-Anker entsteht daraus **nicht**. **Ergebnis: kein VIS-Item trägt REQ-019. Kein Item umgedeutet, keine VIS-ID erfunden;** für Routenempfehlung/Feed ist **keine VIS-ID reserviert**. ID-Bedarf an den Registry-Owner gemeldet. Zeilenstatus **`broken`**, nicht mehr `linked-partial` — eine getragene Hälfte gibt es nicht, wenn die tragende Lesart eine Brücke war. |
| Vision Item (ergänzend, aus dem Messmodell) | VIS-006 (Success Signal — trägt den **Zielwert**, nicht die Anforderung) |
| Canvas Item (atomar) | **CAN-058** (Capability „Routenempfehlungen" — **primärer Anker seit 2026-07-20**), CAN-105 (Risiko), CAN-032 (Wertversprechen), **CAN-130** (Erfolgssignal, `active` seit 2026-07-19). *Rollenkorrektur: bis zum 2026-07-20 stand mit CAN-130 ein **Erfolgssignal** in der Spalte „Canvas Item (primär, atomar)". Ein Erfolgssignal misst, ob eine Capability wirkt — es ist nicht die Capability. Dieselbe Korrektur bei REQ-020 (CAN-127) und REQ-022 (CAN-128).* |
| Acceptance Criterion | **AC-019 (funktional)** — Ein berechtigter Nutzer kann eine sichtbare Routenempfehlung übernehmen; die übernommene Route wird in seiner Planung verfügbar, **ohne dass private Daten des Empfehlenden offengelegt werden**. · **AC-041 (Messkriterium)** — Für Gate B kann die Zahl bestätigter Übernahmen je auswertbarer Empfehlung **datenschutzkonform, sportartspezifisch und reproduzierbar** berechnet werden. |
| Warum zwei AC-IDs und nicht zwei Felder einer AC | Die Nutzerentscheidung stellt ausdrücklich fest, dass das **funktionale** Kriterium bestanden sein kann, während die Produktkennzahl noch keine ausreichende Stichprobe hat — **die Zustände sind unabhängig**. Zwei Felder einer ID verstießen gegen Registry-Regel 5 (eine ID, eine Bedeutung) und wiederholten strukturell den in §3.1 behobenen Defekt „ein Feld, zwei unabhängige Fragen“. Zudem hätten sie den **Funktionsnachweis an OQ-012 gekettet** — eine Blockade, die die Entscheidung ausdrücklich nicht will. Kanonische Begründung: Registry §6.5.1. |
| Measurement Type | **PRODUCT_OUTCOME** |
| Signal / Control Evidence | **Kennzahl (CAN-130):** bestätigte Routenübernahmen ÷ **auswertbare** Routenempfehlungen. **Getrennt ausgewiesen als `run_route_adoptions_per_recommendation` und `bike_route_adoptions_per_recommendation`** — eine Laufroute und eine Radroute haben unterschiedliche Wegenetze und Reichweiten und dürfen nicht gegeneinander verrechnet werden. Ein Gesamtwert darf gezeigt werden, **nie anstelle** der getrennten Sportwerte. Mehrere Nutzer dürfen dieselbe Empfehlung übernehmen — der Durchschnitt kann deshalb > 1,0 liegen. |
| Target / Pass Condition | **> 1,0 bestätigte Routenübernahmen je auswertbarer Empfehlung**, Run und Bike getrennt. Wortlaut: *„Eine veröffentlichte und für mindestens einen berechtigten Empfänger sichtbare Routenempfehlung führt im Durchschnitt zu mehr als einer tatsächlichen Routenübernahme.“* `target_source_type` **EXPLICIT** (CAN-130, Nutzerentscheidung 2026-07-19) · `evidence_status` **planned** · `empirical_result` **MISSING**. Begleitende funktionale Kontrolle aus **AC-019**; die **Berechenbarkeit** der Kennzahl ist **AC-041**. |
| „Auswertbar“ — alle vier Bedingungen müssen erfüllt sein | erfolgreich veröffentlicht · mindestens ein berechtigter Empfänger · im Messfenster sichtbar sein konnte · **nicht** vor möglicher Ausspielung gelöscht, blockiert oder moderativ verborgen. |
| Nicht in den Nenner | private Empfehlungen ohne berechtigten Empfänger · technisch nicht ausgelieferte Empfehlungen · vor Ausspielung gelöschte Empfehlungen · durch Blockierung oder Moderation vollständig unsichtbare Empfehlungen · Test- und Seed-Daten. |
| Sachkorrektur 2026-07-19 | Die Vorfassung dieses Blocks führte datenschutzbedingt unsichtbare Empfehlungen als **„Gegenprobe“**. Das war falsch: eine Gegenprobe wirkt **im Nenner** und hätte genau den Fehler erzeugt, den sie verhindern sollte. Sie sind **separat auszuweisen und ausdrücklich nicht in den Nenner zu nehmen** — sonst wird fehlender Zugang fälschlich als mangelndes Nutzerinteresse gelesen. Die Absicht der alten Formulierung war richtig, ihre Umsetzung nicht. |
| Guardrail-Signale (begleitend, nicht Teil der Kennzahl) | Anzahl auswertbarer Empfehlungen · Empfehlungen ohne berechtigten Empfänger · technisch fehlgeschlagene Ausspielungen · mediane Zahl berechtigter Empfänger je Empfehlung · Anteil Empfehlungen mit mindestens einer Übernahme · Übernahmen je 100 berechtigten Ausspielungen (sofern datenschutzkonform messbar) · Run/Bike-Verteilung · Lösch-, Blockierungs- und Moderationsanteil. |
| Measurement Window | **Rollierende 28 Tage** (CAN-130). **Ersetzt** die frühere Angabe „rollierend je Kalenderwoche“, die aus keinem Artefakt stammte und deshalb als ASSUMPTION geführt werden musste. Das Fenster ist damit **belegt**, nicht mehr angenommen. |
| Telemetrie — zulässige Ereignisse | `route_recommendation_published` · `route_recommendation_eligible` · `route_recommendation_exposed` · `route_adopted` · `route_recommendation_deleted` · `route_recommendation_hidden` |
| Telemetrie — zulässige Felder | pseudonyme `recommendation_id` · pseudonyme `adoption_id` · `sport` (`run`\|`ride`) · Sichtbarkeitskategorie · grober Zeitstempel/Zeitbucket · Ergebnisstatus · Event-Version |
| Telemetrie — **nicht** zulässig | GPS-Koordinaten · Routengeometrie · Start-/Zieladresse · Health-Daten · Klarnamen · E-Mail · vollständige Gerätekennungen · öffentliche Analytics-Profile · Werbe-/Cross-Service-Tracking. **Kein paralleler Standort- oder Verhaltenstracker;** die Kennzahl ist möglichst aus ohnehin nötigen Backend-Ereignissen zu aggregieren. |
| Local-first-Abgrenzung | Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal (CAN-095). Erst **ab Gate B** dürfen für die **ausdrücklich aktivierte** Social-/Empfehlungsfunktion minimierte Metadaten verarbeitet werden. **Rohroute und GPS-Geometrie werden NIE für die Erfolgsmessung verwendet.** Gemessen wird das Ereignis „Empfehlung übernommen“, **nicht** die später gelaufene oder gefahrene Strecke. |
| Evidence Needed | **EV-019** — Zwei-Account-E2E-Flow (funktionaler Nachweis zu AC-019). · **EV-041** — reproduzierbare, datenschutzkonforme Berechnung der Kennzahl, getrennt für Run und Bike, über ein rollierendes 28-Tage-Fenster (zu AC-041). |
| Evidence Source | EV-019, Mindestklasse `real-boundary-smoke` — Netzwerk, Kartenanzeige und Zwei-Account-Flow gegen echte Endpunkte. · EV-041, `evidence_status` **planned**: Metrik, Berechnung und Gate sind definiert, die **Instrumentierung fehlt**. **Die beiden Nachweise sind getrennt und haben unabhängige Zustände.** EV-041 belegt die **Berechenbarkeit**, nicht die Zielerreichung. |
| Source Type | **ASSUMPTION** für die Anforderung selbst · **EXPLICIT** für den Zielwert der Kennzahl (CAN-130). Getrennt geführt, weil Anforderung und Zielwert hier unterschiedlich belegt sind. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. **Zusätzlich MISSING:** der Owner der Telemetrie-Instrumentierung (OQ-012). |
| Release Gate | GATE-B |
| Status | **broken** *(geändert 2026-07-20 Runde 5: VIS-003 war eine Ableitung über ein Zwischenglied und ist entfernt; die Vorfassung führte `linked-partial`)* · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | real-boundary-smoke — Netzwerk und Kartenanzeige; Zwei-Account-Flow (EV-019) gegen echte Endpunkte. |
| Risiko | RISK-015, RISK-021 |
| Offene Entscheidung | offene Fragen: OQ-002 · **Canvas-BLOCKER geschlossen (2026-07-19):** ~~CAN-130 ist reserviert und inhaltlich MISSING~~ → CAN-130 ist `active` und vollständig spezifiziert (Registry §6.3.2); das Messziel hängt **nicht mehr allein an der Vision**. **Geschlossen ist die Definition, nicht der Nachweis.** · **BLOCKER OQ-012 (Telemetrie):** offen sind — ob `exposed` client- oder serverseitig erhoben wird · nötige Event-Metadaten · speicherbare Daten · Aufbewahrung der Rohereignisse · ab wann nur Aggregate · ob eine separate Einwilligung nötig ist · Wirkung von Profil-Privacy, Blockierungen und Löschungen · Entfernung oder Anonymisierung gelöschter Accounts aus den Messdaten · Owner der Instrumentierung · verwendete Analytics-/Event-Lösung. **Blockierend für den externen Gate-B-Erfolgsnachweis und für jede Behauptung, CAN-130 sei empirisch validiert. NICHT blockierend für A0/A1 und NICHT für die Dokumentkorrektur.** · **MISSING OQ-014 (Stichprobenregel):** Mindestzahl auswertbarer Empfehlungen · Mindestzahl berechtigter Empfänger · Mindestdauer des Messfensters · Behandlung von Testkonten · Umgang mit Mehrfachübernahmen desselben Nutzers · Umgang mit gelöschten und moderierten Empfehlungen · getrennte Run-/Bike-Auswertung. **Es wird keine Mindestzahl geraten.** |
| Rationale | Routenübernahme ist das einzige Signal, das den Wert einer Empfehlung direkt misst. Der Zielwert ist seit dem 2026-07-19 **präzise definiert** (CAN-130), aber **nicht validiert** — Definition und Nachweis sind zwei verschiedene Dinge und werden getrennt geführt. Nebenbefund: der Feed nähert sich der Vision-Grenze „kein allgemeines soziales Netzwerk“; das REQ definiert keine Obergrenze der Feed-Inhaltstypen (OPEN QUESTION), was bei steigender Übernahmequote relevant wird. |
| Befund | CAN-105 durch geteilte Routen (Heimadressen). Sekundär: Feed-Inhaltstypen ohne Obergrenze (OPEN QUESTION). Register: RISK-015, RISK-021. **Querschnittsbefund Telemetrie ist für REQ-019 teilweise adressiert** (CAN-130 spezifiziert die Erhebung inhaltlich) und bleibt für REQ-010, REQ-012, REQ-013, REQ-020 und REQ-022 **unverändert offen** — er wird **nicht** stillschweigend aus CAN-130 mitgelöst (§6.3). |

---

### REQ-020 — Teamgründung und Beitritt

| Feld | Wert |
|---|---|
| Trace ID | TRC-020 |
| Vision Item | **VIS-004 — Product Value**, tragende Klausel wörtlich: „Die Plattform verbindet erklärbare Trainingsbelastung, verdiente Progression, **lokale Teams** und reale ortsbezogene Spielmechaniken …". Teamgründung und Beitritt sind die **konstituierende Handlung** von „lokale Teams" — der Bezug ist wörtlich, nicht interpretiert. |
| Vision-Anker — durchgeführte Prüfung (2026-07-20) | **VIS-008 entfernt.** Die Fairness Boundary trägt eine Aussage über **sportgetrennte Wertung**, keine über Teams. Sie hätte bei einer maschinellen Prüfung als erfüllter Vision-Anker gezählt, obwohl sie nichts über Teamgründung sagt. |
| Vision Item (ergänzend, aus dem Messmodell) | VIS-006 (Success Signal — Zielwert „Team nach 60 Tagen > 25 %") |
| Canvas Item (atomar) | **CAN-060** (Capability „Lokale Teams" — **primärer Anker seit 2026-07-20**), CAN-032 (Wertversprechen), CAN-015 (Problem), **CAN-127** (Erfolgssignal). *Rollenkorrektur wie bei REQ-019: CAN-127 ist das Erfolgssignal, nicht die Capability.* |
| Acceptance Criterion | AC-020 — Zu REQ-020 — Then: Es existiert nie ein Team ohne Admin und ungültige Tokens gewähren keinen Zugang. |
| Measurement Type | **PRODUCT_OUTCOME** |
| Signal / Control Evidence | Teambeitritt: Anteil Nutzer, die 60 Tage nach Registrierung Mitglied mindestens eines Teams sind (CAN-127). Als harte Gegenkontrolle daneben: Anzahl Teams ohne Admin und Anzahl abgelaufener oder deaktivierter Tokens, ueber die dennoch ein Beitritt gelingt. |
| Target / Pass Condition | VIS-006 Zeile C: Nutzer in einem Team nach 60 Tagen > 25 %. ASSUMPTION - gesetztes Produktziel ohne empirische Grundlage. Daneben AC-020 als Pass/Fail mit Nullschwelle: 0 Teams ohne Admin zu irgendeinem Zeitpunkt (transaktionale Gruendung) und 0 erfolgreiche Beitritte ueber ungueltige Tokens. Die Gueltigkeitsdauer von Beitrittslinks und QR-Codes ist in keinem Artefakt beziffert: MISSING. |
| Measurement Window | 60 Tage ab Registrierung, rollierende Kohorte (Fenster woertlich aus VIS-006 Zeile C und CAN-127). Transaktions- und Token-Kontrollen bei jedem CI-Lauf und im Zwei-Geraete-Test vor Gate C. |
| Evidence Needed | EV-020 — Datenbanktransaktions- und Zwei-Geräte-Test. |
| Evidence Source | EV-020 (Datenbanktransaktions- und Zwei-Geraete-Test); Mindestklasse real-boundary-smoke - Deep-Link und QR nutzen Kamera und OS-Link-Handling, die Transaktion laeuft gegen die echte Datenbank. |
| Source Type | ASSUMPTION |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. |
| Release Gate | GATE-C |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — Deep-Link/QR nutzen Kamera und OS-Link-Handling; Transaktion gegen echte DB. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002 |
| Rationale | Teambeitritt ist in der Aufgabenstellung ausdruecklich als PRODUCT_OUTCOME genannt und in CAN-127/VIS-006 mit Fenster und Zielwert hinterlegt. Der Zielwert bleibt unvalidiert (ASSUMPTION). Die transaktionale Admin-Garantie wird als Nullschwellen-Kontrolle mitgefuehrt, weil sie ein harter Integritaetsfall ist und nicht in einer Beitrittsquote aufgehen darf. Sportspezifische Trennung ist requirement-spezifisch nicht anwendbar: Teams sind laut PRD keine sportgetrennte Einheit - getrennt sind Rankings, Challenges und Rekorde (REQ-023, REQ-025), nicht die Mitgliedschaft selbst. |

---

### REQ-021 — Aktive Mitglieder und Teamwachstum

| Feld | Wert |
|---|---|
| Trace ID | TRC-021 |
| Vision Item | **VIS-004 — Product Value**, tragende Klausel: „**lokale Teams**" — **trägt nur die Team-Hälfte** (siehe nächste Zeile). |
| Vision-Anker — durchgeführte Prüfung (2026-07-20) | **VIS-008 entfernt** (Fairness Boundary trägt keine Team-Aussage). Gleicher Anker wie TRC-020, aber **eigene Zeile**, weil Gründung (REQ-020) und Wachstum (REQ-021) unabhängig prüfbar sind und unabhängig scheitern können. |
| Statuskorrektur Runde 5 (2026-07-20) — **`linked` → `linked-partial`** | Die Zeile stand auf `linked`, obwohl ihre **eigene** Begründung eine Teildeckung ausweist: VIS-004 nennt „lokale Teams" — die **Existenz** des Teams. REQ-021 fordert **aktive Mitglieder und Wachstum**. Die Vorfassung überbrückte das mit „sind der **Fortbestand** derselben Aussage: ein Team ohne aktive Mitglieder ist kein lokales Team" — **das ist eine Ableitung über ein Zwischenglied**, dieselbe Form, die bei REQ-019 zur Entfernung des Ankers geführt hat. **Unterschied zu REQ-019, der den Anker hier hält:** „lokale Teams" trägt die Team-Hälfte von REQ-021 **wörtlich**, während VIS-003 bei REQ-019 gar keine Hälfte wörtlich trug. Getragen ist die **Team-Hälfte**, nicht getragen die **Wachstums-/Aktivitäts-Hälfte**. Quellenlage geprüft: SRC-003 §1.2 USP „**Team-Wachstums-Loop** — Teamgröße = Spielbrett-Größe; Wachstum ist Spielmechanik" belegt das Wachstum, liegt aber auf **USP-/Canvas-Ebene**, nicht auf Vision-Ebene; SRC-001 Teil 1 nennt Wachstum nicht. **Es wird deshalb keine zweite Verknüpfung gesetzt.** Regel wie bei REQ-042: eine halb tragende Verknüpfung ist `linked-partial`, nie `linked`. |
| Canvas Item (atomar) | CAN-060 (Capability, primär), CAN-128 (Erfolgssignal), CAN-033 (Wertversprechen) |
| Acceptance Criterion | AC-021 — Zu REQ-021 — Then: Nur Mitglieder mit Aktivität im definierten Zeitfenster zählen; Bonus folgt erst nach nachgewiesener Integrat… |
| Measurement Type | **RESEARCH_HYPOTHESIS** |
| Signal / Control Evidence | Aus Simulation und spaeterer Feldmessung: Anteil gezaehlter Mitglieder mit Aktivitaet im definierten Zeitfenster, Verhaeltnis von Einladungen zu real integrierten Mitgliedern, Verteilung des Mentorbonus ueber Teamgroessen, Anteil Teams, deren Stufenaufstieg allein durch Einladungsvolumen erklaerbar waere. Run und Bike werden in der Aktivitaetszaehlung getrennt gefuehrt, damit ein Team nicht durch eine einzige Sportart die Aktivitaetsschwelle erfuellt und die andere verdeckt. |
| Target / Pass Condition | Entscheidungsschwelle MISSING: kein Artefakt beziffert Kapazitaetsgrenzen, Stufenkurve, das 'definierte Zeitfenster' der Aktivitaet oder die Hoehe des Mentorbonus. AC-021 gibt nur die qualitative Bedingung vor - nur Mitglieder mit Aktivitaet im definierten Zeitfenster zaehlen, der Bonus folgt erst nach nachgewiesener Integration. Ohne beziffertes Aktivitaetsfenster ist die Regel nicht pruefbar. Es wird hier kein Wert geraten. |
| Measurement Window | Simulationslaeufe vor Gate C ueber synthetische und reale Teamverlaeufe; im Feld je Kalenderwoche und je 60-Tage-Kohorte, sobald Teams existieren. Das eigentliche Aktivitaetsfenster ist MISSING und muss vor der Messung entschieden werden. |
| Evidence Needed | EV-021 — Zeitfenster- und Integrations-Fixtures. |
| Evidence Source | EV-021 (Zeitfenster- und Integrations-Fixtures); Mindestklasse integration-fake - die Zeitfenster- und Kapazitaetsregel ist reine Logik ohne eigene Grenze (docs/traceability.md). Fuer die Kalibrierung sind reale Teamverlaeufe erforderlich, keine rein synthetischen. |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Die fehlenden Mechanikparameter brauchen einen produktseitigen Entscheider, der nicht benannt ist. |
| Release Gate | GATE-C |
| Status | **linked-partial** *(geändert 2026-07-20 Runde 5: VIS-004 trägt nur die Team-Hälfte; die Vorfassung führte `linked`)* · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | value-risk |
| evidence-class-required | integration-fake — Zeitfenster- und Kapazitätsregel ist reine Logik ohne eigene Grenze; die UI-Fläche fällt unter **REQ-037 und REQ-038** (Nachfolger des deprecateten REQ-014) sowie REQ-025. *Verweis am 2026-07-19 nachgezogen: die Vorfassung nannte hier das deprecatete REQ-014.* |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002 |
| Rationale | Kapazitaet, Stufen und Mentorbonus sind unvalidierte Anreizparameter - genau der Fall, den die Aufgabenstellung unter Quoren und Verfallsmodellen der RESEARCH_HYPOTHESIS zuordnet. Ohne Simulation kann die Mechanik das belohnen, was das REQ ausdruecklich verhindern soll (blosse Einladungen). docs/traceability.md fuehrt REQ-021 zusaetzlich als value-risk: reine Spielmechanik ohne Health-Beitrag, in Spannung zu CAN-033. |
| Befund | Teamkapazität, Stufen und Mentorbonus sind reine Spielmechanik ohne Health-Beitrag; steht in Spannung zu CAN-033 („Spielmechaniken verdrängen die Health-Grundlage nicht“). Der Wertbezug zu CAN-032 ist nur mittelbar. |

**Forschungsplan (RESEARCH_HYPOTHESIS)**

| Feld | Inhalt |
|---|---|
| Hypothese | Kapazitaetsgrenzen, Teamstufen und Mentorbonus belohnen aktive, real integrierte Mitglieder staerker als blosses Einladungsvolumen - ohne die Health-Grundlage zu verdraengen (CAN-033). |
| Plan | Stufe 1: Parametersatz (Kapazitaet, Stufenkurve, Aktivitaetsfenster, Bonushoehe) festlegen lassen - heute MISSING. Stufe 2: Szenariosimulation ueber Teamverlaeufe mit unterschiedlichen Einladungs-/Aktivitaetsmischungen; Kennzahl ist der Anteil des Stufenaufstiegs, der allein durch Einladungen erklaerbar ist. Stufe 3: Feldvalidierung ueber mindestens eine 60-Tage-Kohorte nach Gate C. |
| Fixtures / reale Testdaten | Reale Aktivitaets- und Mitgliedschaftsverlaeufe echter Teams fuer die Kalibrierung; Zeitfenster- und Integrations-Fixtures (EV-021) nur zur Verifikation der Zaehllogik. |
| Entscheidungsschwelle | MISSING - weder ein zulaessiger Anteil einladungsgetriebener Aufstiege noch ein Aktivitaetsfenster ist beziffert. Vom DRI vor Gate C zu entscheiden. |
| Konsequenz bei unzureichender Evidenz | Kapazitaetsstufen und Mentorbonus bleiben deaktiviert; Teams funktionieren ohne Wachstumsmechanik. Kein produktiver Rollout vor bestandenem Gate. |

---

### REQ-022 — Gemeinsame Aktivitäten und Events

| Feld | Wert |
|---|---|
| Trace ID | TRC-022 |
| Vision Item | **VIS-003 — User Need**, tragende Klausel: „sicherer Zugang zu **lokalen Trainingspartnern**" — **trägt nur die Aktivitäts-Hälfte** (siehe Statuskorrektur unten). ⚠️ **Befund Runde 6 (2026-07-20), Status unverändert:** die hier zitierte Klausel enthält mit „**sicher**" und „**Trainingspartner**" zwei Bestandteile, die in **keiner** der vier Quellen vorkommen (Volltextsuche über `docs/sources/`: „Trainingspartner" **0 Treffer**, „Zugang" **0 Treffer**; jedes Vorkommen von „sicher"/„Sicherheit" betrifft Standortfreigabe, UGC-Moderation, Notfall-Assistenz, Auth oder farbenblind-sichere Paletten — **nie** den Zugang zu Personen). Belegt ist der Anschluss an lokale Sportler wortnah: `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md:51` „trainieren heute allein und **wünschen sich Anschluss**" und `:22` „**Echte Gemeinschaft** — Teams, die zusammen trainieren, sich real treffen …". **Der Zeilenstatus `linked-partial` bleibt deshalb unverändert:** die getragene Hälfte überlebt die Verengung von VIS-003, nur ihr Zitatwortlaut nicht. ⚠️ **Die Gegenprüfung ist hier uneins** — eine Linse hält TRC-022 für gefährdet, falls der verengte VIS-003-Kern das gemeinsame Training nicht ausdrücklich nennt, weil die Matrix bei VIS-004 genau diese Rahmen-gegen-Handlung-Unterscheidung schon einmal verworfen hat (siehe nächste Zeile). **Der Fall wird deshalb nicht entschieden, sondern der Nutzerentscheidung über den VIS-003-Wortlaut vorgelegt.** |
| Vision-Anker — jede Verknüpfung einzeln geprüft (2026-07-20) | **VIS-008 entfernt** (Fairness Boundary trägt keine Community-Aussage). **VIS-004 geprüft und VERWORFEN** — obwohl es bei REQ-020 und REQ-021 trägt: VIS-004 nennt „**lokale Teams**" (der organisatorische **Rahmen**) und „reale ortsbezogene **Spielmechaniken**" (Territory/Spiel). Keine dieser beiden Klauseln sagt etwas über **gemeinsame Aktivitäten oder Events** aus. Ein Team ist der Rahmen, in dem gemeinsam trainiert werden *kann*; dass gemeinsam trainiert *wird*, steht dort nicht. Eine Verknüpfung wäre die plausible Lesart ohne tragende Aussage. **Die Nutzerentscheidung erlaubt „VIS-003 und/oder VIS-004" ausdrücklich nur bei fachlicher Einzelbegründung — hier trägt genau eines von beiden.** |
| Vision Item (ergänzend, aus dem Messmodell) | VIS-006 (Success Signal — Zielwert „gemeinsame Aktivität pro Woche > 40 %") |
| Canvas Item (atomar) | **CAN-067** (Capability „Lokale Events" — **primärer Anker seit 2026-07-20**), CAN-015 (Problem), CAN-105 (Risiko), **CAN-128** (Erfolgssignal). *Rollenkorrektur wie bei REQ-019/REQ-020.* |
| Acceptance Criterion | AC-022 — Zu REQ-022 — Then: Echte gemeinsame Aktivität wird erkannt, nicht gemeinsame wird abgelehnt und Eventinhalte sind moderierbar. |
| Measurement Type | **PRODUCT_OUTCOME** |
| Signal / Control Evidence | Gemeinsame Aktivitaet: Anteil Teams mit mindestens einer erkannten realen gemeinsamen Aktivitaet pro Kalenderwoche (CAN-128). Als Gegenprobe die Falsch-Positiv-Rate der Erkennung im Zwei-Geraete-Test (zufaellige raeumliche und zeitliche Naehe ohne gemeinsame Aktivitaet) sowie die Nichterkennungsrate bei tatsaechlich gemeinsamer Aktivitaet. Run und Bike getrennt, weil Gruppendynamik, Abstaende und Geschwindigkeitsprofile - und damit die Ueberschneidungskriterien - sportspezifisch sind. |
| Target / Pass Condition | VIS-006 Zeile C: Teams mit realer gemeinsamer Aktivitaet pro Woche > 40 %. ASSUMPTION - gesetztes Produktziel ohne empirische Grundlage. AC-022 als begleitende Kontrolle: echte gemeinsame Aktivitaet wird erkannt, nicht gemeinsame wird abgelehnt, Eventinhalte sind moderierbar. Zeit- und Distanzschwellen der Ueberschneidung sowie die zulaessige Falsch-Positiv-Rate sind in keinem Artefakt beziffert: MISSING. |
| Measurement Window | Je Kalenderwoche (Fenster woertlich aus VIS-006 Zeile C und CAN-128); Erkennungsguete zusaetzlich je Zwei-Geraete-Testlauf vor Gate C. |
| Evidence Needed | EV-022 — Pure-Function-Fixtures und Zwei-Geräte-Eventtest. |
| Evidence Source | EV-022 (Pure-Function-Fixtures und Zwei-Geraete-Eventtest); Mindestklasse production-verified - die Zeit-/Raumkorrelation zweier realer Aktivitaeten ist eine Feldbedingung (docs/traceability.md). |
| Source Type | ASSUMPTION |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. |
| Release Gate | GATE-C (PRD Release C-D) |
| Status | **linked-partial** *(geändert 2026-07-20 Runde 5: VIS-003 trägt nur die Aktivitäts-Hälfte; die Vorfassung führte `linked`)* · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| Statuskorrektur Runde 5 (2026-07-20) — **`linked` → `linked-partial`** | Die Zeile stand auf `linked`, obwohl ihre eigene Begründung eine Teildeckung ausweist. REQ-022 heißt „Gemeinsame Aktivitäten **und Events**" — zwei Gegenstände. VIS-003 nennt „sicheren Zugang zu **lokalen Trainingspartnern**": das trägt die **gemeinsame Aktivität** (die Handlung, die den Zugang einlöst), sagt aber **nichts über organisierte lokale Events**. Quellenlage geprüft: Events erscheinen in SRC-001 als **L-05** „Lokale Events: erstellen/entdecken/teilnehmen + Moderation" (Teil 3 PRD, Epic L) und in SRC-003 als **Plan 14** — beides **funktionale** Ebene; SRC-001 Teil 1 und SRC-003 §1 nennen Events **nicht**. **Es wird deshalb keine zweite Verknüpfung gesetzt und kein Item umgedeutet.** Regel wie bei REQ-042 und REQ-021: eine halb tragende Verknüpfung ist `linked-partial`, nie `linked`. |
| canvas-risk-status | risk-introduced |
| evidence-class-required | production-verified — Zeit-/Raumkorrelation zweier realer Aktivitäten ist eine Feldbedingung (EV-022, Zwei-Geräte-Test). |
| Risiko | RISK-015 |
| Offene Entscheidung | offene Fragen: OQ-002 |
| Rationale | Gemeinsame Aktivitaet ist in der Aufgabenstellung ausdruecklich als PRODUCT_OUTCOME genannt und mit CAN-128/VIS-006 samt Wochenfenster hinterlegt; der Zielwert bleibt unvalidiert (ASSUMPTION). Die Erkennungsguete wird als Nebenbedingung mitgefuehrt, weil eine hohe Quote wertlos waere, wenn sie durch Falsch-Positive entsteht. docs/traceability.md weist zusaetzlich darauf hin, dass die Erkennung den Vergleich fremder Standortspuren erfordert und damit CAN-105 (Standortmissbrauch) verschaerft. |
| Befund | Erkennung gemeinsamer Aktivität erfordert den Vergleich fremder Standortspuren; verschärft CAN-105. Register: RISK-015. |

---

### REQ-023 — Effort-Normalisierung

| Feld | Wert |
|---|---|
| Trace ID | TRC-023 |
| Vision Item | VIS-008 — Fairness Boundary: Run und Bike besitzen getrennte Metriken, Ziele und interne Wertungen; sportübergreifender  |
| Canvas Item (atomar) | CAN-062, CAN-033, CAN-036 |
| Acceptance Criterion | AC-023 — Zu REQ-023 — Then: Keine Sportart dominiert systematisch; verwendete Version und Faktoren sind nachvollziehbar. |
| Measurement Type | **RESEARCH_HYPOTHESIS** |
| Signal / Control Evidence | Aus Monte-Carlo- und Szenariosimulation ueber reale Aktivitaetsverteilungen: Verteilung des sportuebergreifenden Rangs nach Sportart, systematischer Rangversatz Run gegen Bike, Sensitivitaet des Ergebnisses gegenueber dem Effort-Faktor, Anteil Wertungen, in denen die verwendete Faktorversion nicht nachvollziehbar dokumentiert ist. Die internen Run- und Bike-Wertungen bleiben getrennt und werden nicht normalisiert - das ist selbst eine Pruefbedingung. |
| Target / Pass Condition | AC-023 qualitativ EXPLICIT: keine Sportart dominiert systematisch, verwendete Version und Faktoren sind nachvollziehbar. Eine numerische Entscheidungsschwelle fuer 'systematische Dominanz' ist MISSING - OQ-008 (Effort-, Territory- und Bahngold-Startwerte) ist offen und kein Artefakt in diesem Repository beziffert einen zulaessigen Rangversatz. Startwerte gelten bis zur bestandenen Simulation als ASSUMPTION und duerfen nicht als kalibriert dargestellt werden. |
| Measurement Window | Simulationslaeufe je Faktorversion vor Gate C; nach Rollout rollierende Auswertung je Wertungsperiode (Periodenlaenge ist nicht definiert - MISSING). |
| Evidence Needed | EV-023 — Monte-Carlo-/Szenariosimulation und Kalibrierungsbericht. |
| Evidence Source | EV-023 (Monte-Carlo-/Szenariosimulation und Kalibrierungsbericht); Mindestklasse integration-fake, aber mit der ausdruecklichen Auflage aus docs/traceability.md, dass der Kalibrierungskorpus aus real aufgezeichneten Aktivitaeten bestehen muss und nicht aus synthetischen. RISK-014 (Run/Bike-Effort ist unfair) ist offen. |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Dokumentierte Rollenreferenz zur gekoppelten Frage OQ-008 ('Product/Data') - das ist der Owner der Frage, nicht der REQ-Owner. |
| Release Gate | GATE-C |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | integration-fake — Formel und Simulation ohne Grenze; der Kalibrierungskorpus muss jedoch aus real aufgezeichneten Aktivitäten bestehen, nicht aus synthetischen. |
| Risiko | RISK-014 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-008 · **Canvas-BLOCKER:** CAN-020 (Fairness- und Manipulationsproblem) ist reserviert und inhaltlich MISSING - REQ-023 hat keinen atomaren Canvas-Problembezug; Fairness erscheint nur als Wertversprechen (CAN-033/CAN-036) und Risiko (CAN-104/CAN-109). |
| Rationale | Effort-Faktoren sind in der Aufgabenstellung ausdruecklich der RESEARCH_HYPOTHESIS zugeordnet. Sie sind der Kern der Fairnesszusage und heute unkalibriert; jeder Startwert ist eine Annahme. Sportgetrennte Messung ist hier nicht optional, sondern der Gegenstand der Untersuchung selbst. |

**Forschungsplan (RESEARCH_HYPOTHESIS)**

| Feld | Inhalt |
|---|---|
| Hypothese | Versionierte, simulierte Effort-Faktoren normalisieren Run und Bike so, dass in sportuebergreifenden Team- und Territory-Wertungen keine Sportart systematisch dominiert. |
| Plan | Stufe 1: Kalibrierungskorpus aus real aufgezeichneten Run- und Bike-Aktivitaeten aufbauen. Stufe 2: Monte-Carlo-/Szenariosimulation ueber Faktorvarianten, Kennzahl ist der systematische Rangversatz zwischen den Sportarten. Stufe 3: Kalibrierungsbericht mit versionierten Faktoren; Rollout nur mit protokollierter Version je Wertung. Stufe 4: Nachmessung im Feld je Wertungsperiode. |
| Fixtures / reale Testdaten | Real aufgezeichnete Aktivitaeten beider Sportarten in ausreichender Streuung ueber Dauer, Distanz und Leistungsniveau. Synthetische Verteilungen sind nur zur Verifikation der Simulationsmechanik zulaessig. |
| Entscheidungsschwelle | MISSING - kein zulaessiger Rangversatz beziffert; OQ-008 offen. Vom DRI zusammen mit OQ-008 vor Gate C zu entscheiden. |
| Konsequenz bei unzureichender Evidenz | Keine sportuebergreifende Wertung. Team- und Territory-Wertungen bleiben sportgetrennt, bis die Simulation eine tragfaehige Faktorversion belegt. Kein produktiver Rollout vor bestandenem Gate. |

---

### REQ-024 — Anti-Cheat mit Confidence-Stufen

| Feld | Wert |
|---|---|
| Trace ID | TRC-024 |
| Vision Item | VIS-008 — Fairness Boundary: Run und Bike besitzen getrennte Metriken, Ziele und interne Wertungen; sportübergreifender  |
| Canvas Item (atomar) | CAN-063, CAN-104, CAN-109, CAN-036 |
| CAN-109 — Herabstufung offengelegt (Runde 6, 2026-07-20) | **CAN-109 („Anti-Cheat-Fehler / False Positives gegen reale Nutzer") ist nach Nutzerauftrag Punkt 2 auf `ASSUMPTION` zurückgestuft** (Owner Canvas). **Der Anker bleibt in dieser Zeile stehen** — er wird nicht entfernt und nicht umgedeutet —, trägt aber ab sofort keinen Belegwert mehr. Quellenlage, gegen `docs/sources/` neu erhoben: „False Positive", „fälschlich", „zu Unrecht", „beschuldig", „Einspruch", „Appeal", „Confidence" ergeben in allen vier Quellen **0 Treffer** im Anti-Cheat-Kontext; „Fehlalarm" kommt vor, betrifft aber ausschließlich die **Sturzerkennung** (`SRC-001-REVYR-Vision-Canvas-PRD.md:239`, `SRC-003-REVYR-GESAMTPLAN-FINAL.md:705`). Das Risikoregister von SRC-003 (`:690` „# 10. Technische Risiken", Zeilen `:694-717`) enthält **keine** Zeile zur Anti-Cheat-Fehlklassifikation: `:701` ist die **Gegenrichtung** (= CAN-104), `:705` die Sturzerkennung, `:715` der Datenschutzaspekt der Sensor-Plausibilität. Wortnah gedeckt ist allein eine **Urteilsregel** — `SRC-003:265` „Fehlende Sensoren allein sind kein Betrug, senken aber die Beweiskraft" und `:559` „fehlende Sensoren allein ≠ Betrug" —, also **wie** geurteilt werden darf, nicht das Risiko, **dass** falsch geurteilt wird. ⚠️ **AC-024 ist davon ausdrücklich NICHT betroffen** und bleibt unverändert: sein Wortlaut ist genau diese Urteilsregel und damit wortnah belegt. Unbelegt ist allein die auf CAN-109 aufsetzende **quantitative** Falsch-Positiv-Messung. **Kein Anker entfernt, keine ID vergeben, nichts hochgestuft.** |
| Acceptance Criterion | AC-024 — Zu REQ-024 — Then: Fehlende Sensoren allein führen nicht zur Betrugsannahme; klare Manipulation zählt nicht für Wettbewerb. |
| Measurement Type | **RESEARCH_HYPOTHESIS** |
| Signal / Control Evidence | Ueber einen realen Aktivitaetskorpus, zwingend getrennt fuer Run und Bike: Falsch-Positiv-Rate je Confidence-Stufe (verified-high, verified-standard, low-confidence, review-required, rejected), Anteil review-required an allen Aktivitaeten, Trefferquote gegen bekannte Manipulationsfixtures, Anteil Faelle, in denen allein fehlende Sensoren zu einer Herabstufung fuehren. Die Sporttrennung ist konstitutiv: Geschwindigkeiten, die fuer Run zwingend Manipulation bedeuten, sind fuer Bike legitim. |
| Target / Pass Condition | AC-024 qualitativ EXPLICIT: fehlende Sensoren allein fuehren nicht zur Betrugsannahme; klare Manipulation zaehlt nicht fuer den Wettbewerb. Eine zulaessige Falsch-Positiv-Rate ist MISSING - kein Artefakt beziffert sie, EV-024 verlangt nur ein False-Positive-Review. Schwellen muessen sportgetrennt entschieden werden. OFFENER WIDERSPRUCH: serverseitige Sensorplausibilitaet setzt Rohsensordaten voraus, die REQ-034 nur bei nachgewiesener Notwendigkeit uebertragen will (docs/traceability.md, Befund REQ-024). |
| Measurement Window | Auswertung je Korpusdurchlauf vor Gate C; nach Rollout laufende Ueberwachung der Falsch-Positiv-Rate je Kalendermonat und je Sportart. Das Ueberwachungsintervall ist nicht dokumentiert - Vorschlag waere erfunden, daher offen zu entscheiden. |
| Evidence Needed | EV-024 — Betrugs-/Grenzfall-Fixtures und False-Positive-Review. |
| Evidence Source | EV-024 (Betrugs-/Grenzfall-Fixtures und False-Positive-Review); Mindestklasse production-verified - die Falsch-Positiv-Rate ist erst gegen einen realen Aktivitaetskorpus aussagefaehig. RISK-013 (Anti-Cheat produziert False Positives) ist offen und verlangt zusaetzlich einen Appeal-Flow, den das REQ nicht beschreibt. |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Der Widerspruch zu REQ-034 (Datenminimierung gegen Rohsensordaten) braucht zusaetzlich eine Privacy-Entscheidung; OQ-009 ist offen. |
| Release Gate | GATE-C |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | production-verified — Die Falsch-Positiv-Quote ist erst gegen einen realen Aktivitätskorpus aussagefähig. ⚠️ **Unverändert Runde 6, ausdrücklich begründet:** diese Mindestklasse ist die **höchste** des Vokabulars und ruht ihrer Begründung nach allein auf der CAN-109-Prämisse, die jetzt `ASSUMPTION` ist. Sie wird **trotzdem nicht abgesenkt** — eine Absenkung wäre eine Erleichterung der Prüfhürde und damit der Sache nach eine Hochstufung des Reifegrads. Die Abhängigkeit ist offengelegt, die Auflösung ist eine Nutzerentscheidung. |
| Risiko | RISK-013, RISK-022 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-009 · Widersprüche: CONTRA-004 · **Canvas-BLOCKER:** CAN-020 (Fairness- und Manipulationsproblem) ist reserviert und inhaltlich MISSING - REQ-024 hat keinen atomaren Canvas-Problembezug. |
| Rationale | Anti-Cheat-Schwellen sind in der Aufgabenstellung ausdruecklich der RESEARCH_HYPOTHESIS zugeordnet. Die entscheidende Groesse ist die Fehlbeschuldigung realer Nutzer (CAN-109), nicht die Betrugserkennung allein (CAN-104) - beide Richtungen werden deshalb getrennt gemessen. Ohne bezifferte Schwelle und ohne geloesten Datenminimierungs-Widerspruch darf die Klassifikation keine Wettbewerbswirkung entfalten. ⚠️ **Runde 6 (2026-07-20):** dieser Satz stützt sich auf **CAN-109**, das seit dem 2026-07-20 `ASSUMPTION` ist. Die **getrennte Messung beider Fehlerrichtungen bleibt bestehen** — sie ist die vorsichtigere Auslegung —, gilt aber als Annahme, nicht als belegte Vorgabe. Siehe die Zeile „CAN-109 — Herabstufung offengelegt". |
| Befund | Mindert CAN-104 (Betrug), erzeugt aber zwei neue Risiken: CAN-109 (Falsch-Positive gegen reale Nutzer) und die Spannung zu CAN-088 (Datenminimierung) / REQ-034. **CONTRA-004 ist durch Nutzerentscheidung vom 2026-07-19 aufgelöst** (siehe Abschnitt „Widerspruchs-Auflösungen“): nur minimierte, abgeleitete Plausibilitätssignale gehen an den Server. Implementierungs-Evidence steht aus. Register: RISK-013, RISK-022. |

**Forschungsplan (RESEARCH_HYPOTHESIS)**

| Feld | Inhalt |
|---|---|
| Hypothese | Serverseitige Plausibilitaetsregeln trennen manipulierte von realen Aktivitaeten so, dass reale Nutzer nicht faelschlich als Betrug klassifiziert werden - auch ohne vollstaendige Sensorausstattung. |
| Plan | Stufe 1: realen Aktivitaetskorpus je Sportart aufbauen, inklusive Grenzfaellen (Bahnfahrt, Windschatten, Zugfahrt, Sensorausfall). Stufe 2: Regelsatz gegen den Korpus laufen lassen, Falsch-Positiv- und Falsch-Negativ-Rate je Confidence-Stufe bestimmen. Stufe 3: manuelles False-Positive-Review der Grenzfaelle. Stufe 4: Entscheidung ueber Schwellen und ueber den Umfang uebertragener Sensordaten gemeinsam mit REQ-034. |
| Fixtures / reale Testdaten | Realer Aktivitaetskorpus beider Sportarten plus kuratierte Manipulationsfixtures (Teleport, unplausible Geschwindigkeit, importierte Fremdtracks). Rein synthetische Daten reichen fuer die Falsch-Positiv-Aussage nicht. |
| Entscheidungsschwelle | MISSING - keine zulaessige Falsch-Positiv-Rate beziffert, weder global noch je Sportart. Vor Gate C zu entscheiden. |
| Konsequenz bei unzureichender Evidenz | Keine wettbewerbswirksame Klassifikation: Aktivitaeten werden hoechstens intern markiert, aber nicht aus Rankings, Challenges oder Territory ausgeschlossen. Kein produktiver Rollout vor bestandenem Gate. |

---

### REQ-025 — Challenges, Rankings und idempotente Rewards

| Feld | Wert |
|---|---|
| Trace ID | TRC-025 |
| Vision Item | VIS-004 — Product Value: Die Plattform verbindet erklärbare Trainingsbelastung, verdiente Progression, lokale Teams und  |
| Canvas Item (atomar) | CAN-061, CAN-062, CAN-033 |
| Acceptance Criterion | AC-025 — Zu REQ-025 — Then: Fortschritt ist korrekt und kein Reward wird doppelt vergeben. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Idempotenz und Determinismus: Anzahl doppelt vergebener Rewards unter Nebenlaeufigkeit und bei Wiedereinspielung derselben Aktivitaet, Reproduzierbarkeit des Challenge-Fortschritts ueber deterministische Fixtures, Anteil serverkonfigurierter Challenge-Definitionen, die ohne Client-Release wirksam werden, Anzahl Rankings, in denen Run- und Bike-Ergebnisse vermischt sind. Rankings werden sportgetrennt gefuehrt und getrennt geprueft (VIS-008). |
| Target / Pass Condition | AC-025 als Pass/Fail mit Nullschwelle: der Fortschritt ist korrekt und 0 Rewards werden doppelt vergeben - auch bei Wiederholung und unter Nebenlaeufigkeit gegen die echte Datenbank mit echten Constraints. 0 sportuebergreifend vermischte Rankings. Ein Teilnahme- oder Engagement-Zielwert fuer Challenges wird nicht gesetzt: docs/traceability.md haelt fuer REQ-025 ausdruecklich fest, dass kein Challenge- oder Ranking-Signal in CAN-009/VIS-006 existiert - ein solcher Wert waere erfunden. |
| Measurement Window | Je CI-Lauf der deterministischen Fixtures; Nebenlaeufigkeits- und Wiederholungstest gegen die echte Datenbank vor Gate C und bei jeder Aenderung der Reward-Vergabe. |
| Evidence Needed | EV-025 — Deterministische Fixtures und Wiederholungs-Test. |
| Evidence Source | EV-025 (deterministische Fixtures und Wiederholungs-Test); Mindestklasse real-boundary-smoke - Idempotenz unter Nebenlaeufigkeit haelt nur gegen die echte Datenbank mit echten Constraints (docs/traceability.md). |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. |
| Release Gate | GATE-C |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | value-risk |
| evidence-class-required | real-boundary-smoke — Idempotenz unter Nebenläufigkeit hält nur gegen die echte DB mit echten Constraints. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002 |
| Rationale | Der pruefbare Kern von REQ-025 ist Korrektheit und Idempotenz - eine Betriebsqualitaet mit Nullschwelle, kein Nutzerverhalten. Requirement-spezifische Nichtanwendbarkeit eines Produktsignals: docs/traceability.md fuehrt REQ-025 als value-risk, weil Rankings und Rewards Wettbewerbsmechanik ohne Health-Beitrag sind und kein Erfolgssignal misst, ob sie den Produktwert bewegen; ein erfundenes Teilnahmeziel wuerde diese dokumentierte Luecke verdecken statt sie sichtbar zu halten. |
| Befund | Rankings und Rewards sind Wettbewerbsmechanik ohne Health-Beitrag; Spannung zu CAN-033. Kein Erfolgssignal misst, ob sie den Wert bewegen. |

---

### REQ-026 — Team-Territory

| Feld | Wert |
|---|---|
| Trace ID | TRC-026 |
| Vision Item | VIS-008 — Fairness Boundary: Run und Bike besitzen getrennte Metriken, Ziele und interne Wertungen; sportübergreifender  |
| Vision Item (ergänzend, aus dem Messmodell) | VIS-006 |
| Canvas Item (atomar) | CAN-064, CAN-106, CAN-078, CAN-129, CAN-032 |
| Acceptance Criterion | AC-026 — Zu REQ-026 — Then: Eroberung folgt Formel und Quorum, reale Areale werden dargestellt und das interne Raster ist nie sichtbar. |
| Measurement Type | **RESEARCH_HYPOTHESIS** |
| Signal / Control Evidence | Aus Geo-Fixtures, Simulation und Karten-Lasttest: Determinismus der Eroberungsberechnung bei identischem Eingabeset, Verteilung der Arealwechsel ueber Quorumsvarianten, Renderzeit und Bildrate des Kartenlayers bei realer Datenmenge (NFR-004), Anzahl Pfade, ueber die das interne Raster sichtbar wird, Anteil in die Wertung eingehender Beitraege ohne verifizierten Status. Als nachgelagertes Produktsignal nach bestandenem Gate: Season-Teilnahme aktiver Teams (CAN-129). |
| Target / Pass Condition | Quorumswerte, Verfallsmodell und Arealschwellen sind MISSING (OQ-008). AC-026 gibt qualitativ vor: Eroberung folgt Formel und Quorum, reale benannte Areale werden dargestellt, das interne Raster ist nie sichtbar - 0 Sichtbarkeitspfade (EXPLICIT, Nullschwelle, entspricht Non-Goal CAN-078). NFR-004 fordert viewportbasierte Kartenlayer und einen Geo-Lasttest vor D, nennt aber keine Millisekunden- oder Bildratenschwelle: MISSING. Nachgelagertes Produktziel VIS-006 Zeile D: Season-Teilnahme aktiver Teams > 60 % - ASSUMPTION, unvalidiert. |
| Measurement Window | Simulations- und Lasttestlaeufe je Parametervariante vor Gate D; nach Rollout Auswertung je Season-Zyklus - die Laenge eines Season-Zyklus ist in keinem Artefakt definiert (MISSING, siehe auch REQ-027). |
| Evidence Needed | EV-026 — Geo-Fixtures, Simulation und Karten-Lasttest. |
| Evidence Source | EV-026 (Geo-Fixtures, Simulation und Karten-Lasttest); Mindestklasse real-boundary-smoke - Kartenlayer-Performance und Geo-Lasttest brauchen echtes Geraet und echte Datenmenge. RISK-017 (Polygonoperationen inkonsistent oder langsam) ist offen. |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Dokumentierte Rollenreferenz zu den gekoppelten Fragen OQ-008 ('Product/Data') und OQ-005 ('Engineering'). |
| Release Gate | GATE-D |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | real-boundary-smoke — Kartenlayer-Performance (NFR-004) und Geo-Lasttest brauchen echtes Gerät und echte Datenmenge. |
| Risiko | RISK-015, RISK-017 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-005, OQ-008 |
| Rationale | Territory und Quoren sind in der Aufgabenstellung ausdruecklich der RESEARCH_HYPOTHESIS zugeordnet: die Mechanik ist unvalidiert und ihre Parameter sind offen. Die Unsichtbarkeit des internen Rasters wird als harte Nullschwelle mitgefuehrt, weil sie ein Non-Goal (CAN-078) schuetzt. Sportspezifische Trennung: die Territory-Wertung ist sportuebergreifend und haengt damit unmittelbar an der noch unkalibrierten Effort-Normalisierung aus REQ-023 - solange die fehlt, ist auch die Territory-Fairness nicht bewertbar. |
| Befund | CAN-106 (Geo-Komplexität), CAN-105 (Standortmissbrauch) und NFR-004-Performance. Kein Non-Goal-Verstoß, da Release D (CAN-136) und nicht v1.0. Register: RISK-017, RISK-015. |

**Forschungsplan (RESEARCH_HYPOTHESIS)**

| Feld | Inhalt |
|---|---|
| Hypothese | Nur verifizierte Beitraege und ein Quorum bestimmen reale, benannte Team-Areale; das interne Raster bleibt unsichtbar und die Kartenlayer bleiben unter realer Datenmenge performant filterbar. |
| Plan | Stufe 1: Quorum, Verfallsmodell und Arealschwellen entscheiden (heute MISSING, OQ-008). Stufe 2: Simulation ueber Geo-Fixtures und reale Aktivitaetsdichten, Kennzahl ist Determinismus und Stabilitaet der Arealwechsel. Stufe 3: Karten-Lasttest auf realem Geraet mit realer Datenmenge gegen NFR-004. Stufe 4: Threat-Model fuer Standortmissbrauch (CAN-105) vor jeder Freischaltung. |
| Fixtures / reale Testdaten | Geo-Fixture-Suite plus reale Aktivitaetsdichten aus mindestens einer Stadt; synthetische Gleichverteilungen unterschaetzen die Ballung und sind allein nicht ausreichend. |
| Entscheidungsschwelle | MISSING - Quorumswert, Verfallsrate und Performanceschwelle (NFR-004) sind unbeziffert. Vor Gate D zu entscheiden. |
| Konsequenz bei unzureichender Evidenz | Kein Territory-Rollout. CAN-079 und CAN-136 halten Territory ohnehin bis Stufe D gesperrt; bei nicht bestandener Simulation bleibt es auch danach deaktiviert. |

---

### REQ-027 — Seasons und nach Finalisierung fachlich unveränderbare Historie

| Feld | Wert |
|---|---|
| Trace ID | TRC-027 |
| Vision Item | VIS-004 — Product Value: Die Plattform verbindet erklärbare Trainingsbelastung, verdiente Progression, lokale Teams und  |
| Canvas Item (atomar) | CAN-066, CAN-030 |
| Acceptance Criterion | AC-027 — Zu REQ-027 — Then: Aktive Besitzstände werden zurückgesetzt und historische Records bleiben vollständig abrufbar. |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Datenintegritaet ueber den Season-Wechsel: Anteil zurueckgesetzter Objekte, die tatsaechlich zum aktiven Spielfeld gehoeren; Anzahl veraenderter oder verlorener historischer Snapshots, Trophaeen und Vereinsheim-Eintraege nach zwei Season-Zyklen; Reproduzierbarkeit des Rollovers bei Wiederholung; Anzahl historischer Datensaetze, die nach einem Rollover nicht mehr abrufbar sind. |
| Target / Pass Condition | AC-027 als Pass/Fail mit Nullschwelle: aktive Besitzstaende werden zurueckgesetzt, historische Records bleiben vollstaendig abrufbar - 0 Verluste und 0 nachtraegliche Aenderungen im Zwei-Season-Integrationstest. OFFENER WIDERSPRUCH gegen REQ-017 und NFR-006: welche Historiendaten eine vollstaendige In-App-Accountloeschung ueberleben duerfen, ist ungeklaert (docs/traceability.md, Befund REQ-027). Bis zur Entscheidung ist 'unveraenderlich' nicht widerspruchsfrei pruefbar. Die Laenge einer Season ist in keinem Artefakt definiert (MISSING) - ohne sie ist kein reales Messfenster ableitbar. |
| Measurement Window | Zwei vollstaendige Season-Zyklen im Integrationstest (EV-027); die reale Zyklusdauer ist MISSING und muss vor der Feldmessung entschieden werden. |
| Evidence Needed | EV-027 — Zwei-Season-Integrationstest, Prüfung der fachlichen Unveränderbarkeit nach Finalisierung sowie Nachweis, dass Löschung und Anonymisierung als zulässige Ausnahmen korrekt greifen (Löschung eines Mitglieds mit historischen Capture-Ereignissen). |
| Evidence Source | EV-027 (Titel wie in `Evidence Needed`); Mindestklasse real-boundary-smoke — Season-Rollover mit fachlicher Unveränderbarkeit nach Finalisierung hängt an echten Transaktionen und Constraints. |
| Evidence-Titel — Nachzug (2026-07-19) | Die Vorfassung beider Felder trug „Unveränderlichkeitsprüfung" — die durch **DEC-012 / CONTRA-005** projektweit ersetzte Formulierung. Übernommen ist der in Phase 1 registrierte EV-027-Titel (`ID-REGISTRY.md` §6.6). **Herkunft, ausdrücklich:** DEC-012 gibt für den Begriff „Unveränderlichkeitsprüfung" **keine** Ersatzformulierung vor; es wurde deshalb **keine erfunden**. Der Wortlaut ist **wörtlich** aus der `canonical_file` `docs/prd/…prd.md:293` übernommen, die das PRD am 2026-07-19 bereits migriert hatte. **Provenienz-Vorbehalt:** dieser Wortlaut ist eine Formulierung des PRD-Owners, **nicht** durch DEC-012 vorgegeben und **nicht** vom Nutzer bestätigt. Ändert der Nutzer die Sprachregelung, ist das PRD die zu ändernde Stelle; diese Matrix und die Registry ziehen nach — nicht umgekehrt. |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Der Loeschungs-/Historien-Widerspruch braucht zusaetzlich eine Privacy-Entscheidung; OQ-009 ist offen. |
| Release Gate | GATE-D |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | real-boundary-smoke — Season-Rollover mit fachlicher Unveränderbarkeit nach Finalisierung hängt an echten Transaktionen und Constraints. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-009 · Widersprüche: CONTRA-005 |
| Rationale | Der pruefbare Kern von REQ-027 ist eine Datenintegritaetsgarantie - Ruecksetzumfang und Unveraenderlichkeit - und damit Betriebsqualitaet mit Nullschwelle. Das naheliegende Produktsignal Season-Teilnahme (CAN-129, VIS-006 Zeile D, > 60 %) misst das Territory-/Season-System als Ganzes und wird deshalb bei REQ-026 gefuehrt; ein korrekter Rollover allein kann es weder belegen noch widerlegen. source_type MISSING, weil sowohl die Seasonlaenge als auch der Umfang ueberlebender Historiendaten unbestimmt sind. Sportspezifische Trennung ist requirement-spezifisch nicht anwendbar: der Rollover wirkt auf Besitzstaende und Snapshots, die selbst keine Sportart tragen; sportgetrennt sind die darin gespeicherten Rekorde, deren Vollstaendigkeit je Sportart stichprobenartig zu belegen ist. |
| Befund | **CONTRA-005 ist durch Nutzerentscheidung vom 2026-07-19 aufgelöst.** Die Formulierung „unveränderliche Historie“ ist ersetzt durch: „Nach Finalisierung fachlich unveränderbar, außer aufgrund Löschung, Anonymisierung oder rechtlicher Korrektur.“ Historische Team-/Season-Daten dürfen nur anonymisiert erhalten bleiben; ist wirksame Anonymisierung nicht möglich, muss gelöscht werden. Datenmodell und Event-Historie müssen Identität und historische Aggregate technisch trennen — **vor** Erstellung/Finalisierung des Datenbankschemas. Nachzug, erneut geprüft am 2026-07-19 nach dem Registry-Auftau-Schritt: **PRD nachgezogen** (`prd.md:138` bzw. `:293`), **Registry nachgezogen** (`ID-REGISTRY.md` §6.4 REQ-027, §6.6 EV-027 — beide Titel im Auftau-Schritt korrigiert), **diese Datei nachgezogen** in TRC-027 (§1), der Blocküberschrift (§3) und jetzt auch in `Evidence Needed`/`Evidence Source`. Damit ist der Sprachregelungs-Nachzug zu DEC-012 **in allen vier Dateien vollzogen**; die frühere Aussage „offen bleibt allein die eingefrorene Registry” ist überholt. **Weiterhin offen ist nicht die Sprache, sondern die Sache:** `evidence_status` von CONTRA-005 steht auf `pending` (§7), und für den Nachweis „Datenmodell trennt Identität und historische Aggregate” existiert **keine EV-ID** — siehe §7, CONTRA-005. |

---

### REQ-028 — Deterministische Einzel-Reviere

| Feld | Wert |
|---|---|
| Trace ID | TRC-028 |
| Vision Item | VIS-008 — Fairness Boundary: Run und Bike besitzen getrennte Metriken, Ziele und interne Wertungen; sportübergreifender  |
| Canvas Item (atomar) | CAN-065, CAN-106, CAN-105, CAN-078 |
| Acceptance Criterion | AC-028 — Zu REQ-028 — Then: Dasselbe Eingabeset erzeugt dieselbe Geometrie und denselben Besitzer; Linien-/Drift-Tracks werden abgelehnt. |
| Measurement Type | **RESEARCH_HYPOTHESIS** |
| Signal / Control Evidence | Aus Geo-Fixture-Suite und Property-Tests: Determinismus (identisches Eingabeset erzeugt identische Geometrie und identischen Besitzer), Ablehnungsrate fuer reale Drift- und Linien-Tracks, Verhalten bei Ueberlappung, Teiluebernahme, Restflaechen und Gleichstaenden, Rechenzeit je Flaechenoperation bei realer Track-Laenge. Run und Bike getrennt, weil Rundenlaenge, Kurvenradien und Geschwindigkeit die Rundenerkennung und die Anfahrtssegmentierung unterschiedlich belasten. |
| Target / Pass Condition | AC-028 qualitativ EXPLICIT: dasselbe Eingabeset erzeugt dieselbe Geometrie und denselben Besitzer; Linien- und Drift-Tracks werden abgelehnt. Numerische Schwellen fuer Rundenerkennung, Mindestflaeche, Toleranzen und Gleichstandsaufloesung sind MISSING (OQ-008). Zusaetzliche Freigabebedingung aus dem REQ selbst: bestandene Simulation UND Threat-Model - vor beidem kein produktiver Rollout. ASM-104 haelt Einzel-Reviere bis Stufe D deaktiviert. |
| Measurement Window | Property- und Fixture-Laeufe bei jedem CI-Durchlauf; Simulations- und Threat-Model-Abnahme vor Gate D; reale Drift-Tracks je Sportart vor der Freischaltung. |
| Evidence Needed | EV-028 — Geo-Fixture-Suite, Property-Tests und Threat-Model. |
| Evidence Source | EV-028 (Geo-Fixture-Suite, Property-Tests und Threat-Model); Mindestklasse real-boundary-smoke - die Geometrie ist deterministisch pruefbar, aber die Ablehnung von Linien-/Drift-Tracks braucht reale Drift-Tracks (docs/traceability.md). RISK-016 (Einzel-Reviere verraten Wohnort und Routine) ist kritisch und offen. |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Dokumentierte Rollenreferenz zur gekoppelten Frage OQ-008 ('Product/Data'); das Threat-Model braucht zusaetzlich eine Privacy-Verantwortung, die nicht benannt ist. |
| Release Gate | GATE-D |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | real-boundary-smoke — Geometrie ist deterministisch prüfbar, aber „Linien-/Drift-Tracks werden abgelehnt“ (AC-028) braucht reale Drift-Tracks. |
| Risiko | RISK-016, RISK-017 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-008 · **Canvas-BLOCKER:** Mehrfacher BLOCKER. (1) CAN-021 (Problem hinter Einzel-Revieren und Sportplatz-Challenges) ist reserviert und inhaltlich MISSING. (2) Keine CAN-003-Nachfolgeklausel deckt Einzel-Reviere - CAN-032 fordert ausdruecklich Gemeinschaft, Einzel-Reviere sind per Definition nicht gemeinsam. (3) Kein Erfolgssignal: CAN-124..CAN-129 kennen kein Einzel-Revier-Signal. Das REQ haengt damit nur an der Capability CAN-065 und an Risiko-Items. |
| Rationale | Einzel-Reviere und Revier-Geometrie sind in der Aufgabenstellung ausdruecklich der RESEARCH_HYPOTHESIS zugeordnet. Der Determinismus ist zwar formal pruefbar, aber alle Parameter, die ihn erst definieren, fehlen - deshalb source_type MISSING. Zusaetzlicher Befund aus docs/traceability.md: REQ-028 hat weder Canvas-Problembezug noch Wertklausel noch Erfolgssignal und zahlt damit auf kein dokumentiertes Canvas-Ziel ein. |
| Befund | CAN-106 und CAN-105: Einzel-Reviere kartieren individuelle Bewegungsmuster inklusive Wohnumfeld. Sekundär: CAN-021 reserved, keine Wertklausel, kein Erfolgssignal — das REQ zahlt auf kein dokumentiertes Canvas-Ziel ein. Register: RISK-016, RISK-017. |

**Forschungsplan (RESEARCH_HYPOTHESIS)**

| Feld | Inhalt |
|---|---|
| Hypothese | Rundenerkennung, Anfahrtssegmentierung, Uebernahmeprioritaet und Polygon-Union/-Differenz lassen sich so definieren, dass dasselbe Eingabeset immer dieselbe Geometrie und denselben Besitzer erzeugt und Linien-/Drift-Tracks zuverlaessig abgelehnt werden. |
| Plan | Stufe 1: Geometrie- und Prioritaetsregeln vollstaendig spezifizieren inklusive Gleichstand und Restflaechen. Stufe 2: Property-Tests auf Determinismus und Idempotenz ueber generierte Geometrien. Stufe 3: reale Drift- und Linien-Tracks je Sportart gegen den Ablehnungspfad laufen lassen. Stufe 4: Threat-Model zu Wohnort- und Routinepreisgabe (RISK-016) mit Anonymisierung, Start-/End-Unschaerfe und Retention. |
| Fixtures / reale Testdaten | Geo-Fixture-Suite mit generierten Grenzfaellen plus reale Aufzeichnungen mit Drift, Tunnelverlust und Linienverhalten je Sportart. Ohne reale Drift-Tracks ist die Ablehnungsaussage nicht belastbar. |
| Entscheidungsschwelle | MISSING - Mindestflaeche, Rundenkriterium, Toleranzen und Gleichstandsregel sind unbeziffert (OQ-008). Zusaetzlich fehlt eine Schwelle fuer die zulaessige Preisgabe von Wohnumfeldinformationen. |
| Konsequenz bei unzureichender Evidenz | Einzel-Reviere bleiben deaktiviert (ASM-104 haelt sie ohnehin bis Stufe D aus). Bei nicht bestandener Simulation oder nicht bestandenem Threat-Model erfolgt keine Freischaltung, auch nicht in Stufe D. |

---

### REQ-029 — Sportplatz-Challenges und Bahngold-Score

| Feld | Wert |
|---|---|
| Trace ID | TRC-029 |
| Vision Item | VIS-004 — Product Value: Die Plattform verbindet erklärbare Trainingsbelastung, verdiente Progression, lokale Teams und  |
| Canvas Item (atomar) | CAN-107, CAN-110, CAN-030 |
| Acceptance Criterion | AC-029 — Zu REQ-029 — Then: Nur plausible Runden zählen; geschlossene/private Anlagen bleiben gesperrt und Bahngold verändert keine Effor… |
| Measurement Type | **RESEARCH_HYPOTHESIS** |
| Signal / Control Evidence | Aus realem Bahn-Test und OSM-Access-Review: Erkennungsrate vollstaendiger Runden und Falsch-Positiv-Rate unter realem GPS-Rauschen auf einer echten Bahn, Anteil kuratierter Anlagen mit korrektem Zugangs- und Oeffnungsstatus, Anzahl gesperrter oder privater Anlagen, die dennoch als Challenge-Ort erscheinen, sowie der Nachweis ueber Reward-Fixtures, dass Bahngold weder Effort- noch Territory-Wertung veraendert. |
| Target / Pass Condition | AC-029 qualitativ EXPLICIT mit zwei Nullschwellen: 0 geschlossene oder private Anlagen erscheinen als Challenge-Ort, und Bahngold veraendert in 0 Faellen eine Effort- oder Territory-Wertung (nicht uebertragbarer Progressions-Score, keine Waehrung). GPS-Toleranz, Rundenkriterium und Bahngold-Startwerte sind MISSING (OQ-008). Die Bike-Anwendbarkeit ist laut docs/traceability.md eine OPEN QUESTION und wird hier nicht durch eine Annahme geschlossen. RISK-019 (Bahngold foerdert gesundheitlich riskantes Grinding) verlangt zusaetzlich eine Degressions- und Limitregel, die in keinem Artefakt beziffert ist. |
| Measurement Window | Bahn-Testlaeufe vor Gate D auf mindestens einer realen Anlage; OSM-Access-Review je Kuratierungsdurchlauf; Reward-Fixtures bei jedem CI-Lauf. Ein Ueberwachungsintervall fuer den Zugangsstatus kuratierter Anlagen ist nicht dokumentiert - offen zu entscheiden, nicht zu raten. |
| Evidence Needed | EV-029 — OSM-Access-Review, realer Bahn-Test und Reward-Fixtures. |
| Evidence Source | EV-029 (OSM-Access-Review, realer Bahn-Test und Reward-Fixtures); Mindestklasse production-verified - GPS-tolerante Rundenerkennung auf einer realen Bahn ist eine Feldmessung. RISK-018 (OSM-Sportplatz ist privat oder falsch) und RISK-019 sind offen. |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Dokumentierte Rollenreferenz zur gekoppelten Frage OQ-008 ('Product/Data'); fuer Kuratierung, Sperrliste und Meldesystem existiert keine benannte Betriebsverantwortung. |
| Release Gate | GATE-D |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | production-verified — GPS-tolerante Rundenerkennung auf einer realen Bahn ist eine Feldmessung (EV-029). |
| Risiko | RISK-018, RISK-019 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-008 · **Canvas-BLOCKER:** Staerkster Canvas-BLOCKER aller aktiven Requirements. (1) CAN-021 (Problem hinter Sportplatz-Challenges) ist reserviert und inhaltlich MISSING. (2) Es existiert KEIN atomares Capability-Item fuer Sportplatz-Challenges oder Bahngold - die Capability-Gruppe CAN-047..CAN-070 sowie die spaeter ergaenzten CAN-138, CAN-139, CAN-142 und CAN-143 nennen weder das eine noch das andere (*Bereichsangabe am 2026-07-20 aufgeloest: die frueher hier stehende Schreibweise „CAN-138..CAN-140" umfasste mechanisch das seit dem 2026-07-20 **deprecatete** CAN-140*); CAN-061 (Challenges) traegt laut Registry REQ-025, nicht REQ-029. (3) Kein Erfolgssignal. Es bleiben nur die beiden Risiko-Items CAN-107/CAN-110 und die schwache Wertklausel CAN-030. Zuordnung wurde nicht erfunden. |
| Rationale | Bahngold ist in der Aufgabenstellung ausdruecklich der RESEARCH_HYPOTHESIS zugeordnet. Die Wirkungslosigkeit von Bahngold auf Effort und Territory wird als harte Nullschwelle gemessen, weil sie die Fairnesszusage schuetzt. Die Bike-Anwendbarkeit wird ausdruecklich offen gehalten statt sie als 'nicht relevant' abzutun: eine Bahn ist eine Laufanlage, ob es eine Rad-Entsprechung geben soll, ist eine dokumentierte offene Frage und keine Ableitung. |
| Befund | CAN-107 (OSM-Qualität) und CAN-110 (private/gesperrte Sportanlagen). Sekundär: Bahngold beeinflusst laut REQ ausdrücklich weder Effort noch Territory, hat kein Erfolgssignal und nur schwachen Wertbezug. Register: RISK-018, RISK-019. |

**Forschungsplan (RESEARCH_HYPOTHESIS)**

| Feld | Inhalt |
|---|---|
| Hypothese | Auf kuratierten, oeffentlich zugaenglichen Sportanlagen lassen sich vollstaendige Runden GPS-tolerant so validieren, dass nur plausible Runden zaehlen; Bahngold bleibt dabei ein nicht uebertragbarer Progressions-Score ohne Effort- oder Territory-Wirkung. |
| Plan | Stufe 1: Kuratierungs- und Sperrlistenprozess samt Access-/Opening-Hours-Auswertung definieren. Stufe 2: realer Bahn-Test mit wiederholten Runden zur Bestimmung von Erkennungs- und Falsch-Positiv-Rate. Stufe 3: Reward-Fixtures, die belegen, dass Bahngold keine andere Wertung beeinflusst. Stufe 4: Degressions-/Limitregel gegen Grinding (RISK-019) festlegen und pruefen. |
| Fixtures / reale Testdaten | Reale Rundenaufzeichnungen auf mindestens einer echten Bahn unter unterschiedlichen Empfangsbedingungen; OSM-Daten mit Zugangsattributen; Reward-Fixtures fuer die Wirkungslosigkeitspruefung. |
| Entscheidungsschwelle | MISSING - weder GPS-Toleranz noch Rundenkriterium noch Bahngold-Startwerte noch eine Degressionsregel sind beziffert (OQ-008, RISK-019). |
| Konsequenz bei unzureichender Evidenz | Sportplatz-Challenges und Bahngold bleiben deaktiviert (ASM-104 haelt Bahngold bis Stufe D aus). Ohne verlaesslichen Zugangsstatus wird keine Anlage freigeschaltet. |

---

### REQ-030 — Live-Map und Beschützer-Modus

| Feld | Wert |
|---|---|
| Trace ID | TRC-030 |
| Vision Item | VIS-009 — Privacy Boundary: Profile sind standardmäßig privat; Live-Standort ist pro Aktivität Opt-in, zeitlich begrenzt |
| Canvas Item (atomar) | CAN-068, CAN-105, CAN-037, CAN-031 |
| Acceptance Criterion | AC-030 — Zu REQ-030 — Then: In jedem Pfad endet die Freigabe; unberechtigte und blockierte Personen sehen keinen Standort. |
| Measurement Type | **COMPLIANCE_CONTROL** |
| Signal / Control Evidence | Kontrollierter Nachweis ueber die Endpfad-Matrix: Anteil der Endpfade (regulaeres Beenden, Zeitablauf, App-Kill, Netzverlust, Blockierung, Not-Aus, Geraeteausfall), in denen die Live-Freigabe nachweislich endet; Anzahl Faelle, in denen unberechtigte oder blockierte Personen Standort sehen; Nachweis der Start- und Endpunktverschleierung; Sichtbarkeit des aktiven Freigabestatus in der App; Anteil Beschuetzer-Links, die nicht automatisch enden. |
| Target / Pass Condition | AC-030 als Pass/Fail: in jedem Pfad endet die Freigabe - 100 % der Endpfad-Matrix; 0 Standortsichtbarkeit fuer Unberechtigte und Blockierte; 0 Beschuetzer-Links ohne automatisches Ende. Der maximal zulaessige Freigabezeitraum und der Verschleierungsradius sind in keinem Artefakt beziffert: MISSING; OQ-009 (Datenretention fuer GPS, Health und Live) ist offen. |
| Measurement Window | Vor Gate D und danach bei jeder Aenderung an Freigabe, Realtime-Zustellung oder Blockierlogik; jede Zeile der Endpfad-Matrix einzeln, je Plattform. Penetrationstest je Release-Stufe ab D. |
| Evidence Needed | EV-030 — Threat-Model, Endpfad-Matrix und Penetrationstest. |
| Evidence Source | EV-030 (Threat-Model, Endpfad-Matrix und Penetrationstest); Mindestklasse production-verified - jeder Endpfad inklusive App-Kill, Netzverlust und Not-Aus ist nur real nachweisbar, ein Fake beweist die Beendigung nicht (docs/traceability.md). RISK-015 (Standortfreigabe ermoeglicht Stalking) ist kritisch und offen. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Zusaetzlich offen: OQ-009 ('Privacy/Product') fuer Freigabedauer und Retention. |
| Release Gate | GATE-D |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | production-verified — Jeder Endpfad inklusive App-Kill, Netzverlust und Not-Aus ist nur real nachweisbar; ein Fake beweist die Beendigung nicht. |
| Risiko | RISK-015 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-009 · **Canvas-BLOCKER:** Doppelter BLOCKER. (1) CAN-017 (Sicherheitsproblem) ist reserviert und inhaltlich MISSING - der Canvas nennt kein Sicherheitsproblem, VIS-003 dagegen 'sicheren Zugang'; dokumentierte Canvas/Vision-Divergenz. (2) CAN-031 ('Trainiere sicherer') ist als Wertklausel gefuehrt, laesst aber laut Canvas offen, ob Trainings- oder Datensicherheit gemeint ist - die Klausel ist bis zur Klaerung nicht pruefbar und traegt REQ-030 deshalb nur vorbehaltlich. |
| Rationale | Live-Standortfreigabe ist in der Aufgabenstellung ausdruecklich als COMPLIANCE_CONTROL-Fall (Standortfreigabe, Security) genannt. Requirement-spezifische Nichtanwendbarkeit eines Nutzersignals: eine Nutzungsquote der Live-Freigabe waere sogar schaedlich als Ziel, weil das Produkt keine Anreize zur Standortpreisgabe setzen darf; entscheidend ist ausschliesslich, dass jeder Endpfad haelt. Sportspezifische Trennung ist nicht anwendbar, weil Freigabe, Beendigung und Verschleierung an der Aktivitaet und am Kontakt haengen, nicht an der Sportart; die Endpfad-Matrix wird trotzdem einmal je Sportart durchlaufen, weil Aktivitaetsdauer und Netzabdeckung bei Bike typischerweise groessere Distanzen umfassen. |
| Befund | CAN-105 in der höchsten Ausprägung (Live-Standort an Dritte). CAN-017 (Problembezug) ist reserved; „sicherer“ in CAN-031 ist nicht definiert. Register: RISK-015. |

---

### REQ-031 — Sturzerkennung als Assistenz

| Feld | Wert |
|---|---|
| Trace ID | TRC-031 |
| Vision Item | **MISSING — BLOCKER.** Kein VIS-Item trägt eine Aussage über **Sicherheitsassistenz im Feld**. **VIS-007 ist am 2026-07-20 als Anker entfernt worden**, nicht nur kommentiert. |
| Vision-Anker — durchgeführte Prüfung (2026-07-20) | **VIS-007 trägt REQ-031 nicht.** VIS-007 lautet: „**Health-Ausgaben** sind Orientierung, keine Diagnose. **Score und Empfehlungen** müssen Datenbasis, Gründe und Unsicherheit erklären." REQ-031 erzeugt **weder Score noch Empfehlung noch eine Health-Ausgabe** — es erkennt einen Sturz und startet einen Countdown. **Warum der Anker trotzdem plausibel las:** beide Sätze klingen wie derselbe Vorbehalt („Assistenz, keine Garantie" ↔ „Orientierung, keine Diagnose"). Das ist eine **Analogie zwischen zwei verschiedenen Haftungsvorbehalten**, keine gemeinsame Aussage. Den Sicherheitsvorbehalt trägt **CAN-073** („Keine garantierte Unfallhilfe") — ein Non-Goal im Canvas, kein Vision-Item. **Ebenfalls geprüft und verworfen:** **VIS-003** („sicherer **Zugang** zu lokalen Trainingspartnern") meint soziale Auffindbarkeit, nicht Unfallsicherheit. **VIS-009** regelt Sichtbarkeit von Standortdaten (das trägt REQ-030, nicht REQ-031). **VIS-010** nennt „Safety-System" zwar **wörtlich**, ist aber eine **Freigabebedingung** („wird nicht vor dem Evidence-Gate der vorherigen Stufe veröffentlicht") und **keine Produktzusage** — exakt der Grund, aus dem VIS-005 am 2026-07-19 für REQ-032 verworfen wurde. Dieselbe Regel wird hier angewandt. **Kein Item wird umgedeutet, keine VIS-ID erfunden.** Es ist **nicht einmal eine VIS-ID reserviert** — wie bei REQ-032 und REQ-006 eine MISSING-Position, keine reservierte Leerstelle. |
| Abgrenzung zu REQ-030 — geprüft, damit Schweigen nicht als „geklärt" gelesen wird | **REQ-030 (Live-Map und Beschützer-Modus) behält VIS-009 und bleibt `linked`.** VIS-009 nennt „Live-Standort ist pro Aktivität **Opt-in**, zeitlich begrenzt und start-/endpunktverschleiert" — das ist der Prüfgegenstand von AC-030 **wörtlich**. REQ-030 und REQ-031 teilen sich zwar den Canvas-Anker CAN-068 (Live-Safety), aber ihre Vision-Lage ist **verschieden**: REQ-030 ist im Kern eine Sichtbarkeits-/Privacy-Frage, REQ-031 eine Sensorik-/Assistenzfrage. Ohne diese ausdrückliche Prüfung würde ein Leser aus der Änderung bei REQ-031 schließen, REQ-030 sei mitgeprüft worden — oder umgekehrt, es sei unauffällig. |
| Canvas Item (atomar) | CAN-068 (Capability), CAN-073 (Non-Goal), CAN-031 (Wertversprechen, **nur vorbehaltlich** — „sicherer" ist im Canvas undefiniert, OQ zu CAN-031) |
| Acceptance Criterion | AC-031 — Zu REQ-031 — Then: Ein sichtbarer Countdown startet, kann abgebrochen werden und nur danach wird der definierte Kontakt informie… |
| Measurement Type | **RESEARCH_HYPOTHESIS** |
| Signal / Control Evidence | Aus kontrollierten Falltests und spaeterem Feldbetrieb: Fehlalarmquote pro Aktivitaetsstunde, Nichterkennungsrate in kontrollierten Falltests, Anteil Countdowns, die vom Nutzer abgebrochen werden, Anzahl Faelle, in denen ein Kontakt ohne abgelaufenen Countdown informiert wurde. Run und Bike werden getrennt gefuehrt, weil Sturzsignatur, Beschleunigungsprofil und typische Geschwindigkeit sich zwischen Laufen und Radfahren erheblich unterscheiden - ein gemeinsamer Schwellwert waere fuer mindestens eine der beiden Sportarten falsch. |
| Target / Pass Condition | Kontrollteil EXPLICIT als Pass/Fail: sichtbarer Countdown, jederzeit abbrechbar, Kontakt wird erst danach informiert - 0 vorzeitige Benachrichtigungen. Die Entscheidungsschwelle fuer die Fehlalarmquote ist MISSING: kein Artefakt beziffert eine akzeptable Quote, das REQ verlangt nur ihre Dokumentation. Ohne entschiedene Schwelle darf die Funktion nicht freigeschaltet werden - RISK-020 (Sturzerkennung erzeugt falsche Sicherheit) ist kritisch und CAN-073 haelt 'keine garantierte Unfallhilfe' als Non-Goal fest. |
| Measurement Window | Kontrollierte Falltests je Sportart vor Gate D; Fehlalarmquote fortlaufend je Aktivitaetsstunde im Feld erhoben und je Release-Stufe berichtet. |
| Evidence Needed | EV-031 — Kontrollierte Falltests, Fehlalarmstatistik und Claims-Review. |
| Evidence Source | EV-031 (kontrollierte Falltests, Fehlalarmstatistik und Claims-Review); Mindestklasse production-verified - kontrollierte Falltests und die dokumentierte Fehlalarmquote sind reine Feldnachweise. |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Die Entscheidung ueber eine akzeptable Fehlalarmquote ist zugleich eine Haftungs- und Claim-Entscheidung; OQ-006 ('Product/Legal') ist offen. |
| Release Gate | GATE-D |
| Status | **broken** (Vision-Anker MISSING seit 2026-07-20) · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | production-verified — Kontrollierte Falltests und dokumentierte Fehlalarmquote sind reine Feldnachweise. |
| Risiko | RISK-020 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-006 · **Canvas-BLOCKER:** CAN-017 (Sicherheitsproblem) ist reserviert und inhaltlich MISSING - REQ-031 hat keinen atomaren Canvas-Problembezug. CAN-031 traegt nur vorbehaltlich, weil 'sicherer' im Canvas undefiniert ist. |
| Rationale | Der Detektor ist ein unvalidiertes System mit einer Schwelle, die niemand festgelegt hat - deshalb RESEARCH_HYPOTHESIS und nicht COMPLIANCE_CONTROL, obwohl der Countdown-Teil ein reiner Kontrollnachweis ist. Die Nichtanwendbarkeit eines Nutzersignals ist requirement-spezifisch begruendet: eine Nutzungs- oder Ausloesequote als Ziel waere pervers, weil jede Ausloesung ein unerwuenschtes Ereignis ist. Ohne bezifferte Schwelle bleibt die Funktion aus - das ist die dokumentierte Konsequenz, keine Vertagung. |
| Befund | Nähe zum Non-Goal CAN-073 („keine garantierte Unfallhilfe“); Fehlalarm- und Nichterkennungsrisiko schafft eine Sicherheitserwartung, die das Produkt nicht einlösen darf. Register: RISK-020. |

**Forschungsplan (RESEARCH_HYPOTHESIS)**

| Feld | Inhalt |
|---|---|
| Hypothese | Ein Sturzmuster laesst sich aus Sensordaten je Sportart so erkennen, dass die dokumentierte Fehlalarmquote niedrig genug ist, um die Funktion als reine Assistenz ohne Sicherheitsgarantie anzubieten. |
| Plan | Stufe 1: akzeptable Fehlalarmquote je Sportart entscheiden lassen (heute MISSING). Stufe 2: kontrollierte Falltests mit dokumentiertem Protokoll je Sportart. Stufe 3: Feldmessung der Fehlalarmquote pro Aktivitaetsstunde ueber eine definierte Beobachtungsperiode. Stufe 4: Claims-Review der Assistenzsprache gegen CAN-073 und RISK-020 vor jeder Freischaltung. |
| Fixtures / reale Testdaten | Kontrollierte, protokollierte Sturzversuche je Sportart plus reale Aktivitaetsstunden ohne Sturz als Negativkorpus. Synthetische Sensordaten reichen weder fuer die Erkennungs- noch fuer die Fehlalarmaussage. |
| Entscheidungsschwelle | MISSING - kein Artefakt beziffert eine akzeptable Fehlalarm- oder Nichterkennungsrate. Vor Gate D zu entscheiden, gemeinsam mit der Claim-Freigabe. |
| Konsequenz bei unzureichender Evidenz | Die Sturzerkennung bleibt vollstaendig deaktiviert. Eine Teilaktivierung mit unbekannter Fehlalarmquote ist ausgeschlossen, weil sie genau die Sicherheitserwartung erzeugt, die CAN-073 verbietet. |

---

### REQ-032 — Wearables und Bike-Sensorik

| Feld | Wert |
|---|---|
| Trace ID | TRC-032 |
| Vision Item | **MISSING — BLOCKER.** Kein VIS-Item trägt die Aussage „vollständige und erklärbare Trainingsdaten“. **VIS-005 ist am 2026-07-19 als Anker entfernt worden**, nicht nur kommentiert: es formuliert eine **Freigabebedingung** („erst nach nachgewiesener Datenqualität … freischalten“), keine Zusage über die Vollständigkeit der Signalbasis. Ebenfalls geprüft und verworfen: **VIS-007** betrifft die **Erklärbarkeit der Health-Auswertung**, nicht die **Vollständigkeit** der Signale; **VIS-003** meint die eigene Aufzeichnung, nicht externe Sensorsignale. Beides sind Beinahe-Treffer und werden **nicht umgedeutet** — das wäre derselbe Defekt wie VIS-009 ↔ REQ-014. |
| Canvas Item (atomar) | **CAN-022** (Problem, `active` seit 2026-07-19), CAN-069 (Capability „Wearable-Anbindung"), CAN-052, CAN-137, **CAN-029** (Wertversprechen — siehe Prüfung unten) |
| Wertanker CAN-029 — durchgeführte Einzelprüfung (2026-07-20) | **Ergebnis: der Anker TRÄGT — als belegter Enabler, nicht als Schlusskette.** Der bisherige Glossentext lautete „(Datenqualität für Belastungsverständnis)"; das war eine **eigene Kurzformel des Traceability-Owners** und stand so in keinem Item — genau die Form, in der die verbotene Kette „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" auftrat. **Der Unterschied, der hier den Ausschlag gibt:** das Zwischenglied ist **keine Ableitung von mir**, sondern steht **wörtlich im kanonischen Wortlaut von CAN-022** — dem Problem-Item **desselben** Requirements: „… Dadurch werden **Belastungsanalyse**, sportartspezifische Auswertung und **erklärbare Empfehlungen** weniger vollständig und weniger zuverlässig." CAN-029 ist „Verstehe deine **Belastung** (erklärbare Trainingsorientierung)". Die Verbindung ist damit **innerhalb der eingefrorenen Registry textlich geschlossen**, nicht durch eine plausible Lesart überbrückt. **Umfang der Aussage, präzisiert statt übernommen:** REQ-032 zahlt auf **Vollständigkeit und Zuverlässigkeit** von CAN-029 ein, **nicht auf dessen Existenz**. **Gegenargument, ausdrücklich festgehalten:** CAN-029 ist auch ohne jede Wearable-Anbindung erfüllbar (Score aus Telefon-GPS und Health-Plattform, REQ-010/REQ-013), und REQ-032 kann fehlerfrei sein, während CAN-029 scheitert. Die beiden Aussagen sind also **nicht identisch** — deshalb bleibt CAN-029 **sekundärer Wertanker**, während **CAN-022** der primäre Problem- und **CAN-069** der primäre Capability-Anker ist. |
| Persona | **USER-004** (**primär**) — „Ambitionierte Ausdauersportler:innen mit Wearables oder externen Sensoren“. Die Verknüpfung trägt **unmittelbar**: das Requirement handelt von Apple Watch, Wear OS und Bike-Sensorik, USER-004 ist über genau diesen Gerätebesitz definiert. `source_type` **ASSUMPTION**, unbestätigt. |
| Primäre Verankerung (Nutzerentscheidung 2026-07-19) | REQ-032 ist primär verankert an **USER-004**, **CAN-022** und einem **Vision-Item zu vollständigen und erklärbaren Trainingsdaten**. Zwei der drei Anker existieren, der dritte nicht: Persona **vorhanden** (ASSUMPTION) · Canvas-Problem **vorhanden und inhaltlich entschieden** (ASSUMPTION) · Vision-Item **MISSING — BLOCKER**. |
| Acceptance Criterion | AC-032 — Zu REQ-032 — Then: Status und Messwerte bleiben zwischen Geräten konsistent und nicht unterstützte Kombinationen sind klar benan… |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | Sync-Konsistenz zwischen Wearable/Sensor und Telefon: Abweichung der Kernmetriken (Dauer, Distanz, Herzfrequenz, bei Bike zusaetzlich Trittfrequenz und Geschwindigkeit) zwischen den Geraeten, Anteil Start-/Stopp-Kommandos, die auf beiden Seiten denselben Zustand erzeugen, Verbindungsabbruchrate je Geraetekombination, Anzahl im Release freigeschalteter Kombinationen ohne Eintrag in der Kompatibilitaetsmatrix. Getrennt gefuehrt: Apple Watch und Wear OS im Run-Fall, Bike-Sensorik im Ride-Fall - die Geraetematrix ist damit selbst sportspezifisch. |
| Target / Pass Condition | AC-032 als Pass/Fail: Status und Messwerte bleiben zwischen Geraeten konsistent, nicht unterstuetzte Kombinationen sind klar benannt, und 0 Kombinationen werden ohne Eintrag in der dokumentierten Kompatibilitaetsmatrix freigeschaltet. Eine zulaessige numerische Metrikabweichung zwischen Geraeten ist MISSING - ohne Toleranz ist 'konsistent' nicht verifizierbar. OQ-003 (Minimum iOS/Android und Referenzgeraete) ist offen; ohne Geraetefestlegung ist die Matrix nicht abschliessbar. |
| Measurement Window | Je Geraetekombination mindestens ein vollstaendiger Aktivitaetsdurchlauf vor Gate E; Wiederholung bei jedem OS- oder Firmware-Sprung einer gelisteten Kombination. |
| Evidence Needed | EV-032 — Gerätematrix und reale Integrationstests. |
| Evidence Source | EV-032 (Geraetematrix und reale Integrationstests); Mindestklasse production-verified - Apple Watch, Wear OS und Bike-Sensorik sind ausschliesslich mit echter Hardware belegbar. |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Dokumentierte Rollenreferenz zur gekoppelten Frage OQ-003 ('Engineering/QA') - das ist der Owner der Frage, nicht der REQ-Owner. |
| Release Gate | GATE-E |
| Status | **broken** (Vision-Anker MISSING) · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | production-verified — Apple Watch, Wear OS und Bike-Sensorik sind ausschließlich mit echter Hardware belegbar. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-003 · **Canvas-BLOCKER geschlossen (2026-07-19):** ~~CAN-022 ist reserviert und inhaltlich MISSING~~ → CAN-022 ist `active`: *„Ohne Anbindung bereits genutzter Sportuhren und externer Sensoren fehlen oder verschlechtern sich zentrale Trainingssignale wie Herzfrequenz, Kadenz, Geschwindigkeit, Leistung und Höheninformationen. Dadurch werden Belastungsanalyse, sportartspezifische Auswertung und erklärbare Empfehlungen weniger vollständig und weniger zuverlässig.“* Item Type **PROBLEM**, Release Gate **E**. Der Wearable-Bezug erscheint damit erstmals als **Problem** und nicht nur als Capability. · **Zielgruppen-BLOCKER geschlossen:** ~~CAN-025 ohne PRD-USER-ID~~ → **USER-004**. · **BLOCKER, die bleiben:** (1) **kein Vision-Anker** — und anders als bei REQ-038/REQ-039 ist hier **nicht einmal eine VIS-ID reserviert**; es ist eine MISSING-Position, keine reservierte Leerstelle. (2) **beide vorhandenen Anker sind unbestätigt** (USER-004 und CAN-022 tragen ASSUMPTION). · **Ausdrücklich NICHT in CAN-022 enthalten:** der Komfortaspekt *„Nutzer müssen zusätzlich das Telefon mitführen“*. Er ist eine **separate mögliche Convenience-Aussage**, erhält in diesem Lauf **keine ID** und wird hier weder hineingelesen noch als abgedeckt behandelt — **OPEN QUESTION**. |
| Rationale | REQ-032 misst Synchronisationsqualität und Geräteabdeckung, also Betriebsqualität — nicht Wearable-Guidance (das wäre REQ-033, Coach). Deshalb OPERATIONAL_QUALITY statt RESEARCH_HYPOTHESIS. `source_type` MISSING, weil die entscheidende Größe — die zulässige Metrikabweichung zwischen Geräten — nirgends beziffert ist und OQ-003 die Geräteliste offen lässt. **Nebenbefund entfallen:** der frühere Verweis auf die „ambitionierte“ Persona als im PRD MISSING ist durch USER-004 überholt und wurde nicht stehen gelassen. |

---

### REQ-033 — Coach, Recovery, Wetter und Zyklus unter Claims-Gate

| Feld | Wert |
|---|---|
| Trace ID | TRC-033 |
| Vision Item | VIS-007 — Health-first Boundary: Health-Ausgaben sind Orientierung, keine Diagnose. Score und Empfehlungen müssen Datenb |
| Canvas Item (atomar) | CAN-070, CAN-102, CAN-072, CAN-137, CAN-029 |
| Acceptance Criterion | AC-033 — Zu REQ-033 — Then: Empfehlung nennt Gründe, Grenzen und Datenbasis; sensible Funktionen sind Opt-in und vollständig deaktivierba… |
| Measurement Type | **RESEARCH_HYPOTHESIS** |
| Signal / Control Evidence | Vor dem Gate ausschliesslich Kontroll- und Forschungssignale, kein Nutzersignal: Anteil erzeugter Empfehlungen, die vollstaendig auf die freigegebene Claims-Whitelist abbilden (Claims-Lint), Anteil Empfehlungen mit ausgewiesener Datenbasis, Gruenden und Grenzen, Anzahl Ausgaben nach einem Opt-out, Vorliegen von Rechtsfreigabe und Privacy-Review als dokumentierte Kontrollnachweise. Nach dem Gate zusaetzlich die Regelguete gegen reale Verlaufsdaten, getrennt fuer Run und Bike, weil Regenerationsbedarf und Hitze-/Trinkempfehlung an sportspezifischer Belastungsdauer und Intensitaet haengen. |
| Target / Pass Condition | Freigabebedingung EXPLICIT als Pass/Fail mit Nullschwelle: ohne juristische Claims- und Privacy-Freigabe erscheint keine dieser Funktionen - 0 sichtbare Empfehlungen vor der Freigabe; 0 Ausgaben nach Opt-out. Die Whitelist selbst ist MISSING (OQ-006), damit ist die inhaltliche Pruefschwelle heute nicht bezifferbar. Zusaetzlicher offener BLOCKER: Zyklusdaten sind eine besondere Datenkategorie ohne dokumentierte Rechtsgrundlage im Canvas (docs/traceability.md, Befund REQ-033). |
| Measurement Window | Claims-Lint und Opt-out-Kontrolle bei jedem CI-Lauf; Rechtsfreigabe und Privacy-Review je Funktionsgruppe (Recovery, Coach, Hitze/Trinken, Zyklus) einzeln vor Gate E; Regelguete nach Freischaltung je Vier-Wochen-Fenster. |
| „Privacy-Review" — Befund Runde 6 (2026-07-20), **Wortlaut unverändert** | **Ein querschnittlicher, gate-blockierender Privacy-Review je Funktionsgruppe ist in keiner der vier Quellen belegt.** Volltextsuche über `docs/sources/`: „Privacy-Review", „Privacy Review", „Datenschutz-Review", „Datenschutzprüfung" und „Privacy-Matrix" ergeben **je 0 Treffer**; das Wort „Datenschutz" kommt in **keiner** der vier Quellen vor. Wortnah belegt sind ausschließlich **datenklassengebundene Einzelprüfungen**: `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md:629` „17.4 **Zyklus-bewusst** (Opt-in, sensibelste Datenklasse, **eigene Privacy-Prüfung**)" — an Task 17.4 und die Datenklasse Zyklus gebunden — und `:715` „… **DSGVO-Prüfung in 10.2**" für serverseitig verarbeitete Gesundheitsdaten. Die **Verallgemeinerung** dieser beiden Einzelprüfungen auf einen Abnahmevorgang „je Funktionsgruppe" nimmt keine Quelle vor. Betroffen sind in dieser Datei die Felder `Signal / Control Evidence`, `Measurement Window` und **Forschungsplan Stufe 3**; der Zyklus-Anteil bleibt über `SRC-003:629` gedeckt. ⚠️ **Warum der Wortlaut hier trotzdem nicht geändert wurde — zwei Gründe.** (1) Die Messfelder dieser Datei sind nach §0 **wörtlich** aus der `canonical_file` `docs/prd/…prd.md` übernommen; eine einseitige Umformulierung erzeugte eine Divergenz zum PRD statt sie aufzulösen. Der Nachzug gehört dem PRD-Owner und ist in §9 eingetragen. (2) **Die Gegenprüfung des zugrunde liegenden Befunds zeigt in drei verschiedene Richtungen:** eine Linse will „Privacy-Review" auf die belegte Datenklassen-Prüfung verengen, eine zweite hält den Begriff für lineage-echt und stattdessen die Bezeichnung „Privacy-Matrix" für das Anhängsel ohne Herkunft, eine dritte will beides trennen. **Bei drei einander widersprechenden Korrekturvorschlägen wäre jede Umsetzung eine Auslegung** — sie unterbleibt und der Befund steht offen. **Zeilenstatus, `canvas-risk-status` und Gate-Zuordnung bleiben unverändert.** |
| Evidence Needed | EV-033 — Claims-Lint, Rechtsfreigabe und Privacy-Test. |
| Evidence Source | EV-033 (Claims-Lint, Rechtsfreigabe und Privacy-Test); Mindestklasse real-boundary-smoke fuer die regelbasierte Empfehlung samt Wetter-Netzwerkgrenze; die Freigabe selbst bleibt ein separater, dokumentierter Rechtsnachweis. RISK-008 (Health-Score als medizinische Aussage) und RISK-022 (sensitive Health-Daten serverseitig) sind offen. |
| Source Type | MISSING |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Dokumentierte Rollenreferenz zur gekoppelten Frage OQ-006 ('Product/Legal') - das ist der Owner der Frage, nicht der REQ-Owner. Fuer Zyklusdaten fehlt zusaetzlich eine benannte Privacy-Verantwortung. |
| Release Gate | GATE-E |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | blocked |
| evidence-class-required | real-boundary-smoke — Regelbasierte Empfehlung plus Wetter-Netzwerkgrenze; Freigabe bleibt separat (siehe blocked). |
| Risiko | RISK-008, RISK-022 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-006 |
| Rationale | Recovery und Coach sind in der Aufgabenstellung ausdruecklich der RESEARCH_HYPOTHESIS zugeordnet: die Regeln sind unvalidiert und zugleich rechtlich gesperrt. Requirement-spezifische Nichtanwendbarkeit eines Nutzersignals vor dem Gate: solange die Funktionen nicht erscheinen duerfen, kann es definitionsgemaess kein Nutzungssignal geben - ein Zielwert dafuer waere erfunden. docs/traceability.md fuehrt REQ-033 bereits als 'blocked'. |
| Befund | Das PRD macht die juristische Claims- und Privacy-Freigabe zur Vorbedingung; OQ-006 (Claims-Whitelist) ist offen. Zusätzlich sind Zyklusdaten eine besondere Datenkategorie ohne dokumentierte Rechtsgrundlage im Canvas. Register: RISK-008. |

**Forschungsplan (RESEARCH_HYPOTHESIS)**

| Feld | Inhalt |
|---|---|
| Hypothese | Regenerations-, Coach-, Hitze-/Trink- und Zyklusfunktionen lassen sich regelbasiert so formulieren, dass sie erklaerbar, optional, vollstaendig deaktivierbar und juristisch freigegeben sind - ohne die Grenze zum Medizinprodukt (CAN-072) zu ueberschreiten. |
| Plan | Stufe 1: Claims-Whitelist erstellen und rechtlich freigeben lassen (OQ-006). Stufe 2: Regelsatz je Funktionsgruppe gegen reale Verlaufsdaten pruefen, mit ausgewiesener Datenbasis und Unsicherheit. Stufe 3: Privacy-Review je Funktionsgruppe, fuer Zyklusdaten mit eigener Rechtsgrundlage. Stufe 4: Claims-Lint als CI-Regel, die jede nicht gelistete Formulierung blockiert. |
| Fixtures / reale Testdaten | Reale Belastungs-, Health- und Wetterverlaeufe ueber mindestens mehrere Wochen je Nutzer, getrennt nach Sportart; Fixture-Faelle fuer Grenzsituationen (Hitze, Uebertraining, Datenluecken). |
| Entscheidungsschwelle | MISSING - die Claims-Whitelist (OQ-006) existiert nicht, und fuer die Regelguete ist keine Schwelle definiert. Beides vor Gate E zu entscheiden. |
| Konsequenz bei unzureichender Evidenz | Alle vier Funktionsgruppen bleiben unsichtbar und deaktiviert. Eine Teilfreischaltung ohne Rechtsfreigabe ist ausgeschlossen; CAN-137 sperrt nicht freigegebene medizinische Claims ausdruecklich. |

---

### REQ-034 — Security, Datenschutz und Datenminimierung

| Feld | Wert |
|---|---|
| Trace ID | TRC-034 |
| Vision Item | VIS-009 — Privacy Boundary: Profile sind standardmäßig privat; Live-Standort ist pro Aktivität Opt-in, zeitlich begrenzt |
| Canvas Item (atomar) | CAN-084, CAN-088, CAN-092, CAN-095, CAN-105 |
| Acceptance Criterion | AC-034 — Zu REQ-034 — Then: Zugriff folgt Berechtigung und Zweckbindung; nicht benötigte sensible Daten verlassen das Gerät nicht. |
| Measurement Type | **COMPLIANCE_CONTROL** |
| Signal / Control Evidence | Kontrollierter Nachweis: Anteil Datenzugriffe, die durch Row-Level-Security-Tests abgedeckt sind; Anzahl Endpunkte ohne Rate Limit oder ohne serverseitige Validierung; Nachweis funktionierenden Datenexports und funktionierender Loeschung; Anzahl Datenfluesse, in denen Roh-Health-Verlaeufe ohne nachgewiesene Notwendigkeit das Geraet verlassen; Bundle-Scan auf Secrets im Client, ab A0 einschliesslich des Routing-Provider-Keys. |
| Target / Pass Condition | AC-034 als Pass/Fail mit 100-%-Abdeckung des Datenflussdiagramms und Nullschwellen: Zugriff folgt Berechtigung und Zweckbindung; 0 Secrets im Client (NFR-007, ab A0 auch fuer den Routing-Proxy-Key, CAN-092); 0 Endpunkte ohne Rate Limit und serverseitige Validierung; nicht benoetigte sensible Daten verlassen das Geraet nicht. OFFEN (CONTRA-006): welche REQ-034-Klauseln - Rate Limits, Logging, Retention, Auftragsverarbeitung, EU-Hosting - bereits ab A0 fuer den Routing-Proxy gelten, ist nicht entschieden; CAN-095 praezisiert local-first, schliesst die Frage aber nicht. Retentionsfristen sind MISSING (OQ-009). |
| Measurement Window | Bundle-Scan und Proxy-Kontrollen bei jedem Build ab A0; RLS- und Rate-Limit-Tests bei jedem CI-Lauf ab Stufe B; Security-Review und Datenflussdiagramm vor jedem Gate von A0 bis E; Loeschungsnachweis je Release-Stufe mit Accountfunktion. |
| Evidence Needed | EV-034 — Security-Review, RLS-Tests, Datenflussdiagramm und Löschungsnachweis. |
| Evidence Source | EV-034 (Security-Review, RLS-Tests, Datenflussdiagramm und Loeschungsnachweis); Mindestklasse production-verified - RLS, Rate Limits und Loeschung sind nur gegen die echte Instanz beweisbar, ein Mock kann keine Policy widerlegen (docs/traceability.md). RISK-007 (Client-API-Key wird missbraucht) und RISK-022 (sensitive Health-Daten serverseitig) sind offen. |
| Source Type | EXPLICIT |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Zusaetzlich offen: OQ-005 ('Engineering') fuer EU-Hosting und Backend, OQ-009 ('Privacy/Product') fuer Retention. Fuer den A0-Routing-Proxy existiert keine benannte Betriebsverantwortung, obwohl er ab A0 personenbezogene Wegpunkte verarbeitet. |
| Release Gate | GATE-A0 (Bundle-Scan, Secret- und Proxy-Kontrollen ab A0) und fortlaufend bis GATE-E |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | risk-introduced |
| evidence-class-required | production-verified — RLS, Rate Limits und Löschung sind nur gegen die echte Instanz beweisbar; ein Mock kann keine Policy widerlegen. |
| Risiko | RISK-007, RISK-015, RISK-022 |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-005, OQ-009 · Widersprüche: CONTRA-006 · **Canvas-BLOCKER:** CAN-018 (Datenschutzproblem) ist reserviert und inhaltlich MISSING - REQ-034 hat keinen atomaren Canvas-Problembezug; Datenschutz erscheint nur als Constraint (CAN-088) und Risiko (CAN-105). |
| Rationale | Datenschutz, Secret Management und Security sind in der Aufgabenstellung ausdruecklich als COMPLIANCE_CONTROL-Faelle genannt; sie brauchen bewusst kein Nutzersignal, weil die Wirksamkeit einer Zugriffsregel unabhaengig davon ist, wie viele Nutzer sie beruehren. Sportspezifische Trennung ist requirement-spezifisch nicht anwendbar: Zugriffsregeln, Rate Limits und Loeschung wirken auf denselben Datenbestand unabhaengig von der Sportart - allerdings faellt bei Bike typischerweise mehr Sensorik an (REQ-024), was die Datenminimierungspruefung sportabhaengig macht und deshalb je Sportart einmal durchlaufen wird. |
| Befund | Der A0-Routing-Proxy verarbeitet Start- und Wegpunktkoordinaten **serverseitig ab A0**, während CAN-131 A0 als lokale Stufe beschreibt. **CONTRA-006: `status = resolved`, `evidence_status = pending`, `blocking = true`** (abgeleitet, `blocked_gates = [A0]`, `blocked_activities = [field-test, release]`, `evidence_gate = A0` — §7.0.1). Die Datenfluss-, Logging-, Retention-, Transport-, EU- und Fehlerbehandlungsregeln sind durch die Nutzerentscheidung vom 2026-07-19 festgelegt (siehe §7), die zugehörige Evidence setzt jedoch lauffähigen Code voraus und steht vollständig aus. Blockierend für die A0-Routing-Implementierung. *Die Vorfassung dieses Feldes trug hier den Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` — als `status` unzulässig (Registry §3.1), deshalb auf die zwei Achsen aufgeteilt.* Register: RISK-007, RISK-015, RISK-022. |

---

### REQ-035 — Evidence Ledger und Definition of Done

| Feld | Wert |
|---|---|
| Trace ID | TRC-035 |
| Vision Item | VIS-010 — Delivery Principle: Kein komplexes Community-, Territory- oder Safety-System wird vor dem Evidence-Gate der vo |
| Canvas Item (atomar) | CAN-123, CAN-111, CAN-114, CAN-038 |
| Acceptance Criterion | AC-035 — Zu REQ-035 — Then: Status wird nur bei vollständiger Evidence auf done gesetzt; fehlende Nachweise bleiben sichtbar. |
| Measurement Type | **COMPLIANCE_CONTROL** |
| Signal / Control Evidence | Kontrollierter Nachweis, bewusst ohne Nutzersignal: Anteil auf 'done' gesetzter Tasks und Gates mit vollstaendigem Evidence-Ledger-Eintrag; Anzahl Ledger-Eintraege, in denen bei sportabhaengigen Requirements Run und Bike getrennt nachgewiesen sind; Anzahl CI-Laeufe, in denen die Regel einen echten Verstoss blockiert hat; Anzahl Ledger-Eintraege mit offenen Findings, die dennoch auf 'done' stehen. |
| Target / Pass Condition | AC-035 als Pass/Fail mit 100-%-Abdeckung: kein Task und kein Gate erhaelt 'done' ohne vollstaendigen Ledger-Eintrag mit automatisierten Tests, realen Geraetetests, getrenntem Run- und Bike-Nachweis, offenen Punkten und Messwerten; 0 Eintraege auf 'done' mit unbeantworteten Pflichtfeldern. Die CI-Regel muss in der echten Pipeline mindestens einen echten Verstoss blockiert haben, sonst ist sie unwirksam (docs/traceability.md). |
| Measurement Window | Je Task-Abnahme und je Gate, fortlaufend von P0 bis Gate E; CI-Regel bei jedem Pipeline-Lauf. |
| Evidence Needed | EV-035 — CI-Regel, Ledger-Review und Gate-Checkliste. |
| Evidence Source | EV-035 (CI-Regel, Ledger-Review und Gate-Checkliste); Mindestklasse real-boundary-smoke - die CI-Regel muss in der echten Pipeline einen echten Verstoss blockieren, sonst ist sie nicht wirksam. Datei: docs/EVIDENCE-LEDGER.md. BEFUND: der Ledger enthaelt derzeit ausschliesslich einen Template-Platzhalter mit REQ-000/AC-000/EV-000; diese sind keine echten IDs und muessen als Platzhalter kenntlich bleiben, sonst erzeugt die Referenzpruefung Fehlalarme. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Gerade dieses REQ ist ohne benannten Abnehmer nicht durchsetzbar, weil 'done' eine Personenentscheidung ist. |
| Release Gate | GATE-A0 bis GATE-E (PRD Release A0-E), wirksam bereits ab P0 |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — Die CI-Regel muss in der echten Pipeline einen echten Verstoß blockieren, sonst ist sie nicht wirksam. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002 |
| Rationale | REQ-035 ist ein Prozess- und Nachweisrequirement; sein Erfolg zeigt sich ausschliesslich in kontrollierten Nachweisen. Requirement-spezifische Nichtanwendbarkeit eines Nutzersignals: REQ-035 hat laut Canvas keinen unmittelbaren Nutzerkontakt und ist eine von genau zwei Prozessanforderungen ohne Nutzerproblem; ein Retentions- oder Nutzungsziel fuer 'Evidence-Ledger-Disziplin' waere ein Kategorienfehler. Requirement-spezifische Sport-Nichtanwendbarkeit gilt nicht: der Ledger muss Run und Bike gerade getrennt fuehren (CAN-114), das ist selbst Pruefgegenstand. |

---

### REQ-036 — Store- und Release-Gates

| Feld | Wert |
|---|---|
| Trace ID | TRC-036 |
| Vision Item | VIS-010 — Delivery Principle: Kein komplexes Community-, Territory- oder Safety-System wird vor dem Evidence-Gate der vo |
| Canvas Item (atomar) | CAN-083, CAN-108, CAN-085, CAN-086, CAN-122, CAN-038 |
| Acceptance Criterion | AC-036 — Zu REQ-036 — Then: Kein Release wird ohne vollständige Nachweise und Policy-Abnahmen veröffentlicht. |
| Measurement Type | **COMPLIANCE_CONTROL** |
| Signal / Control Evidence | Kontrollierter Nachweis, bewusst ohne Nutzersignal: Anteil Release-Stufen mit vollstaendig ausgefuellter Policy-Matrix fuer iOS und Android; Vorliegen der Berechtigungsbegruendungen fuer Background-Location und Health; Vollstaendigkeit der Datenschutzangaben im Store-Eintrag; Nachweis eines durchlaufenen Testtracks (TestFlight beziehungsweise Play Internal); Vorliegen des Gate-Sign-offs der vorherigen Stufe; Anzahl Store-Ablehnungen und deren Gruende. |
| Target / Pass Condition | AC-036 als Pass/Fail mit 100-%-Abdeckung: kein Release ohne vollstaendige Nachweise und Policy-Abnahmen; jede Stufe startet erst nach dem Sign-off des vorherigen Gates - 0 uebersprungene Gates. Fuer GATE-A2 zusaetzlich blockierend: der finale oeffentliche Name ist MISSING (OQ-001), CAN-090 verlangt die Markenpruefung vor der Finalisierung. |
| Measurement Window | Je Release-Stufe vor Veroeffentlichung (A0, A1, A2, B, C, D, E); Policy-Matrix zusaetzlich bei jeder Aenderung an Berechtigungen oder Datenkategorien. |
| Evidence Needed | EV-036 — TestFlight/Internal-Test-Bericht, Policy-Matrix und Gate-Sign-off. |
| Evidence Source | EV-036 (TestFlight-/Internal-Test-Bericht, Policy-Matrix und Gate-Sign-off); Mindestklasse production-verified - Testtracks und die Review-Entscheidung sind externe Realbedingungen (docs/traceability.md). RISK-010 (Store lehnt Background-Location/Health/UGC ab) ist kritisch und offen; RISK-011 (Namens-/Markenkollision) ebenfalls. |
| Source Type | **ASSUMPTION** — herabgestuft im PRD-Nachaudit (§2.1); die Vorfassung dieser Zeile trug `EXPLICIT`. |
| Owner | OWNER-BLOCKER (MISSING): kein benannter DRI. OQ-002 ist offen; PRD-Kopfzeile 'Owner' = MISSING. Zusaetzlich offen: OQ-001 (oeffentlicher Name, 'Product/Legal') blockiert GATE-A2. Ein Gate-Sign-off ohne benannten Zeichnungsberechtigten ist nicht erteilbar. |
| Release Gate | GATE-A0 bis GATE-E (PRD Release A0-E); jede Stufe ist ihr eigener Pruefpunkt |
| Status | linked · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | production-verified — TestFlight-/Play-Internal-Tracks und die Review-Entscheidung sind externe Realbedingungen. |
| Risiko | RISK-010, RISK-011 |
| Offene Entscheidung | offene Fragen: OQ-001, OQ-002 |
| Rationale | Store- und Release-Gates sind in der Aufgabenstellung ausdruecklich als COMPLIANCE_CONTROL-Fall genannt. Requirement-spezifische Nichtanwendbarkeit eines Nutzersignals: REQ-036 ist die zweite der beiden Prozessanforderungen ohne unmittelbares Nutzerproblem (Canvas-Anker CAN-083); Downloads oder Bewertungen als Zielwert waeren ein Kategorienfehler, weil sie ueber die Policy-Konformitaet nichts aussagen. Die Sporttrennung bleibt mittelbar relevant, weil die Gate-Exit-Evidenz laut PRD reale Run- und Bike-Aktivitaeten je Plattform verlangt. |

---

### REQ-037 — Accessibility

> **Nachfolger 1 von 2 für das deprecatete REQ-014.** Prüft ausschließlich die **Zugänglichkeit**;
> die Gestaltungssprache liegt bei REQ-038.

| Feld | Wert |
|---|---|
| Trace ID | **TRC-037** |
| Vision Item | **VIS-011 — Accessibility Boundary:** Jeder ausgelieferte Screen muss ohne Farbunterscheidung, mit vergrößerter Schrift und mit Screenreader vollständig bedienbar sein; Zugänglichkeit ist eine Schranke, keine Quote. · **Source Type des Ankers: ASSUMPTION, unbestätigt** — VIS-011 ist neue Produktsubstanz auf Vision-Ebene, inhaltlich aus REQ-014/AC-014/NFR-005 abgeleitet, vom Nutzer aber nie als Vision-Aussage bestätigt. Er **zählt bis zur ausdrücklichen Nutzerbestätigung NICHT als erfüllter Vision-Anker** (Registry §8 Punkt 15). |
| Canvas Item (atomar) | **CAN-099** (`active`, Item Type **CONSTRAINT / VALUE BOUNDARY**, und **ausschließlich** Accessibility). **Kanonischer Wortlaut, nachgezogen 2026-07-20 (Runde 6):** „Die mobile Anwendung muss für Menschen mit unterschiedlichen visuellen, motorischen und assistiven Anforderungen bedienbar sein. Dazu gehören WCAG 2.2 AA, Screenreader-Unterstützung, skalierbare Schrift, ausreichende Bedienflächen, nachvollziehbare Fokusführung und die Regel, dass Farbe niemals der einzige Informationsträger ist." |
| CAN-099 — Nachzug Runde 6 (2026-07-20), **Nutzerauftrag Punkt 3** | **(a) Web-Erstreckung entfernt.** Die Vorfassung lautete „Die mobile Anwendung **und ihre nutzbaren Web-Auskopplungen** müssen …". **Keine der vier Quellen erstreckt die Accessibility-Pflicht auf Web-Artefakte.** Alle vier Vorkommen von „Web-Auskopplung" liegen in `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md:83`, `:484`, `:711`, `:735` und betreffen **ausnahmslos** die CSS-Farbmisch-/Transparenzregel; der einzige Accessibility-Abschnitt aller vier Quellen (`SRC-003:98-102`) nennt Web **nicht** und schließt mit einer reinen iOS/Android-Zeile. Die Kette „die Farbregel gilt für Web, **also** auch die Accessibility-Pflicht" ist eine Ableitung über ein Zwischenglied und damit kein Beleg. ⚠️ **Ausdrücklich NICHT der Grund — Korrektur aus der Gegenprüfung:** die Streichung erfolgt **nicht**, weil die Quellen Web-Artefakte verneinten. Sie bejahen sie: `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md:132` lautet „kein Web-Client (**außer Beschützer-Link**)", `:238` führt „L-03 \| Beschützer-Modus: **Web-Link** für Vertrauensperson (ohne Account) …" als Lieferitem, ebenso `SRC-002-REVYR-Plan-PRD.md:109` und `SRC-003:605`; `SRC-003:83` benennt drei Web-Auskopplungen namentlich. **Es liegt ein reiner Belegmangel vor, kein Widerspruch.** **(b) Nicht belegte Accessibility-Details bleiben stehen** — ebenfalls Nutzerauftrag Punkt 3. Ungedeckt und als ASSUMPTION zu lesen sind: die **Fassungsziffer „2.2"** (alle vier WCAG-Vorkommen — `SRC-001:176`, `SRC-001:256`, `SRC-002:134`, `SRC-003:100` — nennen „WCAG AA" **ohne** Fassung), **„ausreichende Bedienflächen"**, **„nachvollziehbare Fokusführung"** sowie **„motorischen und assistiven Anforderungen"** (Volltextsuche über `docs/sources/`: „Bedienfläche", „Fokusführung", „motor", „assistiv", „barrierefrei" ergeben **je 0 Treffer**). **(c) Nicht entschieden, weil nicht dieser Owner:** der `source_type` von CAN-099 selbst. Er steht laut Canvas auf `EXPLICIT`, weil der Nutzer den Wortlaut gesetzt hat, **ohne** dass eine ausdrückliche Gegenbestätigung vorliegt — **BLOCKER Registry §8 Punkt 43 bleibt bestehen und wird hier nicht geschlossen.** Die Angabe ist aus dieser Zeile entfernt statt fortgeschrieben, damit die Matrix keinen fremden Feldwert behauptet. **REQ-037 selbst bleibt davon unberührt `ASSUMPTION`.** **(d) Atomarer Nachzug erforderlich:** dieselbe Streichung ist in `docs/canvas/…canvas.md`, `docs/prd/…prd.md` (REQ-037-Text und AC-037 `Given`), `docs/EVIDENCE-LEDGER.md` (EV-037) und `docs/prd/…prd.md` (NFR-005 `signal`) nachzuziehen. **In dieser Datei ist der Nachzug vollständig:** §6.7.8 (NFR-005) führte die Web-Erstreckung nie, geprüft am 2026-07-20. Unterbleibt sie in den anderen Dateien, trägt REQ-037 dort eine Geltungsbereichsklausel **ohne** Canvas-Anker — siehe §9. |
| Canvas-Problem | **MISSING — BLOCKER (2026-07-20).** Der Canvas führt **kein Zugänglichkeitsproblem**. Entfernt wurden **zwei** Verknüpfungen, die beide über die in Registry §6.1.1 ausdrücklich **verbotene** Schlusskette „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" liefen: **CAN-013** in §4.1 und **CAN-029** in §4.2. **Warum sie nicht tragen:** CAN-013 handelt von der **Bedeutungsarmut von Trainingsdaten**, CAN-029 von der **Erklärbarkeit der Belastung**. Keines von beiden sagt etwas darüber aus, ob eine Oberfläche **wahrnehmbar und bedienbar** ist — ein perfekt erklärter Belastungsscore kann für eine Screenreader-Nutzerin vollständig unzugänglich sein. **Es wird kein CAN-Item umgedeutet und keine Problem-ID vergeben;** die reservierten CAN-016…CAN-021 decken Accessibility nicht ab. Registry §8 Punkt 37. |
| NFR | **NFR-005** — trägt seit dem 2026-07-19 REQ-037 statt des deprecateten REQ-014. |
| Acceptance Criterion | **AC-037** — alle fünf Bedingungen **einzeln** erfüllt: (a) WCAG-2.2-AA-Audit bestanden · (b) relevante Screens mit **VoiceOver UND TalkBack** geprüft — beide, nicht „ein Screenreader“ · (c) Dynamic Type bzw. Font Scaling geprüft · (d) keine Information ausschließlich durch Farbe · (e) **dokumentierte** Kontrastprüfung. **iOS und Android getrennt nachzuweisen.** |
| Measurement Type | **COMPLIANCE_CONTROL** (Item Type: CONSTRAINT / COMPLIANCE_CONTROL) |
| Signal / Control Evidence | Kontrollierter Nachweis, bewusst ohne Nutzersignal: Anteil ausgelieferter Screens **der mobilen App**, die die dokumentierte Kontrastprüfung bestehen; Anteil Screens mit vollständiger Screenreader-Bedienbarkeit **getrennt für VoiceOver (iOS) und TalkBack (Android)**; Anteil Screens, die bei aktivem Dynamic Type bzw. Font Scaling ohne Abschneiden oder Überlappung bedienbar bleiben; Anzahl Informationen, die **ausschließlich** durch Farbe transportiert werden; Vollständigkeit und Korrektheit der Fokusführung. *(Runde 6, 2026-07-20: „und aller nutzbaren Web-Auskopplungen" entfernt — Nutzerauftrag Punkt 3, Begründung in der Zeile „CAN-099 — Nachzug Runde 6". „Fokusführung" bleibt stehen und ist als ASSUMPTION zu lesen.)* |
| Target / Pass Condition | AC-037 als Pass/Fail mit 100-%-Abdeckung und Nullschwelle, alle fünf Bedingungen einzeln; **0** Informationen ausschließlich durch Farbe. Kein Prozentziel unterhalb von 100 — die Anforderung ist eine **Schranke, keine Quote**. |
| Measurement Window | Kein zeitbasiertes Fenster — vollständige Abdeckungsprüfung je ausgeliefertem Screen. **Accessibility-Basis ab GATE-A0**, **vollständiger Audit spätestens GATE-A2** vor öffentlichem Store-Release; zusätzlich bei jeder Änderung an Navigationsstruktur, Kontrastwerten oder Screenreader-Labels. iOS und Android **getrennt**, Light und Dark Mode **getrennt**. |
| Evidence Needed | **EV-037** — WCAG-2.2-AA-Audit; VoiceOver- und TalkBack-Durchlauf je Plattform; Dynamic-Type-/Font-Scaling-Prüfung; dokumentierte Kontrastprüfung in Light und Dark Mode. |
| Evidence Source | EV-037; Mindestklasse `real-boundary-smoke` — Screenreader, Dynamic Type und Kontrast sind **ausschließlich real** prüfbar; ein Snapshot-Test kann Bedienbarkeit nicht belegen. `evidence_status` **`not-planned`**: es existiert kein Code, keine CI und kein beauftragter Auditor, also **noch kein Messkonzept**. Bewusst nicht `planned` — das würde ein definiertes, nur noch nicht instrumentiertes Messkonzept behaupten. |
| Source Type | **ASSUMPTION.** Die WCAG-**Fassung** ist seit dem 2026-07-19 mit **2.2** beziffert (CAN-099) — die frühere Lücke „WCAG AA ohne Version“ ist geschlossen und ein Audit überhaupt erst bestehbar. `EXPLICIT` wird trotzdem **nicht** vergeben: es ist in keinem Artefakt eine **Rechtsgrundlage** benannt, die WCAG 2.2 AA für dieses Produkt verbindlich macht (kein Verweis auf EAA, BFSG oder eine Store-Vorgabe). Zusätzlich ist der Wortlaut nicht ausdrücklich nutzerbestätigt. |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Für einen externen WCAG-Audit ist zusätzlich **kein Auditor benannt: MISSING.** |
| Release Gate | **GATE-A0** (Accessibility-Basis) bis **GATE-A2** (vollständiger Audit, spätestens vor öffentlichem Store-Release) |
| Status | **not-linked** · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — Screenreader, Dynamic Type und Kontrast sind ausschließlich real prüfbar. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002, OQ-003 · **Canvas-Capability-BLOCKER geschlossen (2026-07-19):** ~~CAN-099 ist reserviert und inhaltlich MISSING~~ → `active` und ausschließlich Accessibility. · **BLOCKER, NEU 2026-07-20: kein canvas-problem-Anker** (siehe Zeile „Canvas-Problem"; Registry §8 Punkt 37). Der Anker war vorhanden und wurde entfernt, weil er die falsche Aussage trug — **die Lücke ist nicht neu entstanden, sie war nur verdeckt.** · **BLOCKER, der bleibt: VIS-011 zählt NICHT als erfüllter Vision-Anker** (ASSUMPTION, unbestätigt) — der Anker ist *belegt und benannt*, aber nicht *bestätigt*; TRC-037 wird deshalb als `not-linked` geführt. · **BLOCKER, NEU 2026-07-20:** CAN-099 steht auf `source_type EXPLICIT`, weil der Nutzer den Wortlaut am 2026-07-20 als verbindlich gesetzt hat — eine **ausdrückliche Gegenbestätigung liegt nicht vor** (Registry §8 Punkt 43). REQ-037 selbst bleibt davon unberührt `ASSUMPTION`. · **MISSING:** Rechtsgrundlage der WCAG-Verbindlichkeit · Screenreader- und Gerätematrix (OQ-003) · kein benannter Auditor. |
| Rationale | Accessibility ist ein kontrollierter Nachweis mit fester Schranke. **Kein Nutzersignal, requirement-spezifisch begründet:** eine Nutzungsquote von Screenreader-Nutzern könnte WCAG-Konformität weder belegen noch widerlegen und würde einen falschen Anreiz setzen — Verzicht auf Zugänglichkeit bei kleiner Nutzergruppe. **Run/Bike-Trennung anwendbar:** die sportspezifischen Tracking-Screens zeigen unterschiedliche Labels und Kernmetriken, also sind auch die Screenreader-Ausgaben verschieden und je Sportart zu prüfen. |

---

### REQ-038 — Monochromes tokenbasiertes Designsystem

> **Nachfolger 2 von 2 für das deprecatete REQ-014.** Prüft ausschließlich die
> **Gestaltungssprache**; die Zugänglichkeit liegt bei REQ-037.

| Feld | Wert |
|---|---|
| Trace ID | **TRC-038** |
| Vision Item | **VIS-012 — reserved, Inhalt MISSING → BLOCKER.** Kein bestehendes VIS-Item trägt ein Designprinzip auf Vision-Ebene; **VIS-011 deckt ausdrücklich nur die Accessibility-Hälfte ab.** Es wird **kein** VIS-Item umgedeutet — das wäre exakt der Defekt VIS-009 ↔ REQ-014. **TRC-038 wird deshalb bewusst als `broken` geführt**, mit sichtbarer Lücke, statt an ein unpassendes Item gehängt zu werden. |
| Canvas Item (atomar) | **CAN-141** (`active`, Item Type **DESIGN CONSTRAINT / PRODUCT PRINCIPLE**, Source Type **EXPLICIT**). **Kanonischer Wortlaut:** „Die Anwendung verwendet ein tokenbasiertes, überwiegend monochromes Designsystem. Farbe wird nur eingesetzt, wenn sie eine definierte fachliche Bedeutung besitzt: Health-Status, Team- und Revieridentität, Sportplatz-Gold sowie bestätigte Feiermomente. Run und Bike werden nicht ausschließlich durch Farbe unterschieden." |
| Canvas-Problem | **MISSING (begründet) — 2026-07-20.** Entfernt wurden **zwei** Verknüpfungen: **CAN-013** in §4.1 und **CAN-029** in §4.2, letztere über die verbotene Kette „Wahrnehmbarkeit als Vorstufe von Verstehen". **Der CAN-013-Eintrag war zusätzlich in sich widersprüchlich:** er nannte CAN-013 als Anker **und** begründete im selben Feld „kein eigenes Problem-Item — begründete Nichtanwendbarkeit". Beides zugleich kann nicht gelten. Aufgelöst zugunsten der Nichtanwendbarkeit: **eine Gestaltungssprache ist eine Constraint (CAN-141), kein Nutzerproblem** — der Canvas führt zu Recht keines. ⚠️ **Offengelegte Divergenz innerhalb der Registry:** §7.5.5 verlangt für diese Fundstelle den Wert „MISSING (**begründet**)", §8 Punkt 37 zählt REQ-038 dagegen zu den drei Requirements **ohne** canvas-problem-Anker und stuft das als **BLOCKER** ein. Beide sind Registry-Aussagen. Ich folge der **feldbezogenen, spezifischeren** Anweisung aus §7.5.5 für den Wert und führe REQ-038 in §6.1 **trotzdem** mit, damit die BLOCKER-Zählung nicht von der Registry abweicht. Die Divergenz wird **nicht** stillschweigend zugunsten einer Seite aufgelöst. |
| Acceptance Criterion | **AC-038** — (a) Farbe erscheint **ausschließlich** in den vier abschließend definierten fachlichen Bedeutungen · (b) Run und Bike sind **nicht ausschließlich** durch Farbe unterscheidbar · (c) alle Farbwerte stammen aus **Design-Tokens**, keine Inline-Literale. |
| Measurement Type | **COMPLIANCE_CONTROL** |
| Signal / Control Evidence | Kontrollierter Nachweis, bewusst ohne Nutzersignal: **Inventar aller im Produkt verwendeten Farbwerte**, jeweils zugeordnet zu einer der vier zulässigen fachlichen Bedeutungen oder als Verstoß markiert; Anzahl Farbwerte außerhalb der Design-Tokens (Inline-Literale); Anzahl Stellen, an denen Run und Bike **ausschließlich** durch Farbe unterschieden werden. |
| Target / Pass Condition | AC-038 als Pass/Fail mit Nullschwellen: (a) **0** Farbeinsätze außerhalb der vier Bedeutungen **Health-Status**, **Team- und Revieridentität**, **Sportplatz-Gold**, **bestätigte Feiermomente** · (b) **0** Stellen, an denen Run und Bike ausschließlich farblich unterschieden werden · (c) **0** Farbwerte außerhalb der Design-Tokens. **Die Liste der vier Bedeutungen ist abschließend, nicht beispielhaft.** |
| Measurement Window | Kein zeitbasiertes Fenster — vollständige Inventarprüfung. Vor jedem Gate von A0 bis A2 und **bei jeder Änderung der Design-Tokens**; zusätzlich bei jedem neu ausgelieferten Screen. |
| Evidence Needed | **EV-038** — Design-Token-Review: Inventar **aller** Farbwerte gegen die vier zulässigen fachlichen Bedeutungen; Prüfung, dass Run und Bike nicht ausschließlich farblich unterschieden werden; Prüfung auf Farb-Literale außerhalb der Tokens. |
| Evidence Source | EV-038; Mindestklasse `real-boundary-smoke`. `evidence_status` **`not-planned`** — es existiert kein Code, **keine Token-Datei** und kein festgelegtes Prüfverfahren; damit noch kein Messkonzept. |
| Source Type | **EXPLICIT** — und zwar belegt, nicht hochgestuft. Der Anker **CAN-141** trägt `source_type EXPLICIT`, weil das monochrome, tokenbasierte Designsystem mit genau diesen vier Farbbedeutungen eine **ausdrückliche Nutzerangabe vom 2026-07-19** ist. Anders als bei REQ-037 hängt die Pass-Bedingung hier **nicht** an NFR-005 und **nicht** an einer externen Norm, deren Verbindlichkeit unbelegt wäre. |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner“ = MISSING. |
| Release Gate | **GATE-A0 bis GATE-A2** (Release A0-A2), erstmalige Abnahme mit GATE-A0 |
| Status | **broken** (Vision-Anker MISSING) · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — ein Farbinventar über Design-Tokens ist statisch prüfbar, die Frage „wird Run/Bike ausschließlich farblich unterschieden?“ jedoch erst am ausgelieferten Screen. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002 · **BLOCKER: REQ-038 hat KEINEN Vision-Anker** (VIS-012 reserved, Inhalt MISSING). Ein Designprinzip auf Vision-Ebene wäre **neue Produktsubstanz** und braucht eine Nutzerentscheidung; es wird hier weder erfunden noch aus einem bestehenden Item herausgelesen. · **Abgrenzung zu CAN-099 — AUFGEHOBEN am 2026-07-20, nicht umformuliert.** Die frühere Fassung dieses Feldes lautete: „dieselbe Beobachtung, zwei Pflichten — der Satzteil ‚Farbe ist nie der einzige Informationsträger‘ wirkt in CAN-099 als Zugänglichkeitsschranke und in CAN-141 als Gestaltungsregel". **Das war die belegte doppelt geführte Pflicht:** eine Klausel, zwei Items, zwei Nachweise, keine Instanz, die entscheidet, welcher gilt. **Neue Lage (Registry §6.3.3):** die Klausel wird **kanonisch und ausschließlich von CAN-099** getragen und ist aus CAN-141 **entfernt**. Der tragende Grund steht ausdrücklich hier, weil er die alte Begründung widerlegt: die beiden Aussagen fallen **in beide Richtungen** auseinander — ein **monochromes** Produkt kann die Klausel verletzen (zwei Grautöne als einziger Unterschied), ein **farbiges** kann sie erfüllen. Sie sind also **unabhängig**, nicht „dieselbe Beobachtung aus zwei Blickwinkeln". In CAN-141 und damit in AC-038 verbleibt ausschließlich die **engere** Regel „Run und Bike werden nicht ausschließlich durch Farbe unterschieden": ein konkretes Unterscheidungspaar, prüfbar gegen die Design-Tokens. **Es entsteht keine dritte Farbregel.** |
| Rationale | Die Gestaltungsregel ist eine **Schranke mit Nullschwelle** und braucht bewusst kein Nutzersignal: ob Farbe sparsam eingesetzt wird, ist unabhängig davon messbar, wie viele Nutzer den Screen sehen. Ein Ästhetik- oder Zufriedenheitswert wäre ein Kategorienfehler. **Run/Bike-Trennung ist hier selbst Prüfgegenstand,** nicht nur Kontext: die Regel „Run und Bike werden nicht ausschließlich durch Farbe unterschieden“ ist eine der drei Pass-Bedingungen. |

---

### REQ-039 — GPX-Export abgeschlossener Aktivitäten

| Feld | Wert |
|---|---|
| Trace ID | **TRC-039** |
| Vision Item | **VIS-013 — reserved, Inhalt MISSING → BLOCKER.** Prüfung aller bestehenden VIS-Items: **VIS-003** nennt Tracking, Health-Auswertung, Fortschrittssignale und Trainingspartner — **keine Portabilität**; **VIS-009** regelt Sichtbarkeit und Werbenutzung, **nicht die Mitnahme** der eigenen Daten. Kein Item wird umgedeutet. **TRC-039 wird bewusst als `broken` geführt.** |
| Canvas Item (atomar) | **CAN-139** (`active`, Item Type **VALUE PROMISE / CAPABILITY**, Source Type **EXPLICIT** seit 2026-07-20). **Kanonischer Wortlaut:** „Nutzer behalten Kontrolle über ihre aufgezeichneten Aktivitäten und können eine abgeschlossene Run- oder Bike-Aktivität als standardkonforme GPX-Datei exportieren, ohne sie veröffentlichen oder mit anderen Nutzern teilen zu müssen." |
| Wertanker — durchgeführte Einzelprüfung (2026-07-20) | **CAN-030 trägt nicht und ist entfernt; CAN-139 trägt.** **CAN-030** ist „Erkenne deinen **Fortschritt**". Eine GPX-Datei zu exportieren ist kein Fortschrittserlebnis — sie erzeugt weder Vergleich noch Trend noch Rückblick. CAN-030 wurde hier als **Universal-Wertanker** benutzt (es steht zusätzlich bei REQ-008, REQ-015, REQ-016, REQ-025, REQ-027, REQ-029) und hätte jede maschinelle Prüfung als erfüllte Wertreferenz bestanden. **CAN-139 trägt den Wert selbst:** es ist seit dem 2026-07-20 ausdrücklich als **VALUE PROMISE / CAPABILITY** typisiert und sein kanonischer Wortlaut beginnt mit „Nutzer behalten **Kontrolle** über ihre aufgezeichneten Aktivitäten" — das *ist* das Wertversprechen. **Offengelegt statt verdeckt:** dass hier Capability- und Wertanker dasselbe Item sind, ist kein Zirkelschluss, sondern die Folge des dualen Item Types aus Runde 4. Die **Wertversprechen-Gruppe CAN-028…CAN-038 enthält weiterhin kein Portabilitäts- oder Kontrollversprechen** — diese Lücke bleibt bestehen und wird nicht durch die Umbuchung geschlossen. |
| Canvas-Problem | **MISSING — BLOCKER (2026-07-20).** Die Verknüpfung auf **CAN-013** mit der Variante „(Daten, die man nicht mitnehmen kann, bleiben fremdbestimmt)" ist **entfernt**. Es ist dieselbe Defektklasse in anderer Formulierung: CAN-013 als Universal-Problemanker. **Bemerkenswert:** das Feld enthielt bereits selbst den Vermerk „schwacher Bezug, offengelegt … der Canvas führt **kein** Portabilitäts- oder Lock-in-Problem. MISSING" — es stand also **gleichzeitig** eine Verknüpfung und ihre Widerlegung im selben Feld. Eine maschinelle Prüfung liest die Verknüpfung und nicht den Vorbehalt daneben; genau deshalb reichte der Vermerk nicht und der Anker musste weg. Registry §8 Punkt 37. |
| Sekundäre Verknüpfung | **REQ-034** (Constraint) — **ausdrücklich nicht primär.** Die Nutzerentscheidung stellt fest: REQ-034 ist **KEIN ausreichend präziser primärer Anker**; die Erwähnung „Datenexport“ trägt die konkrete Capability „GPX-Datei erzeugen und extern öffnen“ nicht. REQ-034 deckt nur Nutzerkontrolle, Datenportabilität, Datenminimierung und „keine unbeabsichtigten Zusatzdaten“ ab — wirksam in den Kriterien (e), (f) und (h). **Es wird nicht behauptet, REQ-034 allein erfülle den GPX-Export.** |
| Acceptance Criterion | **AC-039** — acht einzeln prüfbare Bedingungen: (a) GPX für abgeschlossene **Run**-Aktivität erzeugt · (b) GPX für abgeschlossene **Bike**-Aktivität erzeugt · (c) Zeitstempel und Koordinatenreihenfolge korrekt · (d) Datei in **mindestens einer definierten** kompatiblen Fremd-App öffenbar · (e) keine Health-Daten unbeabsichtigt exportiert · (f) der Nutzer sieht **vor** dem Export, welche Daten enthalten sind · (g) fehlende oder beschädigte Trackdaten führen zu einem **kontrollierten Fehler** · (h) der Export funktioniert **ohne** Veröffentlichung oder Social-Freigabe. |
| Measurement Type | **OPERATIONAL_QUALITY** (im bestehenden Modell: FUNCTIONAL CONTROL) |
| Signal / Control Evidence | **Getrennt für Run und Bike:** Erfolgsrate der GPX-Erzeugung aus abgeschlossenen Aktivitäten; Anteil erzeugter Dateien, die gegen das GPX-Schema valide sind; Anteil Dateien mit korrekter Zeitstempel- und Koordinatenreihenfolge; Öffnungserfolg in der definierten Fremd-App; **Anzahl Health-Datenfelder im Export (Sollwert 0)**; Anteil Fälle mit fehlenden oder beschädigten Trackdaten, die zu einem kontrollierten Fehler statt zu einem Absturz oder einer stillen Teildatei führen. |
| Target / Pass Condition | AC-039 als Pass/Fail, alle acht Bedingungen einzeln; **0 Health-Daten unbeabsichtigt exportiert**. Eine Nutzungs- oder Exportquote wird **nicht** gesetzt — ein solcher Zielwert wäre erfunden. |
| Measurement Window | Vor **GATE-A2**, spätestens vor öffentlichem v1.0-Release; danach bei jeder Änderung am Exportformat, am Datenmodell oder an den exportierten Feldern. **Je Sportart und je Plattform mindestens ein vollständiger Durchlauf**, zusätzlich je ein Negativtest (beschädigte Trackdaten, Health-Daten-Ausschluss). |
| Evidence Needed | **EV-039** — GPX-Export-Test **je Sportart getrennt**: Erzeugung, Schemakonformität, Zeitstempel- und Koordinatenreihenfolge, Öffnen in einer definierten Fremd-App, **Negativtest auf Health-Daten im Export**, kontrollierter Fehlerfall bei beschädigten Trackdaten, Export ohne Veröffentlichung. |
| EV-039 ↔ EV-008 — kanonische Trennung (verbindlich, 2026-07-20) | **EV-039 ist AUSSCHLIESSLICH der GPX-Kompatibilitäts- und Exportnachweis.** Verlauf und Detailansicht werden **nicht** hier nachgewiesen — das ist **EV-008**. Die frühere Überlappung lief **nicht** über das PRD, sondern über die veraltete EV-008-Definition der **Registry**, die nach Registry §1 bei jeder Prüfung gewonnen und den bereits ausgelagerten Nachweis doppelt geführt hätte. **Prüfregel: Wer einen Verlaufs- oder Detailansichts-Nachweis unter EV-039 findet, hat einen Validierungsfehler gefunden.** |
| Evidence Source | EV-039; Mindestklasse `real-boundary-smoke` — **Kompatibilität ist keine Eigenschaft des eigenen Parsers.** Ein Test, der die eigene Datei mit dem eigenen Code wieder einliest, prüft nur sich selbst. `evidence_status` **`not-planned`**. |
| Source Type | **ASSUMPTION** — der Wortlaut stammt aus der Nutzerentscheidung vom 2026-07-19, ist aber nicht ausdrücklich als Anforderungstext bestätigt. **„GPX“ ist zudem kein konkret zitierter Standard:** weder die **Formatversion** (1.0 / 1.1) noch die Referenzanwendung sind benannt — beides MISSING. |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner“ = MISSING. |
| Release Gate | **GATE-A2**, spätestens vor öffentlichem v1.0-Release |
| Status | **broken** (Vision-Anker MISSING) · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — die GPX-Datei muss in einem **echten Fremdsystem** geöffnet werden; Kompatibilität ist keine Eigenschaft des eigenen Parsers. |
| Risiko | kein Registereintrag im Messmodell referenziert; die Canvas-Risikoanker stehen in der Spalte „Canvas Item (atomar)“ |
| Offene Entscheidung | offene Fragen: OQ-002 · **BLOCKER: kein Vision-Anker** (VIS-013 reserved, Inhalt MISSING). · **BLOCKER, NEU 2026-07-20: kein canvas-problem-Anker** (Registry §8 Punkt 37). · **MISSING — die Referenz-Fremdanwendung ist nicht benannt (OQ-016).** Ohne sie ist AC-039 Kriterium **(d)** nicht reproduzierbar prüfbar: „öffnet in irgendeiner App“ ist keine Bestehensbedingung. **Es wird keine App geraten.** · **MISSING: die GPX-Formatversion.** · **OPEN QUESTION, NEU 2026-07-20 (Registry §8 Punkt 36):** der kanonische CAN-139-Wortlaut nennt die Klausel „**in einer kompatiblen Fremdanwendung öffnen**" **nicht mehr**; AC-039 (d) und EV-039 verlangen den Nachweis weiterhin. Über „**standardkonforme** GPX-Datei" ist der Bezug tragbar — Interoperabilität ist die operative Probe auf Standardkonformität —, aber er ist **nicht mehr wörtlich belegt**. **Hier wird weder die AC gestrichen noch der Wortlaut nachträglich ergänzt**; beides wäre eine Entscheidung, die dem Nutzer gehört. |
| Rationale | Der prüfbare Kern ist **Erzeugbarkeit und Interoperabilität**, nicht Nutzerverhalten — deshalb kein Nutzersignal. Die Run-/Bike-Trennung ist zwingend, weil die exportierten Kernmetriken sportartspezifisch sind und ein Exporter, der nur mit Laufdaten getestet wurde, bei Radaktivitäten stillschweigend falsche oder leere Felder schreiben kann. Der **Negativtest auf Health-Daten** ist keine Nebenbedingung, sondern trägt die Datenminimierung aus REQ-034 in den Export hinein: ein GPX mit eingebetteten Herzfrequenzverläufen verlässt das Gerät unkontrolliert. |

---

### ~~REQ-040~~ — Streckenwiederverwendung und Aktivitätsvergleich · **DEPRECATED 2026-07-20**

> **Deprecated in Runde 4 (2026-07-20) auf Nutzerentscheidung; Nachfolger REQ-041 und REQ-042.**
> Grund: REQ-040 war — wie zuvor REQ-014 — ein **Composite** aus zwei unabhängig prüfbaren
> Anforderungen. Sie können unabhängig bestehen oder scheitern, brauchen getrennte Acceptance
> Criteria und sind **unterschiedlich blockiert**: die Wiederverwendung ist heute vollständig
> spezifizierbar, der Vergleich ist ohne **OQ-015** nicht spezifizierbar. Ein gemeinsames
> Requirement kettet den lieferbaren Teil an eine offene Forschungsfrage.
> **Die Composite-Requirement wurde ausdrücklich NICHT auf eine Hälfte verengt.**
> Folge-Deprecations: **AC-040, EV-040, TRC-040, CAN-140** (Registry §7.5.1).

| Feld | Wert |
|---|---|
| Trace ID | ~~TRC-040~~ → **TRC-041**, **TRC-042** |
| Status | **deprecated 2026-07-20** — keine aktive Verknüpfung. Der Block bleibt als Migrationsbeleg stehen; Registry-Regel 3 verbietet die **Referenz** auf eine deprecatete ID, nicht ihren **Migrationsbeleg**. |
| Aufteilung der Felder | Vision-Anker VIS-003 → **nur** TRC-042 (und dort weiterhin als ungeprüfte ASSUMPTION). Für die Wiederverwendungshälfte ist **VIS-014** reserviert, Inhalt MISSING. · Canvas CAN-140 → CAN-142 (Planung) / CAN-143 (Auswertung). · AC-040 Halbsatz 1 („erneut gestartet werden") → AC-042, Halbsatz 2 („mit definierten Kennzahlen gegenübergestellt") → AC-043. · EV-040 Teil 1 → EV-043, Teil 2 → EV-044. |
| Was hier **nicht** passiert ist | Der frühere Zeilenstatus `linked-partial` ist **nicht** auf einen Nachfolger vererbt worden. Beide Nachfolger sind **neu bewertet**: TRC-041 ist `broken` (kein Vision-Anker), TRC-042 ist `linked-partial` (ungeprüfte ASSUMPTION). Eine Vererbung hätte die halbe Deckung von REQ-040 stillschweigend auf die Wiederverwendungshälfte übertragen, für die sie gerade **nicht** galt. |

---

### REQ-041 — Wiederverwendung einer gespeicherten Route

> **Nachfolger 1 von 2 für das deprecatete REQ-040.** Prüft ausschließlich die
> **Planungsfunktion**; der Vergleich liegt bei REQ-042.

| Feld | Wert |
|---|---|
| Trace ID | **TRC-041** |
| Vision Item | **VIS-014 — reserved, Inhalt MISSING → BLOCKER.** Prüfung aller aktiven VIS-Items: **VIS-003** nennt verlässliches Tracking, verständliche Health-Auswertung, konkrete Fortschrittssignale und sicheren Zugang zu lokalen Trainingspartnern — **keine** Wiederverwendung geplanter Strecken; **VIS-004** nennt Belastung, Progression, lokale Teams und ortsbezogene Spielmechaniken — ebenfalls nicht. **Kein Item wird umgedeutet. TRC-041 wird bewusst als `broken` geführt**, mit sichtbarer Lücke, statt an VIS-003 gehängt zu werden — genau letzteres war der Defekt VIS-009 ↔ REQ-014. |
| Vision-Anker — Wechselwirkung mit REQ-006, offengelegt | Die naheliegende Gegenrede lautet „Routenplanung hängt doch an VIS-003 — siehe TRC-006". Genau dieser Anker ist am 2026-07-20 **geprüft und entfernt** worden (Registry §8 Punkt 40; Prüfung in §3 bei REQ-006). Er taugt deshalb **nicht** als Präzedenz für REQ-041. Beide Zeilen sind jetzt konsistent: **weder REQ-006 noch REQ-041 hat einen Vision-Anker.** |
| Canvas Item (atomar) | **CAN-142** (Wiederverwendung einer gespeicherten Route als Grundlage einer geplanten Aktivität). **Kanonischer Wortlaut:** „Nutzer können eine gespeicherte Route erneut als Grundlage einer geplanten Run- oder Bike-Aktivität verwenden." Release-Stufe **A2**. |
| Abgrenzung zu CAN-050 und REQ-006 — geprüft, nicht angenommen | **CAN-050** („Routenplanung und gespeicherte Routen") trägt laut Registry **REQ-006 auf Gate A0**: eine Route **anlegen** und **speichern**. CAN-142 ist deren **erneute Verwendung** auf **Gate A2** — eine andere Handlung zu einem anderen Zeitpunkt. CAN-050 dafür zu benutzen wäre die plausible Lesart mit falscher Bedeutung. **REQ-006** verlangt wörtlich, „eine Route über Wegpunkte oder ein Distanzziel zu planen, das korrekte Run-/Bike-Routingprofil zu verwenden und den Plan vor dem Start zu prüfen" — kein Wort über die Wiederverwendung einer **gespeicherten** Route. |
| Canvas-Problem | **MISSING — BLOCKER.** Der Vorgänger REQ-040 hing an **CAN-013** mit der Begründung „(Vergleich erzeugt Bedeutung)". Diese Verknüpfung ist am 2026-07-20 **entfernt** (verbotene Schlusskette, Registry §7.5.5) und wird **nicht** auf REQ-041 vererbt — sie betraf ohnehin die Vergleichshälfte, nicht die Wiederverwendung. Der Canvas führt **kein** Planungs- oder Wiederverwendungsproblem; **CAN-019** („Planungs- und Orientierungsproblem vor der Aktivität") ist `reserved` und inhaltlich **MISSING**. Es wird keine Problem-ID erfunden. |
| Acceptance Criterion | **AC-042** — fünf einzeln prüfbare Bedingungen: (a) gespeicherte Route für **Run** wiederverwendbar · (b) gespeicherte Route für **Bike** wiederverwendbar · (c) geladene Geometrie und Wegpunkte stimmen mit der gespeicherten überein · (d) das sportartspezifische **Routingprofil** bleibt beim Laden korrekt · (e) eine gelöschte oder beschädigte gespeicherte Route führt zu einem **kontrollierten Fehler**, nicht zu einem stillen Leerstart. **Vollständig spezifizierbar — nicht von OQ-015 abhängig.** |
| Measurement Type | **OPERATIONAL_QUALITY** |
| Signal / Control Evidence | **Getrennt für Run und Bike:** Erfolgsrate des Ladens und Startens einer gespeicherten Route; Anteil geladener Routen, deren Geometrie und Wegpunkte exakt der gespeicherten Fassung entsprechen; Anzahl Fälle, in denen beim Laden ein **falsches Routingprofil** gesetzt wird (Sollwert 0); Anteil gelöschter oder beschädigter Routen, die zu einem kontrollierten Fehler statt zu einem stillen Leerstart oder Absturz führen. |
| Target / Pass Condition | AC-042 als Pass/Fail mit Nullschwellen, **Run und Bike getrennt nachgewiesen**: 100 % Übereinstimmung von Geometrie und Wegpunkten · **0** falsche Routingprofile beim Laden · 100 % kontrollierte Fehlerfälle bei gelöschter oder beschädigter Route. **Eine Wiederverwendungsquote wird ausdrücklich NICHT gesetzt** — ein solcher Zielwert wäre erfunden und würde zudem einen Nutzungsanreiz messen statt Korrektheit. |
| Measurement Window | Vor **GATE-A2**; danach bei jeder Änderung am Routen-Datenmodell, am Ladepfad oder an der Profilzuordnung. **Je Sportart und je Plattform mindestens ein vollständiger Durchlauf**, zusätzlich je ein Negativtest (gelöschte Route, beschädigte Route). |
| Evidence Needed | **EV-043** — Wiederverwendungstest je Sportart: Auswahl und Start einer gespeicherten Route, Abgleich von Geometrie und Wegpunkten gegen die gespeicherte Fassung, Erhalt des sportartspezifischen Routingprofils, kontrollierter Fehlerfall bei gelöschter oder beschädigter Route. |
| Evidence Source | EV-043; Mindestklasse `real-boundary-smoke` — der erneute Start einer gespeicherten Route berührt Persistenz, Kartendarstellung und den Routing-Pfad und ist mit Fixtures allein nicht belegbar. `evidence_status` **`not-planned`** — es existiert kein Code und kein Messkonzept; `planned` würde eine definierte, nur noch nicht instrumentierte Messung behaupten. **NICHT durch OQ-015 blockiert.** |
| Source Type | **ASSUMPTION** — der Wortlaut stammt aus der Nutzerentscheidung vom 2026-07-20 und ist nicht ausdrücklich als Anforderungstext bestätigt (Registry §8 Punkt 43). |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner“ = MISSING. |
| Release Gate | **GATE-A2** |
| Status | **broken** (Vision-Anker MISSING) · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — Persistenz, Kartendarstellung und Routingprofil beim erneuten Laden einer gespeicherten Route sind nur an der echten Grenze belegbar. |
| Risiko | kein Registereintrag im Messmodell referenziert |
| Offene Entscheidung | offene Fragen: OQ-002 · **BLOCKER: kein Vision-Anker** (VIS-014 reserved, Inhalt MISSING — Registry §8 Punkt 38). · **BLOCKER: kein canvas-problem-Anker** (CAN-019 reserved, MISSING). · **BLOCKER: Wortlaut unbestätigt** — CAN-142 und REQ-041 stehen auf ASSUMPTION (Registry §8 Punkt 43). · **AUSDRÜCKLICH NICHT blockiert durch OQ-015.** Das ist keine Nebenbemerkung, sondern der operative Grund der Teilung: die Vergleichbarkeitsdefinition betrifft REQ-042, und REQ-041 darf nicht an ihr hängen. |
| Rationale | Der prüfbare Kern ist die **Wiederherstellungstreue** einer gespeicherten Route — lädt sie exakt so, wie sie gespeichert wurde, und mit dem richtigen Sportprofil. Das ist Betriebsqualität, kein Nutzerverhalten; deshalb kein Nutzersignal. **Run/Bike-Trennung ist hier selbst Prüfgegenstand:** dieselbe Geometrie unter dem falschen Routingprofil zu laden ist genau der Fehlerfall, den (d) ausschließt — RISK-005 („Bike zeigt falsche Laufmetriken") in der Planungsphase. |

---

### REQ-042 — Vergleich fachlich vergleichbarer Aktivitäten

> **Nachfolger 2 von 2 für das deprecatete REQ-040.** Prüft ausschließlich die
> **Auswertungsfunktion**; die Wiederverwendung liegt bei REQ-041.

| Feld | Wert |
|---|---|
| Trace ID | **TRC-042** |
| Vision Item | **VIS-003** — User Need: „… **konkrete Fortschrittssignale** …“. **Der Anker ist unverändert aus TRC-040 übernommen und bleibt eine ungeprüfte ASSUMPTION** (siehe nächste Zeile). |
| Vision-Anker — Einstufung ausdrücklich NICHT hochgestuft (2026-07-20) | Die Registry führt VIS-003 hier ausdrücklich als **zu prüfende Annahme des Traceability-Owners, nicht als eigene Feststellung** (§6.4 REQ-042, §6.6 TRC-042). **Was für den Anker spricht:** eine Gegenüberstellung zweier Aktivitäten auf derselben Strecke *liest sich* als konkretes Fortschrittssignal. **Was ihn nicht trägt:** VIS-003 nennt „Fortschrittssignale“ ohne jede Bestimmung, **woraus** sie entstehen; die Vorfassung bei REQ-040 hat daraus eine Deckung abgeleitet, ohne sie zu belegen. Solange die Klausel nicht ausgelegt ist, ist die Zuordnung **plausibel, aber nicht nachgewiesen** — und genau diese Konstellation ist die wiederkehrende Defektklasse. Zeilenstatus deshalb **`linked-partial`**, nicht `linked`. **Dieselbe Frage ist bei REQ-007 offen** und dort ebenfalls als OPEN QUESTION geführt, nicht entschieden. |
| Canvas Item (atomar) | **CAN-143** (Vergleich fachlich vergleichbarer Aktivitäten auf derselben oder hinreichend ähnlichen Strecke). **Kanonischer Wortlaut:** „Nutzer können fachlich vergleichbare Aktivitäten auf derselben oder hinreichend ähnlichen Strecke anhand sportartspezifischer Kennzahlen miteinander vergleichen.“ Release-Stufe **A2**. |
| Canvas-Problem | **MISSING — BLOCKER.** Der Vorgänger REQ-040 hing an **CAN-013** („Bestehende Tracker liefern Daten ohne verständliche Bedeutung“) mit der Begründung „(Vergleich erzeugt Bedeutung)“. Diese Verknüpfung ist am 2026-07-20 **entfernt** — dieselbe Defektklasse wie bei REQ-037/038/039: CAN-013 als Universal-Problemanker. Der Canvas führt **kein** Problem „ich kann nicht erkennen, ob ich schneller geworden bin“. Es wird **keine** Problem-ID erfunden und **kein** reserviertes Item umgedeutet. |
| Acceptance Criterion | **AC-043** — **feststehend und schon jetzt prüfbar:** (a) Run und Bike **strikt getrennt**, 0 sportübergreifende Vergleiche · (b) **0 irreführende Bestzeiten bei nicht vergleichbarer Geometrie**. **MISSING (OQ-015) und hier NICHT erfunden:** Vergleichbarkeitskriterium, tolerierte Abweichung der Streckenähnlichkeit, verglichene Kennzahlen sowie die Behandlung verkürzter, verlängerter und abgebrochener Aktivitäten. **AC-043 ist bis zur Entscheidung von OQ-015 nicht vollständig prüfbar — AC-042 ist davon unberührt.** |
| Measurement Type | **OPERATIONAL_QUALITY** — für das Requirement. **Die Vergleichslogik selbst bleibt `RESEARCH_HYPOTHESIS` bzw. MISSING**, solange OQ-015 offen ist. Beides wird getrennt geführt: *dass* Nutzer vergleichen können sollen, ist eine Produktannahme; **wie** verglichen wird, ist eine offene Untersuchungsfrage. REQ-042 zählt deshalb **nicht** in die RESEARCH_HYPOTHESIS-Gruppe von §2. |
| Signal / Control Evidence | **Strikt getrennt für Run und Bike:** Anteil Aktivitätspaare, die von der Vergleichslogik als vergleichbar eingestuft werden, gegen ein manuell kuratiertes Referenzurteil; Anzahl **falsch-positiver** Vergleiche (geometrisch nicht vergleichbare Aktivitäten werden gegenübergestellt); Anzahl ausgewiesener Bestzeiten bei nicht vergleichbarer Geometrie (**Sollwert 0**); Anzahl sportübergreifender Vergleiche (**Sollwert 0**); Verhalten bei verkürzten, verlängerten und abgebrochenen Aktivitäten. |
| Target / Pass Condition | **Zweigeteilt, weil nur ein Teil heute bestimmbar ist.** **Feststehend (AC-043):** 0 sportübergreifende Vergleiche · 0 irreführende Bestzeiten bei nicht vergleichbarer Geometrie. **MISSING (OQ-015):** Vergleichbarkeitskriterium, tolerierte Abweichung, verglichene Kennzahlen, Behandlung verkürzter/verlängerter/abgebrochener Aktivitäten. **Diese Werte werden nicht erfunden.** |
| Measurement Window | Vor **GATE-A2**; danach bei jeder Änderung der Vergleichslogik oder der Vergleichbarkeitsschwelle. Fixture-Suite bei jedem CI-Lauf, **sobald eine Schwelle existiert**. |
| Evidence Needed | **EV-044** — Vergleichstest je Sportart: Gegenüberstellung zweier als fachlich vergleichbar erkannter Aktivitäten anhand sportartspezifischer Kennzahlen; **Negativtests** gegen verkürzte, verlängerte, abgebrochene und geometrisch abweichende Aktivitäten; **Negativtest gegen sportübergreifenden Vergleich**. |
| Evidence Source | EV-044; Mindestklasse `real-boundary-smoke`. `evidence_status` **`not-planned`**. **BLOCKER:** ohne die Vergleichs- und Streckenähnlichkeitsdefinition aus **OQ-015** ist **kein Testfall bezifferbar** — die Negativtests sind benannt, aber ohne Toleranzwert nicht ausführbar. **Ausnahme, damit die Blockade nicht pauschal wirkt:** der Negativtest gegen den **sportübergreifenden** Vergleich ist schon heute ausführbar, weil die Sportart ein diskretes Feld ist und keine Toleranz braucht. |
| Source Type | **ASSUMPTION** (Registry §8 Punkt 43) für das Requirement; die Vergleichslogik bleibt `RESEARCH_HYPOTHESIS` bzw. MISSING. |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Die Vergleichbarkeitsdefinition (OQ-015) hat ebenfalls **keinen benannten Entscheider**. |
| Release Gate | **GATE-A2** |
| Status | **linked-partial** · `true-line-status` = pending-watcher · `wired-in-prod?` = no · `evidence-class` = none |
| canvas-risk-status | aligned |
| evidence-class-required | real-boundary-smoke — der Vergleich zweier realer Aufzeichnungen unter echtem GPS-Rauschen ist mit Fixtures allein nicht belegbar. |
| Risiko | kein Registereintrag im Messmodell referenziert |
| Offene Entscheidung | offene Fragen: OQ-002 · **BLOCKER OQ-015 (Vergleichbarkeits- und Streckenähnlichkeitsdefinition):** wann zwei Strecken als **vergleichbar** gelten · **tolerierte Abweichung** · welche Kennzahlen verglichen werden · Behandlung verkürzter, verlängerter und abgebrochener Aktivitäten · Sicherstellung, dass bei nicht vergleichbarer Geometrie **keine irreführende Bestzeit** entsteht. `blocked_gates: [A2]` · `blocked_activities: [implementation]` — **A0 und A1 sind nicht blockiert, und REQ-041 ist es ebenfalls nicht.** · **BLOCKER: kein canvas-problem-Anker.** · **OPEN QUESTION: der Vision-Anker VIS-003 ist eine ungeprüfte ASSUMPTION** und wird hier weder bestätigt noch hochgestuft. |
| Rationale | Der prüfbare Kern ist die **Korrektheit der Vergleichsaussage**, nicht deren Nutzung — deshalb kein Nutzersignal und keine Vergleichsquote. Die **strikte Sporttrennung** ist keine Formalie: eine Radfahrt und ein Lauf über dieselbe Geometrie sind physikalisch unvergleichbar, und ein sportübergreifender „Rekord“ wäre eine falsche Produktaussage. Die Nullschwelle für irreführende Bestzeiten adressiert denselben Fehlerfall **innerhalb** einer Sportart: **eine Bestzeit über eine nur scheinbar identische Strecke ist schlimmer als gar keine Bestzeit**, weil der Nutzer ihr vertraut. |
| Warum eine eigene REQ-ID | Prüfung aller bestehenden Requirements: **keine** deckt diese Aussage exakt und atomar ab. Sie stand ausschließlich als Teilklausel im Composite REQ-008 und danach im Composite REQ-040. **REQ-006** (Routenplanung) und **REQ-007** (routenbezogener Fortschritt) betreffen die **Planung und Durchführung** einer Route **vor** bzw. **während** der Aktivität, nicht den **Vergleich zweier abgeschlossener Aktivitäten**. **REQ-008** ist auf Verlauf und Detailansicht **einer** Aktivität verengt. |

---

## 4. Canvas-Pflichtfelder (atomare IDs)

Alle Werte sind gegenüber der Vorfassung mechanisch von Sammelblock- und Facetten-IDs auf
atomare Registry-IDs umgestellt. `canvas-link` ist für **alle aktiven Requirements**
`docs/canvas/revyr-endurance-platform.canvas.md`. Die Tabellen führen die aus der Registry
abgeleitete Zahl aktiver Requirements (§0.0); **REQ-014 ist als `deprecated` entfallen** und
durch REQ-037/REQ-038 ersetzt.

### 4.1 Problem und Zielnutzer

| REQ-ID | canvas-problem (atomar) | canvas-target-user (atomar) |
|---|---|---|
| REQ-001 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. *(Enabler: sportkorrekte Metrik als Voraussetzung von Bedeutung)* | CAN-023, CAN-024 |
| REQ-002 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. | CAN-023, CAN-024 |
| REQ-003 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. | CAN-023, CAN-024 |
| REQ-004 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. ⚠️ **schwacher Bezug, offengelegt (2026-07-20):** CAN-013 beschreibt Daten, die **vorhanden** sind und nicht interpretiert werden; REQ-004 behandelt **falsche** Daten (Drift, Sprünge). Der Anker bleibt bis zur Nutzerentscheidung stehen — ihn zu entfernen hieße, für REQ-002…REQ-005 gemeinsam eine neue Problemaussage zu erfinden. §6.1.2. | CAN-023, CAN-024 |
| REQ-005 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. | CAN-023, CAN-024 |
| REQ-006 | CAN-019 — MISSING – Planungs- und Orientierungsproblem vor der Aktivität *(reserved, Inhalt MISSING — BLOCKER)* | CAN-023, CAN-024 |
| REQ-007 | CAN-019 — MISSING – Planungs- und Orientierungsproblem vor der Aktivität *(reserved, Inhalt MISSING — BLOCKER)* | CAN-023, CAN-024 |
| REQ-008 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. *(Wiederfinden erzeugt Bedeutung; der **Vergleich** liegt seit 2026-07-19 bei REQ-040)* | CAN-023, CAN-024 |
| REQ-009 | **CAN-022** — „Ohne Anbindung bereits genutzter Sportuhren und externer Sensoren fehlen oder verschlechtern sich zentrale Trainingssignale wie **Herzfrequenz**, …“ *(ersetzt CAN-013 am 2026-07-20; Einzelprüfung in §3: fehlende Daten sind keine bedeutungslosen Daten. Offengelegte Abweichung: CAN-022 trägt Release Gate E, REQ-009 liegt auf A1 — OPEN QUESTION, Registry eingefroren)* | CAN-023, CAN-024, **CAN-025 → USER-004** (sekundär; BLOCKER geschlossen, `source_type` ASSUMPTION) |
| REQ-010 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. *(Kernfacette)* | CAN-023, CAN-024 |
| REQ-011 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. | CAN-023, CAN-024 — **keine USER-004-Verknüpfung** (semantische Einzelprüfung, §3); der frühere CAN-025-BLOCKER ist **gestrichen, nicht ersetzt** |
| REQ-012 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. | CAN-023, CAN-024 |
| REQ-013 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. | CAN-023, CAN-024 |
| ~~REQ-014~~ | **deprecated 2026-07-19** → REQ-037, REQ-038 | — |
| REQ-015 | CAN-016 — MISSING – Fortschritts- und Motivationsproblem *(reserved, Inhalt MISSING — BLOCKER)* | CAN-023, CAN-024; Teamkleidung → CAN-026, CAN-027 |
| REQ-016 | CAN-016 — MISSING – Fortschritts- und Motivationsproblem *(reserved, Inhalt MISSING — BLOCKER)* | CAN-023, CAN-024 |
| REQ-017 | CAN-014 — Soziale Interaktion findet ohne lokale Bindung statt. *(Enabler: Identität als Voraussetzung lokaler Bindung)* | CAN-023, CAN-024, CAN-026, CAN-027 |
| REQ-018 | CAN-014 — Soziale Interaktion findet ohne lokale Bindung statt. | CAN-023, CAN-024, CAN-026, CAN-027 |
| REQ-019 | CAN-014 — Soziale Interaktion findet ohne lokale Bindung statt. | CAN-023, CAN-024 |
| REQ-037 | **MISSING — BLOCKER (2026-07-20).** CAN-013 **entfernt**: die Verknüpfung lief über die in Registry §6.1.1 **verbotene** Kette „Wahrnehmbarkeit als Vorstufe von Verständlichkeit“. Der Canvas führt **kein Zugänglichkeitsproblem**; CAN-016…CAN-021 decken keines ab. Kein Item umgedeutet, keine Problem-ID erfunden. §8 Punkt 37. | CAN-023, CAN-024, CAN-026, CAN-027 |
| REQ-038 | **MISSING (begründet) — 2026-07-20.** CAN-013 **entfernt**. Der Eintrag war in sich widersprüchlich: er nannte CAN-013 als Anker **und** begründete zugleich „kein eigenes Problem-Item“. Aufgelöst zugunsten der Nichtanwendbarkeit — eine Gestaltungssprache ist eine **Constraint** (CAN-141), kein Nutzerproblem. ⚠️ Registry §8 Punkt 37 zählt REQ-038 dennoch zu den BLOCKERn; die Divergenz ist in §3 und §6.1 offengelegt, nicht einseitig aufgelöst. | CAN-023, CAN-024, CAN-026, CAN-027 |
| REQ-039 | **MISSING — BLOCKER (2026-07-20).** CAN-013 **entfernt**. Das Feld führte bis dahin **gleichzeitig** die Verknüpfung *und* ihre Widerlegung („der Canvas führt kein Portabilitäts- oder Lock-in-Problem. MISSING“) — eine maschinelle Prüfung liest die Verknüpfung, nicht den Vorbehalt daneben. §8 Punkt 37. | CAN-023, CAN-024 |
| **REQ-041** | **MISSING — BLOCKER.** Der Canvas führt **kein** Planungs- oder Wiederverwendungsproblem; **CAN-019** ist `reserved`, Inhalt MISSING. Der CAN-013-Bezug des Vorgängers REQ-040 („Vergleich erzeugt Bedeutung“) ist entfernt und wird **nicht** vererbt — er betraf ohnehin die Vergleichshälfte. | CAN-023, CAN-024 |
| **REQ-042** | **MISSING — BLOCKER.** CAN-013 **entfernt** (verbotene Kette, §7.5.5 der Registry). Der Canvas führt kein Problem „ich kann nicht erkennen, ob ich schneller geworden bin“. | CAN-023, CAN-024 |
| REQ-020 | CAN-014 — Soziale Interaktion findet ohne lokale Bindung statt. | CAN-026, CAN-027 primär, CAN-023, CAN-024 sekundär |
| REQ-021 | CAN-015 — Es gibt zu wenig Anlass für echte gemeinsame Aktivität. | CAN-026, CAN-027 |
| REQ-022 | CAN-015 — Es gibt zu wenig Anlass für echte gemeinsame Aktivität. *(Kernfacette)* | CAN-026, CAN-027 primär, CAN-023, CAN-024 als Teilnehmende |
| REQ-023 | CAN-020 — MISSING – Fairness- und Manipulationsproblem *(reserved, Inhalt MISSING — BLOCKER)* | CAN-023, CAN-024 |
| REQ-024 | CAN-020 — MISSING – Fairness- und Manipulationsproblem *(reserved, Inhalt MISSING — BLOCKER)* | CAN-023, CAN-024, CAN-026, CAN-027 |
| REQ-025 | CAN-015 — Es gibt zu wenig Anlass für echte gemeinsame Aktivität. *(Challenges als Anlass)* | CAN-023, CAN-024 |
| REQ-026 | CAN-015 — Es gibt zu wenig Anlass für echte gemeinsame Aktivität. | CAN-026, CAN-027 |
| REQ-027 | CAN-015 — Es gibt zu wenig Anlass für echte gemeinsame Aktivität. | CAN-026, CAN-027 |
| REQ-028 | CAN-021 — MISSING – Problem hinter Einzel-Revieren und Sportplatz-Challenges *(reserved, Inhalt MISSING — BLOCKER)* | CAN-023, CAN-024 |
| REQ-029 | CAN-021 — MISSING – Problem hinter Einzel-Revieren und Sportplatz-Challenges *(reserved, Inhalt MISSING — BLOCKER)* | CAN-023; Bike-Anwendbarkeit (CAN-024) OPEN QUESTION. *(Runde 6, 2026-07-20: die Frage wird durch die Verengung von CAN-024 erstmals **entscheidbar** — mit dem verschmolzenen Item „Freizeit- und Rennradfahrer:innen" ließ sich nicht bestimmen, welcher Radfahrtyp gemeint ist. Die Frage bleibt offen und wird hier **nicht** beantwortet.)* |
| REQ-030 | CAN-017 — MISSING – Sicherheitsproblem *(reserved, Inhalt MISSING — BLOCKER; VIS-003 nennt „sicheren Zugang“, der Canvas kein Sicherheitsproblem (Canvas/Vision-Divergenz))* | CAN-023, CAN-024 |
| REQ-031 | CAN-017 — MISSING – Sicherheitsproblem *(reserved, Inhalt MISSING — BLOCKER)* | CAN-023, CAN-024 |
| REQ-032 | **CAN-022** — Ohne Anbindung bereits genutzter Sportuhren und externer Sensoren fehlen oder verschlechtern sich zentrale Trainingssignale … *(`active` seit 2026-07-19, `source_type` ASSUMPTION)* | CAN-024 primär (Bike-Sensorik), CAN-023 (Watch), **CAN-025 → USER-004 (primär)**. ⚠️ **Befund Runde 6 (2026-07-20), Verknüpfung unverändert:** CAN-024 wird nach Nutzerauftrag Punkt 2 auf den belegten Kern verengt (Owner Canvas). Die hier gesetzte Rolle „**primär (Bike-Sensorik)**" stützt sich auf den **ambitionierten** Anteil des Items. Dieser Anteil steht in `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md:52` unter der Rangmarkierung „**Sekundär:** Ambitionierte Rennradfahrer und Läufer mit festen Strecken und Leistungsfokus" — **nicht** im Primär-Punkt `:51`, aus dem CAN-024 laut Canvas hergeleitet ist. Sensorik ist quellenseitig allein an der ambitionierten Persona festgemacht (`SRC-001:137` „Markus (41, Rennradfahrer …): feste Stammstrecken, **Sensoren**, Leistungsvergleich") bzw. an der ungestuften Rad-Zielgruppe in `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md:65` „**Radfahrer/Rennradfahrer:** … **Sensorik** …". **Folge, präzisiert gegen den Ausgangsbefund:** REQ-032 steht **nicht** ohne belegten Zielnutzer da — CAN-023 bleibt. Unbelegt wird allein die **Sensorik-Verankerung**; einziger verbleibender Träger dafür ist CAN-025 → USER-004, und das ist `ASSUMPTION` mit offenem BLOCKER. **Die Verknüpfung wird hier weder entfernt noch umgeschrieben**, weil der endgültige CAN-024-Wortlaut dem Canvas-Owner obliegt und die Gegenprüfung drei verschiedene Fassungen vorgeschlagen hat. Zeilenstatus TRC-032 bleibt `broken` (Vision-Anker MISSING, unverändert). |
| REQ-033 | CAN-013 — Bestehende Tracker liefern Daten ohne verständliche Bedeutung. | CAN-023, CAN-024 |
| REQ-034 | CAN-018 — MISSING – Datenschutzproblem *(reserved, Inhalt MISSING — BLOCKER; Datenschutz erscheint im Canvas nur als Constraint (CAN-088) und Risiko (CAN-105))* | CAN-023, CAN-024, CAN-026, CAN-027 |
| REQ-035 | CAN-123 — Evidence Ledger *(kein Nutzerproblem — begründete Nichtanwendbarkeit: Prozess-REQ, Anker ist die Evidence-Annahme CAN-123)* | CAN-023, CAN-024, CAN-026, CAN-027 (nur mittelbar, kein direkter Nutzerkontakt) |
| REQ-036 | CAN-083 — Store-Policies sind verbindlich *(kein Nutzerproblem — begründete Nichtanwendbarkeit: Compliance-REQ, Anker ist der Constraint CAN-083)* | CAN-023, CAN-024, CAN-026, CAN-027 (nur mittelbar, kein direkter Nutzerkontakt) |

### 4.2 Wertversprechen, Erfolgssignal, Risikostatus

| REQ-ID | canvas-value-claim | canvas-success-signal | canvas-risk-status |
|---|---|---|---|
| REQ-001 | CAN-028 | MISSING — kein Erfolgssignal; Enabler für CAN-124 | aligned |
| REQ-002 | CAN-028 | CAN-124 (VIS-006 A: W4-Retention > 30 %) | risk-introduced |
| REQ-003 | CAN-028 | CAN-124 (VIS-006 A: W4-Retention > 30 %) | risk-introduced |
| REQ-004 | CAN-028 | MISSING — kein Signal; Enabler für CAN-124, Messgröße ist NFR-001 | aligned |
| REQ-005 | CAN-028 | MISSING — kein Signal; Enabler für CAN-124, Messgröße ist NFR-003 | aligned |
| REQ-006 | CAN-028 | MISSING — kein Erfolgssignal für Routenplanung | blocked |
| REQ-007 | CAN-028 | MISSING — wie REQ-006 | risk-introduced |
| REQ-008 | CAN-030 | MISSING — kein Signal für Verlauf und Detailansicht | aligned |
| REQ-009 | CAN-029 | CAN-126 (Enabler, kein eigenes Signal) | risk-introduced |
| REQ-010 | CAN-029 | CAN-126 (VIS-006 A: Warum-Aufrufe > 25 %) | risk-introduced |
| REQ-011 | CAN-029 | MISSING — kein Signal für Zonen oder Audio-Ansage | risk-introduced |
| REQ-012 | CAN-029 | CAN-125 (VIS-006 A: Check-in > 50 %) | risk-introduced |
| REQ-013 | CAN-029 | CAN-124 und CAN-126 | risk-introduced |
| ~~REQ-014~~ | **deprecated 2026-07-19** → REQ-037, REQ-038 | — | — |
| REQ-015 | CAN-030 und CAN-033 (Anti-Pay-to-Win-Schutz) | MISSING — kein Progressionssignal in CAN-124…CAN-129 | aligned |
| REQ-016 | CAN-030 | MISSING — kein Signal für Recaps/Erfolgskarten | risk-introduced |
| REQ-017 | CAN-032 (Enabler) | MISSING — kein Signal für Accounts/Migration | risk-introduced |
| REQ-018 | CAN-032 | MISSING — kein Signal für Privacy/Moderation | aligned |
| REQ-019 | CAN-032 | **CAN-130** — bestätigte Routenübernahmen je auswertbarer Empfehlung **> 1,0**, Run und Bike getrennt; Fenster **rollierende 28 Tage**. `active` seit 2026-07-19, `source_type` **EXPLICIT**, `evidence_status` **planned**, `empirical_result` **MISSING** | risk-introduced |
| REQ-020 | CAN-032 | CAN-127 (VIS-006 C: Team nach 60 Tagen > 25 %) | aligned |
| REQ-021 | CAN-032 (nur mittelbar) | CAN-127 (VIS-006 C) — DIVERGENZ: das Messmodell verankert REQ-021 an CAN-128, siehe Divergenztabelle | value-risk |
| REQ-022 | CAN-032 | CAN-128 (VIS-006 C: gemeinsame Aktivität > 40 %) | risk-introduced |
| REQ-023 | CAN-033 | MISSING — kein Fairness-Signal in CAN-124…CAN-129 | aligned |
| REQ-024 | CAN-033 | MISSING — Falsch-Positiv-Quote ist Evidence (EV-024), kein Erfolgssignal | risk-introduced |
| REQ-025 | CAN-030 | MISSING — kein Challenge-/Ranking-Signal | value-risk |
| REQ-026 | CAN-032 | CAN-129 (VIS-006 D: Season-Teilnahme > 60 %) | risk-introduced |
| REQ-027 | CAN-030 | CAN-129 (VIS-006 D) — DIVERGENZ: das Messmodell führt CAN-129 ausschließlich bei REQ-026, siehe Divergenztabelle | risk-introduced |
| REQ-028 | MISSING — keine CAN-Wertklausel deckt Einzel-Reviere; CAN-032 fordert ausdrücklich Gemeinschaft | MISSING — kein Signal; CAN-127/CAN-128 sprechen nur von gemeinsamer Aktivität | risk-introduced |
| REQ-029 | CAN-030 (schwach; Bahngold beeinflusst laut REQ nichts) | MISSING — kein Signal | risk-introduced |
| REQ-030 | CAN-031 (OPEN QUESTION: „sicherer“ ist im Canvas nicht definiert) | MISSING — kein Safety-Signal | risk-introduced |
| REQ-031 | CAN-031 (siehe Vorbehalt REQ-030) | MISSING — kein Safety-Signal | risk-introduced |
| REQ-032 | **CAN-029** *(sekundär; Gloss „Datenqualität für Belastungsverständnis“ am 2026-07-20 ersetzt — sie stand in keinem Item. Tragend ist der **kanonische Wortlaut von CAN-022**: „Dadurch werden **Belastungsanalyse** … weniger vollständig und weniger zuverlässig.“ REQ-032 zahlt auf **Vollständigkeit und Zuverlässigkeit** von CAN-029 ein, nicht auf dessen Existenz — Einzelprüfung in §3)* | MISSING — kein Wearable-Signal | aligned |
| REQ-037 | **MISSING — BLOCKER (2026-07-20).** CAN-029 **entfernt**: verbotene Kette „Wahrnehmbarkeit als Vorstufe von Verstehen“. CAN-029 ist die **Erklärbarkeit der Belastung** — ein perfekt erklärter Score kann für eine Screenreader-Nutzerin vollständig unzugänglich sein. Die Wertversprechen-Gruppe CAN-028…CAN-038 enthält **kein** Zugänglichkeitsversprechen. §8 Punkt 37 | MISSING — kein Signal. Requirement-spezifisch begründet: eine Nutzungsquote von Screenreader-Nutzern könnte Konformität weder belegen noch widerlegen | aligned |
| REQ-038 | **MISSING (begründet) — 2026-07-20.** CAN-029 **entfernt** (dieselbe verbotene Kette). Der kanonische Anker von REQ-038 ist **CAN-141** und steht in der Kernmatrix; CAN-141 ist eine **DESIGN CONSTRAINT**, kein Wertversprechen, und wird deshalb **nicht** in diese Spalte gehoben — das wäre dieselbe Rollenverwechslung wie ein Erfolgssignal in der Capability-Spalte | MISSING — kein Signal. Requirement-spezifisch begründet: ein Ästhetik- oder Zufriedenheitswert wäre ein Kategorienfehler; die Regel ist eine Schranke mit Nullschwelle | aligned |
| REQ-039 | **CAN-139** *(2026-07-20 statt CAN-030)* — CAN-139 ist seit Runde 4 Item Type **VALUE PROMISE / CAPABILITY** und beginnt wörtlich mit „Nutzer behalten **Kontrolle** über ihre aufgezeichneten Aktivitäten“. **CAN-030 („Erkenne deinen Fortschritt“) trägt nicht:** ein Dateiexport erzeugt weder Vergleich noch Trend noch Rückblick. Offengelegt: die Wertversprechen-Gruppe CAN-028…CAN-038 enthält weiterhin **kein** Portabilitäts- oder Kontrollversprechen — die Umbuchung schließt diese Lücke nicht | MISSING — kein Export-Signal in CAN-124…CAN-130. Eine Exportquote wäre erfunden | aligned |
| **REQ-041** | **MISSING — begründet.** Die Wertversprechen-Gruppe CAN-028…CAN-038 enthält **kein** Planungs- oder Vorbereitungsversprechen. **CAN-028 („Verlässliches Tracking“) wurde geprüft und nicht übernommen** — es trägt die Aufzeichnungsqualität, nicht die Wiederverwendung eines Plans; es steht bei REQ-006 und trägt dort ebenso wenig. Nicht stillschweigend kopiert | MISSING — kein Wiederverwendungssignal in CAN-124…CAN-130. Eine Wiederverwendungsquote wäre erfunden | aligned |
| **REQ-042** | **CAN-030** — „Erkenne deinen **Fortschritt**“. Zwei Aktivitäten auf derselben Strecke gegenüberzustellen **ist** das Erkennen von Fortschritt; das ist eine direkte Aussage, keine Enabler-Kette. Übernommen aus REQ-040, wo es ausschließlich die Vergleichshälfte trug | MISSING — kein Vergleichssignal in CAN-124…CAN-130 | aligned |
| REQ-033 | CAN-029 | MISSING — kein Coach-/Recovery-Signal | blocked |
| REQ-034 | CAN-031 (OPEN QUESTION: siehe REQ-030) | MISSING — kein Datenschutz-Signal | risk-introduced |
| REQ-035 | MISSING — keine Wertklausel enthält ein Prozess-/Qualitätsversprechen; REQ dient CAN-038 und CAN-123 | MISSING — kein Signal | aligned |
| REQ-036 | MISSING — keine Wertklausel enthält ein Compliance-Versprechen; REQ dient CAN-038 und CAN-083 | MISSING — kein Signal | aligned |

### `canvas-risk-status` — Vergabelogik

Genau ein Wert pro Requirement. Präzedenz bei mehreren zutreffenden Bedingungen:
`blocked` > `non-goal-violation` > `risk-introduced` > `value-risk` > `aligned`.
Sekundärbefunde stehen in §3 in der Zeile „Befund“.

| Wert | Bedeutung |
|---|---|
| aligned | Kein Non-Goal-Konflikt (CAN-072…CAN-079), keine Risikoverschärfung (CAN-100…CAN-110), Wertbezug tragfähig. |
| value-risk | Das Requirement kann erfüllt werden, ohne das Canvas-Wertversprechen zu bewegen, oder steht in Spannung zu CAN-033. |
| non-goal-violation | Das Requirement verletzt ein Non-Goal aus CAN-072…CAN-079. |
| risk-introduced | Das Requirement erzeugt oder verschärft ein Risiko aus CAN-100…CAN-110. |
| blocked | Das Requirement hängt an einer offenen Frage, die vor seiner Release-Stufe beantwortet sein müsste, aber offen bzw. MISSING ist. |

---

## 5. True-Line- und Reality-Ledger-Felder

`true-line-status` steht für **alle aktiven Requirements** auf `pending-watcher` — REQ-041 und
REQ-042 eingeschlossen. Diese Matrix vergibt kein `pass`; das Verdikt gehört ausschließlich dem
Plumbline Watcher.

`wired-in-prod? = no` und `evidence-class = none` für **alle aktiven Requirements**: Es existiert
kein Code und kein `mobile/`-Verzeichnis. Für die in Runde 4 hinzugekommenen REQ-041 und REQ-042
gilt das aus demselben Grund wie für die übrigen — nicht, weil sie neu sind, sondern weil es
nichts gibt, woran ein Watcher prüfen könnte.

**MISSING (Registry §8, Punkt 12):** `VC-001` … `VC-036` haben keine Definitionsdatei; ihr Inhalt
ist nicht dokumentiert. Der Präfix `VC-` wird von der ID-Registry ausdrücklich **nicht** verwaltet
(Registry §5.2). Die Spalte bleibt deshalb als offener Punkt stehen und wird hier nicht mit einer
Bedeutung gefüllt.

⚠️ **BLOCKER — die `VC-`Reihe bildet einen Altstand ab und geht der Requirement-Zahl nach.** Für
**REQ-037, REQ-038, REQ-039, REQ-041 und REQ-042 existiert keine VC-ID.** Sie wird hier **nicht
erfunden**: `VC-` ist nicht registry-verwaltet, ab Phase 2 vergibt ohnehin nur die Registry IDs,
und die vorhandenen VC-IDs haben nicht einmal eine Definitionsdatei — eine neue Nummer würde
einer inhaltsleeren Reihe eine weitere inhaltsleere Nummer hinzufügen. Diese Zeilen tragen
deshalb `MISSING — keine VC-ID (BLOCKER)`. **Die Lücke ist in Runde 4 um einen Fall gewachsen**,
weil die Teilung von REQ-040 aus einer requirementlosen VC-Position zwei gemacht hat — sie
schrumpft nicht dadurch, dass REQ-040 deprecatet wurde. Registry §5.2 und §8 Punkt 12 führen
denselben Befund; die Auflösung ist eine Nutzerentscheidung.

| REQ-ID | vision-link | value-check-id | true-line-status | wired-in-prod? | evidence-class | evidence-class-required |
|---|---|---|---|---|---|---|
| REQ-001 | docs/vision/revyr-endurance-platform.vision.md#VIS-008 | VC-001 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-002 | docs/vision/revyr-endurance-platform.vision.md#VIS-003 | VC-002 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-003 | docs/vision/revyr-endurance-platform.vision.md#VIS-005 | VC-003 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-004 | docs/vision/revyr-endurance-platform.vision.md#VIS-003 *(2026-07-20 statt VIS-007; **Runde 6:** Anker vorhanden, **zählt aber nicht als erfüllt** — die tragende Klausel „verlässliches Tracking" ist auf Bedürfnisebene unbelegt, §6.1.1 — Zeilenstatus `not-linked`)* | VC-004 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-005 | docs/vision/revyr-endurance-platform.vision.md#VIS-005 | VC-005 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-006 | **MISSING — kein Vision-Item** (VIS-003 am 2026-07-20 als unpassender Anker entfernt, §3; keine reservierte VIS-ID) | VC-006 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-007 | **MISSING — kein Vision-Item** (VIS-003 am 2026-07-20 in Runde 5 als unpassender Anker entfernt, §3/§6.1.1; keine reservierte VIS-ID) | VC-007 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-008 | docs/vision/revyr-endurance-platform.vision.md#VIS-003 | VC-008 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-009 | docs/vision/revyr-endurance-platform.vision.md#VIS-007 | VC-009 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-010 | docs/vision/revyr-endurance-platform.vision.md#VIS-007 | VC-010 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-011 | docs/vision/revyr-endurance-platform.vision.md#VIS-007 | VC-011 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-012 | docs/vision/revyr-endurance-platform.vision.md#VIS-003 | VC-012 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-013 | docs/vision/revyr-endurance-platform.vision.md#VIS-007 | VC-013 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| ~~REQ-014~~ | **deprecated 2026-07-19** → REQ-037, REQ-038 | ~~VC-014~~ | — | — | — | — |
| REQ-015 | docs/vision/revyr-endurance-platform.vision.md#VIS-004 | VC-015 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-016 | docs/vision/revyr-endurance-platform.vision.md#VIS-004 | VC-016 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-017 | docs/vision/revyr-endurance-platform.vision.md#VIS-005 | VC-017 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-018 | docs/vision/revyr-endurance-platform.vision.md#VIS-009 | VC-018 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-019 | **MISSING — kein Vision-Item** (VIS-008 entfernt Runde 4, VIS-003 entfernt Runde 5 — die „Feed-Hälfte" war eine Ableitung über ein Zwischenglied, §3/§6.1.1; keine reservierte VIS-ID) | VC-019 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-020 | docs/vision/revyr-endurance-platform.vision.md#VIS-004 *(2026-07-20 statt VIS-008)* | VC-020 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-021 | docs/vision/revyr-endurance-platform.vision.md#VIS-004 *(2026-07-20 statt VIS-008; **trägt nur die Team-Hälfte**, §6.1.1 — Zeilenstatus `linked-partial`)* | VC-021 (Inhalt MISSING) | pending-watcher | no | none | integration-fake |
| REQ-022 | docs/vision/revyr-endurance-platform.vision.md#VIS-003 *(2026-07-20 statt VIS-008; VIS-004 geprüft und verworfen, §3; **trägt nur die Aktivitäts-Hälfte, nicht Events**, §6.1.1 — Zeilenstatus `linked-partial`)* | VC-022 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-023 | docs/vision/revyr-endurance-platform.vision.md#VIS-008 | VC-023 (Inhalt MISSING) | pending-watcher | no | none | integration-fake |
| REQ-024 | docs/vision/revyr-endurance-platform.vision.md#VIS-008 | VC-024 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-025 | docs/vision/revyr-endurance-platform.vision.md#VIS-004 | VC-025 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-026 | docs/vision/revyr-endurance-platform.vision.md#VIS-008 | VC-026 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-027 | docs/vision/revyr-endurance-platform.vision.md#VIS-004 | VC-027 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-028 | docs/vision/revyr-endurance-platform.vision.md#VIS-008 | VC-028 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-029 | docs/vision/revyr-endurance-platform.vision.md#VIS-004 | VC-029 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-030 | docs/vision/revyr-endurance-platform.vision.md#VIS-009 | VC-030 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-031 | **MISSING — kein Vision-Item** (VIS-007 am 2026-07-20 als unpassender Anker entfernt, §3; keine reservierte VIS-ID) | VC-031 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-032 | **MISSING — kein Vision-Item** (VIS-005 am 2026-07-19 als unpassender Anker entfernt, §3) | VC-032 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-033 | docs/vision/revyr-endurance-platform.vision.md#VIS-007 | VC-033 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-034 | docs/vision/revyr-endurance-platform.vision.md#VIS-009 | VC-034 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| REQ-035 | docs/vision/revyr-endurance-platform.vision.md#VIS-010 | VC-035 (Inhalt MISSING) | pending-watcher | no | none | real-boundary-smoke |
| REQ-036 | docs/vision/revyr-endurance-platform.vision.md#VIS-010 | VC-036 (Inhalt MISSING) | pending-watcher | no | none | production-verified |
| **REQ-037** | docs/vision/revyr-endurance-platform.vision.md#VIS-011 (**unbestätigt** — zählt nicht als erfüllter Anker) | **MISSING — keine VC-ID (BLOCKER)** | pending-watcher | no | none | real-boundary-smoke |
| **REQ-038** | **MISSING — VIS-012 reserved, Inhalt MISSING (BLOCKER)** | **MISSING — keine VC-ID (BLOCKER)** | pending-watcher | no | none | real-boundary-smoke |
| **REQ-039** | **MISSING — VIS-013 reserved, Inhalt MISSING (BLOCKER)** | **MISSING — keine VC-ID (BLOCKER)** | pending-watcher | no | none | real-boundary-smoke |
| ~~REQ-040~~ | **deprecated 2026-07-20** → REQ-041, REQ-042 | ~~VC-040 existierte nie~~ | — | — | — | — |
| **REQ-041** | **MISSING — VIS-014 reserved, Inhalt MISSING (BLOCKER)** | **MISSING — keine VC-ID (BLOCKER)** | pending-watcher | no | none | real-boundary-smoke |
| **REQ-042** | docs/vision/revyr-endurance-platform.vision.md#VIS-003 (**ungeprüfte ASSUMPTION**, hier nicht hochgestuft, §3) | **MISSING — keine VC-ID (BLOCKER)** | pending-watcher | no | none | real-boundary-smoke |

### `evidence-class-required` — Klassendefinition

| Klasse | Bedeutung |
|---|---|
| unit-fake | Reine Logik, vollständig mit Fixtures/Mocks beweisbar. |
| integration-fake | Modulverbund gegen In-Memory-/Fake-Boundary beweisbar. |
| real-boundary-smoke | Mindestens ein Durchlauf gegen die **echte** Grenze (reales Gerät, echte OS-API, echter Endpunkt, echter Sensor), je Plattform und — wo einschlägig — je Sportart. |
| production-verified | Eigenschaft ist nur unter realen Feld-/Betriebsbedingungen über Zeit nachweisbar. Ein einzelner Smoke-Durchlauf reicht nicht. |

Die Begründung der Mindestklasse je Requirement steht in §3.

---

## 6. BLOCKER, MISSING, ASSUMPTION und offene Entscheidungen

Nichts hier wird durch eine plausible Annahme ersetzt.

### 6.1 Canvas-BLOCKER (Requirements ohne tragfähigen atomaren Anker)

**Stand nach Runde 4: 16** (nach dem Auftau-Schritt 2 waren es 12, davor 17). **Vier sind
hinzugekommen, keiner ist geschlossen worden.** Die Zahl ist aus der Tabelle unten **gezählt**,
nicht fortgeschrieben.

⚠️ **Die vier neuen BLOCKER sind keine neuen Defekte, sondern aufgedeckte.** REQ-037, REQ-038 und
REQ-039 hatten bis zum 2026-07-20 einen canvas-problem-Anker, der die falsche Aussage trug
(verbotene Schlusskette bzw. CAN-013 als Universal-Anker). REQ-041 und REQ-042 erben die Lücke
von REQ-040. **Die Zahl steigt, weil die Prüfung schärfer geworden ist — nicht, weil das Produkt
schlechter geworden wäre.** Eine sinkende BLOCKER-Zahl wäre hier das schlechtere Ergebnis
gewesen.

| REQ-ID | BLOCKER |
|---|---|
| REQ-006 | CAN-019 (Planungs- und Orientierungsproblem vor der Aktivitaet) ist reserviert und inhaltlich MISSING. REQ-006 hat damit keinen atomaren Canvas-Problembezug, sondern nur Capability- und Constraint-Anker. Zaehlt laut Canvas nicht als erfuellte Canvas-Referenz. |
| REQ-007 | CAN-019 (Planungs- und Orientierungsproblem) ist reserviert und inhaltlich MISSING - kein atomarer Canvas-Problembezug fuer REQ-007. |
| REQ-015 | CAN-016 (Fortschritts- und Motivationsproblem) ist reserviert und inhaltlich MISSING - REQ-015 hat keinen atomaren Canvas-Problembezug; Fortschritt erscheint nur als Wertversprechen (CAN-030/CAN-034), nicht als Problem. |
| REQ-016 | CAN-016 (Fortschritts- und Motivationsproblem) ist reserviert und inhaltlich MISSING - REQ-016 hat keinen atomaren Canvas-Problembezug. |
| REQ-023 | CAN-020 (Fairness- und Manipulationsproblem) ist reserviert und inhaltlich MISSING - REQ-023 hat keinen atomaren Canvas-Problembezug; Fairness erscheint nur als Wertversprechen (CAN-033/CAN-036) und Risiko (CAN-104/CAN-109). |
| REQ-024 | CAN-020 (Fairness- und Manipulationsproblem) ist reserviert und inhaltlich MISSING - REQ-024 hat keinen atomaren Canvas-Problembezug. |
| REQ-028 | Mehrfacher BLOCKER. (1) CAN-021 (Problem hinter Einzel-Revieren und Sportplatz-Challenges) ist reserviert und inhaltlich MISSING. (2) Keine Nachfolgeklausel der Wertversprechen-Gruppe deckt Einzel-Reviere - CAN-032 fordert ausdruecklich Gemeinschaft, Einzel-Reviere sind per Definition nicht gemeinsam. (3) Kein Erfolgssignal: CAN-124..CAN-130 kennen kein Einzel-Revier-Signal. Das REQ haengt damit nur an der Capability CAN-065 und an Risiko-Items. |
| REQ-029 | Staerkster Canvas-BLOCKER. (1) CAN-021 (Problem hinter Sportplatz-Challenges) ist reserviert und inhaltlich MISSING. (2) Es existiert KEIN atomares Capability-Item fuer Sportplatz-Challenges oder Bahngold - CAN-047..CAN-070 nennen weder das eine noch das andere; CAN-061 (Challenges) traegt laut Registry REQ-025, nicht REQ-029. (3) Kein Erfolgssignal. Es bleiben nur die beiden Risiko-Items CAN-107/CAN-110 und die schwache Wertklausel CAN-030. Zuordnung wurde nicht erfunden. |
| REQ-030 | Doppelter BLOCKER. (1) CAN-017 (Sicherheitsproblem) ist reserviert und inhaltlich MISSING - der Canvas nennt kein Sicherheitsproblem, VIS-003 dagegen 'sicheren Zugang'; dokumentierte Canvas/Vision-Divergenz. (2) CAN-031 ('Trainiere sicherer') ist als Wertklausel gefuehrt, laesst aber laut Canvas offen, ob Trainings- oder Datensicherheit gemeint ist - die Klausel ist bis zur Klaerung nicht pruefbar und traegt REQ-030 deshalb nur vorbehaltlich. |
| REQ-031 | CAN-017 (Sicherheitsproblem) ist reserviert und inhaltlich MISSING - REQ-031 hat keinen atomaren Canvas-Problembezug. CAN-031 traegt nur vorbehaltlich, weil 'sicherer' im Canvas undefiniert ist. |
| REQ-034 | CAN-018 (Datenschutzproblem) ist reserviert und inhaltlich MISSING - REQ-034 hat keinen atomaren Canvas-Problembezug; Datenschutz erscheint nur als Constraint (CAN-088) und Risiko (CAN-105). |
| **REQ-039** *(neu identifiziert 2026-07-19, verschärft 2026-07-20)* | **Der Canvas führt kein Portabilitäts- oder Lock-in-Problem.** Die Capability ist mit **CAN-139** vollständig verankert, das **Problem** dahinter — „meine Daten lassen sich nicht mitnehmen“ — existiert im Canvas nicht. **CAN-013 ist am 2026-07-20 als Anker entfernt**, nicht mehr nur als „schwach“ gekennzeichnet: die Kennzeichnung stand direkt neben der Verknüpfung, und eine maschinelle Prüfung liest die Verknüpfung, nicht den Vorbehalt. Anders als bei REQ-038 ist das **keine begründete Nichtanwendbarkeit**: GPX-Export ist eine Nutzer-Capability mit einem echten Nutzerproblem, das der Canvas nur nicht führt. |
| **REQ-037** *(neu 2026-07-20)* | **Der Canvas führt kein Zugänglichkeitsproblem.** Die beiden bisherigen Anker liefen über die in Registry §6.1.1 **verbotene** Kette „Wahrnehmbarkeit als Vorstufe von Verständlichkeit“ — CAN-013 in §4.1 und CAN-029 in §4.2 — und sind entfernt. Keines der reservierten Items CAN-016…CAN-021 deckt Zugänglichkeit ab. **Keine Problem-ID vergeben, kein Item umgedeutet.** Registry §8 Punkt 37. |
| **REQ-038** *(neu 2026-07-20, Einstufung strittig — offengelegt)* | Der canvas-problem-Wert ist **MISSING (begründet)**: eine Gestaltungssprache ist eine **Constraint** (CAN-141), kein Nutzerproblem — Registry §7.5.5 verlangt genau diesen Wert. **Registry §8 Punkt 37 zählt REQ-038 dennoch zu den drei Requirements ohne canvas-problem-Anker und stuft das als BLOCKER ein.** Beide Aussagen stehen in derselben eingefrorenen Registry. Die Zeile steht hier mit, damit die BLOCKER-**Zählung** nicht von der Registry abweicht; die Begründung der Nichtanwendbarkeit bleibt in §6.4 stehen. **Die Divergenz wird nicht einseitig aufgelöst** — das ist eine Nutzerentscheidung. |
| **REQ-041** *(neu 2026-07-20)* | **Der Canvas führt kein Planungs- oder Wiederverwendungsproblem.** **CAN-019** („Planungs- und Orientierungsproblem vor der Aktivität“) ist `reserved` und inhaltlich MISSING — dieselbe Lücke wie bei REQ-006 und REQ-007. Der CAN-013-Bezug des Vorgängers REQ-040 ist entfernt und wird **nicht vererbt**; er betraf die Vergleichshälfte. |
| **REQ-042** *(neu 2026-07-20)* | **Der Canvas führt kein Vergleichsproblem** („ich kann nicht erkennen, ob ich schneller geworden bin“). Der Anker CAN-013 lief über dieselbe verbotene Kette („Vergleich erzeugt Bedeutung“) und ist entfernt. Der Wertanker **CAN-030** trägt (Fortschritt erkennen) — das ersetzt aber kein Problem-Item. |

**Geschlossen im Auftau-Schritt 2 (2026-07-19) — fünf Einträge:**

| REQ-ID | Früherer BLOCKER | Auflösung |
|---|---|---|
| REQ-008 | CAN-071 (Verlauf, Detailansicht und GPX-Export) `reserved`, Inhalt MISSING | CAN-071 **deprecated**, ersetzt durch CAN-138/139/140; REQ-008 hat mit **CAN-138** erstmals einen vollständig passenden atomaren Capability-Anker |
| REQ-009 | CAN-025 („Ambitionierte Ausdauersportler:innen“) ohne PRD-USER-ID | **USER-004** vergeben und im PRD eingetragen; Verknüpfung nach semantischer Einzelprüfung als **sekundär** bestätigt |
| REQ-011 | CAN-025 ohne PRD-USER-ID | **Ersatzlos gestrichen.** Der Vermerk war in **beiden Richtungen** unzutreffend: die USER-ID existiert inzwischen, **und** REQ-011 braucht sie nicht (§3). Nicht durch USER-004 ersetzt. |
| ~~REQ-014~~ | Doppelter BLOCKER: CAN-099 `reserved` **und** kein atomares Item für das monochrome Designsystem | REQ-014 ist **deprecated**. Beide Lücken sind bei den Nachfolgern geschlossen: **CAN-099** (`active`, nur Accessibility) trägt REQ-037, **CAN-141** trägt REQ-038. |
| REQ-019 | CAN-130 („übernommene Routen pro Empfehlung“) `reserved`, Inhalt MISSING | **CAN-130** ist `active` und vollständig spezifiziert (Registry §6.3.2). **Geschlossen ist die Definition, nicht der Nachweis** — `evidence_status` planned, `empirical_result` MISSING. |
| REQ-032 | CAN-022 (Problem hinter Wearable- und Sensoranbindung) `reserved` **und** CAN-025 ohne USER-ID | **CAN-022** ist `active` (Item Type PROBLEM), **USER-004** vergeben. **Der Canvas-BLOCKER ist geschlossen; ein Vision-BLOCKER bleibt** (§6.1.1) — er ist kein Canvas-BLOCKER und wird hier nicht mitgezählt. |

Die verbleibenden zugrunde liegenden reservierten Canvas-IDs (`status = reserved`, Inhalt
MISSING) sind **CAN-016 … CAN-021** — **sechs**; die frühere Angabe „zehn (CAN-016…022, CAN-071,
CAN-099, CAN-130)“ ist ein Altstand. **CAN-022, CAN-099 und CAN-130 sind `active`, CAN-071 und
CAN-140 sind `deprecated`.** Den Inhalt der sechs zu ergänzen hieße, neue Produktsubstanz zu
erfinden — das ist eine Nutzerentscheidung, keine Ableitung.

### 6.1.2 Canvas-Lücken anderer Art — **getrennt gezählt, nicht in §6.1 addiert**

§6.1 zählt ausschließlich **fehlende Problem-Anker**. Die folgenden Befunde sind Lücken anderer
Kategorie und werden deshalb **nicht** mitgezählt; sie in dieselbe Zahl zu werfen würde beide
Zahlen unbrauchbar machen.

| REQ-ID | Lücke | Art |
|---|---|---|
| **REQ-004** *(neu 2026-07-20)* | **Kein atomares Capability-Item.** Die drei Anker waren ein **Risiko** (CAN-100), ein **Wertversprechen** (CAN-028) und eine **Evidence-Annahme** (CAN-113). Keines davon sagt zu, dass das Produkt ein GPS-Datenmodell mit deterministischem Filter **hat**. Bis zum 2026-07-20 stand **CAN-100 — ein Risiko-Item — in der Kernmatrix-Spalte „Canvas Item (primär, atomar)"**. Eine Prüfung „hat jedes Requirement einen Canvas-Link?" bestand das. **CAN-048** („Robustes Foreground-Tracking") trägt laut Registry REQ-002 und wurde **nicht** mitbenutzt. | **BLOCKER**, Nutzer |
| **CAN-050** *(Registry §8 Punkt 39)* | **CAN-050 („Routenplanung UND gespeicherte Routen") ist selbst ein Composite** und wurde zusätzlich in zwei Requirement-Kontexten geführt (REQ-006 laut Registry, REQ-008 laut dieser Matrix). Die Doppelführung bei REQ-008 ist am 2026-07-20 **aufgelöst**; die **Atomisierung** von CAN-050 ist es **nicht** und wird hier nicht vorweggenommen. | **BLOCKER**, Nutzer |
| **REQ-039, REQ-041** | **Keine Wertversprechen-Gruppe deckt Portabilität/Kontrolle bzw. Vorbereitung/Planung ab.** CAN-028…CAN-038 enthält weder das eine noch das andere. Bei REQ-039 ist die Lücke durch den dualen Item Type von **CAN-139** operativ überbrückt, **nicht geschlossen**; bei REQ-041 steht sie offen als MISSING. | **MISSING**, Nutzer |

### 6.1.1 Vision-BLOCKER (getrennt geführt, nicht mit Canvas-BLOCKERn vermischt)

Vision- und Canvas-Lücken bestehen **unabhängig voneinander** (Registry §6.1.1). Sie werden
deshalb getrennt gezählt; ein Vision-BLOCKER ist kein Canvas-BLOCKER.

| REQ-ID | Vision-BLOCKER | Zeilenstatus |
|---|---|---|
| REQ-032 | **Kein VIS-Item** trägt „vollständige und erklärbare Trainingsdaten“. VIS-005 war der bisherige, fachlich unpassende Anker und ist entfernt. **Anders als bei REQ-038 und REQ-039 ist hier nicht einmal eine VIS-ID reserviert** — es ist eine MISSING-Position, keine reservierte Leerstelle. | `broken` |
| REQ-037 | **VIS-011 ist ASSUMPTION und unbestätigt** und zählt nach Registry §8 Punkt 15 **nicht** als erfüllter Vision-Anker. Der Anker ist *belegt und benannt*, aber nicht *bestätigt*. | `not-linked` |
| REQ-038 | **VIS-012 ist `reserved`, Inhalt MISSING.** Kein bestehendes VIS-Item trägt ein Designprinzip auf Vision-Ebene; VIS-011 deckt ausdrücklich nur die Accessibility-Hälfte ab. | `broken` |
| REQ-039 | **VIS-013 ist `reserved`, Inhalt MISSING.** VIS-003 nennt keine Portabilität, VIS-009 regelt Sichtbarkeit statt Mitnahme. | `broken` |
| **REQ-006** *(neu 2026-07-20, registry-beauftragt)* | **VIS-003 trägt Routenplanung nicht** und ist entfernt. Die Prüfung war von Registry §8 Punkt 40 ausdrücklich diesem Owner aufgetragen („nicht zu übernehmen, weil er existiert“). VIS-003 nennt Tracking, Health-Auswertung, Fortschrittssignale und Zugang zu Trainingspartnern — eine Route **vor** dem Start zu planen ist keines davon. **Keine reservierte VIS-ID** — MISSING-Position, keine Leerstelle. Konsistenz: dieselbe Lesart ist für REQ-041 verworfen worden, und dafür wurde eigens VIS-014 reserviert. | `broken` |
| **REQ-031** *(neu 2026-07-20)* | **VIS-007 trägt Sturzerkennung nicht** und ist entfernt. VIS-007 regelt **Health-Ausgaben** (Score, Empfehlungen); REQ-031 erzeugt keine. „Assistenz, keine Garantie“ und „Orientierung, keine Diagnose“ sind zwei **verschiedene** Haftungsvorbehalte, keine gemeinsame Aussage. VIS-003, VIS-009 und VIS-010 einzeln geprüft und verworfen (VIS-010 nennt „Safety-System“ wörtlich, ist aber eine **Freigabebedingung** — derselbe Grund, aus dem VIS-005 für REQ-032 verworfen wurde). **Keine reservierte VIS-ID.** | `broken` |
| **REQ-041** *(neu 2026-07-20)* | **VIS-014 ist `reserved`, Inhalt MISSING.** VIS-003 und VIS-004 geprüft — keines nennt die Wiederverwendung geplanter Strecken. | `broken` |
| **REQ-042** *(neu 2026-07-20, ersetzt REQ-040)* | **VIS-003 ist eine ungeprüfte ASSUMPTION** des Traceability-Owners, aus TRC-040 übernommen und hier **nicht hochgestuft**. „Konkrete Fortschrittssignale“ trägt einen Aktivitätsvergleich **plausibel**; ob es ihn **trägt**, ist ungeklärt. | `linked-partial` |
| **REQ-019** *(verschärft 2026-07-20, Runde 5)* | **VIS-003 entfernt — kein Vision-Anker mehr.** Die Vorfassung führte `linked-partial` mit der Begründung, die „Feed-/Zugangs-Hälfte“ sei getragen. **Diese Hälfte war selbst eine Ableitung:** VIS-003 nennt Zugang zu **Trainingspartnern**, nicht einen Feed; die tragende Verbindung lief über das erfundene Zwischenglied „Feed = Entdeckungsfläche für diesen Zugang“. Eine Ableitung über ein Zwischenglied ist kein Beleg (Registry §6.1.1). **Quellenprüfung Vision-Ebene vollständig durchgeführt** (SRC-001 Teil 1 §1.1–§1.4; SRC-003 §1.1–§1.3): **keine Stelle nennt Routenempfehlung oder Feed.** Der Inhalt steht wörtlich in SRC-001 **§2.5** („TEIL 2 — PRODUCT CANVAS“) und SRC-003 **§4.2** — Canvas- und Spezifikationsebene, nicht Vision. **Keine reservierte VIS-ID.** Details in §3. | `broken` |
| **REQ-007** *(neu 2026-07-20, Runde 5)* | **VIS-003 entfernt.** Die Vorfassung führte hier eine OPEN QUESTION („aus dem Wortlaut nicht entscheidbar“) und ließ den Anker auf `linked` stehen. **Die Quellen entscheiden die Frage:** „Fortschritt“ wird in SRC-001 §1.2, §2.1, §3.3 und SRC-003 §1.1 durchgehend **longitudinal** gebraucht (Verbesserung über die Zeit, Punkte/Ränge/Seasons); die **aktivitätsinterne** Restdistanz erscheint ausschließlich funktional (SRC-001 **T-02** „geplante vs. verbleibende km“, SRC-003 §9 GATE A „verbleibende km korrekt“) — **nie auf Vision-Ebene**. Konsistenz: für **REQ-006**, die Planungshälfte desselben Modus B, ist VIS-003 aus genau diesem Grund entfernt. **Keine reservierte VIS-ID.** Details in §3. | `broken` |
| **REQ-021** *(neu 2026-07-20, Runde 5)* | **VIS-004 trägt nur die Team-Hälfte.** „lokale Teams“ nennt die **Existenz** des Teams; REQ-021 fordert **aktive Mitglieder und Wachstum**. Die Vorfassung überbrückte das mit „Fortbestand derselben Aussage“ — eine Ableitung. Der Anker bleibt, weil die Team-Hälfte **wörtlich** getragen ist; der Status nicht. Wachstum ist in SRC-003 §1.2 als **USP** belegt, nicht auf Vision-Ebene. Keine zweite Verknüpfung gesetzt. | `linked-partial` |
| **REQ-022** *(neu 2026-07-20, Runde 5)* | **VIS-003 trägt nur die Aktivitäts-Hälfte.** REQ-022 hat zwei Gegenstände — gemeinsame Aktivitäten **und Events**. VIS-003 („Zugang zu lokalen Trainingspartnern“) trägt den ersten; **Events nennt kein Vision-Item**. Sie erscheinen als SRC-001 **L-05** und SRC-003 **Plan 14**, beides funktionale Ebene. Keine zweite Verknüpfung gesetzt, kein Item umgedeutet. | `linked-partial` |
| **REQ-004** *(neu 2026-07-20, Runde 6)* | **VIS-003 bleibt, zählt aber nicht als erfüllt.** Die tragende Klausel war „Nutzer benötigen **verlässliches Tracking**”. Der Qualifizierer „verlässlich” steht in **keiner** der vier Quellen (`docs/sources/`, **0 Treffer**); belegt ist auf Bedürfnisebene nur „tracken” ohne Qualifizierer (`SRC-003-REVYR-GESAMTPLAN-FINAL.md:64`). Die Qualitätsforderung existiert ausschließlich als **NFR** (`SRC-001-REVYR-Vision-Canvas-PRD.md:250` Genauigkeit, `:252` Zuverlässigkeit). Der Schritt „Produktqualitätsanforderung ⇒ Nutzerbedürfnis” ist ein **Ebenensprung** und damit dieselbe Ableitungsform, die in Runde 5 bei REQ-007 und REQ-019 verworfen wurde. **Anders als dort wird der Anker nicht entfernt:** VIS-003 ist vorhanden und fachlich passend, nur sein Beleggrad ist ASSUMPTION und unbestätigt — die Lage von REQ-037/VIS-011. Deshalb `not-linked`, **nicht** `broken`. ⚠️ **Abweichung von der Gegenprüfung offengelegt:** die Folgenlinse verlangte `broken`; umgesetzt ist die mildere Einstufung, weil `broken` ein fehlendes Kettenglied behauptet hätte. **Keine VIS-ID vergeben, kein Item umgedeutet.** Endgültige Einstufung hängt an der Nutzerentscheidung über den ASSUMPTION-Rest von VIS-003. | `not-linked` |
| ~~REQ-040~~ | **deprecated 2026-07-20** → REQ-041, REQ-042. Der frühere Befund („VIS-003 trägt nur die Vergleichshälfte”) ist **nicht vererbt**, sondern auf beide Nachfolger **neu bewertet** worden. | — |

**In keinem dieser Fälle wurde ein VIS-Item umgedeutet.** Das wäre exakt der Defekt
VIS-009 ↔ REQ-014, der am 2026-07-19 behoben wurde — ein syntaktisch gültiger, plausibel
lesbarer, fachlich falscher Anker, den eine maschinelle Prüfung als *erfüllt* zählt.

**Zusätzlich geprüft und ausdrücklich NICHT geändert**, damit Schweigen nicht als „geklärt“
gelesen wird:

| REQ-ID | Anker | Ergebnis |
|---|---|---|
| **REQ-030** | VIS-009 | **Trägt.** VIS-009 nennt „Live-Standort ist pro Aktivität **Opt-in**, zeitlich begrenzt und start-/endpunktverschleiert" — das ist AC-030 wörtlich. REQ-030 teilt sich mit REQ-031 den Canvas-Anker CAN-068, aber ihre Vision-Lage ist verschieden: Sichtbarkeit/Privacy gegen Sensorik/Assistenz. Zeilenstatus bleibt `linked`. |
| **REQ-007** | VIS-003 | **Erledigt am 2026-07-20 in Runde 5 — Zeile nach oben in die BLOCKER-Tabelle verschoben.** Die frühere Einstufung „OPEN QUESTION, aus dem Wortlaut nicht entscheidbar“ hatte eine Prämisse, die **entfallen ist**: die Quelldokumente waren nicht lesbar. Sie sind es seit dem 2026-07-20, und sie entscheiden die Frage gegen den Anker. **Ein „nicht entscheidbar“, das nur auf fehlendem Quellenzugriff beruht, ist keine Eigenschaft des Wortlauts** — es war eine Aussage über den Prüfstand, formuliert wie eine Aussage über den Text. |

### 6.2 Owner-Blocker (alle aktiven Requirements)

OQ-002 (finaler Repository-Owner/DRI) ist offen. **Kein aktives Requirement trägt einen echten
Owner**; alle tragen stattdessen einen sichtbaren OWNER-BLOCKER mit Verweis auf OQ-002 (Wortlaut
je Requirement in §3) — die vier am 2026-07-19 hinzugekommenen eingeschlossen. Die Zahl ist die
aus der Registry abgeleitete (§0.0), nicht 36. Der dokumentierte Default bei Nichtauflösung
lautet laut `docs/decisions/open-questions.md`: „Umsetzung bleibt organisatorisch unzugeordnet.“

**Zwei Owner-Blocker über OQ-002 hinaus, neu am 2026-07-19:**

| Was | Requirement | Befund |
|---|---|---|
| **Auditor für den WCAG-2.2-AA-Audit** | REQ-037 | **MISSING** — kein Auditor benannt. Ein Audit ohne benannten Auditor ist keine planbare Abnahme. |
| **Owner der Telemetrie-Instrumentierung** | REQ-019 | **MISSING** (OQ-012). Ohne ihn ist EV-041 nicht zuweisbar. |
| **Entscheider der Vergleichbarkeitsdefinition** | **REQ-042** *(nachgezogen 2026-07-20: REQ-040 ist deprecated)* | **MISSING** (OQ-015). **REQ-041 braucht diesen Entscheider nicht** — die Teilung hat den Owner-Bedarf halbiert. |

### 6.3 Querschnittsbefund — Messlücke Telemetrie · **für ein Requirement adressiert, für vier offen**

Kein Requirement, kein NFR und kein Canvas-Item beschrieb eine Analytics- oder
Telemetrie-Erhebung. Damit waren **alle fünf PRODUCT_OUTCOME-Signale** (REQ-010, REQ-013,
REQ-019, REQ-020, REQ-022) sowie die Check-in-Quote aus REQ-012 **nicht erhebbar**. Zugleich
fordern CAN-095 (local-first ab A0/A1) und REQ-034 (Datensparsamkeit) Zurückhaltung — jede
Erhebung kollidiert mit beiden.

**Teilweise adressiert seit dem 2026-07-19 — ausschließlich für REQ-019.** Mit **CAN-130** ist
eine privacy-minimierte Telemetrie **inhaltlich spezifiziert**: sechs zulässige Ereignisse,
sieben zulässige Felder, eine abschließende Liste unzulässiger Felder, **kein paralleler
Standort- oder Verhaltenstracker**, Aggregation möglichst aus ohnehin nötigen
Backend-Ereignissen. Die verbleibende Entscheidung ist als **OQ-012** geführt.

⚠️ **Für REQ-010, REQ-012, REQ-013, REQ-020 und REQ-022 bleibt die Messlücke unverändert offen.**
Sie wird **nicht** stillschweigend aus CAN-130 mitgelöst: CAN-130 spezifiziert Ereignisse zu
**Routenempfehlungen**, nicht zu Score-Aufrufen, Stimmungs-Check-ins, Teambeitritten oder
gemeinsamen Aktivitäten. Wer aus der Existenz von CAN-130 schließt, die Telemetriefrage sei
erledigt, überträgt eine Lösung auf vier Fälle, für die sie nichts aussagt. **OPEN QUESTION** für
den DRI, berührt OQ-005.

### 6.4 Begründete Nichtanwendbarkeit (requirement-spezifisch)

Kein pauschales „nicht relevant“ und kein „später“. Jede Nichtanwendbarkeit ist am einzelnen
Requirement begründet:

- REQ-005: sportgetrennte Messung nicht anwendbar - die Persistenzschicht speichert fuer Run und Bike dieselbe Trackpunkt-Struktur; sportabhaengig sind nur die abgeleiteten Metriken (REQ-001).
- REQ-037 (übernimmt den Befund des deprecateten REQ-014): kein Nutzersignal - eine Nutzungsquote von Screenreader-Nutzern kann WCAG-Konformitaet weder belegen noch widerlegen und setzt falsche Anreize (Verzicht auf Zugaenglichkeit bei kleiner Nutzergruppe). Sporttrennung bleibt anwendbar - die sportspezifischen Tracking-Screens zeigen unterschiedliche Labels und Kernmetriken, also sind auch die Screenreader-Ausgaben verschieden.
- REQ-038: kein Nutzersignal - ob Farbe sparsam eingesetzt wird, ist unabhaengig davon messbar, wie viele Nutzer den Screen sehen; ein Aesthetik- oder Zufriedenheitswert waere ein Kategorienfehler. Sporttrennung ist hier **nicht** unanwendbar, sondern selbst Pruefgegenstand: 'Run und Bike werden nicht ausschliesslich durch Farbe unterschieden' ist eine der drei Pass-Bedingungen. **Zur Nichtanwendbarkeit des Canvas-Problem-Items siehe den eigenen Punkt weiter unten** (2026-07-20 praezisiert, weil die Abgrenzung jetzt vier statt einem Vergleichsfall nennt).
- REQ-039: kein Nutzersignal - der pruefbare Kern ist Erzeugbarkeit und Interoperabilitaet; eine Exportquote waere erfunden und stuende zudem in Spannung zur Datenminimierung. Sporttrennung ist zwingend, weil die exportierten Kernmetriken sportartspezifisch sind.
- REQ-041: kein Nutzersignal und **keine Wiederverwendungsquote** - der pruefbare Kern ist die Wiederherstellungstreue einer gespeicherten Route, nicht deren Nutzungshaeufigkeit. Sporttrennung ist hier **selbst Pruefgegenstand** (Kriterium (d): das sportartspezifische Routingprofil bleibt beim Laden korrekt), nicht blosser Kontext.
- REQ-042: kein Nutzersignal und keine Vergleichsquote - der pruefbare Kern ist die Korrektheit der Vergleichsaussage, nicht deren Nutzung. Sporttrennung ist **strikt zwingend**: eine Radfahrt und ein Lauf ueber dieselbe Geometrie sind physikalisch unvergleichbar, ein sportuebergreifender 'Rekord' waere eine falsche Produktaussage.
- REQ-038: **kein atomares Canvas-Problem-Item**, requirement-spezifisch begruendet - eine Gestaltungssprache ist eine Constraint (CAN-141), kein Nutzerproblem. Der Canvas fuehrt zu Recht keines. Das unterscheidet REQ-038 von REQ-037, REQ-039, REQ-041 und REQ-042, wo jeweils ein **echtes** Nutzerproblem existiert, das der Canvas nur nicht fuehrt (§6.1). ⚠️ Registry §8 Punkt 37 stuft REQ-038 dennoch als BLOCKER ein; die Divergenz ist in §3, §4.1 und §6.1 offengelegt und **nicht** einseitig aufgeloest.
- REQ-015: kein Nutzersignal und keine Sporttrennung fuer die Kontrolle selbst - Unlock-Idempotenz und Kaufpfad-Freiheit sind sportneutrale Katalogeigenschaften; ein Freischaltungsziel wuerde genau den Anreiz erzeugen, den CAN-075 verbietet.
- REQ-016: kein Nutzersignal - fuer Recaps, Erfolgskarten und Live-Status existiert in CAN-124..CAN-129 und VIS-006 kein Erfolgssignal; eine Teilenquote waere erfunden.
- REQ-017: sportgetrennte Messung nicht anwendbar - Auth, Sync und Loeschung wirken auf denselben Datenbestand; sportabhaengig ist nur die Vollstaendigkeit der migrierten Inhalte (Stichprobe je Sportart).
- REQ-018: kein Nutzersignal und keine Sporttrennung - Sichtbarkeits- und Blockierregeln haengen am Nutzer, nicht an der Sportart; entscheidend ist, dass die Matrix haelt, auch wenn niemand sie bewusst nutzt.
- REQ-020: sportgetrennte Messung der Mitgliedschaft nicht anwendbar - Teams sind laut PRD keine sportgetrennte Einheit; sportgetrennt sind Rankings, Challenges und Rekorde (REQ-023, REQ-025).
- REQ-025: kein Produktsignal - docs/traceability.md haelt ausdruecklich fest, dass kein Challenge- oder Ranking-Signal existiert; ein Teilnahmeziel wuerde diese dokumentierte Luecke verdecken.
- REQ-027: sportgetrennte Messung nicht anwendbar - Rollover wirkt auf Besitzstaende und Snapshots ohne eigene Sportart; sportgetrennt sind nur die darin gespeicherten Rekorde. Das Produktsignal Season-Teilnahme (CAN-129) wird bei REQ-026 gefuehrt, weil ein korrekter Rollover es weder belegen noch widerlegen kann.
- REQ-029: die Bike-Anwendbarkeit wird ausdruecklich NICHT als nicht-anwendbar erklaert - docs/traceability.md fuehrt sie als OPEN QUESTION; eine Rad-Entsprechung zur Laufbahn ist eine offene Produktfrage, keine Ableitung.
- REQ-030: kein Nutzersignal - eine Nutzungsquote der Live-Freigabe waere als Ziel schaedlich, weil das Produkt keine Anreize zur Standortpreisgabe setzen darf. Sporttrennung nur mittelbar (Endpfad-Matrix wird je Sportart durchlaufen, weil Bike groessere Distanzen und Netzluecken umfasst).
- REQ-031: kein Nutzersignal - jede Ausloesung ist ein unerwuenschtes Ereignis; eine Ausloesequote als Ziel waere pervers. Sporttrennung dagegen zwingend (unterschiedliche Sturzsignaturen).
- REQ-033: kein Nutzersignal vor dem Gate - solange die Funktionen rechtlich nicht erscheinen duerfen, kann es definitionsgemaess kein Nutzungssignal geben.
- REQ-034: sportgetrennte Messung der Zugriffsregeln nicht anwendbar - sie wirken datenbestandsweit; die Datenminimierungspruefung wird dennoch je Sportart durchlaufen, weil bei Bike mehr Sensorik anfaellt (REQ-024).
- REQ-035: kein Nutzersignal - Prozessanforderung ohne unmittelbaren Nutzerkontakt (Canvas-Anker CAN-123). Ein Retentionsziel fuer Evidence-Ledger-Disziplin waere ein Kategorienfehler. Sporttrennung ist hier gerade NICHT unanwendbar: der Ledger muss Run und Bike getrennt fuehren (CAN-114).
- REQ-036: kein Nutzersignal - Prozess-/Compliance-Anforderung ohne unmittelbares Nutzerproblem (Canvas-Anker CAN-083). Downloads oder Bewertungen sagen ueber Policy-Konformitaet nichts aus.

Ausdrücklich **nicht** für nicht-anwendbar erklärt: die Bike-Anwendbarkeit von REQ-029 bleibt
OPEN QUESTION.

### 6.5 Divergenzen zwischen Vorfassung und Messmodell

Diese Matrix löst sie **nicht** eigenmächtig auf, sondern macht sie sichtbar.

| # | Divergenz | Betroffen | Behandlung hier |
|---|---|---|---|
| 1 | Die Vorfassung verknüpfte REQ-012 mit VIS-003, das Messmodell mit VIS-006 und VIS-007. | REQ-012 | VIS-003 bleibt primärer Vision-Link (so in Registry TRC-012 hinterlegt); VIS-006/VIS-007 stehen in §3 als ergänzende Vision-Items. Auflösung offen. |
| 2 | Erfolgssignal REQ-021: Vorfassung CAN-127 (Team nach 60 Tagen), Messmodell CAN-128 (gemeinsame Aktivität). | REQ-021 | Beide Zuordnungen sind dokumentiert; §4.2 nennt die Divergenz. Auflösung offen. |
| 3 | Erfolgssignal CAN-129: Vorfassung führte es bei REQ-026 **und** REQ-027, das Messmodell ausschließlich bei REQ-026 (ein korrekter Rollover kann Season-Teilnahme weder belegen noch widerlegen). | REQ-026, REQ-027 | Beide Zuordnungen dokumentiert; §4.2 nennt die Divergenz. Auflösung offen. |
| 4 | `docs/traceability.md` verknüpfte REQ-014 (Designsystem und Accessibility) mit VIS-009 (Privacy Boundary) — fachlich unpassend; zum Zeitpunkt des Befundes deckte **kein** VIS-Item Accessibility ab. | REQ-014 | **Behoben am 2026-07-19, nicht mehr nur vermerkt.** Die Vorfassung ließ VIS-009 „als registrierten Link stehen" — das war die schwächere Behandlung (Begründung §0.1). Der Anker ist auf **VIS-011 (Accessibility Boundary)** umgehängt, im Auftau-Schritt in der Registry vergeben. **Restbefund, der bleibt:** VIS-011 ist `source_type = ASSUMPTION` und vom Nutzer **nicht bestätigt**; er zählt bis dahin nicht als erfüllter Vision-Anker (`ID-REGISTRY.md` §8 Punkt 15). Die Divergenz ist damit von „falscher Anker" auf „unbestätigter Anker" reduziert — **nicht** geschlossen. |
| 5 | Diese Matrix verknüpfte **REQ-032** (Wearables und Bike-Sensorik) mit **VIS-005** (Project Goal). VIS-005 formuliert eine **Freigabebedingung** („erst nach nachgewiesener Datenqualität … freischalten“), keine Zusage über die **Vollständigkeit der Signalbasis**. | REQ-032 | **Anker am 2026-07-19 entfernt, nicht kommentiert** — derselbe Fehlertyp wie VIS-009 ↔ REQ-014 und dieselbe Behandlung. Befund stammt vom Owner der Vision-Datei und ist hier umgesetzt, weil die Matrixzeile in meiner Ownership liegt. **Restbefund:** REQ-032 hat jetzt **überhaupt keinen** Vision-Anker, und es ist **nicht einmal eine VIS-ID reserviert** — die Divergenz ist von „falscher Anker“ auf „kein Anker“ verschoben, **nicht geschlossen**. Ein Item umzudeuten wäre die schlechtere Lösung. |
| 6 | **Registry-Kettenfelder ↔ Matrixzeilen.** `ID-REGISTRY.md` §6.6 führt für **TRC-008, TRC-019 und TRC-032** noch die Kette mit dem **deprecateten Sammelblock-Item CAN-005**, für TRC-032 zusätzlich VIS-005. | TRC-008, TRC-019, TRC-032 | **Kein Widerspruch in der Sache, sondern ein bekannter Nachzug:** die Registry weist die Canvas-Spalte dieser Zeilen ausdrücklich dem **Traceability-Owner in Phase 3** zu. Umgestellt auf CAN-138 (TRC-008), CAN-130 (TRC-019) und CAN-022 (TRC-032); der Vision-Anker von TRC-032 ist entfernt. **Die Registry ist eingefroren und wurde nicht angepasst** — das Kettenfeld dort bildet damit den Altstand ab. Sichtbar gemacht statt still divergiert; Nachzug in §9. |
| 7 | **`source_type`: Matrix ↔ PRD.** Diese Matrix führte 17 Requirements als `EXPLICIT`; `docs/prd/…prd.md` hat sie im Nachaudit einzeln geprüft und **16 auf `ASSUMPTION` herabgestuft**. | REQ-001…006, REQ-008, REQ-009, REQ-011, REQ-015, REQ-018, REQ-025, REQ-030, REQ-035, REQ-036 | **Aufgelöst zugunsten des PRD** (§2.1). Das PRD ist die `canonical_file` für `source_type`; die Werte sind **übernommen, nicht neu bewertet**. Eine Matrix, die `EXPLICIT` behauptet, während die kanonische Datei `ASSUMPTION` führt, wäre ein aktiver Widerspruch — nicht bloß eine Fußnote wert. |
| 8 | **Registry-intern: §7.5.5 gegen §8 Punkt 37 bei REQ-038.** §7.5.5 verlangt für `traceability.md:1489` den Wert **„MISSING (begründet)"**; §8 Punkt 37 zählt REQ-038 zu den drei Requirements **ohne** canvas-problem-Anker und stuft das als **BLOCKER** ein. | REQ-038 | **Nicht einseitig aufgelöst.** Der **Feldwert** folgt der spezifischeren Anweisung (§7.5.5): MISSING (begründet). Die **BLOCKER-Zählung** folgt §8 Punkt 37, damit diese Datei nicht von der Registry abweicht. Beides ist in §3, §4.1, §6.1 und §6.4 sichtbar gemacht. Die Registry ist eingefroren und wird hier **nicht** geändert. |
| 9 | **Registry-intern: OQ-015 referenziert deprecatete IDs.** Registry §8 Punkt 28 und die OQ-Zeile nennen REQ-040, AC-040, EV-040 und CAN-140 — alle vier hat **dieselbe Runde** deprecatet. | OQ-015 | **Diese Matrix zieht auf REQ-042 / AC-043 / EV-044 / CAN-143 nach** und spiegelt den Fehler nicht. Nach Registry §9 Bedingung 3 ist eine Referenz auf eine deprecatete ID ein Validierungsfehler — hier in der eingefrorenen Registry selbst. Nachzug beim Registry-Owner. |
| 10 | **Registry-intern: Gate von CAN-022 gegen Gate von REQ-009.** CAN-022 trägt laut Registry **Release Gate E**, REQ-009 liegt auf **Gate A1**. Seit dem 2026-07-20 ist CAN-022 der canvas-problem-Anker von REQ-009. | REQ-009, CAN-022 | **Offengelegt, nicht geglättet.** Ob ein Problem-Item überhaupt ein eigenes Gate trägt — oder es nur von seinem primären Requirement REQ-032 erbt — ist im Metamodell nicht geregelt. Die Registry ist eingefroren; das Gate wird **nicht** geändert und der Anker **nicht** deswegen verworfen (der Wortlauttreffer auf „Herzfrequenz“ und „externe Sensoren“ bleibt gültig). **OPEN QUESTION** für den Nutzer. |

#### 6.5.1 Die fünf beauftragten Zweifelsfälle — Einzelentscheidungen (2026-07-20)

Jeder Fall ist **einzeln** entschieden und **einzeln** begründet. Es wurde kein Item umgedeutet.
Wo kein tragender Ersatz existiert, steht ein **BLOCKER** statt eines plausiblen Ankers.

| # | Fall | Trägt der Anker? | Entscheidung und tragender Grund |
|---|---|---|---|
| 1 | **REQ-032 → CAN-029** („Datenqualität für Belastungsverständnis“) | **JA** — als belegter Enabler | **Anker bleibt, Gloss ersetzt.** Der Gloss war eine **eigene Kurzformel** und stand in keinem Item — formal dieselbe Gestalt wie die verbotene Kette. **Der Unterschied, der entscheidet:** das Zwischenglied steht **wörtlich im kanonischen Wortlaut von CAN-022**, dem Problem-Item **desselben** Requirements („Dadurch werden **Belastungsanalyse** … weniger vollständig und weniger zuverlässig“). Die Kette ist **innerhalb der eingefrorenen Registry textlich geschlossen**, nicht durch eine Lesart überbrückt. **Präzisiert:** REQ-032 zahlt auf **Vollständigkeit und Zuverlässigkeit** von CAN-029 ein, nicht auf dessen Existenz — CAN-029 ist auch ohne Wearables erfüllbar. Deshalb **sekundärer** Wertanker; primär bleiben CAN-022 (Problem) und CAN-069 (Capability). |
| 2 | **REQ-009 → CAN-013** (statt CAN-022) | **NEIN** — CAN-013 trägt nicht; **CAN-022 trägt** | **Ersetzt durch CAN-022.** CAN-013 („Daten **ohne verständliche Bedeutung**“) beschreibt Daten, die **vorhanden** sind und nicht interpretiert werden. REQ-009 handelt vom Gegenteil: die Herzfrequenz ist **gar nicht da**, solange keine Quelle angebunden ist. **Fehlende Daten sind keine bedeutungslosen Daten.** CAN-013 war hier ein **Universal-Problemanker** — dieselbe Defektklasse wie bei REQ-037/038/039. CAN-022 nennt „**Herzfrequenz**“ und „**externe Sensoren**“ **wörtlich**. Offengelegt: Gate-Divergenz A1 ↔ E (§6.5 Zeile 10). |
| 3 | **REQ-004 → VIS-007** | **NEIN** | **Ersetzt durch VIS-003** („verlässliches Tracking“ — wörtlich, und REQ-004 zahlt direkt auf NFR-001 ein). VIS-007 verlangt, dass **Score und Empfehlungen** Datenbasis, Gründe und Unsicherheit erklären; REQ-004 erzeugt auf **Gate A0** weder das eine noch das andere. Die Brücke „Punkt als *unsicher* klassifiziert = Unsicherheit erklärt“ verwechselt die **Qualitätsmarke eines GPS-Punkts** mit der **Unsicherheit einer Health-Aussage**. **Ausschlaggebend für die Konsistenz:** §3 verwirft VIS-007 bei **REQ-032** wörtlich mit der Begründung, es betreffe „die Erklärbarkeit der Health-Auswertung, nicht die Vollständigkeit der Signale“ — REQ-004 ist ebenfalls ein Signalqualitäts-Requirement. |
| 4 | **REQ-004 → CAN-100** (Risiko-Anker in der Primärspalte) | **NEIN** — nicht als **primärer** Anker | **In die Risiko-Zeile verschoben; Primäranker wird CAN-028.** CAN-100 ist ein **Risiko**-Item („GPS-Drift verfälscht Distanz und Route“). REQ-004 **mindert** dieses Risiko — deshalb steht `canvas-risk-status` auf `aligned`, also ausdrücklich „keine Risikoverschärfung“. Ein Item, das die Zeile selbst als nicht berührt ausweist, kann nicht ihr primärer Anker sein. **Folgebefund, offengelegt statt behoben:** REQ-004 hat damit **kein Capability-Item** — seine Anker sind Risiko, Wertversprechen, Evidence-Annahme. **CAN-048 wurde geprüft und NICHT mitbenutzt** (trägt laut Registry REQ-002). §6.1.2. |
| 5 | **REQ-031 → VIS-007** | **NEIN** | **Entfernt, kein Ersatz → BLOCKER.** VIS-007 regelt **Health-Ausgaben**; REQ-031 erzeugt keine. „Assistenz, keine Garantie“ und „Orientierung, keine Diagnose“ sind zwei **verschiedene** Haftungsvorbehalte — die Ähnlichkeit ist eine **Analogie**, keine gemeinsame Aussage. Den Sicherheitsvorbehalt trägt **CAN-073** (Non-Goal im Canvas), kein VIS-Item. VIS-003, VIS-009 und VIS-010 einzeln geprüft und verworfen. **Keine reservierte VIS-ID** — MISSING-Position wie bei REQ-032 und REQ-006. |
| 6 | **REQ-039 → CAN-030** | **NEIN** | **Ersetzt durch CAN-139.** CAN-030 ist „Erkenne deinen **Fortschritt**“; ein Dateiexport erzeugt weder Vergleich noch Trend noch Rückblick. CAN-030 war ein **Universal-Wertanker** (zusätzlich bei REQ-008, REQ-015, REQ-016, REQ-025, REQ-027, REQ-029). **CAN-139** ist seit Runde 4 Item Type **VALUE PROMISE / CAPABILITY** und beginnt wörtlich mit „Nutzer behalten **Kontrolle** über ihre aufgezeichneten Aktivitäten“ — das ist das Wertversprechen selbst. Offengelegt: die Wertversprechen-Gruppe CAN-028…CAN-038 enthält weiterhin **kein** Portabilitätsversprechen; die Umbuchung überbrückt die Lücke, sie schließt sie nicht. |

**Zusatzfall, nicht in der Auftragsliste, aber von der Registry beauftragt:**

| # | Fall | Trägt der Anker? | Entscheidung |
|---|---|---|---|
| 7 | **REQ-006 → VIS-003** (Registry §8 Punkt 40, Owner: Traceability-Owner) | **NEIN** | **Entfernt, kein Ersatz → BLOCKER, Zeilenstatus `broken`.** VIS-003 nennt vier Bedürfnisse; eine Route **vor** dem Start zu planen ist keines davon. Die Registry ordnet die Prüfung ausdrücklich diesem Owner zu und schreibt vor, den Anker „**nicht** zu übernehmen, weil er existiert“. **Konsistenzgrund:** dieselbe Lesart ist am 2026-07-20 für REQ-041 verworfen worden, und dafür wurde eigens VIS-014 reserviert. Beide Zeilen sind jetzt konsistent ankerlos. |

**Bilanz: zwei tragen (Fall 1 mit korrigiertem Gloss, Fall 2 nach Ersetzung), fünf tragen nicht.**
Von den fünf konnten **drei** durch einen tragenden Anker ersetzt werden (VIS-003 bei REQ-004,
CAN-028 bei REQ-004, CAN-139 bei REQ-039) und **zwei** nicht (REQ-031, REQ-006) — dort steht ein
BLOCKER. **In keinem Fall wurde ein Item umgedeutet, um eine Lücke zu schließen.**

### 6.6 Referenzierte, aber nicht registry-verwaltete ID-Räume

**Korrektur 2026-07-19:** die Registry verwaltet seit dem Auftau-Schritt 2 **zwölf** Präfixe, nicht
mehr zehn — `USER-` und `NFR-` sind hinzugekommen (Registry §5.1, §6.12, §6.13). Die Vorfassung
dieses Abschnitts führte beide als „nicht registry-verwaltet“; das ist überholt und **wird nicht
stehen gelassen**, weil es dieser Datei jetzt widerspräche.

| Präfix | Verwendung in dieser Matrix | Status |
|---|---|---|
| `GATE-` | Spalte `Release Gate` (GATE-A0 … GATE-E) | **Nicht registry-verwaltet.** Registry §5.2 führt `GATE-` als OPEN QUESTION (Aufnahme nicht beauftragt). Die Werte stammen unverändert aus dem Messmodell. |
| `VC-` | Spalte `value-check-id` (§5) | **Nicht registry-verwaltet**, Inhalt MISSING (Registry §8 Punkt 12). **Zusätzlicher BLOCKER seit 2026-07-19:** die Reihe bildet den Altstand von 36 ab; für REQ-037…REQ-040 existiert **keine** VC-ID und es wird keine erfunden (§5). |
| `DEC-` | DEC-005, DEC-011…DEC-013 in Befunden und Widerspruchs-Auflösungen | **Nicht registry-verwaltet** (Registry §5.2). |
| `SRC-` | Belege zum `source_type`-Nachaudit (§2.1): SRC-001, SRC-003, SRC-006 | **Nicht registry-verwaltet** (Registry §5.2). Definitionsort ist `docs/SOURCE-MAP.md`. |

**Nicht mehr in dieser Tabelle — seit dem 2026-07-19 registry-verwaltet:**

| Präfix | Verwendung in dieser Matrix | Neuer Status |
|---|---|---|
| `USER-` | USER-004 als Persona-Anker bei REQ-032 (primär) und REQ-009 (sekundär) | **Registry-verwaltet** (Registry §5.1, §6.12). Die frühere Zeile „ersetzt durch CAN-023/024/026/027; CAN-025 bleibt BLOCKER“ ist erledigt: CAN-025 hat mit **USER-004** eine ID. |
| `NFR-` | NFR-001 … NFR-008; Klassifikation in §6.7 | **Registry-verwaltet** (Registry §5.1, §6.13). Die Vorfassung dieser Zeile hielt fest, NFR-008 komme in dieser Matrix an keiner Stelle vor — **das ist seit dem Nachzug §6.7.11 nicht mehr der Fall**, und die Verwaisung ist aufgelöst (§6.7.11). |

Das verbleibende Restrisiko ist **kein Schönheitsfehler**, aber es ist kleiner geworden: dieselbe
Kollisionsklasse, die für OQ- und ASM-IDs bereits eingetreten ist, bleibt für **vier** statt
zuvor fünf Präfixe möglich. Die Aufnahme der übrigen vier ist eine Nutzerentscheidung
(Registry §8, Punkt 11).

### 6.7 NFR-Audit — alle acht NFRs auf dem Zwei-Achsen-Modell

**Warum dieser Abschnitt existiert.** Das PRD führt alle acht NFRs pauschal als `EXPLICIT`
(`prd.md:194-201`) — in einer Tabelle, die **keine Quellenspalte hat**. Für keinen der acht
Zielwerte wird eine Quelle genannt. Die Vorfassung dieser Matrix übernahm die Einstufung
ungeprüft. Hier sind Herkunft und Nachweis auf **zwei getrennte Achsen** gelegt (Registry §3.1):

- **`source_type`** beantwortet: *Woher stammt der Zielwert?* — `EXPLICIT` | `ASSUMPTION` |
  `MISSING` | `BLOCKER` | `CONTRADICTION`
- **`evidence_status`** beantwortet: *Ist die Erfüllung nachgewiesen?* — `not-required` |
  `not-planned` | `planned` | `pending` | `verified` | `failed` | `blocked`

Die Achsen dürfen **nicht** vermischt werden. `EXPLICIT` + `pending` ist eine **gültige**
Kombination (so bei NFR-007).

**Beweislatte für `EXPLICIT`.** Mindestens eines muss gelten: (a) der Nutzer hat den Wert
ausdrücklich bestätigt, (b) der Wert steht in einer belegten Nutzerquelle, (c) eine verbindliche
externe Regel/Plattformvorgabe wird konkret zitiert. **Keine automatische Vererbung:** ein
Vision-Item „Nutzer benötigen verlässliches Tracking" (VIS-003) macht den Wert „< 3 %"
**nicht** `EXPLICIT`. Qualitative Nutzerabsicht und quantitativer Engineering-Zielwert sind
getrennte Aussagen.

> ⚠️ **`EXPLICIT` bedeutet in §1 dieser Datei etwas anderes.** Die Legende in §1 lautet: „Die
> Pass-Bedingung steht **wörtlich in einem Artefakt**." Das ist eine rein **syntaktische**
> Prüfung — sie fragt, *ob* ein Satz irgendwo steht, nicht *woher* der Wert stammt. Unter der
> §1-Definition ist NFR-001 `EXPLICIT`, unter der Definition dieses Abschnitts `ASSUMPTION`.
> **Beide Definitionen sind für sich richtig und beantworten verschiedene Fragen — aber wer sie
> gleichsetzt, stuft still hoch.** Die §1-Legende darf **nicht** als Beleg für `source_type =
> EXPLICIT` herangezogen werden. Die Vereinheitlichung der beiden Begriffe ist eine offene
> Aufgabe des Datei-Owners und wird hier nicht eigenmächtig vorgenommen.

#### 6.7.1 Übersicht

| ID | Titel | `source_type` (hier) | `source_type` (PRD) | `evidence_status` | `measurement_type` | `release_gate` | Quelle des Zielwerts gefunden? |
|---|---|---|---|---|---|---|---|
| NFR-001 | Distanzgenauigkeit | **ASSUMPTION** | EXPLICIT | pending | OPERATIONAL_QUALITY | GATE-A0 | nein |
| NFR-002 | Batterie | **ASSUMPTION** | EXPLICIT | pending | OPERATIONAL_QUALITY | GATE-A0 | nein — PRD widerspricht sich selbst |
| NFR-003 | Zuverlässigkeit | **ASSUMPTION** | EXPLICIT | pending | OPERATIONAL_QUALITY | GATE-A0 | nein |
| NFR-004 | Performance | **BLOCKER** | EXPLICIT | blocked | OPERATIONAL_QUALITY | GATE-A0 / GATE-D | **es existiert kein Zielwert** |
| NFR-005 | Accessibility | **ASSUMPTION** | EXPLICIT | pending | COMPLIANCE_CONTROL | GATE-A0 bis GATE-A2 | teilweise („WCAG AA" ohne Fassung, ohne Rechtsgrundlage) |
| NFR-006 | Datenschutz | **BLOCKER** | EXPLICIT | blocked | COMPLIANCE_CONTROL | GATE-A0 bis GATE-E | gemischt — DEC-012/DEC-013 belegt, Retention MISSING |
| NFR-007 | Sicherheit | **EXPLICIT** | EXPLICIT | pending | COMPLIANCE_CONTROL | GATE-A0 bis GATE-E | **ja** — DEC-005 (`user-confirmed`), CAN-092, SRC-006 |
| NFR-008 | Wartbarkeit | **MISSING** | EXPLICIT | not-planned | PROCESS_CONTROL | **kein Gate** | nein — Anforderung ist verwaist |

**Ergebnis: eine von acht `EXPLICIT`-Angaben des PRD ist nach dieser Beweislatte haltbar.**
Sieben sind es nicht. Das ist ein Befund über die Quellenlage, **keine** Aussage darüber, dass die
Anforderungen falsch wären — die Werte sind durchweg plausibel. Plausibel ist nicht belegt.

`measurement_type = PROCESS_CONTROL` (nur NFR-008) ist eine **offengelegte Ergänzung** zur
Taxonomie aus §2 (Eigenschaft des Entwicklungsprozesses bzw. der Codebasis, per CI durchsetzbar,
keine Laufzeiteigenschaft des Produkts). Keine der vier bestehenden Klassen passt; eine
Fehlzuordnung wäre schlechter als eine benannte Ergänzung.

**`evidence_status = verified` steht bei keinem der acht.** Es existiert kein Code, kein Build und
kein Testlauf.

#### 6.7.2 Querschnittsbefunde (alle acht betroffen)

| # | Befund | Betroffen |
|---|---|---|
| XC-1 | Die NFR-Tabelle des PRD hat **keine Quellenspalte**; für keinen der acht Zielwerte ist eine Quelle genannt. `docs/SOURCE-MAP.md` zählt 102 `EXPLICIT`-Zellen ohne SRC-Angabe, davon 66 im PRD. | alle acht |
| XC-2 | `EXPLICIT` ist in §1 dieser Datei syntaktisch, hier herkunftsbezogen definiert (Kasten oben). | alle acht |
| XC-3 | **Für keinen der acht NFRs ist ein Owner benannt** (OQ-002 offen). Niemand entscheidet den Zielwert, niemand nimmt die Messung ab. | alle acht |
| XC-4 | **Referenzumgebung MISSING** für jede gerätegebundene Messung: OQ-003 (Minimum iOS/Android, Referenzgeräte) ist offen. Ohne Geräteliste ist kein Messwert vergleichbar. | NFR-001…005 |
| XC-5 | Der ID-Raum `NFR-` ist nicht registry-verwaltet und nicht kollisionsgeschützt (§6.6). Dieselbe Defektklasse, die für `OQ-` (CONTRA-003) und `ASM-` bereits eingetreten ist. | alle acht |

#### 6.7.3 Divergenzen Vision ↔ NFR

Requirement-spezifisch geprüft, nicht angenommen:

| # | Art | Befund |
|---|---|---|
| DIV-1 | COVERAGE_GAP | **Die Vision führt für keinen der acht NFRs einen Zielwert.** Es gibt daher keine numerische Wert-für-Wert-Divergenz. Geprüft am 2026-07-19 je Abschnitt der Vision (Target Group, User Needs, Product Value, Goals, Success Signals, Boundaries, Assumptions, Missing Items). Die einzigen quantitativen Vision-Werte sind die Success Signals aus VIS-006 (>30 %, >50 %, >25 %, >1,0, >25 %, >40 %, >60 %) — keiner davon ist eine Distanz-, Batterie-, Performance-, Accessibility-, Datenschutz- oder Sicherheitsschwelle. Die Abwesenheit wurde **nachgesehen**, nicht unterstellt. |
| DIV-2 | **CONTRADICTION** | Die Vision klassifiziert die VIS-006-Zielwerte als `EXPLICIT` (`vision.md:21`); §1 dieser Matrix klassifiziert **dieselben Werte** als `ASSUMPTION`, „nicht empirisch validiert". **Nicht still der stärkere Wert übernommen** — als Widerspruch gemeldet. Betrifft VIS-006, nicht die acht NFRs; hier geführt, weil es dieselbe Defektklasse ist. Owner: Nutzer (Bestätigung der Werte) bzw. Owner Vision/Traceability. |
| DIV-3 | COVERAGE_GAP | NFR-005 (Accessibility) hatte bis zum 2026-07-19 **überhaupt keine** Vision-Entsprechung — REQ-014 hing an VIS-009. Vision-Lücke durch VIS-011 vorbehaltlich Nutzerbestätigung geschlossen (§0.1, §6.5 Zeile 4); **Canvas-Lücke bleibt BLOCKER** (CAN-099 reserved, kein Canvas-Item für das Designsystem). |
| DIV-4 | COVERAGE_GAP | VIS-009 und NFR-006 decken sich **in beide Richtungen** nicht. Nur Vision: Profile standardmäßig privat; Live-Standort pro Aktivität Opt-in, zeitlich begrenzt, start-/endpunktverschleiert; Health-Daten nicht für Werbung — **keine** dieser drei Klauseln taucht in einem NFR auf. Nur NFR: „EU-orientiertes Hosting" kommt in keinem VIS-Item vor. Kein Widerspruch, aber die Vision-Klauseln hängen an REQ-018/REQ-030 und sind damit **nicht** als nicht-funktionale Schranke geführt. |
| DIV-5 | **CONTRADICTION** | **Das PRD widerspricht sich bei NFR-002 selbst.** `prd.md:195` führt NFR-002 als `EXPLICIT`; `prd.md:362` schreibt zum selben Wert, er sei „für dieses Produkt **nicht empirisch belegt**". Identischer Befund in §3 dieser Datei (REQ-003, `Measurement Window`). Der schwächere, belegte Befund gewinnt: `ASSUMPTION`. Owner: Owner `docs/prd/…prd.md`. |
| DIV-6 | OPEN QUESTION | NFR-006 sagt „EU-orientiertes Hosting"; DEC-013/CONTRA-006 hält fest, dass das für den **nachgelagerten Routing-Anbieter** möglicherweise nicht gilt (§7, CONTRA-006, Abschnitt „EU"). Kein formaler Widerspruch — „orientiert" ist schwach genug, um beides zu decken. **Genau das ist das Problem:** der Begriff ist als Zielwert nicht prüfbar. |

#### 6.7.4 NFR-001 — Distanzgenauigkeit

| Feld | Wert |
|---|---|
| Genaue Aussage | Die aufgezeichnete Distanz weicht nach Anwendung des GPS-Filters um weniger als 3 % von der Distanz einer definierten Referenzstrecke ab. |
| Metrik | Relative Abweichung der gefilterten Trackdistanz gegenüber der bekannten Referenzstreckenlänge |
| Einheit | Prozent |
| Zielwert / Pass-Bedingung | < 3 % Abweichung, getrennt nachgewiesen für **Run und Bike** und getrennt je Plattform (iOS, Android) |
| Quelle des Zielwerts | **KEINE GEFUNDEN.** Der Wert steht in `prd.md:194` ohne Quellenangabe. Volltextsuche über `docs/` am 2026-07-19: „< 3 %" erscheint ausschließlich als Wiederholung dieses PRD-Werts (diese Datei §3 REQ-002/REQ-004; `prd.md:346`, `:378`). Keine Nutzerbestätigung, keine externe Norm, keine Messreihe. |
| `source_type` | **ASSUMPTION** — festgelegt durch Nutzerentscheidung 2026-07-19 (verbindlich vorgegeben) |
| `confirmation_type` | unconfirmed |
| `measurement_type` | OPERATIONAL_QUALITY |
| `measurement_window` | Je vollständigem Lauf über die Referenzstrecke; getrennt Run/Bike, getrennt iOS/Android. **Eine Mindestanzahl Wiederholungen je Kombination nennt kein Artefakt: MISSING** — ohne sie ist kein Konfidenzintervall bestimmbar und ein Einzellauf kann den Wert zufällig treffen. |
| Testmethode | Realer Feldtest auf einer definierten Referenzstrecke bekannter Länge; Vergleich der gefilterten Trackdistanz gegen die Referenzlänge. Mindestklasse `production-verified` (§3, REQ-002) — im Labor nicht nachweisbar. |
| Referenzumgebung | **MISSING** — OQ-003 offen. Auch **die Referenzstrecke selbst** ist in keinem Artefakt benannt oder vermessen: MISSING. |
| `evidence_source` | EV-002 (Gerätetest je Sport und Plattform auf Referenzstrecke), EV-004 (Drift-, Tunnel-, Sprung- und Hochgeschwindigkeits-Fixtures) |
| `evidence_status` | **pending** — kein Code, kein Build, keine Messung. `verified` erst nach realen Referenzstreckentests auf festgelegten Referenzgeräten (Nutzervorgabe). |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002. Zusätzlich blockierend für die Messung: OQ-003 (Owner der Frage: „Engineering/QA" — eine Rolle, keine Person). |
| `release_gate` | GATE-A0 |
| `blocked_gates` | `[A0]` — abgeleitet aus `release_gate` = GATE-A0 |
| `blocked_activities` | `[field-test, release]` — verlustfrei aus dem entfallenen `blocking_scope` übernommen |
| `blocking` (abgeleitet) | **true** (`current_gate = A0 ∈ [A0]`) |
| Rationale | Der Wert ist plausibel und wird als vorläufiges Engineering-Ziel gebraucht, hat aber keine belegte Herkunft. VIS-003 („verlässliches Tracking") ist eine qualitative Absicht und macht 3 % **nicht** `EXPLICIT` — das sind zwei getrennte Aussagen. `EXPLICIT` erst nach ausdrücklicher Nutzerbestätigung oder belastbarer Quelle. |
| Offene Punkte | MISSING: Referenzstrecke nicht benannt und nicht vermessen · MISSING: Anzahl Wiederholungen je Sport/Plattform-Kombination · MISSING: zulässige Verwurfsquote des Filters (`prd.md:378` führt das selbst als MISSING) · BLOCKER: Referenzgeräte (OQ-003) |

#### 6.7.5 NFR-002 — Batterie

| Feld | Wert |
|---|---|
| Genaue Aussage | Der Batterieverbrauch bei aktivem Tracking bleibt unter 10 % pro Stunde auf definierten Referenzgeräten; der Messwert ist zu dokumentieren. |
| Metrik | Batterieladungsabnahme pro Stunde bei aktivem Tracking mit Background-Location |
| Einheit | Prozentpunkte Ladung pro Stunde |
| Zielwert / Pass-Bedingung | < 10 % pro Stunde. **Run und Bike getrennt, iOS und Android getrennt**, je mindestens ein Messlauf. |
| Quelle des Zielwerts | **KEINE GEFUNDEN.** `prd.md:195` nennt den Wert ohne Quelle und bezeichnet ihn selbst als „Ziel". `prd.md:362` und §3 dieser Datei (REQ-003) halten ausdrücklich fest, dass der Wert „für dieses Produkt nicht empirisch belegt" ist. |
| `source_type` | **ASSUMPTION** — Nutzerentscheidung 2026-07-19; zusätzlich durch `prd.md:362` selbst gestützt |
| `confirmation_type` | unconfirmed |
| `measurement_type` | OPERATIONAL_QUALITY |
| `measurement_window` | Eine **zusammenhängende Stunde** aktives Tracking; Wiederholung vor jedem Gate ab A0. |
| Testmethode | Realer Gerätetest mit **aktivem Background-Tracking** über eine zusammenhängende Stunde. Zwingend zu dokumentieren, weil sonst nicht vergleichbar: Display-Zustand (an/aus, Helligkeit), Netzwerkzustand (WLAN/Mobilfunk/Flugmodus), GPS-Sampling-Rate, Kartendarstellung aktiv/inaktiv, Ausgangsladestand, Umgebungstemperatur. |
| Referenzumgebung | **MISSING** — „definierte Referenzgeräte" werden gefordert, aber nirgends definiert (OQ-003). Ohne Geräteliste ist der Wert nicht vergleichbar: derselbe Code ergibt auf unterschiedlichen Geräten stark abweichende Werte. |
| `evidence_source` | EV-003 (30-Minuten-Kill-/Background-Test je Plattform und Sport) deckt das Background-Verhalten ab, **nicht** die Stundenmessung. **Für die Batteriemessung selbst benennt kein Artefakt eine eigene EV-ID: MISSING.** CAN-116 („Batterietests") existiert, ist aber keine EV-ID. |
| `evidence_status` | **pending** — kein Code, kein Gerätetest. Nachweis erst mit festgelegten Referenzgeräten, dokumentiertem Display-, Netzwerk- und GPS-Sampling-Zustand, aktivem Background-Tracking und mindestens einem Messlauf **je Sport und je Plattform** (Nutzervorgabe). |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002; Referenzgeräte OQ-003 |
| `release_gate` | GATE-A0 |
| `blocked_gates` | `[A0]` — abgeleitet aus `release_gate` = GATE-A0 |
| `blocked_activities` | `[field-test, release]` — verlustfrei übernommen |
| `blocking` (abgeleitet) | **true** (`current_gate = A0 ∈ [A0]`) |
| Rationale | Doppelter Befund: (1) der Zielwert hat keine Quelle, (2) das PRD widerspricht seiner eigenen `EXPLICIT`-Angabe an `prd.md:362`. Beides zeigt in dieselbe Richtung. Die Messung ist ohne dokumentierten Gerätezustand wertlos — **Display an/aus allein verändert das Ergebnis stärker als die 10-%-Schwelle.** |
| Offene Punkte | CONTRADICTION: `prd.md:195` EXPLICIT vs. `prd.md:362` „nicht empirisch belegt" (DIV-5) · MISSING: keine eigene EV-ID für die Batteriemessung · BLOCKER: Referenzgeräte (OQ-003) |

#### 6.7.6 NFR-003 — Zuverlässigkeit

| Feld | Wert |
|---|---|
| Genaue Aussage | Bei App-Kill oder Absturz gehen keine Aktivitätsdaten verloren; Session-Recovery ist verpflichtend. |
| Metrik | (a) Anzahl verlorener Aktivitäten, (b) Anteil erfolgreicher Session-Recoveries, (c) Anzahl inkonsistenter Indexe nach Migration |
| Einheit | (a) Anzahl, (b) Prozent, (c) Anzahl |
| Zielwert / Pass-Bedingung | Nullschwelle: 0 verlorene Aktivitäten über Kill- und Migrations-Fixtures, 0 inkonsistente Indexe nach Migration, jede Migration idempotent wiederholbar (`prd.md:394`). Session-Recovery gelingt in **100 %** der 30-Minuten-Kill-Tests je Plattform und je Sportart (`prd.md:362`). |
| Quelle des Zielwerts | **KEINE EIGENSTÄNDIGE QUELLE GEFUNDEN — mit einer Differenzierung:** die Nullschwelle ist keine *gewählte* Zahl, sondern die logische Übersetzung der Anforderung selbst („kein Datenverlust" = 0) und insoweit **nicht belegbedürftig**. Belegbedürftig und **unbelegt** sind: die Anforderung selbst (`prd.md:196`, EXPLICIT ohne Quelle) und die Operationalisierung „30 Minuten", „je Plattform", „je Sportart" aus EV-003. |
| `source_type` | **ASSUMPTION** |
| `confirmation_type` | unconfirmed |
| `measurement_type` | OPERATIONAL_QUALITY |
| `measurement_window` | 30 Minuten je Kill-/Background-Test, je Plattform und je Sportart; Wiederholung vor jedem Gate ab A0 (`prd.md:363`). |
| Testmethode | Kontrolliertes Beenden der App bzw. erzwungener Absturz während laufender Aufzeichnung; anschließend Prüfung auf Vollständigkeit des Tracks und auf erfolgreiche Wiederherstellung der Session. Ergänzend Migrations-Fixtures gegen die lokale Datenbank. |
| Referenzumgebung | **MISSING** — OQ-003. Zusätzlich relevant und nicht spezifiziert: die **OS-Versionen**, da das Kill-Verhalten von iOS und Android versionsabhängig ist (RISK-001 „Background-GPS wird durch OS gedrosselt oder beendet", Severity `critical`). |
| `evidence_source` | EV-003 (30-Minuten-Kill-/Background-Test je Plattform und Sport), EV-005 (SQLite-Repository-Tests, Kill-Test und Migrations-Fixtures) |
| `evidence_status` | **pending** — beide EV-IDs sind definiert, aber es existiert kein Code. Kein Testlauf hat stattgefunden. |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002 |
| `release_gate` | GATE-A0 |
| `blocked_gates` | `[A0]` — abgeleitet aus `release_gate` = GATE-A0 |
| `blocked_activities` | `[implementation, field-test, release]` — verlustfrei übernommen |
| `blocking` (abgeleitet) | **true** (`current_gate = A0 ∈ [A0]`) |
| Rationale | Die Nullschwelle ist sauber und braucht keine externe Quelle — sie folgt aus der Anforderung. `ASSUMPTION` bezieht sich darauf, dass die Anforderung selbst nur mit `EXPLICIT` ohne Quelle im PRD steht und die Testparameter (30 min, je Plattform, je Sportart) in einem **abgeleiteten** Artefakt gesetzt wurden, nicht vom Nutzer. **Warum 30 und nicht 60 Minuten, ist nirgends begründet.** |
| Offene Punkte | MISSING: Auto-Pause-Falschauslösungsrate ohne Schwellwert (`prd.md:362`) · MISSING: Rate technisch abgebrochener Sessions ohne Zielwert — wird gemessen und dokumentiert, aber **nicht bewertet** · MISSING: Begründung des 30-Minuten-Fensters · BLOCKER: Referenzgeräte und OS-Versionen (OQ-003) |

#### 6.7.7 NFR-004 — Performance · **schwächster der acht**

| Feld | Wert |
|---|---|
| Genaue Aussage | Tracking-UI flüssig; Kartenlayer viewportbasiert; Geo-Lasttest vor Stufe D. |
| Metrik | **MISSING** — kein Artefakt benennt eine Metrik. In Frage kämen Bildrate, Renderzeit des Kartenlayers, Frame-Drop-Rate, Interaktionslatenz; **keine davon ist gewählt.** |
| Einheit | **MISSING** — keine Millisekunden-, Bildraten- oder Perzentilangabe in irgendeinem Artefakt |
| Zielwert / Pass-Bedingung | **MISSING.** Wörtlich aus §3 dieser Datei (REQ-026): „NFR-004 fordert viewportbasierte Kartenlayer und einen Geo-Lasttest vor D, nennt aber **keine Millisekunden- oder Bildratenschwelle**: MISSING." Ebenda (REQ-026, `Entscheidungsschwelle`): „Quorumswert, Verfallsrate und Performanceschwelle (NFR-004) sind unbeziffert. Vor Gate D zu entscheiden." |
| Quelle des Zielwerts | **KEINE GEFUNDEN — es gibt keinen Zielwert, den man belegen könnte.** „Flüssig" ist kein Zielwert, sondern ein Adjektiv. |
| `source_type` | **BLOCKER** — ohne Schwelle ist Gate D nicht belastbar planbar und die A0-Klausel nicht abnehmbar |
| `confirmation_type` | unconfirmed |
| `measurement_type` | OPERATIONAL_QUALITY |
| `measurement_window` | **MISSING** — kein Artefakt definiert ein Messfenster oder eine Lastdauer. |
| Testmethode | Teilweise beschrieben: Karten-Lasttest auf realem Gerät mit realer Datenmenge (`prd.md:757` Stufe 3, EV-026). **Was gemessen wird, bleibt offen.** Für die A0-Aussage „Tracking-UI flüssig" benennt kein Artefakt überhaupt eine Testmethode. |
| Referenzumgebung | **MISSING, zweifach:** (1) Geräte (OQ-003); (2) **Datenmenge** — `prd.md:757` fordert „reale Aktivitätsdichten aus mindestens einer Stadt" und hält fest, dass synthetische Gleichverteilungen die Ballung unterschätzen und allein nicht ausreichen. Eine solche Datenbasis existiert nicht. |
| `evidence_source` | EV-026 (Geo-Fixtures, Simulation und Karten-Lasttest) — deckt **nur** den Territory-Anteil ab Stufe D. **Für „Tracking-UI flüssig" ab A0 existiert KEINE EV-ID: MISSING.** |
| `evidence_status` | **blocked** — der Nachweis kann nicht erbracht werden, weil der Zielwert fehlt: ein Test ohne Pass/Fail-Bedingung ist kein Test. Das ist **nicht** `pending`; `pending` würde eine erbringbare, nur noch nicht erbrachte Messung behaupten. |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002; Schwellenentscheidung zusätzlich an OQ-008 gebunden |
| `release_gate` | GATE-A0 (Klausel „Tracking-UI flüssig", unbeziffert) **und** GATE-D (Geo-Lasttest, unbeziffert) |
| `blocked_gates` | `[A0, D]` — abgeleitet aus `release_gate` (GATE-A0 für die Klausel „Tracking-UI flüssig“, GATE-D für den Geo-Lasttest); **beide unbeziffert** |
| `blocked_activities` | `[planning, field-test, release]` — verlustfrei übernommen |
| `blocking` (abgeleitet) | **true** (`current_gate = A0 ∈ [A0, D]`) |
| Rationale | NFR-004 ist der schwächste der acht: Anforderung **ohne Metrik, ohne Einheit, ohne Schwelle, ohne Messfenster, ohne Testdatenbasis**. Es wurde ausdrücklich **kein** plausibler Wert eingesetzt — weder 60 fps noch 16 ms noch ein Perzentil. Jede solche Zahl wäre erfunden. Der Zielwert ist vor Gate D zu entscheiden; für die A0-Klausel gibt es nicht einmal einen Fälligkeitszeitpunkt. |
| Offene Punkte | BLOCKER: keine Performanceschwelle (Metrik, Einheit, Wert) — vor Gate D zu entscheiden · MISSING: keine EV-ID für die A0-Klausel „Tracking-UI flüssig" · MISSING: reale Aktivitätsdichten als Testdatenbasis · MISSING: Messfenster und Lastdauer |

#### 6.7.8 NFR-005 — Accessibility

> **Nachgezogen 2026-07-19:** NFR-005 trägt ab jetzt **REQ-037** statt des deprecateten REQ-014.
> Die Designsystem-Hälfte liegt bei REQ-038 und wird von NFR-005 **nicht** gemessen.

| Feld | Wert |
|---|---|
| Genaue Aussage | WCAG **2.2** AA, Dynamic Type, Screenreader und keine reine Farbcodierung. |
| Getragenes Requirement | **REQ-037** (Accessibility). ~~REQ-014~~ ist deprecated. |
| Metrik | (a) Anteil ausgelieferter Screens, die Kontrast-, Dynamic-Type- und Screenreader-Prüfung in Light **und** Dark Mode bestehen; (b) Anzahl Zustände, die allein über Farbe unterschieden werden |
| Einheit | (a) Prozent, (b) Anzahl |
| Zielwert / Pass-Bedingung | 100 % Abdeckung, 0 Zustände ohne zusätzliches Symbol oder Textlabel. „Kein Prozentziel unterhalb von 100 — die Anforderung ist eine **Schranke, keine Quote**." |
| Quelle des Zielwerts | **TEILWEISE — eine der beiden Lücken ist seit dem 2026-07-19 geschlossen, die andere nicht.** (1) **Fassung: nachgetragen.** Die frühere Angabe „WCAG AA" stand ohne Version, obwohl 2.0 AA, 2.1 AA und 2.2 AA unterschiedliche Erfolgskriterien haben. Die Nutzerentscheidung beziffert die Fassung in CAN-099 und REQ-037 als **2.2**; ein Audit ist damit überhaupt erst bestehbar. (2) **Rechtsgrundlage: weiterhin MISSING.** In keinem Artefakt wird eine Rechtsgrundlage zitiert, die WCAG 2.2 AA für dieses Produkt verbindlich macht — kein Verweis auf EAA, BFSG oder eine Store-Vorgabe. Die Beweislatte „eine verbindliche externe Regel wird **konkret zitiert**" bleibt damit **unerfüllt**: die Norm ist jetzt vollständig benannt, ihre **Verbindlichkeit** nicht. |
| `source_type` | **ASSUMPTION** |
| `confirmation_type` | unconfirmed |
| `measurement_type` | COMPLIANCE_CONTROL |
| `measurement_window` | Je ausgeliefertem Screen, vor jedem Gate ab A0 (**REQ-037** läuft über Release A0-A2: Accessibility-Basis ab A0, vollständiger Audit spätestens A2). Kein zeitbasiertes Fenster — es ist eine **vollständige Abdeckungsprüfung**. |
| Testmethode | Kontrastprüfung, Dynamic-Type-/Font-Scaling-Prüfung und Screenreader-Durchlauf mit **VoiceOver UND TalkBack** in Light und Dark Mode je Screen (**EV-037**). **Der Token-Review gehört seit dem 2026-07-19 nicht mehr hierher** — er ist der Designsystem-Nachweis (EV-038 zu REQ-038) und war in EV-014 mit dem Accessibility-Nachweis vermischt. |
| Referenzumgebung | **MISSING** — weder Geräte (OQ-003) noch die Screenreader-Matrix sind festgelegt: VoiceOver und TalkBack in welchen OS-Versionen, welche Schriftgrößenstufen, welche Kontrastmessmethode. |
| `evidence_source` | **EV-037** (WCAG-2.2-AA-Audit, VoiceOver- und TalkBack-Durchlauf je Plattform, Dynamic-Type-/Font-Scaling-Prüfung, dokumentierte Kontrastprüfung). ~~EV-014~~ ist deprecated. |
| `evidence_status` | **`not-planned`** — **korrigiert von `pending`.** Nach der projektweiten Semantik (Registry §3.2) setzt `pending` eine **implementierte Instrumentierung** voraus, der nur noch Messdaten fehlen. Es existiert kein Code, keine CI und kein beauftragter Auditor — also noch nicht einmal ein Messkonzept. `pending` hätte einen Reifegrad behauptet, den es nicht gibt. |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002. Zusätzlich **MISSING: kein Auditor benannt** für den externen WCAG-Audit. |
| `release_gate` | GATE-A0 (Accessibility-Basis) bis GATE-A2 (vollständiger Audit), erstmalige Abnahme mit GATE-A0 |
| `blocked_gates` | `[A0, A2]` |
| `blocked_activities` | `[implementation, release, store-submission]` |
| `blocking` (abgeleitet) | **true** — `evidence_status = not-planned` blockiert für sich genommen nichts; die Blockade entsteht über `current_gate ∈ blocked_gates` bzw. `current_activity ∈ blocked_activities` (Formel §7.0). |
| Rationale | **Die Nennung einer Norm ist noch keine Verbindlichkeit.** Die Fassungslücke ist geschlossen — „WCAG 2.2 AA" ist ein prüfbarer Zielwert. Was fehlt, ist die Ebene darüber: **warum** diese Norm für dieses Produkt gilt. Deshalb bleibt `ASSUMPTION` statt `EXPLICIT`, obwohl die Norm jetzt vollständig im Text steht. |
| Offene Punkte | ~~**BLOCKER** WCAG-Version nicht spezifiziert~~ → **geschlossen 2026-07-19** (Fassung 2.2, CAN-099/REQ-037) · **MISSING** Rechtsgrundlage der Verbindlichkeit · **MISSING** Screenreader- und Gerätematrix (OQ-003) · **MISSING** kein benannter Auditor · ~~**BLOCKER** CAN-099 reserved und inhaltlich MISSING~~ → **geschlossen**, CAN-099 ist `active` und ausschließlich Accessibility · ~~**BLOCKER** kein atomares Canvas-Item für das tokenbasierte monochrome Designsystem~~ → **geschlossen**, **CAN-141** vergeben (trägt REQ-038, **nicht** NFR-005) · **BLOCKER** VIS-011 als Vision-Anker unbestätigt (§6.5 Zeile 4) |

**Abgrenzung CAN-099 ↔ CAN-141.** Der gemeinsame Satzteil „Farbe ist nie der einzige
Informationsträger" wirkt in **beiden** — als Accessibility-Schranke (AC-037 d) und als
Gestaltungsregel (AC-038 a/b). Dieselbe Beobachtung, **zwei getrennt prüfbare Pflichten, zwei
getrennte Nachweise**. NFR-005 misst nur die erste.

#### 6.7.9 NFR-006 — Datenschutz

| Feld | Wert |
|---|---|
| Genaue Aussage | Privacy by default, EU-orientiertes Hosting, Export/Löschung und Datenminimierung. |
| Metrik | Heterogen je Klausel: Anteil personenbezogener Daten, die eine Accountlöschung nicht überleben; Verarbeitungsregion; Aufbewahrungsfristen je Datenart; Umfang serverseitig verarbeiteter Daten |
| Einheit | Heterogen: Prozent, Regionsbezeichner, Tage, Feldliste |
| Zielwert / Pass-Bedingung | **Nur teilweise bestimmt.** BESTIMMT durch DEC-012: Löschumfang abschließend aufgezählt; historische Daten überleben nur wirksam anonymisiert, sonst Löschung. BESTIMMT durch DEC-013 für den A0-Routing-Proxy: Retention 0 für Koordinaten-Payload, technische Logs max. 7 Tage, `eu-central-1`. **UNBESTIMMT:** Aufbewahrungsfristen für GPS-, Health- und Live-Daten allgemein (OQ-009); Hosting-Region des eigentlichen Backends (OQ-005); Verarbeitungsregion des Routing-Anbieters. |
| Quelle des Zielwerts | **GEMISCHT.** Belegte Nutzerquelle für den Löschumfang: DEC-012 / CONTRA-005 (Nutzerentscheidung 2026-07-19), geführt als SRC-006 in `docs/SOURCE-MAP.md`. Belegte Nutzerquelle für die A0-Proxy-Baseline: DEC-013. **KEINE Quelle** für „EU-orientiertes Hosting" als Zielwert und **KEINE** für Retentionsfristen. |
| `source_type` | **BLOCKER** — der *Requirement*-Kern ist durch zwei belegte Nutzerentscheidungen gedeckt (insoweit EXPLICIT), der *Zielwert* ist es nicht. Der schwächere Befund wird **nicht** vom stärkeren verdeckt. |
| `confirmation_type` | teilweise `user-confirmed` (Löschumfang via DEC-012, A0-Proxy-Baseline via DEC-013); im Übrigen unconfirmed |
| `measurement_type` | COMPLIANCE_CONTROL |
| `measurement_window` | Kein Zeitfenster — Abdeckungs- und Nullschwellenprüfung je Datenfluss. Für Retention wäre das Fenster die jeweilige Frist selbst; **genau die fehlt.** |
| Testmethode | Datenflussdiagramm mit 100 % Abdeckung, RLS-Tests, Löschungsnachweis (EV-034, EV-017). **Für „wirksam anonymisiert" existiert KEIN Prüfverfahren:** `docs/validation/validation-report.md` führt das als Befund B6 — ohne definiertes Verfahren ist Anonymisierungswirksamkeit nicht prüfbar. |
| Referenzumgebung | **MISSING** — Backend nicht entschieden (OQ-005); Verarbeitungsregion und Unterauftragsverarbeiter des Routing-Anbieters laut DEC-013 erst **vor dem ersten externen Feldtest** zu dokumentieren. |
| `evidence_source` | EV-017 (E2E-Flow, Offline-Test und Löschungsnachweis), EV-034 (Security-Review, RLS-Tests, Datenflussdiagramm und Löschungsnachweis), EV-027 (teilweise, für anonymisierte Historie). **Für „Datenmodell trennt Identität und historische Aggregate" existiert KEINE EV-ID** (`EVIDENCE-LEDGER.md`, Marke (z); Registry §8 Punkt 14). |
| `evidence_status` | **blocked** — die von DEC-012 **vor** der Schema-Finalisierung geforderte Trennung ist ohne Retentionsfristen (OQ-009) nicht spezifizierbar, und für „wirksam anonymisiert" fehlt das Prüfverfahren. |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002; OQ-009 nominell „Privacy/Product", OQ-005 „Engineering" — **beides Rollen, keine Personen** |
| `release_gate` | GATE-A0 bis GATE-E; harte Punkte: **vor Finalisierung des Datenbankschemas** (DEC-012) und GATE-B |
| `blocked_gates` | `[A0, B, C, D, E]` — abgeleitet aus `release_gate` = GATE-A0 bis GATE-E; der harte Punkt **vor Finalisierung des Datenbankschemas** (DEC-012) liegt auf der **Tätigkeits**achse, nicht auf einem Gate |
| `blocked_activities` | `[planning, database-schema-finalization, implementation, release]` — verlustfrei übernommen |
| `blocking` (abgeleitet) | **true** |
| Rationale | Der Requirement-Kern ist durch zwei belegte Nutzerentscheidungen gedeckt — das ist die einzige Stelle im Audit neben NFR-007, an der eine Nutzerquelle wirklich trägt. Der **Zielwert** ist es nicht: „EU-orientiertes Hosting" ist als Formulierung nicht prüfbar, und die Retentionsfristen fehlen vollständig. Beides zusammen blockiert eine Architekturentscheidung, die laut DEC-012 **früh** zu treffen ist. |
| Offene Punkte | BLOCKER: Retentionsfristen für GPS, Health und Live MISSING (OQ-009) — blockiert die Schema-Trennung aus DEC-012 · BLOCKER: kein Prüfverfahren für „wirksam anonymisiert" (Validation-Report B6) · BLOCKER: keine EV-ID für „Datenmodell trennt Identität und historische Aggregate" · MISSING: Backend und Hosting-Region (OQ-005) · MISSING: Verarbeitungsregion, Unterauftragsverarbeiter und Transfergrundlage des Routing-Anbieters · OPEN QUESTION: „EU-orientiertes Hosting" als Zielwert nicht prüfbar (DIV-6) |

#### 6.7.10 NFR-007 — Sicherheit · **einziger belegter `EXPLICIT`-Zielwert**

| Feld | Wert |
|---|---|
| Genaue Aussage | Keine Secrets im Client, sichere Auth, RLS, Rate Limits, serverseitige Validierung. |
| Metrik | (a) Anzahl Routing-Provider-Keys im App-Bundle; (b) Anzahl Endpunkte ohne Rate Limit; (c) Anzahl Endpunkte ohne serverseitige Validierung; (d) konkrete Rate-Limit-Werte |
| Einheit | (a)–(c) Anzahl; (d) Requests pro Zeiteinheit |
| Zielwert / Pass-Bedingung | **BESTIMMT:** 0 Secrets im Client, ab A0 auch für den Routing-Proxy-Key; 0 Endpunkte ohne Rate Limit und ohne serverseitige Validierung (§3 REQ-034, `prd.md:892`). **UNBESTIMMT:** die konkreten Rate-Limit-Werte — DEC-013 fordert „Rate Limit, Size-Limit, maximale Wegpunktzahl, Timeout, Kill Switch" **ohne eine einzige Zahl**. |
| Quelle des Zielwerts | **GEFUNDEN — für eine Klausel.** „Keine Secrets im Client" ist durch eine **belegte Nutzerentscheidung** gedeckt: DEC-005 (Status `user-confirmed (2026-07-19)`), CAN-092 (Source Type CONFIRMED, Nutzerentscheidung 2026-07-19), CONTRA-002 (resolved), geführt als SRC-006 in `docs/SOURCE-MAP.md`. Die technische Begründung ist konkret und nachprüfbar: `EXPO_PUBLIC_*` wird ins JS-Bundle inlined und ist aus jedem Build extrahierbar. **Für die übrigen Klauseln: KEINE Quelle gefunden.** |
| `source_type` | **EXPLICIT** — und zwar **nur** für die Klausel „keine Secrets im Client". Die übrigen vier Klauseln werden ausdrücklich **nicht** mit hochgezogen. |
| `confirmation_type` | `user-confirmed` (nur Klausel „keine Secrets im Client"); übrige Klauseln unconfirmed |
| `measurement_type` | COMPLIANCE_CONTROL |
| `measurement_window` | Kein Zeitfenster — Nullschwellenprüfung je Build (Bundle-Scan) und je Endpunkt (Rate Limit, Validierung). Ab A0 fortlaufend bis GATE-E. |
| Testmethode | Bundle-Scan des ausgelieferten JS-Bundles auf Routing-Provider-Keys; Proxy-Integrationstest; Security-Review; RLS-Tests; Endpunkt-Inventar gegen Rate-Limit- und Validierungsabdeckung. Mindestklasse `real-boundary-smoke` (§3, REQ-006): „ein gemockter Routing-Response verdeckt genau den NFR-007-Pfad". |
| Referenzumgebung | Für den Bundle-Scan: ein realer Release-Build je Plattform — **existiert nicht**. Für die Proxy-Kontrollen: die A0-Laufzeit laut CAN-096 (AWS Lambda + API Gateway, `eu-central-1`) — ausdrücklich **nur dokumentiert, nicht gebaut; keine AWS-Ressource angelegt.** |
| `evidence_source` | ASM-103 (Bundle-Scan ohne Routing-Key plus Proxy-Integrationstest), EV-034 (Security-Review, RLS-Tests, Datenflussdiagramm), EV-006 (Routing-Service-Tests) |
| `evidence_status` | **pending** — `EXPLICIT` + `pending` ist hier die **korrekte** Kombination: die Herkunft ist belegt, der Nachweis steht aus. |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002 |
| `release_gate` | GATE-A0 bis GATE-E. DEC-005 stellt ausdrücklich fest: NFR-007 gilt **ab A0**, nicht erst ab Stufe B. |
| `blocked_gates` | `[A0, B, C, D, E]` — abgeleitet aus `release_gate` = GATE-A0 bis GATE-E; DEC-005 stellt ausdrücklich fest, dass NFR-007 **ab A0** gilt |
| `blocked_activities` | `[implementation, release, store-submission]` — verlustfrei übernommen |
| `blocking` (abgeleitet) | **true** |
| Rationale | Der einzige der acht NFRs, bei dem die Beweislatte für `EXPLICIT` tatsächlich erreicht wird — und zwar nur für **eine von fünf Klauseln**. Die Einstufung ist **keine Hochstufung**, sondern die Wiedergabe einer protokollierten Nutzerentscheidung vom 2026-07-19. Insbesondere die Rate-Limit-Werte bleiben MISSING. |
| Offene Punkte | MISSING: konkrete Rate-Limit-, Size-Limit-, Wegpunktzahl- und Timeout-Werte (DEC-013 fordert sie, beziffert keine) · MISSING: Auth-Verfahren und -Standard · MISSING: RLS setzt den offenen Backend-Entscheid voraus (OQ-005) · BLOCKER: kein Code, kein Build — Bundle-Scan nicht durchführbar |

#### 6.7.11 NFR-008 — Wartbarkeit · **Verwaisung aufgelöst, Messdefinition offen**

> **Entscheidung 2026-07-19: NFR-008 wird definiert, NICHT deprecatet** (Registry §6.13.1).
> Die drei vom Nutzer verlangten Vorfragen sind **einzeln** beantwortet, nicht pauschal.

| Vorfrage | Befund |
|---|---|
| Fachlich notwendige NFR? | **Ja.** Die vier Zusagen — TypeScript strict, reine Domainmodule, versionierte Schemas, automatisierte Tests — sind in `CLAUDE.md` und im Gesamtplan **projektweit verbindliche Arbeitsregeln**. Die Substanz existiert; ihr fehlt nur die **Messdefinition**. |
| Durch ein anderes NFR dupliziert? | **Nein.** NFR-001…003 messen Betriebsqualität, NFR-004 Performance, NFR-005 Zugänglichkeit, NFR-006 Datenschutz, NFR-007 Sicherheit. **Keines** trifft eine Aussage über Codestruktur, Typsicherheit, Schemaversionierung oder Testautomatisierung. |
| Nur reservierte, nie definierte ID? | **Nein.** NFR-008 ist in `prd.md:222` mit vier konkreten inhaltlichen Zusagen **definiert**. Reserviert und leer ist etwas anderes. |

**Warum nicht deprecatet.** Eine Anforderung mit realem, nicht dupliziertem Inhalt zu deprecaten,
weil ihre *Messung* fehlt, würde vorhandene Projektsubstanz löschen und die vier Zusagen aus der
Nachweispflicht entfernen. Das wäre die schlechtere der beiden Optionen.

| Feld | Wert |
|---|---|
| Genaue Aussage | TypeScript strict, reine Domainmodule, versionierte Schemas, automatisierte Tests. |
| Metrik | **MISSING (OQ-013)** — kein Artefakt benennt eine Metrik. In Frage kämen Testabdeckung, Anzahl Typfehler, Anteil abhängigkeitsfreier Domainmodule, Anzahl unversionierter Schemas; **keine davon ist gewählt.** |
| Einheit | **MISSING (OQ-013)** |
| Zielwert / Pass-Bedingung | **MISSING (OQ-013).** Vier qualitative Zusagen ohne jede Schwelle. Insbesondere ist **keine Testabdeckungsquote** genannt. ⚠️ **Die in `CLAUDE.md` genannten 80 % wurden ausdrücklich NICHT eingesetzt:** sie sind eine **globale Arbeitsregel des Nutzers**, kein für dieses Produkt beschlossener NFR-Zielwert. Eine qualitative Absicht in einen quantitativen Zielwert umzudeuten, verletzt dieselbe Beweislatte, an der in §6.7 sieben von acht NFRs gescheitert sind. |
| Quelle des Zielwerts | **KEINE GEFUNDEN.** Es existiert kein Artefakt, das eine Schwelle für die vier Zusagen benennt. |
| `source_type` | **MISSING** |
| `confirmation_type` | unconfirmed |
| `measurement_type` | **PROCESS_CONTROL** — offengelegte Ergänzung zur Taxonomie aus §2 (siehe §6.7.1) |
| `measurement_window` | **MISSING (OQ-013)** — eine CI-durchgesetzte Eigenschaft wäre je Commit oder je Build zu prüfen; kein Artefakt legt das fest. |
| Testmethode | **MISSING (OQ-013)** — keine benannt. *Ableitbar* wäre: TypeScript-Compiler im `strict`-Modus als CI-Gate, Importgraph-Prüfung der Domainmodule, Schema-Versionsprüfung, Coverage-Report. **Nichts davon ist in einem Artefakt festgelegt, deshalb wird es hier nicht als Testmethode geführt** — eine ableitbare Methode ist keine beschlossene. |
| Referenzumgebung | **MISSING** — es existiert **keine CI** im Repository. Registry §9 hält fest, dass überhaupt kein ausführbares Prüfwerkzeug vorhanden ist. |
| `evidence_source` | **KEINE.** Kein EV-Eintrag referenziert NFR-008. EV-035 (CI-Regel, Ledger-Review, Gate-Checkliste) gehört zu REQ-035 und deckt die **Evidence-Disziplin** ab, nicht die Wartbarkeit. |
| `evidence_status` | **not-planned** — kein Artefakt sieht überhaupt einen Nachweis vor. Bewusst **nicht** `pending`: das würde einen geplanten, nur noch nicht erbrachten Nachweis behaupten (Registry §3.2). |
| Owner | **OWNER-BLOCKER (MISSING)** — OQ-002; die Messdefinition selbst hat ebenfalls keinen Entscheider (OQ-013). |
| `release_gate` | **MISSING (OQ-013)** — kein Gate referenziert NFR-008; die Gate-Tabelle im PRD nennt es nicht. |
| `blocked_gates` | `[]` |
| `blocked_activities` | `[]` |
| `blocking` (abgeleitet) | **false** — **und genau das ist der Befund.** `blocking = false` bedeutet hier nicht „unkritisch", sondern dass die Anforderung an **keiner Stelle wirksam** wird: kein Gate fordert sie ein, kein Nachweis ist vorgesehen, keine CI existiert, die sie durchsetzen könnte. |

**Verwaisung — beide Teilforderungen adressiert.**

1. **Nicht mehr verwaist.** Die Zeichenfolge „NFR-008" kam vor dem 2026-07-19 im gesamten
   Repository **genau einmal** vor — in ihrer eigenen Definitionszeile (`prd.md:222`). Sie wird
   jetzt von `docs/ID-REGISTRY.md` §6.13, von **OQ-013**, von der Migrationstabelle §7.4 und von
   **diesem Abschnitt** referenziert. Die Vorfassung dieser Matrix nannte NFR-008 an keiner
   Stelle und war damit selbst Teil des Befundes (§6.6).
2. **Nicht als erfüllte Anforderung gezählt.** NFR-008 zählt in der `NFR-`Zeile, **nicht** in der
   Zahl aktiver Requirements — das sind ausschließlich `REQ-`IDs (Regel 11, §0.0). Die beiden
   Zählungen sind getrennt; **NFR-008 ist damit nicht gleichzeitig verwaist und als aktive
   Anforderung gezählt.**

| Offene Punkte | **MISSING (OQ-013):** Metrik, Einheit, Schwellwert, Messfenster, Testmethode, zuständiges Gate, Owner — **alle sieben werden nicht vergeben**, weil keiner aus einem Artefakt ableitbar ist · **MISSING:** keine CI im Repository, die die vier Zusagen durchsetzen könnte · **Befund, der bleibt:** `blocking = false` bei einer inhaltlich notwendigen Anforderung |
|---|---|

## 7. Widerspruchs-Auflösungen (Nutzerentscheidungen 2026-07-19)

### 7.0 Statusmodell — Nachzug auf Registry §3.1 (2026-07-19)

**Was hier vorher falsch war.** Die Vorfassung dieses Abschnitts trug den Status in den
**Überschriften** und mischte dabei zwei unabhängige Fragen in einem Wert:
`RESOLVED (Entscheidung), Implementierungs-Evidence ausstehend` und
`DESIGN-RESOLVED / EVIDENCE-PENDING`. Beide sind als `status`-Wert **unzulässig** (Registry §3.1).
Sie sind hier durch die zwei getrennten Achsen ersetzt. Zugleich behauptete die Einleitung, die
Registry führe CONTRA-004/005/006 „weiterhin als `open`" — **das ist seit dem Auftau-Schritt vom
2026-07-19 überholt**: Registry §6.11 führt alle sechs als `resolved`, §6.11.1 trägt die
Statusfelder. Die Divergenz C6b gegenüber `docs/decisions/decision-log.md` besteht damit nicht mehr.

**Das Modell.** `status` behält ausschließlich `open` | `resolved` und beschreibt **nur**, ob der
fachliche/architektonische Widerspruch **entschieden** wurde. Ein Widerspruch erhält `resolved`,
sobald die Entscheidung getroffen ist — **nicht** erst, wenn die Evidence vorliegt. Die Evidence
lebt auf `evidence_status`.

### 7.0.1 C16 — `blocking_scope` ist ersatzlos entfallen (Nutzerentscheidung 2026-07-19)

**Der Defekt.** Das frühere Feld `blocking_scope` mischte **Release-Gates** und **Tätigkeiten** in
einer einzigen Liste. Die Vokabulare sind **disjunkt**: kein Gate-Bezeichner (`A0`, `B`, `C` …)
ist jemals ein Tätigkeitsbezeichner (`field-test`, `release` …) und umgekehrt. Die alte Formel
verlangte aber, das „aktuell geprüfte Gate" in `blocking_scope` zu suchen. Für jeden Eintrag,
dessen `blocking_scope` **nur Tätigkeiten** enthielt — also für **jeden gegateten Eintrag** —
lieferte die wörtliche Lesart zwangsläufig **`false`**. Die Blockade, die das Feld sichtbar machen
sollte, verschwand genau dann, wenn sie gegen ein Gate geprüft wurde.

**Die Auflösung.** `blocking_scope` ist **ersatzlos entfallen** und durch zwei Felder mit je einem
eigenen, **abschließenden** Wertebereich ersetzt:

| Feld | Abschließender Wertebereich |
|---|---|
| `blocked_gates` | `P0` · `A0` · `A1` · `A2` · `B` · `C` · `D` · `E` |
| `blocked_activities` | `documentation` · `planning` · `implementation` · `field-test` · `release` · `store-submission` · `database-schema-finalization` · `account-release` · `competition-release` · `territory-release` |

`none` ist als Wert entfallen und wird durch die **leere Liste** `[]` ausgedrückt.

**Kanonische Ableitungsformel für `blocking` (verbindlich, Registry §3.1):**

```
blocking = status != resolved
           OR resolution_status != accepted
           OR evidence_status IN [failed, blocked]
           OR current_gate IN blocked_gates
           OR current_activity IN blocked_activities
```

`current_gate` und `current_activity` sind die **Auswertungsparameter** des jeweiligen Prüflaufs.
Ist einer von beiden nicht gesetzt, entfällt **ausschließlich die zugehörige Klausel**; die
übrigen bleiben in Kraft.

⚠️ **Niemals Gate-Bezeichnungen mit Tätigkeitsbezeichnungen vergleichen.** `current_gate` wird
ausschließlich gegen `blocked_gates` geprüft, `current_activity` ausschließlich gegen
`blocked_activities`. **Ein Werkzeug, das ein Gate in `blocked_activities` sucht (oder umgekehrt),
reproduziert exakt den behobenen Defekt.**

**Bei `evidence_status` = `planned` oder `pending`** entsteht ein *aktueller* Blocker **nur** dann,
wenn das gerade geprüfte Gate in `blocked_gates` oder die gerade geprüfte Tätigkeit in
`blocked_activities` steht. `planned`/`pending` allein blockiert nichts.

**Eine einzige Implementierung.** Alle Validatoren importieren **dieselbe** kanonische
Blocking-Funktion. Duplizierte oder abweichende Implementierungen sind unzulässig, ebenso jede
hartkodierte Sonderbehandlung einzelner `CONTRA-`IDs. **Ein Prüfwerkzeug, das `blocking` für eine
bestimmte ID fest verdrahtet, ist selbst der Defekt.** Diese Matrix enthält keine.

⚠️ **BLOCKER — eine solche gemeinsame Implementierung existiert nicht.** Registry §9 hält fest,
dass im Repository **überhaupt kein ausführbares Prüfwerkzeug** vorhanden ist. Die Formel oben ist
damit **Spezifikation, kein Nachweis**. Ein reines Umbenennen des Feldes behebt den Defekt
ebenfalls **nicht**: solange irgendein Werkzeug die alte Formel anwendet, liefert es für gegatete
Einträge weiterhin fälschlich `false`.

**Auswertungskonvention.** `blocking` ist auswertungsrelativ: dieselbe ID kann an einem Gate
blockieren und an einem anderen nicht. Die Werte unten sind die Auswertung **am jeweils eigenen
`evidence_gate` des Eintrags**. Wer gegen ein anderes Gate oder eine andere Tätigkeit prüft,
**leitet neu ab und übernimmt den Tabellenwert nicht**.

| id | `status` | `resolution_status` | `evidence_status` | `blocking` (abgeleitet) | `blocked_gates` | `blocked_activities` | `evidence_gate` |
|---|---|---|---|---|---|---|---|
| CONTRA-001 | resolved | accepted | not-required | **false** | `[]` | `[]` | — |
| CONTRA-002 | resolved | accepted | pending | **true** | `[A0]` | `[implementation, release]` | A0 |
| CONTRA-003 | resolved | accepted | pending | **true** | `[]` | `[documentation]` | — |
| CONTRA-004 | resolved | accepted | pending | **true** | `[C, D]` | `[competition-release, territory-release]` | C |
| CONTRA-005 | resolved | accepted | pending | **true** | `[B]` | `[database-schema-finalization, account-release]` | B |
| CONTRA-006 | resolved | accepted | pending | **true** | `[A0]` | `[field-test, release]` | A0 |

**Nachrechnung — die Werte sind abgeleitet, nicht übernommen.** Ausgewertet am jeweils eigenen
`evidence_gate`, ohne laufende Tätigkeit:

| id | `status != resolved` | `resolution_status != accepted` | `evidence_status IN [failed, blocked]` | `current_gate IN blocked_gates` | Ergebnis |
|---|---|---|---|---|---|
| CONTRA-001 | false | false | false | `—` nicht auswertbar | **false** |
| CONTRA-002 | false | false | false | `A0 ∈ [A0]` → **true** | **true** |
| CONTRA-003 | false | false | false | `—` nicht auswertbar; Tätigkeitsklausel `documentation` greift bei laufender Dokumentation | **true** |
| CONTRA-004 | false | false | false | `C ∈ [C, D]` → **true** | **true** |
| CONTRA-005 | false | false | false | `B ∈ [B]` → **true** | **true** |
| CONTRA-006 | false | false | false | `A0 ∈ [A0]` → **true** | **true** |

⚠️ **Der Unterschied zur alten Formel ist nicht kosmetisch.** Unter `blocking_scope` hätte die
Gate-Klausel für CONTRA-002/004/005/006 gelautet: „ist `A0` in `[implementation, release]`?" — und
damit **`false`** ergeben. **Vier von sechs Widersprüchen wären am eigenen Gate als
nicht-blockierend erschienen.** Die Werte in der Vorfassung dieser Tabelle standen zwar schon auf
`true`, waren aber **nicht aus der Formel ableitbar** — sie waren faktisch **hartkodiert**. Erst
mit `blocked_gates` stimmen Tabelle und Formel überein.

**Sonderfall `evidence_gate = —`** (CONTRA-001, CONTRA-003): der Eintrag wird über
`blocked_activities` wirksam. CONTRA-003 hat `blocked_gates = []` und
`blocked_activities = [documentation]` — solange dokumentiert wird, ist die Klausel erfüllt und
`blocking = true`. **Ein leeres `blocked_gates` bedeutet nicht „blockiert nie", sondern
„blockiert kein Gate";** die Tätigkeitsachse bleibt davon unberührt.

**Zwei OPEN QUESTIONS der Vorfassung sind damit GESCHLOSSEN** — dokumentiert, nicht gelöscht:

| Frühere OPEN QUESTION | Stand |
|---|---|
| Die letzte Formelklausel war für gatelose Einträge nicht auswertbar und fiel stillschweigend auf `false`. | **Geschlossen.** Die Formel hat jetzt **zwei** unabhängige Klauseln; die Tätigkeitsachse greift auch ohne Gate. |
| Die vier Werte `competition-release`, `territory-release`, `database-schema-finalization` und `account-release` lagen **außerhalb** der vom Nutzer genannten Basis-Liste; unklar war, ob die Liste abschließend oder erweiterbar ist. | **Geschlossen.** Sie sind **reguläre Mitglieder** von `blocked_activities`; der Wertebereich ist abschließend definiert. Ein Validator **darf** unbekannte Werte jetzt als Fehler werten — vorher durfte er das ausdrücklich nicht. Registry §8 Punkt 16 ist geschlossen. |

**Diese Matrix ändert die Registry nicht.** Sie referenziert deren Stand.

### CONTRA-004 — Anti-Cheat vs. Datenminimierung

`status: resolved` · `resolution_status: accepted` · `evidence_status: pending` ·
`blocking: true` (abgeleitet) · `blocked_gates: [C, D]` · `blocked_activities: [competition-release, territory-release]` ·
`evidence_gate: C` · `decision_reference: DEC-011` ·
`evidence_reference: EV-024, EV-034 (teilweise)`

**Rationale.** Der Konflikt zwischen serverseitiger Anti-Cheat-Plausibilität und
Datenminimierung ist durch DEC-011 gelöst: Rohsensorverläufe bleiben lokal, serverseitig laufen
ausschließlich die in REQ-024 abschließend aufgezählten abgeleiteten Plausibilitätssignale.
**Ausstehend** ist der Nachweis, dass der real gesendete Payload diesen Umfang einhält, und dass
fehlende Sensoren nie automatisch zu `rejected` führen.

Betrifft REQ-024 ↔ REQ-034 (Anker CAN-063, CAN-104, CAN-109, CAN-088).

Rohsensorverläufe bleiben standardmäßig **lokal** auf dem Gerät. Der Server erhält für
Wettbewerb, Rankings, Territory und Anti-Cheat ausschließlich minimierte, abgeleitete
Plausibilitätssignale: Kadenzmittel/-band, Geschwindigkeitsband, optionales HF-Band (sofern
vorhanden und freigegeben), GPS-Qualitätswert, Accuracy-Zusammenfassung, Teleport-Indikatoren,
Bewegungsplausibilität, Distanz, Dauer, Sportart, Verifikations-Confidence.

**Nicht** standardmäßig an den Server: vollständige HF-Verläufe, vollständige Schrittverläufe,
vollständige Rohsensorserien, unnötige Health-Rohdaten, zusätzliche personenbezogene Daten.

Status-Stufen: `verified-high` | `verified-standard` | `low-confidence` | `review-required` |
`rejected`. Fehlende Sensoren allein sind **kein** Betrug — sie dürfen die Beweiskraft senken
(`low-confidence`), aber nicht automatisch zu `rejected` führen. Eindeutige Teleports,
physikalisch unmögliche Geschwindigkeiten oder klar widersprüchliche Sensordaten dürfen zu
`review-required` oder `rejected` führen. Weitergehende Rohdatenverarbeitung nur nach
ausdrücklichem Opt-in **oder** für eine konkrete Einspruchs-/Betrugsprüfung, zeitlich begrenzt,
mit dokumentiertem Zweck und definierter Löschung.

### CONTRA-005 — Historie vs. Accountlöschung

`status: resolved` · `resolution_status: accepted` · `evidence_status: pending` ·
`blocking: true` (abgeleitet) · `blocked_gates: [B]` · `blocked_activities: [database-schema-finalization, account-release]` ·
`evidence_gate: B` · `decision_reference: DEC-012` ·
`evidence_reference: EV-017, EV-027 (teilweise), **EV-042**` — **Befund der Vorfassung erledigt.**
Sie hielt fest: „für ‚Datenmodell trennt Identität und historische Aggregate' existiert KEINE
EV-ID" (`EVIDENCE-LEDGER.md`, Marke (z); Registry §8 Punkt 14). Im Auftau-Schritt 2 ist dafür
**EV-042** vergeben worden. **Damit ist Registry §8 Punkt 14 als ID-Frage geschlossen — der
Nachweis selbst bleibt `blocked`,** weil die von DEC-012 geforderte Trennung ohne Retentionsfristen
(OQ-009) nicht spezifizierbar ist. `evidence_status = blocked` und ausdrücklich **nicht** `pending`:
das Hindernis ist **kein fehlender Code**, es bliebe auch mit fertigem Code bestehen.

**Rationale.** Der Konflikt zwischen Historienerhalt und Accountlöschung ist durch DEC-012 gelöst.
Ausstehend ist der Nachweis **wirksamer Anonymisierung** und die **technische Trennung** von
Identität und historischen Aggregaten. Letztere ist laut DEC-012 **vor** Finalisierung des
Datenbankschemas herzustellen — daher `blocked_activities = [database-schema-finalization,
account-release]`; `blocked_gates = [B]` bildet ab, dass die Accountlöschung mit Gate B öffentlich
wird. Obwohl
REQ-027 selbst erst in Stufe D liegt. Der Umstand, dass ein Requirement spät im Release-Plan
liegt, verschiebt eine frühe Architekturschranke nicht nach hinten.

Betrifft REQ-027 ↔ REQ-017 (Anker CAN-066, CAN-056, CAN-084, CAN-088).

Accountlöschung entfernt sämtliche personenbezogenen Daten und Identitätszuordnungen,
mindestens: Profil, E-Mail, Auth-Identitäten, Geräte-/Push-Tokens, private Routen, rohe
GPS-Verläufe, Health-Daten, Stimmungseinträge, Live-Sessions, personenbezogene Kommentare und
Medien sowie die Verknüpfungen zwischen Historieneinträgen und der gelöschten Person.

Historische Team- und Season-Daten dürfen **nur** erhalten bleiben, wenn wirksam anonymisiert und
keine Rückführung mehr möglich ist. Beispiel: „Vincent eroberte Gebiet X.“ wird zu
„Gelöschtes Mitglied eroberte Gebiet X.“ Ist wirksame Anonymisierung nicht möglich, **muss** der
Datensatz gelöscht werden.

Die Formulierung „unveränderliche Historie“ ist projektweit verbindlich zu ersetzen durch:
**„Nach Finalisierung fachlich unveränderbar, außer aufgrund Löschung, Anonymisierung oder
rechtlicher Korrektur.“**
(Sprachregelung: `CONTRA-005` / DEC-012 in `docs/decisions/decision-log.md`. Jeder Datei-Owner
zieht in seiner eigenen Datei nach.)

Datenmodell und Event-Historie müssen Identität und historische Aggregate technisch trennen.
Diese Trennung muss **vor** Erstellung/Finalisierung des Datenbankschemas berücksichtigt werden.

**Umsetzungsstand, repoweit per Textsuche geprüft am 2026-07-19 — die frühere Fassung dieses
Abschnitts behauptete „**überall** ersetzt“ und widersprach damit dieser Datei selbst:**

| Datei | Stand |
|---|---|
| `docs/prd/…prd.md` | **nachgezogen** — REQ-027 = „Seasons und nach Finalisierung fachlich unveränderbare Historie“ (`:138`), EV-027 = „Prüfung der fachlichen Unveränderbarkeit nach Finalisierung“ (`:293`) |
| `docs/traceability.md` (diese Datei) | **nachgezogen** in den Titelfeldern TRC-027 (§1) und der Blocküberschrift REQ-027 (§3) |
| `docs/ID-REGISTRY.md` §6.4 / §6.6 | **nachgezogen im Auftau-Schritt 2026-07-19** — REQ-027 und EV-027 tragen die neuen Titel, beide **wörtlich** aus der `canonical_file` (`prd.md:138` bzw. `:293`) übernommen. Die frühere Zeile „offen, nur durch einen erneuten serialisierten Registry-Schritt änderbar” ist damit erledigt; genau dieser Schritt hat stattgefunden. |
| `docs/traceability.md`, Feld `Evidence Needed`/`Evidence Source` zu REQ-027 | **nachgezogen 2026-07-19** (§3, REQ-027). **Provenienz-Vorbehalt bleibt:** DEC-012 gibt für „Unveränderlichkeitsprüfung” **keine** Ersatzformulierung vor — es wurde keine erfunden; übernommen ist der PRD-Wortlaut. Kanonische Datei für EV-027 ist das PRD, nicht diese Matrix. Ändert der Nutzer die Sprachregelung, ist das PRD die zu ändernde Stelle. |

Die Zeichenfolge bleibt bewusst dort stehen, wo dieses Dokument die **alte** Formulierung
*zitiert*, um die Änderung zu belegen (Befund REQ-027, CONTRA-005-Volltext, §9) — dort ist sie
Beleg, nicht Verwendung.

### CONTRA-006 — Routing-Proxy vs. Local-first

`status: resolved` · `resolution_status: accepted` · `evidence_status: pending` ·
`blocking: true` (abgeleitet) · `blocked_gates: [A0]` · `blocked_activities: [field-test, release]` · `evidence_gate: A0` ·
`decision_reference: OQ-011, DEC-013` **und ein „ADR zum A0-Routing-Proxy” = MISSING** ·
`evidence_reference: EV-006, EV-034; A0-Routing-Evidence (a)…(n) laut docs/EVIDENCE-LEDGER.md`

**Rationale.** Die Kollision zwischen Local-first und serverseitigem Routing ist durch die
Entscheidung für einen transienten, datenminimierten EU-Routing-Proxy **gelöst**; der Nachweis der
Privacy-, Logging-, Retention- und Security-Eigenschaften **steht aus**.

**MISSING im `decision_reference`.** Die Vorgabe nennt einen „ADR zum A0-Routing-Proxy” — **ein
solches Artefakt existiert im Repository nicht** (`find docs -iname “*adr*”` liefert am
2026-07-19 nichts; ADR erscheint nur als Absichtserklärung in CAN-089, DEC-005 und dem
Delivery-Plan). Der Verweis wird als **MISSING** geführt und **nicht** durch ein erfundenes
Dokument ersetzt.

**Warum der frühere Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` entfallen ist.** Er war als
`status`-Wert unzulässig (Registry §3.1) und ist auf die beiden Achsen aufgeteilt. Der von der
Vorfassung beschriebene **Zielkonflikt der Arbeitsanweisung** — an einer Stelle wird
`CONTRA-006 = RESOLVED` als Erfolgskriterium verlangt, an anderer ausdrücklich, dass CONTRA-006
blockierend bleibt, bis Datenfluss, Providerbedingungen, Logging, Retention, Transparenz,
Sicherheitskontrollen und Evidence vollständig geprüft sind — **war kein echter Konflikt, sondern
ein Symptom der Feldüberladung.** Auf zwei Achsen sind beide Forderungen gleichzeitig erfüllbar
und widersprechen sich nicht: `status = resolved` (die Grundsatzfrage *ist* entschieden) **und**
`blocking = true` (der Nachweis steht aus). Der Konflikt ist damit **aufgelöst, nicht
weggeschrieben**; er wurde auch nicht selbst entschieden — das Statusmodell stammt vom Nutzer.

**Was weiterhin gilt.** Ein Großteil der Evidence (Tests gegen Logs, Rate Limit, Secret-Scan des
Bundles) setzt lauffähigen Code voraus. **Es existiert kein Code**, also kann keiner dieser
Nachweise erbracht worden sein. `evidence_status` steht deshalb auf `pending`, nicht auf
`verified`.

Betrifft REQ-006, REQ-007 und REQ-034 (Anker CAN-091 … CAN-097, CAN-095, CAN-131).

Festgelegt ist:

- **Zweckbindung und Persistenz.** Der Proxy verarbeitet Start-/Ziel-/Wegpunktkoordinaten
  ausschließlich transient zur angeforderten Routenberechnung. Keine anwendungsseitige Persistenz
  von Koordinaten, berechneter Route oder vollständigen Request-/Response-Bodies. Keine Werbung,
  Profilbildung, Produktanalyse, Trainingsanalyse, Standortstatistik, Wiederverwendung,
  Modelltraining, kein Verkauf und keine Weitergabe. Retention für Koordinaten-Payload:
  Application 0, Cache 0, Analytics 0.
- **Client-Payload.** Der Client sendet nur: `sport` (`run`|`ride`), erforderliche Koordinaten,
  notwendige Routingparameter, technisch erforderliche Request-ID. **Nicht:** Benutzername,
  E-Mail, Account-ID, Health-Daten, Aktivitätsverlauf, vollständiger GPS-Track, Team-/Profildaten,
  Gerätekennungen (sofern nicht zwingend).
- **Logging.** Request-/Response-Bodies dürfen **nicht** geloggt werden. Nicht in Logs, Traces
  oder Fehlermeldungen: Latitude, Longitude, Wegpunktlisten, vollständige Provider-URLs mit
  Koordinaten, Routengeometrien, Start-/Zieladressen. Zulässig: zufällige Request-ID, Zeitstempel,
  HTTP-Status, Verarbeitungsdauer, Routingprofil, Anzahl Wegpunkte, normalisierte Fehlerkategorie,
  Provider-Latenz, Rate-Limit-Ereignis. Technische Logs dürfen keine Standortrekonstruktion
  ermöglichen. Aufbewahrung technischer Logs: max. 7 Tage, sofern keine nachgewiesene
  technische/gesetzliche Notwendigkeit für eine andere Frist besteht; eine Änderung braucht eine
  dokumentierte Entscheidung.
- **Transport und Secrets.** Nur HTTPS/TLS, keine unverschlüsselten Endpunkte, Provider-Key nur
  serverseitig, keine Secrets in App, Repo oder Logs; Secrets via AWS Secrets Manager oder
  verschlüsselte Lambda-Env, restriktive IAM, Rotation/Widerruf möglich (CAN-092, NFR-007).
- **EU.** Lambda und API Gateway in `eu-central-1` (CAN-096). **Vor dem ersten externen Feldtest**
  zusätzlich zu dokumentieren: Verarbeitungsregion des Routinganbieters, ob Daten den EWR
  verlassen, Unterauftragsverarbeiter, Transfergrundlage. Die Bezeichnung „EU-Proxy“ darf **nicht**
  den Eindruck erwecken, die gesamte Verarbeitung liege in der EU, wenn der nachgelagerte Anbieter
  außerhalb verarbeitet.
- **Provider.** Vor externem Feldtest zu dokumentieren: Rollenverteilung Controller/Processor,
  Auftragsverarbeitungsvertrag, Unterauftragsverarbeiter, Verarbeitungsregion, Provider-Retention,
  Ausschluss eigener Werbe-/Profiling-/Trainingszwecke, Lösch- und Sicherheitsregeln. Wer das nicht
  erfüllt, darf nicht für produktive oder externe A0-Tests eingesetzt werden.
- **Rechtsgrundlage und Transparenz.** Vor dem ersten externen Feldtest: Verantwortlicher, Zweck,
  Rechtsgrundlage, Empfänger/Auftragsverarbeiter, Übermittlungsregionen, Speicherdauer,
  Betroffenenrechte, Datenschutzkontakt. Die Datenschutzerklärung muss vor Nutzung der
  Routenplanung verständlich erklären: „Zur Berechnung deiner Route werden die ausgewählten
  Start-, Ziel- und Wegpunkte kurzfristig an unseren EU-Routing-Proxy und den eingesetzten
  Routinganbieter übermittelt. Die App speichert diese Koordinaten im Proxy nicht dauerhaft.“
- **Missbrauchsschutz.** Rate Limit, Size-Limit, maximale Wegpunktzahl, Timeout, Kill Switch,
  Koordinatenvalidierung und normalisierte Fehler dürfen **nicht** zu dauerhafter
  Koordinatenspeicherung führen. IP-Adressen nur soweit technisch erforderlich, keine dauerhafte
  Speicherung und keine Verknüpfung mit Routenanfragen; separat zu dokumentieren.
- **Fehlerbehandlung.** Providerfehler nie ungefiltert an den Client. Die Fehlerantwort enthält nur
  internen Fehlercode, nutzergeeignete Nachricht, Request-ID und gegebenenfalls einen
  Retry-Hinweis — keine Provider-Secrets, internen URLs, Koordinaten, vollständigen
  Providerantworten und keine Stack Traces.
- **Ablageort.** `infra/routing-proxy/` (CAN-097, OQ-011 resolved), ausdrücklich **nicht**
  `backend/`. **In diesem Lauf nur dokumentiert — nichts davon wurde gebaut, angelegt oder
  deployt; das Verzeichnis existiert nicht.**

**Früherer „Zielkonflikt der Anweisung" — aufgelöst durch das Statusmodell, nicht durch eine
Entscheidung dieser Datei.** Die Vorfassung führte an dieser Stelle einen offenen Zielkonflikt:
einerseits `CONTRA-006 = RESOLVED` als Erfolgskriterium, andererseits „bleibt OPEN/BLOCKING, bis
Evidence vorliegt". Beide Forderungen sind auf zwei Achsen widerspruchsfrei erfüllbar
(`status = resolved` **und** `blocking = true`); die Begründung steht oben im Statusblock. Der
Konflikt bestand nicht in der Sache, sondern darin, dass ein einziges Feld zwei Fragen tragen
sollte. **Nicht aufgelöst und ausdrücklich offen bleibt die Sache selbst:** Verarbeitungsregion
des Routinganbieters, Auftragsverarbeitungsvertrag, Unterauftragsverarbeiter, Transfergrundlage,
Rechtsgrundlage und Transparenztexte sind **vor dem ersten externen Feldtest** zu dokumentieren
und heute sämtlich **MISSING**. Der `infra/routing-proxy/`-Ablageort ist **nur dokumentiert** —
nichts wurde gebaut, angelegt oder deployt; das Verzeichnis existiert nicht und keine
AWS-Ressource wurde erzeugt.

### Local-first-Präzisierung (CAN-095, gilt überall)

> Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal. Für die
> Routenberechnung dürfen ausschließlich die erforderlichen Wegpunkte transient an einen
> kontrollierten Routing-Proxy übertragen werden. Der Proxy speichert keine Koordinaten oder
> Routengeometrien dauerhaft.

Die Mobile-App enthält **keinen** Routing-Provider-Key; sie kennt nur eine konfigurierbare
Proxy-Basis-URL, einen providerneutralen `RoutingPort` und einen `RoutingClient` (CAN-093).
Providername und Providerantwort dürfen nicht in Domain- oder UI-Code gelangen. Der Proxy
übersetzt `run` → `foot-walking` und `ride` → `cycling-regular` (CAN-094).

---

## 8. Abdeckung

**Alle Zahlen sind aus dieser Datei und aus `docs/ID-REGISTRY.md` §6.4 abgeleitet, nicht
fortgeschrieben.** Die Basiszahl aktiver Requirements steht in §0.0. ⚠️ **Weder 36 noch 39 ist ein
gültiger Erwartungswert — und keine der beiden Zahlen darf verboten werden** (Registry §10.2
Bindung 2). Eine Prüfung, die auf einer festen Zahl besteht **oder** eine ausschließt, ist zu
korrigieren, nicht die Daten.

| Prüfung | Ergebnis |
|---|---|
| Aktive Requirements laut Registry §6.4 | **40** (REQ-001…REQ-042 minus REQ-014 und REQ-040 `deprecated`; REQ-000 ist `template-placeholder`) |
| Aktive Requirements in dieser Matrix | **40** ✓ |
| Deprecatete Requirements als `deprecated` geführt, nicht gelöscht | **2 / 2** — REQ-014 und REQ-040 (§1, §3, §4.1, §4.2, §5) |
| Jede aktive REQ-* erscheint genau einmal in der Kernmatrix | ja |
| Jede aktive REQ-* trägt alle Pflichtfelder | **40 / 40** (Messmodell, Verknüpfung, Risiko, offene Entscheidung — §3) |
| Jede AC-* genau einer Requirement zugeordnet | ja. **41 aktive AC gegen 40 REQ ist korrekt:** REQ-019 trägt AC-019 (funktional) **und** AC-041 (Messkriterium). Die 1:1-Erwartung ist zu korrigieren, nicht die Daten (Registry §6.5.1, §10). |
| Jede EV-* verweist auf mindestens eine Requirement bzw. ein Acceptance Criterion | ja. **42 aktive EV gegen 40 REQ ist korrekt:** EV-041 (zweiter Nachweis zu REQ-019) und EV-042 (CONTRA-005 / REQ-017 / REQ-027). |
| Aktive TRC-Zeilen | **40** — 1:1 zu den aktiven Requirements ✓ |
| Vision-Links, die als **erfüllter** Anker zählen | **27 / 40** *(Runde 6, vorher 28; Runde 5 vorher 31)*. Nicht gezählt (**dreizehn**): **REQ-004** (VIS-003 vorhanden, tragende Klausel „verlässliches Tracking" auf Bedürfnisebene unbelegt — *neu Runde 6*), **REQ-006** (Anker entfernt, keine reservierte ID), **REQ-007** (Anker entfernt, keine reservierte ID — *Runde 5*), **REQ-019** (Anker entfernt, keine reservierte ID — *verschärft Runde 5, vorher „trägt nur die Feed-Hälfte"*), **REQ-021** (VIS-004 trägt nur die Team-Hälfte — *Runde 5*), **REQ-022** (VIS-003 trägt nur die Aktivitäts-Hälfte — *Runde 5*), **REQ-031** (Anker entfernt, keine reservierte ID), **REQ-032** (kein Anker, keine reservierte ID), **REQ-037** (VIS-011 unbestätigt), **REQ-038** (VIS-012 reserved, MISSING), **REQ-039** (VIS-013 reserved, MISSING), **REQ-041** (VIS-014 reserved, MISSING), **REQ-042** (VIS-003 ungeprüfte ASSUMPTION). Alle dreizehn in §6.1.1. **Diese Zahl ist deckungsgleich mit dem Zeilenstatus `linked` in der nächsten Zeile — das ist die Gegenprobe:** ein `linked-partial`, `not-linked` oder `broken` darf nie als erfüllter Anker mitgezählt werden. |
| Fehlende Vision-Links (rein syntaktisch) | **8** *(vorher 6)* — REQ-006, **REQ-007**, **REQ-019**, REQ-031, REQ-032, REQ-038, REQ-039, REQ-041. ⚠️ **Diese Zahl allein ist irreführend** und steht nur zum Vergleich hier: sie zählt REQ-037 (Anker vorhanden, unbestätigt), **REQ-004** (Anker vorhanden, tragende Klausel unbelegt — *neu Runde 6*) sowie REQ-021, REQ-022 und REQ-042 (Anker vorhanden, halb bzw. ungeprüft tragend) **nicht** mit. Genau diese Blindheit hatte die Vorfassung „Fehlende Vision-Links \| 0" erzeugt, während REQ-014 an einem **fachlich falschen** Anker hing. **Die syntaktische Zahl ist von 3 über 6 auf 8 gestiegen und in Runde 6 unverändert geblieben, die semantische von 5 über 9 und 12 auf 13** — jedes Mal, weil geprüft wurde, nicht weil sich das Produkt geändert hat. Der Sprung in Runde 5 stammt daraus, dass die vier Quelldokumente erstmals lesbar waren; der Zuwachs in Runde 6 daraus, dass sie jetzt **im Repository** liegen und jede Abwesenheit repo-relativ nachprüfbar ist. **Dass die syntaktische Zahl in Runde 6 stehen bleibt, während die semantische steigt, ist der Beleg dafür, dass die Lücke bei REQ-004 rein syntaktisch unsichtbar ist.** |
| Zeilenstatus der Kernmatrix | linked **27**, broken **8**, not-linked **2**, linked-partial **3** — Summe **40** ✓ *(Runde 6: REQ-004 `linked → not-linked`. Runde 5: REQ-007 und REQ-019 `→ broken`; REQ-021 und REQ-022 `→ linked-partial`; REQ-019 verlässt dabei `linked-partial`.)* ⚠️ **`scripts/validation/verify.py` prüft diese Zeile gegen ein hartkodiertes Literal und meldet deshalb einen Fehlschlag** — bekannte Werkzeug-Falschmeldung, offengelegt in `docs/validation/validation-report.md` §5.2 und Registry §13.3. **Die Zahlen hier sind gezählt; das Literal des Werkzeugs ist es nicht.** Das Werkzeug ist eingefroren und wird nicht angepasst, um einen Zählstand zu bestätigen. |
| Fehlende Canvas-Links (atomar) | **0** — jede aktive Requirement trägt mindestens ein aktives atomares Canvas-Item; **16** tragen zusätzlich einen dokumentierten Problem-BLOCKER (§6.1, vorher 12). ⚠️ **Diese Zeile ist für sich genommen wertlos** und steht nur mit der nächsten zusammen: bis zum 2026-07-20 erfüllte REQ-004 sie mit einem **Risiko-Item** in der Primärspalte. |
| Requirements ohne atomares **Capability**-Item | **1** — REQ-004 (§6.1.2). Getrennt von §6.1 gezählt, weil §6.1 ausschließlich fehlende **Problem**-Anker führt. |
| Reservierte Canvas-IDs (`status = reserved`, Inhalt MISSING) | **6** — CAN-016 … CAN-021. CAN-022, CAN-099 und CAN-130 sind `active`; CAN-071 und CAN-140 sind `deprecated`. |
| Requirements mit Measurement Type | 40 / 40 |
| Requirements mit Signal bzw. Control Evidence | 40 / 40 |
| Requirements mit Target/Pass Condition | 40 / 40 |
| Requirements mit Measurement Window | 40 / 40 |
| Requirements mit Evidence Source | 40 / 40 |
| Requirements mit Owner-Feld | 40 / 40 (davon **40 als sichtbarer OWNER-BLOCKER, 0 echte Owner**) |
| Requirements mit Release Gate | 40 / 40 |
| RESEARCH_HYPOTHESIS mit vollständigem Forschungsplan | 9 / 9 |
| `true-line-status = pending-watcher` | **40 / 40** — maschinell aus der §5-Tabelle gezählt |
| `wired-in-prod? = no` | **40 / 40** — maschinell gezählt |
| `evidence-class = none` | **40 / 40** — maschinell gezählt; es existiert kein Code |
| `Measurement Type` | OPERATIONAL_QUALITY **16**, COMPLIANCE_CONTROL **10**, RESEARCH_HYPOTHESIS **9**, PRODUCT_OUTCOME **5** — Summe **40** ✓ |
| `Source Type` | EXPLICIT **2**, ASSUMPTION **25**, MISSING **13** — Summe **40** ✓ (nach dem PRD-Nachaudit, §2.1). **Die EXPLICIT-Zahl ist trotz drei neuer `EXPLICIT`-Canvas-Items unverändert** — der Source Type eines Requirements folgt nicht dem seines Ankers (§2). |
| `canvas-risk-status` | aligned **16**, risk-introduced **20**, value-risk **2**, blocked **2**, non-goal-violation **0** — Summe **40** ✓ |
| `evidence-class-required` | real-boundary-smoke **25**, production-verified **13**, integration-fake **2**, unit-fake **0** — Summe **40** ✓ |
| Semantisch falsche Anker in Runde 4 **entfernt** | **11** — VIS-008 bei REQ-019/020/021/022 (4) · verbotene Schlusskette bei REQ-037 (2×), REQ-038 (2×), REQ-039 (1×) (5) · VIS-007 bei REQ-004 und REQ-031 (2). Zusätzlich **rollenfalsch** umgestellt: CAN-100 (Risiko in der Capability-Spalte), CAN-130/CAN-127/CAN-128 (Erfolgssignale in der Capability-Spalte), CAN-050 (Anker im falschen Requirement-Kontext), CAN-030 (Universal-Wertanker bei REQ-039). |
| Anker, die **ersetzt** werden konnten, gegen solche, die als BLOCKER offen bleiben | **ersetzt 8** (VIS-003 bei REQ-019/022, VIS-004 bei REQ-020/021, VIS-003 und CAN-028 bei REQ-004, CAN-022 bei REQ-009, CAN-139 bei REQ-039) · **als BLOCKER offengelegt 7** (canvas-problem bei REQ-037/038/039/041/042, Vision bei REQ-006/031). **Kein Item wurde umgedeutet, um eine Lücke zu schließen.** |
| `CONTRA-`Einträge auf dem Statusmodell §3.1 | 6 / 6 (§7.0.1); `blocking` durchweg **abgeleitet und nachgerechnet**, keine ID-spezifische Sonderbehandlung |
| Feld `blocking_scope` als **lebendes Feld** in dieser Datei | **0** — vollständig durch `blocked_gates` + `blocked_activities` ersetzt (§7.0.1). Die 9 verbliebenen Nennungen der Zeichenfolge beschreiben den **entfallenen** Zustand und verwenden ihn nicht. |
| NFRs auf dem Zwei-Achsen-Modell mit `blocked_gates` / `blocked_activities` | **8 / 8** (§6.7) |
| NFRs mit belegter Quelle des Zielwerts | **1 / 8** (nur NFR-007, Klausel „keine Secrets im Client"). Siehe §6.7. |
| NFRs ohne jeden Zielwert | **2 / 8** — NFR-004 (Performance) und NFR-008 (Wartbarkeit). Kein Wert wurde eingesetzt; insbesondere **keine Testabdeckungsquote**. |
| NFRs ohne Gate-Zuordnung | **1 / 8** — NFR-008 (MISSING, OQ-013). |
| Verwaiste NFRs | **0** — NFR-008 war bis zum 2026-07-19 verwaist (Zeichenfolge kam repoweit **einmal** vor, in seiner eigenen Definitionszeile). Es wird jetzt von der Registry §6.13, von OQ-013 und von §6.7.11 dieser Datei referenziert. **NFR-008 ist damit nicht gleichzeitig verwaist und als aktive Anforderung gezählt** — es zählt in der `NFR-`Zeile, nicht in der REQ-Zahl. |
| Deprecatete IDs in Verknüpfungsspalten | **0** |
| Deprecatete IDs in wörtlich übernommenem Messfeld-Text | **4 — siehe §8.1, nicht 0.** Von 6 auf 4 gefallen und neu gezählt. Zwei zusätzliche **aktive** Verweise (REQ-021 → REQ-014, REQ-029 → CAN-071) sind bei dieser Zählung aufgefallen und **korrigiert** worden; sie waren in der Vorfassung nicht erfasst. |
| Ad-hoc-Facetten-IDs als Verknüpfung | 0 (Nennung nur in der Ablösetabelle §0) |
| VC-IDs für die aktiven Requirements | **35 / 40 — BLOCKER.** Die `VC-`Reihe bildet einen Altstand ab; für **REQ-037, REQ-038, REQ-039, REQ-041 und REQ-042 existiert keine VC-ID** und es wird keine erfunden (§5, §6.6). Die vorhandenen VC-IDs haben ohnehin keine Definitionsdatei. **Die Lücke ist in Runde 4 von vier auf fünf Fälle gewachsen**, weil die Teilung von REQ-040 aus einer VC-losen Position zwei gemacht hat. |
| In dieser Datei vergebene neue IDs | **0** |
| In dieser Datei bestätigte Elemente | **0** — kein `user-confirmed`, kein `verified`, kein Watcher-Verdikt |

### 8.1 Restbefund — deprecatete IDs in wörtlich übernommenem Text

Die Messfelder in §3 sind **wörtlich** aus dem Messmodell übernommen und wurden nicht
umgeschrieben. **Vier** dieser Textstellen nennen noch deprecatete Sammelblock-IDs. Das verstößt
gegen Registry-Regel 3 („Kein Dokument referenziert eine ID mit `status = deprecated`“). Der Text
wird hier **nicht** stillschweigend korrigiert, weil er als Beleg wörtlich bleiben soll —
stattdessen steht der Befund offen.

⚠️ **Die Zahl ist von 6 auf 4 gefallen und wurde neu gezählt, nicht fortgeschrieben.**

| Fundstelle | Genannte deprecatete ID | Atomare Nachfolger laut Registry §7.3 |
|---|---|---|
| REQ-015, `Target / Pass Condition` | CAN-009 | CAN-124 … CAN-130 |
| REQ-016, `Target / Pass Condition` | CAN-009 | CAN-124 … CAN-130 |
| REQ-025, `Target / Pass Condition` | CAN-009 | CAN-124 … CAN-130 |
| REQ-028, `Offene Entscheidung` (Canvas-BLOCKER) | CAN-003 | CAN-028 … CAN-038 |

**Zwei Fundstellen der Vorfassung sind entfallen, beide ausgewiesen statt still gestrichen:**

| Entfallene Fundstelle | Grund |
|---|---|
| REQ-008, `Target / Pass Condition` (CAN-009) | Das Feld ist im Zuge der **Verengung** von REQ-008 neu geschrieben worden und nennt CAN-009 nicht mehr. |
| REQ-028, §6.1 (CAN-003, dieselbe Aussage doppelt geführt) | §6.1 ist neu geschrieben; die Formulierung lautet jetzt „keine Nachfolgeklausel der Wertversprechen-Gruppe“ und nennt keine deprecatete ID mehr. |

**Zwei weitere lebende Verweise auf deprecatete IDs sind bei dieser Zählung aufgefallen und
korrigiert worden** — sie waren in der Vorfassung **nicht** als Restbefund erfasst:

| Fundstelle | Was | Korrektur |
|---|---|---|
| REQ-021, `evidence-class-required` | „die UI-Fläche fällt unter **REQ-014** und REQ-025“ — ein **aktiver** Verweis auf eine deprecatete Requirement | nachgezogen auf **REQ-037 und REQ-038** |
| REQ-029, `Offene Entscheidung` | Bereichsangabe „CAN-047..**CAN-071**“, deren Endpunkt seit dem 2026-07-19 deprecated ist | am 2026-07-19 nachgezogen auf „CAN-047..CAN-070 sowie CAN-138..CAN-140“ — **dieser Nachzug war am 2026-07-20 selbst wieder falsch**, weil die Bereichsschreibweise `CAN-138..CAN-140` mechanisch das inzwischen deprecatete **CAN-140** umfasste. **Jetzt als Aufzählung geführt: CAN-138, CAN-139, CAN-142, CAN-143.** ⚠️ **Lehre, ausdrücklich festgehalten:** eine Bereichsangabe über IDs ist gegen spätere Deprecations blind — sie „enthält“ eine ID, die niemand je hingeschrieben hat. Dieselbe Falle steckte in der Legacy-Spalte des Canvas. Bereichsschreibweisen über ID-Räume sind zu vermeiden. |

⚠️ **Methodischer Befund zur Zählung selbst.** Die erste Zählung dieses Nachzugs benutzte den
Ausschluss `CAN-009(?![-\d])` und war damit **blind für deutsche Bindestrich-Komposita**: die
Fundstelle bei REQ-016 lautet „kein **CAN-009-/VIS-006**-Signal“ und wurde nicht erkannt. Der
Ausschluss wurde auf `(?!\d)` korrigiert und die Zählung wiederholt. **Korrigiert wurde die
Prüfung, nicht der Befund** — die Fundstelle bei REQ-016 ist echt und steht oben in der Tabelle.

**Nicht als Restbefund gezählt** und ausdrücklich zulässig: der Deprecation-Block zu REQ-014 in
§3, die Migrationsangaben bei REQ-008, REQ-032, REQ-037 und REQ-038 sowie die Ablösetabelle in §0.
Sie **benennen** deprecatete IDs, um deren Ablösung zu belegen, und **verknüpfen** nicht mit ihnen.
Registry-Regel 3 verbietet die Referenz, nicht den Migrationsbeleg.

Alle verbliebenen Aussagen bleiben inhaltlich richtig — sie stellen fest, dass **kein**
Nachfolgeitem des jeweiligen Blocks das Requirement trägt. **Ergänzung 2026-07-19:** die
Klammerzusätze „(+ CAN-130 reserved)“ sind entfallen, weil **CAN-130 seit dem 2026-07-19 `active`
ist**. Die Aussagen zu REQ-015, REQ-016 und REQ-025 bleiben davon unberührt: CAN-130 ist ein
Signal für **Routenempfehlungen** und trägt weder Progression noch Recaps noch Challenges.

### Nicht als erfüllte Referenz gezählt

Reservierte Canvas-IDs (`status = reserved`, Inhalt MISSING) werden gemäß Registry §3 **nicht**
als erfüllte Referenz gezählt. Sie erscheinen in §4 und §6.1 ausdrücklich als BLOCKER — **es sind
jetzt sechs statt zehn**: CAN-016, CAN-017, CAN-018, CAN-019, CAN-020, CAN-021.

**Nicht mehr in dieser Liste:** **CAN-022**, **CAN-099** und **CAN-130** sind seit dem 2026-07-19
`active` und zählen als erfüllte Referenz; **CAN-071** ist `deprecated`. ⚠️ **Nachfolgekette
transitiv aufgelöst (2026-07-20):** die frühere Formulierung „durch CAN-138, CAN-139 und CAN-140
ersetzt" nannte mit **CAN-140** eine ID, die seit dem 2026-07-20 selbst `deprecated` ist. Die
**wirksame** Nachfolgemenge von CAN-071 ist **CAN-138, CAN-139, CAN-142, CAN-143**. Wer eine
Deprecation-Kette mechanisch auflöst, muss ihr **bis zu einem aktiven Eintrag** folgen — ein
Nachzug, der auf CAN-140 stehen bleibt, landet wieder auf einer deprecateten ID. Dieselbe Regel
gilt für REQ-008 → REQ-040 → REQ-041/REQ-042.

`REQ-000`, `AC-000` und `EV-000` sind Template-Platzhalter der Eintragsvorlage in
`docs/EVIDENCE-LEDGER.md` (Registry §4) und **keine** Requirements. Sie erscheinen in dieser
Matrix nicht und sind von jeder Abdeckungszählung ausgenommen — auch von der Ableitung in §0.0.

---

## 9. Statusnachzug in anderen Dateien (hier nicht geändert)

Diese Datei hat ausschließlich `docs/traceability.md` verändert. Die folgenden Punkte gehören
anderen Datei-Ownern:

| Datei | Nachzug |
|---|---|
| `docs/decisions/open-questions.md` | **kein Nachzug offen** (geprüft am 2026-07-19). Die frühere Fassung behauptete hier, OQ-011 werde „weiterhin als offen geführt“ — das ist falsch: `open-questions.md:17` führt OQ-011 als **RESOLVED (Nutzer, 2026-07-19)** mit Auflösungsabschnitt ab `:19`. Datei und Registry stimmen überein. |
| `docs/decisions/decision-log.md` | **kein Nachzug offen** (erneut geprüft am 2026-07-19 nach dem Statusmodell-Nachzug). Der Ledger trägt die Statusfelder nach Registry §3.1 für alle sechs CONTRA-IDs; der frühere Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` kommt dort nur noch als **Zitat des korrigierten Alt-Werts** vor (`:47`, `:346`), nicht mehr als `status`. **Zwei überholte Aussagen der Vorfassung dieser Zeile sind entfernt:** (1) „der Ledger führt alle drei noch als `open`" — war schon am 2026-07-19 falsch; (2) „`:19` CONTRA-006 als DESIGN-RESOLVED / EVIDENCE-PENDING" und „offen ist allein die eingefrorene Registry" — beides ist seit dem Nachzug in Ledger und Registry überholt. |
| `docs/ID-REGISTRY.md` (wieder eingefroren) | **kein Nachzug offen** (geprüft am 2026-07-19 nach dem Auftau-Schritt). Die frühere Fassung führte hier „§6.11 führt CONTRA-004/005/006 als `open`; §6.4 führt REQ-027 als ‚Seasons und unveränderliche Historie'” — beides ist erledigt: §3.1 trägt das Statusmodell, §6.11.1 die Statusfelder je CONTRA-ID, §6.4/§6.6 die nachgezogenen Titel von REQ-027/EV-027, §6.1 den neuen Eintrag VIS-011. **Offen und ausdrücklich nicht in diesem Schritt vergeben:** eine EV-ID für „Datenmodell trennt Identität und historische Aggregate” (Registry §8 Punkt 14) — das ist ein neuer serialisierter Registry-Schritt. |
| `docs/validation/validation-report.md` — **Feld-Nachzug `blocking_scope`** | **BLOCKER, einziger verbliebener Owner.** Das Feld ist projektweit entfallen (C16, Registry §3.1), wird dort aber **noch als lebendes Feld geführt**: Spaltenüberschriften in zwei Tabellen und die **alte Formel** mit der Klausel „das aktuell geprüfte Gate ist in `blocking_scope` enthalten". ⚠️ **Ein reines Umbenennen genügt nicht:** `blocked_gates` war vorher **nicht darstellbar** und ist **neu zu befüllen**. Solange dort die alte Formel steht, reproduziert jede daran orientierte Prüfung den behobenen Defekt und liefert für gegatete Einträge fälschlich `false`. |
| Nachgezogen — **kein Nachzug mehr offen** (geprüft am 2026-07-19) | `docs/prd/…prd.md`, `docs/decisions/decision-log.md`, `docs/EVIDENCE-LEDGER.md`, `docs/vision/…vision.md`, `docs/canvas/…canvas.md`, `docs/decisions/open-questions.md`. **Befund zur Messmethode, offengelegt:** eine reine Zeichenkettenzählung von „`blocking_scope`" weist in vier dieser Dateien weiterhin Treffer aus (PRD 6, decision-log 4, vision 3, Ledger 2). Die Einzelprüfung zeigt: **alle sind Migrationsbeschreibungen** — sie *benennen* das entfallene Feld, um seine Entfernung zu belegen, und verwenden es nicht. **Eine Zählung, die das nicht unterscheidet, meldet einen Nachzug, den es nicht gibt.** Dieselbe Unterscheidung gilt für die 9 verbliebenen Vorkommen in **dieser** Datei (§0.2 Nr. 8, §7.0.1). |
| `docs/prd/…prd.md` — **Messwert im C16-Abschnitt veraltet** | `prd.md` beziffert die Restvorkommen mit „`docs/traceability.md` (20 Vorkommen), `docs/decisions/decision-log.md` (9) …". Diese Zahlen sind der Stand **vor** den Nachzügen der jeweiligen Owner. Für diese Datei sind 0 lebende Verwendungen verblieben. Nachzug beim PRD-Owner; **hier nicht geändert.** |
| **Gemeinsame Implementierung der Blocking-Funktion** | **BLOCKER, keinem Owner zugewiesen.** Alle Validatoren sollen **dieselbe** kanonische Funktion importieren. Es existiert **kein ausführbares Prüfwerkzeug im Repository** (Registry §9) — die Formel ist damit Spezifikation, kein Nachweis. |
| `docs/prd/…prd.md` — **NFR-Tabelle** | **Nachzug offen:** `prd.md:194-201` führt alle acht NFRs als `EXPLICIT` in einer Tabelle **ohne Quellenspalte**. Nach §6.7 ist genau eine dieser Angaben haltbar (NFR-007). Besonders zu korrigieren: **NFR-002**, wo das PRD sich selbst widerspricht (`:195` EXPLICIT vs. `:362` „nicht empirisch belegt”, DIV-5). Diese Matrix ändert das PRD **nicht**. |
| `docs/prd/…prd.md` | ASM-001 … ASM-004 → ASM-101 … ASM-104 (Registry §7.1); fehlende USER-ID für „ambitionierte Ausdauersportler:innen“ (CAN-025). **Nicht mehr offen:** der Titel von REQ-027 ist im PRD bereits nachgezogen (`:138`), ebenso EV-027 (`:293`) — die frühere Fassung führte ihn hier zu Unrecht als offen. |
| `docs/vision/…vision.md` | ASM-001 … ASM-003 → ASM-201 … ASM-203 (Registry §7.1). |
| `docs/canvas/…canvas.md` | Inhalt der **sechs** verbliebenen reservierten CAN-Items (CAN-016…CAN-021) ist eine Nutzerentscheidung. **Korrigiert von „zehn":** CAN-022, CAN-099 und CAN-130 sind seit dem 2026-07-19 `active`, CAN-071 ist `deprecated`. |
| `docs/ID-REGISTRY.md` §6.6 — **Kettenfelder TRC-008, TRC-019, TRC-032** | **Nachzug offen, Registry eingefroren.** Die Registry führt für diese drei Zeilen noch die Kette mit dem deprecateten Sammelblock-Item **CAN-005**, für TRC-032 zusätzlich **VIS-005**. Sie weist die Umstellung ausdrücklich dem **Traceability-Owner in Phase 3** zu; sie ist in dieser Matrix vollzogen (CAN-138, CAN-130, CAN-022; VIS-005 entfernt). **Das Kettenfeld der Registry bildet damit den Altstand ab** — sichtbar gemacht statt still divergiert (§6.5 Zeile 6). |
| `docs/prd/…prd.md` — **`source_type`-Nachaudit** | **Kein Nachzug offen, Richtung umgekehrt:** das PRD hat die 17 `EXPLICIT`-Zeilen einzeln geprüft und 16 herabgestuft; **diese Matrix ist dem PRD gefolgt** (§2.1). Die frühere Zeile „PRD führt alle acht NFRs als EXPLICIT" ist erledigt — `prd.md` trägt die NFR-Einstufungen nach dem Zwei-Achsen-Modell. |
| Vision-Items **VIS-012**, **VIS-013**, **VIS-014** sowie Items zu „vollständigen und erklärbaren Trainingsdaten", zur **Routenplanung**, zur **Sicherheitsassistenz**, zum **routenbezogenen Fortschritt** und zu **Routenempfehlung/Feed** | **BLOCKER, Owner ist der Nutzer. Erneut gewachsen am 2026-07-20 (Runde 5).** VIS-012, VIS-013 und VIS-014 sind `reserved` mit Inhalt **MISSING**. Für **REQ-032** (Trainingsdaten), **REQ-006** (Routenplanung), **REQ-031** (Sicherheitsassistenz), **REQ-007** (routenbezogener Fortschritt, *neu*) und **REQ-019** (Routenempfehlung/Feed, *neu*) ist **nicht einmal eine VIS-ID reserviert** — MISSING-Positionen, keine Leerstellen. Damit haben **acht** Requirements keinen Vision-Anker (REQ-006, REQ-007, REQ-019, REQ-031, REQ-032, REQ-038, REQ-039, REQ-041), **eines** einen unbestätigten (REQ-037) und **drei** einen halb bzw. ungeprüft tragenden (REQ-021, REQ-022, REQ-042) — §6.1.1. **ID-Bedarf: zwei weitere VIS-IDs** (routenbezogener Fortschritt, Routenempfehlung/Feed) — hier wird **keine Nummer genannt und keine vergeben**; die Registry ist eingefroren, die Vergabe liegt allein beim Registry-Owner. Der Inhalt wäre in jedem Fall neue Produktsubstanz und wird hier **nicht erfunden**. |
| `docs/vision/…vision.md` — **VIS-008-Entlastung** | **Nachzug offen.** Die Vision-Datei kann Abschnitte enthalten, die VIS-008 weiterhin als Anker der Community-Requirements (REQ-019…REQ-022) beschreiben. Diese Matrix hat die Verknüpfungen entfernt; die **Vision-Datei ändert sie nicht** — sie gehört einem anderen Owner. |
| `docs/prd/…prd.md`, `docs/canvas/…canvas.md`, `docs/EVIDENCE-LEDGER.md` — **REQ-006, REQ-031, REQ-004, REQ-009** | **Nachzug offen, neu am 2026-07-20.** Die hier entfernten Anker (VIS-003 ↔ REQ-006, VIS-007 ↔ REQ-004 und ↔ REQ-031, CAN-013 ↔ REQ-009, CAN-100 als Primäranker von REQ-004, CAN-030 als Wertanker von REQ-039) können in diesen Dateien noch stehen. **Diese Matrix ändert sie nicht.** Solange sie dort stehen, meldet eine dateiübergreifende Prüfung einen Widerspruch — **das ist richtig so und darf nicht durch Angleichung an den Altstand beseitigt werden.** |
| `docs/ID-REGISTRY.md` — **OQ-015 referenziert vier deprecatete IDs** | **BLOCKER beim Registry-Owner.** §8 Punkt 28 und die OQ-015-Zeile nennen REQ-040, AC-040, EV-040 und CAN-140 — alle vier hat dieselbe Runde deprecatet. Nach Registry §9 Bedingung 3 ist das ein Validierungsfehler **in der eingefrorenen Registry selbst**. Diese Matrix zieht auf REQ-042/AC-043/EV-044/CAN-143 nach und **spiegelt den Fehler nicht**. |
| `docs/ID-REGISTRY.md` — **§7.5.5 gegen §8 Punkt 37 bei REQ-038** | **Nachzug offen beim Registry-Owner.** Zwei Registry-Stellen verlangen Unterschiedliches (Feldwert „MISSING (begründet)" gegen Einstufung als BLOCKER). Behandlung hier: §6.5 Zeile 8. |
| `docs/ID-REGISTRY.md` — **Gate von CAN-022** | **OPEN QUESTION beim Registry-Owner.** CAN-022 trägt Release Gate E, ist seit dem 2026-07-20 aber auch canvas-problem-Anker von REQ-009 (Gate A1). Ob ein Problem-Item ein eigenes Gate trägt, ist im Metamodell nicht geregelt (§6.5 Zeile 10). |
| `docs/decisions/open-questions.md` — **OQ-012 … OQ-016** | **Kein Nachzug offen** (geprüft am 2026-07-19): die fünf offenen Fragen sind dort eingetragen. Diese Matrix referenziert sie in §3 (REQ-019, REQ-039, **REQ-042**) und §6.7.11 (OQ-013). *Nachgezogen 2026-07-20: OQ-015 hängt jetzt an REQ-042, nicht mehr am deprecateten REQ-040.* |
| `docs/architecture/revyr-target-architecture.md` | §6 führt `routingProfile` app-seitig, obwohl CAN-094 die Profilübersetzung im Proxy verortet; §9 nennt noch „Public Key im Development“ und bindet den Proxy an „Produktion“ — überholt durch CAN-091/CAN-092. |
| `docs/EVIDENCE-LEDGER.md` | Empfehlung der Registry §4: Eintragsvorlage auf eine Nicht-ID-Notation umstellen (z. B. `<REQ-ID>`), damit REQ-000/AC-000/EV-000 keine Fehlalarme mehr erzeugen. |
| `docs/canvas/…canvas.md` — **Runde-6-Herabstufungen (Nutzerauftrag Punkt 2 und 3)** | **Nachzug offen, Owner Canvas.** Diese Matrix hat die Herabstufungen von **CAN-119**, **CAN-109**, **CAN-024**, **CAN-051** und die Streichung der Web-Erstreckung aus **CAN-099** in ihren eigenen Feldern **abgebildet**, aber sie ändert den Canvas **nicht**. Solange die Items dort ihren alten Source Type bzw. Wortlaut tragen, meldet eine dateiübergreifende Prüfung einen Widerspruch — **das ist richtig so und darf nicht durch Angleichung an den Altstand beseitigt werden.** ⚠️ **Ausdrücklich nicht vorweggenommen:** der endgültige Wortlaut von CAN-024 und die Frage, ob CAN-119 den Matrix- oder den Review-Teil behält. Die Gegenprüfung hat dafür **einander widersprechende** Fassungen vorgeschlagen; die Wahl ist eine Nutzerentscheidung. |
| `docs/prd/…prd.md` — **atomarer Nachzug REQ-037 / AC-037 / NFR-005** | **BLOCKER, Owner PRD.** Die Web-Erstreckung ist hier entfernt (§3 REQ-037), steht aber noch im PRD: Anforderungstext REQ-037, **`Given`-Spalte von AC-037** und **`signal` von NFR-005**. **Der Schnitt muss atomar sein.** Bleibt er im PRD stehen, trägt AC-037 eine Vorbedingung, für die es nach dieser Runde **keinen Canvas-Anker mehr gibt** — ein neuer Traceability-Defekt statt eines behobenen. Dasselbe gilt für `docs/EVIDENCE-LEDGER.md` (EV-037-Kopf zitiert REQ-037 inklusive Web-Auskopplungen). |
| `docs/prd/…prd.md` — **REQ-007, `Target / Pass Condition` und `source_type`** | **Nachzug offen, Owner PRD.** (1) Die Berufung auf CAN-051 als Autorität („hält fest, dass die Subtraktion ausdrücklich verboten ist") ist hier entfernt und steht im PRD noch. (2) **Feldbenennung:** `prd.md` führt REQ-007 mit `ASSUMPTION` (Anforderungsherkunft), diese Matrix mit `MISSING` (Zielwertherkunft). **Das ist kein Widerspruch, sondern eine Namenskollision zweier Achsen unter demselben Label.** Die Auflösung ist eine Umbenennung auf `target_source_type` und damit ein **Metamodell-Eingriff beim Registry-Owner** — hier ausdrücklich **nicht** durch Angleichung eines der beiden Werte vorweggenommen. |
| `docs/prd/…prd.md` — **REQ-033, „Privacy-Review"** | **Nachzug offen, Owner PRD.** Die Messfelder dieser Matrix sind wörtlich aus der `canonical_file` übernommen und deshalb **unverändert** geblieben; der Befund ist am Requirement offengelegt. Betroffen im PRD: **AC-033** (`Given`: „Claims-Whitelist und Privacy-Review sind freigegeben"), `signal`, `measurement_window` und `research_plan` Stufe 3 von REQ-033. **Der Begriff ist in keiner der vier Quellen belegt**; wortnah gedeckt ist nur eine datenklassengebundene Einzelprüfung (`docs/sources/SRC-003-…:629`, `:715`). |
| `docs/risks/revyr-risk-register.md` — **RISK-006, RISK-013, RISK-022** | **Nachzug offen, Owner Risiko.** Drei Gegenmaßnahmen benennen Mechanismen, die in keiner der vier Quellen vorkommen: **RISK-006** „Polyline-Projektion, Hysterese, Off-Route-Fixtures" (A0, high), **RISK-013** „mehrstufige Confidence, Review, Testdaten und **Appeal-Flow**", **RISK-022** „DPIA/**Privacy Review**". Sie sind als **ASSUMPTION-abgeleitet** zu kennzeichnen. **Die Risiken selbst bleiben `open`** — diese Matrix schließt keines und senkt keine Einstufung. |
| `docs/decisions/decision-log.md` — **DEC-004** | **OPEN QUESTION beim Entscheidungs-Owner.** DEC-004 („Route-Fortschritt basiert auf Polyline-Projektion und Off-Route-Logik") steht auf `proposed` und ist zugleich der **alleinige** Träger der Pass-Bedingung von REQ-007, die von `docs/sources/SRC-004-…:416-417` bewusst abweicht. Nutzerauftrag Punkt 4 erhält REQ-007 ausdrücklich — **die Bestätigung von DEC-004 steht davon getrennt weiterhin aus.** |
| `scripts/validation/verify.py` — **D-Tally** | **Kein Nachzug durch diesen Owner, ausdrücklich.** Das Werkzeug vergleicht den Zeilenstatus mit einem hartkodierten Literal und meldet nach der Runde-6-Herabstufung weiterhin einen Fehlschlag. Nach Registry §13.3 ist ein fehlgeschlagener Check ein **Befund**, der am Dokument behoben wird, **nicht am Werkzeug**; die Werkzeuge sind eingefroren (Nutzerauftrag Punkt 6). **Die Zahlen in §8 sind gezählt, nicht an das Literal angepasst.** Die Falschmeldung ist in `docs/validation/validation-report.md` §5.2 offengelegt. |

---

## 10. Bestätigung

Die Matrix ist vollständig verknüpft und mit dem Messmodell verschränkt, aber **nicht durch den
Nutzer bestätigt**. Die Assistenz bestätigt sie nicht in seinem Namen.
Höchster erreichbarer Stand nach dieser Korrektur: **`READY_FOR_USER_CONFIRMATION`**.
`true-line-status` bleibt bei **allen aktiven Requirements** `pending-watcher` — die aus der
Registry abgeleitete Zahl (§0.0), einschließlich REQ-041 und REQ-042. `wired-in-prod?`
bleibt `no`, `evidence-class` bleibt `none`; es existiert kein Code. **Ein Plumbline-Watcher-
Verdikt wird hier nicht ausgestellt**, und der Gesamtstatus des Vorhabens bleibt
**BLOCKED_TRACEABILITY**.
