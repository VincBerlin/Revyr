# Product Vision: REVYR Endurance Platform

Status: ready-for-user-confirmation  
Feature Slug: `revyr-endurance-platform`  
Öffentlicher Produktname: `MISSING` – „REVYR“ bleibt bis zur Markenprüfung nur Arbeitstitel  
Confirmation Status: pending-user-confirmation

## Product Vision Statement

> Eine Health-first Ausdauerplattform für Läufer:innen und Radfahrer:innen, die verlässliches Tracking in verständliche Trainingsorientierung übersetzt, reale lokale Gemeinschaft fördert und erst nach nachgewiesener Fairness die Stadt zum Spielfeld erweitert.

## Product Vision Board

| Area | ID | Value | Source Type | Source | User Decision Needed |
|---|---|---|---|---|---|
| Product Vision Statement | VIS-001 | Eine Health-first Ausdauerplattform für Läufer:innen und Radfahrer:innen, die Training verständlich macht, reale lokale Gemeinschaft fördert und die Stadt schrittweise zum fairen Spielfeld erweitert. | EXPLICIT | SRC-001/SRC-003 | no |
| Target Group | VIS-002 | Primär Freizeit-Läufer:innen und Radfahrer:innen von 20–45 Jahren mit 1–4 Aktivitäten pro Woche; sekundär ambitionierte Sportler:innen, Laufgruppen, Radsportgruppen und Vereine. | EXPLICIT | SRC-001 | no |
| User Need | VIS-003 | Nutzer benötigen Tracking ihrer Aktivitäten, eine verständliche statt abstrakte Auswertung ihrer Belastung, spürbaren Fortschritt über die Zeit und Anschluss an lokale Sportler:innen und Teams. *(verengt 2026-07-20 — Protokoll im Abschnitt „Verengung von VIS-003")* | EXPLICIT **nur für den verengten Kern**; die abgetrennten Qualifizierer „verlässlich" (Tracking) und „sicher" (Zugang) sind **ASSUMPTION — NOCH NICHT BESTÄTIGT** | Kern: SRC-001 (Z. 20, 21, 26, 47, 51, 136) und SRC-003 (Z. 45, 64). Für „sicher": **keine Quelle**. Für „verlässlich": nur NFR-Ebene (SRC-001 Z. 250, 252), nicht Bedürfnisebene | **JA — für die abgetrennten Qualifizierer** |
| Product Value | VIS-004 | Die Plattform verbindet erklärbare Trainingsbelastung, verdiente Progression, lokale Teams und reale ortsbezogene Spielmechaniken in einem konsistenten Run/Bike-Produkt. | EXPLICIT | SRC-001/SRC-003 | no |
| Project Goal | VIS-005 | Zuerst einen belastbaren Health-Tracker etablieren; danach Accounts, Community, Teams und erst nach nachgewiesener Datenqualität Territory- und Live-Systeme freischalten. | EXPLICIT | SRC-003 | no |
| Success Signal | VIS-006 | W4-Retention >30 %, Check-in-Quote >50 %, Warum-Aufrufe >25 %; später Teambeitritt, gemeinsame Aktivitäten und Season-Teilnahme als stufenbezogene Signale. | EXPLICIT | SRC-001 | no |
| Health-first Boundary | VIS-007 | Health-Ausgaben sind Orientierung, keine Diagnose. Score und Empfehlungen müssen Datenbasis, Gründe und Unsicherheit erklären. | EXPLICIT | SRC-001/SRC-003 | no |
| Fairness Boundary | VIS-008 | Run und Bike besitzen getrennte Metriken, Ziele und interne Wertungen; sportübergreifender Effort wird nur mit simulierten und versionierten Faktoren verwendet. | EXPLICIT | SRC-003 | no |
| Privacy Boundary | VIS-009 | Profile sind standardmäßig privat; Live-Standort ist pro Aktivität Opt-in, zeitlich begrenzt und start-/endpunktverschleiert; Health-Daten werden nicht für Werbung genutzt. | EXPLICIT | SRC-001/SRC-003 | no |
| Delivery Principle | VIS-010 | Kein komplexes Community-, Territory- oder Safety-System wird vor dem Evidence-Gate der vorherigen Stufe veröffentlicht. | EXPLICIT | SRC-003 | no |
| Accessibility Boundary | VIS-011 | Jeder ausgelieferte Screen muss ohne Farbunterscheidung, mit vergrößerter Schrift und mit Screenreader vollständig bedienbar sein; Zugänglichkeit ist eine Schranke, keine Quote. | **ASSUMPTION — NOCH NICHT BESTÄTIGT** | abgeleitet aus **REQ-037** (Nachfolger des deprecateten REQ-014), **AC-037** und NFR-005 im PRD; **keine** eigenständige Vision-Quelle | **JA — Nutzerentscheidung erforderlich** |

Die Zeilen VIS-001 … VIS-011 sind die **aktiven** Vision-Items (11). **Drei** weitere IDs sind
reserviert und inhaltlich MISSING — VIS-012, VIS-013 und **VIS-014** — sie stehen bewusst **nicht**
in dieser Tabelle und zählen nicht als Vision-Items (Abschnitt „Reservierte Vision-Items ohne
Inhalt"). *Korrigiert am 2026-07-20: die Vorfassung nannte hier „zwei" und ließ **VIS-014** aus,
obwohl `docs/ID-REGISTRY.md` §8 Punkt 38 es seit dem 2026-07-20 als reserviert führt und
`docs/traceability.md` es an fünf Stellen als Anker von REQ-041 nennt. Eine Zählung, die eine
reservierte ID übergeht, meldet weniger Lücken, als es gibt.*

## Target Group

- Primär: Freizeit-Läufer:innen und Radfahrer:innen mit 1–4 Aktivitäten pro Woche.
- Sekundär: ambitionierte Ausdauersportler:innen mit Strecken-, Sensor- und Leistungsfokus.
- Organisationen: Laufgruppen, Radsportgruppen und Vereine, die ein lokales digitales Zuhause benötigen.

### Persona-Referenz USER-004 (Nachzug 2026-07-19) — **unbestätigt**

Diese Vision **referenziert** Personas, sie definiert sie nicht. Kanonische Definitionsdatei aller
`USER-`IDs ist `docs/prd/revyr-endurance-platform.prd.md`; kanonisches ID-Register ist
`docs/ID-REGISTRY.md`, Abschnitt 6.12. Bei Abweichung gelten Register und PRD.

| ID | Persona | Source Type | Vision-Bezug |
|---|---|---|---|
| USER-004 | Ambitionierte Ausdauersportler:innen mit Wearables oder externen Sensoren | **ASSUMPTION — NOCH NICHT BESTÄTIGT** | zweiter Aufzählungspunkt oben (sekundäre Zielgruppe); Board-Zelle VIS-002 („sekundär ambitionierte Sportler:innen") |

**Beschreibung** (wörtlich aus der Nutzerentscheidung vom 2026-07-19, unverändert übernommen):

> Läufer:innen und Radfahrer:innen, die regelmäßig trainieren, bereits eine Sportuhr, einen
> Herzfrequenzgurt oder Fahrradsensoren verwenden und erwarten, dass vorhandene Trainingssignale
> ohne Medienbruch in ihre Aktivitäts- und Belastungsauswertung einfließen.

**Warum diese Persona entstanden ist.** Der Canvas führt die Zielgruppe als `CAN-025`
(„Ambitionierte Ausdauersportler:innen"), das PRD kannte jedoch nur `USER-001…003`.
`docs/traceability.md` vermerkte den Bruch bei REQ-009, REQ-011 und REQ-032 als „ambitionierte
Persona MISSING im PRD". Die ID `USER-004` wurde in Phase 1 vor der Vergabe im gesamten Repository
als **frei geprüft** und **nicht** ungeprüft aus der Anweisung übernommen (`docs/ID-REGISTRY.md`
§6.12).

**Warum `ASSUMPTION` und nicht `EXPLICIT`.** Der Wortlaut stammt aus einer Entscheidung über die
Formulierung, nicht aus einer belegten Quelle. Die Quellen `SRC-001`/`SRC-003`, auf die sich
USER-001…003 stützen, sind laut `docs/SOURCE-MAP.md` **nicht im Repository auffindbar (BLOCKER)** —
sie taugen deshalb auch hier nicht als Beleg. Bis zur ausdrücklichen Bestätigung der Persona bleibt
der Source Type `ASSUMPTION` (`docs/ID-REGISTRY.md` §8, Punkt 22).

**Ausdrücklich nicht mitentschieden.** `REQ-009` und `REQ-011` werden erst noch **semantisch**
darauf geprüft, ob sie zu USER-004 gehören. Diese Vision nimmt die Prüfung nicht vorweg und stellt
**keine** Universalverknüpfung her (`docs/ID-REGISTRY.md` §8, Punkt 23). Primär verankert ist
USER-004 bislang an REQ-032, zusammen mit CAN-022 — der dritte von der Nutzerentscheidung verlangte
Anker fehlt (nächster Abschnitt).

**Offen (BLOCKER, nicht von hier aus behebbar).** Die kanonische Persona-**Zeile** in
`docs/prd/revyr-endurance-platform.prd.md` (Tabelle USER-001…003, dort Zeilen 32–34) ist noch
**nicht** ergänzt, und `docs/prd/…prd.md:793` führt weiterhin „CAN-025 … hat im PRD **keine
USER-ID**" als Canvas-BLOCKER. Beides liegt außerhalb der Ownership dieser Datei; der Nachzug ist
dem PRD-Owner zugewiesen (`docs/ID-REGISTRY.md` §7.4). Solange er aussteht, ist USER-004 hier
referenziert, aber im PRD nicht definiert — eine Abdeckungsprüfung, die allein diese Referenz
zählt, meldet eine Deckung, die es im PRD nicht gibt.

## User Needs

1. Aktivitäten zuverlässig aufzeichnen und wiederfinden.
2. Belastung und Fortschritt verständlich statt als Blackbox interpretieren.
3. Run und Bike als gleichwertige, aber metrisch getrennte Sportwelten nutzen.
4. Anschluss an lokale Sportler:innen und Teams finden. *(korrigiert 2026-07-20: die Vorfassung
   lautete „Lokale Trainingspartner und Gruppen **sicher** finden." — „Trainingspartner", „Zugang"
   und der Qualifizierer „sicher" bezogen auf den Kontakt zu Personen sind in keiner der vier
   Quellen belegt; siehe Abschnitt „Verengung von VIS-003".)*
5. Verdienten Status und langfristige Historie aufbauen.

## Product Value

- **Health:** nachvollziehbare Auswertung mit Datenbasis und Unsicherheit.
- **Progression:** Belohnung realer Leistung ohne Kauf-Boosts.
- **Community:** Mechaniken, die reale gemeinsame Aktivitäten belohnen.
- **Territory:** späteres lokales Spielfeld, erst nach Anti-Cheat-, Geo- und Privacy-Gates.

## Business or Project Goals

- Einen stabilen, store-konformen Tracker als eigenständig nutzbares Produkt veröffentlichen.
- Retention zunächst über Health-Verständnis und Trainingsnutzen statt über Social-Zwang erzeugen.
- Community- und Territory-Funktionen nur auf belastbarer Daten- und Safety-Grundlage aufbauen.
- Eine Architektur schaffen, die Run und Bike ohne doppelte Produktlogik unterstützt.

## Success Signals

| Phase | Signal | Ziel | Source Type |
|---|---|---:|---|
| A | W4-Retention aktiver Tracker-Nutzer | > 30 % | EXPLICIT |
| A | Stimmungs-Check-in nach Aktivität | > 50 % | EXPLICIT |
| A | Öffnen der Score-Erklärung | > 25 % | EXPLICIT |
| B | Übernommene Routen pro Empfehlung | > 1,0 | EXPLICIT |
| C | Nutzer in einem Team nach 60 Tagen | > 25 % | EXPLICIT |
| C | Teams mit realer gemeinsamer Aktivität pro Woche | > 40 % | EXPLICIT |
| D | Season-Teilnahme aktiver Teams | > 60 % | EXPLICIT |

## Accessibility Boundary (VIS-011) — neu am 2026-07-19, **unbestätigt**

> ⚠️ **Dieses Vision-Item ist neue Produktsubstanz und vom Nutzer nicht bestätigt.**
> Es wird sichtbar als `ASSUMPTION` geführt und darf bis zur ausdrücklichen Bestätigung **nicht**
> als erfüllter Vision-Anker für **REQ-037** gezählt werden (`docs/ID-REGISTRY.md` §8, Punkt 15).

**Geltungsbereich nach der Zerlegung von REQ-014 (Nachzug 2026-07-19).** REQ-014
(„Designsystem und Accessibility") ist **deprecated** und in zwei atomare Anforderungen zerlegt:

| Nachfolger | Aussage | Vision-Anker |
|---|---|---|
| **REQ-037** — Accessibility | WCAG 2.2 AA; Schriftgrößen, Screenreader, Fokusführung, Kontraste, Bedienflächen auf iOS **und** Android nachgewiesen; Farbe nie einziger Informationsträger | **VIS-011** (dieses Item) — `ASSUMPTION`, unbestätigt |
| **REQ-038** — Monochromes tokenbasiertes Designsystem | Farbe nur mit fachlicher Bedeutung: Health-Status, Team-/Revieridentität, Sportplatz-Gold, bestätigte Feiermomente | **VIS-012** — reserviert, Inhalt **MISSING** (BLOCKER) |

> **VIS-011 trägt ausschließlich REQ-037.** Es trägt **nicht** REQ-038. Das monochrome
> Designsystem ist eine Gestaltungsaussage, Zugänglichkeit eine Bedienbarkeitsschranke; sie werden
> mit verschiedenen Verfahren geprüft, an verschiedenen Gates nachgewiesen und können unabhängig
> voneinander scheitern. VIS-011 auf REQ-038 auszudehnen wäre exakt der Fehler, dessen Behebung
> dieses Item überhaupt erst ausgelöst hat: ein syntaktisch gültiger Anker mit falscher Bedeutung.

Weitere IDs des Nachzugs: `AC-014` → **AC-037** (Accessibility) und **AC-038** (Designsystem);
`EV-014` → **EV-037** und **EV-038**; `TRC-014` → **TRC-037** und **TRC-038**. Die Alt-IDs
REQ-014, AC-014, EV-014 und TRC-014 werden **nicht wiederverwendet**.

**Aussage.** Jeder ausgelieferte Screen muss ohne Farbunterscheidung, mit vergrößerter Schrift und
mit Screenreader vollständig bedienbar sein. Zugänglichkeit ist eine **Schranke, keine Quote** —
es gibt kein Prozentziel unterhalb vollständiger Abdeckung.

**Warum dieses Item entstanden ist.** REQ-014 (Designsystem und Accessibility) war in
`docs/traceability.md` an **VIS-009 (Privacy Boundary)** gehängt. Zwischen Datenschutz und
Zugänglichkeit besteht keine fachliche Überschneidung; die ID war syntaktisch gültig, las sich
plausibel und trug die falsche Bedeutung. Drei unabhängige Vorbefunde
(`docs/prd/…prd.md:554`, `docs/traceability.md:517`, `docs/traceability.md:1444`) hatten bereits
festgehalten, dass **kein** VIS-Item Accessibility abdeckt. Die Prüfung von VIS-001 … VIS-010 im
Auftau-Schritt bestätigt das; die Einzelbegründung je Item steht in `docs/ID-REGISTRY.md` §6.1.1.

**Warum `ASSUMPTION` und nicht `EXPLICIT`.** Der Inhalt ist aus dem damaligen REQ-014, AC-014 und
NFR-005 abgeleitet — heute **REQ-037** und **AC-037**. Das PRD führte REQ-014 als `EXPLICIT` mit
Quelle `SRC-003`. `SRC-003` ist laut `docs/SOURCE-MAP.md` **nicht im Repository auffindbar
(BLOCKER)** und taugt deshalb nicht als Beleg. Eine Anforderung auf REQ-Ebene macht eine Aussage
auf Vision-Ebene außerdem nicht automatisch zur bestätigten Produktabsicht: das sind zwei
getrennte Aussagen. Ohne Nutzerbestätigung bleibt es eine Annahme.

Die Zerlegung ändert daran nichts: **REQ-037 wird in `docs/ID-REGISTRY.md` §6.6 selbst als
`ASSUMPTION` geführt**, solange sein Wortlaut nicht ausdrücklich nutzerbestätigt ist (§8, Punkt 24).
Ein unbestätigtes Vision-Item und eine unbestätigte Anforderung bestätigen einander nicht.

**Was sich seit dem 2026-07-19 geklärt hat.** Zwei Punkte des ursprünglichen Textes sind durch die
Nutzerentscheidung vom selben Tag überholt und werden hier korrigiert statt stehen gelassen:

- Die **Canvas-Lücke ist geschlossen.** `CAN-099` ist nicht mehr `reserved`, sondern `active` und
  inhaltlich entschieden — und ab jetzt **ausschließlich Accessibility** (Item Type
  `CONSTRAINT` / `COMPLIANCE_CONTROL`, `measurement_type = COMPLIANCE_CONTROL`). Für das
  tokenbasierte monochrome Designsystem existiert mit **`CAN-141`** ein **eigenes** atomares
  Canvas-Item (Source Type `EXPLICIT`). Damit hat REQ-037 den Canvas-Anker CAN-099 und REQ-038 den
  Canvas-Anker CAN-141. `docs/ID-REGISTRY.md` §8, Punkt 3 ist insoweit erledigt.
- Die **WCAG-Fassung ist festgelegt:** **WCAG 2.2 AA**. Die frühere Feststellung „das PRD nennt
  ‚WCAG AA' ohne Versionsangabe" beschreibt den Altstand und ist nicht mehr der offene Punkt.

**Was weiterhin offen bleibt.**

- **Keine Rechtsgrundlage zitiert.** In keinem Artefakt steht, aus welcher Rechtsnorm sich die
  Verbindlichkeit von WCAG 2.2 AA ableitet. Die Fassung ist gewählt, nicht hergeleitet.
- **Release-Gates:** Accessibility-**Basis** ab `A0`, vollständiger **Audit** spätestens `A2` vor
  öffentlichem Store-Release. Der Audit selbst ist nicht terminiert.
- **`EV-037` steht auf `evidence_status = not-planned`** — für die Accessibility-Prüfung existiert
  noch kein Messkonzept. `owner` = MISSING (`OQ-002`), `reference_environment` = MISSING
  (`OQ-003`). Ohne benannten Owner und ohne definierte Referenzgeräte ist „auf iOS und Android
  nachgewiesen" nicht prüfbar formuliert.
- **`TRC-037` hat den Zeilenstatus `not-linked`** — nicht `linked`. Grund: VIS-011 ist
  `ASSUMPTION` und unbestätigt und zählt nicht als erfüllter Vision-Anker. Die Kette
  VIS-011 ↔ CAN-099 ↔ REQ-037 ↔ AC-037 ↔ EV-037 ist vollständig **benannt**, aber nicht
  **belegt**.
- **`TRC-038` hat den Zeilenstatus `broken`** — der Vision-Anker VIS-012 ist reserviert und
  inhaltlich MISSING. Die Lücke wird bewusst sichtbar geführt, statt REQ-038 an ein unpassendes
  VIS-Item zu hängen.

**Nachzug durch Phase 2/3** (nicht von hier aus geändert, andere Datei-Owner):
`docs/traceability.md` und `docs/prd/…prd.md` ersetzen REQ-014/AC-014/EV-014/TRC-014 durch die
Nachfolger-IDs und hängen den Accessibility-Teil von VIS-009 auf **VIS-011** um. VIS-009 selbst
bleibt unverändert gültig — es verliert nur einen Anker, der nie zu ihm gehörte.

## Reservierte Vision-Items ohne Inhalt (Nachzug 2026-07-19) — **BLOCKER**

Diese IDs wurden in Phase 1 **reserviert**, damit Phase 2/3 weder eine ID erfindet noch eine
Anforderung still an ein unpassendes Vision-Item hängt. Sie haben **keinen Inhalt**. Ein Inhalt
wird hier ausdrücklich **nicht** vergeben: eine Aussage auf Vision-Ebene wäre neue Produktsubstanz
und braucht eine Nutzerentscheidung. Sie stehen deshalb **nicht** im Vision Board oben und zählen
**nicht** als Vision-Items.

| ID | Status | Vorgesehene Aussage | Content | Source Type | Betroffene Anforderung |
|---|---|---|---|---|---|
| VIS-012 | `reserved` | Designprinzip auf Vision-Ebene (monochromes, tokenbasiertes Designsystem; Farbe nur mit fachlicher Bedeutung) | **MISSING** — Vorschlag mit Fundstelle unten, **nicht eingesetzt** | **MISSING** | REQ-038 hat **keinen** Vision-Anker |
| VIS-013 | `reserved` | Datenportabilität auf Vision-Ebene (Nutzer können ihre Aktivitätsdaten in einem offenen Format mitnehmen) | **MISSING** — Fundstelle vorhanden, aber auf **Compliance-Ebene**; siehe unten | **MISSING** | REQ-039 (GPX-Export) hat **keinen** Vision-Anker |
| **VIS-014** *(nachgetragen 2026-07-20)* | `reserved` | Wiederverwendung geplanter Strecken auf Vision-Ebene | **MISSING** — auf Vision-Ebene **nicht belegbar**; siehe unten | **MISSING** | REQ-041 hat **keinen** Vision-Anker |

### Quellenprüfung der drei reservierten Items (2026-07-20) — **kein Item gefüllt**

Die vier Quelldokumente sind seit dem 2026-07-20 lesbar. Sie wurden gegen die drei reservierten
Items geprüft. **Das Ergebnis ist für alle drei verschieden** — und das ist der Punkt: eine
einheitliche Antwort wäre hier das Warnzeichen gewesen. **Es wird kein Item gefüllt, keine VIS-ID
vergeben und kein Status geändert.** Der Blocker bleibt in allen drei Fällen bestehen; was sich
ändert, ist seine *Art*.

| ID | Ergebnis der Quellenprüfung | Blocker-Art danach |
|---|---|---|
| **VIS-012** | **Wortlaut auf oberster Ebene vorhanden.** SRC-003 führt „**# 2. Design-System: Schwarz-Weiß, futuristisch, sportlich-spielerisch**" als eigenen Hauptabschnitt und eröffnet ihn mit: *„**Designprinzip: ‚Farbe muss man sich verdienen.'** Die App ist konsequent monochrom — Farbe existiert nur, wo sie Bedeutung trägt …"*. SRC-003 §11 führt es zusätzlich als **entschieden** (`✅ Schwarz-Weiß, „Farbe muss man sich verdienen"`). Damit ist es keine Feature-Aussage, sondern ein **produktweites Prinzip** | „**noch nicht entschieden**" — nicht mehr „inhaltlich nicht ableitbar" |
| **VIS-013** | **Wortlaut vorhanden, aber auf der falschen Ebene.** Der einzige Beleg ist SRC-003 §8, Zeile der Store-Readiness-Matrix: *„\| Datenexport \| A/2.8 \| **GPX-Export erfüllt Portabilität** \| dito \|"*. Ergänzend SRC-001 §3.5 (NFR Privacy/DSGVO: „…, **Datenexport**, …") und SRC-002 §10. **Alle drei sind Compliance-Anforderungen, keine Produktzusage.** Das Wort „Portabilität" kommt in allen vier Quellen **genau einmal** vor — in einer Store-Matrix | „**Ebenensprung, vom Nutzer zu entscheiden**" — der Satz ist zitierbar, seine Beförderung auf Vision-Ebene ist es nicht |
| **VIS-014** | **Auf Vision-Ebene nicht belegbar.** Die Wiederverwendung steht ausschließlich funktional: SRC-001 **T-05** „Verlauf (Liste/Detail), **Routen speichern/wiederverwenden**, Streckenrekord-Vergleich" (Teil 3 PRD). Auf Identitätsebene existiert nur eine **Zielgruppen**-Beobachtung: SRC-003 §1.3 „Radfahrer/Rennradfahrer: längere Distanzen, **feste Stammstrecken**, Sensorik, Gruppenausfahrten" und SRC-001 §3.3 (Persona Markus) „feste Stammstrecken". **Das beschreibt eine Eigenschaft der Zielgruppe, nicht eine Zusage des Produkts** | unverändert „**inhaltlich nicht ableitbar**" |

**Vorgeschlagener Wortlaut für VIS-012 — Vorschlag, nicht Inhalt.** Er steht hier bewusst
außerhalb der Tabelle oben und **außerhalb** des Vision Boards, damit ihn keine maschinelle Prüfung
als gesetzt liest:

> *Die Oberfläche ist konsequent monochrom. Farbe existiert nur dort, wo sie fachliche Bedeutung
> trägt, und wirkt dadurch wie eine Belohnung — „Farbe muss man sich verdienen".*
>
> Quelle: SRC-003 §2 (Eröffnungsabsatz), bestätigt in SRC-003 §11 („Design | ✅").
> `source_type` wäre **EXPLICIT | SRC-003**. **Status: unbestätigt — Nutzerentscheidung.**

⚠️ **Sachkorrektur zu einer früheren Formulierung.** Eine Vorfassung dieses Befunds beschrieb
SRC-003 §2 als „Designprinzip auf oberster Ebene **samt abschließender Farbliste**". Das ist
falsch und darf nicht übernommen werden: der **Eröffnungsabsatz** von §2 nennt **drei**
Bedeutungsfarben (Teamfarben, Health-Status, Feier-Momente). Die **abschließende** Liste steht eine
Ebene tiefer in **§2.1** („Bedeutungsfarben (**einzige Ausnahmen**)") und nennt **fünf**: Teamfarben,
Einzel-Revier-Farben, **Gold** für Sportplatz-Challenges, Health-Ampel, Feier-Momente. Wer §2 als
abschließend zitiert, verliert zwei Bedeutungsfarben — darunter Gold, das SRC-001 (G-12, R-01) als
reservierte Bedeutungsfarbe führt. **Der obige Vorschlag nennt deshalb bewusst keine Farbliste;**
die Liste gehört auf Canvas-/Requirement-Ebene, wo sie vollständig geführt werden kann.

**Warum für VIS-013 und VIS-014 kein Wortlaut vorgeschlagen wird.** Bei VIS-012 ist die
Vision-Ebene die Ebene der Quelle. Bei VIS-013 läge zwischen Fundstelle (Store-Compliance) und
Ziel (Produktzusage) ein Ebenensprung, bei VIS-014 zwischen Zielgruppen-Eigenschaft und
Produktzusage ebenso. **Einen solchen Sprung stillschweigend zu vollziehen ist genau der
wiederkehrende Defekt** — eine Formulierung, die plausibel liest, deren Quelle die Aussage aber
nicht trägt. Beide brauchen eine Nutzerentscheidung, keinen Formulierungsvorschlag.

**Warum kein bestehendes Item einspringt.** Für **VIS-013** wurden alle bestehenden Items geprüft:
`VIS-003` (User Need) nennt Tracking, Auswertung der Belastung, Fortschritt und Anschluss an lokale
Sportler:innen und Teams — **keine** Portabilität *(Wortlaut am 2026-07-20 verengt; die Prüfung
bleibt gültig, sie wird durch den engeren Wortlaut nur eindeutiger)*; `VIS-009` (Privacy Boundary)
regelt **Sichtbarkeit** und Werbenutzung, nicht
**Mitnahme**. Sichtbarkeitskontrolle und Datenmitnahme sind verschiedene Zusagen. `REQ-034`
verknüpft den Export nur **sekundär** als Constraint (Nutzerkontrolle, Datenminimierung) und trägt
die Capability nicht. Für **VIS-012** gilt die Prüfung aus `docs/ID-REGISTRY.md` §6.1.1: sie fand
für **keine** der beiden Hälften von REQ-014 einen Anker; VIS-011 wurde nur für die
Accessibility-Hälfte angelegt.

## Verengung von VIS-003 (2026-07-20) — Qualifizierer „verlässlich" und „sicher" abgetrennt

Die vier Quelldokumente liegen seit dem 2026-07-20 im Repository (`docs/sources/`). VIS-003 wurde
Klausel für Klausel gegen sie geprüft. **Zwei Qualifizierer halten der wortnahen Prüfung nicht
stand.** Sie werden aus dem Kern herausgenommen und sichtbar als `ASSUMPTION` weitergeführt — sie
werden **nicht** gelöscht und **nicht** stillschweigend ausgetauscht.

**Vorher:** *„Nutzer benötigen **verlässliches** Tracking, verständliche statt abstrakte
Health-Auswertung, konkrete **Fortschrittssignale** und einen **sicheren Zugang zu lokalen
Trainingspartnern**."*

**Nachher:** *„Nutzer benötigen Tracking ihrer Aktivitäten, eine verständliche statt abstrakte
Auswertung ihrer Belastung, spürbaren Fortschritt über die Zeit und Anschluss an lokale
Sportler:innen und Teams."*

| Klausel | Ergebnis | Beleg bzw. Abwesenheitsbefund |
|---|---|---|
| Tracking | **Kern belegt, Qualifizierer nicht** | `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md:64` „**Runner/Jogger:** tracken, Leistung verstehen …". „verlässlich" hat in allen vier Quellen **0 Treffer**. Nächstliegend sind zwei NFR-Zeilen — `SRC-001:250` „Distanzabweichung < 3 % auf bekannter Referenzstrecke" und `SRC-001:252` „Kein Datenverlust bei App-Kill/Absturz während Tracking (Recovery-Pflicht)". Das sind **Produktanforderungen**, keine Aussagen über ein Nutzerbedürfnis; der Schritt „Qualitätsanforderung ⇒ Nutzer benötigt diese Qualität" ist ein Ebenensprung. `SRC-001:18` sagt ausdrücklich, dass bestehende Apps das Aufzeichnen leisten („Bestehende Apps zeichnen das auf — mehr nicht") — ein Zuverlässigkeitsdefizit wird als Nutzerproblem gerade **nicht** behauptet |
| verständliche statt abstrakte Auswertung | **vollständig belegt, unverändert tragend** | `SRC-001:47` „Bestehende Tracker liefern Zahlen ohne Bedeutung (Was heißt „Belastung 82"?) … **Ich verstehe meinen Fortschritt nicht**"; `SRC-003:45` „Tracking + **verständliche Belastungsanalyse**"; `SRC-001:136` „**Kernbedürfnis:** erklärte Auswertung + lokales Team in ihrer Pace" |
| Fortschritt | **Substanz belegt, Begriff „Signale" nicht** | `SRC-001:21` „**Spürbaren Fortschritt** — Punkte, Ränge, Avatare, Seasons"; `SRC-001:47`. „Fortschrittssignal" hat **0 Treffer**; „Signal" kommt nur als Geschäfts-Kennzahl (`SRC-001:102` „Erfolgssignale") und als Anti-Cheat-Begriff (`SRC-003:715`) vor. Nur die **Formulierung** wurde ersetzt, nicht die Aussage |
| Anschluss an lokale Sportler:innen und Teams | **Kern belegt, Qualifizierer „sicher" nicht** | `SRC-001:51` „trainieren heute allein und **wünschen sich Anschluss**"; `SRC-001:26` „**findet ein offenes Team** in seiner Pace-Klasse — und läuft am Samstag nicht mehr allein"; `SRC-001:14` „**dich mit den Sportlern deiner Umgebung verbindet**"; `SRC-001:136`. „Trainingspartner" und „Zugang" haben je **0 Treffer** |

**Warum „sicher" nicht trägt.** Das Wort kommt in den vier Quellen **zwölfmal** vor
(`SRC-001:196, 202, 255` · `SRC-002:65, 108` · `SRC-003:59, 80, 132, 149, 383, 602, 705`). **Keine
dieser zwölf Stellen qualifiziert den Zugang zu Personen.** Sie betreffen UGC-Moderation, eine
farbenblind-sichere Farbpalette, Auth-Security, Sturzerkennung, Claims-Absicherung und das
Freigabe-Sicherheitsmodell für den Standort. Die frühere Fassung stützte die Klausel auf die
Zusammensetzung mehrerer getrennter Fundstellen. Genau das ist die Ableitung über ein Zwischenglied
(„weil es Schutzmechanismen um Social-Funktionen gibt, ist der Zugang zu Partnern sicher") — sie
steht in keiner Quelle und ist derselbe Defekttyp, den dieses Repository bei „Feed =
Entdeckungsfläche" bereits verworfen hat. **Neu und wesentlich:** dieser Maßstab war bisher nur auf
die *Ableitungen* aus VIS-003 angewandt worden, nie auf seine *Definition*.

> ⚠️ **Präzisierung gegenüber einer schärferen Vorfassung des Befunds (Beleglinse).** Es wäre
> **falsch** zu sagen, die Quellen verbänden Sicherheit überhaupt nicht mit sozialem Kontakt. Sie
> führen sehr wohl eine Schutzarchitektur: `SRC-001:36` „Profile standardmäßig privat";
> `SRC-003:374` „privates Profil → „**Follower-Anfrage**" mit Annehmen/Ablehnen … **Blockieren**
> wirkt beidseitig sofort überall"; `SRC-003:524` „Blockierter findet Nutzer nirgends";
> `SRC-001:196` UGC-Sicherheit. Eine Follower-Anfrage **ist** eine Zugangskontrolle zu einer
> Person. Was fehlt, ist ausschließlich die **Bedürfnis**-Formulierung: die Quellen führen den
> Schutz als Produkt-Leitplanke, funktionale Anforderung oder Risiko-Mitigation, an keiner Stelle
> als Nutzerbedürfnis. `SRC-001:47` zählt die Nutzerprobleme abschließend auf — „Ich verstehe
> meinen Fortschritt nicht · Ich habe niemanden · Es gibt kein Ziel außer mir selbst" — Sicherheit
> ist keines der drei. **Der Befund bleibt; seine Reichweite ist enger, als die Vorfassung
> behauptete.** Ebenfalls berichtigt: `SRC-001:98` (Live-Standort) wurde in der Vorfassung als
> „sicher"-Fundstelle geführt und enthält weder „sicher" noch „Sicherheit"; die Zuordnung lief über
> die Überschrift `SRC-001:94` „Gesundheits- & Safety-Grenzen".

**Konkurrierender Wortlautvorschlag — Vorschlag, nicht Inhalt.** Die Gegenprüfung unter der
Übermaßlinse hält den oben eingesetzten Kern für **zu eng** und schlägt eine Schlussklausel vor:

> *„… spürbaren Fortschritt über die Zeit sowie Anschluss an lokale Sportler:innen und Teams **bis
> hin zu gemeinsamem Training und realen Treffen**."*
>
> Belege der Ergänzung: `SRC-001:22` „**Echte Gemeinschaft** — Teams, die **zusammen trainieren,
> sich real treffen** und gemeinsam ihr Revier verteidigen"; `SRC-001:47` „keinerlei Grund, **sich
> real zu treffen**"; `SRC-001:26` „finden, messen und **treffen** … läuft am Samstag nicht mehr
> allein"; `SRC-003:64` „**gemeinsam laufen**"; `SRC-001:136` „**nicht mehr allein laufen**".
> **Status: unbestätigt — Nutzerentscheidung.**

Der Vorschlag ist **nicht eingesetzt**, weil er Produktsubstanz hinzufügt, die der bisherige
Wortlaut nicht führte, und der Auftrag dieses Laufs Verengung erlaubt, nicht Erweiterung. Er steht
hier, weil sein Einwand **sachlich trägt** und eine Folge hat, die nicht verschwiegen werden darf:
`docs/traceability.md:962` hat **VIS-004** als Anker von REQ-022 mit der Begründung verworfen, ein
Team sei „der Rahmen, in dem gemeinsam trainiert werden kann; **dass** gemeinsam trainiert wird,
steht dort nicht". Der hier eingesetzte Kern („Anschluss an lokale Sportler:innen und Teams") ist
materiell dieselbe Rahmenaussage. **Nach dem repo-eigenen Maßstab kann VIS-003 damit die gemeinsame
Aktivität von REQ-022 nicht mehr tragen** — es sei denn, der Nutzer setzt die Schlussklausel ein.
Der Traceability-Owner ist zuständig; von hier aus wird weder umgehängt noch VIS-004 umgedeutet.

**Folgen außerhalb dieser Datei — gemeldet, nicht ausgeführt.** Die Verengung wirkt auf Zeilen, die
anderen Ownern gehören. Sie werden hier benannt, damit die Wirkung nicht unbemerkt bleibt:

| Betroffen | Wirkung | Owner |
|---|---|---|
| `docs/traceability.md:426` (**TRC-004**) | Die Zeile benennt „verlässliches Tracking" als „**tragende Klausel wörtlich**" und beansprucht „Keine Schlusskette, sondern dieselbe Aussage". Mit der Abtrennung entfällt diese Klausel; der verengte Kern deckt eine Aussage über Tracking-**Qualität** nicht. Die Zeile **bricht** — sie ist nicht nur „berührt". REQ-004 liegt auf **GATE-A0** (`docs/traceability.md:194`), es entsteht dort ein **neuer Vision-Anker-BLOCKER** | Traceability |
| `docs/traceability.md:372` (TRC-002), `:545` (TRC-008) | Zitieren den VIS-003-Wortlaut vollständig, **ohne** eine tragende Klausel zu benennen — reiner Textnachzug, kein Bruch | Traceability |
| `docs/traceability.md:961/976`, `docs/ID-REGISTRY.md:846` (**TRC-022**) | Begründen den Anker wörtlich mit „die Klausel ‚sicherer Zugang zu lokalen Trainingspartnern'". Dieser Wortlaut existiert nicht mehr. Siehe den Absatz zum konkurrierenden Vorschlag | Traceability / Registry |
| `docs/traceability.md:232` (TRC-042) | Klausel „Fortschrittssignale"; bereits als ungeprüfte ASSUMPTION markiert | Traceability |
| `docs/canvas/…canvas.md:422`, `docs/ID-REGISTRY.md:390`, `docs/prd/…prd.md:1513` (**CAN-017**) | Die Prämisse „VIS-003 nennt ‚sicheren Zugang', der Canvas nennt kein Sicherheitsproblem — Canvas/Vision-Divergenz" verliert ihre Formulierungsgrundlage. **CAN-017 ist deshalb nicht aufzulösen**: sein Gegenstand hat eine eigene Quellenbasis — `SRC-003:704` „Live Location = Stalking-Risiko" und `SRC-003:713` „Einzel-Reviere verraten Wohngebiet/Lauf-Routine". Der BLOCKER bleibt stehen, nur der Prämissentext ist umzuhängen | Canvas / Registry / PRD |
| `docs/canvas/…canvas.md:163` (CAN-031 „Trainiere sicherer"), `:160` (CAN-028 „Verlässliches Tracking") | Beide sind aktiv und tragen dieselben Qualifizierer, beide als `ASSUMPTION`. Damit ist die Diagnose **nicht** „die Vision hat ‚sicher' erfunden", sondern: **zwei Artefakte tragen denselben unbelegten Qualifizierer in verschiedenen Slots**. Die Nutzerentscheidung zu „sicher" ist gemeinsam für VIS-003 und CAN-031 vorzulegen, sonst wird derselbe Defekt an einer Stelle behoben und an der anderen konserviert. Nach der Verengung entsteht zudem eine **Divergenz in Gegenrichtung**: der Canvas verspricht „Verlässliches Tracking" als Wert, die Vision nennt es nicht mehr als Bedürfnis | Canvas |

**Was hier ausdrücklich nicht geschieht.** Es wird **keine** VIS-ID vergeben, **kein** Vision-Item
umgedeutet, **nichts** hochgestuft und **kein** bestehender Blocker entfernt. Der Gesamtstatus
bleibt `BLOCKED_TRACEABILITY`. Die Herabstufung betrifft ausschließlich die beiden benannten
Qualifizierer; die Aussage von VIS-003 im Übrigen bleibt bestehen.

**Decision-Record-Verknüpfung 2026-07-20 (Runde 6).** Die hier dokumentierte Verengung von VIS-003
— EXPLICIT für den verengten Kern, ASSUMPTION für die abgetrennten Qualifizierer „verlässlich" und
„sicher" — ist als **DEC-014** in `docs/decisions/decision-log.md` protokolliert. Die
EXPLICIT-Aussage in der Vision-Tabelle (Zeile 18) verweist damit auf einen dauerhaften
Entscheidungssatz; Änderungen an dieser Verengung sind über DEC-014 zu führen, nicht am
Vision-Item selbst.

## VIS-003 trägt REQ-007 und REQ-019 nicht (Quellenprüfung 2026-07-20) — **BLOCKER**

`docs/traceability.md` hat am 2026-07-20 die Anker **VIS-003 ↔ REQ-007** (routenbezogener
Fortschritt) und **VIS-003 ↔ REQ-019** (Routenempfehlungen und Feed) entfernt. Der Befund wird
hier gespiegelt, weil **VIS-003 in dieser Datei definiert ist** — stünde er nur in der
Traceability-Matrix, bliebe hier ein Item stehen, das zwei Requirements zu tragen scheint.

**VIS-003 lautet seit der Verengung vom 2026-07-20:** Tracking der Aktivitäten · verständliche
statt abstrakte Auswertung der Belastung · spürbarer **Fortschritt über die Zeit** · **Anschluss an
lokale Sportler:innen und Teams**. Die Klauseln, auf die sich REQ-007 und REQ-019 beriefen, lauteten
in der Vorfassung „konkrete **Fortschrittssignale**" und „**sicherer Zugang zu lokalen
Trainingspartnern**". **Der Befund dieses Abschnitts wird durch die Verengung nicht abgeschwächt,
sondern verschärft:** REQ-007 und REQ-019 stützten sich auf Formulierungen, die inzwischen selbst
als nicht quellengedeckt abgetrennt bzw. ersetzt sind.

| Requirement | Beanspruchte Klausel (Vorfassung) | Warum sie nicht trägt |
|---|---|---|
| **REQ-007** | „konkrete **Fortschrittssignale**" — heute „spürbarer Fortschritt über die Zeit" | Die Quellen gebrauchen „Fortschritt" durchgehend **longitudinal**: SRC-001 §1.2 („**Spürbaren Fortschritt** — Punkte, Ränge, Avatare, Seasons"), §2.1 („Ich verstehe meinen **Fortschritt** nicht"), §3.3 („will verstehen, **ob sie sich verbessert**"), SRC-003 §1.1 („Challenges & Spiel — **Fortschritt**, Seasons, Areale"). REQ-007 misst den Fortschritt **innerhalb einer laufenden Aktivität**. Dieser erscheint in den Quellen ausschließlich **funktional** — SRC-001 **T-02** „geplante vs. verbleibende km", SRC-003 §9 GATE A „verbleibende km korrekt" — **nie auf Vision-Ebene**. Die Verengung macht das explizit: der neue Wortlaut sagt „über die Zeit" und schließt die aktivitätsinterne Lesart aus, die den entfernten Anker überhaupt erst ermöglicht hatte |
| **REQ-019** | „sicherer **Zugang zu lokalen Trainingspartnern**" — Klausel in dieser Form **entfallen** | Die Verbindung lief über ein eingefügtes Zwischenglied: „ein Feed ist die **Entdeckungsfläche** für diesen Zugang". Das Wort steht in **keiner** Quelle. VIS-003 spricht vom Anschluss an **Personen**, REQ-019 von der Empfehlung von **Strecken**. Vollständige Prüfung der Vision-Ebene (SRC-001 Teil 1 §1.1–§1.4; SRC-003 §1.1–§1.3) ergibt **keine** Aussage zu Empfehlung oder Feed. Nächster Kandidat SRC-003 §1.3 „Runner/Jogger: … **Strecken entdecken** …" — benennt ein Bedürfnis der Zielgruppe, nicht ein empfehlungsbasiertes Produktverhalten. **Zusätzlich seit dem 2026-07-20:** die beanspruchte Klausel existiert im Wortlaut nicht mehr — „Zugang" und „Trainingspartner" haben in allen vier Quellen 0 Treffer |

**Wo der Inhalt von REQ-019 tatsächlich steht.** SRC-001 **§2.5** *Social Loop* beschreibt ihn
nahezu wörtlich, SRC-003 **§4.2** spezifiziert ihn vollständig. Beide liegen auf **Canvas- bzw.
Systemspezifikations-Ebene** — SRC-001 §2 trägt die Überschrift „TEIL 2 — PRODUCT CANVAS". Der
Canvas-Anker CAN-058 ist damit belegt; **ein Vision-Anker entsteht daraus nicht.** Dass eine
Aussage in den Quellen *vorkommt*, macht sie nicht zu einer Vision-Aussage.

**Es wird kein Vision-Item angelegt und keines umgedeutet.** Für beide Aussagen ist — anders als
bei REQ-038/039/041 — **keine VIS-ID reserviert**. Der ID-Bedarf ist an den Registry-Owner
gemeldet; eine Nummer wird hier **nicht** genannt, die Registry ist eingefroren.

## Fehlender Vision-Anker für REQ-032 (Wearables und Bike-Sensorik) — **BLOCKER**

Die Nutzerentscheidung vom 2026-07-19 verlangt, REQ-032 primär an drei Anker zu hängen: an
**USER-004**, an **CAN-022** und an **ein Vision-Item zu vollständigen und erklärbaren
Trainingsdaten**. Die ersten beiden existieren. **Das dritte existiert nicht.**

**Prüfergebnis: kein bestehendes Vision-Item trägt diese Aussage.** Geprüft wurde, ob ein Item die
Aussage *trägt* — nicht, ob es sich plausibel darauf lesen lässt.

| Vision-Item | Aussage | Trägt „vollständige und erklärbare Trainingsdaten"? |
|---|---|---|
| VIS-001 | Produktvisionssatz | nein — Dachaussage ohne Aussage zur Datengrundlage; als primärer Anker einer einzelnen Anforderung zu unspezifisch |
| VIS-002 | Zielgruppe | nein — Zielgruppendefinition, keine Produkteigenschaft. **Trägt aber USER-004** (sekundäre Zielgruppe) |
| VIS-003 | User Need (Tracking, Auswertung der Belastung, Fortschritt, Anschluss an lokale Sportler:innen und Teams) | **nein — und seit dem 2026-07-20 aus einem zusätzlichen Grund.** Die Vorfassung begründete das „nein" damit, „verlässliches Tracking" meine die Zuverlässigkeit der **eigenen** Aufzeichnung, nicht die Übernahme **externer** Sensorsignale (dieselbe Falle wie bei REQ-014, §6.1.1). Diese Begründung stützte sich auf einen Qualifizierer, der inzwischen selbst als unbelegt abgetrennt ist. Sie wird deshalb ersetzt: der verengte Wortlaut nennt **Tracking der Aktivitäten ohne jede Qualifizierung** und sagt zur Herkunft der Signale **überhaupt nichts** — weder zur Vollständigkeit noch zur Übernahme externer Sensorik. Das „nein" trägt damit stärker als zuvor |
| VIS-004 | Product Value (u. a. „erklärbare Trainingsbelastung") | **nein, nächstliegender Kandidat** — deckt *erklärbar* ab, aber **nicht** *vollständig*, und sagt nichts über die Herkunft der Signale |
| VIS-005 | Project Goal („erst nach nachgewiesener Datenqualität Territory- und Live-Systeme freischalten") | **nein — und der derzeitige Anker ist damit fragwürdig** (siehe unten) |
| VIS-006 | Success Signals | nein — Retention- und Nutzungsquoten belegen Datenvollständigkeit nicht |
| VIS-007 | Health-first Boundary („Datenbasis, Gründe und Unsicherheit erklären") | **nein, trotz starker Anziehungskraft** — das Item verlangt, Lücken und Unsicherheit **offenzulegen**. Das ist der korrekte Umgang mit unvollständigen Daten, **nicht** die Zusage, dass die Daten vollständig sind. Die Aussagen sind komplementär, nicht deckungsgleich |
| VIS-008 | Fairness Boundary (getrennte Run/Bike-Metriken) | nein — Wertungsfairness, nicht Signalvollständigkeit |
| VIS-009 | Privacy Boundary | nein |
| VIS-010 | Delivery Principle | nein — Freigabereihenfolge |
| VIS-011 | Accessibility Boundary | nein |
| VIS-012 / VIS-013 / **VIS-014** | reserviert | **konstruktiv nein** — alle drei sind inhaltlich MISSING und können per Definition nichts tragen. *VIS-014 am 2026-07-20 ergänzt; die Vorfassung führte nur zwei.* |

**Nebenbefund zum bestehenden Anker.** `docs/traceability.md:112` führt TRC-032 mit der
Vision-Spalte **`VIS-005`**, und `docs/traceability.md:1374` verweist auf
`…vision.md#VIS-005`. VIS-005 sagt jedoch, dass Territory- und Live-Systeme **erst nach
nachgewiesener Datenqualität** freigeschaltet werden — eine **Freigabebedingung für eine spätere
Stufe**, keine Zusage über Vollständigkeit und Erklärbarkeit der Trainingsdaten. Der Anker ist
syntaktisch gültig und liest sich plausibel, trägt aber eine andere Bedeutung — derselbe Fehlertyp
wie VIS-009 ↔ REQ-014. Die Korrektur der Zeile liegt beim Traceability-Owner; **von hier aus wird
weder umgehängt noch VIS-005 umgedeutet.**

**Es wird hier kein Vision-Item angelegt.** Phase 1 ist abgeschlossen und die ID-Registry ist
eingefroren — nur Phase 1 vergibt IDs. Für diese Aussage wurde in Phase 1 **keine VIS-ID
reserviert**: `docs/ID-REGISTRY.md` §8, Punkt 21 führt sie als **MISSING** mit Owner **Nutzer**.

> ⚠️ **Beleg-BLOCKER, aufgefallen am 2026-07-20.** Die Vorfassung stützte diese Aussage auf ein
> zweites Bein: „*und `id-migration.json` enthält unter `new_ids` keinen entsprechenden Eintrag
> (reserviert wurden dort nur VIS-012 und VIS-013)*". **Diese Datei existiert im Repository nicht.**
> Geprüft am 2026-07-20: kein `id-migration.json` unterhalb des Repository-Wurzelverzeichnisses,
> und keine Datei enthält den Schlüssel `new_ids` (der Wurzelbaum umfasst `docs/`, `CLAUDE.md`,
> `README.md`, `intake-package.json`). Der Satz ist deshalb **entfernt und nicht ersetzt**.
> **Die Schlussfolgerung bleibt bestehen** — sie trägt über `ID-REGISTRY.md` §8 Punkt 21, der
> existiert und lesbar ist. Was entfällt, ist ein Beleg, **nicht** der Befund. Der Verweis war
> genau die wiederkehrende Defektklasse: eine Fundstellenangabe, die präzise klingt (Dateiname,
> Feldname, Aufzählung der Einträge) und deren Ziel es nicht gibt. **Owner des Nachzugs: wer immer
> `id-migration.json` erzeugt hat — die Datei ist entweder nie ins Repository gelangt oder sie
> wurde entfernt; beides ist von hier aus nicht entscheidbar und wird nicht vermutet.**

Eine benötigte, aber nicht migrierte ID ist nach der
ID-Disziplin ein **BLOCKER** — nicht ein Anlass, eine neue VIS-ID zu erfinden oder eines der Items
VIS-001 … VIS-011 stillschweigend umzudeuten. (Hier wird bewusst **keine** konkrete Nummer
genannt: die nächste freie VIS-ID vergibt ausschließlich der ID-Owner nach Auftauen der Registry.)

**Folge.** REQ-032 hat damit zwei seiner drei geforderten Primäranker (USER-004, CAN-022) und
**keinen gültigen Vision-Anker**. Solange das so ist, darf REQ-032 nicht als vollständig verankert
gezählt werden.

## Boundaries

- Kein Medizinprodukt und keine Diagnose.
- Kein Chat-Messenger und kein allgemeines soziales Netzwerk.
- Keine kaufbaren Leistungswerte, Boosts oder notwendigen Avatar-Items.
- Kein Territory, keine öffentliche Live-Map und keine Sturzerkennung vor den jeweiligen Safety-Gates.
- Der Arbeitstitel darf nicht ungeprüft in finale Bundle IDs, Domains oder öffentliche Store-Metadaten eingebrannt werden.

## Präzisierungen zu Datenhaltung und Historie (Nachzug 2026-07-19)

Dieser Abschnitt **referenziert** bestätigte Entscheidungen; er definiert sie nicht. Kanonisch
sind die genannten Dateien. Er ändert die Zellen VIS-001…VIS-010 oben nicht — deren Wortlaut ist
in `docs/ID-REGISTRY.md`, Abschnitt 6.1, als `title` gespiegelt und dort eingefroren.

### Local-first-Präzisierung

Kanonisch: `CAN-095` in `docs/canvas/revyr-endurance-platform.canvas.md`. Wörtlicher Wortlaut
der Nutzerentscheidung vom 2026-07-19:

> Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal. Für die
> Routenberechnung dürfen ausschließlich die erforderlichen Wegpunkte transient an einen
> kontrollierten Routing-Proxy übertragen werden. Der Proxy speichert keine Koordinaten oder
> Routengeometrien dauerhaft.

Das präzisiert VIS-009 (Privacy Boundary) und die Stufe A0, ersetzt sie aber nicht.

**Status nach dem verbindlichen Statusmodell** (`docs/ID-REGISTRY.md` §3.1; der frühere Mischwert
`DESIGN-RESOLVED / EVIDENCE-PENDING` ist als `status` unzulässig und am 2026-07-19 auf die zwei
Achsen aufgeteilt worden):

| Feld | Wert |
|---|---|
| `status` | `resolved` — die Grundsatzfrage ist entschieden |
| `resolution_status` | `accepted` |
| `evidence_status` | **`planned`** (korrigiert 2026-07-19, siehe unten) |
| `blocking` | `true` — **berechnet**, nie gelesen (Formel unten) |
| `blocked_gates` | `A0` |
| `blocked_activities` | `field-test`, `release` |
| `evidence_gate` | `A0` |
| `decision_reference` | `OQ-011`, `DEC-013`; „ADR zum A0-Routing-Proxy" = **MISSING**, existiert nicht |

**Feldmigration `blocking_scope` → `blocked_gates` + `blocked_activities` (2026-07-19).** Das Feld
`blocking_scope` ist projektweit **ersatzlos entfallen**. Es mischte Release-Gates und Tätigkeiten
in *einer* Liste; da beide Vokabulare disjunkt sind, lieferte die wörtliche Lesart für jeden
gegateten Eintrag `false` — die Blockade verschwand genau dann, wenn gegen ein Gate geprüft wurde.
Die kanonische Formel lautet:

```
blocking = (status != 'resolved')
        OR (resolution_status != 'accepted')
        OR (evidence_status IN ['failed','blocked'])
        OR (current_gate IN blocked_gates)
        OR (current_activity IN blocked_activities)
```

`current_gate` wird **ausschließlich** gegen `blocked_gates` geprüft, `current_activity`
**ausschließlich** gegen `blocked_activities`. Gate-Bezeichner in `blocked_activities` (oder
umgekehrt) sind ein Validierungsfehler, kein Toleranzfall. Die Alt-Werte `field-test` und `release`
sind beide Tätigkeiten und wandern nach `blocked_activities`; `blocked_gates` ist **neu** befüllt
und war vorher nicht darstellbar.

> ⚠️ **Ein reines Umbenennen behebt den Defekt nicht.** Solange irgendein Werkzeug die alte Formel
> anwendet, liefert es für gegatete Einträge weiterhin fälschlich `false`. Eine gemeinsame
> Implementierung der Blocking-Funktion existiert im Repository **nicht** (BLOCKER), und das Feld
> `blocking_scope` lebt außerhalb dieser Datei weiter — gemessen am 2026-07-19 in
> `docs/traceability.md` (20), `docs/prd/…prd.md` (14), `docs/decisions/decision-log.md` (9),
> `docs/validation/validation-report.md` (7) und `docs/EVIDENCE-LEDGER.md` (1). Diese Dateien
> haben andere Owner und wurden von hier aus nicht geändert.

**Warum `evidence_status = planned` und nicht `pending`.** Nach der projektweiten Semantik
(Nutzerentscheidung 2026-07-19) ist die Grenze zwischen `planned` und `pending` die
**Instrumentierung**, nicht die Absicht: `planned` = Metrik, Berechnung und zuständiges Gate sind
definiert, die Instrumentierung fehlt; `pending` = Instrumentierung implementiert, aber Messdaten
oder Messfenster fehlen noch. **In diesem Repository existiert kein Code** — es kann folglich
nichts instrumentiert sein, und ein Eintrag ohne Code steht höchstens auf `planned`. Der frühere
Wert `pending` war damit unvereinbar mit der Semantik und ist korrigiert.

> **BEFUND (nicht von hier aus behebbar).** Die Phase-1-Migration führt für `CONTRA-005` und
> `CONTRA-006` weiterhin `evidence_status = pending`. Das widerspricht der projektweiten Semantik
> derselben Phase. Diese Datei folgt der Semantik; die Angleichung von
> `docs/decisions/decision-log.md` und `docs/validation/validation-report.md` liegt bei deren
> Ownern. Der Widerspruch wird hier **gemeldet, nicht stillschweigend übernommen**.

`CONTRA-006` (`docs/decisions/decision-log.md`) ist damit **entschieden, aber nicht
nachgewiesen** — und bleibt blockierend für die A0-Routing-Implementierung. Offen bleibt der
Nachweis für Datenfluss, Providerbedingungen, Logging, Retention, Transparenz und
Sicherheitskontrollen. Ein Großteil dieser Evidence setzt lauffähigen Code voraus, der noch nicht
existiert. Bis dahin ist die Präzisierung eine Design-Zusage, keine belegte Eigenschaft.

### Formulierung „unveränderliche Historie“

Kanonisch: `CONTRA-005` in `docs/decisions/decision-log.md`. Grundsatzentscheidung des Nutzers
vom 2026-07-19. Die Formulierung „unveränderliche Historie“ wird projektweit ersetzt durch:

> Nach Finalisierung fachlich unveränderbar, außer aufgrund Löschung, Anonymisierung oder
> rechtlicher Korrektur.

Historische Team- und Season-Daten dürfen eine Accountlöschung nur überleben, wenn sie wirksam
anonymisiert sind und keine Rückführung auf die gelöschte Person mehr möglich ist. Ist wirksame
Anonymisierung nicht möglich, muss der Datensatz gelöscht werden. Datenmodell und Event-Historie
müssen Identität und historische Aggregate technisch trennen — **vor** Erstellung und
Finalisierung des Datenbankschemas.

Hinweis zum Geltungsbereich dieser Datei: Die Zeichenfolge „unveränderliche Historie“ kommt in
dieser Vision **nicht** vor (geprüft am 2026-07-19). Hier war also nichts zu ersetzen; der
Eintrag steht als Referenz auf die bindende Entscheidung. Die tatsächlichen Fundstellen liegen in
`docs/prd/revyr-endurance-platform.prd.md` (REQ-027), `docs/traceability.md`,
`docs/implementation/revyr-delivery-plan.md` und `docs/decisions/decision-log.md` — sie gehören
anderen Datei-Ownern und wurden von hier aus nicht geändert.

**Status nach dem verbindlichen Statusmodell** (`docs/ID-REGISTRY.md` §3.1): `status = resolved`,
`resolution_status = accepted`, **`evidence_status = planned`** (korrigiert, Begründung wie oben:
ohne Code keine Instrumentierung), `blocking = true` (berechnet), **`blocked_gates = B`**,
**`blocked_activities = database-schema-finalization, account-release`**, `evidence_gate = B`,
`decision_reference = DEC-012`. Die Entscheidung liegt vor, die Implementierungs-Evidence steht
aus.

**Korrektur 2026-07-19.** Die frühere Feststellung, für den Nachweis „Datenmodell trennt Identität
und historische Aggregate" existiere **keine EV-ID**, beschreibt den Altstand. Phase 1 hat dafür
**`EV-042`** reserviert (`docs/ID-REGISTRY.md` §6.8; zugeordnet zu CONTRA-005 / REQ-017 /
REQ-027). `docs/ID-REGISTRY.md` §8, Punkt 14 ist damit **als ID-Frage** geschlossen.

> **Geschlossen ist die ID, nicht der Nachweis.** EV-042 benennt den Nachweis, es erbringt ihn
> nicht. Die Trennung von Identität und historischen Aggregaten muss **vor** Erstellung und
> Finalisierung des Datenbankschemas belegt werden — `blocked_activities` enthält
> `database-schema-finalization` genau deshalb. Solange kein Datenmodell existiert, ist der
> Nachweis nicht führbar. Der Eintrag in `docs/EVIDENCE-LEDGER.md` (Marke (z)) ist noch
> nachzuziehen; die Datei hat einen anderen Owner.

## Assumptions

Kanonische ID-Quelle: `docs/ID-REGISTRY.md`, Abschnitt 6.9. Die Vision **referenziert** ASM-IDs,
sie vergibt keine.

| ID | Assumption | Source Type | Validation |
|---|---|---|---|
| ASM-201 | Eine gestufte öffentliche v1.0 aus A0/A1/A2 reduziert Risiko gegenüber einem einzigen überladenen MVP. | ASSUMPTION | Release- und Ressourcenschätzung |
| ASM-202 | Ein Health-Score mit sichtbarer Confidence ist verständlicher und rechtlich robuster als ein einzelner absoluter Score. | ASSUMPTION | Nutzer- und Claims-Test |
| ASM-203 | Der technische Slug kann vorläufig stabil bleiben, auch wenn der öffentliche Name wechselt. | ASSUMPTION | Repo-/Release-Entscheidung |

### ASM-Migration (Nachzug 2026-07-19)

Die alten IDs `ASM-001`…`ASM-003` dieser Datei sind **deprecated**. Sie kollidierten mit
gleichnamigen, fachlich völlig anderen Annahmen im PRD: `ASM-002` bezeichnete hier den
Health-Score mit Confidence, im PRD dagegen SQLite statt AsyncStorage. Ein Auftrag
„prüfe ASM-002“ hätte je nach gelesener Datei eine andere Annahme geprüft.

| Alt-ID (deprecated) | Neue ID | Bedeutung, die in dieser Datei gemeint war |
|---|---|---|
| ASM-001 | ASM-201 | Risikoreduktion durch gestufte v1.0 |
| ASM-002 | ASM-202 | Health-Score mit sichtbarer Confidence |
| ASM-003 | ASM-203 | Stabiler technischer Slug |

Die Nummern `ASM-001`…`ASM-003` werden **nicht** wiederverwendet. Die Vision-Annahmen liegen
ab jetzt im Bereich `ASM-2xx`, die PRD-Annahmen im Bereich `ASM-1xx`. Vollständige
Migrationstabelle inklusive Fundstellen: `docs/ID-REGISTRY.md`, Abschnitt 7.1.

## Missing Items

Kanonisches Register: `docs/decisions/open-questions.md`. Diese Vision **referenziert** OQ-IDs, sie definiert sie nicht. Bei Abweichung gilt das Register.

| ID | Item | Source Type | Impact |
|---|---|---|---|
| OQ-001 | Finaler öffentlicher Name und markenrechtliche Freigabe | MISSING | Blockiert öffentliche Store-/Domain-Festlegung, nicht die interne Produktplanung |
| OQ-002 | Finaler Owner/DRI im Repository | MISSING | Vor Umsetzung im Projekt-README benennen |
| OQ-007 | Geschäftsmodell und Preislogik | MISSING | Muss vor kostenintensiver Skalierung, spätestens vor v3, entschieden werden |

## Confirmation Status

`pending-user-confirmation`

Die Assistenz bestätigt diese Vision nicht im Namen des Nutzers.

**Ausdrücklich unbestätigt und gesondert vorzulegen:** `VIS-011` (Accessibility Boundary) ist am
2026-07-19 neu entstanden, weil das damalige REQ-014 an einem semantisch falschen Anker hing. Es
ist als **ganzes Item** unbestätigt. Solange der Nutzer es nicht bestätigt, zählt es **nicht** als
erfüllter Vision-Anker für **REQ-037** — eine Abdeckungsprüfung, die es mitzählt, meldet eine
Deckung, die es nicht gibt.

*Korrigiert am 2026-07-20:* Die Vorfassung nannte VIS-011 „die **einzige** Zeile des Vision Boards
mit `User Decision Needed = JA`". Das trifft seit der Verengung von VIS-003 nicht mehr zu. **VIS-003
trägt seither ebenfalls `JA`** — allerdings mit anderer Reichweite: bei VIS-011 ist das **ganze
Item** unbestätigt, bei VIS-003 nur die **abgetrennten Qualifizierer** „verlässlich" und „sicher";
sein verengter Kern bleibt `EXPLICIT` und tragfähig. Die beiden Zeilen dürfen nicht gleich gezählt
werden.

**Zur Nutzerentscheidung offen (Stand 2026-07-19).** Diese Datei legt vor, sie entscheidet nicht:

| Gegenstand | Art | Wirkung, solange offen |
|---|---|---|
| Bestätigung von **VIS-011** | BLOCKER | REQ-037 hat keinen belegten Vision-Anker; TRC-037 bleibt `not-linked` |
| Inhalt von **VIS-012** | BLOCKER | REQ-038 hat **keinen** Vision-Anker; TRC-038 bleibt `broken` |
| Inhalt von **VIS-013** | BLOCKER | REQ-039 (GPX-Export) hat **keinen** Vision-Anker |
| Inhalt von **VIS-014** *(2026-07-20 nachgetragen)* | BLOCKER | REQ-041 hat **keinen** Vision-Anker; TRC-041 bleibt `broken`. Fehlte in dieser Aufstellung, obwohl die ID seit dem 2026-07-20 reserviert ist |
| Abgetrennte Qualifizierer von **VIS-003**: „**verlässlich**" (Tracking) und „**sicher**" (Zugang) *(neu 2026-07-20)* | ASSUMPTION, **keine Quelle** für „sicher"; „verlässlich" nur auf NFR-Ebene | Beide sind aus dem Kern herausgenommen und als `ASSUMPTION` geführt. Folge: **TRC-004 bricht** — `docs/traceability.md:426` benennt „verlässliches Tracking" als tragende Klausel, REQ-004 liegt auf **GATE-A0**. „sicher" ist gemeinsam mit **CAN-031** („Trainiere sicherer") zu entscheiden, sonst wird derselbe unbelegte Qualifizierer an einer Stelle behoben und an der anderen konserviert |
| Schlussklausel „**bis hin zu gemeinsamem Training und realen Treffen**" in VIS-003 *(neu 2026-07-20)* | Vorschlag, **nicht eingesetzt** — wortnah belegt (`SRC-001:22`, `:26`, `:47`, `:136`; `SRC-003:64`) | Ohne sie kann VIS-003 nach dem repo-eigenen Maßstab (`docs/traceability.md:962`, VIS-004-Verwerfung) die gemeinsame Aktivität von **REQ-022** nicht mehr tragen. Einsetzen wäre Erweiterung, nicht Verengung — deshalb Nutzerentscheidung |
| Vision-Item zu **vollständigen und erklärbaren Trainingsdaten** | MISSING, **keine ID reserviert** | REQ-032 fehlt der dritte Primäranker; TRC-032 hängt weiter am unpassenden VIS-005 |
| Vision-Item zu **routenbezogenem Fortschritt** *(neu 2026-07-20, Runde 5)* | MISSING, **keine ID reserviert** | REQ-007: VIS-003 ist entfernt, TRC-007 steht auf `broken`. **ID-Bedarf an den Registry-Owner gemeldet; hier keine Nummer genannt** |
| Vision-Item zu **Routenempfehlung und Feed** *(neu 2026-07-20, Runde 5)* | MISSING, **keine ID reserviert** | REQ-019: VIS-003 ist entfernt, TRC-019 steht auf `broken`. **ID-Bedarf gemeldet; hier keine Nummer genannt** |
| Bestätigung von **USER-004** als Persona | BLOCKER | Persona bleibt `ASSUMPTION`; PRD-Zeile fehlt noch |
| Gehören **REQ-009** und **REQ-011** an USER-004? | OPEN QUESTION | ausdrücklich **keine** Universalverknüpfung — Prüfung ist semantisch und steht aus |
| Rechtsgrundlage für **WCAG 2.2 AA** | MISSING | Fassung ist gewählt, nicht hergeleitet |

Diese Vision ist damit **nicht** bestätigungsreif. Der Gesamtstatus des Vorhabens bleibt
`BLOCKED_TRACEABILITY`; `true-line-status` bleibt `pending-watcher`, `wired-in-prod` = `no`,
`evidence-class` = `none` (es existiert kein Code). Die Assistenz bestätigt nichts im Namen des
Nutzers und erklärt keine Planungsreife.
