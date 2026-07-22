# Product Canvas: REVYR Endurance Platform

Status: ready-for-user-confirmation  
Feature Slug: `revyr-endurance-platform`  
Public Brand: MISSING – REVYR ist vorläufiger Arbeitstitel  
ID-Hoheit: `docs/ID-REGISTRY.md`

## ID-Hoheit und Referenzregel

`docs/ID-REGISTRY.md` ist die einzige kanonische Quelle für CAN-IDs. Dieser Canvas **führt**
die Inhalte seiner Items, **vergibt** aber keine IDs. Bei Abweichung gilt die Registry.

Ab Phase 2 ist die Registry eingefroren: Wer ein fehlendes Canvas-Item braucht, meldet das als
BLOCKER zurück und legt keine ID an.

**Was sich am 2026-07-19 geändert hat.** Die zwölf ursprünglichen Canvas-Items waren
Sammelblöcke: eine Tabellenzelle enthielt mehrere unabhängig prüfbare Aussagen. Ein Requirement
konnte deshalb nur auf einen ganzen Prosaabschnitt zeigen statt auf die eine Aussage, die es
tatsächlich trägt. Drei Beispiele aus dem Bestand:

- Die Klausel „Verlässliches Tracking“ stand ausschließlich im Prosa-Block „Value Promise“ und
  **nicht** in der CAN-003-Tabellenzeile. Sieben A0-Requirements (REQ-001 bis REQ-007) konnten
  ihren Wertbezug deshalb nur auf Prosa stützen. Jetzt: **CAN-028**.
- CAN-001 nannte weder ein Fortschritts- noch ein Sicherheits- noch ein Datenschutzproblem,
  obwohl 14 Requirements ein solches Problem bräuchten. Diese Lücken sind jetzt als reservierte,
  inhaltlich offene Items sichtbar (CAN-016 bis CAN-022) statt unsichtbar. **Nachtrag:** CAN-022
  ist am selben Tag im Auftau-Schritt 2 inhaltlich entschieden worden und steht deshalb nicht
  mehr in der Reserve-Tabelle, sondern unter „Problem". CAN-016 bis CAN-021 bleiben reserviert
  und inhaltlich MISSING.
- CAN-002 nannte „ambitionierte Ausdauersportler:innen“, wofür das PRD keine USER-ID führt.
  Jetzt: **CAN-025**, ausdrücklich als BLOCKER markiert.

Die alten IDs bleiben mit `status = deprecated` in der Registry erhalten und werden nicht
wiederverwendet. Der Ursprungstext bleibt weiter unten wörtlich stehen.

**Was der Auftau-Schritt 2 am 2026-07-19 zusätzlich geändert hat.** Sieben Items sind
hinzugekommen oder inhaltlich gefüllt worden; ein Item ist deprecatet worden. Alle IDs stammen
aus `docs/ID-REGISTRY.md` (§6.3, §6.3.1, §6.3.2, §7.4) und aus der Migrationstabelle des
ID-Ownership-Laufs. **Dieser Canvas hat keine ID vergeben.**

| ID | Was | Vorher |
|---|---|---|
| ~~CAN-071~~ | deprecatet, ersetzt durch CAN-138, CAN-139, CAN-140 | reserviert, Inhalt MISSING |
| CAN-138 | Verlauf und Detailansicht (Stufe A0) | Teil von CAN-071 |
| CAN-139 | GPX-Export (Stufe A2) | Teil von CAN-071 |
| ~~CAN-140~~ | Streckenwiederverwendung und Vergleich (Stufe A2) — **am 2026-07-20 selbst deprecatet**, siehe Runde-4-Tabelle unten | Teil von CAN-071 |
| CAN-141 | Monochromes tokenbasiertes Designsystem | existierte nicht |
| CAN-022 | Datenqualitätsproblem ohne Wearable-/Sensoranbindung | reserviert, Inhalt MISSING |
| CAN-099 | Accessibility, WCAG 2.2 AA — **nur noch** Accessibility | reserviert, Inhalt MISSING |
| CAN-130 | Erfolgssignal übernommene Routen je Empfehlung | reserviert, Inhalt MISSING |

Der Defekt hinter CAN-071 ist derselbe wie der oben beschriebene, nur eine Ebene tiefer: das
Item trug drei fachlich getrennte Capabilities auf **zwei verschiedenen Release-Stufen** (A0
bzw. A2). Eine gemeinsame ID kann nicht gleichzeitig zu zwei Gates fällig sein. Der
Designsystem-Anteil, den CAN-099 bisher implizit mittrug, ist nach CAN-141 ausgelagert:
CAN-099 regelt **Zugänglichkeit**, CAN-141 die **Gestaltungssprache**.

**Was Runde 4 am 2026-07-20 geändert hat.** Drei aktive Items haben den kanonischen Wortlaut
der Nutzerentscheidung erhalten, ein Composite ist geteilt worden, und eine doppelt geführte
Pflicht ist einseitig aufgelöst. Alle IDs stammen aus `docs/ID-REGISTRY.md` (§6.3.1, §6.3.3,
§7.5). **Dieser Canvas hat auch in Runde 4 keine ID vergeben.**

| ID | Was | Vorher |
|---|---|---|
| CAN-099 | kanonischer Wortlaut A · Item Type **CONSTRAINT / VALUE BOUNDARY** · Source Type **EXPLICIT** · trägt die Farbregel jetzt kanonisch | Wortlaut Runde 3, Item Type `constraint`, Source Type MISSING |
| CAN-141 | kanonischer Wortlaut B · Item Type **DESIGN CONSTRAINT / PRODUCT PRINCIPLE** · generische Farbregel **entfernt** | Wortlaut Runde 3, Item Type `constraint`, Farbregel doppelt geführt |
| CAN-139 | kanonischer Wortlaut C · Item Type **VALUE PROMISE / CAPABILITY** · Source Type **EXPLICIT** | Wortlaut Runde 3, Item Type `capability`, ASSUMPTION, Fremd-App-Klausel im Wortlaut |
| CAN-138 | kanonischer Wortlaut, **bleibt ungeteilt** | „…eine Detailansicht mit Strecke, Dauer, Distanz … öffnen" |
| ~~CAN-140~~ | deprecatet, ersetzt durch **CAN-142** (Planung) und **CAN-143** (Auswertung) | aktiv, Composite aus zwei Aussagen |
| CAN-142 | Wiederverwendung einer gespeicherten Route (A2) | Teil von CAN-140 |
| CAN-143 | Vergleich fachlich vergleichbarer Aktivitäten (A2) | Teil von CAN-140 |

**Abweichung von der wörtlichen Anweisung — ausdrücklich gemeldet (Registry §6.3.3).** Die
Anweisung lautete, für die drei kanonischen Aussagen A, B und C „jeweils die nächste
tatsächlich freie CAN-ID zu reservieren". Für alle drei existierte bereits ein **aktives** Item
(CAN-099, CAN-141, CAN-139), das dieselbe Aussage trägt. Drei neue IDs hätten drei Dubletten
erzeugt — genau die Defektklasse, gegen die dieselbe Entscheidung die Regel aufstellt, nicht
beide Items aktiv zu lassen. Deshalb wurde jeweils das vorhandene Item auf den kanonischen Text
gezogen und **keine** neue ID vergeben. Der Nutzer kann das überstimmen; dann wären CAN-099,
CAN-139 und CAN-141 zu deprecaten und drei weitere freie IDs zu vergeben. Die
Wortlautbestätigung selbst ist offen (Registry §8 Punkt 43).

**Transitive Nachfolge — wichtig für jeden mechanischen Nachzug.** Die `replacement_id` von
CAN-071 bleibt nach Registry-Regel 1 unverändert bei CAN-138, CAN-139, CAN-140. Die **wirksame
Nachfolgemenge** ist aber CAN-138, CAN-139, **CAN-142, CAN-143** — CAN-140 ist seit dem
2026-07-20 selbst deprecatet. Wer CAN-071 auflöst, muss die Kette bis zu einem **aktiven**
Eintrag weiterverfolgen; ein Nachzug, der auf CAN-140 stehen bleibt, landet auf einer
deprecateten ID.

**Was Runde 6 am 2026-07-20 geändert hat (Quellen- und Belegnachzug).** Die vier Quelldokumente
liegen seit diesem Lauf im Repository unter `docs/sources/` und sind damit erstmals unmittelbar
zitierfähig; alle Fundstellen unten sind gegen diese Dateien nachgeschlagen, nicht übernommen.
Sechs Items sind nachgeprüft worden. **Es wurde keine ID vergeben, kein Item umgedeutet und
nichts hochgestuft.** Jede Herabstufung steht mit Datum, Grund und Fundstelle in der
Befundspalte des betroffenen Items. Der Gesamtstatus bleibt `BLOCKED_TRACEABILITY`;
`true-line-status` bleibt `pending-watcher`. Nichts in dieser Runde ist eine Freigabe oder ein
Gate-Verdikt.

| ID | Was | Vorher |
|---|---|---|
| CAN-024 | **Aussage verengt** auf „Radfahrer:innen (Rangstufe primär)"; Source Type EXPLICIT bleibt, Herkunft unverändert | „Freizeit- und Rennradfahrer:innen", EXPLICIT |
| CAN-051 | **Source Type EXPLICIT → ASSUMPTION**; Source als **TEILBELEGT** ausgewiesen; Wortlaut unverändert | EXPLICIT (SRC-001/SRC-003) |
| CAN-099 | **Erstreckung auf „nutzbare Web-Auskopplungen" aus dem Wortlaut entfernt** (Nutzerauftrag); Source Type gespalten geführt; Falschaussage zu AC-037 korrigiert | Wortlaut Runde 4, Source Type EXPLICIT |
| CAN-109 | Source Type **EXPLICIT → ASSUMPTION**; Begründung verschärft, Fundstellen ergänzt, zwei Aussagen korrigiert | EXPLICIT (SRC-003) |
| CAN-119 | Aussage auf „Sichtbarkeits-Matrix (Testtabelle Plan 7)" **verkürzt**; Selbstwiderspruch, Lineage der gestrichenen Klausel und EV-018-Konflikt offengelegt | EXPLICIT (SRC-003), Wortlaut „Privacy-Matrix und Privacy-Review" |
| CAN-141 | **nur Befundpräzisierung** — Aussage, Item Type und Source Type unverändert | Wortlaut Runde 4 |

**Werkzeugbefund zur Entstehung dieses Eintrags (2026-07-20, nachträglich korrigiert).** Die
Änderungen an CAN-109 und CAN-119 sind innerhalb **eines** Laufs von **mehreren gleichzeitig
arbeitenden Bearbeitungsschritten** vorgenommen worden. Die Vorfassung dieses Absatzes deutete
das als **zwei getrennte Runden** („Runde 5" und „Runde 6") und behauptete einen „zweiten
Bearbeiter". **Das war falsch und ist hier ersetzt, nicht stehen gelassen.** Es gab an diesem
Tag **einen** Lauf — Runde 6 — mit **einer** Nutzeranweisung. Die Doppelbezeichnung war ein
Artefakt der Bearbeitungswerkzeuge, kein Vorgang im Projekt. Inhaltlich ist an den Befunden zu
CAN-109 und CAN-119 dadurch nichts geändert; korrigiert ist ausschließlich ihre Datierung und
ihre Zuschreibung.

**Warum CAN-119 nicht zusätzlich verengt oder zurückgesetzt worden ist.** Es lagen mehrere,
einander widersprechende Verengungsvorschläge vor. Der eine verlangte, die Matrix-Hälfte zu
behalten und den Review-Teil abzutrennen; der andere das Gegenteil, weil die Matrix bereits als
**EV-018** über **CAN-057** vollständig verkettet geführt wird und eine Verengung auf sie ein
anbindungsloses Zweitexemplar erzeugte — und weil ausgerechnet die gestrichene Review-Klausel
diejenige mit belegter Canvas-Herkunft ist (Ursprungstext „## Evidence", Zeile 584:
„- Claims-, Privacy- und Threat-Model-Reviews."). Jede dieser Verengungen entscheidet eine
**Wortlautfrage**, die nach der Arbeitsregel dem Nutzer gehört. Es ist deshalb keine der
Verengungen gegen die andere durchgesetzt worden, sondern beide Hälften sind mit Fundstelle
ausgewiesen. **Es geht dadurch kein belegter Inhalt verloren** — er wird nur
nicht länger als quellenwörtlich ausgegeben.

## Legacy-Canvas-Items (deprecated, nicht mehr referenzierbar)

| ID | Abschnitt | Ersetzt durch | Reservierte, inhaltlich offene Lücke |
|---|---|---|---|
| ~~CAN-001~~ | Problem | CAN-013 … CAN-015, CAN-022 | CAN-016 … CAN-021 |
| ~~CAN-002~~ | Users / Customers | CAN-023 … CAN-027 | — |
| ~~CAN-003~~ | Value Promise | CAN-028 … CAN-038 | — |
| ~~CAN-004~~ | Current Alternatives | CAN-039 … CAN-046 | — |
| ~~CAN-005~~ | Key Capabilities | CAN-047 … CAN-070, CAN-138, CAN-139 (aus CAN-071), CAN-142, CAN-143 (aus CAN-140) | — (CAN-071 und CAN-140 deprecatet, siehe unten) |
| ~~CAN-006~~ | Non-Goals | CAN-072 … CAN-079 | — |
| ~~CAN-007~~ | Constraints | CAN-080 … CAN-099, CAN-141 | — |
| ~~CAN-008~~ | Risks | CAN-100 … CAN-110 | — |
| ~~CAN-009~~ | Success Signal | CAN-124 … CAN-130 | — |
| ~~CAN-010~~ | Evidence | CAN-111 … CAN-123 | — |
| ~~CAN-011~~ | Allowed Scope | CAN-131 … CAN-137 | — |
| ~~CAN-012~~ | Unresolved Questions | ersatzlos – Referenzen zeigen auf die OQ-IDs in `docs/decisions/open-questions.md` | — |

## Deprecatete atomare Canvas-Items (nicht mehr referenzierbar)

Anders als die Legacy-Sammelblöcke oben waren dies bereits atomar gemeinte Items. Sie haben
sich als Composites erwiesen und sind deshalb deprecatet worden.

| ID | Alte Aussage | Ersetzt durch | Grund | Deprecated am |
|---|---|---|---|---|
| ~~CAN-071~~ | MISSING – Verlauf, Detailansicht und GPX-Export | CAN-138 (A0), CAN-139 (A2), CAN-140 (A2) — **wirksam:** CAN-138, CAN-139, CAN-142, CAN-143 | Drei fachlich getrennte Capabilities auf zwei verschiedenen Release-Stufen in einer ID. Ein Item, das gleichzeitig zu Gate A0 und zu Gate A2 fällig wäre, ist nicht prüfbar. | 2026-07-19 |
| ~~CAN-140~~ | Nutzer können eine gespeicherte Strecke erneut verwenden und eine erneute Aktivität mit einer fachlich vergleichbaren früheren Aktivität vergleichen. | CAN-142 (Planung, A2), CAN-143 (Auswertung, A2) | Zwei Aussagen, die nach der Atomisierungsregel zu trennen sind: eine **Planungsfunktion** und eine **Auswertungsfunktion**. Sie sind unabhängig auslieferbar, haben unterschiedliche Nutzerwerte (Vorbereitung gegen Rückblick), brauchen unterschiedliche Acceptance Criteria und können unabhängig bestehen oder scheitern — die Wiederverwendung ist heute vollständig spezifizierbar, der Vergleich ist es ohne OQ-015 **nicht**. Ein gemeinsames Item kettet den lieferbaren Teil an eine offene Forschungsfrage. | 2026-07-20 |

Die IDs CAN-071 und CAN-140 werden **nicht wiederverwendet**. Jede neue Referenz auf CAN-071
oder CAN-140 in einem Projektdokument ist ein Validierungsfehler. Kanonische
Migrationstabellen: `docs/ID-REGISTRY.md` §7.4 (CAN-071) und §7.5 (CAN-140).

**Geprüft, nicht angenommen (Registry §6.3.3).** Vor der Vergabe von CAN-142 und CAN-143 wurde
geprüft, ob ein bestehendes atomares Item eine der beiden Hälften bereits trägt. **CAN-050**
(„Routenplanung und gespeicherte Routen") trägt REQ-006 auf Gate **A0**: eine Route *anlegen*
und *speichern*. Die erneute Verwendung einer bereits gespeicherten Route liegt auf Gate **A2**
und ist eine andere Handlung; CAN-050 dafür zu benutzen wäre die plausible Lesart mit falscher
Bedeutung. Auch REQ-006 nennt die Wiederverwendung mit keinem Wort. Für die Auswertungshälfte
trägt **kein** aktives Item die Aussage — sie stand ausschließlich als Teilklausel im Composite
REQ-008 und danach in CAN-140. **Nebenbefund:** CAN-050 ist selbst ein Composite und wird
zusätzlich als Anker für REQ-008 geführt, obwohl die Registry es REQ-006 zuordnet — Registry §8
Punkt 39 (BLOCKER). Dieser Canvas deutet CAN-050 **nicht** um.

## Atomare Canvas-Items

Ein Item bildet **genau eine** kontrollierbare Aussage ab. Requirements und
`docs/traceability.md` referenzieren ausschließlich diese IDs.

### Problem

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-013 | Bestehende Tracker liefern Daten ohne verständliche Bedeutung. | EXPLICIT | SRC-001 | CAN-001, Tabellenzelle CAN-001 + Prosa 'Problem' | Ersetzt Facette CAN-001-a aus docs/traceability.md. |
| CAN-014 | Soziale Interaktion findet ohne lokale Bindung statt. | EXPLICIT | SRC-001 | CAN-001, Tabellenzelle CAN-001 + Prosa 'Problem' | Ersetzt Facette CAN-001-b aus docs/traceability.md. |
| CAN-015 | Es gibt zu wenig Anlass für echte gemeinsame Aktivität. | EXPLICIT | SRC-001 | CAN-001, Tabellenzelle CAN-001 + Prosa 'Problem' | Ersetzt Facette CAN-001-c aus docs/traceability.md. |
| CAN-022 | Ohne Anbindung bereits genutzter Sportuhren und externer Sensoren fehlen oder verschlechtern sich zentrale Trainingssignale wie Herzfrequenz, Kadenz, Geschwindigkeit, Leistung und Höheninformationen. Dadurch werden Belastungsanalyse, sportartspezifische Auswertung und erklärbare Empfehlungen weniger vollständig und weniger zuverlässig. | ASSUMPTION | Nutzerentscheidung 2026-07-19 | CAN-001, **nicht im Ursprungstext dieses Canvas enthalten** | Item Type PROBLEM · Anker REQ-032 / AC-032 · Release Gate E. Inhalt am 2026-07-19 vom Nutzer entschieden, Status damit von `reserved` auf `active`. **Source Type ASSUMPTION**, bis der Wortlaut ausdrücklich nutzerbestätigt ist. **Ausdrücklich NICHT enthalten:** der Komfortaspekt „Nutzer müssen zusätzlich das Telefon mitführen" — laut Nutzerentscheidung eine separate mögliche Convenience-Aussage; sie wird in diesem Lauf **nicht** angelegt und erhält **keine** CAN-ID. Persona-Bezug: USER-004. |

### Zielnutzer

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-023 | Freizeit-Läufer:innen | EXPLICIT | SRC-001 | CAN-002, Prosa 'Users / Customers', Aufzählungspunkt 1 | Zuordnung PRD: USER-001. |
| CAN-024 | Radfahrer:innen (Rangstufe primär) | EXPLICIT | SRC-001 | CAN-002, Prosa 'Users / Customers', Aufzählungspunkt 1 | Zuordnung PRD: USER-002. Der Canvas-Punkt nennt Laufende und Radfahrende in einem Satz; das PRD führt sie als zwei Personas, daher zwei Atome. **VERENGT am 2026-07-20 (Runde 6); Source Type EXPLICIT bleibt.** Vorheriger Wortlaut: „Freizeit- und Rennradfahrer:innen". Grund: „Renn-" steht weder in der Herkunftszeile dieses Canvas (Ursprungstext Zeile 484: „- Freizeit-Läufer:innen und Radfahrer:innen.") noch in der Quelle `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md`:51 („**Primär:** Freizeit-Läufer:innen und Radfahrer:innen (20–45), 1–4 Aktivitäten/Woche …"). Das Wort steht in SRC-001 ausschließlich in Zeile 52 („**Sekundär:** Ambitionierte Rennradfahrer und Läufer mit festen Strecken und Leistungsfokus …") und in der Persona-Zeile 137 — dort untrennbar mit „Ambitionierte", „feste Strecken" und „Leistungsfokus" verbunden. Der frühere Wortlaut hatte alle drei Qualifikatoren abgeworfen und dabei die Rangunterscheidung **Primär/Sekundär** gelöscht, die die Quelle ausdrücklich setzt. Das Präfix „Freizeit-" ist orthographisch nur an „Läufer:innen" gebunden; es auf Radfahrende zu verteilen wäre eine Zwischenstufe — „Freizeit" kommt in SRC-002, SRC-003 und SRC-004 überhaupt nicht vor (Volltextsuche 2026-07-20 über `docs/sources/`). **Der Zusatz „(Rangstufe primär)" ist tragend, nicht dekorativ:** er ist wörtlich aus „**Primär:**" (SRC-001:51) entnommen; ohne ihn umfasst „Radfahrer:innen" begrifflich auch die ambitionierten Rennradfahrenden und überschneidet sich mit **CAN-025**, mit dem CAN-024 in `docs/traceability.md` bei REQ-032 gemeinsam steht. **Herkunftsangabe bleibt unverändert und ist geprüft korrekt:** die Spalte „Herkunft" bezeichnet die canvas-interne Provenienz (Ursprungstext „## Users / Customers", Zeilen 482–487), **nicht** eine Fundstelle in SRC-001; der Vorwurf, „Prosa 'Users / Customers'" komme in keiner Quelle vor, geht damit an der Spaltensemantik vorbei und wird **nicht** übernommen. **NICHT vorgenommen, Nutzerentscheidung:** ein Quellenwechsel auf `SRC-001/SRC-003` würde den Renn-Anteil wörtlich decken (`docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md`:65 „- **Radfahrer/Rennradfahrer:** längere Distanzen, feste Stammstrecken, Sensorik, Gruppenausfahrten" — eine Rad-Zielgruppe **ohne** Rangstufung) und wäre mit der PRD-Seite konsistent, die USER-002 bereits auf SRC-001/SRC-003 führt; er deckt „Freizeit-" weiterhin nicht und blendet die Rangstufung aus. **FOLGE, offengelegt statt geglättet:** `docs/traceability.md` führt CAN-024 bei REQ-032 als „primär (Bike-Sensorik)". Der Sensorikbedarf ist quellenseitig nur an der **sekundären** Persona (SRC-001:137 „feste Stammstrecken, Sensoren, Leistungsvergleich") und an der ungestuften Rad-Zielgruppe (SRC-003:65) verankert, nicht an der primären Gruppe. Nach dieser Verengung trägt CAN-024 diese Verankerung nicht mehr; der Nachzug liegt beim Traceability-Owner. **Asymmetrie-Hinweis:** CAN-023 behält „Freizeit-Läufer:innen" aus demselben Aufzählungspunkt — die beiden aus einem Punkt gespaltenen Atome decken damit unterschiedlich weite Populationen ab. CAN-023 wird in diesem Lauf **nicht** angefasst. **Decision-Record-Verknüpfung 2026-07-20 (Runde 6):** Die hier dokumentierte Klausel-scharfe Verengung ist als **DEC-014** in `docs/decisions/decision-log.md` protokolliert; die EXPLICIT-Aussage („Radfahrer:innen (Rangstufe primär)") verweist damit auf einen dauerhaften Entscheidungssatz. |
| CAN-025 | Ambitionierte Ausdauersportler:innen | EXPLICIT | SRC-001 | CAN-002, Prosa 'Users / Customers', Aufzählungspunkt 2 | **Teilweise gelöst am 2026-07-19.** Die ID-Frage ist geschlossen: die Registry führt **USER-004** „Ambitionierte Ausdauersportler:innen mit Wearables oder externen Sensoren", Source Type ASSUMPTION. **Offen bleibt der PRD-Nachzug** — das PRD führt weiterhin nur USER-001..003; USER-004 ist bis dahin eine zulässige Waise nach Registry-Regel 10. `docs/traceability.md` vermerkt bei REQ-009, REQ-011 und REQ-032 noch 'ambitionierte Persona MISSING im PRD'; REQ-032 wird primär an USER-004 verankert, die Verknüpfung von REQ-009 und REQ-011 ist **semantisch zu prüfen und ausdrücklich keine Universalverknüpfung**. Dieser Canvas ändert weder PRD noch Traceability. |
| CAN-026 | Lauf- und Radsportgruppen | EXPLICIT | SRC-001 | CAN-002, Prosa 'Users / Customers', Aufzählungspunkt 3 | Zuordnung PRD: USER-003. |
| CAN-027 | Vereine und lokale Communities | EXPLICIT | SRC-001 | CAN-002, Prosa 'Users / Customers', Aufzählungspunkt 4 | Zuordnung PRD: USER-003. OPEN QUESTION: Der Punkt fasst Vereine (Rechtsträger) und lokale Communities (informell) zusammen; ob das PRD zwei getrennte USER-IDs braucht, ist nicht entschieden. |

### Value Promise

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-028 | Verlässliches Tracking | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Prosa 'Value Promise' (Blockzitat) | Ersetzt Facette CAN-003-p1. Kernbefund der Atomisierung: Diese Klausel stand NUR im Prosa-Block, nicht in der CAN-003-Tabellenzeile. REQ-001..REQ-007 (sieben A0-REQs) konnten deshalb bisher nur auf Prosa zeigen. |
| CAN-029 | Verstehe deine Belastung (erklärbare Trainingsorientierung) | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Tabellenzelle CAN-003 + Prosa | Ersetzt Facette CAN-003-v1. |
| CAN-030 | Erkenne deinen Fortschritt | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Tabellenzelle CAN-003 | Ersetzt Facette CAN-003-v2. |
| CAN-031 | Trainiere sicherer | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Tabellenzelle CAN-003 | Ersetzt Facette CAN-003-v3. OPEN QUESTION (aus docs/traceability.md, REQ-030): Der Canvas lässt offen, ob 'sicherer' Trainingssicherheit oder Datensicherheit meint. Die Klausel ist bis zur Klärung nicht prüfbar. |
| CAN-032 | Finde reale lokale Gemeinschaft | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Tabellenzelle CAN-003 + Prosa | Ersetzt Facette CAN-003-v4. |
| CAN-033 | Spielmechaniken verdrängen die Health-Grundlage nicht | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Tabellenzelle CAN-003 | Ersetzt Facette CAN-003-v5. |
| CAN-034 | Verdiente Progression | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Prosa 'Value Promise' (Blockzitat) | Nur im Prosa-Block, nicht in der Tabellenzelle – gleiches Defektmuster wie CAN-028. |
| CAN-035 | Reihenfolge: Tracking und Health zuerst, Progression, Gemeinschaft und Territory danach | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Prosa 'Value Promise' (Blockzitat) | Nur im Prosa-Block. Inhaltlich deckungsgleich mit VIS-005 und den Stufen CAN-131..CAN-137. |
| CAN-036 | Fairness-Gate vor späteren Stufen | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Prosa 'Value Promise' (Blockzitat, 'klare Fairness-, Privacy- und Evidence-Gates') | Der Prosa-Satz nennt drei Gates in einer Aufzählung; sie werden von unterschiedlichen REQs getragen (Fairness: REQ-023/REQ-024) und sind daher getrennte Atome. |
| CAN-037 | Privacy-Gate vor späteren Stufen | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Prosa 'Value Promise' (Blockzitat) | Getragen von REQ-018 und REQ-034. |
| CAN-038 | Evidence-Gate vor späteren Stufen | ASSUMPTION | SRC-001/SRC-005 | CAN-003, Prosa 'Value Promise' (Blockzitat) | Getragen von REQ-035 und REQ-036. |

### Current Alternatives

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-039 | Strava | EXPLICIT | SRC-001/SRC-003 | CAN-004, Tabellenzelle CAN-004 + Prosa-Tabelle 'Current Alternatives' | Stärke: Tracking, Segmente, Netzwerk. Adressierte Lücke: lokale Team- und Territory-Mechanik sowie erklärbarer Health-Fokus. |
| CAN-040 | Garmin Connect | EXPLICIT | SRC-001/SRC-003 | CAN-004, Tabellenzelle CAN-004 + Prosa-Zeile 'Garmin/Apple/Google/Fitbit' | Stärke: Geräte- und Health-Ökosystem. Lücke: plattformübergreifende lokale Community und verdiente Progression. Die Prosa-Zeile fasst vier Anbieter zusammen; die CAN-004-Zelle nennt sie einzeln. |
| CAN-041 | Apple Fitness | EXPLICIT | SRC-001/SRC-003 | CAN-004, Tabellenzelle CAN-004 + Prosa-Zeile 'Garmin/Apple/Google/Fitbit' | Stärke und Lücke wie CAN-040 (gemeinsame Prosa-Zeile). |
| CAN-042 | Google/Fitbit | EXPLICIT | SRC-001/SRC-003 | CAN-004, Tabellenzelle CAN-004 + Prosa-Zeile 'Garmin/Apple/Google/Fitbit' | Stärke und Lücke wie CAN-040 (gemeinsame Prosa-Zeile). |
| CAN-043 | Whoop | EXPLICIT | SRC-001/SRC-003 | CAN-004, Tabellenzelle CAN-004 + Prosa-Tabelle | Stärke: Belastungs- und Recovery-Fokus. Lücke: Transparenz, Smartphone-Basis und lokale Community. |
| CAN-044 | Lauf- und Radsportvereine | EXPLICIT | SRC-001/SRC-003 | CAN-004, Tabellenzelle CAN-004 + Prosa-Zeile 'WhatsApp/Vereine' | Stärke: reale Gruppen. Lücke: strukturierte Aktivitäten, Fortschritt und sichere Auffindbarkeit. |
| CAN-045 | WhatsApp-Gruppen | EXPLICIT | SRC-001/SRC-003 | CAN-004, Tabellenzelle CAN-004 + Prosa-Zeile 'WhatsApp/Vereine' | Stärke und Lücke wie CAN-044 (gemeinsame Prosa-Zeile). |
| CAN-046 | Lokale Event-Plattformen | EXPLICIT | SRC-001/SRC-003 | CAN-004, nur Tabellenzelle CAN-004 | MISSING: Die Prosa-Tabelle 'Current Alternatives' enthält für diese Alternative KEINE Zeile; Stärke und adressierte Lücke sind nicht dokumentiert. |

### Key Capabilities

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-047 | Run und Bike als zwei getrennte, gleichwertige Sportmodi in einer App | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 ('Robustes Run/Bike-Tracking') + Prosa 1 | Trägt REQ-001 (Sportmodus als zentrale Konfiguration). |
| CAN-048 | Robustes Foreground-Tracking | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 + Prosa 1 | Trägt REQ-002. |
| CAN-049 | Background- und Recovery-Verhalten | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 1 ('mit robustem Background- und Recovery-Verhalten') | Trägt REQ-003. Eigenes Atom, weil separat prüfbar (EV-003) und mit eigenem Risiko (CAN-108 Store-Ablehnung). |
| CAN-050 | Routenplanung und gespeicherte Routen | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 ('geplante Routen') + Prosa 2 | Trägt REQ-006. |
| CAN-051 | Echte routebezogene Restdistanz | ASSUMPTION | SRC-001/SRC-003 (Kern) + SRC-005/DEC-004 (Qualifier) — **TEILBELEGT** | CAN-005, Prosa 2 ('echte routebezogene Restdistanz') | Trägt REQ-007. Eigenes Atom, weil **DEC-004 die einfache Distanzsubtraktion ausschließen soll**. **HERABGESTUFT am 2026-07-20 (Runde 6): EXPLICIT → ASSUMPTION.** **Gedeckt aus SRC-001/SRC-003** ist allein, dass bei einer geplanten Route eine verbleibende Distanz angezeigt wird und korrekt sein muss: `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md`:160 „\| T-02 \| Modus B: Route per Wegpunkte planen oder km-Ziel; geplante vs. verbleibende km \| Plan 1 \|" und `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md`:682 „**GATE A:** … · verbleibende km korrekt · …". **Nicht gedeckt ist der Qualifier „echte routebezogene"** und das Verbot der Distanzsubtraktion: Volltextsuche über alle vier Quellen (2026-07-20, `docs/sources/`) nach „routebezogen", „routenbezogen", „Projektion", „projiz", „monoton", „Korridor", „Hysterese" ergibt **null Treffer**. Die einzige Quelle, die den Rechenweg überhaupt festlegt, spezifiziert das **Gegenteil**: `docs/sources/SRC-004-tracking-and-planned-routes.md`:416–418 „`export function remainingDistanceMeters(plannedMeters: number, coveredMeters: number): number { return Math.max(0, plannedMeters - coveredMeters); }`". CAN-051 ist damit keine Ableitung aus den Quellen, sondern eine **bewusste Abweichung** von SRC-004. Ihr alleiniger Träger ist SRC-005/DEC-004, und **DEC-004 steht in `docs/decisions/decision-log.md` auf `proposed`, nicht `user-confirmed`** — die frühere Präsensformulierung „verbietet ausdrücklich" ist deshalb entschärft. **Source wird NICHT getauscht:** SRC-001/SRC-003 bleiben stehen, weil sie den Kern wörtlich tragen; ein Total-Tausch auf SRC-005/DEC-004 behandelte ein teilbelegtes Item wie ein unbelegtes und entzöge einem wörtlichen GATE-A-Kriterium seinen Canvas-Anker. **Der Vorwurf „Zirkelbeleg" wird nicht übernommen:** „CAN-005, Prosa 2" steht in der Spalte **Herkunft** (canvas-interne Provenienz, Ursprungstext Zeile 505), nicht in der Spalte **Source**; dasselbe Muster tragen sämtliche Geschwister CAN-047 … CAN-054. Die Herkunft bleibt deshalb unverändert. **NICHT vorgenommen:** eine Herabstufung auf `MISSING` — sie wäre nach der Sprachregelung des Artefaktsatzes eine **Hochstufung** der Strenge und ist von diesem Lauf ausgeschlossen; die Frage bleibt offen. Nachzuziehen bei ihren Ownern sind die Stellen, die CAN-051 als Autorität zitieren (Pass-Bedingung zu AC-007 in PRD und Traceability) sowie der Registry-Eintrag zu CAN-051. |
| CAN-052 | Erklärbarer Health-Score mit Fallback und Confidence | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 ('erklärbare Health-Auswertung') + Prosa 3 | Trägt REQ-009 bis REQ-013. |
| CAN-053 | Progression | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 + Prosa 4 | — |
| CAN-054 | Rückblicke | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 4 | Trägt REQ-016. |
| CAN-055 | Verdiente Avatar-Identität | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 4 | Trägt REQ-015. |
| CAN-056 | Accounts | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 + Prosa 5 | Trägt REQ-017. |
| CAN-057 | Privacy-Einstellungen und Sichtbarkeitssteuerung | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 5 | Trägt REQ-018. |
| CAN-058 | Routenempfehlungen | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 5 | Trägt REQ-019. |
| CAN-059 | Moderation | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 5 | Trägt REQ-018. |
| CAN-060 | Lokale Teams | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 + Prosa 6 | Trägt REQ-020 und REQ-021. |
| CAN-061 | Challenges | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 + Prosa 6 | Trägt REQ-025. |
| CAN-062 | Rankings | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 6 | Trägt REQ-023 und REQ-025. |
| CAN-063 | Anti-Cheat | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 6 | Trägt REQ-024. |
| CAN-064 | Team-Territory | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 ('Territory') + Prosa 7 | Trägt REQ-026. |
| CAN-065 | Einzel-Territory | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 7 | Trägt REQ-028. Achtung: laut CAN-079 im ersten Release ausgeschlossen. |
| CAN-066 | Seasons | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 7 | Trägt REQ-027. |
| CAN-067 | Lokale Events | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 7 | Trägt REQ-022. |
| CAN-068 | Live-Safety | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 + Prosa 8 | Trägt REQ-030 und REQ-031. |
| CAN-069 | Wearable-Anbindung | EXPLICIT | SRC-001/SRC-003 | CAN-005, Tabellenzelle CAN-005 + Prosa 8 | Trägt REQ-032. |
| CAN-070 | Erklärbare Coach-Funktionen | EXPLICIT | SRC-001/SRC-003 | CAN-005, Prosa 8 | Trägt REQ-033. |
| CAN-138 | Nutzer können lokal gespeicherte Run- und Bike-Aktivitäten in einem Verlauf anzeigen und eine ausgewählte Aktivität mit Route, Dauer, Distanz und sportartspezifischer Kernmetrik in einer Detailansicht öffnen. | ASSUMPTION | Nutzerentscheidung 2026-07-19, kanonischer Wortlaut 2026-07-20 | Nachfolger 1 von 3 des deprecateten CAN-071 | **Kanonischer Wortlaut seit Runde 4 (2026-07-20)**; der frühere Text („…eine Detailansicht mit **Strecke**, Dauer, Distanz … öffnen") trug dieselbe Aussage, deshalb **keine** neue ID. **CAN-138 BLEIBT EIN GEMEINSAMES ITEM — es wird ausdrücklich NICHT geteilt.** Begründung nach der Atomisierungsregel: (a) beide Funktionen gehören zum selben **A0-Nutzerfluss**; (b) die Detailansicht ist die **unmittelbare Vertiefung** des Verlaufs und nicht unabhängig auslieferbar; (c) beide werden gemeinsam durch **REQ-008** ausgeliefert; (d) **gleiches Gate** (A0); (e) **gleiches lokales Aktivitätsmodell**. Kein einziges Trennkriterium ist erfüllt — mehrere Verben in einem Satz trennen nicht. **Release-Stufe A0.** Trägt REQ-008 in seiner **verengten** Fassung; **GPX-Export und Streckenvergleich gehören NICHT dazu** (→ REQ-039 bzw. REQ-041/REQ-042). Acceptance Criteria prüfen **Run und Bike getrennt**: gespeicherte Aktivität erscheint nach Neustart im Verlauf · Detailansicht lädt den korrekten Track · Run zeigt Pace · Bike zeigt Geschwindigkeit · keine Aktivität geht nach regulärem Abschluss verloren · beschädigte oder unbekannte Aktivitätsdaten führen zu einem kontrollierten Zustand. **Source Type ASSUMPTION**, solange der Wortlaut nicht ausdrücklich nutzerbestätigt ist. |
| CAN-139 | Nutzer behalten Kontrolle über ihre aufgezeichneten Aktivitäten und können eine abgeschlossene Run- oder Bike-Aktivität als standardkonforme GPX-Datei exportieren, ohne sie veröffentlichen oder mit anderen Nutzern teilen zu müssen. | EXPLICIT | Nutzerentscheidung 2026-07-20 (kanonischer Wortlaut C) | Nachfolger 2 von 3 des deprecateten CAN-071 | **Kanonischer Wortlaut seit Runde 4 (2026-07-20); KEINE neue ID**, weil das vorhandene aktive Item im Kern dieselbe Capability trug (Registry §6.3.3 C). **Item Type VALUE PROMISE / CAPABILITY** · **Source Type EXPLICIT** (vorher ASSUMPTION) · `measurement_type` OPERATIONAL_QUALITY. **Primäres Requirement: REQ-039.** **REQ-034 bleibt AUSSCHLIESSLICH sekundärer Security-/Privacy-/Portabilitäts-Constraint** — das GPX-Canvas-Item darf **nicht allein über REQ-034 getragen** werden; die Erwähnung „Datenexport" trägt die konkrete Capability nicht. **Release-Stufe A2**, spätestens vor öffentlichem v1.0-Release. **BEFUND (Registry §8 Punkt 36, OPEN QUESTION):** der kanonische Text nennt „in einer kompatiblen Fremdanwendung öffnen" **nicht mehr**; AC-039 (d) und EV-039 verlangen den Nachweis weiterhin. Der Bezug ist über „**standardkonforme** GPX-Datei" tragbar — Interoperabilität ist die operative Probe auf Standardkonformität — aber er ist nicht mehr wörtlich belegt. Das wird offengelegt statt stillschweigend gedeckt: es wird weder die AC gestrichen noch der Wortlaut nachträglich ergänzt. **MISSING:** die Referenz-Fremdanwendung ist nicht benannt (OQ-016). Es wird keine App geraten. **BELEGPRÜFUNG gegen die Quelldokumente (2026-07-20): CAN-139 TRÄGT REQ-039.** GPX-Export steht in allen drei Quellen (SRC-001 T-06, SRC-003 Plan 2.8, SRC-002 §3); „Portabilität" steht **wörtlich** in SRC-003 §8 („Datenexport \| A/2.8 \| GPX-Export erfüllt Portabilität"). **Korrektur der OPEN-QUESTION-Prämisse (§8 Punkt 36):** die Fremd-App-Klausel ist **nicht generell unbelegt** — sie ist das **Akzeptanzkriterium der Quelle**: SRC-001 T-06 und SRC-003 Plan 2.8 nennen beide wörtlich „**Fremd-App öffnet Datei**". AC-039 (d) und EV-039 geben damit die Quelle wieder und stehen nicht ohne Grundlage da; unbelegt ist die Klausel **allein im kanonischen CAN-139-Wortlaut**. Die Wortlautfrage bleibt beim Nutzer — es wird weder die AC gestrichen noch der Text ergänzt. **UNBELEGT:** „standardkonform" (keine Quelle nennt eine Formatversion 1.0/1.1). **TEILBELEGT:** „ohne veröffentlichen oder teilen zu müssen" — SRC-001 §2 beschreibt v1.0 als „alles lokal, **ohne Account**", SRC-003 2.8 nennt das **Share Sheet**; die Quellen **beschreiben eine Architektur**, in der die Klausel gilt, **fordern sie aber nirgends als Bedingung**. Aus „es gibt keinen Feed" folgt nicht „der Export darf nie einen voraussetzen". Einzelnachweis im PRD bei REQ-039. |
| CAN-142 | Nutzer können eine gespeicherte Route erneut als Grundlage einer geplanten Run- oder Bike-Aktivität verwenden. | ASSUMPTION | Nutzerentscheidung 2026-07-20 | Nachfolger 1 von 2 des deprecateten CAN-140 (Planungsfunktion) | **Release-Stufe A2.** Trägt **REQ-041**; AC-042, EV-043, TRC-041. **Vollständig spezifizierbar ohne OQ-015** — genau deshalb von CAN-143 getrennt. Acceptance Criteria prüfen **Run und Bike getrennt**: gespeicherte Route für Run wiederverwendbar · gespeicherte Route für Bike wiederverwendbar · geladene Geometrie und Wegpunkte stimmen mit der gespeicherten überein · sportartspezifisches Routingprofil bleibt beim Laden korrekt · gelöschte oder beschädigte Route führt zu einem kontrollierten Fehler. **Abgrenzung zu CAN-050:** CAN-050 ist das *Anlegen und Speichern* einer Route (A0, REQ-006), CAN-142 ist deren *erneute Verwendung* (A2). **Source Type ASSUMPTION** — der Wortlaut stammt aus der Nutzerentscheidung, ist aber in keiner Nutzerquelle als Anforderungstext belegt. **BLOCKER:** REQ-041 hat keinen Vision-Anker; VIS-014 ist reserviert und inhaltlich MISSING, TRC-041 bleibt `broken` (Registry §8 Punkt 38). |
| CAN-143 | Nutzer können fachlich vergleichbare Aktivitäten auf derselben oder hinreichend ähnlichen Strecke anhand sportartspezifischer Kennzahlen miteinander vergleichen. | ASSUMPTION | Nutzerentscheidung 2026-07-20 | Nachfolger 2 von 2 des deprecateten CAN-140 (Auswertungsfunktion) | **Release-Stufe A2.** Trägt **REQ-042**; AC-043, EV-044, TRC-042. **Run und Bike strikt getrennt**; keine irreführende Bestzeit bei nicht vergleichbarer Geometrie. **Benötigt zusätzliche Regeln zur Streckenähnlichkeit.** Die Vergleichslogik bleibt **RESEARCH_HYPOTHESIS bzw. MISSING**, solange **OQ-015** offen ist: wann zwei Strecken als vergleichbar gelten · tolerierte Abweichung · welche Kennzahlen verglichen werden · Behandlung verkürzter, verlängerter und abgebrochener Aktivitäten. Es wird keine Toleranz geraten. **Source Type ASSUMPTION.** **Hinweis zum Vision-Bezug:** TRC-042 führt VIS-003 als Anker — das ist eine **ungeprüfte ASSUMPTION** des Traceability-Owners und wird von diesem Canvas **nicht** bestätigt und **nicht** hochgestuft. Er ist nach dem Muster von Registry §6.1.1 zu prüfen, nicht zu übernehmen, weil er existiert. |

**Verbindliche Stufung der CAN-071- und CAN-140-Nachfolger.** A0: Aktivitätsverlauf,
Aktivitätsdetail, lokale Persistenz, Recovery, Run-/Bike-korrekte Darstellung (CAN-138).
A2: öffentlicher GPX-Export und Datenportabilität vor öffentlichem v1.0-Release (CAN-139),
gespeicherte Route erneut als Planungsgrundlage verwenden (CAN-142), fachlich valider
Streckenvergleich (CAN-143). **CAN-142 und CAN-143 liegen auf demselben Gate, sind aber
unterschiedlich blockiert:** CAN-142 ist heute spezifizierbar, CAN-143 nicht, solange OQ-015
offen ist. Genau diese Asymmetrie war der Grund, CAN-140 zu teilen — ein gemeinsames Item hätte
den lieferbaren Teil an die offene Forschungsfrage gekettet.

### Non-Goals

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-072 | Kein Medizinprodukt und keine medizinische Diagnose | EXPLICIT | SRC-001 | CAN-006, Tabellenzelle CAN-006 + Prosa 'Non-Goals' | — |
| CAN-073 | Keine garantierte Unfallhilfe | EXPLICIT | SRC-001 | CAN-006, Prosa 'Non-Goals' | Nur in der Prosa, nicht in der CAN-006-Zelle. Berührt REQ-031 unmittelbar. |
| CAN-074 | Kein Chat-Messenger und kein allgemeiner Messenger | EXPLICIT | SRC-001 | CAN-006, Tabellenzelle CAN-006 + Prosa | — |
| CAN-075 | Kein Verkauf von Leistungsstatus, Leistungs-Boosts oder Spielvorteilen | EXPLICIT | SRC-001 | CAN-006, Tabellenzelle CAN-006 + Prosa | — |
| CAN-076 | Keine Indoor-, Gym- oder Workout-Plattform | EXPLICIT | SRC-001 | CAN-006, Tabellenzelle CAN-006 + Prosa | — |
| CAN-077 | Kein vollwertiger Web-Client | EXPLICIT | SRC-001 | CAN-006, nur Tabellenzelle CAN-006 | Nur in der Zelle, nicht in der Prosa-Liste. |
| CAN-078 | Kein sichtbares H3- oder Raster-Gameplay | EXPLICIT | SRC-001 | CAN-006, nur Prosa 'Non-Goals' | Nur in der Prosa, nicht in der CAN-006-Zelle. |
| CAN-079 | Kein Territory-System im ersten Release / Tracker-MVP | EXPLICIT | SRC-001 | CAN-006, Tabellenzelle CAN-006 + Prosa | — |

### Constraints

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-080 | Eine gemeinsame iOS-/Android-Codebasis | EXPLICIT | SRC-001/SRC-003 | CAN-007, Tabellenzelle CAN-007 | — |
| CAN-081 | Expo/React Native/TypeScript als App-Basis; native Dev-Builds für Background-, Health- und Widget-Funktionen | EXPLICIT | SRC-001/SRC-003 | CAN-007, Prosa 'Constraints', Punkt 1 | — |
| CAN-082 | Deutsche Launch-Sprache mit i18n-Vorbereitung | EXPLICIT | SRC-001/SRC-003 | CAN-007, Tabellenzelle CAN-007 | — |
| CAN-083 | Store-Policies sind verbindlich | EXPLICIT | SRC-001/SRC-003 | CAN-007, Tabellenzelle CAN-007 | — |
| CAN-084 | DSGVO ist verbindlich | EXPLICIT | SRC-001/SRC-003 | CAN-007, Tabellenzelle CAN-007 | — |
| CAN-085 | Background-Location erfordert eine belastbare Berechtigungsbegründung | EXPLICIT | SRC-001/SRC-003 | CAN-007, Tabellenzelle CAN-007 | — |
| CAN-086 | Health-Berechtigungen erfordern eine belastbare Berechtigungsbegründung | EXPLICIT | SRC-001/SRC-003 | CAN-007, Tabellenzelle CAN-007 | — |
| CAN-087 | Reale Gerätetests auf iOS und Android pro Gate | EXPLICIT | SRC-001/SRC-003 | CAN-007, Tabellenzelle CAN-007 + Prosa Punkt 2 | — |
| CAN-088 | Zweckbindung und Datenminimierung für Standort- und Health-Daten | EXPLICIT | SRC-001/SRC-003 | CAN-007, Prosa 'Constraints', Punkt 3 | — |
| CAN-089 | Karten-, Routing- und Backendanbieter bleiben ADR-Entscheidungen | EXPLICIT | SRC-001/SRC-003 | CAN-007, Prosa 'Constraints', Punkt 4 | — |
| CAN-090 | Der öffentliche Name darf erst nach Markenprüfung finalisiert werden | EXPLICIT | SRC-001/SRC-003 | CAN-007, Prosa 'Constraints', Punkt 5 | — |
| CAN-091 | Externes Routing läuft ab Stufe A0 ausschließlich über einen minimalen serverseitigen Routing-Proxy | CONFIRMED | Nutzerentscheidung 2026-07-19 | CAN-007, Prosa 'Constraints', bestätigte Nutzerentscheidung 2026-07-19 | Quelle: DEC-005 (user-confirmed), CONTRA-002 (resolved). |
| CAN-092 | Kein Routing-API-Key als EXPO_PUBLIC_*-Variable im App-Bundle; NFR-007 gilt ab A0 | CONFIRMED | Nutzerentscheidung 2026-07-19 | CAN-007, Prosa 'Constraints', bestätigte Nutzerentscheidung 2026-07-19 | EXPO_PUBLIC_* wird ins JS-Bundle inlined und ist aus jedem Build extrahierbar. |
| CAN-093 | Die Mobile-App kennt nur eine konfigurierbare Proxy-Basis-URL, einen providerneutralen RoutingPort und einen RoutingClient; Providername und Providerantwort dürfen nicht in Domain- oder UI-Code gelangen | CONFIRMED | Nutzerentscheidung 2026-07-19 | CAN-007, Nutzerentscheidung 2026-07-19 | Neu aufgenommen aus der Nutzerentscheidung vom 2026-07-19. |
| CAN-094 | Der Routing-Proxy übersetzt den Sportmodus in das Providerprofil: run → foot-walking, ride → cycling-regular | CONFIRMED | Nutzerentscheidung 2026-07-19 | CAN-007, Nutzerentscheidung 2026-07-19 | Die Profilnamen bleiben damit serverseitig und tauchen nicht in SportConfig-nahem App-Code als Providerbegriff auf. Hinweis: docs/architecture/revyr-target-architecture.md, Abschnitt 6, führt 'routingProfile' derzeit noch in der App-seitigen SportConfig – Klärung durch den Architektur-Owner in Phase 3. |
| CAN-095 | Local-first-Präzisierung: Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal; für die Routenberechnung dürfen ausschließlich die erforderlichen Wegpunkte transient an einen kontrollierten Routing-Proxy übertragen werden; der Proxy speichert keine Koordinaten oder Routengeometrien dauerhaft | CONFIRMED | Nutzerentscheidung 2026-07-19 | CAN-007, Nutzerentscheidung 2026-07-19 | Wörtliche Nutzerformulierung. Adressiert CONTRA-006 (offen), schließt ihn aber nicht – CONTRA-006 fragt zusätzlich, welche REQ-034-Klauseln (Rate Limits, Logging, Retention, Auftragsverarbeitung, EU-Hosting) ab A0 für den Proxy gelten. |
| CAN-096 | A0-Laufzeit des Routing-Proxys: AWS Lambda und API Gateway, Region eu-central-1, Provider-Key nur serverseitig, Rate Limit, Timeout und Kill Switch | CONFIRMED | Nutzerentscheidung 2026-07-19 | CAN-007, Nutzerentscheidung 2026-07-19 | NUR DOKUMENTIERT. In diesem Lauf wird nichts davon gebaut, deployt oder als AWS-Ressource angelegt. |
| CAN-097 | Ablageort des A0-Routing-Proxys im Repository: infra/routing-proxy/ – ausdrücklich nicht backend/ | CONFIRMED | Nutzerentscheidung 2026-07-19 | CAN-007, Nutzerentscheidung 2026-07-19 (OQ-011) | Begründung des Nutzers: begrenzte, austauschbare Infrastrukturkomponente; backend/ bleibt für Stufe B reserviert. |
| CAN-098 | Der vollständige Backend-Entscheid für Geo, Auth, Realtime und EU-Hosting bleibt offen | EXPLICIT | SRC-001/SRC-003 | CAN-007, Prosa 'Constraints', letzter Punkt | Verweist auf OQ-005. Der A0-Proxy präjudiziert diesen Entscheid nicht. |
| CAN-099 | Die mobile Anwendung muss für Menschen mit unterschiedlichen visuellen, motorischen und assistiven Anforderungen bedienbar sein. Dazu gehören WCAG 2.2 AA, Screenreader-Unterstützung, skalierbare Schrift, ausreichende Bedienflächen, nachvollziehbare Fokusführung und die Regel, dass Farbe niemals der einzige Informationsträger ist. | EXPLICIT (belegter Kern) / ASSUMPTION (benannte Details) | Nutzerentscheidung 2026-07-20 (kanonischer Wortlaut A) | CAN-007, **nicht im Ursprungstext dieses Canvas enthalten** | **Kanonischer Wortlaut seit Runde 4 (2026-07-20); KEINE neue ID**, weil das vorhandene aktive Item dieselbe Pflicht trug (Registry §6.3.3 A). **CAN-099 ist AUSSCHLIESSLICH Accessibility** — der Designsystem-Anteil liegt bei CAN-141. **Item Type CONSTRAINT / VALUE BOUNDARY** · **Source Type EXPLICIT** (vorher MISSING) · `measurement_type` COMPLIANCE_CONTROL. **Primäres Requirement: REQ-037.** **Acceptance Criteria und Evidence prüfen AUSSCHLIESSLICH Accessibility** (AC-037, EV-037) — kein Gestaltungs-, Ästhetik- oder Farbsemantikkriterium. **Pass Condition:** WCAG-2.2-AA-Audit bestanden; relevante Screens mit **VoiceOver UND TalkBack** geprüft; Dynamic Type bzw. Font Scaling geprüft; ausreichende Bedienflächen; nachvollziehbare Fokusführung; keine Information ausschließlich durch Farbe; dokumentierte Kontrastprüfung. **Release-Gates:** Accessibility-Basis ab **A0**, vollständiger Audit spätestens **A2** vor öffentlichem Store-Release. **Farbregel (Runde-4-Entscheidung):** „Farbe ist niemals der einzige Informationsträger" wird **kanonisch hier** geführt und ist aus CAN-141 entfernt. Präzisierung gegenüber NFR-005: „WCAG AA" ohne Fassung ist nicht prüfbar; die Fassung ist **2.2**. **BLOCKER (Registry §8 Punkt 43):** der Source Type steht auf EXPLICIT, weil der Nutzer den Wortlaut am 2026-07-20 als verbindlich gesetzt hat — eine ausdrückliche Gegenbestätigung liegt nicht vor. **BELEGPRÜFUNG gegen die Quelldokumente (2026-07-20): CAN-099 TRÄGT REQ-037.** Belegt sind WCAG AA (SRC-001 §3.5, SRC-003 §2.4, SRC-002 §10), Screenreader inkl. der Namen VoiceOver/TalkBack (SRC-003 §2.4), Dynamic Type/Font Scaling (SRC-001 §3.5, SRC-003 §2.4) und „Farben nie einziger Informationsträger" (SRC-001 §3.5 — generisch; SRC-003 §2.4 sagt enger „**Teamfarben**"). **UNBELEGT und offengelegt statt geglättet:** die Fassungsziffer **2.2** (alle vier WCAG-Fundstellen sagen „WCAG AA" **ohne** Fassung: `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md`:176 und :256, `docs/sources/SRC-002-REVYR-Plan-PRD.md`:134, `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md`:100) · **„motorische Anforderungen", „assistive Anforderungen", „ausreichende Bedienflächen", „nachvollziehbare Fokusführung"** (Volltextsuche über `docs/sources/` am 2026-07-20: **null** Treffer für „motorisch", „assistiv", „Bedienfläche", „Fokusführung", „barrierefrei" — Standardvokabular der Praxis, das als Quellenaussage durchginge). **Diese Details bleiben ASSUMPTION** (Nutzerauftrag 2026-07-20); der Wortlaut wird **nicht** nachträglich gekürzt, und der Source Type wird deshalb ab Runde 6 **gespalten** geführt: EXPLICIT für den belegten Kern, ASSUMPTION für die hier namentlich benannten Details. **WEB-ERSTRECKUNG AM 2026-07-20 (Runde 6) AUS DEM WORTLAUT ENTFERNT** (Nutzerauftrag). Vorher: „Die mobile Anwendung **und ihre nutzbaren Web-Auskopplungen** müssen …". Grund ist ein reiner **Belegmangel**: der einzige Accessibility-Abschnitt aller vier Quellen (`docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md`:98–102 „## 2.4 Accessibility & Plattformkonventionen") nennt Web nicht und schließt mit einer reinen iOS-/Android-Zeile; die vier „Web-Auskopplung"-Fundstellen (SRC-003:83, :484, :711, :735) betreffen ausnahmslos die **CSS-Farbmisch-Regel**. Die Kette „Farbregel gilt für Web → Accessibility auch" wird **nicht** gebaut. **Ausdrücklich NICHT die Begründung:** die Quellen verneinen die Existenz von Web-Artefakten nicht — `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md`:132 nimmt den Beschützer-Link vom Nicht-Ziel aus („kein Web-Client **(außer Beschützer-Link)**"), und SRC-003:83 benennt drei Web-Auskopplungen namentlich. **Nicht belegt ist nicht dasselbe wie von der Quelle verneint.** **KORREKTUR EINER FALSCHAUSSAGE DIESES ITEMS (2026-07-20):** der frühere Satz „Diese vier stehen **nicht** in AC-037 und werden nicht geprüft" ist unzutreffend und wird zurückgenommen. Er widersprach der Pass-Condition-Liste in derselben Zelle (Bedienflächen und Fokusführung stehen dort), und die Fassungsziffer 2.2 steht in AC-037 als Pass-Bedingung sowie in EV-037 als store-release-blockierender Nachweis. Die Überdehnung ist also **nicht folgenlos**. **NACHZUG BEI FREMDEN OWNERN, ausdrücklich offen:** die Web-Erstreckung steht weiterhin in REQ-037, in der Given-Spalte von AC-037, im `signal`-Feld von NFR-005 und im EV-037-Kopf. Dieser Canvas ändert diese Dateien **nicht**. Solange der Nachzug aussteht, trägt AC-037 eine Vorbedingung **ohne** Canvas-Anker; das ist ein bekannter, hier offengelegter Zwischenzustand und kein stillschweigender Schnitt. Einzelnachweis im PRD bei REQ-037. **Decision-Record-Verknüpfung 2026-07-20 (Runde 6):** Die klausel-scharfe Trennung (EXPLICIT für den belegten Kern; ASSUMPTION für Bedienflächen, Fokusführung, motorische/assistive Anforderungen; Entfernung der Web-Erstreckung) ist als **DEC-014** in `docs/decisions/decision-log.md` protokolliert. |
| CAN-141 | Die Anwendung verwendet ein tokenbasiertes, überwiegend monochromes Designsystem. Farbe wird nur eingesetzt, wenn sie eine definierte fachliche Bedeutung besitzt: Health-Status, Team- und Revieridentität, Sportplatz-Gold sowie bestätigte Feiermomente. Run und Bike werden nicht ausschließlich durch Farbe unterschieden. | EXPLICIT | Nutzerentscheidung 2026-07-20 (kanonischer Wortlaut B) | Neu vergeben im Auftau-Schritt 2; **nicht im Ursprungstext dieses Canvas enthalten** | **Kanonischer Wortlaut seit Runde 4 (2026-07-20); KEINE neue ID** (Registry §6.3.3 B). **Item Type DESIGN CONSTRAINT / PRODUCT PRINCIPLE** · **Source Type EXPLICIT**. **Primäres Requirement: REQ-038.** Schließt die zweite Canvas-Lücke des deprecateten REQ-014 (die erste ist CAN-099). **Darf NICHT mit Accessibility kombiniert werden.** **Farbregel-Bereinigung (Runde 4):** die generische Klausel „Farbe ist nie der einzige Informationsträger" ist aus CAN-141 **entfernt** und wird ausschließlich von CAN-099 getragen. Der frühere Vermerk, sie wirke „in CAN-099 als Accessibility-Schranke und in CAN-141 als Gestaltungsregel — dieselbe Beobachtung, zwei getrennt prüfbare Pflichten", war die belegte **doppelt geführte Pflicht** und ist aufgehoben. Begründung der Zuordnung: die Klausel schützt die **Wahrnehmbarkeit** von Information; ihr Ausfall trifft Menschen mit Farbfehlsichtigkeit und ist ein **Zugänglichkeitsdefekt**, kein Gestaltungsdefekt — ein monochromes Produkt kann sie verletzen (zwei Grautöne als einziger Unterschied), ein farbiges kann sie erfüllen. Die beiden Aussagen sind **unabhängig**, nicht dieselbe Beobachtung aus zwei Blickwinkeln. In CAN-141 verbleibt ausschließlich die engere Regel „Run und Bike werden nicht ausschließlich durch Farbe unterschieden" — ein konkretes Unterscheidungspaar, prüfbar gegen die Design-Tokens. **Es entsteht keine dritte Farbregel.** Zulässige Farbbedeutungen abschließend: Health-Status · Team- und Revieridentität · Sportplatz-Gold · bestätigte Feiermomente. **BLOCKER (Registry §8 Punkt 43):** Source Type EXPLICIT ohne ausdrückliche Gegenbestätigung. **BELEGPRÜFUNG gegen die Quelldokumente (2026-07-20): CAN-141 TRÄGT REQ-038 — von den drei Ankern dieser Runde am deutlichsten.** SRC-003 §2 sagt wörtlich „**Designprinzip: ‚Farbe muss man sich verdienen.'** Die App ist **konsequent monochrom** — Farbe existiert nur, wo sie Bedeutung trägt"; SRC-001 M-04 nennt das „Schwarz-Weiß-Design-System („Farbe muss man sich verdienen")" mit dem Akzeptanzkriterium „**Design-Tokens**; beide Modi; WCAG AA"; SRC-003 §2.1 überschreibt die Farbliste mit „**Bedeutungsfarben (einzige Ausnahmen)**" — das trägt auch die Abschließlichkeit. Der `source_type EXPLICIT` ist damit **zusätzlich quellenseitig** gedeckt, nicht nur durch die Nutzerentscheidung; das ist ein zweiter unabhängiger Beleg, **keine Hochstufung**. **ZWEI ABWEICHUNGEN, offengelegt statt geglättet:** (1) **Fünf zu vier** — SRC-001 M-04 und SRC-003 §2.1 führen **fünf** Bedeutungen (Team · **Einzel-Revier** · Sportplatz-Gold · Health-Ampel · Feier); CAN-141 zieht Team und Einzel-Revier zu „Team- und Revieridentität" zusammen. Inhaltsgleich, aber AC-038 nennt die **Vierer**-Liste abschließend, während beide Quellen fünf Einträge führen. (2) **Abschwächung** — SRC-003 §2.1 sagt zum Run-/Bike-Modus: „bleibt monochrom; unterscheidet sich durch Ikonografie + Typo-Akzent, **nicht durch Farbe**". Die Quelle verbietet die Farbunterscheidung **ganz**, CAN-141 nur die **ausschließliche**. Die Klausel ist damit **schwächer als ihre Quelle** — sie wird hier weder verschärft noch die Abweichung verschwiegen. Beides sind Wortlautfragen und gehören dem Nutzer. Einzelnachweis im PRD bei REQ-038. **PRÄZISIERUNG (Runde 6, 2026-07-20) — Aussage, Item Type und Source Type bleiben unverändert.** (a) **Die zu CAN-099 verschobene Farbregel steht dort auf einer einzigen Fundstelle.** Nur `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md`:256 formuliert sie generisch („Farben nie einziger Informationsträger"); `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md`:101 sagt enger „**Teamfarben** nie einziger Informationsträger (immer + Logo/Name auf dem Areal)". Die Regel ist damit **einfach**, nicht doppelt gestützt. Das ändert nichts an der Runde-4-Zuordnung und ist **keine** Rücknahme der Entdopplung — es wird nur nicht länger der Eindruck erzeugt, beide Quellen trügen dieselbe Reichweite. (b) **Abgrenzung zur Web-Streichung bei CAN-099:** die Entfernung der Accessibility-Erstreckung auf Web-Auskopplungen berührt die **CSS-Farbmisch-Regel** aus SRC-003:83/:484/:711/:735 nicht — sie ist quellenseitig ausdrücklich auf „alle Web-Auskopplungen (Erfolgskarten-Renderer, Beschützer-Web-Link, Marketing-Seiten)" erstreckt und gehört zur Gestaltungssprache, nicht zur Zugänglichkeit. **Abwesenheitsbefund:** diese Regel ist derzeit in **keinem** Canvas-Item als Aussage geführt, auch nicht in CAN-141. Das wird hier als Lücke berichtet; es wird **kein** Item darum erweitert und **keine** ID vergeben. |

**Warum REQ-014 nicht umgedeutet wurde.** Die bisherige Composite-Requirement
„Designsystem/Accessibility" ist in der Registry **deprecatet** und durch zwei atomare
Requirements ersetzt (Accessibility → REQ-037, monochromes Designsystem → REQ-038), je mit
eigenen Acceptance Criteria und Evidence-Einträgen. Eine stillschweigende Umdeutung von
REQ-014 auf nur noch einen der beiden Inhalte hätte den Nachweis des jeweils anderen
unsichtbar gemacht. Migrationstabelle: `docs/ID-REGISTRY.md` §7.4.

### Risks

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-100 | GPS-Drift verfälscht Distanz und Route | EXPLICIT | SRC-003 | CAN-008, Tabellenzelle CAN-008 + Prosa 'Risks' | Register: RISK-002. |
| CAN-101 | Batterieverbrauch verhindert längere Nutzung | EXPLICIT | SRC-003 | CAN-008, Tabellenzelle CAN-008 + Prosa | Register: RISK-003. |
| CAN-102 | Falsche Health-Claims | EXPLICIT | SRC-003 | CAN-008, Tabellenzelle CAN-008 + Prosa | Register: RISK-008. |
| CAN-103 | Namens- und Markenkollision | EXPLICIT | SRC-003 | CAN-008, Tabellenzelle CAN-008 + Prosa | Register: RISK-011. |
| CAN-104 | Betrug und Manipulation von Aktivitäten | EXPLICIT | SRC-003 | CAN-008, Tabellenzelle CAN-008 | Register: RISK-013 (Gegenmaßnahme Anti-Cheat). |
| CAN-105 | Standortmissbrauch | EXPLICIT | SRC-003 | CAN-008, Tabellenzelle CAN-008 + Prosa | Register: RISK-015 und RISK-016. |
| CAN-106 | Geo-Komplexität | EXPLICIT | SRC-003 | CAN-008, Tabellenzelle CAN-008 + Prosa | Register: RISK-017. |
| CAN-107 | OSM-Qualität | EXPLICIT | SRC-003 | CAN-008, Tabellenzelle CAN-008 | Register: RISK-018. |
| CAN-108 | Store-Ablehnung | EXPLICIT | SRC-003 | CAN-008, Tabellenzelle CAN-008 + Prosa | Register: RISK-010. |
| CAN-109 | Anti-Cheat-Fehler (False Positives gegen reale Nutzer) | ASSUMPTION | SRC-003 (indirekt) | CAN-008, nur Prosa 'Risks' | Register: RISK-013. Eigenes Atom, weil es die Gegenrichtung zu CAN-104 ist: CAN-104 ist Betrug, CAN-109 ist die Fehlbeschuldigung. **Klausel-scharfe Korrektur 2026-07-20 (Runde 6, Nutzeranweisung):** Source Type **EXPLICIT → ASSUMPTION** herabgestuft, weil dies ein **abgeleitetes Risiko** ist. SRC-003 kennt die tragende Schutzregel „Fehlende Sensoren allein sind kein Betrug, senken aber die Beweiskraft" (SRC-003:265, Task 10.2 SRC-003:559) — daraus **folgt implizit**, dass Anti-Cheat-Verfahren zu Fehlbeschuldigungen führen können, aber **die eigene Risikozeile** „Fehlbeschuldigung realer Nutzer" **steht nicht im Risikoregister von SRC-003** und nicht in SRC-001/SRC-002/SRC-004. Die Ableitung ist plausibel und produktrelevant — sie ist keine Quellenaussage. Das RISK-013-Register führt die Risikoart, das Wort „False Positive" oder „Fehlbeschuldigung" steht dort nicht. **Behandlung:** ASSUMPTION, bis der Nutzer die Aussage entweder als Produktentscheidung bestätigt (dann CONFIRMED) oder als Ableitung des Traceability-Owners verwirft. **NACHTRAG Runde 6 (2026-07-20, Quellennachzug gegen `docs/sources/`) — die Herabstufung wird bestätigt, ihre Begründung aber verschärft.** (a) Es handelt sich **nicht** um ein „implizites Folgen", sondern um eine nach dem Beweismaßstab unzulässige **Zwischenstufe**: `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md`:265 und :559 stellen eine **Urteilsregel** auf („Fehlende Sensoren allein sind kein Betrug, senken aber die Beweiskraft" / „fehlende Sensoren allein ≠ Betrug") — eine Regel, **wie** geurteilt werden darf, nicht ein Risiko, **dass** falsch geurteilt wird. Verschärfend: SRC-003:265 nennt als Rechtsfolge fehlender Sensoren ausdrücklich die **gesenkte Beweiskraft** und gerade **nicht** `verified=false`; die Stelle schließt den von CAN-109 beschriebenen Fall an dieser Stelle also aus, statt ihn zu behaupten. (b) **Abwesenheitsbefund, Volltextsuche 2026-07-20 über alle vier Quellen:** „False Positiv", „fälschlich", „zu Unrecht", „beschuldig", „Einspruch", „Appeal" — **null** Treffer. Das Risikoregister von SRC-003 („# 10. Technische Risiken", :690, Tabellenzeilen :694–717) enthält **keine** Zeile zur Anti-Cheat-Fehlklassifikation: Nr. 8 (:701) ist die **Gegenrichtung** (= CAN-104), Nr. 12 (:705) betrifft Fehlalarme der **Sturzerkennung**, Nr. 19 (:712) Schummeln, Nr. 22 (:715) den Datenschutz der Sensor-Plausibilität. (c) **Korrektur der obenstehenden Aussage über RISK-013:** das Wort „False Positives" steht dort sehr wohl — `docs/risks/revyr-risk-register.md` führt RISK-013 wörtlich als „Anti-Cheat produziert False Positives … mehrstufige Confidence, Review, Testdaten und Appeal-Flow". Unbelegt ist es allein **in den vier Quellen**; RISK-013 gehört zum Artefaktsatz und kann CAN-109 nicht stützen (Zirkelbeleg). Auch „Confidence", „Appeal" und „Review" im Anti-Cheat-Sinn kommen in keiner Quelle vor. (d) **Die Herkunftsangabe „nur Prosa 'Risks'" ist geprüft KORREKT und bleibt:** der Ursprungstext dieses Canvas nennt unter „## Risks" (Zeile 573) wörtlich „Anti-Cheat-Fehler". Der Einwand, dieser Abschnitt sei prosafrei, trifft nur auf die **atomare** Items-Tabelle „### Risks" zu, nicht auf den Ursprungstext. Dasselbe gilt für das Nachbaritem **CAN-110** („private Sportanlagen" steht ebenfalls in Zeile 573) — dort besteht kein Handlungsbedarf. (e) **Ausdrücklich unberührt:** AC-024 gibt die Urteilsregel aus SRC-003:265/:559 wieder und ist quellengedeckt; die Herabstufung von CAN-109 trifft **nur** die darauf aufgesetzte quantitative Falsch-Positiv-Messung, nicht das Akzeptanzkriterium. Diese Abgrenzung ist beim PRD-/Traceability-Nachzug einzuhalten. **Decision-Record-Verknüpfung 2026-07-20 (Runde 6):** Die Herabstufung EXPLICIT → ASSUMPTION ist als **DEC-014** in `docs/decisions/decision-log.md` protokolliert. |
| CAN-110 | Private oder gesperrte Sportanlagen | EXPLICIT | SRC-003 | CAN-008, nur Prosa 'Risks' | Register: RISK-018. |

### Evidence-Annahmen

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-111 | Unit- und Property-Tests der Domainlogik | EXPLICIT | SRC-003 | CAN-010, Tabellenzelle CAN-010 + Prosa 'Evidence' | — |
| CAN-112 | Integrationstests | EXPLICIT | SRC-003 | CAN-010, Tabellenzelle CAN-010 | — |
| CAN-113 | Referenzstrecken | EXPLICIT | SRC-003 | CAN-010, Tabellenzelle CAN-010 + Prosa | — |
| CAN-114 | Reale Run- und Bike-Gerätetests je Plattform | EXPLICIT | SRC-003 | CAN-010, Prosa 'Evidence' | Run und Bike werden getrennt nachgewiesen. |
| CAN-115 | App-Kill- und Background-Tests | EXPLICIT | SRC-003 | CAN-010, Tabellenzelle CAN-010 + Prosa | — |
| CAN-116 | Batterietests | EXPLICIT | SRC-003 | CAN-010, Tabellenzelle CAN-010 + Prosa | — |
| CAN-117 | Health-Gerätetests | EXPLICIT | SRC-003 | CAN-010, Tabellenzelle CAN-010 | — |
| CAN-118 | Claims-Review | EXPLICIT | SRC-003 | CAN-010, Prosa 'Evidence' | — |
| CAN-119 | Sichtbarkeits-Matrix (Testtabelle Plan 7) | EXPLICIT (belegter Kern) · ASSUMPTION (Privacy-Review) | SRC-003 | CAN-010, Tabellenzelle CAN-010 + Prosa | **Klausel-scharfe Korrektur 2026-07-20 (Runde 6, Nutzeranweisung):** Ursprünglicher Wortlaut „Privacy-Matrix und Privacy-Review" **klauselscharf getrennt**. **Belegt (EXPLICIT):** „**Sichtbarkeits-Matrix** (Testtabelle in Plan 7)" — SRC-003:363, Task 7.3 SRC-003:522, GATE B SRC-003:683. Wortwahl aus der Quelle übernommen: **„Sichtbarkeits-"**, nicht „Privacy-". **ASSUMPTION (nicht in Quelle gefunden):** ein eigener „Privacy-Review"-Prozess als evidence artifact — SRC-003 nennt zwar Data-Protection-Anforderungen und Threat-Model-Review (CAN-120), aber **keine als „Privacy-Review" benannte** Prüfhandlung als Evidence-Item. **Behandlung:** Kern der Zeile bleibt EXPLICIT (Sichtbarkeits-Matrix). Die „Privacy-Review"-Aussage ist **ASSUMPTION**, bis der Nutzer entweder eine Quelle nennt (dann EXPLICIT) oder sie als eigene Prozessentscheidung bestätigt (dann CONFIRMED) oder sie verwirft. **Metamodell nicht geändert:** Keine neue CAN-ID vergeben (Registry eingefroren), die Splitkennzeichnung erfolgt hier innerhalb der Befund-Spalte. **NACHTRAG Runde 6 (2026-07-20, Quellennachzug gegen `docs/sources/`) — vier Korrekturen und ein offengelegter Konflikt.** (a) **Die Aussage-Spalte ist verkürzt worden, die Source-Type-Spalte nicht.** Die Klausel „Privacy-Review" steht seit der obigen Korrektur nicht mehr in der Aussage, wird in der Source-Type-Spalte aber weiterhin als ASSUMPTION geführt — ein Selbstwiderspruch. Er wird hier **offengelegt und nicht geglättet**; die Wiederaufnahme oder endgültige Streichung der Klausel ist eine **Wortlautfrage und gehört dem Nutzer**. (b) **Die gestrichene Klausel hat als einzige der beiden eine belegte Canvas-Herkunft.** Der Ursprungstext dieses Canvas nennt unter „## Evidence" (Zeile 584) wörtlich „- Claims-, Privacy- und Threat-Model-Reviews." — das ist die gemeinsame Lineage von CAN-118, CAN-119 und CAN-120 und nennt einen **Review**, **keine Matrix**. Umgekehrt kommt „Matrix" im gesamten Ursprungstext nicht vor. Belegseitig verhält es sich genau andersherum: die Quellen kennen die **Sichtbarkeits-Matrix** (SRC-003:363, :522, :683; `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md`:192) und **keinen** Privacy-Review. Beide Hälften sind also auf je eigene Weise defekt; die obige Korrektur behebt nur eine davon. (c) **Abwesenheit präzise:** „Privacy-Matrix", „Privacy-Review" und „Datenschutz" ergeben in allen vier Quellen **null** Treffer. Privacy-bezogene **Prüfungen** existieren jedoch, nur eng gebunden und nicht als querschnittlicher Nachweisvorgang: SRC-003:629 „eigene Privacy-Prüfung" (Task 17.4 Zyklusdaten, Stufe E), SRC-003:715 „DSGVO-Prüfung in 10.2" (serverseitige Gesundheitsdaten, Stufe C), SRC-003:643 „\| Privacy Policy + Terms \| A \| App Privacy Labels korrekt …". Der Satz, es gebe **gar keine** privacy-bezogene Prüfung, wäre zu weit und wird hier zurückgenommen. (d) **Die obenstehende Begründung „SRC-003 nennt … Threat-Model-Review (CAN-120)" ist unzutreffend.** „Threat-Model-Review" kommt in keiner Quelle vor; belegt ist nur „**Threat-Model** Standortfreigabe + Sicherheitsmodell … Dokument extern gegengeprüft" (SRC-003:602). Dieselbe quellenlose „-Review"-Prägung trägt **CAN-118** („Claims-Review"; die Quellen sagen „Juristische Claims-Prüfung", SRC-003:626, und „Claims juristisch freigegeben", SRC-003:686). **CAN-118 und CAN-120 sind mit derselben Linse getrennt zu prüfen** — ohne diese Prüfung bleibt die Bereinigung von CAN-119 wirkungslos. Sie werden in diesem Lauf **nicht** angefasst und **nicht** umgedeutet; der Prüfbedarf steht unter „Offene Punkte dieses Canvas". (e) **Herkunft „Tabellenzelle CAN-010" — Abwesenheitsbefund:** der Ursprungstext dieses Canvas führt unter „## Evidence" ausschließlich eine Prosa-Liste, **keine Tabelle**. Die referenzierte Tabellenzelle ist in diesem Dokument nicht reproduziert und hier daher nicht überprüfbar; das gilt gleichermaßen für CAN-111 bis CAN-117 und CAN-121 bis CAN-123. Es wird **nichts** umgedeutet und keine Herkunftsangabe geändert. (f) **Offengelegter Konflikt, nicht entschieden:** dieselbe Sache wird im PRD bereits quellentreu als **EV-018** („Sichtbarkeits-Matrix, Zwei-Account- und Moderationstest") geführt und ist über **CAN-057** verkettet. Die Umbenennung von CAN-119 auf „Sichtbarkeits-Matrix" kann deshalb ein **anbindungsloses Zweitexemplar** erzeugen und die Doppelzählung desselben Nachweises bei **GATE B** begünstigen. Dieser Canvas entscheidet das nicht und hängt keinen Anker um. **Decision-Record-Verknüpfung 2026-07-20 (Runde 6):** Die klausel-scharfe Trennung (EXPLICIT für „Sichtbarkeits-Matrix", ASSUMPTION für „Privacy-Review"-Anteil) ist als **DEC-014** in `docs/decisions/decision-log.md` protokolliert. |
| CAN-120 | Threat-Model-Review | EXPLICIT | SRC-003 | CAN-010, Prosa 'Evidence' | — |
| CAN-121 | Simulationen für Effort, Territory und Rewards | EXPLICIT | SRC-003 | CAN-010, Tabellenzelle CAN-010 + Prosa | — |
| CAN-122 | Store-Testtracks | EXPLICIT | SRC-003 | CAN-010, Tabellenzelle CAN-010 + Prosa | — |
| CAN-123 | Evidence Ledger | EXPLICIT | SRC-003 | CAN-010, Tabellenzelle CAN-010 + Prosa | Datei: docs/EVIDENCE-LEDGER.md. |

### Success Signals

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-124 | W4-Retention aktiver Tracker-Nutzer | EXPLICIT | SRC-001 | CAN-009, Tabellenzelle CAN-009 ('hält Nutzer nach vier Wochen') | Ersetzt Facette CAN-009-a. Zielwert steht in VIS-006 Zeile A: > 30 %. Der Canvas selbst nennt keinen Zielwert (MISSING im Canvas, vorhanden in der Vision). |
| CAN-125 | Quote der Stimmungs-Check-ins nach einer Aktivität | EXPLICIT | SRC-001 | CAN-009, Tabellenzelle CAN-009 ('Health-Erklärungen werden genutzt') | Teil-Ersatz für Facette CAN-009-b. Zielwert VIS-006 Zeile A: > 50 %. CAN-009-b bündelte zwei unterschiedlich messbare Signale in einer Aussage – daher zwei Atome (CAN-125, CAN-126). |
| CAN-126 | Öffnungsrate der Score-Erklärung ('Warum'-Aufrufe) | EXPLICIT | SRC-001 | CAN-009, Tabellenzelle CAN-009 ('Health-Erklärungen werden genutzt') | Teil-Ersatz für Facette CAN-009-b. Zielwert VIS-006 Zeile A: > 25 %. |
| CAN-127 | Anteil Nutzer in einem Team nach 60 Tagen | EXPLICIT | SRC-001 | CAN-009, Tabellenzelle CAN-009 ('spätere Community-Systeme erhöhen reale gemeinsame Aktivitäten') | Teil-Ersatz für Facette CAN-009-c. Zielwert VIS-006 Zeile C: > 25 %. CAN-009-c bündelte drei Signale. |
| CAN-128 | Anteil Teams mit realer gemeinsamer Aktivität pro Woche | EXPLICIT | SRC-001 | CAN-009, Tabellenzelle CAN-009 | Teil-Ersatz für Facette CAN-009-c. Zielwert VIS-006 Zeile C: > 40 %. |
| CAN-129 | Season-Teilnahme aktiver Teams | EXPLICIT | SRC-001 | CAN-009, Tabellenzelle CAN-009 | Teil-Ersatz für Facette CAN-009-c. Zielwert VIS-006 Zeile D: > 60 %. |
| CAN-130 | Eine veröffentlichte und für mindestens einen berechtigten Empfänger sichtbare Routenempfehlung führt im Durchschnitt zu mehr als einer tatsächlichen Routenübernahme. Run und Bike werden getrennt ausgewertet. | EXPLICIT | Nutzerentscheidung 2026-07-19 | CAN-009, **nicht im Ursprungstext dieses Canvas enthalten** | Trägt REQ-019 / AC-041. `measurement_type` PRODUCT_OUTCOME · `evidence_status` **planned** · `empirical_result` **MISSING** · `release_gate` **B** · Messfenster **rollierende 28 Tage** · Zielwert **> 1,0**. Vollständige Spezifikation direkt unter dieser Tabelle — sie wird **nicht gekürzt**, weil Nenner-Definition und Ausschlussregeln der eigentliche Inhalt der Entscheidung sind. |

#### CAN-130 — vollständige Spezifikation (Nutzerentscheidung 2026-07-19)

| Feld | Wert |
|---|---|
| `measurement_type` | PRODUCT_OUTCOME |
| `source_type` / `target_source_type` | EXPLICIT |
| `evidence_status` | **planned** — Metrik, Berechnung und zuständiges Gate sind definiert, die Instrumentierung fehlt. Es existiert kein Code. |
| `empirical_result` | **MISSING** |
| `release_gate` | **B** |
| `measurement_window` | rollierende 28 Tage |
| `target_or_pass_condition` | **> 1,0** bestätigte Routenübernahmen je auswertbarer Empfehlung |

**Kennzahl** = bestätigte Routenübernahmen / auswertbare Routenempfehlungen.

**„Auswertbar" nur wenn** die Empfehlung: erfolgreich veröffentlicht wurde; mindestens einen
berechtigten Empfänger hatte; im Messfenster sichtbar sein konnte; **nicht** vor möglicher
Ausspielung gelöscht, blockiert oder moderativ verborgen wurde.

**Nicht in den Nenner:** private Empfehlungen ohne berechtigten Empfänger · technisch nicht
ausgelieferte Empfehlungen · vor Ausspielung gelöschte Empfehlungen · durch Blockierung oder
Moderation vollständig unsichtbare Empfehlungen · Test- und Seed-Daten.

**Mehrere Nutzer dürfen dieselbe Empfehlung übernehmen** — der Durchschnitt kann daher > 1,0
sein. Das ist kein Rechenfehler, sondern die Absicht der Kennzahl.

**Getrennt auszuweisen:** `run_route_adoptions_per_recommendation` und
`bike_route_adoptions_per_recommendation`. Ein Gesamtwert darf gezeigt werden, aber **nie
anstelle** der getrennten Sportwerte.

**Guardrail-Signale:** Anzahl auswertbarer Empfehlungen · Empfehlungen ohne berechtigten
Empfänger · technisch fehlgeschlagene Ausspielungen · mediane Zahl berechtigter Empfänger je
Empfehlung · Anteil Empfehlungen mit mindestens einer Übernahme · Übernahmen je 100
berechtigten Ausspielungen (sofern datenschutzkonform messbar) · Run/Bike-Verteilung · Lösch-,
Blockierungs- und Moderationsanteil.

**Datenschutzbedingt unsichtbare Empfehlungen werden SEPARAT ausgewiesen, NICHT als Gegenprobe
in den Nenner.** Sonst wird fehlender *Zugang* fälschlich als mangelndes *Nutzerinteresse*
gelesen — das ist der Unterschied zwischen „die Funktion überzeugt nicht" und „die Funktion war
nie sichtbar".

**Telemetrie (privacy-minimiert).** Zulässige Ereignisse: `route_recommendation_published` ·
`route_recommendation_eligible` · `route_recommendation_exposed` · `route_adopted` ·
`route_recommendation_deleted` · `route_recommendation_hidden`. Zulässige Felder: pseudonyme
`recommendation_id` · pseudonyme `adoption_id` · `sport` (`run`|`ride`) ·
Sichtbarkeitskategorie · grober Zeitstempel bzw. Zeitbucket · Ergebnisstatus · Event-Version.
**Nicht zulässig:** GPS-Koordinaten · Routengeometrie · Start-/Zieladresse · Health-Daten ·
Klarnamen · E-Mail · vollständige Gerätekennungen · öffentliche Analytics-Profile ·
Werbe-/Cross-Service-Tracking. **Kein paralleler Standort- oder Verhaltenstracker**; die
Kennzahl ist möglichst aus ohnehin nötigen Backend-Ereignissen zu aggregieren.

**Local-first-Abgrenzung.** A0/A1: Aktivitäts-, Health- und Verlaufsdaten bleiben standardmäßig
lokal. Ab B dürfen für die **ausdrücklich aktivierte** Social-/Empfehlungsfunktion minimierte
Metadaten verarbeitet werden. **Rohroute und GPS-Geometrie NIE für die Erfolgsmessung.**
Gemessen wird das Ereignis „Empfehlung übernommen", **nicht** die später gelaufene oder
gefahrene Strecke.

**Getrenntes funktionales und Mess-Kriterium.** AC-019 ist in zwei Kriterien geteilt.
Funktional: „Ein berechtigter Nutzer kann eine sichtbare Routenempfehlung übernehmen. Die
übernommene Route wird in seiner Planung verfügbar, ohne dass private Daten des Empfehlenden
offengelegt werden." Messkriterium (AC-041): „Für Gate B kann die Zahl bestätigter Übernahmen
je auswertbarer Empfehlung datenschutzkonform, sportartspezifisch und reproduzierbar berechnet
werden." **Das funktionale Kriterium kann bestanden sein, während die Produktkennzahl noch
keine ausreichende Stichprobe hat.**

**Stichprobenregel — vor endgültiger Bewertung zu definieren** (OQ-014): Mindestzahl
auswertbarer Empfehlungen · Mindestzahl berechtigter Empfänger · Mindestdauer des Messfensters ·
Behandlung von Testkonten · Umgang mit Mehrfachübernahmen desselben Nutzers · Umgang mit
gelöschten und moderierten Empfehlungen · getrennte Run-/Bike-Auswertung. Bis dahin gilt:
`target_source_type` EXPLICIT, `evidence_status` planned, `empirical_result` MISSING. **Es wird
keine Mindestzahl geraten.**

**Offene Entscheidung OQ-012 — privacy-minimierte Telemetrie für Routenempfehlungen.** Status
`open`, Source Type MISSING. Vor Gate B zu klären: ob `exposed` client- oder serverseitig
erhoben wird · welche Event-Metadaten nötig sind · welche Daten gespeichert werden dürfen ·
Aufbewahrung der Rohereignisse · ab wann nur noch Aggregate · ob eine separate Einwilligung
nötig ist · Wirkung von Profil-Privacy, Blockierungen und Löschungen · Entfernung bzw.
Anonymisierung gelöschter Accounts aus den Messdaten · Owner der Instrumentierung · verwendete
Analytics-/Event-Lösung. **Blockierend** für den externen Gate-B-Erfolgsnachweis von REQ-019
und für **jede** Behauptung, CAN-130 sei empirisch validiert. **Nicht blockierend** für A0/A1
und nicht für diese Dokumentkorrektur.

### Allowed Scope je Release-Stufe

| ID | Aussage | Source Type | Source | Herkunft | Befund / Hinweis |
|---|---|---|---|---|---|
| CAN-131 | Stufe A0: robustes Tracking, Planung, Verlauf, Persistenz und Designbasis; nicht erlaubt vor Gate: Health-Behauptungen, Social, Territory | ASSUMPTION | SRC-003/SRC-005 | CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile A0 | OPEN QUESTION: Die Zeile beschreibt A0 als lokale Stufe, während der bestätigte A0-Routing-Proxy (CAN-091, CAN-096) serverseitig Wegpunkte verarbeitet. CONTRA-006 ist dazu offen; CAN-095 präzisiert local-first, löst den Widerspruch aber nicht vollständig. |
| CAN-132 | Stufe A1: Health-Basis und erklärbarer Score; nicht erlaubt vor Gate: Community- und Wettbewerbssysteme | ASSUMPTION | SRC-003/SRC-005 | CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile A1 | — |
| CAN-133 | Stufe A2 / v1.0: Rückblicke, Export, Avatarbasis, Widgets und Store-Release; nicht erlaubt vor Gate: Accounts und öffentlicher UGC | ASSUMPTION | SRC-003/SRC-005 | CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile A2 | — |
| CAN-134 | Stufe B / v2: Accounts, Profile, Empfehlungen, Feed und Moderation; nicht erlaubt vor Gate: Teams/Territory ohne Anti-Cheat | ASSUMPTION | SRC-003/SRC-005 | CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile B | — |
| CAN-135 | Stufe C / v3: Teams, Rankings, Challenges und Anti-Cheat; nicht erlaubt vor Gate: Territory/Live ohne Simulation und Threat-Model | ASSUMPTION | SRC-003/SRC-005 | CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile C | — |
| CAN-136 | Stufe D / v4: Territory, Seasons, Events und Live-Safety; nicht erlaubt vor Gate: Coach-/Recovery-Claims ohne Freigabe | ASSUMPTION | SRC-003/SRC-005 | CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile D | — |
| CAN-137 | Stufe E / v5: Wearables, Coach, Recovery, Wetter und Zyklus; nicht erlaubt: nicht freigegebene medizinische Claims | ASSUMPTION | SRC-003/SRC-005 | CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile E | — |

## Reservierte, inhaltlich offene Canvas-Items (BLOCKER)

Diese IDs sind vergeben, damit spätere Phasen keine eigenen IDs erfinden müssen. Ihr **Inhalt
ist MISSING** und aus keinem vorhandenen Artefakt ableitbar — er würde neue Produktsubstanz
hinzufügen und braucht deshalb eine Nutzerentscheidung. Sie zählen nicht als erfüllte
Canvas-Referenz.

| ID | Fehlende Aussage | Herkunft | Wer hängt daran | Warum nicht ableitbar |
|---|---|---|---|---|
| CAN-016 | MISSING – Fortschritts- und Motivationsproblem | CAN-001 | REQ-015, REQ-016 | Der Canvas nennt Fortschritt nur als Wertversprechen (CAN-030), nicht als Problem. |
| CAN-017 | MISSING – Sicherheitsproblem | CAN-001 | REQ-030, REQ-031 | VIS-003 nennt „sicheren Zugang“, der Canvas nennt kein Sicherheitsproblem — Canvas/Vision-Divergenz. |
| CAN-018 | MISSING – Datenschutzproblem | CAN-001 | REQ-034 | Datenschutz erscheint nur als Constraint (CAN-088) und Risiko (CAN-105). |
| CAN-019 | MISSING – Planungs- und Orientierungsproblem vor der Aktivität | CAN-001 | REQ-006, REQ-007 | Routenplanung ist im Canvas nur Capability (CAN-050, CAN-051). |
| CAN-020 | MISSING – Fairness- und Manipulationsproblem | CAN-001 | REQ-023, REQ-024 | Fairness ist im Canvas nur Wertversprechen (CAN-033, CAN-036) und Risiko (CAN-104, CAN-109). |
| CAN-021 | MISSING – Problem hinter Einzel-Revieren und Sportplatz-Challenges | CAN-001 | REQ-028, REQ-029 | Einzel-Reviere haben laut `docs/traceability.md` weder Problembezug noch Wertklausel noch Erfolgssignal. |

**Am 2026-07-19 aus dieser Tabelle entfernt, weil inhaltlich entschieden:** CAN-022 (steht
jetzt unter „Problem"), CAN-099 (unter „Constraints") und CAN-130 (unter „Success Signals").
**CAN-071 und CAN-140 sind nicht entschieden, sondern deprecatet** — beide waren Composites;
CAN-071 ist durch CAN-138, CAN-139 und CAN-140 ersetzt, CAN-140 seinerseits durch CAN-142 und
CAN-143. Sie stehen deshalb im Abschnitt „Deprecatete atomare Canvas-Items", nicht hier — ein
deprecatetes Item ist **keine offene Reserve**. **CAN-138 bis CAN-143 standen nie in dieser
Tabelle**: CAN-138 bis CAN-140 sind Nachfolger-IDs von CAN-071, CAN-142 und CAN-143 sind
Nachfolger-IDs von CAN-140, CAN-141 ist neu vergeben. **Sechs** reservierte Items bleiben
offen: CAN-016 bis CAN-021. Diese Zahl ist aus der Tabelle oben abzulesen und aus
`docs/ID-REGISTRY.md` §7.3 abzuleiten — sie darf in keinem Werkzeug als Literal stehen. Der
frühere Stand „zehn reservierte Canvas-Items (CAN-016…022, CAN-071, CAN-099, CAN-130)" ist
**überholt**: CAN-022, CAN-099 und CAN-130 sind aktiv, CAN-071 ist deprecatet.

**Nicht anwendbar statt fehlend.** Zwei Requirements haben bewusst keinen Problembezug:
REQ-035 (Evidence Ledger und Definition of Done) und REQ-036 (Store- und Release-Gates) sind
Prozess- und Compliance-Anforderungen ohne unmittelbares Nutzerproblem. Ihr Canvas-Anker ist
CAN-123 (Evidence Ledger) beziehungsweise CAN-083 (Store-Policies). Für sie wird **kein**
Problem-Item reserviert. Das ist die einzige requirement-spezifische Nichtanwendbarkeit in
diesem Canvas; sie wird ausdrücklich **nicht** auf andere Requirements verallgemeinert. Alle
übrigen Lücken sind entweder in der Tabelle oben oder unter „Offene Punkte dieses Canvas"
geführt — darunter die drei Requirements ohne Problem-Anker, die in keiner der beiden
Reserve-Kategorien aufgehen.

**Ausdrücklich KEINE Nichtanwendbarkeit: REQ-037, REQ-038 und REQ-039.** Seit der Bereinigung
der in `docs/ID-REGISTRY.md` verbotenen Schlusskette „Wahrnehmbarkeit als Vorstufe von
Verständlichkeit" haben diese drei Requirements **keinen canvas-problem-Anker** mehr. Das ist
eine **Lücke**, kein bewusster Verzicht: Zugänglichkeit, Gestaltungssprache und
Datenportabilität sind sehr wohl nutzerseitige Probleme — der Canvas führt sie nur nicht.
Deshalb wird hier **nicht** die Begründungsfigur von REQ-035/REQ-036 auf sie übertragen, und es
wird auch **kein** vorhandenes Problem-Item umgedeutet: CAN-013 („Bestehende Tracker liefern
Daten ohne verständliche Bedeutung") trägt keine der drei Aussagen, und die reservierten
CAN-016 … CAN-021 decken keine davon ab. Der Punkt bleibt als **BLOCKER** offen
(Registry §8 Punkt 37); eine neue Problem-ID vergibt dieser Canvas nicht — die Registry ist
eingefroren.

**Der frühere BLOCKER „Source Type für CAN-099 ist nirgends festgelegt" ist damit nicht
verschwunden, sondern ersetzt.** `docs/ID-REGISTRY.md` führt CAN-099 seit dem 2026-07-20 mit
Source Type **EXPLICIT**, weil der Nutzer den Wortlaut als verbindlich gesetzt hat; nach der
ID-Hoheitsregel gilt die Registry. Offen bleibt die **ausdrückliche Gegenbestätigung** des
Wortlauts — sie wird als Registry §8 Punkt 43 geführt und steht oben in „Offene Punkte dieses
Canvas". Der Source Type wurde weder geraten noch von einem Nachbaritem übernommen.

---

# Ursprungstext

Die folgenden Abschnitte sind der **wörtliche Ursprungstext** des Canvas. Sie belegen die
Herkunft der atomaren Items und werden nicht gelöscht. **Sie sind kein Referenzziel**:
Requirements und Traceability zeigen ausschließlich auf CAN-IDs, nie auf diese Prosa.

## Problem

Training wird aufgezeichnet, aber häufig nicht erklärt. Nutzer sehen Pace, Herzfrequenz und Kilometer, erhalten jedoch zu wenig verständliche Orientierung. Gleichzeitig bleiben Social-Funktionen oft anonym und ortsunabhängig. Das Produkt soll deshalb erst den Trainingsnutzen lösen und darauf reale lokale Gemeinschaft aufbauen.

## Users / Customers

- Freizeit-Läufer:innen und Radfahrer:innen.
- Ambitionierte Ausdauersportler:innen.
- Lauf- und Radsportgruppen.
- Vereine und lokale Communities.

## Value Promise

> Verlässliches Tracking und erklärbare Trainingsorientierung zuerst; verdiente Progression, lokale Gemeinschaft und Territory danach – mit klaren Fairness-, Privacy- und Evidence-Gates.

## Current Alternatives

| Alternative | Stärke | Lücke, die adressiert wird |
|---|---|---|
| Strava | Tracking, Segmente, Netzwerk | lokale Team- und Territory-Mechanik sowie erklärbarer Health-Fokus |
| Garmin/Apple/Google/Fitbit | Geräte- und Health-Ökosystem | plattformübergreifende lokale Community und verdiente Progression |
| Whoop | Belastungs- und Recovery-Fokus | Transparenz, Smartphone-Basis und lokale Community |
| WhatsApp/Vereine | reale Gruppen | strukturierte Aktivitäten, Fortschritt und sichere Auffindbarkeit |

## Key Capabilities

1. Run/Bike-Tracking mit robustem Background- und Recovery-Verhalten.
2. Routenplanung und echte routebezogene Restdistanz.
3. Health-Score mit Erklärbarkeit, Fallback und Confidence.
4. Progression, Rückblicke und verdiente Avatar-Identität.
5. Accounts, Privacy, Empfehlungen und Moderation.
6. Teams, Challenges, Rankings und Anti-Cheat.
7. Team- und Einzel-Territory, Seasons und lokale Events.
8. Live-Safety, Wearables und erklärbare Coach-Funktionen.

## Non-Goals

- Keine medizinische Diagnose oder garantierte Unfallhilfe.
- Kein allgemeiner Messenger.
- Keine Indoor-Workout-Plattform im definierten Scope.
- Kein Verkauf von Leistungsstatus oder Spielvorteilen.
- Kein sichtbares H3-/Raster-Gameplay.
- Kein volles Territory-System im Tracker-MVP.

## Constraints

- Expo/React Native/TypeScript als gemeinsame App-Basis; native Dev-Builds für Background-, Health- und Widget-Funktionen.
- iOS und Android müssen pro Gate real getestet werden.
- Standort- und Health-Daten erfordern Zweckbindung und Datenminimierung.
- Karten-, Routing- und Backendanbieter bleiben ADR-Entscheidungen.
- Der öffentliche Name darf erst nach Markenprüfung finalisiert werden.
- **Bestätigte Nutzerentscheidung 2026-07-19 (DEC-005 `user-confirmed`, CONTRA-002 `resolved`; Quelle `docs/decisions/decision-log.md`):** Externes Routing läuft bereits ab Stufe A0 ausschließlich über einen minimalen serverseitigen Routing-Proxy. Ein Routing-API-Key als `EXPO_PUBLIC_*`-Variable im App-Bundle ist ausgeschlossen; NFR-007 („keine Secrets im Client") gilt damit ab A0 und nicht erst ab Stufe B. Der Proxy ist bewusst minimal (Key-Halten, Weiterleitung, Rate Limit) und präjudiziert den vollständigen Backend-Entscheid nicht.
- Der vollständige Backend-Entscheid (Geo, Auth, Realtime, EU-Hosting für die sozialen Stufen) bleibt davon unberührt und offen — siehe OQ-005.

**Korrekturhinweis 2026-07-19 zum Ursprungstext.** Der ursprüngliche letzte Constraint-Punkt
lautete zusätzlich: „Der Ablageort des A0-Proxys im Repository ist noch nicht entschieden —
siehe OQ-011.“ Dieser Satz ist **überholt**. Der Nutzer hat OQ-011 am 2026-07-19 entschieden:
Ablageort ist `infra/routing-proxy/`, ausdrücklich **nicht** `backend/`. Begründung des
Nutzers: eine begrenzte, austauschbare Infrastrukturkomponente; `backend/` bleibt für Stufe B
reserviert. Die vollständige Entscheidung ist in CAN-091 bis CAN-098 abgebildet. Die
Registry führt OQ-011 als `resolved`; das kanonische Register
`docs/decisions/open-questions.md` führt ihn noch als offen und wird in Phase 3 von seinem
Datei-Owner nachgezogen — dieser Canvas ändert das Register nicht.

## Risks

Siehe `docs/risks/revyr-risk-register.md`. Kritisch sind GPS-/Batterierisiken, Health-Claims, Standortmissbrauch, Anti-Cheat-Fehler, Geo-Komplexität, private Sportanlagen, Store-Policies und Namenskollision.

## Success Signal

Der erste Nachweis ist nicht Territory-Nutzung, sondern ein stabiler Tracker mit W4-Retention, verständlichen Health-Auswertungen und nachweisbarer Datenqualität. Community- und Territory-Signale werden erst in späteren Phasen bewertet.

## Evidence

- Unit- und Property-Tests der Domainlogik.
- Referenzstrecken und reale Run/Bike-Gerätetests.
- App-Kill-, Background- und Batterietests.
- Claims-, Privacy- und Threat-Model-Reviews.
- Simulationen für Effort, Territory und Rewards.
- Store-Testtracks und Evidence Ledger.

## Allowed Scope (Produkt-Scope je Release-Stufe)

Dieser Abschnitt beschreibt den **fachlichen** Scope pro Release-Stufe. Er ist kein Datei-Scope. Die maschinell prüfbaren Datei-/Verzeichnismuster stehen im separaten Abschnitt „Allowed change scope". Atomar geführt in CAN-131 bis CAN-137.

| Stufe | Erlaubter Scope | Nicht erlaubt vor Gate |
|---|---|---|
| A0 | robustes Tracking, Planung, Verlauf, Persistenz, Designbasis | Health-Behauptungen, Social, Territory |
| A1 | Health-Basis und erklärbarer Score | Community- und Wettbewerbssysteme |
| A2 / v1.0 | Rückblicke, Export, Avatarbasis, Widgets, Store-Release | Accounts und öffentlicher UGC |
| B / v2 | Accounts, Profile, Empfehlungen, Feed, Moderation | Teams/Territory ohne Anti-Cheat |
| C / v3 | Teams, Rankings, Challenges, Anti-Cheat | Territory/Live ohne Simulation/Threat-Model |
| D / v4 | Territory, Seasons, Events, Live-Safety | Coach-/Recovery-Claims ohne Freigabe |
| E / v5 | Wearables, Coach, Recovery, Wetter, Zyklus | nicht freigegebene medizinische Claims |

## Allowed change scope

Maschinell geprüfter Datei-Scope für `plumbline-scope-check` (Stufe A0). Alle Muster sind
repo-relativ. Dieser Abschnitt ist eine Schranke: Was hier nicht steht, darf in A0 nicht
geändert werden. Erweiterungen für A1 und spätere Stufen sind eigene, bestätigte
Scope-Änderungen.

Stand: es existiert noch kein Code. Die Expo-App entsteht unter `mobile/`, die
Projektdokumentation liegt unter `docs/`, der A0-Routing-Proxy unter `infra/routing-proxy/`.

Hinweis zur Parserform: In diesem Abschnitt wird jede Zeile, die mit einem Listenzeichen
beginnt, als Pfadmuster gelesen. Erläuterungen stehen deshalb ausschließlich als Fließtext.

- `mobile/app/**`
- `mobile/src/**`
- `mobile/assets/**`
- `mobile/*.json`
- `mobile/*.js`
- `mobile/*.ts`
- `mobile/.env.example`
- `mobile/.gitignore`
- `infra/routing-proxy/**`
- `docs/**`
- `docs/architecture/**`
- `docs/decisions/**`
- `docs/implementation/**`
- `docs/risks/**`
- `docs/traceability.md`
- `docs/EVIDENCE-LEDGER.md`
- `docs/ID-REGISTRY.md`
- `intake-package.json`
- `.gitignore`

Die Einträge unter `docs/` werden von `docs/**` bereits abgedeckt. Sie stehen trotzdem
einzeln in der Liste, weil der Nutzer sie am 2026-07-19 ausdrücklich benannt hat und weil eine
spätere Verengung von `docs/**` sonst still die benannten Pfade mitentfernen würde.

Bewusst gesperrt und damit nicht enthalten: generierte native Projekte (`mobile/ios/`,
`mobile/android/`), CI-Konfiguration, Root-Konfigurationsdateien außer `.gitignore` und
`intake-package.json` sowie jedes Server-/Backend-Verzeichnis mit Ausnahme des einen,
namentlich freigegebenen Pfades `infra/routing-proxy/`.

Ausdrücklich **nicht** pauschal freigegeben — weder jetzt noch als stillschweigende Folge der
Proxy-Entscheidung: `backend/**`, beliebige Server-Endpunkte, Auth, Profile, Social, Realtime,
Territory-Backend und allgemeine Datenpersistenz. Diese Aufzählung ist eine Schranke, keine
Aufzählung von Beispielen.

Verbindliche Schranke: Der Routing-Proxy darf **nicht stillschweigend zu einem allgemeinen
Backend erweitert werden.** `infra/routing-proxy/` ist für genau einen Zweck freigegeben:
das serverseitige Halten des
Routing-Provider-Keys und die Weiterleitung von Routing-Anfragen. Ein neuer Endpunkt außerhalb
dieses Routing-Scope ist eine Scope-Erweiterung und braucht **alle vier** Schritte: eine neue
ADR, eine ausdrückliche Scope-Freigabe durch den Nutzer, aktualisierte Requirements samt
Traceability und aktualisierte Risiken. Ein Endpunkt, der nur „praktisch dort schon liegt“,
ist keine Begründung. Der vollständige Backend-Entscheid bleibt offen (OQ-005); der A0-Proxy
präjudiziert ihn nicht.

Prüfung am 2026-07-19 (Auftau-Schritt 2): Die neuen Items CAN-138 bis CAN-141 sowie die
gefüllten Items CAN-022, CAN-099 und CAN-130 verlangen **keinen neuen Pfad**. Verlauf,
Detailansicht, GPX-Erzeugung, Streckenvergleich und Designtokens entstehen unter
`mobile/src/**` beziehungsweise `mobile/app/**` und sind damit bereits abgedeckt; eine
GPX-Datei ist ein Laufzeitartefakt und kein Repositorypfad. Die Telemetrie aus CAN-130 ist auf
Stufe B fällig und wird hier ausdrücklich **nicht** vorab freigegeben. Der Allowed change scope
bleibt deshalb **unverändert**.

Erneute Prüfung am 2026-07-20 (Runde 4): Die kanonisierten Wortlaute von CAN-099, CAN-138,
CAN-139 und CAN-141 und die beiden neuen Items **CAN-142** und **CAN-143** verlangen ebenfalls
**keinen neuen Pfad**. Wiederverwendung einer gespeicherten Route und Streckenvergleich sind
Domain- und UI-Logik unter `mobile/src/**` beziehungsweise `mobile/app/**`; eine gespeicherte
Route ist ein Laufzeitdatensatz in der lokalen Persistenz, kein Repositorypfad. Der Allowed
change scope bleibt **unverändert**. Es entsteht in diesem Lauf kein Implementierungscode, kein
Deployment und keine AWS-Ressource, und es wird kein Verzeichnis angelegt.

Zum Umsetzungsstand: Der Pfad `infra/routing-proxy/` ist im Scope aufgenommen und
dokumentiert. Das Verzeichnis wird in diesem Lauf **nicht angelegt** und es entsteht kein
Implementierungscode, kein Deployment und keine AWS-Ressource. Die dokumentierte A0-Laufzeit
(AWS Lambda und API Gateway, Region eu-central-1, Provider-Key nur serverseitig, Rate Limit,
Timeout, Kill Switch) ist Beschreibung, nicht Umsetzung.

## Unresolved Questions

Kanonisches Register: `docs/decisions/open-questions.md`. Die ID-Hoheit liegt bei
`docs/ID-REGISTRY.md`. Dieser Canvas **referenziert** OQ-IDs, er definiert sie nicht. Bei
Abweichung gilt das Register.

| ID | Question | Needed By | Source Type |
|---|---|---|---|
| OQ-001 | Welcher öffentliche Name wird markenrechtlich freigegeben? | vor Store-Metadaten / Gate A2 | MISSING |
| OQ-003 | Welche OS-/Geräteversionen werden unterstützt? | vor A0 Feldtest | MISSING |
| OQ-004 | Welche Karten-/Routinganbieter und Kostenlimits gelten? | vor öffentlichem A2/B | MISSING |
| OQ-005 | Welches Backend besteht Geo-, Realtime-, Auth- und EU-Hosting-Prototyp? | vor Stufe B | MISSING |
| OQ-006 | Welche Health-Formulierungen werden freigegeben? | vor A1 Public Beta und E | MISSING |
| OQ-007 | Welches Geschäftsmodell trägt Karten-, Realtime- und Moderationskosten? | vor Stufe C | MISSING |
| OQ-008 | Welche Effort-, Territory- und Bahngold-Startwerte gelten? | vor Stufe C/D | MISSING |
| OQ-012 | Wie wird die privacy-minimierte Telemetrie für Routenempfehlungen ausgestaltet? | vor Gate B | MISSING |
| OQ-014 | Welche Stichproben- und Auswertungsregel gilt für CAN-130 / AC-041? | vor Gate B | MISSING |
| OQ-015 | Wann gelten zwei Strecken als fachlich vergleichbar (CAN-143 / REQ-042)? | vor Gate A2 | MISSING |
| OQ-016 | Welche Fremdanwendung dient als Referenz für den GPX-Kompatibilitätsnachweis (CAN-139 / REQ-039)? | vor Gate A2 | MISSING |

**Hinweis zu OQ-012 bis OQ-016.** Diese IDs sind am 2026-07-19 in `docs/ID-REGISTRY.md`
reserviert worden und werden hier nur **referenziert**. Im kanonischen Register
`docs/decisions/open-questions.md` sind sie noch **nicht** eingetragen; der Nachzug liegt beim
Datei-Owner (Registry-Regel 10, zulässiges Nachzugsfenster). Dieser Canvas ändert das Register
nicht. OQ-013 (Messdefinition NFR-008) betrifft kein Canvas-Item und wird hier nicht geführt.

**Nachzug OQ-015 (Runde 4, 2026-07-20).** OQ-015 war ursprünglich für CAN-140 / REQ-040
reserviert. Beide IDs sind seit dem 2026-07-20 deprecatet; die Frage wandert **vollständig und
inhaltlich unverändert** auf **CAN-143 / REQ-042** (und damit AC-043, EV-044). Sie wandert
**nicht** auf CAN-142 / REQ-041 — die Wiederverwendung einer gespeicherten Route ist ohne
OQ-015 vollständig spezifizierbar. Es wurde **keine neue OQ-ID** vergeben.

**OQ-011 ist entschieden und deshalb aus dieser Liste entfernt.** Ablageort des
A0-Routing-Proxys: `infra/routing-proxy/` (Nutzerentscheidung 2026-07-19). Die Registry führt
ihn als `resolved`; `docs/decisions/open-questions.md` führt ihn noch als offen und wird in
Phase 3 vom Datei-Owner nachgezogen.

## Offene Punkte dieses Canvas

Nichts davon wird durch eine plausible Annahme ersetzt.

| Punkt | Art |
|---|---|
| Inhalt der sechs reservierten Items CAN-016 … CAN-021 | BLOCKER |
| Wortlautbestätigung der in Runde 4 kanonisierten Items: **CAN-099, CAN-139, CAN-141** stehen auf **EXPLICIT**, weil der Nutzer den Wortlaut am 2026-07-20 als verbindlich gesetzt hat — eine ausdrückliche Gegenbestätigung liegt nicht vor (Registry §8 Punkt 43) | BLOCKER |
| Wortlaut von CAN-022, CAN-138, CAN-142 und CAN-143 ist ASSUMPTION, nicht nutzerbestätigt | ASSUMPTION |
| **REQ-037, REQ-038 und REQ-039 haben keinen canvas-problem-Anker.** Nach Entfernung der in der Registry verbotenen Schlusskette „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" führt dieser Canvas weder ein Zugänglichkeits- noch ein Gestaltungs- noch ein Portabilitätsproblem. Es wird **kein** CAN-Item umgedeutet und **keine** neue Problem-ID vergeben; die reservierten CAN-016 … CAN-021 decken keines der drei ab (Registry §8 Punkt 37) | BLOCKER |
| Inhalt von **VIS-014** — REQ-041 (CAN-142) hat keinen Vision-Anker, TRC-041 bleibt `broken`. VIS-003 wurde geprüft und trägt die Aussage **nicht** (Registry §8 Punkt 38) | BLOCKER |
| **CAN-050** ist selbst ein Composite („Routenplanung" **und** „gespeicherte Routen") und wird zusätzlich als Anker für REQ-008 geführt, obwohl die Registry es REQ-006 zuordnet. Dieser Canvas deutet CAN-050 nicht um (Registry §8 Punkt 39) | BLOCKER |
| Der kanonische CAN-139-Wortlaut nennt „in einer kompatiblen Fremdanwendung öffnen" **nicht mehr**; AC-039 (d) und EV-039 verlangen den Nachweis weiterhin. Der Bezug ist über „standardkonform" tragbar, aber nicht mehr wörtlich belegt (Registry §8 Punkt 36) | OPEN QUESTION |
| PRD-Nachzug der Persona USER-004 (CAN-025); Verknüpfung von REQ-009 und REQ-011 nur semantisch zu prüfen | BLOCKER (ID-Frage geschlossen) |
| Vergleichbarkeitsdefinition für CAN-143: Kriterium, Toleranz, Kennzahlen, Sonderfälle | MISSING, OQ-015 |
| Referenz-Fremdanwendung für den GPX-Kompatibilitätsnachweis (CAN-139) | MISSING, OQ-016 |
| Privacy-minimierte Telemetrie für Routenempfehlungen (CAN-130) | OPEN QUESTION, OQ-012 |
| Stichproben- und Auswertungsregel für CAN-130 | MISSING, OQ-014 |
| `empirical_result` für CAN-130 — es existiert kein Code, also keine Messung | MISSING |
| Bedeutung von „sicherer“ in CAN-031 (Trainings- oder Datensicherheit) | OPEN QUESTION |
| Stärke und adressierte Lücke der Alternative „lokale Event-Plattformen“ (CAN-046) | MISSING |
| Widerspruch „A0 ist lokal“ (CAN-131) gegen den serverseitigen Routing-Proxy ab A0 (CAN-091, CAN-096) | OPEN QUESTION, CONTRA-006 |
| Öffentlicher Produktname | MISSING, OQ-001 |
| Komfortaspekt „Nutzer müssen zusätzlich das Telefon mitführen“ — bewusst **ohne** ID, in diesem Lauf nicht angelegt | bewusste Auslassung, kein Versehen |
| **CAN-118 („Claims-Review") und CAN-120 („Threat-Model-Review") tragen dieselbe quellenlose „-Review"-Prägung wie der gestrichene CAN-119-Teil.** Die Bezeichnungen kommen in keiner der vier Quellen vor; belegt sind nur „Juristische Claims-Prüfung" (SRC-003:626), „Claims juristisch freigegeben" (SRC-003:686) und „Threat-Model Standortfreigabe … Dokument extern gegengeprüft" (SRC-003:602). Beide sind mit derselben Linse getrennt zu prüfen; ohne diese Prüfung bleibt die Bereinigung von CAN-119 wirkungslos. In diesem Lauf **nicht** angefasst und **nicht** umgedeutet | PRÜFBEDARF (Runde 6) |
| **Selbstwiderspruch in CAN-119:** die Source-Type-Spalte führt „ASSUMPTION (Privacy-Review)" für eine Klausel, die seit dem parallelen Lauf nicht mehr in der Aussage steht. Wiederaufnahme oder endgültige Streichung ist eine Wortlautfrage | OPEN QUESTION (Runde 6) |
| **Nachzug nach der CAN-099-Web-Streichung.** Die Erstreckung auf „nutzbare Web-Auskopplungen" steht weiterhin in REQ-037, in der Given-Spalte von AC-037, im `signal`-Feld von NFR-005 und im EV-037-Kopf. Bis zum Nachzug durch deren Owner trägt AC-037 eine Vorbedingung **ohne** Canvas-Anker. Dieser Canvas ändert die betroffenen Dateien nicht | NACHZUG (Owner PRD / Evidence Ledger / Traceability) |
| **Nachzug nach der CAN-024-Verengung.** `docs/traceability.md` führt CAN-024 bei REQ-032 als „primär (Bike-Sensorik)"; der Sensorikbedarf ist quellenseitig nur an der sekundären Persona (SRC-001:137) bzw. an der ungestuften Rad-Zielgruppe (SRC-003:65) verankert. Diese Verankerung trägt CAN-024 nach der Verengung nicht mehr | NACHZUG (Owner Traceability) |
| **Nachzug nach der CAN-051-Herabstufung.** Die Pass-Bedingung zu AC-007 beruft sich in PRD und Traceability auf CAN-051 als Autorität („die Subtraktion ist ausdrücklich verboten"); CAN-051 ist seit Runde 6 ASSUMPTION und DEC-004 steht auf `proposed` | NACHZUG (Owner PRD / Traceability) |
| **Die CSS-Farbmisch-Regel für Web-Auskopplungen (SRC-003:83, :484, :711, :735) ist in keinem Canvas-Item als Aussage geführt** — auch nicht in CAN-141. Es wird kein Item darum erweitert und keine ID vergeben | MISSING (Abwesenheitsbefund, Runde 6) |
| **Rundenbezeichnung — korrigiert.** Eine Vorfassung dieses Canvas führte „Runde 5" und „Runde 6" als zwei parallele Bearbeitungen desselben Tages. Das war ein Werkzeugartefakt: es gab **einen** Lauf (Runde 6) auf **eine** Nutzeranweisung. Alle Einträge dieses Laufs sind auf „Runde 6" vereinheitlicht | KORRIGIERT (Runde 6) |

## User Confirmation

Die Assistenz bestätigt diesen Canvas nicht im Namen des Nutzers. Status bleibt
`ready-for-user-confirmation`. Der Plumbline-Watcher hat kein Verdikt abgegeben;
`true-line-status` bleibt `pending-watcher`.
