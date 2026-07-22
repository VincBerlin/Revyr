# REVYR Risk Register

Stand: 2026-07-18  
Ergänzt: 2026-07-19 (fünf Risiken aus der serverseitigen Verarbeitung ab A0 sowie sechs Risiken
aus der Telemetrie-Erhebung für CAN-130 ab Stufe B — sämtlich **ohne RISK-ID**, siehe unten)  
Status: active – pending-user-confirmation

Die Zeile „Stand: 2026-07-18" bleibt unverändert stehen: `docs/ID-REGISTRY.md` §3 stützt ihre
`created_at`-Ableitung für RISK-001…RISK-024 ausdrücklich auf diesen Wortlaut. Die Ergänzung
vom 2026-07-19 vergibt keine neuen RISK-IDs und ändert den registrierten Bestand nicht.

| Risk ID | Risk | Severity | Phase | Mitigation | Status |
|---|---|---|---|---|---|
| RISK-001 | Background-GPS wird durch OS gedrosselt oder beendet | critical | A0 | Dev-Build früh, Foreground Service/Background Mode, Journaling, Kill-Tests | open |
| RISK-002 | GPS-Drift verfälscht Distanz und Route | high | A0 | erweitertes TrackPoint-Schema, Filter-Fixtures, Referenzstrecken | open |
| RISK-003 | Batterieverbrauch verhindert längere Nutzung | high | A0 | sportabhängiges Sampling und 1h-Messläufe | open |
| RISK-004 | Alte Run&Bike-Annahmen gelangen in neue Implementierung | high | P0 | alten Plan superseden, neutraler Slug, neue Architektur als einzige Quelle | open |
| RISK-005 | Bike zeigt falsche Laufmetriken | high | A0 | SportConfig, getrennte UI-/Domain-Tests | open |
| RISK-006 | Routenrest ist bei Abweichungen falsch | high | A0 | Polyline-Projektion, Hysterese, Off-Route-Fixtures | open |
| RISK-007 | Client-API-Key wird missbraucht | high | P0/A2 | Proxy oder eingeschränkte kurzlebige/public Strategie, Quoten | open |
| RISK-008 | Health-Score wird als medizinische Aussage verstanden | critical | A1/E | Confidence, Gründe, Claims-Whitelist, Rechtsprüfung | open |
| RISK-009 | Nutzer ohne HF-Hardware erhalten unbrauchbares Produkt | high | A1 | Fallback-Score und sichtbare Datenbasis | open |
| RISK-010 | Store lehnt Background-Location/Health/UGC ab | critical | A-D | frühe Testtracks, Policy-Matrix, ehrliche Permissions | open |
| RISK-011 | Namens-/Markenkollision | critical | A2 | neue Namensfindung und professionelle Prüfung vor öffentlichem Release | open |
| RISK-012 | Backend-Fehlentscheidung erzeugt Lock-in/Kosten | high | B | vergleichbarer Geo/Auth/Realtime-Prototyp und ADR | open |
| RISK-013 | Anti-Cheat produziert False Positives | high | C | mehrstufige Confidence, Review, Testdaten und Appeal-Flow | open |
| RISK-014 | Run/Bike-Effort ist unfair | high | C/D | Simulation, versionierte Faktoren und getrennte interne Rankings | open |
| RISK-015 | Standortfreigabe ermöglicht Stalking | critical | D | Threat-Model, Opt-in, Zeitlimit, Unschärfe, Block in Realtime | open |
| RISK-016 | Einzel-Reviere verraten Wohnort und Routine | critical | D | Follower-Default, Anonymisierung, Start-/End-Unschärfe, Retention | open |
| RISK-017 | Polygonoperationen sind inkonsistent oder langsam | high | D | PostGIS, Eventlog, Transaktionen, Geo-Fixtures, Spatial Index | open |
| RISK-018 | OSM-Sportplatz ist privat oder falsch | high | D | Access/Opening-Hours, Kuratierung, Meldesystem, Sperrliste | open |
| RISK-019 | Bahngold fördert gesundheitlich riskantes Grinding | high | D | Degression, Belohnungslimits, Health-Hinweise, keine Verlustmechanik | open |
| RISK-020 | Sturzerkennung erzeugt falsche Sicherheit | critical | D | Assistenzsprache, Countdown, Fehlalarmquote, kein Rettungsversprechen | open |
| RISK-021 | Moderationsaufwand skaliert nicht | high | B-D | Melden/Blockieren ab B, Queue, SLA, Kostenentscheidung vor C | open |
| RISK-022 | Sensitive Health-Daten werden unnötig serverseitig verarbeitet | critical | C/E | Datenminimierung, nur aggregierte Signale, DPIA/Privacy Review | open |
| RISK-023 | Scope wächst vor Nachweis der Kernretention | high | alle | Gates, Feature Flags, Territory nicht vor D | open |
| RISK-024 | User Confirmation wird fälschlich als erteilt angenommen | high | planning | Confirmation Status bleibt pending bis exakte Nutzerbestätigung | open |

## Neue Risiken aus der serverseitigen Verarbeitung ab A0

> **BLOCKER — ID-Vergabe nicht möglich.** `docs/ID-REGISTRY.md` ist ab Phase 2 eingefroren und
> reserviert **keine** RISK-ID über RISK-024 hinaus (Registry §6.8, Bestandsabgleich §10:
> „RISK | 24 | 24 aktiv"). Nach Registry-Regel 3 meldet ein Agent außerhalb Phase 1 eine
> fehlende ID als BLOCKER, statt sie zu erfinden. Die folgenden fünf Risiken sind daher
> **inhaltlich** erfasst, aber **ohne RISK-ID**. Die Marken (a)…(e) sind reine
> abschnittslokale Lesemarken, **keine IDs**. Sobald die Registry entfroren wird, sind hier
> echte RISK-IDs zu vergeben und die Zeilen in die Haupttabelle zu überführen.

Diese Risiken entstehen sämtlich aus DEC-005 (Routing-Proxy ab A0) und DEC-013
(A0-Privacy-Baseline). Vor dem 2026-07-19 existierte in A0 keine serverseitige
Verarbeitungsfläche — die Risikolage der Stufe A0 hat sich dadurch verändert und ist mit
RISK-001…RISK-024 nicht mehr vollständig abgebildet.

| Marke (keine ID) | Risk | Severity | Phase | Mitigation | Status |
|---|---|---|---|---|---|
| (a) | Koordinaten-Leak über Logs, Traces oder Fehlermeldungen — Standortrekonstruktion aus technischen Logs, obwohl die Koordinaten selbst nicht persistiert werden | critical | A0 | Body-Logging-Verbot, Allowlist zulässiger Logfelder (Request-ID, Zeitstempel, Status, Dauer, Profil, Wegpunktzahl, Fehlerkategorie, Provider-Latenz, Rate-Limit-Ereignis), normalisierte Fehlerantworten ohne Provider-URLs und Stack Traces, Logaufbewahrung max. 7 Tage, automatisierter Test gegen die Logausgabe | open |
| (b) | Routinganbieter verarbeitet außerhalb des EWR — die Bezeichnung „EU-Proxy" erzeugt eine unzutreffende Erwartung, obwohl nur Lambda/API Gateway in `eu-central-1` liegen | critical | A0 | Verarbeitungsregion, EWR-Übermittlung, Unterauftragsverarbeiter und Transfergrundlage vor erstem externem Feldtest dokumentieren (offene Punkte (a)…(d) in `docs/decisions/open-questions.md`); Sprachregelung für „EU-Proxy"; Anbieter ohne AVV nicht produktiv einsetzen | open |
| (c) | Secret-Leak des Provider-Keys — Key gelangt ins App-Bundle, Repository, Logs oder in eine Fehlerantwort | critical | A0 | Key ausschließlich serverseitig, AWS Secrets Manager oder verschlüsselte Lambda-Env, restriktive IAM, Rotation und Widerruf möglich, Secret-Scan des gebauten Bundles und des Repositories, Fehlerantworten ohne Provider-Secrets und interne URLs | open |
| (d) | Kostenrisiko ohne wirksames Rate Limit — offener Proxy-Endpunkt wird fremdgenutzt und erzeugt Provider- und AWS-Kosten; verschärft, weil das Geschäftsmodell (OQ-007) offen ist | high | A0 | Rate Limit, Size-Limit, maximale Wegpunktzahl, Timeout, Kill Switch, Koordinatenvalidierung, Kosten-Alarm; Missbrauchsschutz darf laut DEC-013 **nicht** zu dauerhafter Koordinatenspeicherung führen | open |
| (e) | Scope-Creep des Proxys zum De-facto-Backend — Auth, Aktivitäts-Sync oder Territory-Logik wachsen in `infra/routing-proxy/` hinein und entscheiden OQ-005 faktisch vor | high | A0-B | Ablage bewusst in `infra/routing-proxy/`, nicht `backend/` (OQ-011); Funktionsumfang auf Routenberechnung begrenzt; jede Erweiterung braucht eine dokumentierte Entscheidung und berührt OQ-005; `plumbline-scope-check` gegen den Allowed change scope | open |

**Wechselwirkung mit bestehenden Risiken.** RISK-007 („Client-API-Key wird missbraucht", Phase
`P0/A2`) ist durch DEC-005 nicht erledigt, sondern **verlagert**: die Angriffsfläche wandert vom
App-Bundle auf den Proxy-Endpunkt und ist ab **A0** statt ab A2 wirksam. Die Phasenangabe von
RISK-007 ist damit veraltet. Die Korrektur unterbleibt hier bewusst — RISK-007 zu ändern hieße,
eine bestehende registrierte Risikodefinition umzudeuten; das ist eine Nutzerentscheidung.
Ebenso berührt (a) die Stoßrichtung von RISK-022, betrifft aber Standort- statt Health-Daten und
wirkt ab A0 statt ab C/E.

## Neue Risiken aus der Telemetrie-Erhebung für CAN-130 (Routenempfehlungen, ab Stufe B)

> **BLOCKER — ID-Vergabe weiterhin nicht möglich.** Der Auftau-Schritt 2 vom 2026-07-19 hat neue
> VIS-, CAN-, REQ-, AC-, EV-, TRC-, USER- und OQ-IDs reserviert, jedoch **keine RISK-ID**.
> `docs/ID-REGISTRY.md` ist seitdem wieder eingefroren und führt **keine** RISK-ID über RISK-024
> hinaus. Nach Registry-Regel 3 wird das als BLOCKER gemeldet, statt eine ID zu erfinden — auch
> dann, wenn zeitgleich andere ID-Räume erweitert wurden. Die folgenden sechs Risiken sind daher
> **inhaltlich** erfasst, aber **ohne RISK-ID**. Die Marken (f)…(k) setzen die abschnittslokale
> Zählung des vorigen Abschnitts fort, sind reine Lesemarken und **keine IDs**. Sobald die
> Registry entfroren wird, sind hier echte RISK-IDs zu vergeben — die nächste freie ist dann zu
> **prüfen**, nicht aus dieser Notiz abzuleiten.

Diese Risiken entstehen aus der Nutzerentscheidung vom 2026-07-19 zu CAN-130: die Kennzahl
„bestätigte Routenübernahmen je auswertbarer Empfehlung" setzt eine serverseitige
Ereigniserhebung voraus. Damit entsteht ab Stufe B eine **Verarbeitungsfläche für soziales
Interaktionsverhalten**, die es in A0/A1 nicht gibt. Sie ist mit RISK-001…RISK-024 nicht
abgebildet: RISK-022 betrifft Health-Daten, RISK-015/016 betreffen Standortfreigabe und
Reviergrenzen — **keines** betrifft Empfehlungs- und Übernahmeereignisse. Die offenen Punkte sind
in `docs/decisions/open-questions.md` als **OQ-012** (Erhebung) und **OQ-014** (Stichprobenregel)
geführt.

| Marke (keine ID) | Risk | Severity | Phase | Mitigation | Status |
|---|---|---|---|---|---|
| (f) | **Re-Identifikation über verkettete Telemetrie** — pseudonyme `recommendation_id` und `adoption_id` sind für sich genommen unkritisch, werden aber gemeinsam mit Sportart, Sichtbarkeitskategorie und Zeitbucket gespeichert. In dünn besetzten Zeitfenstern oder kleinen Empfängerkreisen ist daraus rekonstruierbar, **wer wessen Route übernommen hat** — ein Sozialgraph, den die Funktion selbst nicht offenlegt | critical | B | Zeitstempel nur als grober Bucket, Sichtbarkeitskategorie statt Empfängerliste, keine Speicherung von Empfänger-IDs, k-Anonymitätsschwelle vor jeder Auswertung, frühestmögliche Aggregation, Rohereignis-Retention kurz und dokumentiert (OQ-012 Punkte 4 und 5), Privacy-Review vor Instrumentierung | open |
| (g) | **Scope-Creep der Telemetrie zum Verhaltens- oder Standorttracker** — die Ereignisliste wächst über die für CAN-130 nötigen sechs Ereignisse hinaus; Routengeometrie, Start-/Zieladresse oder Health-Bezug wandern „für bessere Auswertung" hinein. Die Nutzerentscheidung verbietet das ausdrücklich, aber kein technisches Mittel erzwingt es | critical | B | Abschließende Allowlist der sechs zulässigen Ereignisse und der zulässigen Felder, `event_version` mit Schema-Prüfung, automatisierter Allowlist-Test der tatsächlich gesendeten Felder (analog zum Logfeld-Test des Routing-Proxys), jede Erweiterung braucht eine dokumentierte Entscheidung, kein paralleler Standort- oder Verhaltenstracker, Aggregation aus ohnehin nötigen Backend-Ereignissen statt eigener Erhebung | open |
| (h) | **Fehlende oder untaugliche Einwilligungsgrundlage** — ob die Aktivierung der Social-/Empfehlungsfunktion die Messung trägt oder eine **separate** Einwilligung nötig ist, ist offen (OQ-012 Punkt 6). Eine falsch gewählte Grundlage macht die gesamte Messreihe unverwertbar und ist rückwirkend nicht heilbar; zusätzlich Store-Policy-Risiko | critical | B | Rechtsgrundlage **vor** Instrumentierung klären, nicht nachträglich; Messung an die ausdrückliche Aktivierung der Funktion koppeln; Widerruf muss die Erhebung wirksam beenden; kein Werbe- oder Cross-Service-Tracking; Abstimmung mit OQ-006 (Claims) und der Datenschutzerklärung | open |
| (i) | **Gelöschte Accounts bleiben in den Messdaten** — DEC-012 verlangt, dass Löschung alle personenbezogenen Daten und Identitätszuordnungen entfernt. Telemetrie-Rohereignisse sind ein **eigener** Speicherort, der bei der Löschimplementierung übersehen werden kann; historische Aggregate müssen zugleich stabil bleiben. Kollidiert direkt mit CONTRA-005 und NFR-006 | critical | B | Telemetrie-Ereignisse ausdrücklich in den Löschumfang aufnehmen und in EV-017 mitprüfen; Trennung Identität ↔ Aggregat (EV-042) auch für Telemetrie anwenden; Löschung darf bereits gebildete Aggregate nicht rückwirkend verfälschen — Verfahren dokumentieren; **vor** Finalisierung des Datenbankschemas entscheiden | open |
| (j) | **Fehlinterpretation der Kennzahl durch Nennerverzerrung** — datenschutzbedingt unsichtbare, gelöschte, blockierte oder moderativ verborgene Empfehlungen gehören nicht in den Nenner. Landen sie dort, wird **fehlender Zugang als mangelndes Nutzerinteresse gelesen** und eine funktionierende Funktion fälschlich als gescheitert bewertet — oder umgekehrt ein zu kleiner Nenner erzeugt einen scheinbar hohen Quotienten | high | B | Nenner-/Zähler-Definition aus CAN-130 verbindlich implementieren; datenschutzbedingt unsichtbare Empfehlungen **separat ausweisen**, nie als Gegenprobe im Nenner; Guardrail-Signale mitführen (Zahl auswertbarer Empfehlungen, Empfehlungen ohne berechtigten Empfänger, technisch fehlgeschlagene Ausspielungen, mediane Empfängerzahl, Anteil mit mindestens einer Übernahme, Lösch-/Blockierungs-/Moderationsanteil); Stichprobenregel (OQ-014) **vor** der Bewertung festlegen | open |
| (k) | **Sportartübergreifende Aggregation verdeckt eine schwache Sportart** — CAN-130 verlangt getrennte Werte `run_route_adoptions_per_recommendation` und `bike_route_adoptions_per_recommendation`. Ein Gesamtwert darf gezeigt werden, aber **nie anstelle** der getrennten Werte. Wird nur der Gesamtwert berichtet, kann eine gut laufende Sportart eine gescheiterte tragen und Gate B fälschlich passieren | high | B | Getrennte Kennzahlen sind die Pflichtausgabe, der Gesamtwert ist optional und nie Ersatz; Gate-B-Bewertung prüft **beide** Sportarten einzeln; Run und Bike werden getrennt verifiziert (projektweite Regel); Dashboards, die nur den Gesamtwert zeigen, gelten nicht als Nachweis | open |

**Wechselwirkung mit bestehenden Risiken.**

- **RISK-022** („Sensitive Health-Daten werden unnötig serverseitig verarbeitet", Phase `C/E`)
  trifft die Stoßrichtung von (f) und (g), betrifft aber **Health-Daten ab C/E**. Die
  Telemetriefläche betrifft **soziale Interaktionsdaten ab B** und ist damit früher wirksam und
  von anderem Datentyp. RISK-022 wird hier **nicht** umgedeutet — eine Änderung der registrierten
  Risikodefinition ist eine Nutzerentscheidung.
- **RISK-015/RISK-016** (Stalking, Wohnort- und Routinepreisgabe, Phase `D`) beschreiben
  Standortpreisgabe. (f) beschreibt eine **Beziehungs**-Rekonstruktion ohne Standortdaten und
  wirkt ab **B** statt ab D.
- **RISK-021** (Moderationsaufwand skaliert nicht) wird durch (j) verschärft: ohne definierte
  Moderationswege (OQ-010) ist nicht bestimmbar, wann eine Empfehlung als „vollständig
  unsichtbar" gilt — die Nennerbildung hängt daran.
- **RISK-024** (User Confirmation fälschlich als erteilt angenommen) gilt hier unverändert: die
  sechs Risiken sind aus einer Nutzerentscheidung **abgeleitet** und in diesem Lauf **nicht**
  vom Nutzer bestätigt.

**Kein Nachweis.** Es existiert kein Code, keine Instrumentierung, kein Event und keine Messreihe.
Sämtliche Mitigationen sind **geplant, nicht umgesetzt**. Keine der Zeilen ist geprüft, und keine
darf als wirksam geführt werden.

## Risk Review Rule

- Critical: Review vor jedem betroffenen Gate.
- High: Owner und Evidence vor Start des Workstreams.
- Kein Risiko wird auf `closed` gesetzt, ohne verlinkte Evidence oder Entscheidung.
