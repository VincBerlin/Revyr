# REVYR Target Architecture

Status: proposed – READY_FOR_USER_CONFIRMATION  
true-line-status: `pending-watcher` (kein selbst ausgestelltes Plumbline-Verdikt)

Letzte Korrektur: 2026-07-19 — Routing-Architekturgrenze (Abschnitt 9), Trennung von Identität
und historischen Aggregaten (Abschnitt 15), minimierte Anti-Cheat-Signale (Abschnitt 16).
Diese Änderungen dokumentieren ausschließlich; in diesem Lauf wurde kein Code geschrieben, kein
Verzeichnis angelegt und keine AWS-Ressource erzeugt.

## 1. Architecture Drivers

- zuverlässiges Foreground-/Background-GPS auf iOS und Android
- getrennte Run-/Bike-Metriken ohne doppelte Screens
- offline-first Aktivitätsspeicherung und spätere Synchronisation
- erklärbare, versionierte Health- und Scoring-Formeln
- Geo-/Realtime-Fähigkeit ab späteren Releases
- Privacy by default und Datenminimierung
- testbare Domainlogik und reale Hardware-Evidence

## 2. Mobile Stack

- Expo / React Native / TypeScript strict
- expo-router
- native Dev-Builds und EAS Profiles; Expo Go nur für begrenzte frühe UI-Smokes
- Zustand oder gleichwertiger kleiner State-Container für UI-/Sessionzustand
- SQLite mit versionierten Migrationen für Aktivitäten, Tracks und Sync Queue
- Jest/Testing Library plus Property Tests für Geo-/Scoringlogik

## 3. Module Boundaries

```text
app/                 Navigation und Screen-Komposition
src/components/      wiederverwendbare UI
src/domain/          pure Regeln, keine Device-/Network-Imports
src/config/          SportConfig, Theme, Feature Flags, Versionen
src/services/        Location, Routing, Health, BLE, Backend, Share
src/db/              SQLite, Migrationen, Repositories, Sync Queue
src/state/           Session- und UI-Zustand
src/telemetry/       technische, datensparsame Messwerte
```

Screens dürfen keine Scoring-, GPS-Filter-, Route-Progress- oder Territory-Formeln enthalten.

`src/services/routing/` enthält ausschließlich den `RoutingClient` gegen die Proxy-Basis-URL —
keinen Providernamen, keinen Provider-Key, keine Provider-Antworttypen (Abschnitt 9.1).

## 4. Core Data Contracts

```ts
export type Sport = 'run' | 'ride';

export interface TrackPointV1 {
  latitude: number;
  longitude: number;
  timestampMs: number;
  accuracyMeters: number | null;
  altitudeMeters: number | null;
  speedMps: number | null;
  headingDegrees: number | null;
  source: 'foreground' | 'background' | 'wearable' | 'import';
  isMocked: boolean | null;
  quality: 'raw' | 'accepted' | 'low-confidence' | 'rejected';
}

export interface ActivityV1 {
  id: string;
  schemaVersion: 1;
  sport: Sport;
  status: 'active' | 'paused' | 'completed' | 'recovered' | 'discarded';
  startedAtMs: number;
  endedAtMs: number | null;
  movingDurationMs: number;
  elapsedDurationMs: number;
  distanceMeters: number;
  routeId: string | null;
  plannedDistanceMeters: number | null;
  verificationStatus: 'local-only' | 'verified-high' | 'verified-standard' | 'low-confidence' | 'review-required' | 'rejected';
}
```

Trackpunkte werden in Chunks/Rows persistiert und nicht als ein einzelnes JSON-Feld behandelt.

## 5. Tracking State Machine

```text
idle → starting → tracking ↔ paused → stopping → completed
                    ↓             ↘
                 recovering ← app restart / crash
                    ↓
                  failed
```

Jeder Übergang ist idempotent, persistiert und getestet. Ein zweiter Start darf keine parallele Session erzeugen.

## 6. Sport Configuration

```ts
interface SportConfig {
  sport: Sport;
  primaryMetric: 'pace' | 'speed';
  autoPauseSpeedMps: number;
  distanceIntervalMeters: number;
  defaultGoalRangeKm: readonly [number, number];
  territoryMinimumContributionMeters: number;
}
```

Run und Bike verwenden dieselben Komponenten, lesen aber ausschließlich aus `SportConfig`.

**Korrektur 2026-07-19 — `routingProfile` entfernt.** Frühere Fassungen führten
`routingProfile: 'foot-walking' | 'cycling-regular'` app-seitig in `SportConfig`. Das
widerspricht CAN-093 und CAN-094: `foot-walking` und `cycling-regular` sind Providerprofil-Namen
und dürfen laut bestätigter Nutzerentscheidung vom 2026-07-19 nicht in Domain- oder UI-Code
gelangen. Die Abbildung `run → foot-walking` / `ride → cycling-regular` liegt ausschließlich im
Routing-Proxy (Abschnitt 9.4). Die App kennt nur `sport: 'run' | 'ride'`.
Dies schließt den in `docs/ID-REGISTRY.md`, CAN-094 (`notes`), vermerkten Klärungspunkt an den
Architektur-Owner.

## 7. Route Progress Algorithm

1. GPS-Punkt filtern.
2. Punkt auf ein lokales Fenster der geplanten Polyline projizieren.
3. Distanz entlang der Polyline bis zur Projektion berechnen.
4. Fortschritt mit Hysterese gegen GPS-Rücksprünge stabilisieren.
5. Restdistanz entlang der verbleibenden Polyline berechnen.
6. Seitlichen Abstand zur Route als Off-Route-Wert bewerten.
7. Bei deutlicher Umkehr eine explizite Rückwärts-/Neuberechnungsentscheidung treffen.

`plannedDistance - trackedDistance` ist ausdrücklich nicht zulässig.

## 8. Local Persistence

- SQLite mit `schema_migrations`.
- `active_sessions`, `activities`, `track_points`, `routes`, `route_points`, `health_samples`, `sync_queue`.
- Session-Journal nach Zeit- oder Punktintervall.
- atomarer Abschluss der Aktivität.
- Recovery liest letzte konsistente Session und zeigt Nutzerentscheidung.

AsyncStorage ist nur für kleine Preferences wie Theme oder letzter Sportmodus zulässig.

**Local-first (präzisierter Wortlaut, CAN-095, Nutzerentscheidung 2026-07-19).**
Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal. Für die
Routenberechnung dürfen ausschließlich die erforderlichen Wegpunkte transient an einen
kontrollierten Routing-Proxy übertragen werden. Der Proxy speichert keine Koordinaten oder
Routengeometrien dauerhaft.

Diese Präzisierung ist die einzige zulässige Abweichung vom lokalen Default in A0/A1. Sie
erweitert den Proxy nicht auf Aktivitäts-, Health- oder Verlaufsdaten (Abschnitt 9.2).

## 9. Routing Architecture Boundary

Grundlage: DEC-005 (`user-confirmed`, 2026-07-19), CONTRA-002 (`resolved`), OQ-011 (vom Nutzer am
2026-07-19 entschieden), CAN-091 bis CAN-097, REQ-006, REQ-007, REQ-034, NFR-007.
Status des zugehörigen Widerspruchs: **CONTRA-006 = DESIGN-RESOLVED / EVIDENCE-PENDING**
(blockierend für die A0-Routing-Implementierung, siehe Abschnitt 9.9).

**Überholte Aussagen, hiermit ersetzt.** Die frühere Fassung dieses Abschnitts erlaubte einen
„eingeschränkten, rotierbaren Public Key im Development“ und verortete den Proxy erst in der
„Produktion“. Beides ist durch DEC-005 überholt: Der Proxy existiert ab A0, und ein Routing-Key
als `EXPO_PUBLIC_*`-Variable ist ausgeschlossen — `EXPO_PUBLIC_*` wird ins JS-Bundle inlined und
ist aus jedem Build extrahierbar (CAN-092).

### 9.1 Grenze in einem Satz

Die Mobile-App enthält **keinen** Routing-Provider-Key und **keinen** Providernamen. Sie kennt
ausschließlich eine konfigurierbare Proxy-Basis-URL, einen providerneutralen `RoutingPort` und
einen `RoutingClient`, der diesen Port implementiert.

```text
UI / Screens
   │  kennt nur Domain-Typen
Domain (src/domain/route*)          ← kein Provider-, kein HTTP-, kein Proxy-Wissen
   │  RoutingPort (Interface, providerneutral)
RoutingClient (src/services/routing/)
   │  HTTPS an ${ROUTING_PROXY_BASE_URL}/v1/route
──────────────── Architekturgrenze ────────────────
Routing-Proxy (infra/routing-proxy/, AWS Lambda + API Gateway, eu-central-1)
   │  hält den Provider-Key, übersetzt sport → Providerprofil, normalisiert die Antwort
Routinganbieter (Name und Rohantwort enden hier)
```

Verbindlich:
- Providername, Providerprofil-Bezeichner, Provider-URLs, Provider-Fehlertexte und
  Provider-Rohantworten dürfen **nicht** in `src/domain/`, `src/config/`, `src/components/`,
  `app/` oder in Zustandsspeichern auftauchen. Sie enden im Proxy.
- `RoutingPort` ist das einzige Routing-Vokabular der Domain. Ein Providerwechsel darf **keine**
  Domain- oder UI-Datei berühren.
- Die Proxy-Basis-URL ist Konfiguration (`src/config/`), kein Secret. Sie ist keine Rechtfertigung
  dafür, weitere Werte client-seitig zu hinterlegen.

### 9.2 Was der Client senden darf — abschließende Liste

Zulässig: `sport` (`'run' | 'ride'`), die für die Berechnung erforderlichen Koordinaten, die
notwendigen Routingparameter, eine technisch erforderliche Request-ID.

Ausdrücklich **nicht** zulässig: Benutzername, E-Mail, Account-ID, Health-Daten,
Aktivitätsverlauf, vollständiger GPS-Track, Team- oder Profildaten, Gerätekennungen (sofern nicht
zwingend erforderlich).

### 9.3 Request- und Response-Form

Vorschlag, noch nicht bestätigt. Die Feldlisten unten sind eine Architekturableitung aus der
Nutzerentscheidung vom 2026-07-19, keine bestätigte Schnittstellenspezifikation.

```ts
// Client → Proxy
export interface RouteRequestV1 {
  schemaVersion: 1;
  sport: Sport;                                  // 'run' | 'ride' — niemals ein Providerprofil
  waypoints: readonly { lat: number; lon: number }[];
  options?: RoutingOptionsV1;                    // Allowlist: MISSING, siehe unten
  requestId: string;                             // zufällig, nicht personenbeziehbar, nicht persistent
}

// Proxy → Client (Erfolg): normalisiert, providerfrei
export interface RouteResultV1 {
  schemaVersion: 1;
  requestId: string;
  distanceMeters: number;
  durationSeconds: number;
  geometry: readonly { lat: number; lon: number }[];
}

// Proxy → Client (Fehler): normalisiert, keine Provider-Interna
export interface RouteErrorV1 {
  schemaVersion: 1;
  requestId: string;
  code:
    | 'invalid_input'
    | 'too_many_waypoints'
    | 'payload_too_large'
    | 'rate_limited'
    | 'upstream_timeout'
    | 'upstream_error'
    | 'routing_disabled';
  message: string;                               // nutzergeeignet, deutsch, ohne Interna
  retryAfterSeconds?: number;
}
```

- `RoutingOptionsV1` — **MISSING.** Welche Routingparameter erlaubt sind, ist aus keinem Artefakt
  ableitbar und hängt an OQ-004 (Karten-/Routinganbieter). Kein Parameter wird hier geraten. Bis
  zur Entscheidung gilt: nur Parameter, die für die angeforderte Berechnung zwingend notwendig
  sind, und keine, die zusätzliche Personen- oder Kontextdaten transportieren.
- `RouteResultV1` enthält bewusst **kein** Feld für Providername, Provider-Antwortobjekt,
  Provider-Request-URL oder Provider-Fehlercode.
- Der Client behandelt jede Antwort als nicht vertrauenswürdig, bis sie gegen dieses Schema
  validiert ist (Validierung an der Systemgrenze).

### 9.4 Sportmodus → Providerprofil

Die Übersetzung findet **ausschließlich im Proxy** statt (CAN-094):

| App sendet | Proxy übersetzt nach |
|---|---|
| `run` | `foot-walking` |
| `ride` | `cycling-regular` |

Die rechte Spalte existiert nirgends im App-Code. Ein unbekannter `sport`-Wert führt zu
`invalid_input`, nicht zu einem Default-Profil.

### 9.5 Proxy-Kontrollen

Alle Kontrollen sind verbindlich und dürfen die Datenschutzzusagen aus 9.6 nicht aushebeln —
insbesondere darf Missbrauchsschutz nicht zu dauerhafter Koordinatenspeicherung führen.

| Kontrolle | Zweck | Schwellwert |
|---|---|---|
| Koordinatenvalidierung | Lat/Lon-Bereich, endliche Zahlen, kein NaN, plausible Anzahl | **MISSING** (Plausibilitätsgrenzen nicht entschieden) |
| Wegpunkt-Limit | begrenzt Kosten und Payload | **MISSING** (Höchstzahl nicht entschieden) |
| Request-Size-Limit | verhindert überdimensionierte Bodies | **MISSING** (Byte-Grenze nicht entschieden) |
| Rate Limiting | Missbrauch und Kostenexplosion | **MISSING** (Rate und Fenster nicht entschieden) |
| Timeout gegen den Provider | verhindert hängende Lambdas | **MISSING** (Millisekunden nicht entschieden) |
| Kill Switch | sofortige Abschaltung des Routings ohne Deployment | Zustand an/aus; Antwort `routing_disabled` |
| Normalisierte Fehler | kein Providerfehler ungefiltert an den Client | Codeliste aus 9.3 |
| Keine Secret-Leaks | Provider-Key nur serverseitig | Pass/Fail |
| Keine Koordinaten in Standardlogs | keine Standortrekonstruktion aus Logs | Pass/Fail |
| Keine dauerhafte Routenspeicherung | Zweckbindung | Retention 0 |

Die als **MISSING** markierten Schwellwerte sind aus keinem vorhandenen Artefakt ableitbar. Sie
werden hier bewusst nicht geraten; sie sind vor der A0-Routing-Implementierung zu entscheiden.

### 9.6 Datenfluss, Retention und Logging

**Zweckbindung.** Start-, Ziel- und Wegpunktkoordinaten werden ausschließlich transient zur
angeforderten Routenberechnung verarbeitet. Keine Werbung, keine Profilbildung, keine
Produktanalyse, keine Trainingsanalyse, keine Standortstatistik, keine Wiederverwendung, kein
Modelltraining, kein Verkauf und keine Weitergabe.

**Retention des Koordinaten-Payloads:** Application 0, Cache 0, Analytics 0. Keine
anwendungsseitige Persistenz von Koordinaten, berechneter Route oder vollständigen Request-/
Response-Bodies.

**Logging.** Request- und Response-Bodies werden nicht geloggt.

| Nicht in Logs, Traces oder Fehlermeldungen | Zulässig in technischen Logs |
|---|---|
| Latitude, Longitude | zufällige Request-ID |
| Wegpunktlisten | Zeitstempel |
| vollständige Provider-URLs mit Koordinaten | HTTP-Status |
| Routengeometrien | Verarbeitungsdauer |
| Start-/Zieladressen | Routingprofil |
| — | Anzahl Wegpunkte |
| — | normalisierte Fehlerkategorie |
| — | Provider-Latenz |
| — | Rate-Limit-Ereignis |

Technische Logs dürfen in keiner Kombination eine Standortrekonstruktion ermöglichen.
Aufbewahrung technischer Logs: **max. 7 Tage**, sofern keine nachgewiesene technische oder
gesetzliche Notwendigkeit für eine andere Frist besteht; eine Abweichung braucht eine
dokumentierte Entscheidung. IP-Adressen nur soweit technisch erforderlich, ohne dauerhafte
Speicherung und ohne Verknüpfung mit Routenanfragen; separat zu dokumentieren.

**Transport und Secrets.** Nur HTTPS/TLS, keine unverschlüsselten Endpunkte. Provider-Key
ausschließlich serverseitig, nie in App, Repository oder Logs. Secrets über AWS Secrets Manager
oder verschlüsselte Lambda-Environment-Variablen, restriktive IAM-Rechte, Rotation und Widerruf
möglich.

**Fehlerbehandlung.** Ein Providerfehler erreicht den Client nie ungefiltert. Die Fehlerantwort
enthält nur internen Fehlercode, nutzergeeignete Nachricht, Request-ID und gegebenenfalls einen
Retry-Hinweis — keine Provider-Secrets, keine internen URLs, keine Koordinaten, keine
vollständigen Providerantworten, keine Stack Traces.

### 9.7 Zielstruktur `infra/routing-proxy/` — nur dokumentiert

Ablageort laut Nutzerentscheidung vom 2026-07-19 zu OQ-011: `infra/routing-proxy/`,
**ausdrücklich nicht** `backend/`. Begründung des Nutzers: begrenzte, austauschbare
Infrastrukturkomponente; `backend/` bleibt für Stufe B reserviert (CAN-097).

```text
infra/routing-proxy/
  src/
    handler.ts             # API-Gateway-Einstiegspunkt, orchestriert nur
    routing-provider.ts    # einziger Ort mit Providername, Provider-URL und Key-Zugriff
    validation.ts          # Koordinaten-, Wegpunkt- und Size-Validierung
    rate-limit.ts          # Rate Limiting und Kill-Switch-Auswertung
    response-mapper.ts     # Providerantwort → RouteResultV1 / RouteErrorV1
  tests/
  package.json
  tsconfig.json
  infrastructure/          # IaC-Definition (nicht ausgerollt)
  README.md
```

> **Dieses Verzeichnis existiert nicht und wurde in diesem Lauf nicht angelegt.** Der Block oben
> ist eine Zielbeschreibung. Es wurde keine Datei darin erzeugt, kein Code geschrieben, kein
> Deployment ausgeführt und keine AWS-Ressource angelegt. Die Datei-Aufteilung folgt der
> Nutzervorgabe vom 2026-07-19 und hat keine eigene CAN-ID (siehe 9.9).

`routing-provider.ts` ist die einzige Datei im gesamten Repository, die den Providernamen kennt.
`response-mapper.ts` ist die einzige Stelle, an der eine Providerantwort in `RouteResultV1`
übergeht; danach existiert die Rohantwort nicht mehr.

### 9.8 A0-Laufzeit

- AWS Lambda und API Gateway (CAN-096).
- Region **eu-central-1**.
- Provider-Key nur serverseitig; Rate Limit, Timeout und Kill Switch aktiv.

**Hinweispflicht zur Bezeichnung.** Die Bezeichnung „EU-Proxy“ darf nicht den Eindruck erwecken,
die gesamte Verarbeitung liege in der EU, wenn der nachgelagerte Routinganbieter außerhalb
verarbeitet. Vor dem ersten externen Feldtest sind zusätzlich zu dokumentieren:
Verarbeitungsregion des Anbieters, ob Daten den EWR verlassen, Unterauftragsverarbeiter und
Transfergrundlage.

### 9.9 Offene Punkte dieses Abschnitts

- **CONTRA-006 bleibt DESIGN-RESOLVED / EVIDENCE-PENDING.** Der Datenfluss ist entworfen, die
  Evidence nicht erbracht. Die entscheidenden Nachweise (Test gegen Logs, Rate-Limit-Test,
  Secret-Scan des Bundles) setzen lauffähigen Code voraus, der in diesem Lauf ausgeschlossen war.
  CONTRA-006 ist damit **nicht** `RESOLVED`. Er blockiert die A0-Routing-Implementierung.
- **MISSING:** sämtliche Schwellwerte aus 9.5 und die Parameter-Allowlist `RoutingOptionsV1`.
- **MISSING (vor erstem externem Feldtest):** Providerbedingungen — Rollenverteilung
  Controller/Processor, Auftragsverarbeitungsvertrag, Unterauftragsverarbeiter,
  Verarbeitungsregion, Provider-Retention, Ausschluss eigener Werbe-, Profiling- und
  Trainingszwecke, Lösch- und Sicherheitsregeln. Ein Anbieter, der das nicht erfüllt, darf nicht
  für produktive oder externe A0-Tests eingesetzt werden. Abhängig von OQ-004.
- **MISSING (vor erstem externem Feldtest):** Rechtsgrundlage und Transparenzangaben —
  Verantwortlicher, Zweck, Rechtsgrundlage, Empfänger/Auftragsverarbeiter,
  Übermittlungsregionen, Speicherdauer, Betroffenenrechte, Datenschutzkontakt. Die
  Datenschutzerklärung muss vor Nutzung der Routenplanung verständlich erklären: „Zur Berechnung
  deiner Route werden die ausgewählten Start-, Ziel- und Wegpunkte kurzfristig an unseren
  EU-Routing-Proxy und den eingesetzten Routinganbieter übermittelt. Die App speichert diese
  Koordinaten im Proxy nicht dauerhaft.“
- **BLOCKER (ID-Raum):** Für die Proxy-Kontrollen aus 9.5 (Koordinatenvalidierung,
  Wegpunkt-Limit, Request-Size-Limit, normalisierte Fehler, Logging-Verbote) existiert **kein**
  atomares Canvas-Item. CAN-096 deckt nur Rate Limit, Timeout und Kill Switch ab. Ebenso hat die
  Dateiaufteilung aus 9.7 keine eigene ID. Die ID-Registry ist eingefroren; hier wurde keine ID
  vergeben. Vergabe ist Sache eines künftigen Registry-Laufs.
- **OPEN QUESTION (nicht von diesem Dokument entschieden):** CAN-131 beschreibt A0 weiterhin als
  lokale Stufe, während der A0-Proxy serverseitig Wegpunkte verarbeitet. CAN-095 präzisiert
  local-first, hebt die Spannung aber nicht auf.

## 10. Health Architecture

- Rohdaten bleiben lokal, sofern ein Serverzweck nicht nachgewiesen ist.
- Score-Version und Eingabesignale werden gespeichert.
- Ausgabe enthält Score, Reasons, Confidence und fehlende Signale.
- Claims-Copy kommt aus einer freigegebenen, lintbaren Whitelist.
- fehlende HF reduziert Confidence, blockiert aber keine Aktivität.

## 11. Backend Decision Gate

Vor Stufe B wird ein Prototyp mit denselben Tests für Kandidaten gebaut:

- Apple-/Google-/E-Mail-Auth
- Postgres-/Geo-Query im Radius
- Row-Level-Security
- Realtime-Kanal
- EU-Region
- Push/Storage
- Kosten- und Lock-in-Modell

Supabase/PostGIS ist ein Kandidat, keine vorweggenommene Entscheidung.

## 12. Geo and Territory

- Team-Areale: versionierte reale Polygone; internes Raster nur für Berechnung.
- Einzel-Reviere: PostGIS-Operationen serverseitig, Eventlog und Geometrieversionen. Das Eventlog
  ist nach Finalisierung fachlich unveränderbar, außer aufgrund Löschung, Anonymisierung oder
  rechtlicher Korrektur (Abschnitt 15).
- Viewport Queries, räumliche Indizes, vereinfachte Geometrien und später Vector Tiles.
- Gleichstände und konkurrierende Captures werden transaktional mit deterministischem Tie-Break verarbeitet.

## 13. Security and Privacy

- private Profile als Default
- Start-/Endpunkt-Unschärfe
- Block-Listen in allen Reads/Realtime-Kanälen
- RLS und serverseitige Authorization
- Rate Limits und Abuse Detection
- kein Versand von Roh-HF-Verläufen für Anti-Cheat; nur notwendige aggregierte Signale
  (abschließende Signalliste in Abschnitt 16)
- dokumentierte Retention und vollständige Löschung (Löschumfang in Abschnitt 15)
- Routing: keine dauerhafte Koordinatenspeicherung, keine Koordinaten in Logs (Abschnitt 9.6)

## 14. Observability

Technische Metriken ohne unnötige Standort-/Health-Inhalte:
- Sessionstartfehler
- Location-Lücken
- GPS-Qualitätsverteilung
- Batteriemessung aus Testläufen
- Routing-Latenz/Fehler
- Recovery-Erfolg
- Crashfreie Sessions

Produktanalytics für Health- oder Standortdaten werden separat datenschutzgeprüft.

## 15. Trennung von Identität und historischen Aggregaten

Grundlage: CONTRA-005, Grundsatzentscheidung des Nutzers vom 2026-07-19.
Status: **RESOLVED (Entscheidung)** — Implementierungs-Evidence steht aus.
Betroffene Requirements: REQ-017 (Accountlöschung), REQ-027 (Seasons/Historie), REQ-034
(Datenschutz), NFR-006.

### 15.1 Zeitpunkt — dies gilt vor dem Schema, nicht danach

Diese Trennung ist **vor** Erstellung und Finalisierung des Datenbankschemas zu berücksichtigen.
Sie ist keine spätere Migration. Ein Schema, das Historieneinträge direkt an eine Personen-ID
hängt, ist nachträglich nicht mehr sauber löschbar — deshalb prägt diese Entscheidung Schema und
Sync von Anfang an und nicht erst zu Stufe D.

### 15.2 Sprachregelung — „unveränderliche Historie“ ist ersetzt

Die Formulierung „unveränderliche Historie“ wird projektweit ersetzt durch:

> Nach Finalisierung fachlich unveränderbar, außer aufgrund Löschung, Anonymisierung oder
> rechtlicher Korrektur.

Das gilt auch für Eventlogs, Snapshots, Trophäen, Zeitreise und Vereinsheim (Abschnitt 12 und
`docs/implementation/revyr-delivery-plan.md`, Abschnitt 9).

### 15.3 Technische Trennung

Datenmodell und Event-Historie müssen Identität und historische Aggregate technisch trennen: Ein
historischer Eintrag verweist auf einen auflösbaren Akteursbezug, nicht auf eingebettete
Personendaten. Wird die Person gelöscht, verliert der Eintrag seinen Personenbezug, ohne dass das
Aggregat zerbricht.

```text
identity domain                     history domain
───────────────                     ──────────────
Profil, E-Mail, Auth-Identitäten    Team-Gesamtstände (aggregiert)
Geräte-/Push-Tokens                 Season-Statistiken (nicht personenbezogen)
private Routen                      Capture-Ereignisse (anonymisierbar)
rohe GPS-Verläufe                   Gebiets-/Teamwerte (aggregiert)
Health-Daten, Stimmungseinträge
Live-Sessions
personenbezogene Kommentare/Medien

        └── auflösbarer Bezug, kein eingebetteter Personendatensatz ──┘
```

Beispiel für die Wirkung: „Vincent eroberte Gebiet X.“ wird nach Löschung zu
„Gelöschtes Mitglied eroberte Gebiet X.“

### 15.4 Was eine Accountlöschung entfernt

Die Accountlöschung entfernt sämtliche personenbezogenen Daten und Identitätszuordnungen,
mindestens: Profil, E-Mail, Auth-Identitäten, Geräte- und Push-Tokens, private Routen, rohe
GPS-Verläufe, Health-Daten, Stimmungseinträge, Live-Sessions, personenbezogene Kommentare und
Medien sowie die Verknüpfungen zwischen Historieneinträgen und der gelöschten Person.

### 15.5 Was erhalten bleiben darf — und die harte Grenze

Historische Team- und Season-Daten dürfen **nur** erhalten bleiben, wenn sie wirksam anonymisiert
sind und keine Rückführung mehr möglich ist: anonymisierte Team-Gesamtstände, nicht
personenbezogene Season-Statistiken, anonymisierte Capture-Ereignisse, aggregierte Gebiets- und
Teamwerte.

**Ist wirksame Anonymisierung nicht möglich, MUSS der Datensatz gelöscht werden.** Erhaltung ist
die Ausnahme, nicht der Default; im Zweifel wird gelöscht.

Offen (**MISSING**): das Prüfverfahren für „wirksam anonymisiert“ — insbesondere ab welcher
Gruppengröße ein Aggregat als nicht rückführbar gilt. Kein Schwellwert ist aus den Artefakten
ableitbar; hier wird keiner geraten. Abhängig von OQ-009 (Datenretention).

## 16. Anti-Cheat-Signale und Datenminimierung

Grundlage: CONTRA-004, Grundsatzentscheidung des Nutzers vom 2026-07-19.
Status: **RESOLVED (Entscheidung)** — Implementierungs-Evidence steht aus.
Betroffene Requirements: REQ-024, REQ-034; verwandt: DEC-007, RISK-013, RISK-022, CAN-104,
CAN-109. Ergänzt Abschnitt 13.

Rohsensorverläufe bleiben standardmäßig **lokal auf dem Gerät**. Der Server erhält für
Wettbewerb, Rankings, Territory und Anti-Cheat ausschließlich minimierte, abgeleitete
Plausibilitätssignale.

| Zulässig an den Server (abgeleitet, minimiert) | Nicht standardmäßig an den Server |
|---|---|
| Kadenzmittel und Kadenzband | vollständige HF-Verläufe |
| Geschwindigkeitsband | vollständige Schrittverläufe |
| optionales HF-Band (sofern vorhanden und freigegeben) | vollständige Rohsensorserien |
| GPS-Qualitätswert | unnötige Health-Rohdaten |
| Accuracy-Zusammenfassung | zusätzliche personenbezogene Daten |
| Teleport-Indikatoren | |
| Bewegungsplausibilität | |
| Distanz, Dauer, Sportart | |
| Verifikations-Confidence | |

Verifikationsstatus: `verified-high`, `verified-standard`, `low-confidence`, `review-required`,
`rejected`. Die Werte entsprechen `ActivityV1.verificationStatus` in Abschnitt 4.

Regeln:
- **Fehlende Sensoren sind kein Betrug.** Sie dürfen die Beweiskraft senken
  (`low-confidence`), aber nicht automatisch zu `rejected` führen.
- Eindeutige Teleports, physikalisch unmögliche Geschwindigkeiten oder klar widersprüchliche
  Sensordaten dürfen zu `review-required` oder `rejected` führen.
- Weitergehende Rohdatenverarbeitung nur nach ausdrücklichem Opt-in **oder** für eine konkrete
  Einspruchs- beziehungsweise Betrugsprüfung — zeitlich begrenzt, mit dokumentiertem Zweck und
  definierter Löschung.

Offen (**MISSING**): die konkreten Schwellwerte für Teleport-Erkennung, physikalische
Geschwindigkeitsgrenzen je Sportart und die Zuordnung von Signalkombinationen zu den fünf
Verifikationsstufen. Diese Werte sind aus keinem Artefakt ableitbar und hängen an OQ-008;
REQ-024 ist im Messmodell als RESEARCH_HYPOTHESIS geführt. Hier wird kein Wert geraten.

## 17. Status, offene Punkte und Grenzen dieses Dokuments

- **Owner: BLOCKER.** Dieses Dokument hat keinen benannten Owner. OQ-002 (finaler
  Repository-Owner/DRI) ist **MISSING**. Kein stiller Nullwert: Die Architekturentscheidungen
  hier sind organisatorisch unzugeordnet, bis OQ-002 entschieden ist.
- **Kein Watcher-Verdikt.** `true-line-status` bleibt `pending-watcher`. Dieses Dokument stellt
  sich keines aus.
- **Keine Selbstbestätigung.** Höchster hier erreichbarer Status ist
  `READY_FOR_USER_CONFIRMATION`.
- **CONTRA-006** bleibt DESIGN-RESOLVED / EVIDENCE-PENDING und blockiert die
  A0-Routing-Implementierung (Abschnitt 9.9).
- **CONTRA-004** und **CONTRA-005** sind als Grundsatzentscheidung RESOLVED; ihre
  Implementierungs-Evidence steht aus.
- **Keine ID vergeben.** `docs/ID-REGISTRY.md` ist eingefroren und wurde von diesem Dokument nur
  gelesen. Wo eine benötigte ID fehlt, steht ein BLOCKER statt einer erfundenen ID.
