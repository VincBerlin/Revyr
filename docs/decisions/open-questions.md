# Open Questions and Decision Gates

**Kanonisches Register.** Diese Datei ist die einzige Stelle, an der OQ-IDs definiert werden. Canvas (`docs/canvas/revyr-endurance-platform.canvas.md`), PRD (`docs/prd/revyr-endurance-platform.prd.md`) und Vision (`docs/vision/revyr-endurance-platform.vision.md`) referenzieren diese IDs ausschließlich. Eine OQ-ID bezeichnet projektweit genau eine Entscheidung. Neue offene Punkte werden hier angelegt, nicht in den referenzierenden Dokumenten.

| ID | Decision | Source Type | Owner | Deadline | Default if unresolved |
|---|---|---|---|---|---|
| OQ-001 | finaler öffentlicher Produktname | MISSING | Product/Legal | vor Gate A2 | kein öffentlicher Store-Release |
| OQ-002 | finaler Repository-Owner/DRI | MISSING *(Quellenprüfung 2026-07-20: bestätigt, §Q1)* | Product | vor P0 Start | Umsetzung bleibt organisatorisch unzugeordnet |
| OQ-003 | Minimum iOS/Android und Referenzgeräte | MISSING *(Quellenprüfung 2026-07-20: bestätigt, §Q2)* | Engineering/QA | vor A0 Feldtest | keine Gate-Abnahme |
| OQ-004 | Karten-/Routinganbieter | **TEILWEISE BELEGT** *(Quellenprüfung 2026-07-20: Startanbieter, Prüfzeitpunkt, Kriterien und Alternativen sind in den Quellen entschieden; offen ist allein der finale Entscheid — §Q3)* | Engineering/Product | vor A2/B ⚠️ **weicht von den Quellen ab, siehe §Q3** | Provider-Adapter bleibt experimentell |
| OQ-005 | Backend | MISSING | Engineering | vor B | kein Social-/Territory-Start |
| OQ-006 | Claims-Whitelist | MISSING | Product/Legal | vor A1 Public Beta | Health-Copy bleibt intern/Test |
| OQ-007 | Geschäftsmodell | MISSING | Product/Business | vor C | keine kostensteigernden Scale-Entscheidungen |
| OQ-008 | Effort-/Territory-/Bahngold-Startwerte | MISSING | Product/Data | vor C/D | Feature Flags bleiben aus |
| OQ-009 | Datenretention für GPS, Health und Live | MISSING | Privacy/Product | vor B/D | minimales Retention-Prinzip |
| OQ-010 | Moderations-SLA und Betrieb | MISSING | Operations | vor B Public | UGC bleibt begrenzt/deaktiviert |
| OQ-011 | Ablageort und Deployment-Ziel des A0-Routing-Proxys im Repository | **RESOLVED (Nutzer, 2026-07-19)** | Engineering | erledigt | entfällt — siehe Auflösung unten |
| OQ-012 | Privacy-minimierte Telemetrie für Routenempfehlungen (CAN-130 / REQ-019 / AC-041) | MISSING | MISSING (OQ-002) | vor Gate B | kein Gate-B-Erfolgsnachweis für REQ-019; CAN-130 gilt als **nicht** empirisch validiert |
| OQ-013 | Messdefinition, Zielwert und Gate-Zuordnung für NFR-008 (Wartbarkeit) | MISSING | MISSING (OQ-002) | MISSING — kein Gate referenziert NFR-008 | NFR-008 bleibt wirkungslos |
| OQ-014 | Stichproben- und Auswertungsregel für CAN-130 / AC-041 | MISSING | MISSING (OQ-002) | vor Gate B | Kennzahl wird nicht abschließend bewertet |
| OQ-015 | Vergleichbarkeits- und Streckenähnlichkeitsdefinition für den Aktivitätsvergleich (**REQ-042**) | MISSING | MISSING (OQ-002) | vor Gate A2 | Aktivitätsvergleich wird nicht implementiert; **REQ-041 ist davon unberührt** |
| OQ-016 | Referenz-Fremdanwendung für den GPX-Kompatibilitätsnachweis (REQ-039) | MISSING | MISSING (OQ-002) | vor Gate A2 | AC-039 Kriterium (d) bleibt nicht reproduzierbar prüfbar |

## Quellenprüfung OQ-002, OQ-003, OQ-004 (2026-07-20)

Die vier Quelldokumente (SRC-001 … SRC-004) sind seit dem 2026-07-20 lesbar und wurden gegen diese
drei offenen Fragen geprüft. **Es wurde kein Wert geraten und keine Frage geschlossen.** Ergebnis:
zwei bleiben unverändert MISSING, eine ist deutlich enger als ihr Titel vermuten lässt.

### §Q1 — OQ-002 (Repository-Owner/DRI): **MISSING bestätigt**

Alle vier Quellen wurden auf `Owner`, `DRI`, `verantwortlich` geprüft. **Keine Quelle nennt eine
Person, eine Rolle oder eine Organisation als Verantwortliche.** Die einzigen Treffer für „owner"
stehen in SRC-003 §5.3 (Datenmodell-Zielbild) und sind **Spaltennamen eines Datenbankschemas** —
`owner_team_id`, `owner_id`, `owner_type`. Sie bezeichnen den Besitzer eines *Areals*, nicht den
Verantwortlichen eines Repositorys.

> ⚠️ **Ausdrücklich festgehalten, weil es die naheliegende Fehlleistung wäre:** eine Volltextsuche
> nach „owner" liefert in SRC-003 Treffer. Sie als Beleg für einen benannten DRI zu lesen, wäre
> exakt der wiederkehrende Defekt — ein syntaktisch gültiger Fund, der die Aussage nicht trägt.

Die Zuordnung „Product" in der Owner-Spalte oben ist eine **Rollenangabe dieses Registers**, keine
Quellenaussage. SRC-001 §3.6 führt sieben offene Punkte und weist **keinem** einen Owner zu.
**Nutzerentscheidung. Es wird kein Name und keine Rolle vorgeschlagen.**

### §Q2 — OQ-003 (Minimum-OS und Referenzgeräte): **MISSING bestätigt — aber nicht leer**

Die Quellen **fordern** Referenzgeräte und Plattformnachweise, **benennen** aber weder ein
Gerätemodell noch eine Mindest-OS-Version. In allen vier Dokumenten kommt **keine einzige**
iOS- oder Android-Versionsnummer, kein SDK-Level und kein Gerätemodell vor.

| Was die Quellen verbindlich fordern | Fundstelle |
|---|---|
| „Ziel < 10 %/h **auf Referenzgeräten**" | SRC-001 §3.5 (NFR Batterie) |
| „Distanzabweichung < 3 % auf bekannter **Referenzstrecke**" | SRC-001 §3.5 (NFR Genauigkeit) |
| „Messlauf **je Sport + Plattform**" | SRC-002 §10 |
| Ledger-Pflichtzeilen „Echtes Gerät ✅ **Modell + OS**", „iOS geprüft ✅ **Version**", „Android geprüft ✅ **Version**" | SRC-003 §9 (Eintragsvorlage) |
| GATE A: „je Sport 1 Aktivität ≥ 30 min mit gesperrtem Bildschirm korrekt (**iOS und Android**)" | SRC-003 §9 |

**Das ist die präzise Lage:** die Quellen verlangen, Modell und OS-Version zu *protokollieren*, und
setzen **keine Untergrenze**. Ein Nachweis „auf Referenzgeräten" ist ohne benannte Geräte nicht
reproduzierbar — das Kriterium ist formuliert, aber nicht prüfbar.

**A0-Gate-Bedingung.** Der Delivery Plan führt OQ-003 als A0-Gate-Bedingung. Das deckt sich mit
SRC-003 §9 GATE A, das den Feldtest auf echter Hardware auf **beiden** Plattformen verlangt.
**Nutzerentscheidung. Es wird kein Gerät und keine Version geraten.**

### §Q3 — OQ-004 (Karten-/Routinganbieter): **enger als der Titel — und mit einer Terminabweichung**

Anders als bei OQ-002 und OQ-003 sagen die Quellen hier **Verbindliches**, und zwar
übereinstimmend an vier Stellen:

| Aussage | Fundstellen |
|---|---|
| **Startanbieter ist entschieden:** „Stufe A: react-native-maps (Apple Maps iOS / Google Android) + OpenRouteService (foot-walking / cycling-regular)" | SRC-003 §5.4; SRC-001 §3.6 Punkt 3 („Start: react-native-maps + OpenRouteService") |
| **Offen ist der Kosten-Entscheid, nicht der Start:** „**Anbieter-Review vor Stufe B** … → ADR" | SRC-003 §5.4, §10 Risiko 5, §11 |
| **Prüfkriterien benannt:** „Kosten: Google-Preise, ORS-Limits" | SRC-003 §5.4 |
| **Alternativen benannt:** „Mapbox, MapLibre+OSM" | SRC-003 §5.4 |

**Was daraus folgt.** OQ-004 ist **nicht** die Frage „welcher Anbieter?" — der Startanbieter steht
fest und ist in CAN-094 abgebildet. Offen ist allein der **finale Kosten-Entscheid per ADR**.
**Die Frage wird hier trotzdem nicht geschlossen:** ein ADR ist ein Ergebnis, kein Dokumentzustand,
und der Entscheid ist eine Nutzerentscheidung.

> ⚠️ **Terminabweichung, nicht geglättet.** Alle vier Quellenstellen datieren den ADR **„vor Stufe B"
> bzw. „vor v2.0"** (SRC-003 §5.4, §10, §11; SRC-001 §3.6; SRC-002 §11 Blocker-Kette
> „Karten-ADR (→ v2.0)"). **Keine Quelle nennt A0 oder A2** — die Stufenbezeichnungen A0/A1/A2
> kommen in den Quellen überhaupt nicht vor, dort gibt es nur die Stufen A–E. Die Vorziehung auf
> **vor A0**, die `docs/traceability.md` im REQ-006-Befund vornimmt, ist eine **projektinterne
> Ableitung** aus der Routing-Proxy-Entscheidung vom 2026-07-19, keine Quellenaussage. Der
> Delivery Plan führt OQ-004 als A0-Gate-Bedingung. **Beide Termine stehen nebeneinander, weil
> beide belegt sind — der eine aus den Quellen, der andere aus einer Projektentscheidung. Welcher
> gilt, ist eine Nutzerentscheidung und wird hier nicht durch Angleichung entschieden.**

**Herkunft OQ-012 … OQ-016.** Diese fünf IDs wurden in **Phase 1, Auftau-Schritt 2** (2026-07-19)
in `docs/ID-REGISTRY.md` reserviert und vor der Vergabe als frei geprüft; die Registry ist
seitdem wieder eingefroren. Ihre Eintragung hier ist der von Registry-Regel 10 vorgesehene
**Nachzug** (§7.4.4), keine Neuvergabe. Dieser Schritt vergibt **keine** ID.

**`blocked_gates` / `blocked_activities` je Eintrag** (Feldmodell C16, siehe
`docs/decisions/decision-log.md`; Gate- und Tätigkeitsvokabular werden **nie** miteinander
verglichen):

| ID | blocked_gates | blocked_activities |
|---|---|---|
| OQ-012 | `B` | — (leer) |
| OQ-013 | — (leer) | — (leer) |
| OQ-014 | `B` | — (leer) |
| OQ-015 | `A2` | `implementation` |
| OQ-016 | `A2` | `field-test` |

Bei OQ-013 bedeutet die doppelt leere Liste **nicht** „unkritisch": NFR-008 wird an keiner Stelle
wirksam — kein Gate fordert es ein, kein Nachweis ist vorgesehen, keine CI existiert. Genau das
ist der Befund.

## Auflösung OQ-011 (Nutzerentscheidung, 2026-07-19)

- **Ablageort:** `infra/routing-proxy/` — ausdrücklich **nicht** `backend/`.
  Begründung: begrenzte, austauschbare Infrastrukturkomponente; `backend/` bleibt für Stufe B
  reserviert und wird durch diese Entscheidung nicht präjudiziert.
- **Laufzeit A0:** AWS Lambda + API Gateway, Region `eu-central-1`, Provider-Key ausschließlich
  serverseitig, Rate Limit, Timeout, Kill Switch.
- **Mobile-App:** enthält keinen Routing-Provider-Key. Sie kennt nur eine konfigurierbare
  Proxy-Basis-URL, einen providerneutralen `RoutingPort` und einen `RoutingClient`.
  Providername und Providerantwort dürfen nicht in Domain- oder UI-Code gelangen.
  Die Profilübersetzung `run → foot-walking` und `ride → cycling-regular` liegt im Proxy.
- **Nur dokumentiert, nicht gebaut.** Das Verzeichnis `infra/routing-proxy/` wurde in diesem
  Lauf **nicht angelegt**; es existiert keine Quelldatei und keine AWS-Ressource.

Abgebildet in CAN-096 und CAN-097 (Registry §6.3), Registry-Status OQ-011 = `resolved`.

## OQ-012 — Privacy-minimierte Telemetrie für Routenempfehlungen

`status: open` · `source_type: MISSING` · `blocked_gates: [B]` · `blocked_activities: []` ·
Owner: **MISSING (OQ-002)** · fällig **vor Gate B**

Betrifft CAN-130 (Erfolgssignal übernommene Routen), REQ-019, AC-041 und EV-041.

### Warum die Frage entsteht

CAN-130 misst „bestätigte Routenübernahmen je auswertbarer Routenempfehlung" über ein rollierendes
28-Tage-Fenster, getrennt für Run und Bike. Diese Kennzahl ist **nur** berechenbar, wenn im
Backend Ereignisse zu Veröffentlichung, Berechtigung, Ausspielung und Übernahme entstehen. Damit
entsteht ab Stufe B eine **Verarbeitungsfläche, die es in A0/A1 nicht gibt** — vergleichbar zu der
durch DEC-005/DEC-013 entstandenen Routing-Fläche, aber mit einem anderen Datentyp: sozialem
Interaktionsverhalten statt Koordinaten.

### Vor Gate B zu klären (abschließende Liste)

| # | Zu klären |
|---|---|
| 1 | Wird `route_recommendation_exposed` **client- oder serverseitig** erhoben? |
| 2 | Welche **Event-Metadaten** sind für die Kennzahl tatsächlich nötig — und welche nicht? |
| 3 | Welche Daten dürfen **gespeichert** werden (im Unterschied zu: nur transient verarbeitet)? |
| 4 | **Aufbewahrungsdauer der Rohereignisse.** |
| 5 | Ab wann liegen **nur noch Aggregate** vor? |
| 6 | Ist eine **separate Einwilligung** nötig, oder trägt die Aktivierung der Social-/Empfehlungsfunktion? |
| 7 | Wie wirken **Profil-Privacy, Blockierungen und Löschungen** auf die Messung? |
| 8 | Wie werden **gelöschte Accounts** aus den Messdaten entfernt oder anonymisiert? |
| 9 | Wer ist **Owner der Instrumentierung**? |
| 10 | Welche **Analytics-/Event-Lösung** wird eingesetzt? |

Keiner der zehn Punkte wird durch eine plausible Annahme geschlossen. „Später klären" ist als
Auflösung ausdrücklich unzureichend.

### Bereits festgelegter Rahmen (Nutzerentscheidung 2026-07-19) — nicht Gegenstand dieser Frage

Der folgende Rahmen steht fest und ist **nicht** offen; OQ-012 klärt nur die zehn Punkte oben
innerhalb dieses Rahmens.

**Zulässige Ereignisse:** `route_recommendation_published` · `route_recommendation_eligible` ·
`route_recommendation_exposed` · `route_adopted` · `route_recommendation_deleted` ·
`route_recommendation_hidden`.

**Zulässige Felder:** pseudonyme `recommendation_id`, pseudonyme `adoption_id`, `sport`
(`run`|`ride`), Sichtbarkeitskategorie, grober Zeitstempel bzw. Zeitbucket, Ergebnisstatus,
Event-Version.

**Unzulässig:** GPS-Koordinaten, Routengeometrie, Start-/Zieladresse, Health-Daten, Klarnamen,
E-Mail, vollständige Gerätekennungen, öffentliche Analytics-Profile, Werbe- und
Cross-Service-Tracking. **Kein paralleler Standort- oder Verhaltenstracker.** Die Kennzahl ist
möglichst aus ohnehin nötigen Backend-Ereignissen zu aggregieren.

**Local-first-Abgrenzung:** In A0/A1 bleiben Aktivitäts-, Health- und Verlaufsdaten standardmäßig
lokal. Erst ab Stufe B dürfen für die **ausdrücklich aktivierte** Social-/Empfehlungsfunktion
minimierte Metadaten verarbeitet werden. Rohroute und GPS-Geometrie werden **nie** für die
Erfolgsmessung verwendet. Gemessen wird das Ereignis „Empfehlung übernommen", **nicht** die
später gelaufene oder gefahrene Strecke.

**Datenschutzbedingt unsichtbare Empfehlungen** werden **separat ausgewiesen** und gehen **nicht**
als Gegenprobe in den Nenner ein — sonst wird fehlender Zugang fälschlich als mangelndes
Nutzerinteresse gelesen.

### Blocking-Abgrenzung (ausdrücklich)

**NICHT blockierend für:**

- Gate A0 und Gate A1 — dort existiert die Empfehlungsfunktion nicht.
- Die **Dokumentkorrektur** (`documentation`) — `blocked_activities` ist ausdrücklich leer.
  Dokumentation und Planung dürfen uneingeschränkt fortgesetzt werden.
- Das **funktionale** Kriterium AC-019 („ein berechtigter Nutzer kann eine sichtbare
  Routenempfehlung übernehmen"). Es kann bestanden sein, während die Produktkennzahl noch keine
  ausreichende Stichprobe hat.

**Blockierend für:**

- Den **externen Gate-B-Erfolgsnachweis von REQ-019**.
- **Jede Behauptung, CAN-130 sei empirisch validiert.** `empirical_result` bleibt **MISSING**,
  `evidence_status` von EV-041 bleibt `planned` (Metrik und Gate definiert, Instrumentierung
  fehlt), `target_source_type` bleibt `EXPLICIT`.

### Abhängigkeit

OQ-012 klärt, **womit** gemessen werden darf. **OQ-014** klärt, **ab wann genug gemessen ist**
(Mindestzahl auswertbarer Empfehlungen, Mindestzahl berechtigter Empfänger, Mindestdauer des
Messfensters, Testkonten, Mehrfachübernahmen, gelöschte und moderierte Empfehlungen, getrennte
Run-/Bike-Auswertung). Beide müssen vor einer abschließenden Bewertung von CAN-130 geschlossen
sein; keine der beiden ersetzt die andere. Es wird **keine Mindestzahl geraten**.

### Neue Risiken

Die aus dieser Erhebung entstehenden Risiken sind in `docs/risks/revyr-risk-register.md` erfasst
(Marken (f)…(k)) — **ohne RISK-ID**, weil die Registry eingefroren ist und keine RISK-ID über
RISK-024 hinaus reserviert.

## Neue offene Punkte aus CONTRA-006 — vor dem ersten externen Feldtest zu klären

> **BLOCKER — ID-Vergabe für diese sieben Punkte weiterhin nicht möglich.** Der Auftau-Schritt 2
> vom 2026-07-19 hat **OQ-012 … OQ-016** reserviert, jedoch **ausschließlich** für fünf andere
> Gegenstände (Telemetrie, NFR-008-Messdefinition, CAN-130-Stichprobenregel,
> **REQ-042**-Vergleichbarkeit — bis zur Teilung vom 2026-07-20 als REQ-040 geführt —,
> GPX-Referenz-App). Für die folgenden sieben Punkte wurde **keine**
> OQ-ID reserviert; die Registry ist seit dem Auftau-Schritt wieder eingefroren und führt
> **keine** OQ-ID über OQ-016 hinaus. **Runde 4 (2026-07-20) hat daran nichts geändert: sie hat
> ebenfalls keine OQ-ID vergeben.** Nach Registry-Regel 3 meldet ein Agent außerhalb Phase 1
> eine fehlende ID als BLOCKER, statt sie zu erfinden — auch dann, wenn kurz zuvor andere IDs
> vergeben wurden. Die Punkte sind daher **inhaltlich** erfasst, aber **ohne OQ-ID**. Die Marken
> (a)…(g) sind reine abschnittslokale Lesemarken, **keine IDs**, und dürfen nicht als solche
> referenziert werden. Sobald die Registry erneut entfroren wird, sind hier echte OQ-IDs zu
> vergeben — die nächste freie ist dann zu **prüfen**, nicht aus dieser Notiz abzuleiten.

Alle sieben Punkte entstehen aus DEC-013 / CONTRA-006 und sind **blockierend für den ersten
externen Feldtest** der Routenplanung, nicht erst für Stufe B.

| Marke (keine ID) | Decision | Source Type | Owner | Deadline | Default if unresolved |
|---|---|---|---|---|---|
| (a) | Verarbeitungsregion des Routinganbieters | MISSING | Engineering/Privacy | vor erstem externem Feldtest | kein externer Feldtest der Routenplanung |
| (b) | Verlassen die Daten den EWR? | MISSING | Privacy/Legal | vor erstem externem Feldtest | Bezeichnung „EU-Proxy" darf nicht verwendet werden |
| (c) | Unterauftragsverarbeiter des Routinganbieters | MISSING | Privacy/Legal | vor erstem externem Feldtest | Provider nicht für produktive oder externe A0-Tests einsetzbar |
| (d) | Transfergrundlage für Drittlandübermittlung | MISSING | Legal | vor erstem externem Feldtest | keine Übermittlung außerhalb des EWR |
| (e) | Auftragsverarbeitungsvertrag mit dem Routinganbieter (inkl. Rollenverteilung Controller/Processor, Provider-Retention, Ausschluss eigener Werbe-/Profiling-/Trainingszwecke, Lösch- und Sicherheitsregeln) | MISSING | Legal/Engineering | vor erstem externem Feldtest | Provider nicht für produktive oder externe A0-Tests einsetzbar |
| (f) | Rechtsgrundlage der Übermittlung (Verantwortlicher, Zweck, Empfänger, Übermittlungsregionen, Speicherdauer, Betroffenenrechte, Datenschutzkontakt) | MISSING | Legal/Privacy | vor erstem externem Feldtest | Routenplanung bleibt intern/Test |
| (g) | Datenschutzerklärung mit dem verbindlichen Routing-Absatz, verfügbar **vor** Nutzung der Routenplanung | MISSING | Legal/Product | vor erstem externem Feldtest | Routenplanung wird nicht freigeschaltet |

Kein Punkt wird durch eine plausible Annahme geschlossen. „Später klären" ist als Auflösung
ausdrücklich unzureichend; jeder Punkt braucht eine benannte, dokumentierte Entscheidung.

## OQ-013 — Messdefinition, Zielwert und Gate-Zuordnung für NFR-008 (Wartbarkeit)

`status: open` · `source_type: MISSING` · `blocked_gates: []` · `blocked_activities: []` ·
Owner: **MISSING (OQ-002)**

NFR-008 („TypeScript strict, reine Domainmodule, versionierte Schemas, automatisierte Tests")
wurde am 2026-07-19 geprüft und **nicht deprecatet**: die Anforderung ist fachlich notwendig, von
keinem anderen NFR dupliziert und in `prd.md` tatsächlich definiert (nicht nur reserviert). Was
fehlt, ist ausschließlich die Messdefinition.

**Zu klären:** Metrik (Testabdeckung? Typfehler? Anteil abhängigkeitsfreier Domainmodule? Anzahl
unversionierter Schemas? — **keine ist gewählt**) · Einheit · Schwellwert · Messfenster (je
Commit, je Build) · Testmethode · zuständiges Gate · Owner.

**Ausdrücklich nicht gesetzt:** Es wird **keine Testabdeckungsquote** vergeben. Die in
`CLAUDE.md` genannten 80 % sind eine globale Arbeitsregel des Nutzers, **kein** für dieses Produkt
beschlossener NFR-Zielwert. Eine Übernahme wäre eine erfundene Schwelle.

**Befund.** `blocked_gates` und `blocked_activities` **dieser offenen Frage** sind beide leer —
OQ-013 blockiert derzeit nichts. Das ist **keine** Unbedenklichkeitsaussage, sondern der Kern des
Befunds: ein must-artiges Qualitätsziel, das an kein Gate gebunden ist, keinen Nachweis vorsieht
und von keiner CI durchgesetzt wird, ist wirkungslos. Ein Qualitätsziel wird nicht dadurch
wirksam, dass man seine Wirkungslosigkeit dokumentiert.

**Präzisierung 2026-07-20 — NFR-008 selbst führt kein `blocking` mehr.** Die Felder oben sind die
Achsen **dieser OQ**, nicht die von NFR-008. Nach der Nutzerentscheidung vom 2026-07-20 führt der
gesamte `NFR-`Raum **kein** `blocking`: die Achsen bleiben auf `OQ-` und `CONTRA-` beschränkt
(keine Metamodell-Erweiterung). Grund: die Achse `status` (`open`/`resolved`) beantwortet „Ist die
Grundsatzfrage entschieden?" — ein NFR ist keine Entscheidung, sondern eine Anforderung, und
benutzt `active`/`deprecated`/`reserved`. Wendet man die Formel trotzdem an, ergibt sie für **alle
acht** NFRs `blocking = true`: mechanisch reproduzierbar und fachlich bedeutungslos.
**NFR-008 wird ausdrücklich nicht deprecatet** — die Anforderung ist fachlich real, von keinem
anderen NFR dupliziert und im PRD mit vier konkreten Zusagen definiert. Ihre Wirkungslosigkeit
steht jetzt in den Feldern, die es dafür gibt: `evidence_gate = MISSING`,
`evidence_status = not-planned`. Der Befund wird dadurch nicht kleiner, sondern nur an die
Stelle geschrieben, an der ihn eine Prüfung findet.

## OQ-014 — Stichproben- und Auswertungsregel für CAN-130 / AC-041

`status: open` · `source_type: MISSING` · `blocked_gates: [B]` · `blocked_activities: []` ·
Owner: **MISSING (OQ-002)**

**Vor der endgültigen Bewertung von CAN-130 zu definieren:** Mindestzahl auswertbarer
Empfehlungen · Mindestzahl berechtigter Empfänger · Mindestdauer des Messfensters · Behandlung von
Testkonten · Umgang mit Mehrfachübernahmen desselben Nutzers · Umgang mit gelöschten und
moderierten Empfehlungen · getrennte Run-/Bike-Auswertung.

**Es wird keine Mindestzahl geraten.** Bis zur Entscheidung gilt: `target_source_type` =
`EXPLICIT`, `evidence_status` (EV-041) = `planned`, `empirical_result` = **MISSING**.

Abgrenzung zu OQ-012: OQ-012 klärt, **womit** gemessen werden darf; OQ-014 klärt, **ab wann genug
gemessen ist**. Beide sind vor einer abschließenden Bewertung zu schließen.

## OQ-015 — Vergleichbarkeits- und Streckenähnlichkeitsdefinition für den Aktivitätsvergleich (REQ-042)

`status: open` · `source_type: MISSING` · `blocked_gates: [A2]` ·
`blocked_activities: [implementation]` · Owner: **MISSING (OQ-002)**

**Betroffene IDs nach der Teilung vom 2026-07-20:** CAN-143 · REQ-042 · AC-043 · EV-044 · TRC-042.

**Zu klären:** wann zwei Strecken als **vergleichbar** gelten · **tolerierte Abweichung der
Streckenähnlichkeit** und die Methode, mit der sie bestimmt wird · welche Kennzahlen verglichen
werden · Behandlung verkürzter, verlängerter oder abgebrochener Aktivitäten ·
**keine irreführende Bestzeit bei nicht vergleichbarer Geometrie**. Run und Bike strikt getrennt.

Bis zur Entscheidung bleibt die konkrete Vergleichslogik `RESEARCH_HYPOTHESIS` bzw. **MISSING**;
AC-043 und EV-044 sind ohne sie nicht vollständig spezifizierbar. Es wird **keine**
Vergleichstoleranz und **keine** Ähnlichkeitsschwelle geraten.

### Migration 2026-07-20 — Gegenstand präzisiert, keine neue Frage

Die Nutzerentscheidung vom 2026-07-20 hat das Composite **CAN-140 geteilt** und in dessen Folge
REQ-040, AC-040, EV-040 und TRC-040 deprecatet. OQ-015 wandert damit **vollständig** auf die
Auswertungshälfte:

| Bezug in OQ-015 bis 2026-07-19 | ab 2026-07-20 | Status der Alt-ID |
|---|---|---|
| REQ-040 | **REQ-042** | deprecated, replacement_id REQ-041, REQ-042 |
| AC-040 | **AC-043** | deprecated, replacement_id AC-042, AC-043 |
| EV-040 | **EV-044** | deprecated, replacement_id EV-043, EV-044 |
| — (kein Canvas-Bezug geführt) | **CAN-143** | CAN-140 deprecated, replacement_id CAN-142, CAN-143 |

**OQ-015 blockiert die Planungshälfte ausdrücklich NICHT.** REQ-041 (Wiederverwendung einer
gespeicherten Route), AC-042, EV-043, CAN-142 und TRC-041 sind **vollständig spezifizierbar** und
stehen unter keiner offenen Frage dieses Registers. Das ist der operative Grund, aus dem die
Teilung vorgenommen wurde: unter der alten, ungeteilten ID hätte OQ-015 eine lieferbare Funktion
mitblockiert. Wer die Blockade weiterhin auf „Streckenwiederverwendung und Vergleich" bezieht,
liest den Stand vor dem 2026-07-20.

### Warum aus der Teilung KEINE neue OQ-ID entsteht — geprüft, nicht angenommen

> **ABWEICHUNG von der wörtlichen Anweisung, ausdrücklich gemeldet.** Der Auftrag lautete, die
> neuen offenen Fragen aus der Teilung „mit den in Phase 1 reservierten OQ-IDs" anzulegen.
> **Phase 1 hat in Runde 4 keine OQ-ID reserviert** (`new_oq_ids: []` in
> `scratchpad/id-migration-r4.json`); die Registry führt weiterhin **keine** OQ-ID über OQ-016
> hinaus und ist eingefroren. Eine ID zu vergeben wäre außerhalb von Phase 1 unzulässig, eine
> „naheliegende nächste" abzuleiten genau der Defekt, den CONTRA-003 für den OQ-Raum bereits
> nachgewiesen hat. Der Nutzer kann diese Abweichung überstimmen — dann ist die Registry für eine
> Vergabe zu entfrieren und die nächste freie ID zu **prüfen**, nicht aus dieser Notiz abzuleiten.

Der Gegenstand der Teilung ist geprüft worden, statt reflexhaft eine neue Frage anzulegen:

| Aussage aus der Teilung | Bereits durch eine offene Frage getragen? |
|---|---|
| Wann gelten zwei Strecken als „hinreichend ähnlich"? | **ja — OQ-015**, ausdrücklich („tolerierte Abweichung"). Der Wortlaut oben ist um „Streckenähnlichkeit" **präzisiert**, weil die Nutzerentscheidung sie namentlich fordert. Keine zweite Frage: eine Vergleichbarkeitsdefinition **ist** die Ähnlichkeitsdefinition |
| Welche sportartspezifischen Kennzahlen werden verglichen? | **ja — OQ-015**, unverändert |
| Behandlung verkürzter, verlängerter, abgebrochener Aktivitäten | **ja — OQ-015**, unverändert |
| Wiederverwendung einer gespeicherten Route (REQ-041) | **keine offene Frage** — vollständig spezifizierbar |

**Zwei Punkte aus Runde 4 sind offen, aber ausdrücklich KEINE OQ-Einträge.** Sie werden hier
benannt, damit sie nicht dadurch verschwinden, dass für sie keine ID existiert:

| Marke (keine ID) | Punkt | Warum keine OQ-ID |
|---|---|---|
| (h) | **Inhalt von VIS-014** — REQ-041 hat keinen Vision-Anker; VIS-014 ist reserviert, Inhalt MISSING, TRC-041 ist `broken` | Das ist eine **fehlende Aussage in der Vision**, keine unentschiedene Produktfrage. Ein Vision-Item wäre neue Produktsubstanz; es wird hier weder erfunden noch aus VIS-003 abgeleitet. Registry §8 Punkt 38 (**BLOCKER**) |
| (i) | **Fremd-App-Klausel von CAN-139** — der kanonische Wortlaut nennt „in einer kompatiblen Fremdanwendung öffnen" nicht mehr, AC-039 (d) und EV-039 [G4] verlangen sie weiterhin | Das ist eine **Scope-Frage zu einer bereits getroffenen Entscheidung**, keine neue offene Entscheidung. Registry §8 Punkt 36. **Nicht zu verwechseln mit OQ-016**: OQ-016 fragt *welche* App, (i) fragt *ob die Klausel überhaupt noch gilt*. Wird (i) zugunsten des Wegfalls entschieden, wird OQ-016 gegenstandslos — die umgekehrte Richtung gilt nicht |

Die Marken (h) und (i) sind abschnittslokale Lesemarken, **keine IDs**, und dürfen nicht als solche
referenziert werden.

## OQ-016 — Referenz-Fremdanwendung für den GPX-Kompatibilitätsnachweis (REQ-039)

`status: open` · `source_type: MISSING` · `blocked_gates: [A2]` ·
`blocked_activities: [field-test]` · Owner: **MISSING (OQ-002)**

AC-039 verlangt, dass die exportierte Datei „in **mindestens einer definierten** kompatiblen
Fremd-App" geöffnet werden kann. Welche App das ist, legt **kein Artefakt** fest — ohne
Festlegung ist das Kriterium nicht reproduzierbar prüfbar, und zwei Prüfer können mit
unterschiedlichen Apps zu unterschiedlichen Ergebnissen kommen.

**Es wird keine App geraten.** Zu entscheiden sind Name, Version und Plattform der
Referenzanwendung sowie, ob ein Nachweis je Plattform (iOS und Android) nötig ist.

**Vorgelagerte Frage, ohne ID — Marke (i) im OQ-015-Abschnitt.** Der am 2026-07-20 als kanonisch
gesetzte CAN-139-Wortlaut nennt das Öffnen in einer Fremdanwendung **nicht mehr**; AC-039 (d) und
EV-039 [G4] verlangen es weiterhin. **OQ-016 setzt voraus, dass die Klausel gilt.** Entscheidet
der Nutzer, dass sie mit dem neuen Wortlaut entfallen ist, wird OQ-016 **gegenstandslos** — die
umgekehrte Richtung gilt nicht: eine Referenz-App zu benennen beantwortet nicht, ob der Nachweis
überhaupt gefordert ist. Die beiden Fragen werden deshalb **nicht** zusammengelegt.

## Notes

OQ-005 (Backend) ist durch die Nutzerentscheidung vom 2026-07-19 zum A0-Routing-Proxy **nicht**
geschlossen. Der A0-Proxy ist eine minimale Sicherheitsmaßnahme für NFR-007 und präjudiziert
Geo-, Auth-, Realtime- und EU-Hosting-Entscheidungen nicht. Der Ablageort `infra/routing-proxy/`
wurde bewusst getrennt von `backend/` gewählt, um genau diese Präjudizierung zu vermeiden.

OQ-004 (Karten-/Routinganbieter) wird durch OQ-011 **nicht** geschlossen. Die Punkte (a)…(e)
oben sind eine Vorbedingung für jede Anbieterwahl: ein Anbieter, der sie nicht erfüllt, ist für
produktive oder externe A0-Tests nicht einsetzbar. Damit rückt ein Teil von OQ-004 zeitlich vor
— von „vor A2/B" auf „vor erstem externem Feldtest".

OQ-009 (Datenretention) wird durch OQ-012 **nicht** geschlossen und OQ-012 nicht durch OQ-009.
OQ-009 betrifft GPS-, Health- und Live-Daten; OQ-012 betrifft Telemetrie-Rohereignisse der
Empfehlungsfunktion — ein eigener Datentyp mit eigener Aufbewahrungsfrage (Punkt 4 und 5 der
OQ-012-Liste). Wer eine der beiden Fristen aus der anderen ableitet, überträgt eine Entscheidung,
die nicht getroffen wurde.

OQ-010 (Moderations-SLA) berührt OQ-012 an einer Stelle: moderativ verborgene Empfehlungen sind
aus dem Nenner von CAN-130 ausgeschlossen. Ohne definierte Moderationswege ist nicht bestimmbar,
wann eine Empfehlung als „vollständig unsichtbar" gilt — OQ-010 ist damit eine Vorbedingung für
die saubere Nennerbildung, nicht nur für den Betrieb.

OQ-009 (Datenretention) wird durch DEC-013 nur **teilweise** vorweggenommen: für den
Koordinaten-Payload des Proxys ist die Retention auf 0 festgelegt und für technische Logs auf
max. 7 Tage. Für GPS-Verläufe, Health- und Live-Daten auf dem Gerät und später serverseitig
bleibt OQ-009 unverändert offen.
