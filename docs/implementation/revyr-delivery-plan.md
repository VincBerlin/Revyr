# REVYR Delivery Plan

Status: READY_FOR_USER_CONFIRMATION  
true-line-status: `pending-watcher` (kein selbst ausgestelltes Plumbline-Verdikt)  
Feature Slug: `revyr-endurance-platform`  
Supersedes: den bisherigen technischen „Run&Bike — Tracking + Planned Routes Implementation Plan“ als verbindlichen Umsetzungsplan.

Letzte Korrektur: 2026-07-20 — Nachzug der deprecateten IDs REQ-014 (zwei Fundstellen: P0-01 und
A0-Scope) und REQ-040 auf ihre Nachfolger; Release-Zuordnung von Workstream A0.4 korrigiert;
A2-Scope um REQ-039/REQ-041/REQ-042 ergänzt; unzulässiger `status`-Wert
`DESIGN-RESOLVED / EVIDENCE-PENDING` an drei Stellen auf die zwei Achsen aufgelöst.
Vorherige Korrektur: 2026-07-19 — Repository-Struktur (Abschnitt 2), Local-first-Präzisierung
(Abschnitt 2.2), A0-Routing-Evidenzliste als Gate-Bedingung (Abschnitt 4), Sprachregelung zur
Historie (Abschnitt 9). In diesem Lauf wurde ausschließlich dokumentiert: kein Code, kein
Verzeichnis, kein Deployment, keine AWS-Ressource.

## 1. Delivery Principles

1. **Health-first, evidence-first:** Das Produkt startet als verlässlicher Tracker; Spiel und Social dürfen keine instabile Trackingbasis kaschieren.
2. **Eine Architektur, zwei Sportwelten:** Run und Bike teilen Komponenten, aber nie unpassende Metriken oder Schwellen.
3. **Native Risiken früh:** Background Location, Health, BLE, Widgets und Store-Berechtigungen werden auf echten Geräten geprüft, nicht erst am Ende.
4. **Keine Scheinklarheit:** Offene Provider-, Claims-, Marken- und Geschäftsentscheidungen werden als Gates geführt.
5. **Kein Task ohne Requirement und Evidence:** Jeder Task verweist auf REQ/AC/EV und aktualisiert das Ledger.

## 2. Repository Structure

**Korrektur 2026-07-19.** Die frühere Fassung führte nur `backend/  # ab Stufe B` und ein
undifferenziertes `infra/`. Das war falsch: Der Routing-Proxy existiert bereits ab **A0** und
liegt laut bestätigter Nutzerentscheidung zu OQ-011 in `infra/routing-proxy/` —
**ausdrücklich nicht** in `backend/`. Begründung des Nutzers: begrenzte, austauschbare
Infrastrukturkomponente; `backend/` bleibt für Stufe B reserviert (CAN-097, DEC-005, CONTRA-002).

```text
mobile/
  app/                         # expo-router routes, dünne Screens
  src/domain/                  # reine, versionierte Regeln
  src/config/                  # sport, theme, feature flags, Proxy-Basis-URL
  src/services/                # location, routing (nur RoutingClient), health, BLE, backend
  src/db/                      # SQLite, migrations, repositories, sync queue
  src/state/                   # UI/session stores
  src/components/              # wiederverwendbare UI
  src/telemetry/               # privacy-sichere technische Messungen
infra/
  routing-proxy/               # AB A0 — serverseitiger Routing-Proxy (Zielstruktur, s. u.)
  …                            # weitere: migrations, policies, environments
backend/                       # RESERVIERT FÜR STUFE B — Auth, Geo, Realtime, Moderation.
                               # In A0/A1/A2 existiert hier nichts. Der Routing-Proxy
                               # gehört NICHT hierher.
docs/                          # Vision, Canvas, PRD, ADRs, Evidence, Risiken
```

### 2.1 Zielstruktur `infra/routing-proxy/` — nur dokumentiert

```text
infra/routing-proxy/
  src/handler.ts               # API-Gateway-Einstiegspunkt
  src/routing-provider.ts      # einziger Ort mit Providername, Provider-URL und Key-Zugriff
  src/validation.ts            # Koordinaten-, Wegpunkt- und Size-Validierung
  src/rate-limit.ts            # Rate Limiting und Kill Switch
  src/response-mapper.ts       # Providerantwort → normalisiertes Ergebnis / normalisierter Fehler
  tests/
  package.json
  tsconfig.json
  infrastructure/              # IaC-Definition (nicht ausgerollt)
  README.md
```

> **Dieses Verzeichnis existiert nicht und wurde in diesem Lauf nicht angelegt.** Der Block ist
> eine Zielbeschreibung für eine spätere Implementierungsphase. A0-Laufzeit: AWS Lambda und API
> Gateway, Region eu-central-1 (CAN-096) — ebenfalls nur dokumentiert, nicht bereitgestellt.
> Details der Architekturgrenze: `docs/architecture/revyr-target-architecture.md`, Abschnitt 9.

Die Mobile-App enthält keinen Routing-Provider-Key. Sie kennt nur eine konfigurierbare
Proxy-Basis-URL, einen providerneutralen `RoutingPort` und einen `RoutingClient`. Providername
und Providerantwort dürfen nicht in Domain- oder UI-Code gelangen (CAN-093). Die Übersetzung
`run → foot-walking` und `ride → cycling-regular` liegt im Proxy (CAN-094).

### 2.2 Local-first — präzisierter Wortlaut

Verbindliche Formulierung (CAN-095, Nutzerentscheidung 2026-07-19). Sie ersetzt jede pauschale
Aussage, A0/A1 sei „vollständig lokal“ oder „ohne Backend“:

> Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal. Für die
> Routenberechnung dürfen ausschließlich die erforderlichen Wegpunkte transient an einen
> kontrollierten Routing-Proxy übertragen werden. Der Proxy speichert keine Koordinaten oder
> Routengeometrien dauerhaft.

Diese Präzisierung erweitert den Proxy nicht auf Aktivitäts-, Health- oder Verlaufsdaten.
CONTRA-006 bleibt trotz dieser Präzisierung blockierend. **Statuswert korrigiert 2026-07-20:** der
frühere Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` ist als `status` nach Registry §3.1
unzulässig; er trug zwei Fragen in einem Feld. Die kanonischen Achsen lauten `status = resolved`
(die Grundsatzfrage ist entschieden), `evidence_status = pending`, `blocked_gates = [A0]`,
`blocked_activities = [field-test, release]` → `blocking = true` am eigenen Gate.

## 3. Phase 0 — Entscheidungen und technische Basis

**Ziel:** Alte Identität und falsche technische Annahmen entfernen, bevor Feature-Code entsteht.

| Task | Requirement | Output | Acceptance |
|---|---|---|---|
| P0-01 | REQ-001, **REQ-038** | neutraler interner App-Slug, Bundle-/Scheme-Konvention, Theme- und Sport-Config | kein öffentlicher Arbeitstitel in hardcodierten Plattform-IDs · **MISSING: für den Output „Theme- und Sport-Config" existiert keine Acceptance-Bedingung** (siehe Befund unten) |
| P0-02 | REQ-004 | `TrackPointV1` mit accuracy, altitude, speed, heading, source und mocked/quality flags | Schema + Fixtures + Serialisierungstest |
| P0-03 | REQ-005, REQ-017, REQ-027 | SQLite-Spike, Migrationen, Session-Journal, Trackpoint-Chunks | Kill-/Recovery-Prototyp ohne Datenverlust; Identität und historische Aggregate im Schema getrennt (CONTRA-005) |
| P0-04 | REQ-006, REQ-007 | Routing-ADR, Proxy-Schnittstellenvertrag und Route-Progress-Prototyp | Routeprojektion, Off-Route und Rückwärtsfall getestet; App kennt nur `sport`, Wegpunkte und Proxy-Basis-URL |
| P0-05 | REQ-034 | Secret-/API-Key-Strategie und Datenflussdiagramm inkl. Routing-Proxy | **kein** Routing-Key im Client — auch nicht im Development |
| P0-06 | REQ-035 | CI, Evidence-Ledger-Template, PR-Checkliste | kein Merge bei fehlenden Tests/REQ-Links |

**Nachzug 2026-07-20 zu P0-01 — das deprecatete REQ-014 aufgelöst.** REQ-014 („Designsystem und
Accessibility") ist seit dem 2026-07-19 `deprecated` und in **REQ-037** (Accessibility) und
**REQ-038** (monochromes tokenbasiertes Designsystem) zerlegt (Registry §6.4, §7.4). Dieser Plan
führte es an **zwei** Stellen weiter aktiv — hier und im A0-Scope in Abschnitt 4. Frühere Berichte
nannten nur eine der beiden Fundstellen; beide sind jetzt aufgelöst.

**Warum P0-01 ausschließlich REQ-038 erhält — fachlich entschieden, nicht aufgeteilt geraten.**
Der Output von P0-01 ist Konfiguration: App-Slug, Bundle-/Scheme-Konvention sowie Theme- und
Sport-Config. Die **Theme-Config ist der Träger des tokenbasierten Designsystems** und damit
REQ-038. **REQ-037 wird hier ausdrücklich NICHT gesetzt:** Accessibility ist Verhalten auf
ausgelieferten Screens (Screenreader, Fokusführung, Dynamic Type, Bedienflächen) und in P0
weder herstellbar noch prüfbar. Sie beginnt mit Workstream A0.1 und ist dort verankert. Ein
REQ-037 an P0-01 würde eine Accessibility-Abdeckung behaupten, für die es in P0 keinen Nachweis
und keine Acceptance-Bedingung gibt.

**BEFUND, nicht mitrepariert: P0-01 hat keine Acceptance-Bedingung für seinen Designsystem-Anteil.**
Die Acceptance lautet ausschließlich „kein öffentlicher Arbeitstitel in hardcodierten
Plattform-IDs" — das prüft den Slug (REQ-001), nicht die Theme-Config. Die Bedingung, unter der
die Token-Basis als geliefert gilt, ist **MISSING**. Sie wird hier **nicht erfunden**; AC-038 und
EV-038 definieren die Prüfung auf Requirement-Ebene, eine Task-Acceptance leitet sich daraus
nicht automatisch ab.

**Zeitpunktregel zu P0-03 (CONTRA-005).** Die technische Trennung von Identität und historischen
Aggregaten gilt **vor** Finalisierung des Datenbankschemas — nicht erst zu Stufe C oder D, in der
Teams, Seasons und Territory entstehen. Ein Schema, das Historieneinträge direkt an eine
Personen-ID hängt, ist nachträglich nicht mehr sauber löschbar. Details:
`docs/architecture/revyr-target-architecture.md`, Abschnitt 15.

**Korrektur 2026-07-19 zu P0-05.** Die frühere Akzeptanz lautete „Produktionsschlüssel nicht im
Client; Development-Ausnahme dokumentiert“. Diese Development-Ausnahme ist durch DEC-005
(`user-confirmed`) entfallen: `EXPO_PUBLIC_*` wird ins JS-Bundle inlined und ist aus jedem Build
extrahierbar; ein Development-Key wäre damit derselbe Defekt in kleinerer Auflage (CAN-092).
NFR-007 gilt ab A0.

**Gate P0:** Architekturentscheidungen dokumentiert; alter Plan 1 ist ausdrücklich `superseded`.

## 4. A0 — Tracking Core

**Scope:** REQ-001–REQ-008, **REQ-037** (Accessibility-**Basis**), **REQ-038** (monochromes
tokenbasiertes Designsystem, erstmalige Abnahme mit Gate A0), anwendbare Teile REQ-034–REQ-036.

**Nachzug 2026-07-20 — zweite REQ-014-Fundstelle.** Dies ist die zweite der beiden Stellen, an
denen das deprecatete REQ-014 aktiv geführt wurde. Hier erhalten **beide** Nachfolger einen
Eintrag, anders als bei P0-01: die Registry weist REQ-037 „Accessibility-Basis ab A0, vollständiger
Audit spätestens A2" zu und REQ-038 „Release A0–A2, erstmalige Abnahme mit GATE-A0". Beide sind auf
A0 fällig, mit unterschiedlichem Umfang — die Aufteilung ist damit belegt, nicht gewählt.

**Geltungsbereich von REQ-008 in A0 — verengt.** REQ-008 trägt in A0 **ausschließlich Verlauf und
Detailansicht** (Canvas-Anker CAN-138). **GPX-Export (REQ-039), Wiederverwendung gespeicherter
Routen (REQ-041) und Aktivitätsvergleich (REQ-042) gehören NICHT zu A0** — alle drei sind auf
Release **A2** geführt. Der frühere Alttext von REQ-008 („gespeicherte Routen, Streckenvergleich
und GPX-Export werden unterstützt") ist seit dem 2026-07-19 nicht mehr sein Umfang.

### Workstream A0.1 — Scaffold und Domain
- Expo/React Native/TypeScript strict mit Dev-Build-Profilen.
- SportConfig für Run/Bike.
- Geo-, Stats-, Speed/Pace-, Filter- und Route-Progress-Domainmodule.
- Design-Tokens und Accessibility-Basis.

### Workstream A0.2 — Session Engine
- explizite Zustände: `idle`, `starting`, `tracking`, `paused`, `recovering`, `stopping`, `failed`.
- Vordergrund- und Hintergrund-Location in dieselbe Session-Pipeline.
- sportabhängige Auto-Pause und Samplingwerte.
- periodische Journaling-Persistenz.

### Workstream A0.3 — Planung und Navigation
- Wegpunkte und Distanzziel.
- Routeberechnung ausschließlich über `RoutingPort`/`RoutingClient` gegen den Routing-Proxy;
  kein Provider-SDK und kein Provider-Key in der App.
- Projektion auf Polyline statt `planned - covered`.
- Off-Route-Status und optionaler Audiohinweis hinter Feature Flag.

### Workstream A0.5 — Routing-Proxy (`infra/routing-proxy/`)
Eigener Workstream, weil der Proxy ab A0 existiert und nicht Teil des Mobile-Scaffolds ist.
- Schnittstellenvertrag Request/Response/Fehler (normalisiert, providerfrei).
- Übersetzung `run → foot-walking`, `ride → cycling-regular` serverseitig.
- Kontrollen: Koordinatenvalidierung, Wegpunkt-Limit, Request-Size-Limit, Rate Limiting,
  Timeout, Kill Switch, normalisierte Fehler.
- Logging ohne Koordinaten; Retention des Koordinaten-Payloads 0 (Application, Cache, Analytics);
  technische Logs max. 7 Tage.
- Secrets serverseitig (AWS Secrets Manager oder verschlüsselte Lambda-Env), restriktive IAM,
  Rotation möglich.
- Laufzeit AWS Lambda + API Gateway, Region eu-central-1.

> **Konkrete Schwellwerte sind MISSING** — Wegpunkt-Höchstzahl, Byte-Grenze, Rate und Fenster,
> Timeout in Millisekunden sowie die Allowlist erlaubter Routingparameter sind aus keinem
> Artefakt ableitbar und werden hier nicht geraten. Sie sind vor Beginn dieses Workstreams zu
> entscheiden (abhängig von OQ-004).

### Workstream A0.4 — Verlauf und Detailansicht
- Activity/Route Repositories auf SQLite.
- Verlauf und Detailansicht lokal gespeicherter Run- und Bike-Aktivitäten (REQ-008, CAN-138,
  AC-008, **EV-008**). Die Detailansicht zeigt Route, Dauer, Distanz und die
  **sportartspezifische** Kernmetrik — Run zeigt Pace, Bike zeigt Geschwindigkeit.

> **Korrektur 2026-07-20 — dieser Workstream führte drei A2-Funktionen in A0.** Die frühere
> Fassung lautete „Verlauf, Detail, gespeicherte Routen, Vergleich" und „GPX-Export mit
> Datenminimierung". Damit standen **GPX-Export (REQ-039)**, **Wiederverwendung gespeicherter
> Routen (REQ-041)** und **Aktivitätsvergleich (REQ-042)** in einem A0-Workstream, obwohl alle
> drei auf Release **A2** geführt werden. Sie sind nach Abschnitt 6 (A2) verschoben. Der
> Workstream-Titel „Verlauf und Export" war dadurch ebenfalls irreführend und lautet jetzt
> „Verlauf und Detailansicht".
>
> **Der Vergleich ist zusätzlich nicht implementierbar:** ohne die Vergleichbarkeits- und
> Streckenähnlichkeitsdefinition aus **OQ-015** ist AC-043 nicht vollständig spezifizierbar.
> OQ-015 führt `blocked_activities = [implementation]` — ein A0-Workstream hätte diese Blockade
> mechanisch nicht gefunden, weil er gegen ein Gate und nicht gegen die Tätigkeit prüft.

**Gate A0:**
- je Sport und Plattform 30 Minuten mit gesperrtem Bildschirm;
- App-Kill ohne Punktverlust;
- Distanzabweichung <3 % auf Referenzstrecke;
- dokumentierter Batteriewert;
- Bike zeigt km/h, Run zeigt min/km;
- routebezogener Fortschritt besteht Umweg-/Rückwärts-Fixtures;
- **die A0-Routing-Evidenzliste unten ist vollständig erbracht.**

### Gate-Bedingung A0-Routing — Evidenzliste

Diese Liste ist Gate-Bedingung, nicht Empfehlung. Gate A0 besteht nicht, solange eine Zeile offen
ist. Sie adressiert CONTRA-006, der bis dahin `status = resolved` bei `evidence_status = pending`,
`blocked_gates = [A0]` und `blocked_activities = [field-test, release]` trägt und damit
blockierend für die A0-Routing-Implementierung bleibt (Statuswert korrigiert 2026-07-20; der
frühere Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` ist als `status` unzulässig).

| # | Nachweis | Bestehenskriterium | REQ | EV-Anker |
|---|---|---|---|---|
| R-01 | Bundle-Scan eines Release-Builds (iOS und Android) | kein Routing-Provider-Key, kein Providername, keine Provider-URL im Bundle | REQ-034 | EV-034 |
| R-02 | Statische Prüfung der Importgrenze | kein Provider-Bezeichner in `src/domain/`, `src/config/`, `src/components/`, `app/`; `foot-walking`/`cycling-regular` kommen im App-Code nicht vor | REQ-006, REQ-034 | EV-006 |
| R-03 | Vertragstest Client→Proxy | Request enthält ausschließlich `sport`, Wegpunkte, erlaubte Parameter, Request-ID — nichts sonst | REQ-006, REQ-034 | EV-006 |
| R-04 | Profilübersetzung im Proxy | `run → foot-walking`, `ride → cycling-regular`; unbekannter Sportwert ergibt normalisierten Fehler, kein Default-Profil | REQ-006 | EV-006 |
| R-05 | Koordinatenvalidierung | ungültige Lat/Lon, NaN und Grenzwerte werden abgewiesen | REQ-006, REQ-034 | EV-006 |
| R-06 | Wegpunkt-Limit | Überschreitung ergibt `too_many_waypoints`, kein Provideraufruf | REQ-034 | EV-034 |
| R-07 | Request-Size-Limit | überdimensionierter Body wird vor Providerkontakt abgewiesen | REQ-034 | EV-034 |
| R-08 | Rate-Limit-Test | Limitüberschreitung ergibt `rate_limited`; kein Koordinaten-Log dabei | REQ-034 | EV-034 |
| R-09 | Timeout-Test | Providerverzögerung ergibt `upstream_timeout` statt hängender Anfrage | REQ-006 | EV-006 |
| R-10 | Kill-Switch-Test | Abschaltung ohne Deployment wirkt; App zeigt verständlichen Zustand | REQ-006 | EV-006 |
| R-11 | Log-Inspektion nach Testlauf | in Logs, Traces und Fehlermeldungen keine Latitude, Longitude, Wegpunktliste, Routengeometrie, vollständige Provider-URL oder Start-/Zieladresse | REQ-034 | EV-034 |
| R-12 | Retention-Nachweis | Koordinaten-Payload: Application 0, Cache 0, Analytics 0; keine persistierte Routengeometrie | REQ-034 | EV-034 |
| R-13 | Log-Aufbewahrung | technische Logs max. 7 Tage oder dokumentierte, begründete Abweichung | REQ-034 | EV-034 |
| R-14 | Fehlerdurchreichung | Providerfehler erreicht den Client nie ungefiltert: kein Secret, keine interne URL, keine Koordinate, kein Stack Trace | REQ-006, REQ-034 | EV-034 |
| R-15 | Transport und Secrets | nur HTTPS/TLS; Key ausschließlich serverseitig; kein Secret in Repository oder Logs; Rotation nachgewiesen | REQ-034 | EV-034 |
| R-16 | Region | Lambda und API Gateway in eu-central-1 nachgewiesen | REQ-034 | EV-034 |
| R-17 | Reale Routenszenarien | zehn reale Szenarien **je Sportart getrennt** (Run und Bike) über den Proxy | REQ-006 | EV-006 |
| R-18 | Providerbedingungen dokumentiert | Controller/Processor-Rollen, AV-Vertrag, Unterauftragsverarbeiter, Verarbeitungsregion, Provider-Retention, Ausschluss eigener Werbe-/Profiling-/Trainingszwecke, Lösch- und Sicherheitsregeln | REQ-034 | EV-034 |
| R-19 | Transferlage dokumentiert | Verarbeitungsregion des Anbieters, ob Daten den EWR verlassen, Transfergrundlage; die Bezeichnung „EU-Proxy“ erweckt keinen falschen Eindruck | REQ-034 | EV-034 |
| R-20 | Transparenz vor erstem externem Feldtest | Verantwortlicher, Zweck, Rechtsgrundlage, Empfänger, Übermittlungsregionen, Speicherdauer, Betroffenenrechte, Datenschutzkontakt; Datenschutzerklärung erklärt die Wegpunktübermittlung vor Nutzung der Routenplanung | REQ-034 | EV-034 |

**BLOCKER zum ID-Raum.** R-01 bis R-20 sind Nachweise, keine registrierten Evidence-Items. Die
Spalte „EV-Anker“ nennt nur die bestehenden Oberitems EV-006 (REQ-006) und EV-034 (REQ-034); für
die einzelnen Nachweise existiert **keine eigene EV-ID**. `docs/ID-REGISTRY.md` ist eingefroren,
deshalb wurde hier keine ID vergeben und keine erfunden. Die Vergabe ist Sache eines künftigen
Registry-Laufs.

R-18 bis R-20 hängen an OQ-004 (Karten-/Routinganbieter) und sind ohne diese Entscheidung nicht
erbringbar. Ein Anbieter, der R-18 nicht erfüllt, darf nicht für produktive oder externe A0-Tests
eingesetzt werden.

## 5. A1 — Health Foundation

**Scope:** REQ-009–REQ-013.

1. HealthKit/Health Connect lesen und Workouts schreiben.
2. BLE-HF-Adapter mit sauberem Verbindungsstatus.
3. Belastungs-Score als versionierte reine Funktion.
4. Confidence-Modell: vollständige HF, teilweise HF, kein HF.
5. Warum-Sheet mit Gründen, fehlenden Signalen und Orientierungssprache.
6. Zonen, optionale Ansage, Check-in und Trendkarten.
7. Claims-Lint in CI.

**Gate A1:** echte Aktivitäten iOS/Android; Score mit und ohne HF; kein Tracking-Block bei fehlender Hardware; freigegebene Copy.

## 6. A2 — Public v1.0 Experience

**Scope:** REQ-015–REQ-016, **REQ-039** (GPX-Export), **REQ-041** (Wiederverwendung einer
gespeicherten Route), **REQ-042** (Vergleich fachlich vergleichbarer Aktivitäten), **REQ-037**
(vollständiger WCAG-2.2-AA-Audit), **REQ-038** (Designsystem-Abnahme) und vollständige
Store-/Privacy-Anforderungen.

- Basis-Avatar lokal; keine kaufbaren Items.
- Wochenrückblick und Erfolgskarten.
- iOS Live Activities / Android Foreground Notification und Widget.
- Onboarding, Permission Education und Datenexport.
- finaler öffentlicher Name, Store-Texte, Privacy Policy und Testtracks.

### Aus A0 nach A2 verschoben (Nachzug 2026-07-20)

Diese drei Funktionen standen zuvor in Workstream A0.4. Sie sind eigenständige Requirements mit
Release **A2** und werden hier **getrennt** geführt, weil sie unabhängig voneinander bestehen oder
scheitern können.

| Task | Requirement | Output | Acceptance / Evidence | Blockiert durch |
|---|---|---|---|---|
| A2-EX | **REQ-039** | GPX-Export einer abgeschlossenen Run- oder Bike-Aktivität mit Datenminimierung, ohne Veröffentlichung oder Social-Freigabe | AC-039, **EV-039** ([G1]…[G8] im Evidence Ledger) | **OQ-016** — die Referenz-Fremdanwendung für [G4] ist MISSING; es wird keine App geraten |
| A2-RU | **REQ-041** | erneute Verwendung einer gespeicherten Route als Grundlage einer geplanten Aktivität | AC-042, **EV-043** ([RU1]…[RU6]) | — **nicht blockiert**; vollständig spezifizierbar |
| A2-VG | **REQ-042** | Gegenüberstellung fachlich vergleichbarer Aktivitäten anhand sportartspezifischer Kennzahlen | AC-043, **EV-044** ([VG1]…[VG6]) | **OQ-015** — Vergleichbarkeits- und Streckenähnlichkeitsdefinition MISSING; `blocked_activities = [implementation]` |

**Warum drei Tasks und nicht einer.** REQ-040 („Streckenwiederverwendung und Aktivitätsvergleich")
ist am 2026-07-20 als Composite `deprecated` und in REQ-041 und REQ-042 zerlegt worden. Der
tragende Grund ist hier operativ sichtbar: **A2-RU ist heute umsetzbar, A2-VG nicht.** Ein
gemeinsamer Task hätte die lieferbare Hälfte an der blockierten mitblockiert — oder, schlimmer,
die blockierte Hälfte über die lieferbare als erledigt gelten lassen.

**Run und Bike werden in allen drei Tasks getrennt nachgewiesen.** A2-VG vergleicht **nie**
sportartübergreifend.

**Gate A2:** Store-Einreichung erst nach Naming-Entscheid und vollständiger Evidence.
Zusätzlich: **EV-039, EV-043 und EV-044 sind Gate-A2-Bedingungen.** EV-044 kann vor der
Entscheidung von OQ-015 nicht einmal als Testfall beziffert werden — das ist kein offener Rest,
sondern eine Gate-Blockade.

## 7. B — Platform and Social

**Scope:** REQ-017–REQ-019.

1. Backend-Prototyp vergleicht Geo, Realtime, Apple Login, EU-Region und RLS.
2. ADR entscheidet Provider; Empfehlung ist keine Vorentscheidung.
3. Auth und lokale Datenmigration.
4. Offline-first Upload Queue und Konfliktregeln.
5. Profile/Sichtbarkeit/Block/Report/Moderation.
6. Routenempfehlungen und berechtigter Feed.

Ab dieser Stufe entsteht `backend/`. Der bereits ab A0 bestehende `infra/routing-proxy/` wird
dadurch **nicht** nach `backend/` verschoben und präjudiziert den Backend-Entscheid (OQ-005)
nicht.

**Gate B:** Registrierung → Offline-Aktivität → Sync → Empfehlung → Übernahme → Löschung mit zwei Accounts.

Die Löschprüfung folgt CONTRA-005: Sie entfernt Profil, E-Mail, Auth-Identitäten, Geräte-/
Push-Tokens, private Routen, rohe GPS-Verläufe, Health-Daten, Stimmungseinträge, Live-Sessions,
personenbezogene Kommentare und Medien sowie die Verknüpfungen zwischen Historieneinträgen und
der gelöschten Person. Erhaltene historische Aggregate müssen nachweislich anonymisiert sein
(„Gelöschtes Mitglied eroberte Gebiet X.“); ist wirksame Anonymisierung nicht möglich, muss der
Datensatz gelöscht werden.

## 8. C — Teams and Fair Competition

**Scope:** REQ-020–REQ-025.

- Teamtransaktionen, Einladungen, Admin und aktive Mitgliedschaft.
- gemeinsame Aktivität als pure Funktion.
- Effort-Simulation vor produktiver Punktevergabe.
- Anti-Cheat mit Confidence und manueller Review-Stufe.
- idempotente Challenges, Rankings und Rewards.

**Gate C:** Simulation, Betrugs-Fixtures, Zwei-Geräte-Test und kein Doppelreward.

## 9. D — Territory, Seasons and Live Safety

**Scope:** REQ-026–REQ-031.

### D1 Team Territory
Arealdefinition, Quorum, Effort, Rendering, Performance und Seasons.

### D2 Individual Territory
Erst nach separater Spezifikation:
- Tracksegmentierung in Anfahrt/Runde/Rückweg;
- Ringbildung und Mindestfläche;
- deterministische Priorität vollständige Einnahme > Teilübernahme > Gleichstand;
- atomare PostGIS-Operationen;
- Geometrieversion und Eventlog — nach Finalisierung fachlich unveränderbar, außer aufgrund
  Löschung, Anonymisierung oder rechtlicher Korrektur (CONTRA-005);
- Start-/End-Unschärfe und Sichtbarkeit.

### D3 Sports Venues
- nur öffentlich zugängliche und kuratierte Orte;
- Access-/Opening-Hours-Prüfung;
- Bahngold als Score, nicht als Währung;
- GPS-Toleranz, Startlinie und physiologische Mindestzeiten.

### D4 Live and Safety
Threat-Model, Ende aller Freigabepfade, Beschützer-Link, Realtime-Budget, Sturzerkennung mit Fehlalarmquote.

**Gate D:** Geo-Simulation, Lasttest, Privacy-Review, echte Bahn-/Live-/Safety-Gerätetests.

## 10. E — Wearables and Guidance

**Scope:** REQ-032–REQ-033.

- Watch-Companions und Bike-Sensoren anhand einer verbindlichen Matrix.
- Recovery/Coach/Wetter/Zyklus nur nach Claims- und Privacy-Gate.
- Regelbasierte Erklärbarkeit vor lernenden Modellen.

## 11. Definition of Ready per Task

Ein Task startet nur, wenn:
- REQ-, AC- und EV-ID existieren;
- Abhängigkeiten erfüllt sind;
- Datenschutz-/Claims-Auswirkung bewertet ist;
- Teststrategie und reale Geräte benannt sind;
- offene Produktentscheidung nicht versteckt wird.

## 12. Definition of Done per Task

- Tests grün und relevante Domainlogik vollständig abgedeckt.
- reale iOS-/Android-Nachweise, sofern Plattformcode betroffen ist.
- Run und Bike getrennt geprüft.
- Evidence Ledger aktualisiert.
- ADR/Schema/API-Dokumentation aktualisiert.
- keine offenen Critical-/High-Defects.
- Requirement- und Traceability-Status aktualisiert.

## 13. Status, offene Punkte und Grenzen dieses Plans

- **Owner: BLOCKER.** Kein Task in diesem Plan hat einen benannten Owner. OQ-002 (finaler
  Repository-Owner/DRI) ist **MISSING** und als Default „Umsetzung bleibt organisatorisch
  unzugeordnet“ geführt. Das ist hier sichtbar vermerkt und kein stiller Nullwert.
- **CONTRA-006:** `status = resolved` (entschieden), `evidence_status = pending`,
  `blocked_gates = [A0]`, `blocked_activities = [field-test, release]` → **`blocking = true`**,
  blockierend für die A0-Routing-Implementierung. **Entschieden ist nicht nachgewiesen.** Der
  frühere Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` war als `status` unzulässig (Registry
  §3.1) und ist am 2026-07-20 an allen drei Fundstellen dieser Datei aufgelöst. Die Evidenzliste
  in Abschnitt 4 ist die Bedingung, unter der er geschlossen werden kann.
- **BLOCKER (deprecatete IDs, Nachzug 2026-07-20 erledigt in dieser Datei, offen anderswo):**
  REQ-014 stand hier an **zwei** Stellen aktiv (P0-01 und A0-Scope); beide sind auf REQ-037 /
  REQ-038 aufgelöst. REQ-040, AC-040, EV-040, CAN-140 und TRC-040 kommen in dieser Datei nicht
  vor. In **anderen** Dateien laufen beide Deprecation-Wellen noch: REQ-014/AC-014/EV-014/TRC-014
  und CAN-071 aus Runde 3, REQ-040/AC-040/EV-040/CAN-140/TRC-040 aus Runde 4. Diese Datei ändert
  fremde Dateien nicht.
- **BLOCKER (Vision-Anker REQ-041):** A2-RU ist technisch vollständig spezifizierbar, hat aber
  **keinen** Vision-Anker. VIS-014 ist reserviert, Inhalt **MISSING**; TRC-041 ist `broken`.
  VIS-003 wurde geprüft und **verworfen** — es nennt Tracking, Health-Auswertung,
  Fortschrittssignale und Trainingspartner, **keine** Wiederverwendung geplanter Strecken. Es
  wird kein bestehendes Vision-Item umgedeutet, um die Zeile zu schließen.
- **MISSING (P0-01):** für den Output „Theme- und Sport-Config" existiert keine
  Task-Acceptance-Bedingung; die vorhandene prüft nur den App-Slug.
- **CONTRA-004 und CONTRA-005: RESOLVED (Entscheidung)**, Implementierungs-Evidence steht aus.
- **MISSING:** alle Schwellwerte des Routing-Proxys (Wegpunkt-Limit, Size-Limit, Rate, Timeout)
  und die Allowlist erlaubter Routingparameter — abhängig von OQ-004. Nicht geraten.
- **MISSING:** das Prüfverfahren für „wirksam anonymisiert“ nach CONTRA-005 — abhängig von
  OQ-009. Nicht geraten.
- **BLOCKER (ID-Raum):** Die Nachweise R-01…R-20 haben keine eigenen EV-IDs; die ID-Registry ist
  eingefroren und wurde von diesem Plan nur gelesen.
- **ÜBERHOLT und korrigiert 2026-07-20.** Die frühere Fassung dieses Punktes behauptete,
  `docs/decisions/open-questions.md` führe OQ-011 „weiterhin als offen" und
  `docs/decisions/decision-log.md` führe CONTRA-004, CONTRA-005 und CONTRA-006 „noch als `open`".
  **Beides trifft nicht mehr zu** — nachgesehen, nicht angenommen: OQ-011 steht dort als
  `RESOLVED (Nutzer, 2026-07-19)`, und alle drei CONTRA-Einträge stehen auf `resolved`
  (Entscheidung) bei `evidence_status = pending`. Der Satz „Beide Dateien gehören anderen Ownern"
  war zusätzlich falsch: beide gehören demselben Owner wie diese Datei. Ein stehengebliebener
  Nachzugsvermerk, der längst erledigt ist, ist derselbe Defekt wie ein fehlender — er meldet
  einen Zustand, den niemand mehr nachrechnet.
- **Keine Selbstbestätigung.** Höchster hier erreichbarer Status ist
  `READY_FOR_USER_CONFIRMATION`; `true-line-status` bleibt `pending-watcher`.
