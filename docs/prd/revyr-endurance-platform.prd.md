# PRD: REVYR Endurance Platform

Status: `READY_FOR_USER_CONFIRMATION`  
Gesamtstatus des Vorhabens: **`BLOCKED_TRACEABILITY`** — unverändert. Dieser Korrekturlauf hebt die Blockade **nicht** auf; `READY_FOR_AGILETEAM_PLANNING` ist ausgeschlossen.  
True-Line-Status: `pending-watcher` — dieses PRD gibt **kein** Plumbline-Watcher-Verdikt ab und stellt sich keines aus.  
Wired in prod: `no` · Evidence-Class: `none` — **es existiert kein Code im Repository.** Keine Aussage dieses Dokuments ist durch Laufzeitverhalten belegt; `evidence_status = verified` steht bei **keinem einzigen** Nachweis. Der Nenner wird nicht als feste Zahl geführt, sondern aus `docs/ID-REGISTRY.md` abgeleitet (§10.2) — Stand 2026-07-20: **42 aktive** `EV-`Einträge, 2 deprecated, 0 reserviert, 1 `template-placeholder`.  
Feature Slug: `revyr-endurance-platform`  
Owner: MISSING – im Repository zu benennen (OQ-002). Solange OQ-002 offen ist, trägt **jedes** aktive Requirement im Messmodell einen sichtbaren OWNER-BLOCKER statt eines stillen Nullwerts.  
Public Brand: MISSING – REVYR ist vorläufiger Arbeitstitel (OQ-001)  
User Confirmation Required: yes

**ID-Disziplin:** Kanonische Quelle für alle `VIS-`, `CAN-`, `REQ-`, `AC-`, `TRC-`, `EV-`, `RISK-`, `ASM-`, `OQ-`, `CONTRA-`, `USER-` und `NFR-`IDs ist `docs/ID-REGISTRY.md`. Die Registry ist eingefroren; dieses PRD **referenziert** IDs, es vergibt, benennt und deprecated keine. Wo eine benötigte ID fehlt, steht hier ein BLOCKER und keine erfundene Nummer. Die Räume `USER-` und `NFR-` sind seit dem 2026-07-19 registry-verwaltet (Registry §5.1, §6.12, §6.13); der frühere Befund XC-5 („`NFR-` nicht kollisionsgeschützt") ist damit für die Verwaltung erledigt, nicht für die Messdefinition.

### Zählregel — jeder Zählstand ist abgeleitet, keiner ist festgeschrieben

Frühere Fassungen dieses Dokuments trugen feste Requirement-Zahlen als Erwartungswert. Das ist projektweit unzulässig (Registry §2 Regel 11, §9 Bedingung 8, **§10.2**) und hier entfernt. Die Regel gilt seit Runde 4 **nicht nur für `REQ-`**, sondern gleichermaßen für `VIS-`, `CAN-`, `AC-`, `TRC-`, `EV-`, `RISK-`, `ASM-`, `OQ-`, `CONTRA-`, `USER-` und `NFR-`.

```
zaehle(praefix, status) = |{ e ∈ Registry-Definitionstabellen :
                                praefix(e.id) = praefix ∧ e.status = status }|

aktiv(p)       = zaehle(p, "active")               // bzw. "open" für OQ-/CONTRA-
deprecated(p)  = zaehle(p, "deprecated")           // NIE in aktiv() enthalten
reserviert(p)  = zaehle(p, "reserved")             // GETRENNT ausgewiesen, nie addiert
platzhalter(p) = zaehle(p, "template-placeholder") // von jeder Abdeckungsprüfung ausgenommen
```

**Vier Bindungen, wörtlich aus Registry §10.2:**

1. Aktive, deprecatete und reservierte Einträge werden **immer getrennt** ausgewiesen. Eine Gesamtzahl ohne Statusaufschlüsselung ist kein gültiger Zählstand. **Reservierte Einträge sind nie erfüllte Referenzen** und werden nie zur aktiven Zahl addiert.
2. **Kein Literal — weder als Erwartungs- noch als Verbotswert.** Ein Werkzeug, das eine feste Anzahl auf eine Verbotsliste setzt, ist an einen Zählstand gebunden wie eines, das sie erwartet. Beides ist derselbe Defekt.
3. Quelle ist **ausschließlich** `docs/ID-REGISTRY.md`, und zwar nur ihre Definitionstabellen (erkennbar an einer `canonical_file` in Backticks in Spalte 4) — nicht ihre Migrations-, Zähl- oder Befundtabellen.
4. **Wer eine Zahl nennt, nennt Datum und Ableitungsweg.**

**Abgeleiteter Stand 2026-07-20** (gezählt, nicht abgeschrieben; Ableitungsweg: Definitionstabellen der Registry, je Präfix und Statusklasse getrennt):

| Präfix | aktiv | deprecated | reserviert | `template-placeholder` |
|---|---:|---:|---:|---:|
| REQ | **40** | 2 (REQ-014, REQ-040) | 0 | 1 (`REQ-000`) |
| AC | **41** | 2 (AC-014, AC-040) | 0 | 1 (`AC-000`) |
| EV | **42** | 2 (EV-014, EV-040) | 0 | 1 (`EV-000`) |
| TRC | **40** | 2 (TRC-014, TRC-040) | 0 | 0 |
| NFR | **8** | 0 | 0 | 0 |

Herleitung REQ: REQ-001…REQ-042 sind vergeben (42 IDs); **REQ-014** ist `deprecated` (→ REQ-037, REQ-038), **REQ-040** ist seit dem 2026-07-20 `deprecated` (→ REQ-041, REQ-042); `REQ-000` ist ein `template-placeholder` des Evidence Ledgers und **kein** Requirement. 42 − 2 = 40.

⚠️ **AC und EV übersteigen REQ absichtlich.** REQ-019 trägt seit dem 2026-07-19 **zwei** Acceptance Criteria (AC-019 funktional, AC-041 Messkriterium) und **zwei** Evidences (EV-019, EV-041); EV-042 hängt an CONTRA-005/REQ-017/REQ-027. Die Querproben sind erfüllt: `aktiv(TRC) = aktiv(REQ)` (40 = 40) · `aktiv(AC) = aktiv(REQ) + 1` (41 = 41) · `aktiv(EV) = aktiv(REQ) + 2` (42 = 42). Die bisher implizite 1:1-Beziehung REQ↔AC↔EV gilt nicht mehr. **Jede Prüfung, die 1:1 oder eine feste Anzahl erwartet oder verbietet, ist zu korrigieren — nicht die Daten.**

## Source Summary

| Source | Summary |
|---|---|
| SRC-001 | REVYR Vision, Product Canvas und PRD vom 2026-07-16; enthält Produktvision, Zielgruppen, Core Loops, Release-Scope und Feature-Anforderungen. |
| SRC-002 | REVYR Plan-PRD vom 2026-07-16; enthält die bisherige Anforderung-zu-Task- und Gate-Zuordnung. |
| SRC-003 | REVYR Gesamtplan FINAL vom 2026-07-16; enthält Produktidentität, Architekturziel, Release-Fahrplan, Arbeitspakete, Risiken und Evidence Gates. |
| SRC-004 | Run&Bike Tracking + Planned Routes Implementation Plan; technischer TDD-Plan für den frühen Tracking-Prototyp, teilweise veraltet. |
| SRC-005 | Statische Konsistenzprüfung vom 2026-07-18: identifizierte Konflikte bei Branding, Bike-Metriken, GPS-Datenmodell, Routenfortschritt, Persistenz, API-Key-Sicherheit, Traceability und v1-Scope. |

## Problem Statement

| Field | Value | Source Type | Source |
|---|---|---|---|
| Problem Statement | Ausdauersportler erhalten häufig Trackingdaten ohne verständliche Orientierung und Social-Funktionen ohne reale lokale Bindung. Die Produktgrundlage muss zunächst zuverlässig, erklärbar und sicher sein, bevor Wettbewerb und Territory darauf aufbauen. | EXPLICIT | SRC-001/SRC-003 |

## Target Users

| ID | User | Need | Source Type | Source |
|---|---|---|---|---|
| USER-001 | Freizeit-Läufer:in | zuverlässiges Tracking, verständlicher Fortschritt, lokale Trainingspartner | EXPLICIT | SRC-001 |
| USER-002 | Freizeit-/Rennradfahrer:in | Geschwindigkeit, Höhen-/Sensordaten, Routen und faire Bike-Wertung | EXPLICIT | SRC-001/SRC-003 |
| USER-003 | Lokale Sportgruppe oder Verein | Mitglieder, gemeinsame Aktivitäten, Organisation und langfristige Identität | EXPLICIT | SRC-001 |
| **USER-004** | **Ambitionierte Ausdauersportler:innen mit Wearables oder externen Sensoren** | Läufer:innen und Radfahrer:innen, die regelmäßig trainieren, bereits eine Sportuhr, einen Herzfrequenzgurt oder Fahrradsensoren verwenden und erwarten, dass vorhandene Trainingssignale **ohne Medienbruch** in ihre Aktivitäts- und Belastungsauswertung einfließen | **ASSUMPTION** | Canvas-Anker CAN-025; Wortlaut Nutzerentscheidung 2026-07-19 |

**USER-004 nachgezogen (2026-07-19).** Die Canvas-Zielgruppe **CAN-025** („Ambitionierte Ausdauersportler:innen") hatte im PRD keine USER-ID; `docs/traceability.md` vermerkte das bei REQ-009, REQ-011 und REQ-032 als „ambitionierte Persona MISSING im PRD". Die ID ist in `docs/ID-REGISTRY.md` §6.12 vergeben — **vor der Vergabe als frei geprüft**, nicht aus einer Anweisung übernommen. Damit ist Registry §8 Punkt 5 **als ID-Frage** geschlossen.

⚠️ **BLOCKER — USER-004 ist unbestätigt.** `source_type` **ASSUMPTION**: Beschreibung und Abgrenzung gegenüber USER-001/USER-002 sind aus CAN-025 und der Nutzerentscheidung abgeleitet, aber vom Nutzer **nicht als Persona bestätigt**. Bis dahin trägt keine Anforderung USER-004 als *belegten* Zielgruppenanker.

**Keine Universalverknüpfung.** USER-004 wird **nicht** pauschal an alle Requirements gehängt, die Herzfrequenz oder Sensorik berühren. Die semantische Prüfung von REQ-009 und REQ-011 ist im Messmodell je Requirement einzeln dokumentiert und fällt **unterschiedlich** aus.

## Goals

1. Einen stabilen iOS-/Android-Tracker mit sauber getrennten Run/Bike-Erlebnissen veröffentlichen.
2. Health-Auswertungen nachvollziehbar, optional und nicht-diagnostisch gestalten.
3. Community- und Territory-Funktionen nur nach Datenqualitäts-, Anti-Cheat- und Safety-Nachweis freischalten.
4. Vollständige Traceability und Evidence pro Requirement sicherstellen.

## Non-Goals

- Medizinprodukt oder Diagnose.
- Allgemeiner Chat-Messenger.
- Kaufbare Leistungs- oder Territory-Vorteile.
- Territory oder öffentliche Live-Karte im ersten Store-Release.
- Endgültige Festlegung des öffentlichen Namens innerhalb dieses PRD.

## Assumptions

**ID-Migration nachgezogen (2026-07-19).** Die früheren PRD-IDs `ASM-001`…`ASM-004` kollidierten mit gleichnamigen, fachlich unverwandten Annahmen in `docs/vision/revyr-endurance-platform.vision.md` — dasselbe Defektmuster wie zuvor bei den OQ-IDs. `docs/ID-REGISTRY.md` (§6.9, §7.1) hat den Raum getrennt: `ASM-1xx` = Annahmen des PRD, `ASM-2xx` = Annahmen der Vision. Die Alt-IDs bleiben dort als `deprecated` erhalten und werden nicht wiederverwendet.

| Alt-ID (PRD, deprecated) | Neue ID | Bedeutung |
|---|---|---|
| ASM-001 | **ASM-101** | Aufteilung der v1.0 in A0/A1/A2 |
| ASM-002 | **ASM-102** | SQLite statt AsyncStorage |
| ASM-003 | **ASM-103** | A0-Routing über serverseitigen Proxy |
| ASM-004 | **ASM-104** | Einzel-Reviere/Bahngold bis D deaktiviert |

| ID | Assumption | Source Type | Validation |
|---|---|---|---|
| ASM-101 | Der öffentliche v1.0-Release wird intern in A0, A1 und A2 geteilt. | ASSUMPTION | Ressourcen- und Release-Review |
| ASM-102 | SQLite beziehungsweise eine transaktionale lokale Datenbank ersetzt die vollständige Track-Speicherung in AsyncStorage. | ASSUMPTION | technischer Spike |
| ASM-103 | **Für A0 entschieden, nicht mehr offen (Nutzerentscheidung 2026-07-19; DEC-005 `user-confirmed`, CONTRA-002 `resolved`):** Externes Routing läuft bereits ab Stufe A0 ausschließlich über einen minimalen serverseitigen Routing-Proxy; ein Routing-API-Key als `EXPO_PUBLIC_*`-Variable im App-Bundle ist ausgeschlossen. NFR-007 („keine Secrets im Client") gilt damit ab A0. Für Stufen ab A1 bleibt die Annahme „Proxy oder gleichwertiger Schutz" bestehen. | CONFIRMED (A0) / ASSUMPTION (ab A1) | A0: Bundle-Scan ohne Routing-Key plus Proxy-Integrationstest; ab A1: Karten-/Routing-ADR |
| ASM-104 | Einzel-Reviere und Bahngold bleiben bis Stufe D deaktiviert. | ASSUMPTION | Scope-Bestätigung |

### Bestätigte Entscheidung zu A0-Routing (CONTRA-002, DEC-005)

Der Nutzer hat am 2026-07-19 entschieden: Der A0-Routing-Zugriff erfolgt über einen minimalen serverseitigen Proxy, der den Anbieter-API-Key hält und weiterleitet. Damit gilt NFR-007 ab A0 statt erst ab Stufe B, und REQ-006/REQ-007 sind in A0 nur über den Proxy umsetzbar. Quelle: `docs/decisions/decision-log.md`, DEC-005 (`user-confirmed`, 2026-07-19); CONTRA-002 ist dort als `resolved` geführt.

Konsequenz für die Implementierung: Ein Routing-API-Key darf nicht als `EXPO_PUBLIC_*`-Variable geführt werden, da `EXPO_PUBLIC_*` ins JS-Bundle inlined und aus jedem Build extrahierbar ist. Die Angabe `EXPO_PUBLIC_ORS_API_KEY` in der Repository-`CLAUDE.md` widerspricht dieser Entscheidung und muss vom Owner der Datei korrigiert werden; dieses PRD ändert `CLAUDE.md` nicht.

**Ablageort entschieden (OQ-011, Nutzerentscheidung 2026-07-19).** Der A0-Routing-Proxy liegt unter `infra/routing-proxy/` — ausdrücklich **nicht** unter `backend/`. Begründung des Nutzers: begrenzte, austauschbare Infrastrukturkomponente; `backend/` bleibt für Stufe B reserviert. Laufzeit A0: AWS Lambda und API Gateway, Region `eu-central-1`, Provider-Key ausschließlich serverseitig, Rate Limit, Timeout und Kill Switch. Canvas-Anker: CAN-096 (Laufzeit) und CAN-097 (Ablageort).

> **Nur dokumentiert, nicht gebaut.** Weder dieses PRD noch der laufende Korrekturlauf legt `infra/routing-proxy/` an, erzeugt Quelldateien darin, deployt etwas oder erstellt AWS-Ressourcen. Der Pfad existiert hier ausschließlich als dokumentierter Ablageort und als Eintrag im Allowed change scope des Canvas.

**Client-/Proxy-Schnittstelle (Nutzerentscheidung 2026-07-19).** Die Mobile-App enthält **keinen** Routing-Provider-Key. Sie kennt ausschließlich eine konfigurierbare Proxy-Basis-URL, einen providerneutralen `RoutingPort` und einen `RoutingClient` (CAN-093). Providername und Providerantwort dürfen nicht in Domain- oder UI-Code gelangen. Die Übersetzung des Sportmodus in das Providerprofil — `run` → `foot-walking`, `ride` → `cycling-regular` — liegt im Proxy (CAN-094).

**Local-first-Präzisierung (verbindlicher Wortlaut, Nutzerentscheidung 2026-07-19; CAN-095).** Diese Formulierung gilt für jede Stelle in diesem PRD, an der „local-first" oder „lokal" als Datenschutzzusage auftritt — insbesondere REQ-005, REQ-006, REQ-007 und REQ-034:

> Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal. Für die Routenberechnung dürfen ausschließlich die erforderlichen Wegpunkte transient an einen kontrollierten Routing-Proxy übertragen werden. Der Proxy speichert keine Koordinaten oder Routengeometrien dauerhaft.

Ausdrücklich **nicht** mitentschieden und weiterhin offen:

- Der vollständige Backend-Entscheid für Geo, Auth, Realtime und EU-Hosting der sozialen Stufen (OQ-005). Der A0-Proxy ist minimal und darf nicht als Vorentscheidung für die Backend-Plattform gewertet werden.
- Anbieterwahl für Karten/Routing und Kostenlimits (OQ-004).
- Die vollständige Datenschutz-Baseline des Proxys (CONTRA-006): Datenfluss, Providerbedingungen, Logging, Retention, Transparenz, Sicherheitskontrollen und die zugehörige Evidence. Der Entwurf ist entschieden, die Evidence steht aus — siehe Abschnitt „Widerspruchs-Auflösungen": CONTRA-006 trägt `status: resolved` · `resolution_status: accepted` · `evidence_status: pending` · `blocking: true` (Scope `field-test`, `release`; `evidence_gate` A0). Dieser Punkt bleibt blockierend für die A0-Routing-Implementierung.

## Open Questions

Kanonisches Register: `docs/decisions/open-questions.md`. Dieses PRD **referenziert** OQ-IDs, es definiert sie nicht. Bei Abweichung gilt das Register.

| ID | Question | Owner | Needed By | Source Type |
|---|---|---|---|---|
| OQ-001 | Finaler öffentlicher Name und Marke? | Product/Legal | Gate A2 | MISSING |
| OQ-002 | Finaler Repository-Owner/DRI (PRD-Kopfzeile „Owner")? | Product | vor P0 Start | MISSING |
| OQ-003 | Minimum iOS/Android und Referenzgeräte? | Engineering/QA | vor A0 Feldtest | MISSING |
| OQ-004 | Karten-/Routinganbieter und Kostenstrategie? Die Key-Haltung ist ab A0 entschieden (serverseitiger Proxy, siehe ASM-103); Anbieterwahl und Kostenlimits bleiben offen. | Engineering/Product | vor A2/B | MISSING |
| OQ-005 | Backendentscheidung nach Geo/Auth/Realtime-Prototyp? Vom A0-Routing-Proxy unberührt und weiterhin offen. | Engineering | vor B | MISSING |
| OQ-006 | Health-Claims-Whitelist? | Product/Legal | vor A1 Public Beta | MISSING |
| OQ-007 | Monetarisierungsmodell? | Product/Business | vor C | MISSING |
| OQ-011 | Ablageort und Deployment-Ziel des A0-Routing-Proxys im Repository? | Engineering | vor A0-Routing-Implementierung | **RESOLVED** (Nutzer, 2026-07-19): `infra/routing-proxy/`, nicht `backend/`; Laufzeit AWS Lambda + API Gateway, `eu-central-1`. |
| **OQ-012** | Privacy-minimierte Telemetrie für Routenempfehlungen: client- oder serverseitiges `exposed`-Ereignis, nötige Event-Metadaten, speicherbare Daten, Aufbewahrung der Rohereignisse, ab wann nur Aggregate, separate Einwilligung nötig, Wirkung von Profil-Privacy/Blockierungen/Löschungen, Entfernung oder Anonymisierung gelöschter Accounts aus den Messdaten, Owner der Instrumentierung, verwendete Analytics-/Event-Lösung? | MISSING (OQ-002) | vor Gate B | MISSING |
| **OQ-013** | Messdefinition, Zielwert und Gate-Zuordnung für NFR-008 (Wartbarkeit): Metrik, Einheit, Schwellwert, Messfenster, Testmethode, zuständiges Gate, Owner? | MISSING (OQ-002) | offen — kein Gate fordert NFR-008 heute ein | MISSING |
| **OQ-014** | Stichproben- und Auswertungsregel für CAN-130 / AC-041: Mindestzahl auswertbarer Empfehlungen, Mindestzahl berechtigter Empfänger, Mindestdauer des Messfensters, Behandlung von Testkonten, Umgang mit Mehrfachübernahmen desselben Nutzers, Umgang mit gelöschten und moderierten Empfehlungen, getrennte Run-/Bike-Auswertung? | MISSING (OQ-002) | vor Gate B | MISSING |
| **OQ-015** | Vergleichbarkeitsdefinition für den Aktivitätsvergleich — seit dem 2026-07-20 **REQ-042** (vorher REQ-040, deprecated): wann gelten zwei Strecken als vergleichbar, tolerierte Abweichung der Streckenähnlichkeit, verglichene Kennzahlen, Behandlung verkürzter/verlängerter/abgebrochener Aktivitäten? | MISSING (OQ-002) | vor Gate A2 | MISSING |
| **OQ-016** | Referenz-Fremdanwendung für den GPX-Kompatibilitätsnachweis (REQ-039, AC-039 Kriterium d)? | MISSING (OQ-002) | vor Gate A2 | MISSING |

**OQ-012 bis OQ-016 sind im Auftau-Schritt 2 (2026-07-19) in `docs/ID-REGISTRY.md` §6.10 vergeben worden.** Dieses PRD referenziert sie; das kanonische Register bleibt `docs/decisions/open-questions.md`, in dem der Nachzug noch aussteht (BLOCKER für den Owner jener Datei, nicht für dieses PRD).

**Blockierwirkung nach dem kanonischen Modell (Registry §3.1) — Gates und Tätigkeiten werden getrennt geführt und nie gegeneinander verglichen:**

| OQ | `blocked_gates` | `blocked_activities` | ausdrücklich **nicht** blockiert |
|---|---|---|---|
| OQ-012 | `[B]` | `[]` | A0, A1, `documentation` — die Dokumentkorrektur und die Implementierungsplanung laufen weiter |
| OQ-013 | `[]` | `[]` | nichts — **und genau das ist der Befund:** NFR-008 ist an kein Gate gebunden und damit wirkungslos, nicht unbedenklich |
| OQ-014 | `[B]` | `[]` | A0, A1, `documentation` |
| OQ-015 | `[A2]` | `[implementation]` | A0, A1 — **REQ-042** ist erst ab A2 fällig. **REQ-041 ist von OQ-015 ausdrücklich NICHT blockiert** — das ist der operative Grund der Teilung |
| OQ-016 | `[A2]` | `[field-test]` | A0, A1, `documentation` |

⚠️ **BEFUND — die Registry führt für OQ-015 noch die deprecateten Nachfolge-IDs.** `docs/ID-REGISTRY.md` Zeile 1012 (OQ-015-Definitionszeile) und §8 Punkt 28 nennen als betroffene IDs weiterhin **REQ-040, AC-040, EV-040 und CAN-140** — alle vier sind in derselben Runde 4 `deprecated` gesetzt worden (§7.5). Nach Registry §9 Bedingung 3 („kein Dokument referenziert eine ID mit `status = deprecated`") ist das ein Validierungsfehler **in der Registry selbst**. Dieses PRD zieht auf die aktiven Nachfolger **REQ-042, AC-043, EV-044, CAN-143** nach und meldet die Abweichung, statt sie stillschweigend zu spiegeln. **Die Registry ist eingefroren; die Korrektur liegt beim Registry-Owner.** Bis dahin gilt für die reine ID-Frage §1 (Registry), für die Sachfrage die Deprecation derselben Registry — ein Widerspruch, der sichtbar bleibt.

**Statusnachzug offen (BLOCKER für die Owner der jeweiligen Dateien, nicht für dieses PRD).** `docs/ID-REGISTRY.md` (§6.10) führt OQ-011 als `resolved`. `docs/decisions/open-questions.md` führt OQ-011 zum Zeitpunkt dieser Korrektur weiterhin als offen, und `docs/traceability.md` nennt OQ-011 weiterhin als Blocker für REQ-006. Beide Dateien liegen außerhalb der Dateihoheit dieses PRD und wurden hier **nicht** geändert. Bis zum Nachzug widersprechen sich die Register sichtbar; maßgeblich ist laut Registry-Regel die Registry.

## Requirements

| Requirement ID | Requirement | Priority | Release | Source Type | Source |
|---|---|---|---|---|---|
| REQ-001 | **Sportmodus als zentrale Konfiguration:** Das System MUSS Run und Bike über einen globalen Sportmodus und versionierte Konfigurationsobjekte steuern; UI, Metriken, Routing, Auto-Pause, Sampling, Ziele und Rekorde dürfen nicht in Screens dupliziert oder hart codiert werden. | Must | A0 | EXPLICIT | SRC-003 |
| REQ-002 | **Foreground-Tracking:** Die App MUSS eine Run- oder Bike-Aktivität mit einem Tipp starten und GPS-Punkte, Dauer, Distanz, Live-Karte sowie sportgerechte Kernmetrik anzeigen. | Must | A0 | EXPLICIT | SRC-001/SRC-004 |
| REQ-003 | **Background, Pause und Recovery:** Tracking MUSS bei gesperrtem Bildschirm fortlaufen, Pause/Resume und sportabhängige Auto-Pause unterstützen sowie eine laufende Session nach App-Kill oder Absturz wiederherstellen. | Must | A0 | EXPLICIT | SRC-003 |
| REQ-004 | **Erweitertes GPS-Datenmodell und Filter:** Jeder Trackpunkt MUSS mindestens Position, Zeit, Genauigkeit und verfügbare Bewegungsmetadaten speichern; unplausible oder ungenaue Punkte werden durch reine, getestete Filterfunktionen markiert oder ausgeschlossen. | Must | A0 | ASSUMPTION | SRC-005 |
| REQ-005 | **Robuste lokale Aktivitätsspeicherung:** Aktive und abgeschlossene Sessions MÜSSEN versioniert und transaktional in einer lokalen Datenbank gespeichert werden; große Tracks dürfen nicht als einzelnes unversioniertes AsyncStorage-JSON persistiert werden. | Must | A0 | ASSUMPTION | SRC-005 |
| REQ-006 | **Routenplanung:** Nutzer MÜSSEN eine Route über Wegpunkte oder ein Distanzziel planen, das korrekte Run-/Bike-Routingprofil verwenden und den Plan vor dem Start prüfen können. | Must | A0 | EXPLICIT | SRC-001/SRC-004 |
| REQ-007 | **Routenbezogener Fortschritt:** Bei einer geplanten Route MUSS „verbleibend“ entlang der geplanten Geometrie berechnet werden und darf nicht nur Gesamtdistanz minus gelaufene Distanz sein; Abweichung und falsche Richtung müssen erkannt werden. | Must | A0 | ASSUMPTION | SRC-005 |
| REQ-008 | **Verlauf und Detailansicht:** Nutzer MÜSSEN lokal gespeicherte Run- und Bike-Aktivitäten in einem Verlauf anzeigen und eine Detailansicht mit Strecke, Dauer, Distanz und sportartspezifischer Kernmetrik öffnen können. | Must | A0 | **ASSUMPTION** | CAN-138; Wortlaut Nutzerentscheidung 2026-07-19 |
| REQ-009 | **Herzfrequenzquellen:** Die App MUSS Herzfrequenz aus HealthKit, Health Connect oder unterstützten BLE-Sensoren lesen können und Quelle sowie Datenlücken transparent kennzeichnen. | Must | A1 | EXPLICIT | SRC-001/SRC-003 |
| REQ-010 | **Erklärbarer Belastungs-Score mit Confidence:** Nach jeder Aktivität MUSS ein Belastungs-Score mit Gründen, verwendeten Signalen und Confidence-Stufe angezeigt werden; ohne Herzfrequenz wird ein klar begrenzter Fallback verwendet. | Must | A1 | ASSUMPTION | SRC-001/SRC-005 |
| REQ-011 | **HF-Zonen und optionale Ansage:** HF-Zonen MÜSSEN schätzbar und manuell korrigierbar sein; Live-Zonenhinweise und Audio sind optional und vollständig deaktivierbar. | Should | A1 | EXPLICIT | SRC-001/SRC-003 |
| REQ-012 | **Stimmungs-Check-in und Korrelation:** Nach einer Aktivität SOLL ein kurzer Stimmungs-Check-in möglich sein; Korrelationen werden erst nach ausreichender Datenmenge und mit Unsicherheit dargestellt. | Should | A1 | EXPLICIT | SRC-001 |
| REQ-013 | **Health-Home und Steigerungshinweis:** Home MUSS den aktuellen Wochenzustand zeigen und bei deutlich erhöhter Belastung einen orientierenden, nicht diagnostischen Hinweis ausgeben. | Must | A1 | EXPLICIT | SRC-001/SRC-003 |
| ~~REQ-014~~ | **DEPRECATED 2026-07-19 → REQ-037 (Accessibility) und REQ-038 (Monochromes Designsystem).** Siehe Migrationstabelle unten. Neue Referenzen auf REQ-014 sind ein Validierungsfehler. | — | — | — | Registry §6.4 |
| REQ-015 | **Verdiente Avatar-Progression:** Basis-Avatare dürfen frei angepasst werden; leistungsbezogene Items, Teamkleidung und Season-Objekte dürfen nur durch definierte reale Leistungen freigeschaltet und nicht gekauft werden. | Should | A2-B-C | EXPLICIT | SRC-001/SRC-003 |
| REQ-016 | **Recaps, Erfolgskarten und Live-Status:** Die App SOLL Wochenrückblicke, teilbare Erfolgskarten und plattformgerechte Live-Aktivitätsanzeigen bereitstellen, ohne sensible Start-/Endpunkte offenzulegen. | Should | A2 | EXPLICIT | SRC-001/SRC-003 |
| REQ-017 | **Accounts, Auth und Datenmigration:** Ab v2 MÜSSEN E-Mail, Apple und Google Auth, Offline-Sync, Migration lokaler Aktivitäten und vollständige In-App-Accountlöschung unterstützt werden. **Löschumfang (CONTRA-005, Nutzerentscheidung 2026-07-19):** Die Accountlöschung entfernt sämtliche personenbezogenen Daten und Identitätszuordnungen, mindestens Profil, E-Mail, Auth-Identitäten, Geräte- und Push-Tokens, private Routen, rohe GPS-Verläufe, Health-Daten, Stimmungseinträge, Live-Sessions, personenbezogene Kommentare und Medien sowie die Verknüpfungen zwischen Historieneinträgen und der gelöschten Person. Historische Team- und Season-Daten dürfen NUR erhalten bleiben, wenn sie wirksam anonymisiert sind und keine Rückführung mehr möglich ist; ist wirksame Anonymisierung nicht möglich, MUSS der Datensatz gelöscht werden. Datenmodell und Event-Historie MÜSSEN Identität und historische Aggregate technisch trennen — diese Trennung ist **vor** Erstellung und Finalisierung des Datenbankschemas zu berücksichtigen. | Must | B | EXPLICIT | SRC-001/SRC-003 + CONTRA-005 |
| REQ-018 | **Privacy, Sichtbarkeit und Moderation:** Profile sind standardmäßig privat; Follow-Anfragen, Blockieren, Melden, Moderationsqueue, Regeln und Sichtbarkeitsmatrix MÜSSEN ab der ersten Social-Version vollständig funktionieren. | Must | B | EXPLICIT | SRC-001/SRC-003 |
| REQ-019 | **Routenempfehlungen und Feed:** Nutzer SOLLEN neue Routen erkennen, mit strukturierten Hinweisen empfehlen und von berechtigten Followern mit einem Tipp übernehmen lassen können. | Should | B | EXPLICIT | SRC-001/SRC-003 |
| REQ-020 | **Teamgründung und Beitritt:** Teams MÜSSEN transaktional mit Admin entstehen; Beitritt erfolgt über kontrollierbare Links oder QR-Codes mit Ablauf und Deaktivierung. | Must | C | EXPLICIT | SRC-001/SRC-003 |
| REQ-021 | **Aktive Mitglieder und Teamwachstum:** Teamkapazität, Stufen und Mentorbonus MÜSSEN aktive Mitglieder und echte Integration statt bloßer Einladungen belohnen. | Must | C | EXPLICIT | SRC-001/SRC-003 |
| REQ-022 | **Gemeinsame Aktivitäten und Events:** Gemeinsame Aktivitäten MÜSSEN aus Zeit- und räumlicher Überschneidung deterministisch erkannt werden; geplante Gruppenaktivitäten und Events nutzen dieselbe Logik und Moderation. | Must | C-D | EXPLICIT | SRC-001/SRC-003 |
| REQ-023 | **Effort-Normalisierung:** Sportübergreifende Team- oder Territory-Wertungen MÜSSEN versionierte, simulierte Effort-Faktoren verwenden; interne Run- und Bike-Wertungen bleiben in echten sportbezogenen Metriken getrennt. | Must | C | EXPLICIT | SRC-001/SRC-003 |
| REQ-024 | **Anti-Cheat mit Confidence-Stufen und minimiertem Signalumfang:** Aktivitäten MÜSSEN serverseitig auf Geschwindigkeit, Teleports und verfügbare Sensorplausibilität geprüft und als `verified-high`, `verified-standard`, `low-confidence`, `review-required` oder `rejected` klassifiziert werden. **Signalumfang (CONTRA-004, Nutzerentscheidung 2026-07-19):** Rohsensorverläufe bleiben standardmäßig LOKAL auf dem Gerät. Der Server erhält für Wettbewerb, Rankings, Territory und Anti-Cheat ausschließlich minimierte, abgeleitete Plausibilitätssignale: Kadenzmittel und -band, Geschwindigkeitsband, optionales HF-Band (sofern vorhanden und freigegeben), GPS-Qualitätswert, Accuracy-Zusammenfassung, Teleport-Indikatoren, Bewegungsplausibilität, Distanz, Dauer, Sportart und Verifikations-Confidence. NICHT standardmäßig an den Server: vollständige HF-Verläufe, vollständige Schrittverläufe, vollständige Rohsensorserien, unnötige Health-Rohdaten, zusätzliche personenbezogene Daten. Weitergehende Rohdatenverarbeitung ausschließlich nach ausdrücklichem Opt-in ODER für eine konkrete Einspruchs-/Betrugsprüfung, zeitlich begrenzt, mit dokumentiertem Zweck und definierter Löschung. Fehlende Sensoren allein sind KEIN Betrug: sie dürfen die Beweiskraft senken (`low-confidence`), aber nicht automatisch zu `rejected` führen. Eindeutige Teleports, physikalisch unmögliche Geschwindigkeiten oder klar widersprüchliche Sensordaten dürfen zu `review-required` oder `rejected` führen. | Must | C | ASSUMPTION | SRC-003/SRC-005 + CONTRA-004 |
| REQ-025 | **Challenges, Rankings und idempotente Rewards:** Wochen-Challenges, sportgetrennte Rankings, Meilensteine und Rewards MÜSSEN serverkonfigurierbar, nachvollziehbar und idempotent sein. | Must | C | EXPLICIT | SRC-001/SRC-003 |
| REQ-026 | **Team-Territory:** Ab v4 dürfen nur verifizierte Beiträge und ein Quorum reale, benannte Team-Areale beeinflussen; internes Raster bleibt unsichtbar und Kartenlayer müssen performant filterbar sein. | Must | D | EXPLICIT | SRC-001/SRC-003 |
| REQ-027 | **Seasons und nach Finalisierung fachlich unveränderbare Historie:** Seasons MÜSSEN nur das aktive Spielfeld zurücksetzen; Snapshots, Trophäen, Vereinsheim und Zeitreise bleiben erhalten und sind **nach Finalisierung fachlich unveränderbar, außer aufgrund Löschung, Anonymisierung oder rechtlicher Korrektur** (CONTRA-005, Nutzerentscheidung 2026-07-19). Historische Team- und Season-Daten überdauern eine Accountlöschung nur in wirksam anonymisierter, nicht rückführbarer Form — anonymisierte Team-Gesamtstände, nicht personenbezogene Season-Statistiken, anonymisierte Capture-Ereignisse, aggregierte Gebiets- und Teamwerte. Beispiel: „Vincent eroberte Gebiet X." wird zu „Gelöschtes Mitglied eroberte Gebiet X." Ist wirksame Anonymisierung nicht möglich, MUSS der Datensatz gelöscht werden. | Must | D | EXPLICIT | SRC-001/SRC-003 + CONTRA-005 |
| REQ-028 | **Deterministische Einzel-Reviere:** Einzel-Reviere dürfen erst nach Simulation und Threat-Model freigeschaltet werden; Rundenerkennung, Anfahrtssegmentierung, Übernahmepriorität, Polygon-Union/-Differenz, Restflächen und Gleichstände MÜSSEN deterministisch definiert sein. | Must | D | ASSUMPTION | SRC-003/SRC-005 |
| REQ-029 | **Sportplatz-Challenges und Bahngold-Score:** Freigegebene öffentliche Sportanlagen dürfen als goldene Challenge-Orte erscheinen; Runden und Rekorde werden GPS-tolerant validiert. Bahngold ist ein nicht übertragbarer Progressions-Score, keine Währung und beeinflusst kein Territory. | Should | D | ASSUMPTION | SRC-003/SRC-005 |
| REQ-030 | **Live-Map und Beschützer-Modus:** Live-Standort MUSS pro Aktivität explizit aktiviert, zeitlich begrenzt, sichtbar angezeigt, notabschaltbar und start-/endpunktverschleiert sein; Beschützer-Links enden automatisch. | Must | D | EXPLICIT | SRC-001/SRC-003 |
| REQ-031 | **Sturzerkennung als Assistenz:** Sturzerkennung darf nur als Assistenzfunktion mit Countdown, Abbruchmöglichkeit, dokumentierter Fehlalarmquote und ohne Sicherheitsgarantie angeboten werden. | Should | D | EXPLICIT | SRC-001/SRC-003 |
| REQ-032 | **Wearables und Bike-Sensorik:** Apple Watch, Wear OS und unterstützte Bike-Sensoren dürfen erst nach dokumentierter Kompatibilitätsmatrix freigeschaltet werden; Start/Stopp und Kernmetriken müssen konsistent synchronisieren. | Should | E | EXPLICIT | SRC-001/SRC-003 |
| REQ-033 | **Coach, Recovery, Wetter und Zyklus unter Claims-Gate:** Regenerations-, Coach-, Hitze-/Trink- und Zyklusfunktionen dürfen erst nach juristischer Claims- und Privacy-Freigabe erscheinen und müssen regelbasiert, erklärbar, optional und deaktivierbar sein. | Should | E | EXPLICIT | SRC-001/SRC-003 |
| REQ-034 | **Security, Datenschutz und Datenminimierung:** Das System MUSS EU-orientiertes Hosting, sichere Auth, Row-Level-Security, Rate Limits, serverseitige Validierung, Datenexport, Löschung und Datensparsamkeit umsetzen; Roh-Health-Verläufe werden nur bei nachgewiesener Notwendigkeit übertragen. **Datenminimierung konkretisiert (CONTRA-004):** Rohsensorverläufe bleiben standardmäßig lokal; serverseitig werden ausschließlich die in REQ-024 abschließend aufgezählten abgeleiteten Plausibilitätssignale verarbeitet. Weitergehende Rohdatenverarbeitung nur nach ausdrücklichem Opt-in oder für eine konkrete, zeitlich begrenzte Einspruchs-/Betrugsprüfung mit dokumentiertem Zweck und definierter Löschung. **Local-first konkretisiert (CAN-095):** Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal; für die Routenberechnung dürfen ausschließlich die erforderlichen Wegpunkte transient an einen kontrollierten Routing-Proxy übertragen werden; der Proxy speichert keine Koordinaten oder Routengeometrien dauerhaft. **Löschung konkretisiert (CONTRA-005):** siehe REQ-017 (Löschumfang) und REQ-027 (anonymisierte Historie). **A0-Proxy-Baseline (CONTRA-006 — `status: resolved`, `evidence_status: pending`, `blocking: true`):** Zweckbindung, Retention 0 für Koordinaten-Payload, Logging-Verbote, Transport- und Secret-Regeln nach Abschnitt „Widerspruchs-Auflösungen"; die zugehörige Evidence steht aus und ist blockierend. | Must | A0-E | EXPLICIT | SRC-001/SRC-003 + CONTRA-004/005/006 |
| REQ-035 | **Evidence Ledger und Definition of Done:** Kein Task oder Gate darf als abgeschlossen gelten, bevor automatisierte Tests, reale Gerätetests, Run/Bike-Nachweise, offene Punkte und Messwerte im Evidence Ledger dokumentiert sind. | Must | A0-E | EXPLICIT | SRC-003 |
| REQ-036 | **Store- und Release-Gates:** Jede Release-Stufe MUSS die zugehörigen iOS-/Android-Policies, Berechtigungsbegründungen, Datenschutzangaben und Testtracks vor Veröffentlichung bestehen; spätere Stufen starten erst nach dem vorherigen Gate. | Must | A0-E | EXPLICIT | SRC-003 |
| **REQ-037** | **Accessibility:** Die mobile Anwendung MUSS WCAG 2.2 AA erfüllen. Schriftgrößen, Screenreader, Fokusführung, Kontraste und Bedienflächen werden auf iOS und Android nachgewiesen. Farbe ist niemals der einzige Informationsträger. ⚠️ **Web-Erstreckung entfernt 2026-07-20** (Nutzerauftrag Schritt 3): der Halbsatz „und alle nutzbaren Web-Auskopplungen" ist gestrichen. Grund ist ein **Belegmangel, kein Widerspruch** — keine der vier Quellen erstreckt die Accessibility-Pflicht auf Web (Nachweis in der CAN-099-Belegprüfung unten). Die verbleibenden nicht quellengedeckten Klauseln (Fassungsziffer **2.2**, **Bedienflächen**, **Fokusführung**) bleiben im Wortlaut stehen und bleiben `ASSUMPTION` — sie werden nicht gestrichen und nicht hochgestuft. | Must | A0 (Basis) – A2 (vollständiger Audit) | **ASSUMPTION** | **CAN-099** (kanonischer Accessibility-Anker, Item Type CONSTRAINT / VALUE BOUNDARY, Source Type EXPLICIT), NFR-005; Wortlaut Nutzerentscheidung 2026-07-19, kanonisiert 2026-07-20, Web-Erstreckung entfernt 2026-07-20 |
| **REQ-038** | **Monochromes tokenbasiertes Designsystem:** Die Anwendung MUSS ein tokenbasiertes, überwiegend monochromes Designsystem verwenden. Farbe wird nur eingesetzt, wenn sie eine definierte fachliche Bedeutung besitzt: Health-Status, Team- und Revieridentität, Sportplatz-Gold sowie bestätigte Feiermomente. Run und Bike werden nicht ausschließlich durch Farbe unterschieden. | Must | A0-A2 | **EXPLICIT** | **CAN-141** (Item Type DESIGN CONSTRAINT / PRODUCT PRINCIPLE, Source Type EXPLICIT) — bereits festgelegtes Designprinzip, ausdrückliche Nutzerangabe 2026-07-19, kanonisiert 2026-07-20 |
| **REQ-039** | **GPX-Export abgeschlossener Aktivitäten:** Nutzer MÜSSEN eine abgeschlossene Run- oder Bike-Aktivität als standardkonforme GPX-Datei exportieren und in einer kompatiblen Fremdanwendung öffnen können. | Must | A2, spätestens vor öffentlichem v1.0-Release | **ASSUMPTION** | **CAN-139** (Item Type VALUE PROMISE / CAPABILITY, Source Type EXPLICIT); sekundär REQ-034; Wortlaut Nutzerentscheidung 2026-07-19, Canvas-Wortlaut kanonisiert 2026-07-20 |
| ~~REQ-040~~ | **DEPRECATED 2026-07-20 → REQ-041 (Wiederverwendung einer gespeicherten Route) und REQ-042 (Vergleich fachlich vergleichbarer Aktivitäten).** Composite aus Planungs- und Auswertungsfunktion. Siehe Migrationstabelle Runde 4. Neue Referenzen auf REQ-040 sind ein Validierungsfehler. | — | — | — | Registry §6.4, §7.5 |
| **REQ-041** | **Wiederverwendung einer gespeicherten Route:** Nutzer MÜSSEN eine gespeicherte Route erneut als Grundlage einer geplanten Run- oder Bike-Aktivität verwenden können. | Must | A2 | **ASSUMPTION** | CAN-142; Wortlaut Nutzerentscheidung 2026-07-20 |
| **REQ-042** | **Vergleich fachlich vergleichbarer Aktivitäten:** Nutzer MÜSSEN fachlich vergleichbare Aktivitäten auf derselben oder hinreichend ähnlichen Strecke anhand sportartspezifischer Kennzahlen miteinander vergleichen können. Run und Bike bleiben dabei **strikt getrennt**. | Must | A2 | **ASSUMPTION** | CAN-143; Wortlaut Nutzerentscheidung 2026-07-20. **Vergleichslogik MISSING bis OQ-015** |

### Migrationstabelle Requirements (Auftau-Schritt 2, 2026-07-19)

Kanonische Quelle: `docs/ID-REGISTRY.md` §6.4 und §7.4. Dieses PRD zieht **nach**; es vergibt und deprecatet keine IDs.

| Alt | Vorgang | Neu | Begründung |
|---|---|---|---|
| REQ-014 | **deprecated** | **REQ-037** + **REQ-038** | Composite aus zwei unabhängig prüfbaren Anforderungen mit **verschiedenen Prüfverfahren, Nachweisen und Gates**. Zugänglichkeit (WCAG, Screenreader, Dynamic Type) und Gestaltungssprache (tokenbasiert, monochrom) können unabhängig voneinander bestehen oder fallen. **Ausdrücklich nicht umgedeutet** — kein stilles Verengen auf eine der beiden Hälften. Folge: AC-014, EV-014 und TRC-014 sind ebenfalls deprecated. |
| REQ-008 | **verengt**, nicht deprecated | REQ-008 (Kern) · **REQ-039** (GPX-Export) · **REQ-041/REQ-042** (Wiederverwendung bzw. Vergleich, vormals REQ-040) | Dieselbe Anforderung, auf ihren atomaren Kern reduziert — keine neue Bedeutung, deshalb **keine neue ID** für den Rest. Alttitel „Verlauf, Wiederverwendung und Export"; Alttext: „Abgeschlossene Aktivitäten MÜSSEN in Verlauf und Detailansicht verfügbar sein; gespeicherte Routen, Streckenvergleich und GPX-Export werden unterstützt." Canvas-Anker **CAN-138** statt des deprecateten CAN-071. **REQ-008 bleibt auf diesen Scope verengt: GPX-Export und Streckenvergleich gehören NICHT dazu.** |
| CAN-071 | **deprecated** | **CAN-138** (A0) · **CAN-139** (A2) · ~~CAN-140~~ → **CAN-142, CAN-143** (A2) | Drei fachlich getrennte Capabilities auf **zwei** Release-Stufen in einem Item. **Transitive Kette beachten:** CAN-140 ist am 2026-07-20 selbst deprecated worden. Die wirksame Nachfolgemenge von CAN-071 lautet damit **CAN-138, CAN-139, CAN-142, CAN-143**. Ein Nachzug, der auf CAN-140 stehen bleibt, landet auf einer deprecateten ID. |

### Migrationstabelle Requirements (Runde 4, 2026-07-20)

Kanonische Quelle: `docs/ID-REGISTRY.md` §6.3.3, §6.4 und §7.5. Dieses PRD zieht **nach**; es vergibt und deprecatet keine IDs.

| Alt | Vorgang | Neu | Begründung |
|---|---|---|---|
| REQ-040 | **deprecated** | **REQ-041** + **REQ-042** | Composite — wie zuvor REQ-014. Zwei unabhängig prüfbare Anforderungen: die **Wiederverwendung** einer gespeicherten Route (Planung, Vorbereitung) und der **Vergleich** abgeschlossener Aktivitäten (Auswertung, Rückblick). Sie erfüllen die Trennkriterien der Atomisierungsregel **fünffach**: unabhängig auslieferbar · unterschiedliche Nutzerwerte · unterschiedliche Acceptance Criteria · unabhängig bestehend oder scheiternd · **unterschiedlich blockiert**. Der letzte Punkt ist der operative: REQ-041 ist heute vollständig spezifizierbar, REQ-042 ist es ohne **OQ-015** nicht. Ein gemeinsames Item hätte den lieferbaren Teil an eine offene Forschungsfrage gekettet. **Ausdrücklich NICHT auf eine Hälfte verengt.** Folge-Deprecations: AC-040, EV-040, TRC-040. |
| CAN-140 | **deprecated** | **CAN-142** (Planung) + **CAN-143** (Auswertung) | Dieselbe Teilung auf Canvas-Ebene. |
| AC-040 | **deprecated** | **AC-042** + **AC-043** | Der Alttext belegt die Composite-Natur wörtlich: erster Halbsatz („erneut gestartet werden") → AC-042, zweiter („werden mit definierten Kennzahlen gegenübergestellt") → AC-043. Eine ID kann die zwei unabhängigen Zustände „heute erfüllbar" und „ohne OQ-015 nicht spezifizierbar" nicht gleichzeitig tragen (Registry-Regel 5, vgl. §6.5.1). |
| EV-040 | **deprecated** | **EV-043** + **EV-044** | Zwei Nachweise mit **unterschiedlichem Blockierungszustand** in einer ID. |
| TRC-040 | **deprecated** | **TRC-041** + **TRC-042** | Die Zeile referenzierte vier deprecatete IDs; ihr einziger Vision-Anker betraf nur **eine** der beiden Hälften. |

**CAN-138 bleibt ausdrücklich ungeteilt.** Die Teilungsprüfung ist durchgeführt und **negativ** ausgefallen — fünf Gründe, jeder einzeln tragend: (a) beide Funktionen gehören zum selben **A0-Nutzerfluss**; (b) die Detailansicht ist die **unmittelbare Vertiefung** des Verlaufs und nicht unabhängig auslieferbar; (c) beide werden gemeinsam durch **REQ-008** ausgeliefert; (d) **gleiches Gate** (A0); (e) **gleiches lokales Aktivitätsmodell**. Kein einziges Trennkriterium ist erfüllt — **mehrere Verben in einem Satz trennen nicht.**

**Verbindliche Stufung (Nutzerentscheidung 2026-07-19, fortgeschrieben 2026-07-20):**

| Stufe | Umfang |
|---|---|
| **A0** | Aktivitätsverlauf, Aktivitätsdetail, lokale Persistenz, Recovery, Run-/Bike-korrekte Darstellung (REQ-008) |
| **A2** | öffentlicher GPX-Export (**REQ-039**), Wiederverwendung einer gespeicherten Route (**REQ-041**) und fachlich valider Streckenvergleich (**REQ-042**) — Datenportabilität vor öffentlichem v1.0-Release |

**Warum REQ-039 eine eigene ID hat und REQ-034 nicht genügt.** Die Nutzerentscheidung stellt ausdrücklich fest: **REQ-034 ist KEIN ausreichend präziser primärer Anker.** Die Erwähnung „Datenexport" in REQ-034 trägt die konkrete Capability „GPX-Datei erzeugen und extern öffnen" nicht. REQ-034 bleibt **sekundäre Constraint-Verknüpfung** — Nutzerkontrolle, Datenportabilität, Datenminimierung, keine unbeabsichtigten Zusatzdaten. Es wird **nicht** behauptet, REQ-034 allein erfülle den GPX-Export.

**Warum REQ-041 und REQ-042 je eine eigene ID haben — geprüft, nicht angenommen.** Beide Aussagen wurden gegen den **aktiven** Bestand geprüft, bevor neue IDs vergeben wurden:

| Hälfte | Geprüfter Kandidat | Trägt er die Aussage? |
|---|---|---|
| **Wiederverwendung** (REQ-041) | **CAN-050** „Routenplanung und gespeicherte Routen" | **Nein.** CAN-050 trägt laut Registry **REQ-006** auf **Gate A0**: eine Route **anlegen** und **speichern**. Die erneute Verwendung einer bereits gespeicherten Route liegt auf **Gate A2** und ist eine andere Handlung. CAN-050 dafür zu benutzen wäre die plausible Lesart mit falscher Bedeutung. |
| | **REQ-006 / AC-006 / EV-006** | **Nein.** REQ-006 lautet „…eine Route über Wegpunkte oder ein Distanzziel planen, das korrekte Run-/Bike-Routingprofil verwenden und den Plan vor dem Start prüfen". **Kein Wort über Wiederverwendung.** AC-006 und EV-006 folgen REQ-006. |
| **Vergleich** (REQ-042) | alle aktiven CAN-/REQ-Items | **Nein.** Die Aussage stand ausschließlich als Teilklausel im Composite REQ-008 und danach in CAN-140/REQ-040. REQ-006 und REQ-007 betreffen **Planung und Durchführung**, nicht den **Vergleich** zweier abgeschlossener Aktivitäten. |

⚠️ **BLOCKER — Wortlaut unbestätigt (Registry §8 Punkte 24 und 43).** Zwei Klassen, getrennt geführt:

- `source_type` **ASSUMPTION**: REQ-008 (verengt), REQ-037, REQ-039, **REQ-041**, **REQ-042**, CAN-022, CAN-138, **CAN-142**, **CAN-143**. Der Wortlaut ist aus der Nutzerentscheidung übernommen, aber nicht ausdrücklich als Anforderungstext bestätigt.
- `source_type` **EXPLICIT ohne ausdrückliche Gegenbestätigung**: **CAN-099**, **CAN-139**, **CAN-141** sowie REQ-038. Sie stehen auf EXPLICIT, weil der Nutzer den Wortlaut am 2026-07-20 als verbindlich gesetzt hat — eine Gegenbestätigung liegt **nicht** vor. Das ist offengelegt, nicht als erledigt behandelt.

⚠️ **BLOCKER — Vision-Anker fehlen (drei, nicht zwei).** **REQ-038**, **REQ-039** und seit dem 2026-07-20 auch **REQ-041** haben **keinen** Vision-Anker. `VIS-012` (Designprinzip), `VIS-013` (Datenportabilität) und `VIS-014` (Wiederverwendung geplanter Strecken) sind in der Registry **reserviert, Inhalt MISSING**. Die Prüfung aller bestehenden VIS-Items ergab keinen Treffer: VIS-003 nennt keine Portabilität und keine Wiederverwendung geplanter Strecken, VIS-009 regelt Sichtbarkeit statt Mitnahme, VIS-004 nennt Teams und Spielmechanik. Es wird ausdrücklich **kein** VIS-Item umgedeutet — genau der Defekt VIS-009 ↔ REQ-014, der oben behoben wurde. `TRC-038`, `TRC-039` und `TRC-041` werden deshalb bewusst als `broken` geführt statt an ein unpassendes Item gehängt.

⚠️ **`canvas-problem` bei REQ-037, REQ-038, REQ-039 — am 2026-07-20 requirement-spezifisch aufgelöst, NICHT pauschal.** Die bisher in `docs/traceability.md` geführten Verknüpfungen zu CAN-013 und CAN-029 beruhten auf der in Registry §6.1.1 **ausdrücklich verbotenen** Schlusskette „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" und sind entfernt. Bis dahin wurden alle drei gemeinsam als BLOCKER geführt. Die Einzelprüfung gegen SRC-001 und SRC-003 zeigt: **das ist für die drei nicht dieselbe Lage.**

| REQ | Wert | Begründung in einem Satz |
|---|---|---|
| **REQ-037** | **MISSING — BLOCKER, bleibt** | Zugänglichkeit **hat** ein Nutzerproblem (Menschen, die die App nicht bedienen können); der Canvas führt es nur nicht. Eine Nichtanwendbarkeit zu behaupten wäre falsch. |
| **REQ-038** | **MISSING — begründete Nichtanwendbarkeit** | SRC-003 §2 typisiert die Gestaltungssprache selbst als **„Designprinzip"** — eine selbstgesetzte Regel, keine Antwort auf eine beschriebene Nutzernot. |
| **REQ-039** | **MISSING — begründete Nichtanwendbarkeit, mit offengelegtem Rest** | SRC-003 §8 führt den Export als **Store-Compliance-Zeile**, SRC-001 §3.5 als **Privacy/DSGVO-NFR**, SRC-001 T-06 als **funktionale Capability** — drei Rahmungen, keine davon ein Nutzerproblem. |

**Die Unterscheidung ist der Punkt, nicht die Formalie.** „Kein Problem-Item nötig" gilt nur, wo die Quellen das Requirement selbst als Prinzip oder Pflicht rahmen (REQ-038, REQ-039) — nicht, wo ein Problem existiert und nur nicht aufgeschrieben ist (REQ-037). Ein pauschales „nicht relevant" für alle drei hätte die REQ-037-Lücke unsichtbar gemacht. Es wird weiterhin **kein** CAN-Item umgedeutet und **keine** neue Problem-ID vergeben; die reservierten CAN-016…CAN-021 decken keines der drei ab. Die Einzelbegründungen stehen bei den Requirements. **`docs/traceability.md` §4.1 führt für alle drei noch den pauschalen Vorstand — Nachzug durch den Traceability-Owner erforderlich (BLOCKER, fremdes Eigentum).**

## Acceptance Criteria

| AC ID | Requirement ID | Given | When | Then | Source Type |
|---|---|---|---|---|---|
| AC-001 | REQ-001 | Ein Nutzer hat einen Sportmodus gewählt. | Der Nutzer zwischen Run und Bike wechselt. | Alle sportabhängigen Metriken, Schwellen, Labels und Routingprofile wechseln konsistent; Run zeigt Pace, Bike zeigt Geschwindigkeit. | EXPLICIT |
| AC-002 | REQ-002 | Standortberechtigung ist erteilt und kein Tracking aktiv. | Der Nutzer eine Aktivität startet und sich bewegt. | Die Route und Live-Metriken aktualisieren sich fortlaufend und die Aktivität kann kontrolliert beendet werden. | EXPLICIT |
| AC-003 | REQ-003 | Eine Aktivität läuft. | Der Bildschirm gesperrt, die App beendet oder eine Pause erkannt wird. | Die Aktivität bleibt lückenlos, Pausenzeit verfälscht keine Metrik und die Session ist wiederherstellbar. | EXPLICIT |
| AC-004 | REQ-004 | Rohpunkte mit variierender Qualität liegen vor. | Der GPS-Filter angewendet wird. | Akzeptierte, verworfene und unsichere Punkte sind deterministisch und nachvollziehbar klassifiziert. | ASSUMPTION |
| AC-005 | REQ-005 | Eine Aktivität erzeugt fortlaufend Trackpunkte. | Die App schreibt, beendet, startet neu oder migriert ein Schema. | Keine Aktivität geht verloren und Migrationen sowie Indexe bleiben konsistent. | ASSUMPTION |
| AC-006 | REQ-006 | Ein Nutzer befindet sich im Planungsmodus. | Wegpunkte oder ein Distanzziel eingegeben werden. | Eine plausible Route beziehungsweise ein Ziel mit Distanz und Fehlermeldungen wird angezeigt. | EXPLICIT |
| AC-007 | REQ-007 | Eine geplante Route ist aktiv. | Der Nutzer der Route folgt, abweicht, umkehrt oder Schleifen läuft. | Fortschritt bleibt monoton plausibel, Restdistanz folgt der Route und Off-Route-Zustand wird sichtbar. | ASSUMPTION |
| AC-008 | REQ-008 | Mindestens eine Run- **und** mindestens eine Bike-Aktivität wurden regulär abgeschlossen und lokal gespeichert. | Der Nutzer den Verlauf öffnet, die App neu startet und eine Detailansicht öffnet. | **Run und Bike werden getrennt geprüft:** (a) die gespeicherte Aktivität erscheint **nach Neustart** im Verlauf · (b) die Detailansicht lädt den **korrekten** Track · (c) **Run zeigt Pace** · (d) **Bike zeigt Geschwindigkeit** · (e) keine Aktivität geht nach regulärem Abschluss verloren · (f) beschädigte oder unbekannte Aktivitätsdaten führen zu einem **kontrollierten Zustand**, nicht zu einem Absturz oder stillen Verlust. | **ASSUMPTION** |
| AC-009 | REQ-009 | Eine kompatible Datenquelle ist freigegeben oder verbunden. | Eine Aktivität aufgezeichnet wird. | Live-/Verlaufs-HF und Quelle werden korrekt dargestellt; fehlende HF blockiert Tracking nicht. | EXPLICIT |
| AC-010 | REQ-010 | Eine Aktivität mit vollständigen oder unvollständigen Health-Daten endet. | Der Score berechnet und geöffnet wird. | Nutzer sehen Score, konkrete Gründe, Datenbasis, fehlende Signale und die Unsicherheit der Aussage. | ASSUMPTION |
| AC-011 | REQ-011 | HF-Daten und Zonen sind verfügbar. | Der Nutzer trainiert oder Einstellungen ändert. | Zonen und Hinweise reagieren korrekt; Deaktivierung verhindert jede Ansage. | EXPLICIT |
| AC-012 | REQ-012 | Eine Aktivität endet. | Der Nutzer einen Check-in abgibt und mindestens vier Wochen Daten vorliegen. | Der Check-in dauert unter zwei Sekunden und Trends werden ohne Kausalitätsbehauptung angezeigt. | EXPLICIT |
| AC-013 | REQ-013 | Wochen- und Vier-Wochen-Daten liegen vor. | Home geöffnet oder die Schwelle überschritten wird. | Aktivitäten, Belastung und Trend sind korrekt; Hinweise verwenden freigegebene Orientierungssprache. | EXPLICIT |
| ~~AC-014~~ | ~~REQ-014~~ | **DEPRECATED 2026-07-19 → AC-037 (Accessibility) und AC-038 (Designsystem).** Der Alttext vermischte dieselben zwei Prüfungen wie REQ-014. | — | — | — |
| AC-015 | REQ-015 | Ein Unlock-Kriterium ist definiert. | Die zugehörige verifizierte Leistung erreicht wird. | Das Item wird genau einmal freigeschaltet; ohne Leistung oder Kauf ist es nicht verfügbar. | EXPLICIT |
| AC-016 | REQ-016 | Eine Aktivität oder Woche abgeschlossen ist. | Ein Rückblick, Export oder Lockscreen-Status erzeugt wird. | Metriken sind korrekt, exportierbar und sensible Standortdaten sind reduziert. | EXPLICIT |
| AC-017 | REQ-017 | Lokale Daten existieren oder ein Account wird erstellt; historische Team-/Season-Einträge verweisen auf diesen Nutzer. | Der Nutzer sich anmeldet, offline trainiert oder sein Konto löscht. | Daten migrieren/synchronisieren deterministisch; Löschung entfernt alle personenbezogenen Daten und Identitätszuordnungen gemäß Retention-Regeln; verbleibende historische Aggregate sind wirksam anonymisiert und nicht rückführbar, sonst gelöscht. | EXPLICIT |
| AC-018 | REQ-018 | Zwei Nutzer und Social-Inhalte existieren. | Sichtbarkeit geändert, blockiert oder gemeldet wird. | Nur erlaubte Daten sind sichtbar; Blockierung wirkt beidseitig sofort und Meldungen sind bearbeitbar. | EXPLICIT |
| AC-019 | REQ-019 | Eine Routenempfehlung ist veröffentlicht und für einen **berechtigten** Empfänger sichtbar. | Der berechtigte Nutzer die Empfehlung übernimmt. | **Funktionales Kriterium:** Ein berechtigter Nutzer kann eine sichtbare Routenempfehlung übernehmen. Die übernommene Route wird in seiner Planung verfügbar, **ohne dass private Daten des Empfehlenden offengelegt werden**. | EXPLICIT |
| AC-020 | REQ-020 | Berechtigte Nutzer gründen oder betreten ein Team. | Gründung, Scan, Ablauf oder Deaktivierung ausgeführt wird. | Es existiert nie ein Team ohne Admin und ungültige Tokens gewähren keinen Zugang. | EXPLICIT |
| AC-021 | REQ-021 | Ein Team hat neue, aktive und inaktive Mitglieder. | Kapazität, Stufe oder Mentorbonus berechnet wird. | Nur Mitglieder mit Aktivität im definierten Zeitfenster zählen; Bonus folgt erst nach nachgewiesener Integration. | EXPLICIT |
| AC-022 | REQ-022 | Mindestens zwei freigegebene Aktivitäten oder ein Event vorliegen. | Nähe, Zeit und Teilnahme ausgewertet werden. | Echte gemeinsame Aktivität wird erkannt, nicht gemeinsame wird abgelehnt und Eventinhalte sind moderierbar. | EXPLICIT |
| AC-023 | REQ-023 | Run- und Bike-Aktivitäten fließen in eine gemeinsame Mechanik. | Effort und Rang berechnet werden. | Keine Sportart dominiert systematisch; verwendete Version und Faktoren sind nachvollziehbar. | EXPLICIT |
| AC-024 | REQ-024 | Eine Aktivität synchronisiert wird — mit vollständiger, teilweiser oder fehlender Sensorausstattung. | Plausibilitätsregeln angewendet werden. | Fehlende Sensoren allein führen nicht zur Betrugsannahme (höchstens `low-confidence`, nie automatisch `rejected`); klare Manipulation zählt nicht für Wettbewerb; an den Server gelangen ausschließlich die in REQ-024 aufgezählten abgeleiteten Signale, keine Rohsensorserien. | ASSUMPTION |
| AC-025 | REQ-025 | Challenge-Definitionen und verifizierte Aktivitäten vorliegen. | Fortschritt oder Reward verarbeitet wird. | Fortschritt ist korrekt und kein Reward wird doppelt vergeben. | EXPLICIT |
| AC-026 | REQ-026 | Territory-Simulation und Geo-Daten sind freigegeben. | Teams Beiträge leisten oder Layer umschalten. | Eroberung folgt Formel und Quorum, reale Areale werden dargestellt und das interne Raster ist nie sichtbar. | EXPLICIT |
| AC-027 | REQ-027 | Eine Season endet; im Bestand existieren Einträge eines zwischenzeitlich gelöschten Mitglieds. | Der Season-Abschluss ausgeführt wird. | Aktive Besitzstände werden zurückgesetzt; historische Records bleiben vollständig abrufbar und nach Finalisierung fachlich unveränderbar, außer aufgrund Löschung, Anonymisierung oder rechtlicher Korrektur; Einträge gelöschter Mitglieder erscheinen anonymisiert und nicht rückführbar. | EXPLICIT |
| AC-028 | REQ-028 | Eine zielgebundene, verifizierte Aktivität eine Fläche umschließt. | Einnahme, Überlappung, Teilübernahme oder Gleichstand berechnet wird. | Dasselbe Eingabeset erzeugt dieselbe Geometrie und denselben Besitzer; Linien-/Drift-Tracks werden abgelehnt. | ASSUMPTION |
| AC-029 | REQ-029 | Ein zugänglicher, kuratierter Sportplatz existiert. | Vollständige Runden oder Rekorde erkannt werden. | Nur plausible Runden zählen; geschlossene/private Anlagen bleiben gesperrt und Bahngold verändert keine Effort- oder Territory-Wertung. | ASSUMPTION |
| AC-030 | REQ-030 | Ein Nutzer eine Live-Freigabe startet. | Freigabe endet, App beendet, blockiert oder Not-Aus ausgelöst wird. | In jedem Pfad endet die Freigabe; unberechtigte und blockierte Personen sehen keinen Standort. | EXPLICIT |
| AC-031 | REQ-031 | Sturzähnliche Sensordaten auftreten. | Das Muster erkannt wird. | Ein sichtbarer Countdown startet, kann abgebrochen werden und nur danach wird der definierte Kontakt informiert. | EXPLICIT |
| AC-032 | REQ-032 | Ein unterstütztes Wearable oder Sensor gekoppelt ist. | Aktivität gestartet, pausiert oder beendet wird. | Status und Messwerte bleiben zwischen Geräten konsistent und nicht unterstützte Kombinationen sind klar benannt. | EXPLICIT |
| AC-033 | REQ-033 | Claims-Whitelist und Privacy-Review sind freigegeben. | Eine Empfehlung erzeugt wird. | Empfehlung nennt Gründe, Grenzen und Datenbasis; sensible Funktionen sind Opt-in und vollständig deaktivierbar. | EXPLICIT |
| AC-034 | REQ-034 | Personen-, Health- oder Standortdaten verarbeitet werden. | Daten gespeichert, synchronisiert, exportiert oder gelöscht werden. | Zugriff folgt Berechtigung und Zweckbindung; nicht benötigte sensible Daten verlassen das Gerät nicht. | EXPLICIT |
| AC-035 | REQ-035 | Ein Task oder Release-Gate zur Abnahme vorgelegt wird. | Die Definition of Done geprüft wird. | Status wird nur bei vollständiger Evidence auf done gesetzt; fehlende Nachweise bleiben sichtbar. | EXPLICIT |
| AC-036 | REQ-036 | Eine Release-Stufe zur Veröffentlichung vorgesehen ist. | Gate und Store-Readiness geprüft werden. | Kein Release wird ohne vollständige Nachweise und Policy-Abnahmen veröffentlicht. | EXPLICIT |
| **AC-037** | **REQ-037** | Die ausgelieferten Screens der mobilen App liegen vor. ⚠️ **Web-Erstreckung entfernt 2026-07-20** (Nutzerauftrag Schritt 3, synchron mit REQ-037, NFR-005-`signal` und dem kanonischen CAN-099-Wortlaut) — vorher: „…der mobilen App **und aller nutzbaren Web-Auskopplungen**". | Der Accessibility-Nachweis geführt wird. | Alle fünf Bedingungen einzeln erfüllt: (a) **WCAG-2.2-AA-Audit bestanden** · (b) relevante Screens mit **VoiceOver UND TalkBack** geprüft — beide, nicht „ein Screenreader" · (c) **Dynamic Type** bzw. Font Scaling geprüft · (d) **keine Information ausschließlich durch Farbe** · (e) **dokumentierte** Kontrastprüfung. **iOS und Android getrennt nachzuweisen.** | **ASSUMPTION** |
| **AC-038** | **REQ-038** | Die Design-Tokens und die ausgelieferten Screens liegen vor. | Das Farbinventar gegen die zulässigen fachlichen Bedeutungen geprüft wird. | (a) Farbe erscheint **ausschließlich** in den vier abschließend definierten fachlichen Bedeutungen (Health-Status, Team-/Revieridentität, Sportplatz-Gold, bestätigte Feiermomente) · (b) Run und Bike sind **nicht ausschließlich** durch Farbe unterscheidbar · (c) alle Farbwerte stammen aus **Design-Tokens**, keine Inline-Literale. | **EXPLICIT** |
| **AC-039** | **REQ-039** | Je eine regulär abgeschlossene Run- und Bike-Aktivität mit vollständigen Trackdaten liegt vor; zusätzlich ein Fall mit fehlenden oder beschädigten Trackdaten. | Der Nutzer den Export auslöst. | Acht einzeln prüfbare Bedingungen: (a) GPX für abgeschlossene **Run**-Aktivität erzeugt · (b) GPX für abgeschlossene **Bike**-Aktivität erzeugt · (c) **Zeitstempel und Koordinatenreihenfolge korrekt** · (d) Datei in **mindestens einer definierten** kompatiblen Fremd-App öffenbar · (e) **keine Health-Daten unbeabsichtigt exportiert** · (f) der Nutzer sieht **vor** dem Export, welche Daten enthalten sind · (g) fehlende oder beschädigte Trackdaten führen zu einem **kontrollierten Fehler** · (h) der Export funktioniert **ohne** Veröffentlichung oder Social-Freigabe. | **ASSUMPTION** |
| ~~AC-040~~ | ~~REQ-040~~ | **DEPRECATED 2026-07-20 → AC-042 (Wiederverwendung) und AC-043 (Vergleich).** Der Alttext vermischte eine heute erfüllbare mit einer ohne OQ-015 nicht spezifizierbaren Bedingung. | — | — | — |
| **AC-042** | **REQ-041** | Mindestens eine Route wurde zuvor regulär geplant und gespeichert — je eine für **Run** und für **Bike**; zusätzlich liegt ein Fall mit gelöschter oder beschädigter gespeicherter Route vor. | Der Nutzer eine gespeicherte Route als Grundlage einer neuen geplanten Aktivität auswählt und startet. | **Fünf einzeln prüfbare Bedingungen, alle heute spezifizierbar:** (a) gespeicherte Route für **Run** wiederverwendbar · (b) gespeicherte Route für **Bike** wiederverwendbar · (c) die geladene Route stimmt in **Geometrie und Wegpunkten** mit der gespeicherten überein · (d) das **sportartspezifische Routingprofil** bleibt beim Laden korrekt (Abgrenzung zu REQ-001/REQ-006) · (e) eine gelöschte oder beschädigte gespeicherte Route führt zu einem **kontrollierten Fehler**, nicht zu einem stillen Leerstart. **Nicht von OQ-015 abhängig** — das ist der operative Grund der Teilung. | **ASSUMPTION** |
| **AC-043** | **REQ-042** | Mindestens zwei regulär abgeschlossene Aktivitäten **derselben** Sportart auf derselben oder hinreichend ähnlicher Strecke liegen vor; zusätzlich je ein verkürzter, verlängerter, abgebrochener und geometrisch abweichender Fall sowie ein Aktivitätspaar **verschiedener** Sportarten. | Der Vergleich ausgeführt wird. | **Feststehend und schon jetzt prüfbar:** (a) Run und Bike **strikt getrennt** — es wird nie sportübergreifend verglichen · (b) **keine irreführende Bestzeit bei nicht vergleichbarer Geometrie**. **MISSING (OQ-015) und hier ausdrücklich NICHT erfunden:** das Vergleichbarkeitskriterium selbst, die tolerierte Abweichung der Streckenähnlichkeit, die verglichenen Kennzahlen sowie die Behandlung verkürzter, verlängerter und abgebrochener Aktivitäten. **AC-043 ist bis zur Entscheidung von OQ-015 nicht vollständig prüfbar; AC-042 ist davon unberührt.** | **ASSUMPTION** |
| **AC-041** | **REQ-019** | Routenempfehlungen und Übernahmen sind über ein rollierendes 28-Tage-Fenster erfasst. | Die Kennzahl für Gate B berechnet wird. | **Messkriterium:** Für Gate B kann die Zahl bestätigter Übernahmen je auswertbarer Empfehlung **datenschutzkonform, sportartspezifisch und reproduzierbar** berechnet werden. **Prüft die Berechenbarkeit der Kennzahl, nicht ihren Zielwert** — ob > 1,0 erreicht wird, ist eine Produktfrage und keine Abnahmebedingung. | MISSING (OQ-012, OQ-014) |

### AC-019 aufgeteilt — zwei IDs statt zweier Felder (2026-07-19)

**AC-019** behält das **funktionale** Kriterium, das **Messkriterium** ist nach **AC-041** ausgelagert. Kanonische Begründung: `docs/ID-REGISTRY.md` §6.5.1.

Ausschlaggebend ist ein Satz der Nutzerentscheidung selbst: *„Das funktionale Kriterium kann bestanden sein, während die Produktkennzahl noch keine ausreichende Stichprobe hat."* Die beiden Kriterien haben damit **zu jedem Zeitpunkt unabhängige Zustände**. Zwei Felder derselben AC-ID hätten eine ID mit zwei unabhängig wahren oder falschen Aussagen belastet — ein Verstoß gegen Registry-Regel 5 und strukturell derselbe Defekt (ein Feld, zwei unabhängige Fragen), den das getrennte CONTRA-Statusmodell bereits behoben hat.

| | AC-019 (funktional) | AC-041 (Messkriterium) |
|---|---|---|
| Nachweisart | E2E-Flow zwischen zwei Konten (EV-019) | Auswertbarkeit einer aggregierten Kennzahl (EV-041) |
| Fälligkeit | mit der Funktion | zu Gate B, abhängig von OQ-012 und OQ-014 |
| Blockierbarkeit | durch Implementierungsfehler | durch fehlende Telemetrie-Entscheidung |

Eine gemeinsame ID hätte den **Funktionsnachweis an die offene Telemetriefrage gekettet** — eine Blockade, die die Nutzerentscheidung ausdrücklich nicht will („Blocking: NICHT für A0/A1, NICHT für die Dokumentkorrektur").

**Folge:** REQ-019 ist das erste Requirement mit **zwei** Acceptance Criteria. Jede Prüfung, die `Anzahl AC == Anzahl REQ` erwartet, ist zu korrigieren — **die Prüfung, nicht die Daten**.

## Non-Functional Requirements

**Vollständiges NFR-Audit, eingetragen am 2026-07-19.** Die frühere Tabelle führte alle acht NFRs mit `Source Type = EXPLICIT` bei nur vier Spalten und **ohne eine einzige Quellenangabe**. Sieben der acht Angaben halten der Beweislatte nicht stand und wurden korrigiert. Kein Zielwert wurde erfunden; wo keiner ableitbar war, steht MISSING, BLOCKER oder OPEN QUESTION.

### Zwei getrennte Achsen

`source_type` und `evidence_status` beantworten **verschiedene Fragen** und werden nicht vermischt. `EXPLICIT + pending` ist eine gültige Kombination.

| Achse | Frage | Werte |
|---|---|---|
| `source_type` | Woher stammt der Zielwert / die Pass-Bedingung? | `EXPLICIT` · `ASSUMPTION` · `MISSING` · `BLOCKER` · `CONTRADICTION` |
| `evidence_status` | Ist die Erfüllung nachgewiesen? | `not-required` · `not-planned` · `planned` · `pending` · `verified` · `failed` · `blocked` |

**Beweislatte für `EXPLICIT`** — mindestens eines muss gelten: (a) der Nutzer hat den Wert ausdrücklich bestätigt, (b) der Wert steht in einer belegten Nutzerquelle, (c) eine verbindliche externe Regel oder Plattformvorgabe wird **konkret zitiert**.

**Keine automatische Vererbung.** Eine qualitative Nutzerabsicht („Tracking muss präzise sein") macht einen quantitativen Engineering-Zielwert („< 3 %") **nicht** EXPLICIT. Das sind zwei getrennte Aussagen.

⚠️ **`EXPLICIT` bedeutet in `docs/traceability.md` etwas anderes.** Dessen Legende definiert rein syntaktisch: „Die Pass-Bedingung steht wörtlich in einem Artefakt." Das prüft nur, **ob** ein Satz irgendwo steht, nicht **woher** der Wert stammt. Die Traceability-Definition ist nicht falsch — sie beantwortet eine andere Frage —, darf aber **nicht** als Beleg für `source_type = EXPLICIT` herangezogen werden. Wer beide gleichsetzt, stuft still hoch.

**`evidence_status = verified` bei keinem einzigen NFR.** Der Nenner ist abgeleitet, nicht festgeschrieben: `aktiv(NFR)` = **8** (Stand 2026-07-20). Es existiert kein Code, kein Build, kein Gerätetest und keine CI. Kein Nachweis wird hier als erbracht erklärt.

### Übersicht

⚠️ **Die Spalte `blocking` ist am 2026-07-20 ersatzlos entfallen** — siehe „NFR-008 — Runde 4" weiter unten. Sie führte **acht hartkodierte Werte, die niemand nachrechnen konnte**: für den `NFR-`Raum existiert weder eine Formel noch eine Eingabe noch ein Wertebereich. Die Achsen `status`, `resolution_status`, `blocking`, `blocked_gates` und `blocked_activities` sind nach Registry §3.1 und §9 Bedingung 9 **ausschließlich** für `OQ-` und `CONTRA-` definiert. Die Spalte wurde **entfernt, nicht umgerechnet**. An ihre Stelle tritt `evidence_gate` — das Feld, das die tragende Frage tatsächlich beantwortet: **welches Gate fordert die Anforderung ein?** Es ist Teil des eingefrorenen Modells; es wurde **nichts erweitert**.

**`evidence_gate` ist abgeleitet, nicht erfunden.** Kein Artefakt nennt für NFR-001…NFR-007 ein eigenes Evidence-Gate. Der Wert wird deshalb aus dem bereits belegten `release_gate` abgeleitet — **das früheste Gate, an dem der Nachweis fällig wird** — und ist als Ableitung gekennzeichnet. Für **NFR-008 ist auch `release_gate` MISSING**, also bleibt `evidence_gate` MISSING; hier wird **nichts** abgeleitet.

| ID | Titel | `source_type` (Stand 2026-07-18, historisch) | `source_type` (**gültig**) | `evidence_status` | `evidence_gate` (abgeleitet) | `release_gate` |
|---|---|---|---|---|---|---|
| NFR-001 | Distanzgenauigkeit | EXPLICIT | **ASSUMPTION** | `pending` | A0 | GATE-A0 |
| NFR-002 | Batterie | EXPLICIT | **ASSUMPTION** | `pending` | A0 | GATE-A0 |
| NFR-003 | Zuverlässigkeit | EXPLICIT | **ASSUMPTION** | `pending` | A0 | GATE-A0 |
| NFR-004 | Performance | EXPLICIT | **BLOCKER** | `blocked` | A0 | GATE-A0 / GATE-D |
| NFR-005 | Accessibility | EXPLICIT | **ASSUMPTION** | **`not-planned`** (korrigiert, vorher `pending`) | A0 | GATE-A0 bis GATE-A2 |
| NFR-006 | Datenschutz | EXPLICIT | **BLOCKER** | `blocked` | A0 | GATE-A0 bis GATE-E |
| NFR-007 | Sicherheit | EXPLICIT | **EXPLICIT** (klauselbeschränkt) | `pending` | A0 | GATE-A0 bis GATE-E |
| NFR-008 | Wartbarkeit | EXPLICIT | **MISSING** | `not-planned` | **MISSING** | **MISSING** |

> **Spalte 3 ist Historie, Spalte 4 ist der gültige Wert.** Wer Spalte 3 als aktuellen `source_type` liest, liest für **alle acht** Zeilen einen überholten Wert. Das ist keine hypothetische Verwechslung: `docs/ID-REGISTRY.md` §8 Punkt 42 meldet für NFR-008 eine Divergenz „PRD **EXPLICIT** gegen Registry **MISSING**" — sie beruht genau auf dieser Verwechslung. **Der gültige PRD-Wert für NFR-008 ist `MISSING` und stimmt mit der Registry überein; eine Divergenz besteht nicht.** Der Befund wird gemeldet, nicht durch eine Textänderung erzeugt: die historische Spalte wird **nicht** rückwirkend überschrieben, weil das die Auditspur des Nachaudits zerstören würde. Die Auflösung von §8 Punkt 42 liegt beim Registry-Owner.

Summe gültig: `EXPLICIT` 1 · `ASSUMPTION` 4 · `BLOCKER` 2 · `MISSING` 1 (abgeleitet aus Spalte 4, Stand 2026-07-20). Owner benannt: **0 von 8**. Referenzumgebung definiert: **0 von 8**. `evidence_gate` benannt: **7 von 8** — für NFR-008 MISSING.

**Nachträge vom 2026-07-19:**

- **NFR-005** trägt ab jetzt **REQ-037** statt des deprecateten REQ-014. `evidence_status` von `pending` auf **`not-planned`** korrigiert — nach der projektweiten Semantik setzt `pending` eine implementierte Instrumentierung voraus, die es nicht gibt. Die WCAG-**Fassung** ist mit **2.2** beziffert; die **Rechtsgrundlage** fehlt weiterhin, deshalb bleibt `ASSUMPTION`.
- **NFR-008** wird **nicht deprecatet**, sondern als aktive, aber unvollständig definierte Anforderung geführt (Begründung im eigenen Abschnitt). Die Verwaisung ist aufgehoben, die **Wirkungslosigkeit nicht**. Messdefinition offen als **OQ-013**.
- **`blocking_scope` ist projektweit entfallen** und durch `blocked_gates` und `blocked_activities` ersetzt (Details im Abschnitt „Feldwechsel"). **Nachtrag 2026-07-20:** diese beiden Felder gelten ausschließlich für `OQ-` und `CONTRA-`; sie sind aus den NFR-Abschnitten wieder **entfernt** worden, weil sie dort nie definiert waren.

**Nachtrag vom 2026-07-20:**

- **Die Spalte `blocking` ist aus der Übersicht und aus allen acht NFR-Abschnitten entfernt.** Der `NFR-`Raum führt **kein** `blocking`, **kein** `blocked_gates` und **kein** `blocked_activities`. Es wurde **keine Metamodell-Erweiterung** vorgenommen — die Frage ist innerhalb des eingefrorenen Modells gelöst. Begründung, Alternativenprüfung und die vier Prüfschritte stehen im Abschnitt „NFR-008 — Runde 4".

**NFR-008 zählt in der NFR-Zählung (8 von 8), NICHT in der Zahl aktiver Requirements.** Die beiden Zählungen sind getrennt und werden nie addiert; beide werden nach der Zählregel oben aus der Registry abgeleitet. NFR-008 ist damit nicht gleichzeitig verwaist und als aktive Anforderung gezählt.

### Querschnittsbefunde

| # | Befund | Art |
|---|---|---|
| XC-1 | Die frühere NFR-Tabelle hatte keine Source-Spalte und nannte für **keinen** der acht Zielwerte eine Quelle. `docs/SOURCE-MAP.md` zählt 102 `EXPLICIT`-Zellen ohne jede SRC-Angabe, davon 66 im PRD; die acht NFR-Zeilen gehörten in diese Klasse. | **BLOCKER** |
| XC-2 | Begriffskollision `EXPLICIT` zwischen diesem Audit und `docs/traceability.md` (siehe Warnung oben). | **BLOCKER**, Owner `docs/traceability.md` |
| XC-3 | Für **keinen** der acht NFRs ist ein Owner benannt (OQ-002). Kein NFR hat jemanden, der den Zielwert entscheidet oder die Messung abnimmt. | **BLOCKER** |
| XC-4 | Die Referenzumgebung ist für jede gerätegebundene Messung MISSING (OQ-003). Betrifft NFR-001, NFR-002, NFR-003, NFR-004, NFR-005. | **BLOCKER** |
| XC-5 | ~~Der ID-Raum `NFR-` ist **nicht registry-verwaltet** und damit nicht kollisionsgeschützt~~ → **GESCHLOSSEN am 2026-07-19:** `NFR-` und `USER-` sind in `docs/ID-REGISTRY.md` §5.1, §6.12 und §6.13 aufgenommen. Der Bestand ist unverändert übernommen, **keine NFR wurde umgedeutet und keine neue vergeben**. **Weiterhin nicht registry-verwaltet:** `DEC-`, `SRC-`, `VC-`, `GATE-` — deren Aufnahme bleibt eine offene Nutzerentscheidung. | **erledigt** / Restumfang **OPEN QUESTION** |

### Divergenzen Vision ↔ NFR

Requirement-spezifisch geprüft, nicht pauschal abgetan:

| # | Befund | Art |
|---|---|---|
| DIV-1 | Die Vision führt für **keinen** der acht NFRs einen Zielwert. Es gibt daher keine numerische Wert-für-Wert-Divergenz. Geprüft am 2026-07-19 gegen `docs/vision/…vision.md`, Abschnitte Target Group, User Needs, Product Value, Business Goals, Success Signals, Boundaries, Assumptions, Missing Items sowie VIS-001…VIS-011. Die einzigen quantitativen Vision-Werte sind die VIS-006-Success-Signals (>30 %, >50 %, >25 %, >1,0, >25 %, >40 %, >60 %) — keiner davon ist eine Distanz-, Batterie-, Performance-, Accessibility-, Datenschutz- oder Sicherheitsschwelle. Die Abwesenheit wurde **je Abschnitt nachgesehen, nicht angenommen**. | COVERAGE_GAP |
| DIV-2 | Die Vision klassifiziert die VIS-006-Zielwerte als `EXPLICIT`; `docs/traceability.md` klassifiziert **dieselben Werte** als `ASSUMPTION`, „nicht empirisch validiert". Nicht still zugunsten des stärkeren Werts aufgelöst, sondern als **CONTRADICTION** gemeldet. Betrifft VIS-006, nicht die acht NFRs — hier geführt, weil es dieselbe Defektklasse ist. | **BLOCKER**, Owner Nutzer / Vision / Traceability |
| DIV-3 | NFR-005 (Accessibility) hatte bis zum 2026-07-19 **überhaupt keine** Entsprechung in der Vision; das damalige REQ-014 hing an VIS-009 (Privacy Boundary) — fachlich unpassend. **VIS-011 (Accessibility Boundary)** wurde angelegt, `source_type = ASSUMPTION`, **unbestätigt**; NFR-005 trägt seit dem 2026-07-19 **REQ-037**. **Teilweise geschlossen:** die Canvas-Lücken sind erledigt — CAN-099 ist `active` (Accessibility) und **CAN-141** neu vergeben (Designsystem, trägt REQ-038). **Offen bleibt:** VIS-011 unbestätigt, und **REQ-038 hat überhaupt keinen Vision-Anker** (VIS-012 reserviert, Inhalt MISSING). | **BLOCKER** |
| DIV-4 | VIS-009 (Privacy Boundary) und NFR-006 decken sich in **beide Richtungen** nicht. Nur VIS-009: Profile standardmäßig privat; Live-Standort pro Aktivität Opt-in, zeitlich begrenzt, start-/endpunktverschleiert; Health-Daten nicht für Werbung. Nur NFR-006: „EU-orientiertes Hosting". Kein Widerspruch, aber eine Deckungslücke: die Vision-Klauseln hängen an REQ-018/REQ-030, nicht an einem NFR, und sind damit nicht als nicht-funktionale Schranke geführt. | OPEN QUESTION |
| DIV-5 | **Das PRD widersprach sich bei NFR-002 selbst.** Die alte NFR-Tabelle führte `EXPLICIT`; die REQ-003-Messmodellzelle schreibt zum selben Wert: „für dieses Produkt **nicht empirisch belegt**". Identischer Befund in `docs/traceability.md`. Der schwächere, belegte Befund gewinnt: NFR-002 = `ASSUMPTION`. | CONTRADICTION, **aufgelöst** |
| DIV-6 | NFR-006 sagt „EU-orientiertes Hosting"; DEC-013 / CONTRA-006 hält fest, dass das für den nachgelagerten Routing-Anbieter möglicherweise **nicht** gilt. Kein formaler Widerspruch — „orientiert" ist schwach genug, um beides zu decken. **Genau das ist das Problem:** der Begriff ist als Zielwert nicht prüfbar. | OPEN QUESTION |

### NFR-001 — Distanzgenauigkeit

| Feld | Wert |
|---|---|
| genaue Aussage | Die aufgezeichnete Distanz weicht nach Anwendung des GPS-Filters um weniger als 3 % von der Distanz einer definierten Referenzstrecke ab. |
| Metrik | Relative Abweichung der gefilterten Trackdistanz gegenüber der bekannten Referenzstreckenlänge |
| Einheit | Prozent |
| Zielwert / Pass-Bedingung | **< 3 % Abweichung**, getrennt nachgewiesen für Run und Bike und getrennt je Plattform (iOS, Android) |
| Quelle des Zielwerts | **KEINE GEFUNDEN.** Der Wert stand hier ohne Quellenangabe. Volltextsuche über `docs/` am 2026-07-19: „< 3 %" erscheint ausschließlich als Wiederholung dieses PRD-Werts. Keine Nutzerbestätigung, keine externe Norm, keine Messreihe. |
| `source_type` | **ASSUMPTION** (vorher EXPLICIT) — festgelegt durch Nutzerentscheidung 2026-07-19 |
| `confirmation_type` | `unconfirmed` |
| `measurement_type` | **OPERATIONAL_QUALITY** |
| `measurement_window` | Je vollständigem Lauf über die Referenzstrecke; getrennt Run und Bike, getrennt iOS und Android. Eine **Mindestanzahl Wiederholungen** je Kombination nennt kein Artefakt: **MISSING** — ohne sie ist kein Konfidenzintervall bestimmbar und ein Einzellauf kann den Wert zufällig treffen. |
| Testmethode | Realer Feldtest auf einer definierten Referenzstrecke bekannter Länge; Vergleich der gefilterten Trackdistanz gegen die Referenzlänge. Mindestklasse `production-verified` — im Labor nicht nachweisbar. |
| Referenzumgebung | **MISSING** — OQ-003 (Minimum iOS/Android und Referenzgeräte) ist offen. Auch die Referenzstrecke selbst ist in keinem Artefakt benannt oder vermessen: **MISSING**. |
| `evidence_source` | EV-002 (Gerätetest je Sport und Plattform auf Referenzstrecke), EV-004 (Drift-, Tunnel-, Sprung- und Hochgeschwindigkeits-Fixtures) |
| `evidence_status` | **`pending`** — kein Code, kein Build, keine Messung. `verified` erst nach realen Referenzstreckentests auf festgelegten Referenzgeräten. |
| `owner` | **MISSING — OWNER-BLOCKER** (OQ-002). Zusätzlich blockierend für die Messung: OQ-003, Owner der Frage „Engineering/QA". |
| `release_gate` | **GATE-A0** (Stufe A0) |
| `evidence_gate` | **A0** — abgeleitet aus `release_gate` (frühestes Gate, an dem der Nachweis fällig wird). **Kein `blocking`, kein `blocked_gates`, kein `blocked_activities`:** diese Achsen sind nach Registry §3.1 und §9 Bedingung 9 ausschließlich für `OQ-` und `CONTRA-` definiert (§6.13.2, Runde 4). |
| rationale | Der Wert ist plausibel und wird als vorläufiges Engineering-Ziel gebraucht, hat aber **keine belegte Herkunft**. VIS-003 („Nutzer benötigen verlässliches Tracking") ist eine qualitative Absicht und macht 3 % nicht EXPLICIT — das sind zwei getrennte Aussagen. EXPLICIT erst nach ausdrücklicher Nutzerbestätigung oder belastbarer Quelle. |

**Offene Punkte:** MISSING Referenzstrecke (nicht benannt, nicht vermessen) · MISSING Wiederholungsanzahl je Sport/Plattform-Kombination · MISSING zulässige Verwurfsquote des Filters · **BLOCKER** Referenzgeräte (OQ-003).

### NFR-002 — Batterie

| Feld | Wert |
|---|---|
| genaue Aussage | Der Batterieverbrauch bei aktivem Tracking bleibt unter 10 % pro Stunde auf definierten Referenzgeräten; der Messwert ist zu dokumentieren. |
| Metrik | Batterieladungsabnahme pro Stunde bei aktivem Tracking mit Background-Location |
| Einheit | Prozentpunkte Ladung pro Stunde |
| Zielwert / Pass-Bedingung | **< 10 % pro Stunde.** Run und Bike getrennt, iOS und Android getrennt, je mindestens ein Messlauf. |
| Quelle des Zielwerts | **KEINE GEFUNDEN.** Der Wert stand ohne Quelle und wird von der Quelle selbst als „Ziel" bezeichnet. Die REQ-003-Messmodellzelle und `docs/traceability.md` halten ausdrücklich fest, dass der Wert „für dieses Produkt nicht empirisch belegt" ist. |
| `source_type` | **ASSUMPTION** (vorher EXPLICIT) — Nutzerentscheidung 2026-07-19; zusätzlich durch das PRD selbst gestützt (DIV-5) |
| `confirmation_type` | `unconfirmed` |
| `measurement_type` | **OPERATIONAL_QUALITY** |
| `measurement_window` | Eine **zusammenhängende Stunde** aktives Tracking; Wiederholung vor jedem Gate ab A0. |
| Testmethode | Realer Gerätetest mit aktivem Background-Tracking über eine zusammenhängende Stunde. **Zwingend zu dokumentieren, weil sonst nicht vergleichbar:** Display-Zustand (an/aus, Helligkeit), Netzwerkzustand (WLAN/Mobilfunk/Flugmodus), GPS-Sampling-Rate, Kartendarstellung aktiv/inaktiv, Ausgangsladestand, Umgebungstemperatur. |
| Referenzumgebung | **MISSING** — „definierte Referenzgeräte" werden gefordert, aber nirgends definiert (OQ-003). Ohne Geräteliste ist der Wert nicht vergleichbar: derselbe Code ergibt auf unterschiedlichen Geräten stark abweichende Werte. |
| `evidence_source` | EV-003 (30-Minuten-Kill-/Background-Test) deckt das Background-Verhalten ab, **nicht** die Stundenmessung. Für die Batteriemessung selbst benennt kein Artefakt eine eigene EV-ID: **MISSING**. CAN-116 („Batterietests") existiert, ist aber keine EV-ID. |
| `evidence_status` | **`pending`** — kein Code, kein Gerätetest. Nachweis erst mit festgelegten Referenzgeräten, dokumentiertem Display-, Netzwerk- und GPS-Sampling-Zustand, aktivem Background-Tracking und mindestens einem Messlauf **je Sport und je Plattform**. |
| `owner` | **MISSING — OWNER-BLOCKER** (OQ-002); Referenzgeräte OQ-003 („Engineering/QA") |
| `release_gate` | **GATE-A0** (Stufe A0) |
| `evidence_gate` | **A0** — abgeleitet aus `release_gate` (frühestes Gate, an dem der Nachweis fällig wird). **Kein `blocking`, kein `blocked_gates`, kein `blocked_activities`:** diese Achsen sind nach Registry §3.1 und §9 Bedingung 9 ausschließlich für `OQ-` und `CONTRA-` definiert (§6.13.2, Runde 4). |
| rationale | Doppelter Befund: (1) der Zielwert hat keine Quelle, (2) das PRD widersprach seiner eigenen EXPLICIT-Angabe. Beides zeigt in dieselbe Richtung. Die Messung ist ohne dokumentierten Gerätezustand wertlos — Display an/aus allein verändert das Ergebnis stärker als die 10-%-Schwelle. |

**Offene Punkte:** CONTRADICTION aufgelöst (DIV-5) · MISSING eigene EV-ID für die Batteriemessung · **BLOCKER** Referenzgeräte (OQ-003).

### NFR-003 — Zuverlässigkeit

| Feld | Wert |
|---|---|
| genaue Aussage | Bei App-Kill oder Absturz gehen keine Aktivitätsdaten verloren; Session-Recovery ist verpflichtend. |
| Metrik | (a) Anzahl verlorener Aktivitäten, (b) Anteil erfolgreicher Session-Recoveries, (c) Anzahl inkonsistenter Indexe nach Migration |
| Einheit | (a) Anzahl, (b) Prozent, (c) Anzahl |
| Zielwert / Pass-Bedingung | **Nullschwelle:** 0 verlorene Aktivitäten über Kill- und Migrations-Fixtures, 0 inkonsistente Indexe nach Migration, jede Migration idempotent wiederholbar. Session-Recovery gelingt in **100 %** der 30-Minuten-Kill-Tests je Plattform und je Sportart. |
| Quelle des Zielwerts | **KEINE EIGENSTÄNDIGE QUELLE GEFUNDEN.** Die Nullschwelle ist keine gewählte Zahl, sondern die logische Übersetzung der Anforderung selbst („kein Datenverlust" = 0) — insoweit nicht belegbedürftig. Belegbedürftig **und unbelegt** sind: die Anforderung selbst (EXPLICIT ohne Quelle) und die Operationalisierung „30 Minuten", „je Plattform", „je Sportart" aus EV-003. |
| `source_type` | **ASSUMPTION** (vorher EXPLICIT) |
| `confirmation_type` | `unconfirmed` |
| `measurement_type` | **OPERATIONAL_QUALITY** |
| `measurement_window` | 30 Minuten je Kill-/Background-Test, je Plattform und je Sportart; Wiederholung vor jedem Gate ab A0. |
| Testmethode | Kontrolliertes Beenden der App bzw. erzwungener Absturz während laufender Aufzeichnung; anschließende Prüfung auf Vollständigkeit des Tracks und erfolgreiche Wiederherstellung der Session. Ergänzend Migrations-Fixtures gegen die lokale Datenbank. |
| Referenzumgebung | **MISSING** — OQ-003. Zusätzlich relevant und **nicht spezifiziert: die OS-Versionen**, da das Kill-Verhalten von iOS und Android versionsabhängig ist (RISK-001 „Background-GPS wird durch OS gedrosselt oder beendet", Severity critical). |
| `evidence_source` | EV-003 (30-Minuten-Kill-/Background-Test je Plattform und Sport), EV-005 (SQLite-Repository-Tests, Kill-Test und Migrations-Fixtures) |
| `evidence_status` | **`pending`** — beide EV-IDs sind definiert, aber es existiert kein Code. Kein Testlauf hat stattgefunden. |
| `owner` | **MISSING — OWNER-BLOCKER** (OQ-002) |
| `release_gate` | **GATE-A0** (Stufe A0) |
| `evidence_gate` | **A0** — abgeleitet aus `release_gate` (frühestes Gate, an dem der Nachweis fällig wird). **Kein `blocking`, kein `blocked_gates`, kein `blocked_activities`:** diese Achsen sind nach Registry §3.1 und §9 Bedingung 9 ausschließlich für `OQ-` und `CONTRA-` definiert (§6.13.2, Runde 4). |
| rationale | Die Nullschwelle ist sauber und braucht keine externe Quelle — sie folgt aus der Anforderung. ASSUMPTION bezieht sich darauf, dass die Anforderung selbst nur mit EXPLICIT **ohne Quelle** geführt wurde und die Testparameter (30 min, je Plattform, je Sportart) in einem **abgeleiteten** Artefakt gesetzt wurden, nicht vom Nutzer. Warum 30 und nicht 60 Minuten, ist nirgends begründet. |

**Offene Punkte:** MISSING Auto-Pause-Falschauslösungsrate ohne Schwellwert · MISSING Zielwert für die Rate technisch abgebrochener Sessions (wird gemessen und dokumentiert, aber nicht bewertet) · MISSING Begründung des 30-Minuten-Fensters · **BLOCKER** Referenzgeräte und OS-Versionen (OQ-003).

### NFR-004 — Performance

| Feld | Wert |
|---|---|
| genaue Aussage | Die Tracking-UI bleibt flüssig; Kartenlayer werden viewportbasiert geladen; vor Stufe D findet ein Geo-Lasttest statt. |
| Metrik | **MISSING** — kein Artefakt benennt eine Metrik. In Frage kämen Bildrate, Renderzeit des Kartenlayers, Frame-Drop-Rate, Interaktionslatenz; **keine davon ist gewählt**. |
| Einheit | **MISSING** — keine Millisekunden-, Bildraten- oder Perzentilangabe in irgendeinem Artefakt |
| Zielwert / Pass-Bedingung | **MISSING.** Wörtlich aus `docs/traceability.md`: „NFR-004 fordert viewportbasierte Kartenlayer und einen Geo-Lasttest vor D, nennt aber keine Millisekunden- oder Bildratenschwelle: MISSING." Ebenda: „Entscheidungsschwelle MISSING — Quorumswert, Verfallsrate und Performanceschwelle (NFR-004) sind unbeziffert. Vor Gate D zu entscheiden." |
| Quelle des Zielwerts | **KEINE GEFUNDEN** — es gibt keinen Zielwert, den man belegen könnte. „Flüssig" ist kein Zielwert, sondern ein Adjektiv. |
| `source_type` | **BLOCKER** (vorher EXPLICIT) — BLOCKER statt MISSING, weil die Definition greift: **ohne Zielwert ist ein Gate bzw. Test nicht belastbar planbar.** Der Geo-Lasttest ist als Pflicht vor Gate D festgeschrieben, hat aber keine Pass/Fail-Bedingung. Ein Test ohne Bestehensgrenze kann nicht bestanden werden — er kann nur behauptet werden. |
| `confirmation_type` | `unconfirmed` |
| `measurement_type` | **OPERATIONAL_QUALITY** |
| `measurement_window` | **MISSING** — kein Artefakt definiert ein Messfenster oder eine Lastdauer. |
| Testmethode | Teilweise beschrieben: Karten-Lasttest auf realem Gerät mit realer Datenmenge (Stufe 3, EV-026). **Was gemessen wird, bleibt offen.** Für die A0-Aussage „Tracking-UI flüssig" benennt kein Artefakt überhaupt eine Testmethode. |
| Referenzumgebung | **MISSING, zweifach:** (1) Geräte (OQ-003); (2) **Datenmenge** — gefordert sind „reale Aktivitätsdichten aus mindestens einer Stadt", weil synthetische Gleichverteilungen die Ballung unterschätzen; eine solche Datenbasis **existiert nicht**. |
| `evidence_source` | EV-026 (Geo-Fixtures, Simulation und Karten-Lasttest) — deckt nur den Territory-Anteil ab Stufe D. Für „Tracking-UI flüssig" ab A0 existiert **KEINE EV-ID: MISSING**. |
| `evidence_status` | **`blocked`** — nicht `pending`. Der Test ist benannt, kann aber kein Ergebnis liefern, solange keine Schwelle existiert. Der Nachweis scheitert **nicht an fehlendem Code**, sondern an der fehlenden Bestehensbedingung — das bliebe auch mit fertigem Code so. |
| `owner` | **MISSING — OWNER-BLOCKER** (OQ-002); Schwellenentscheidung zusätzlich an OQ-008 gebunden |
| `release_gate` | **GATE-A0** (Klausel „Tracking-UI flüssig", unbeziffert) **und GATE-D** (Geo-Lasttest, unbeziffert) |
| `evidence_gate` | **A0** — abgeleitet aus `release_gate` (frühestes Gate, an dem der Nachweis fällig wird). **Kein `blocking`, kein `blocked_gates`, kein `blocked_activities`:** diese Achsen sind nach Registry §3.1 und §9 Bedingung 9 ausschließlich für `OQ-` und `CONTRA-` definiert (§6.13.2, Runde 4). |
| rationale | **NFR-004 ist der schwächste der acht:** Anforderung ohne Metrik, ohne Einheit, ohne Schwelle, ohne Messfenster, ohne Datenbasis. Es wurde ausdrücklich **kein** plausibler Wert eingesetzt — weder 60 fps noch 16 ms noch ein Perzentil. Jede solche Zahl wäre erfunden. Der Zielwert ist vor Gate D zu entscheiden; für die A0-Klausel gibt es nicht einmal einen Fälligkeitszeitpunkt. |

**Offene Punkte:** **BLOCKER** keine Performanceschwelle (Metrik, Einheit, Wert) — vor Gate D zu entscheiden · MISSING EV-ID für die A0-Klausel „Tracking-UI flüssig" · MISSING reale Aktivitätsdichten als Testdatenbasis · MISSING Messfenster und Lastdauer.

### NFR-005 — Accessibility

| Feld | Wert |
|---|---|
| genaue Aussage | Alle Screens erfüllen WCAG AA, unterstützen Dynamic Type und Screenreader und verwenden keine reine Farbcodierung. |
| Metrik | (a) Anteil ausgelieferter Screens, die Kontrast-, Dynamic-Type- und Screenreader-Prüfung in Light und Dark Mode bestehen; (b) Anzahl Zustände, die allein über Farbe unterschieden werden |
| Einheit | (a) Prozent, (b) Anzahl |
| Zielwert / Pass-Bedingung | **100 % Abdeckung, 0 Zustände** ohne zusätzliches Symbol oder Textlabel. „Kein Prozentziel unterhalb von 100 — die Anforderung ist eine Schranke, keine Quote." |
| Quelle des Zielwerts | **TEILWEISE — eine der beiden Lücken ist seit dem 2026-07-19 geschlossen, die andere nicht.** (1) **Fassung: nachgetragen.** Die frühere Angabe „WCAG AA" stand ohne Version, obwohl 2.0 AA, 2.1 AA und 2.2 AA unterschiedliche Erfolgskriterien haben. Die Nutzerentscheidung vom 2026-07-19 beziffert die Fassung in CAN-099 und REQ-037 als **2.2**. (2) **Rechtsgrundlage: weiterhin MISSING.** In keinem Artefakt wird eine Rechtsgrundlage zitiert, die WCAG 2.2 AA für dieses Produkt verbindlich macht — kein Verweis auf EAA, BFSG oder eine Store-Vorgabe. Die Beweislatte „eine verbindliche externe Regel wird **konkret zitiert**" bleibt damit **unerfüllt**: die Norm ist jetzt vollständig benannt, ihre Verbindlichkeit nicht. |
| `source_type` | **ASSUMPTION** (vorher EXPLICIT) |
| `confirmation_type` | `unconfirmed` |
| `measurement_type` | **COMPLIANCE_CONTROL** |
| `measurement_window` | Je ausgeliefertem Screen, vor jedem Gate ab A0 (**REQ-037** läuft über Release A0-A2: Accessibility-Basis ab A0, vollständiger Audit spätestens A2). Kein zeitbasiertes Fenster — es ist eine vollständige Abdeckungsprüfung. |
| Testmethode | Kontrastprüfung, Dynamic-Type-/Font-Scaling-Prüfung und Screenreader-Durchlauf mit **VoiceOver UND TalkBack** in Light und Dark Mode je Screen (**EV-037**). Der **Token-Review** gehört seit dem 2026-07-19 **nicht mehr hierher** — er ist der Designsystem-Nachweis (EV-038 zu REQ-038) und war in EV-014 mit dem Accessibility-Nachweis vermischt. |
| Referenzumgebung | **MISSING** — weder Geräte (OQ-003) noch die **Screenreader-Matrix** sind festgelegt: VoiceOver und TalkBack in welchen OS-Versionen, welche Schriftgrößenstufen, welche Kontrastmessmethode. |
| `evidence_source` | **EV-037** (WCAG-2.2-AA-Audit, VoiceOver- und TalkBack-Durchlauf je Plattform, Dynamic-Type-/Font-Scaling-Prüfung, dokumentierte Kontrastprüfung). Ersetzt das deprecatete EV-014. |
| `evidence_status` | **`not-planned`** (korrigiert 2026-07-19, vorher `pending`). Zwei Schritte, beide begründet: **(1) `pending` ist ausgeschlossen** — nach der projektweiten Semantik setzt `pending` eine **implementierte Instrumentierung** voraus, und es existiert weder Code noch Build noch CI. **(2) `planned` wäre ebenfalls zu hoch.** `planned` verlangt, dass Metrik, Berechnung **und** Messverfahren definiert sind. Metrik und Pass-Bedingung sind es — das Verfahren nicht: Referenzgeräte (OQ-003), Screenreader-Matrix (VoiceOver/TalkBack in welchen OS-Versionen), Schriftgrößenstufen und Kontrastmessmethode sind **MISSING**. **Was nicht spezifiziert ist, kann nicht instrumentiert werden**; ein Zielwert ohne Messverfahren ist noch kein Messkonzept. Konsistent mit **EV-037** (`not-planned`, Registry §6.7). |
| `owner` | **MISSING — OWNER-BLOCKER** (OQ-002) |
| `release_gate` | **GATE-A0 bis GATE-A2**, erstmalige Abnahme mit GATE-A0, vollständiger Audit spätestens GATE-A2 vor öffentlichem Store-Release |
| `evidence_gate` | **A0** — abgeleitet aus `release_gate` (frühestes Gate, an dem der Nachweis fällig wird). **Kein `blocking`, kein `blocked_gates`, kein `blocked_activities`:** diese Achsen sind nach Registry §3.1 und §9 Bedingung 9 ausschließlich für `OQ-` und `CONTRA-` definiert (§6.13.2, Runde 4). |
| rationale | **Die Nennung einer Norm ist noch keine Verbindlichkeit.** Die Fassung ist seit dem 2026-07-19 mit **2.2** beziffert; damit ist ein Audit überhaupt erst bestehbar oder durchfallbar. `ASSUMPTION` bleibt trotzdem, weil die zweite Hälfte der Beweislatte offen ist: **keine zitierte Rechtsgrundlage**, die WCAG 2.2 AA für dieses Produkt verbindlich macht. Die Einstufung wurde **nicht** hochgezogen, nur weil eine Lücke geschlossen wurde. |

**Offene Punkte:** ~~**BLOCKER** WCAG-Version nicht spezifiziert~~ → **geschlossen 2026-07-19** (Fassung 2.2, CAN-099/REQ-037) · MISSING Rechtsgrundlage der Verbindlichkeit · MISSING Screenreader- und Gerätematrix (OQ-003) · ~~**BLOCKER** CAN-099 `reserved` und inhaltlich MISSING~~ → **geschlossen**, CAN-099 ist `active` und ausschließlich Accessibility · ~~**BLOCKER** kein atomares Canvas-Item für das tokenbasierte monochrome Designsystem~~ → **geschlossen**, **CAN-141** vergeben (trägt REQ-038, nicht NFR-005) · **BLOCKER** VIS-011 als Vision-Anker unbestätigt (DIV-3).

⚠️ **Präzisierung 2026-07-20 zur geschlossenen Fassungslücke — kein Wiederaufreißen des Blockers.** „Fassung nachgetragen / BLOCKER geschlossen" heißt: es ist **eine Fassung benannt**, sodass ein Audit überhaupt bestehbar oder durchfallbar ist. Es heißt **nicht**, dass die Ziffer quellenbelegt wäre. Volltextsuche über alle vier Quellen: alle vier WCAG-Nennungen (`docs/sources/SRC-001-…:176`, `:256`, `SRC-002-…:134`, `SRC-003-…:100`) lauten „WCAG AA" bzw. „WCAG-AA" **ohne Fassungsangabe**; „WCAG 2" ergibt **0 Treffer**. Die Ziffer **2.2** ist damit `ASSUMPTION` — konsistent mit der Belegtabelle bei REQ-037 („UNBELEGT") und mit `source_type = ASSUMPTION` hier. Das ist **nicht folgenlos**: `docs/EVIDENCE-LEDGER.md` führt EV-037 [ACC1] „WCAG-2.2-AA-Audit bestanden" als **vor A2 blockierend für den Store-Release**. Der geschlossene Spezifikationsblocker bleibt geschlossen; die Belegfrage ist davon getrennt und bleibt offen.

**Web-Erstreckung: NFR-005 war nie betroffen.** Die Klausel „und alle nutzbaren Web-Auskopplungen" stand in REQ-037, AC-037 (Given) und im `signal`-Feld des REQ-037-Messmodells, **nicht** in den Feldern dieses NFR-Abschnitts. Durch ihre Entfernung am 2026-07-20 ändert sich hier kein Wert — der Vermerk steht nur, damit die Abwesenheit nicht als Übersehen gelesen wird.

**NFR-005 trägt ab jetzt REQ-037, nicht mehr REQ-014.** REQ-014 ist deprecated; die Designsystem-Hälfte liegt bei REQ-038 und wird **nicht** von NFR-005 gemessen. Abgrenzung: **CAN-099 regelt die Zugänglichkeit, CAN-141 die Gestaltungssprache.** Der gemeinsame Satzteil „Farbe ist nie der einzige Informationsträger" wirkt in beiden — als Accessibility-Schranke (AC-037 d) und als Gestaltungsregel (AC-038 a/b). Dieselbe Beobachtung, zwei getrennt prüfbare Pflichten, zwei getrennte Nachweise.

### NFR-006 — Datenschutz

| Feld | Wert |
|---|---|
| genaue Aussage | Privacy by default, EU-orientiertes Hosting, Export und Löschung sowie Datenminimierung. |
| Metrik | Heterogen je Klausel: Anteil personenbezogener Daten, die eine Accountlöschung nicht überleben; Verarbeitungsregion; Aufbewahrungsfristen je Datenart; Umfang serverseitig verarbeiteter Daten |
| Einheit | Heterogen: Prozent, Regionsbezeichner, Tage, Feldliste |
| Zielwert / Pass-Bedingung | **Nur teilweise bestimmt.** BESTIMMT durch **DEC-012**: Löschumfang abschließend aufgezählt; historische Daten überleben nur wirksam anonymisiert, sonst Löschung. BESTIMMT durch **DEC-013** für den A0-Routing-Proxy: Retention 0 für Koordinaten-Payload, technische Logs max. 7 Tage, `eu-central-1`. **UNBESTIMMT:** Aufbewahrungsfristen für GPS-, Health- und Live-Daten allgemein (OQ-009); Hosting-Region des eigentlichen Backends (OQ-005); Verarbeitungsregion des Routing-Anbieters. |
| Quelle des Zielwerts | **GEMISCHT.** Belegte Nutzerquelle für den Löschumfang: **DEC-012** und CONTRA-005 (Nutzerentscheidung 2026-07-19), geführt als **SRC-006**. Belegte Nutzerquelle für die A0-Proxy-Baseline: **DEC-013**. **KEINE** Quelle für „EU-orientiertes Hosting" als Zielwert und **KEINE** für Retentionsfristen. |
| `source_type` | **BLOCKER** (vorher EXPLICIT) — BLOCKER, weil eine **Architekturentscheidung** ohne den fehlenden Zielwert nicht belastbar planbar ist: DEC-012 schreibt vor, dass Datenmodell und Event-Historie Identität und historische Aggregate technisch trennen müssen — **vor** Erstellung und Finalisierung des Datenbankschemas. Diese Trennung hängt an den Retentionsfristen, die MISSING sind (OQ-009). Das Schema kann damit nicht belastbar entworfen werden. |
| `requirement_source_type` | **EXPLICIT** — der Requirement-**Kern** ist durch zwei belegte Nutzerentscheidungen gedeckt. Getrennt geführt, weil Anforderung und Zielwert hier unterschiedlich zu bewerten sind. |
| `confirmation_type` | **teilweise `user-confirmed`** (Löschumfang via DEC-012, A0-Proxy-Baseline via DEC-013); im Übrigen `unconfirmed` |
| `measurement_type` | **COMPLIANCE_CONTROL** |
| `measurement_window` | Kein Zeitfenster — Abdeckungs- und Nullschwellenprüfung je Datenfluss. Für Retention wäre das Fenster die jeweilige Frist selbst; **genau die fehlt**. |
| Testmethode | Datenflussdiagramm mit 100 % Abdeckung, RLS-Tests, Löschungsnachweis (EV-034, EV-017). Für **„wirksam anonymisiert" existiert KEIN Prüfverfahren**: `docs/validation/validation-report.md` führt das als Befund B6 — ohne definiertes Verfahren ist Anonymisierungswirksamkeit nicht prüfbar. |
| Referenzumgebung | **MISSING** — Backend nicht entschieden (OQ-005); Verarbeitungsregion und Unterauftragsverarbeiter des Routing-Anbieters laut DEC-013 erst vor dem ersten externen Feldtest zu dokumentieren. |
| `evidence_source` | EV-017 (E2E-Flow, Offline-Test und Löschungsnachweis), EV-034 (Security-Review, RLS-Tests, Datenflussdiagramm und Löschungsnachweis), EV-027 (teilweise, für anonymisierte Historie), **EV-042** (Trennung von Identität und historischen Aggregaten — neu vergeben 2026-07-19; der Nachweis trägt `evidence_status: blocked`). |
| `evidence_status` | **`blocked`** — nicht `pending`. Mehrere Nachweise haben **keine Pass/Fail-Bedingung**: Retentionsfristen fehlen (OQ-009), ein Prüfverfahren für „wirksam anonymisiert" fehlt (Befund B6), und für die Schema-Trennung existiert keine EV-ID. Das ist **kein Code-Problem**: auch mit fertigem Code bliebe unentscheidbar, ob der Test bestanden ist. |
| `owner` | **MISSING — OWNER-BLOCKER** (OQ-002); OQ-009 nominell „Privacy/Product", OQ-005 „Engineering" — beides **Rollen, keine Personen** |
| `release_gate` | **GATE-A0 bis GATE-E**; harte Punkte: **vor Finalisierung des Datenbankschemas** (DEC-012) und **GATE-B** |
| `evidence_gate` | **A0** — abgeleitet aus `release_gate` (frühestes Gate, an dem der Nachweis fällig wird). **Kein `blocking`, kein `blocked_gates`, kein `blocked_activities`:** diese Achsen sind nach Registry §3.1 und §9 Bedingung 9 ausschließlich für `OQ-` und `CONTRA-` definiert (§6.13.2, Runde 4). |
| rationale | Der Requirement-Kern ist durch zwei belegte Nutzerentscheidungen gedeckt und deshalb als `requirement_source_type = EXPLICIT` geführt — **die einzige Stelle neben NFR-007, an der eine Nutzerquelle wirklich trägt**. Der **Zielwert** ist es nicht: „EU-orientiertes Hosting" ist als Formulierung nicht prüfbar, und die Retentionsfristen fehlen vollständig. Beides zusammen blockiert eine Architekturentscheidung, die laut DEC-012 früh zu treffen ist. Der schwächere Befund wurde **nicht** durch den stärkeren verdeckt. |

**Offene Punkte:** **BLOCKER** Retentionsfristen für GPS, Health und Live MISSING (OQ-009) — blockiert die Schema-Trennung aus DEC-012 · **BLOCKER** kein Prüfverfahren für „wirksam anonymisiert" (Befund B6) · ~~**BLOCKER** keine EV-ID für „Datenmodell trennt Identität und historische Aggregate"~~ → **als ID-Frage geschlossen 2026-07-19: EV-042.** Der Nachweis selbst bleibt `blocked` (OQ-009) · MISSING Backend und Hosting-Region (OQ-005) · MISSING Verarbeitungsregion, Unterauftragsverarbeiter und Transfergrundlage des Routing-Anbieters · **OPEN QUESTION** „EU-orientiertes Hosting" ist als Zielwert nicht prüfbar (DIV-6).

### NFR-007 — Sicherheit

| Feld | Wert |
|---|---|
| genaue Aussage | Keine Secrets im Client, sichere Auth, Row-Level-Security, Rate Limits, serverseitige Validierung. |
| Metrik | (a) Anzahl Routing-Provider-Keys im App-Bundle; (b) Anzahl Endpunkte ohne Rate Limit; (c) Anzahl Endpunkte ohne serverseitige Validierung; (d) konkrete Rate-Limit-Werte |
| Einheit | (a)–(c) Anzahl; (d) Requests pro Zeiteinheit |
| Zielwert / Pass-Bedingung | **BESTIMMT:** 0 Secrets im Client, ab A0 auch für den Routing-Proxy-Key; 0 Endpunkte ohne Rate Limit und serverseitige Validierung. **UNBESTIMMT:** die konkreten Rate-Limit-Werte. DEC-013 fordert „Rate Limit, Size-Limit, maximale Wegpunktzahl, Timeout, Kill Switch" — **ohne eine einzige Zahl**. |
| Quelle des Zielwerts | **GEFUNDEN — für eine Klausel.** „Keine Secrets im Client" ist durch eine **belegte Nutzerentscheidung** gedeckt: **DEC-005** (`user-confirmed`, 2026-07-19), **CAN-092** (Source Type `CONFIRMED`), CONTRA-002 (`resolved`), geführt als **SRC-006**. Die technische Begründung ist konkret und nachprüfbar: `EXPO_PUBLIC_*` wird ins JS-Bundle inlined und ist aus jedem Build extrahierbar. Für die übrigen Klauseln: **KEINE Quelle gefunden**. |
| `source_type` | **EXPLICIT** — **klauselbeschränkt**, siehe Aufschlüsselung unten. Diese Einschränkung ist **Teil der Klassifikation**, nicht eine Fußnote dazu. |
| `confirmation_type` | **`user-confirmed`** (nur Klausel „keine Secrets im Client"); übrige Klauseln `unconfirmed` |
| `measurement_type` | **COMPLIANCE_CONTROL** |
| `measurement_window` | Kein Zeitfenster — Nullschwellenprüfung je Build (Bundle-Scan) und je Endpunkt (Rate Limit, Validierung). Ab A0 fortlaufend bis GATE-E. |
| Testmethode | Bundle-Scan des ausgelieferten JS-Bundles auf Routing-Provider-Keys; Proxy-Integrationstest; Security-Review; RLS-Tests; Endpunkt-Inventar gegen Rate-Limit- und Validierungsabdeckung. Mindestklasse `real-boundary-smoke` — „ein gemockter Routing-Response verdeckt genau den NFR-007-Pfad". |
| Referenzumgebung | Für den Bundle-Scan: **ein realer Release-Build je Plattform — existiert nicht.** Für die Proxy-Kontrollen: die A0-Laufzeit laut CAN-096 (AWS Lambda + API Gateway, `eu-central-1`) — ausdrücklich **nur dokumentiert, nicht gebaut, keine AWS-Ressource angelegt**. |
| `evidence_source` | ASM-103 (Bundle-Scan ohne Routing-Key plus Proxy-Integrationstest), EV-034 (Security-Review, RLS-Tests, Datenflussdiagramm), EV-006 (Routing-Service-Tests) |
| `evidence_status` | **`pending`** — die Testmethode ist konkret und die Pass-Bedingung für die Kernklausel eindeutig; **es fehlt ausschließlich der Gegenstand**: kein Code, kein Build, kein Bundle. Deshalb `pending` und nicht `blocked`. Die Klausel „Rate Limits" ist dagegen ohne Zahlenwert nicht prüfbar und insoweit blockiert. |
| `owner` | **MISSING — OWNER-BLOCKER** (OQ-002) |
| `release_gate` | **GATE-A0 bis GATE-E.** DEC-005 stellt ausdrücklich fest: „NFR-007 gilt ab A0-E" — **nicht** erst ab Stufe B. |
| `evidence_gate` | **A0** — abgeleitet aus `release_gate` (frühestes Gate, an dem der Nachweis fällig wird). **Kein `blocking`, kein `blocked_gates`, kein `blocked_activities`:** diese Achsen sind nach Registry §3.1 und §9 Bedingung 9 ausschließlich für `OQ-` und `CONTRA-` definiert (§6.13.2, Runde 4). |
| rationale | Dies ist der **einzige** der acht NFRs, bei dem die Beweislatte für EXPLICIT tatsächlich erreicht wird — und zwar **nur für eine von fünf Klauseln**. Die Einstufung ist keine Hochstufung, sondern die Wiedergabe einer protokollierten Nutzerentscheidung vom 2026-07-19. Die übrigen vier Klauseln werden ausdrücklich **nicht** mit hochgezogen. `EXPLICIT + pending` ist hier die korrekte Kombination: die Herkunft ist belegt, der Nachweis steht aus. |

**Klausel-Aufschlüsselung — die Einstufung gilt nicht pauschal:**

| Klausel | `source_type` | Quelle |
|---|---|---|
| keine Secrets im Client | **EXPLICIT** | DEC-005 `user-confirmed`, CAN-092 `CONFIRMED`, CONTRA-002 `resolved`, SRC-006 |
| sichere Auth | **ASSUMPTION** | keine gefunden — kein Auth-Verfahren, kein Standard, keine Schwelle benannt |
| Row-Level-Security | **ASSUMPTION** | keine gefunden — setzt zudem den offenen Backend-Entscheid OQ-005 voraus |
| Rate Limits | **MISSING** | keine gefunden — kein Artefakt nennt einen Zahlenwert |
| serverseitige Validierung | **ASSUMPTION** | keine gefunden — Nullschwelle stammt aus `docs/traceability.md`, einem **abgeleiteten** Artefakt |

**Offene Punkte:** MISSING konkrete Rate-Limit-, Size-Limit-, Wegpunktzahl- und Timeout-Werte (DEC-013 fordert sie, beziffert keine) · MISSING Auth-Verfahren und -Standard · MISSING RLS setzt den offenen Backend-Entscheid voraus (OQ-005) · **BLOCKER** kein Code, kein Build — Bundle-Scan nicht durchführbar.

### NFR-008 — Wartbarkeit

| Feld | Wert |
|---|---|
| genaue Aussage | TypeScript strict, reine Domainmodule, versionierte Schemas, automatisierte Tests. |
| Metrik | **MISSING** — kein Artefakt benennt eine Metrik. In Frage kämen Testabdeckung, Anzahl Typfehler, Anteil abhängigkeitsfreier Domainmodule, Anzahl unversionierter Schemas; **keine davon ist gewählt**. |
| Einheit | **MISSING** |
| Zielwert / Pass-Bedingung | **MISSING.** Vier qualitative Zusagen **ohne jede Schwelle**. Insbesondere ist **keine Testabdeckungsquote** genannt — weder hier noch in einem anderen Artefakt. |
| Quelle des Zielwerts | **KEINE GEFUNDEN.** Volltextsuche über `docs/` am 2026-07-19: die Zeichenfolge „NFR-008" erschien im gesamten Repository **genau einmal** — in ihrer eigenen Definitionszeile. Kein Requirement, kein AC, keine EV-ID, keine Traceability-Zeile, kein Gate und kein Risiko referenzierte NFR-008. **Verwaisung inzwischen aufgehoben** (siehe unten), der fehlende Zielwert nicht. |
| `source_type` | **MISSING** (vorher EXPLICIT) — MISSING und **nicht** BLOCKER: die Anforderung blockiert derzeit kein Gate, **weil kein Gate sie referenziert**. Genau das ist der Befund — sie ist **wirkungslos**, nicht blockierend. |
| `confirmation_type` | `unconfirmed` |
| `measurement_type` | **PROCESS_CONTROL** — **Ergänzung zur bestehenden Taxonomie, offengelegt statt fehlzugeordnet.** Keine der vier im Repo verwendeten Klassen passt: es ist keine Laufzeiteigenschaft (nicht `OPERATIONAL_QUALITY`), keine Konformität gegen eine externe Schranke (nicht `COMPLIANCE_CONTROL`), keine Untersuchungsfrage (nicht `RESEARCH_HYPOTHESIS`) und kein Nutzersignal (nicht `PRODUCT_OUTCOME`). |
| `measurement_window` | **MISSING** — eine CI-durchgesetzte Eigenschaft wäre je Commit oder je Build zu prüfen; kein Artefakt legt das fest. |
| Testmethode | **MISSING** — keine benannt. *Ableitbar* wäre: TypeScript-Compiler im `strict`-Modus als CI-Gate, Importgraph-Prüfung der Domainmodule, Schema-Versionsprüfung, Coverage-Report. **Nichts davon ist in einem Artefakt festgelegt, deshalb wird es hier nicht als Testmethode geführt.** |
| Referenzumgebung | **MISSING** — es existiert **keine CI** im Repository. `docs/ID-REGISTRY.md` §9 hält fest, dass überhaupt kein ausführbares Prüfwerkzeug vorhanden ist. |
| `evidence_source` | **KEINE.** Kein EV-Eintrag referenziert NFR-008. EV-035 (CI-Regel, Ledger-Review, Gate-Checkliste) gehört zu REQ-035 und deckt die **Evidence-Disziplin** ab, nicht die Wartbarkeit. |
| `evidence_status` | **`not-planned`** — nicht `pending`. Kein Artefakt sieht überhaupt einen Nachweis für NFR-008 vor. `pending` wäre die falsche Aussage: **es steht nichts aus, weil nichts geplant ist.** |
| `owner` | **MISSING — OWNER-BLOCKER** (OQ-002) |
| `release_gate` | **MISSING** — kein Gate referenziert NFR-008. Die Gate-Tabelle nennt es nicht. Die Zuordnung ist Gegenstand von **OQ-013** und wird hier **nicht geraten**. |
| `evidence_gate` | **MISSING** — **kein Gate fordert NFR-008 ein.** Das ist der Befund, nicht eine Formalie. Zusammen mit `evidence_status = not-planned` (kein Messkonzept) und dem Fehlen jeder CI ist die Anforderung **inhaltlich real und operativ folgenlos**. Das bleibt so bis **OQ-013**. **Kein `blocking`, kein `blocked_gates`, kein `blocked_activities`** — der `NFR-`Raum führt diese Felder nicht (§6.13.2). |
| rationale | **Dass ein Must-artiges Qualitätsziel wirkungslos ist, ist der eigentliche Befund — nicht seine Unbedenklichkeit.** Nach `docs/ID-REGISTRY.md` §9 wäre ein aktiver Eintrag ohne jede Referenz eine **Waise** und damit ein Validierungsfehler. Die Verwaisung ist mit der Aufnahme von `NFR-` in die Registry (§6.13) aufgehoben; die fehlende Wirksamkeit ist es nicht. |

### NFR-008 — Entscheidung: definieren statt deprecaten (2026-07-19)

Die Vorgabe verlangte eine der beiden Auflösungen und nannte drei Vorfragen. Sie sind **einzeln** beantwortet, nicht pauschal:

| Vorfrage | Befund |
|---|---|
| Fachlich notwendige NFR? | **Ja.** Die vier Zusagen — TypeScript strict, reine Domainmodule, versionierte Schemas, automatisierte Tests — sind in `CLAUDE.md` und im Gesamtplan **projektweit verbindliche Arbeitsregeln** (u. a. „TDD ist mandatory", „TypeScript strict", `src/domain/` als „pure, dependency-free logic"). Die Substanz existiert; ihr fehlt **nur die Messdefinition**. |
| Durch ein anderes NFR dupliziert? | **Nein.** NFR-001…003 messen Betriebsqualität (Genauigkeit, Batterie, Zuverlässigkeit), NFR-004 Performance, NFR-005 Zugänglichkeit, NFR-006 Datenschutz, NFR-007 Sicherheit. **Keines** trifft eine Aussage über Codestruktur, Typsicherheit, Schemaversionierung oder Testautomatisierung. |
| Nur reservierte, nie definierte ID? | **Nein.** NFR-008 ist in diesem PRD mit **vier konkreten inhaltlichen Zusagen** definiert, nicht bloß reserviert. |

**Ergebnis: NFR-008 wird NICHT deprecatet.** Sie bleibt `active` mit unvollständiger Messdefinition. Kanonisch: `docs/ID-REGISTRY.md` §6.13.1.

⚠️ **Nicht vergeben — und zwar bewusst:** Metrik, Einheit, Schwellwert, Messfenster, Testmethode, Owner und Gate. Alle sieben sind aus keinem Artefakt ableitbar; sie sind Gegenstand von **OQ-013**. **Insbesondere wurde keine Testabdeckungsquote gesetzt:** die in `CLAUDE.md` genannten 80 % sind eine **globale Arbeitsregel des Nutzers**, kein für dieses Produkt beschlossener NFR-Zielwert. Sie hier einzusetzen wäre genau die stille Vererbung, die die Beweislatte verbietet.

**Verwaisung aufgehoben.** NFR-008 wird seit dem 2026-07-19 von `docs/ID-REGISTRY.md` §6.13 und §6.13.1, von **OQ-013** und von der Migrationstabelle referenziert. Zuvor kam die Zeichenfolge im gesamten Repository genau einmal vor — in ihrer eigenen Definitionszeile.

**Zählregel — NFR-008 ist nicht gleichzeitig verwaist und als aktive Anforderung gezählt.** NFR-008 zählt in der **NFR-Zählung** (`aktiv(NFR)`, Stand 2026-07-20: 8), **nicht** in `aktiv(REQ)` (Stand 2026-07-20: 40). Diese umfasst ausschließlich `REQ-`IDs. Die beiden Zählungen sind getrennt und werden nie addiert; beide werden nach der Zählregel im Kopf dieses Dokuments aus der Registry abgeleitet.

### NFR-008 — Runde 4 (2026-07-20): der `NFR-`Raum führt kein `blocking`

**Der Anlass ist belegt.** Die Übersichtstabelle oben führte bis zum 2026-07-20 eine Spalte `blocking` mit **acht hartkodierten Werten** (sieben `true`, für NFR-008 `false`). Zusammen mit den sechs `CONTRA-`Werten waren das 14 `blocking`-Werte im Projekt — und **die acht NFR-Werte rechnete niemand nach**: für den `NFR-`Raum existiert weder Formel noch Eingabe noch Wertebereich. Zusätzlich schrieb der NFR-008-Abschnitt selbst `blocked_gates = []` und `blocked_activities = []` fest, obwohl Registry §3.1 diese Achsen ausdrücklich **nur** für `OQ-` und `CONTRA-` definiert.

**Die Vorgabe stellte zwei Auflösungen zur Wahl: die kanonischen Achsen auf `NFR-` ausdehnen ODER `NFR-`Einträge gar kein `blocking` führen lassen. Entschieden ist die zweite.** Die vier Prüfschritte einzeln, nicht pauschal:

| Prüfung | Ergebnis |
|---|---|
| Passt die Achse `status` (`open`/`resolved`) auf ein NFR? | **Nein.** Sie beantwortet „Ist die Grundsatzfrage **entschieden**?" — eine Frage, die nur ein Widerspruch oder eine offene Frage hat. Ein NFR ist **keine Entscheidung**, sondern eine Anforderung; es benutzt die Achse `active`/`deprecated`/`reserved`. |
| Was liefert die Formel, wenn man sie trotzdem anwendet? | **Für alle acht NFRs `blocking = true`** — denn `active NOT IN [resolved]` ist immer wahr. Syntaktisch gültig, mechanisch reproduzierbar und **fachlich bedeutungslos**. Genau das Muster, gegen das dieses Dokument an anderer Stelle warnt. |
| Passt `resolution_status` (`undecided`/`decision-documented`/`accepted`)? | **Nein.** Ein Reifegrad einer Entscheidung; für ein NFR ohne Entscheidungsvorgang **nicht besetzbar, ohne einen Wert zu erfinden**. |
| Braucht es eine Metamodell-Erweiterung? | **Nein — und deshalb wird keine vorgenommen.** Die tragende Information ist im eingefrorenen Modell darstellbar: **welches Gate** die Anforderung einfordert, steht in `evidence_gate`; **wie weit** der Nachweis ist, in `evidence_status`. Für NFR-008 sind das `MISSING` und `not-planned`. |

**Ergebnis.** Der `NFR-`Raum führt **kein `blocking`, kein `blocked_gates`, kein `blocked_activities`**. Die Achsen bleiben auf `OQ-` und `CONTRA-` beschränkt. Aus der Übersichtstabelle ist die Spalte **entfernt**, aus allen acht NFR-Abschnitten sind die drei Zeilen **entfernt**. **NFR-008 wird nicht deprecatet** — die Begründung von 2026-07-19 gilt unverändert: die Anforderung hat realen, nicht duplizierten Inhalt, und eine Anforderung wegen fehlender Messung zu deprecaten würde Projektsubstanz löschen.

**Der Befund bleibt — er wird jetzt ohne Hilfsfeld gesagt.** Der frühere Satz „`blocking = false` ist hier kein Entwarnungssignal" ist ersatzlos gestrichen: er erklärte einen Wert, den es nicht geben darf.

> NFR-008 wird an **keiner Stelle wirksam**. `evidence_gate` ist **MISSING** — kein Gate fordert die Anforderung ein. `evidence_status` ist **not-planned** — es existiert kein Messkonzept. Es existiert **keine CI**, die die vier Zusagen durchsetzen könnte. Die Anforderung ist **inhaltlich real und operativ folgenlos**. Das bleibt so bis **OQ-013**.

**Offene Punkte:** ~~**BLOCKER** NFR-008 ist verwaist~~ → **geschlossen 2026-07-19** durch Aufnahme in die Registry (§6.13) und OQ-013 · ~~**BLOCKER** NFR-008 trägt ein `blocking`, das niemand nachrechnet~~ → **geschlossen 2026-07-20** (Registry §8 Punkt 35): der `NFR-`Raum führt kein `blocking` · **MISSING** Metrik, Einheit, Schwellwert, Messfenster, Testmethode, Owner und Gate (OQ-013, Registry §8 Punkt 25) · **MISSING** keine CI im Repository, die die vier Zusagen durchsetzen könnte · **BEFUND, unverändert:** NFR-008 ist an kein Gate gebunden und damit heute **wirkungslos**.

## Risks

Verbindliches Register: `docs/risks/revyr-risk-register.md`.

## Widerspruchs-Auflösungen (CONTRA-004, CONTRA-005, CONTRA-006)

Kanonisches Widerspruchs-Ledger: `docs/decisions/decision-log.md`, IDs geführt in `docs/ID-REGISTRY.md` §6.11. Dieses PRD **referenziert** die CONTRA-IDs und arbeitet die Entscheidungen inhaltlich ein; es vergibt keine IDs.

**Statusmodell nachgezogen (2026-07-19).** Die frühere Tabelle mischte Entscheidung und Nachweis in einem Feld (`DESIGN-RESOLVED / EVIDENCE-PENDING`). Diese Mischwerte sind als `status` **unzulässig** und wurden auf getrennte Achsen aufgeteilt. Kanonische Quelle der Feldwerte ist `docs/ID-REGISTRY.md` §6.11.1, wortgleich gespiegelt in `docs/decisions/decision-log.md`; bei Abweichung gilt die Registry. Die frühere **Statusdivergenz** (Registry führte CONTRA-004…006 noch als `open`) besteht **nicht mehr** — die Registry ist im Auftau-Schritt nachgezogen worden.

| Achse | Zulässige Werte | Bedeutung |
|---|---|---|
| `status` | `open` · `resolved` | **Nur** ob der fachliche/architektonische Widerspruch **entschieden** ist. Unzulässig: `DESIGN-RESOLVED`, `EVIDENCE-PENDING`, `pending`, `closed`, `mitigated`. |
| `resolution_status` | `undecided` · `decision-documented` · `accepted` | Reifegrad der Entscheidung |
| `evidence_status` | `not-required` · `not-planned` · `planned` · `pending` · `verified` · `failed` · `blocked` | Stand des Nachweises |

Ein Widerspruch erhält `status: resolved`, **sobald die Entscheidung getroffen ist — nicht erst, wenn die Evidence vorliegt.** Die Evidence lebt auf der `evidence_status`-Achse.

### Feldwechsel: `blocking_scope` ist entfallen (2026-07-19, C16)

**Der behobene Defekt.** `blocking_scope` mischte **Release-Gates** und **Tätigkeiten** in einer Liste. Die beiden Vokabulare sind disjunkt — deshalb lieferte die wörtliche Lesart der alten Formel („das aktuell geprüfte Gate ist in `blocking_scope` enthalten") für **jeden gegateten Eintrag `false`**: die Blockade verschwand genau dann, wenn gegen ein Gate geprüft wurde. Die Tabellenwerte standen zwar auf `true`, waren aber faktisch hartkodiert und nicht das Ergebnis der Formel.

`blocking_scope` ist **ersatzlos entfallen** und durch zwei disjunkte Felder ersetzt:

| Feld | Abgeschlossener Wertebereich |
|---|---|
| `blocked_gates` | `P0` · `A0` · `A1` · `A2` · `B` · `C` · `D` · `E` |
| `blocked_activities` | `documentation` · `planning` · `implementation` · `field-test` · `release` · `store-submission` · `database-schema-finalization` · `account-release` · `competition-release` · `territory-release` |

Die Werte sind **verlustfrei** übernommen: jeder Alt-Wert war eine Tätigkeit und steht jetzt in `blocked_activities`. `blocked_gates` ist **neu befüllt** und war vorher überhaupt nicht darstellbar — das ist exakt der behobene Defekt. Der Wert `none` ist entfallen und wird durch die leere Liste `[]` ausgedrückt.

**`blocking` wird abgeleitet, nie hartkodiert.** Kanonische Formel (Registry §3.1); **alle** Validatoren importieren dieselbe Implementierung, keine duplizierte Fassung, keine ID-spezifische Sonderbehandlung:

```
blocking = status            NOT IN ['resolved']
           OR resolution_status NOT IN ['accepted']
           OR evidence_status       IN ['failed', 'blocked']
           OR current_gate          IN blocked_gates
           OR current_activity      IN blocked_activities
```

⚠️ **Der Wortlaut der ersten Klausel ist normativ und nicht austauschbar (Registry §9 Bedingung 10, Runde 4).** Normativ ist `status NOT IN ['resolved']` — **ausdrücklich nicht** `status == 'open'`. Für die zwei gültigen Werte sind beide Fassungen äquivalent; für einen **fehlenden, leeren oder ungültigen** `status` sind sie es nicht:

| `status` | `status == 'open'` | `status NOT IN ['resolved']` (normativ) |
|---|---|---|
| `open` | `true` | `true` |
| `resolved` | `false` | `false` |
| fehlend / leer / ungültig | **`false` — die Blockade verschwindet still** | **`true` — fail-closed** |

Die normative Fassung ist **fail-closed**: ein fehlender `status` blockiert und erzeugt zusätzlich einen **Validierungsfehler**, keinen Toleranzfall. Frühere Berichte in diesem Lauf haben die Formel als `status == open` zitiert; **Wortlaut und Implementierung werden auf die normative Fassung angeglichen — nicht umgekehrt.**

⚠️ **Geltungsbereich: ausschließlich `OQ-` und `CONTRA-` (Registry §3.1, §9 Bedingung 9).** Die Felder `status`, `resolution_status`, `blocking`, `blocked_gates` und `blocked_activities` existieren **nur** für diese beiden Präfixe. Ein Werkzeug, das eines davon für einen `NFR-`, `REQ-`, `CAN-`, `VIS-`, `AC-`, `EV-` oder `TRC-`Eintrag liest, schreibt oder berechnet, **ist selbst der Defekt**. `evidence_status` gilt dagegen projektweit.

Verbindliche Auswertungsregeln:

- `current_gate` wird **ausschließlich** gegen `blocked_gates` geprüft, `current_activity` **ausschließlich** gegen `blocked_activities`. **Gate-Bezeichnungen werden niemals mit Tätigkeitsbezeichnungen verglichen.**
- Bei `evidence_status` `planned` oder `pending` entsteht ein aktueller Blocker **nur**, wenn das gerade geprüfte Gate in `blocked_gates` oder die gerade geprüfte Tätigkeit in `blocked_activities` steht.
- Ist `current_gate` oder `current_activity` nicht gesetzt, entfällt **ausschließlich die zugehörige Klausel**; die übrigen bleiben in Kraft.
- Eine leere `blocked_gates`-Liste bedeutet „blockiert kein Gate", **nicht** „blockiert nie".
- Ein Gate-Bezeichner in `blocked_activities` (oder umgekehrt) ist ein **Validierungsfehler**, kein Toleranzfall.

Wer gegen ein anderes Gate prüft, leitet neu ab und übernimmt den Tabellenwert nicht.

| ID | `status` | `resolution_status` | `evidence_status` | `blocking` (abgeleitet) | `blocked_gates` | `blocked_activities` | `evidence_gate` | `decision_reference` |
|---|---|---|---|---|---|---|---|---|
| CONTRA-004 | `resolved` | `accepted` | `pending` | **`true`** | `[C, D]` | `[competition-release, territory-release]` | **C** | DEC-011 |
| CONTRA-005 | `resolved` | `accepted` | `pending` | **`true`** | `[B]` | `[database-schema-finalization, account-release]` | **B** | DEC-012 |
| CONTRA-006 | `resolved` | `accepted` | `pending` | **`true`** | `[A0]` | `[field-test, release]` | **A0** | OQ-011, DEC-013, **ADR zum A0-Routing-Proxy = MISSING** |

**Nachrechnung — die `blocking`-Werte sind erstmals gerechnet, nicht gesetzt** (ausgewertet am jeweils eigenen `evidence_gate`, ohne laufende Tätigkeit):

| ID | `status NOT IN [resolved]` | `resolution_status NOT IN [accepted]` | `evidence_status IN [failed, blocked]` | `current_gate IN blocked_gates` | Ergebnis |
|---|---|---|---|---|---|
| CONTRA-004 | false | false | false | `C ∈ [C, D]` → **true** | **`true`** |
| CONTRA-005 | false | false | false | `B ∈ [B]` → **true** | **`true`** |
| CONTRA-006 | false | false | false | `A0 ∈ [A0]` → **true** | **`true`** |

Unter der alten Formel hätten alle drei am eigenen Gate `false` ergeben, weil `C`, `B` und `A0` in keiner Tätigkeitsliste vorkommen können.

`rationale` je Eintrag:

- **CONTRA-004** — Die Kollision zwischen serverseitiger Anti-Cheat-Plausibilität und der Datenminimierung aus REQ-034 ist durch DEC-011 entschieden: nur minimierte, abgeleitete Plausibilitätssignale verlassen das Gerät. Der Nachweis, dass der Server tatsächlich **nur** diese Signale empfängt und dass fehlende Sensoren nie automatisch zu `rejected` führen, setzt laufenden Code und Betrugsfixtures voraus — **es existiert kein Code**.
- **CONTRA-005** — Die Kollision zwischen „unveränderlicher Historie" und dem Löschanspruch ist durch DEC-012 entschieden. Der Nachweis der technischen Trennung von Identität und historischen Aggregaten ist **vor** Finalisierung des Datenbankschemas fällig; ein Schema existiert nicht. Für diese Trennung ist am 2026-07-19 **EV-042** vergeben worden — zuvor hatte der Nachweis **keine EV-ID** und lief nur als Marke (z) im Evidence Ledger. Damit ist Registry §8 Punkt 14 **als ID-Frage** geschlossen; **der Nachweis selbst bleibt `blocked`**, weil die von DEC-012 geforderte Trennung ohne Retentionsfristen (OQ-009) nicht spezifizierbar ist.
- **CONTRA-006** — Die Kollision zwischen Local-first und serverseitigem Routing ist durch die Entscheidung für einen transienten, datenminimierten EU-Routing-Proxy **gelöst**; der Nachweis der Privacy-, Logging-, Retention- und Security-Eigenschaften steht aus.

> **MISSING — `decision_reference` von CONTRA-006 unvollständig.** Als Entscheidungsbeleg ist neben OQ-011 ein „ADR zum A0-Routing-Proxy" vorgesehen. Ein solches Dokument existiert im Repository **nicht** (`find docs -iname "*adr*"` am 2026-07-19: kein Treffer). Die Referenz wird als **MISSING** geführt und **nicht** stillschweigend durch DEC-013 ersetzt — DEC-013 ist die Privacy-Baseline, nicht der Architekturentscheid über den Proxy als solchen. Das Anlegen des ADR liegt beim Architektur-Owner; dieses PRD legt es nicht an.

> ~~**OPEN QUESTION — Wertebereich von `blocking_scope`.**~~ **GESCHLOSSEN am 2026-07-19 (Nutzerentscheidung C16, Registry §8 Punkt 16).** Die vier Werte `competition-release`, `territory-release`, `database-schema-finalization` und `account-release` lagen außerhalb der damaligen Basis-Liste. Der Konflikt ist nicht durch Streichen der Werte gelöst, sondern durch **Aufteilung des Feldes**: alle vier sind jetzt reguläre Elemente des abgeschlossenen `blocked_activities`-Vokabulars, und Gates haben mit `blocked_gates` ein eigenes, disjunktes Feld. Siehe Abschnitt „Feldwechsel" oben.

> ⚠️ **BLOCKER, terminiert — der Feldwechsel ist außerhalb dieses PRD noch nicht nachgezogen.** `blocking_scope` lebt am 2026-07-19 in weiteren Dateien fort: `docs/traceability.md` (20 Vorkommen), `docs/decisions/decision-log.md` (9), `docs/validation/validation-report.md` (7), `docs/EVIDENCE-LEDGER.md` (1), `docs/vision/revyr-endurance-platform.vision.md` (1). Diese Dateien liegen außerhalb der Dateihoheit dieses PRD und wurden hier **nicht** geändert. **Ein reines Umbenennen des Feldes behebt den Defekt nicht:** solange ein Werkzeug die alte Formel anwendet, liefert es für gegatete Einträge weiterhin fälschlich `false`.

> ⚠️ **MISSING — es existiert keine gemeinsame Implementierung der Blocking-Funktion.** Die Vorgabe verlangt, dass **alle** Validatoren dieselbe Implementierung importieren. Im Repository existiert derzeit **überhaupt kein ausführbares Prüfwerkzeug** (`docs/ID-REGISTRY.md` §9). Die Formel oben ist die normative Spezifikation für jede spätere Implementierung; dieses PRD schreibt **keinen Code**.

### CONTRA-004 — Anti-Cheat gegen Datenminimierung

`status: resolved` · `resolution_status: accepted` · `evidence_status: pending` · `blocking: true` (abgeleitet) · `blocked_gates: [C, D]` · `blocked_activities: [competition-release, territory-release]` · `evidence_gate: C` · `decision_reference: DEC-011`

Rohsensorverläufe bleiben standardmäßig lokal auf dem Gerät. Serverseitig zulässig sind ausschließlich minimierte, abgeleitete Plausibilitätssignale: Kadenzmittel und -band, Geschwindigkeitsband, optionales HF-Band (sofern vorhanden und freigegeben), GPS-Qualitätswert, Accuracy-Zusammenfassung, Teleport-Indikatoren, Bewegungsplausibilität, Distanz, Dauer, Sportart, Verifikations-Confidence. Nicht standardmäßig serverseitig: vollständige HF-Verläufe, vollständige Schrittverläufe, vollständige Rohsensorserien, unnötige Health-Rohdaten, zusätzliche personenbezogene Daten. Statuswerte: `verified-high`, `verified-standard`, `low-confidence`, `review-required`, `rejected`. Fehlende Sensoren allein sind kein Betrug — sie dürfen die Beweiskraft senken, aber nicht automatisch zu `rejected` führen. Eindeutige Teleports, physikalisch unmögliche Geschwindigkeiten oder klar widersprüchliche Sensordaten dürfen zu `review-required` oder `rejected` führen. Weitergehende Rohdatenverarbeitung nur nach ausdrücklichem Opt-in oder für eine konkrete, zeitlich begrenzte Einspruchs-/Betrugsprüfung mit dokumentiertem Zweck und definierter Löschung.

**Weiterhin offen:** Die zulässige Falsch-Positiv-Rate je Confidence-Stufe ist in keinem Artefakt beziffert (MISSING, siehe Messmodell REQ-024). RISK-013 verlangt zusätzlich einen Einspruchs-/Appeal-Flow, den kein Requirement beschreibt — **BLOCKER**, kein Requirement-Text darf ihn stillschweigend voraussetzen.

### CONTRA-005 — Historie gegen Accountlöschung

`status: resolved` · `resolution_status: accepted` · `evidence_status: pending` · `blocking: true` (abgeleitet) · `blocked_gates: [B]` · `blocked_activities: [database-schema-finalization, account-release]` · `evidence_gate: B` · `decision_reference: DEC-012`

Die Accountlöschung entfernt sämtliche personenbezogenen Daten und Identitätszuordnungen (Aufzählung in REQ-017). Historische Team- und Season-Daten dürfen nur wirksam anonymisiert und nicht rückführbar erhalten bleiben; ist das nicht möglich, ist der Datensatz zu löschen. Die Formulierung „unveränderliche Historie" ist in diesem PRD **überall** ersetzt durch: *„Nach Finalisierung fachlich unveränderbar, außer aufgrund Löschung, Anonymisierung oder rechtlicher Korrektur."* Datenmodell und Event-Historie müssen Identität und historische Aggregate technisch trennen; diese Trennung ist vor Erstellung und Finalisierung des Datenbankschemas zu berücksichtigen.

**Weiterhin offen:** Die Retentionsfristen selbst sind MISSING (OQ-009). „Wirksam anonymisiert" ist im Repository nicht mit einem Prüfverfahren hinterlegt — ohne Verfahren ist die Bedingung nicht abschließend testbar (**MISSING**, vom DRI vor Gate B zu entscheiden).

### CONTRA-006 — Routing-Proxy gegen Local-first

`status: resolved` · `resolution_status: accepted` · `evidence_status: pending` · `blocking: true` (abgeleitet) · `blocked_gates: [A0]` · `blocked_activities: [field-test, release]` · `evidence_gate: A0` · `decision_reference: OQ-011, DEC-013, ADR zum A0-Routing-Proxy (**MISSING**)`

> **Interpretation der Blockade (verbindlich, Nutzerentscheidung 2026-07-19):** **Dokumentation und Implementierungsplanung dürfen fortgesetzt werden.** Blockiert bleiben bis zur Privacy-Evidence ausschließlich der **externe A0-Feldtest** und das **A0-Release** — deshalb `blocked_activities: [field-test, release]` und **nicht** `documentation` oder `planning`.

**Der frühere Zielkonflikt in der Auftragslage ist durch das getrennte Statusmodell aufgelöst — nicht durch eine Selbstbestätigung.** Die Nutzeranweisung verlangte an einer Stelle „CONTRA-006 = RESOLVED", an anderer Stelle, dass CONTRA-006 blockierend bleibt, bis Datenfluss, Providerbedingungen, Logging, Retention, Transparenz, Sicherheitskontrollen und die Evidence vollständig dokumentiert und geprüft sind. Beides ist gleichzeitig wahr, sobald die Achsen getrennt werden: die **Entscheidung** ist getroffen (`status: resolved`), der **Nachweis** steht aus (`evidence_status: pending`) und bleibt **blockierend** (`blocking: true`). Der frühere Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` ist als `status` unzulässig und wurde aufgeteilt.

Der wesentliche Teil dieser Evidence — Tests gegen Logs, Rate-Limit-Nachweis, Secret-Scan des Bundles — setzt lauffähigen Code voraus. **Es existiert kein Code.** Kein Nachweis wird hier als erbracht erklärt, und dieses PRD stellt sich kein Watcher-Verdikt aus.

Entschieden ist der Entwurf:

- **Zweckbindung und Persistenz.** Der Proxy verarbeitet Start-, Ziel- und Wegpunktkoordinaten ausschließlich transient zur angeforderten Routenberechnung. Keine anwendungsseitige Persistenz von Koordinaten, berechneter Route oder vollständigen Request-/Response-Bodies. Keine Werbung, Profilbildung, Produktanalyse, Trainingsanalyse, Standortstatistik, Wiederverwendung, kein Modelltraining, kein Verkauf und keine Weitergabe. Retention für den Koordinaten-Payload: Application 0, Cache 0, Analytics 0.
- **Client-Payload.** Der Client sendet nur: `sport` (`run`|`ride`), die erforderlichen Koordinaten, notwendige Routingparameter und eine technisch erforderliche Request-ID. Nicht: Benutzername, E-Mail, Account-ID, Health-Daten, Aktivitätsverlauf, vollständiger GPS-Track, Team-/Profildaten, Gerätekennungen (sofern nicht zwingend).
- **Logging.** Request- und Response-Bodies dürfen nicht geloggt werden. Nicht in Logs, Traces oder Fehlermeldungen: Latitude, Longitude, Wegpunktlisten, vollständige Provider-URLs mit Koordinaten, Routengeometrien, Start-/Zieladressen. Zulässig: zufällige Request-ID, Zeitstempel, HTTP-Status, Verarbeitungsdauer, Routingprofil, Anzahl Wegpunkte, normalisierte Fehlerkategorie, Provider-Latenz, Rate-Limit-Ereignis. Technische Logs dürfen keine Standortrekonstruktion ermöglichen. Aufbewahrung technischer Logs: maximal 7 Tage, sofern keine nachgewiesene technische oder gesetzliche Notwendigkeit für eine andere Frist besteht; eine Änderung braucht eine dokumentierte Entscheidung.
- **Transport und Secrets.** Nur HTTPS/TLS, keine unverschlüsselten Endpunkte. Provider-Key ausschließlich serverseitig, keine Secrets in App, Repository oder Logs; Secrets über AWS Secrets Manager oder verschlüsselte Lambda-Env, restriktive IAM, Rotation und Widerruf möglich.
- **Missbrauchsschutz.** Rate Limit, Size-Limit, maximale Wegpunktzahl, Timeout, Kill Switch, Koordinatenvalidierung und normalisierte Fehler dürfen **nicht** zu dauerhafter Koordinatenspeicherung führen. IP-Adressen nur soweit technisch erforderlich, keine dauerhafte Speicherung und keine Verknüpfung mit Routenanfragen; separat zu dokumentieren.
- **Fehlerbehandlung.** Providerfehler gelangen nie ungefiltert an den Client. Die Fehlerantwort enthält nur internen Fehlercode, nutzergeeignete Nachricht, Request-ID und gegebenenfalls einen Retry-Hinweis — keine Provider-Secrets, internen URLs, Koordinaten, vollständigen Providerantworten oder Stack Traces.

Ausstehende Nachweise (jeder einzelne blockierend für die A0-Routing-Implementierung):

| # | Ausstehender Nachweis | Art | Fällig |
|---|---|---|---|
| 1 | Verarbeitungsregion des Routinganbieters, ob Daten den EWR verlassen, Unterauftragsverarbeiter, Transfergrundlage | **MISSING** | vor erstem externem Feldtest |
| 2 | Rollenverteilung Controller/Processor, Auftragsverarbeitungsvertrag, Provider-Retention, Ausschluss eigener Werbe-/Profiling-/Trainingszwecke, Lösch- und Sicherheitsregeln | **MISSING** | vor erstem externem Feldtest |
| 3 | Rechtsgrundlage und Transparenz: Verantwortlicher, Zweck, Rechtsgrundlage, Empfänger/Auftragsverarbeiter, Übermittlungsregionen, Speicherdauer, Betroffenenrechte, Datenschutzkontakt | **MISSING** | vor erstem externem Feldtest |
| 4 | Datenschutzerklärungstext vor Nutzung der Routenplanung (Wortlaut siehe unten) | **MISSING** | vor erstem externem Feldtest |
| 5 | Testnachweis, dass keine Koordinaten in Logs, Traces oder Fehlermeldungen erscheinen | `evidence_status: pending` (setzt lauffähigen Code voraus, in diesem Lauf verboten) | vor A0-Freigabe |
| 6 | Nachweis von Rate Limit, Size-Limit, Timeout und Kill Switch | `evidence_status: pending` (setzt lauffähigen Code voraus); die **Zahlenwerte** selbst sind **MISSING** — DEC-013 fordert sie, beziffert keine | vor A0-Freigabe |
| 7 | Secret-Scan des App-Bundles ohne Routing-Provider-Key | `evidence_status: pending` (setzt Build voraus) | vor A0-Freigabe |
| 8 | Benannte Betriebsverantwortung für den Proxy, der ab A0 personenbezogene Wegpunkte verarbeitet | **BLOCKER** (OQ-002 offen) | vor A0-Routing-Implementierung |

Verbindlicher Nutzerhinweistext, den die Datenschutzerklärung vor Nutzung der Routenplanung verständlich erklären muss:

> Zur Berechnung deiner Route werden die ausgewählten Start-, Ziel- und Wegpunkte kurzfristig an unseren EU-Routing-Proxy und den eingesetzten Routinganbieter übermittelt. Die App speichert diese Koordinaten im Proxy nicht dauerhaft.

Die Bezeichnung „EU-Proxy" darf **nicht** den Eindruck erwecken, die gesamte Verarbeitung liege in der EU, wenn der nachgelagerte Anbieter außerhalb verarbeitet. Ein Anbieter, der die Punkte 1–2 nicht erfüllt, darf nicht für produktive oder externe A0-Tests eingesetzt werden.

## Evidence Needed

| Evidence ID | Requirement ID | Evidence Needed | Source Type |
|---|---|---|---|
| EV-001 | REQ-001 | Konfigurations-Unit-Tests und Screen-Checkliste für iOS/Android. | EXPLICIT |
| EV-002 | REQ-002 | Gerätetest je Sport und Plattform auf Referenzstrecke. | EXPLICIT |
| EV-003 | REQ-003 | 30-Minuten-Kill-/Background-Test je Plattform und Sport. | EXPLICIT |
| EV-004 | REQ-004 | Drift-, Tunnel-, Sprung- und Hochgeschwindigkeits-Fixtures. | ASSUMPTION |
| EV-005 | REQ-005 | SQLite-Repository-Tests, Kill-Test und Migrations-Fixtures. | ASSUMPTION |
| EV-006 | REQ-006 | Routing-Service-Tests und zehn reale Routenszenarien je Sport. | EXPLICIT |
| EV-007 | REQ-007 | Polyline-Projektions-Fixtures und reale Abweichungstests. | ASSUMPTION |
| EV-008 | REQ-008 | Repository- und UI-Test für Verlauf und Detailansicht, **je Sportart getrennt** (Run zeigt Pace, Bike zeigt Geschwindigkeit); Neustart-Test auf Persistenz; Negativtest auf beschädigte oder unbekannte Aktivitätsdaten. **Kanonische Trennung (verbindlich, 2026-07-20): EV-008 ist AUSSCHLIESSLICH Evidence für Verlauf und Detailansicht** — es enthält **keinen** GPX-, Export-, Portabilitäts- oder Fremd-App-Nachweis. Der GPX-Kompatibilitätstest ist am 2026-07-19 nach **EV-039** ausgelagert. **Wer einen GPX-Nachweis unter EV-008 findet, hat einen Validierungsfehler gefunden.** | ASSUMPTION |
| EV-009 | REQ-009 | Echte Geräte und BLE-Gurt je Plattform. | EXPLICIT |
| EV-010 | REQ-010 | Formeltests mit/ohne HF und UI-Test des Warum-Sheets. | ASSUMPTION |
| EV-011 | REQ-011 | Zonen-Unit-Tests und Kopfhörer-Gerätetest. | EXPLICIT |
| EV-012 | REQ-012 | Zeitmessung, Fixture-Korrelation und Copy-Review. | EXPLICIT |
| EV-013 | REQ-013 | Wochen-Fixtures und Claims-Lint. | EXPLICIT |
| ~~EV-014~~ | ~~REQ-014~~ | **DEPRECATED 2026-07-19 → EV-037 + EV-038.** Der Alttext belegt die Composite-Natur wörtlich: „**Token**-Review" ist der Designsystem-Nachweis (→ EV-038), „**Accessibility- und Screenreader-Check**" der Zugänglichkeitsnachweis (→ EV-037). Zwei Verfahren, eine ID. | — |
| EV-015 | REQ-015 | Idempotenz- und Unlock-Fixtures. | EXPLICIT |
| EV-016 | REQ-016 | Bildexport-, Widget- und Privacy-Snapshot-Test. | EXPLICIT |
| EV-017 | REQ-017 | E2E-Flow, Offline-Test und Löschungsnachweis, einschließlich Nachweis der technischen Trennung von Identität und historischen Aggregaten sowie eines Anonymisierungsnachweises für überlebende Historieneinträge. | EXPLICIT |
| EV-018 | REQ-018 | Sichtbarkeits-Matrix, Zwei-Account- und Moderationstest. | EXPLICIT |
| EV-019 | REQ-019 | Zwei-Account-E2E-Flow. | EXPLICIT |
| EV-020 | REQ-020 | Datenbanktransaktions- und Zwei-Geräte-Test. | EXPLICIT |
| EV-021 | REQ-021 | Zeitfenster- und Integrations-Fixtures. | EXPLICIT |
| EV-022 | REQ-022 | Pure-Function-Fixtures und Zwei-Geräte-Eventtest. | EXPLICIT |
| EV-023 | REQ-023 | Monte-Carlo-/Szenariosimulation und Kalibrierungsbericht. | EXPLICIT |
| EV-024 | REQ-024 | Betrugs-/Grenzfall-Fixtures, False-Positive-Review und Nachweis des minimierten Signalumfangs: der serverseitig empfangene Payload enthält keine Rohsensorserien und keine vollständigen HF-/Schrittverläufe. | ASSUMPTION |
| EV-025 | REQ-025 | Deterministische Fixtures und Wiederholungs-Test. | EXPLICIT |
| EV-026 | REQ-026 | Geo-Fixtures, Simulation und Karten-Lasttest. | EXPLICIT |
| EV-027 | REQ-027 | Zwei-Season-Integrationstest, Prüfung der fachlichen Unveränderbarkeit nach Finalisierung sowie Nachweis, dass Löschung und Anonymisierung als zulässige Ausnahmen korrekt greifen (Löschung eines Mitglieds mit historischen Capture-Ereignissen). | EXPLICIT |
| EV-028 | REQ-028 | Geo-Fixture-Suite, Property-Tests und Threat-Model. | ASSUMPTION |
| EV-029 | REQ-029 | OSM-Access-Review, realer Bahn-Test und Reward-Fixtures. | ASSUMPTION |
| EV-030 | REQ-030 | Threat-Model, Endpfad-Matrix und Penetrationstest. | EXPLICIT |
| EV-031 | REQ-031 | Kontrollierte Falltests, Fehlalarmstatistik und Claims-Review. | EXPLICIT |
| EV-032 | REQ-032 | Gerätematrix und reale Integrationstests. | EXPLICIT |
| EV-033 | REQ-033 | Claims-Lint, Rechtsfreigabe und Privacy-Test. | EXPLICIT |
| EV-034 | REQ-034 | Security-Review, RLS-Tests, Datenflussdiagramm und Löschungsnachweis. | EXPLICIT |
| EV-035 | REQ-035 | CI-Regel, Ledger-Review und Gate-Checkliste. | EXPLICIT |
| EV-036 | REQ-036 | TestFlight/Internal-Test-Bericht, Policy-Matrix und Gate-Sign-off. | EXPLICIT |
| **EV-037** | **REQ-037** | WCAG-2.2-AA-Audit; **VoiceOver- und TalkBack-Durchlauf je Plattform**; Dynamic-Type-/Font-Scaling-Prüfung; dokumentierte Kontrastprüfung in Light und Dark Mode. | ASSUMPTION |
| **EV-038** | **REQ-038** | Design-Token-Review: Inventar **aller** Farbwerte gegen die vier zulässigen fachlichen Bedeutungen; Prüfung, dass Run und Bike nicht ausschließlich farblich unterschieden werden; Prüfung auf Farb-Literale außerhalb der Tokens. | EXPLICIT |
| **EV-039** | **REQ-039** | GPX-Export-Test **je Sportart getrennt**: Erzeugung, Schemakonformität, Zeitstempel- und Koordinatenreihenfolge, Öffnen in einer definierten Fremd-App, **Negativtest auf Health-Daten im Export**, kontrollierter Fehlerfall bei beschädigten Trackdaten, Export ohne Veröffentlichung. **Kanonische Trennung (verbindlich, 2026-07-20): EV-039 ist AUSSCHLIESSLICH der GPX-Kompatibilitäts- und Exportnachweis** — Verlauf und Detailansicht werden hier **nicht** nachgewiesen (das ist EV-008). | ASSUMPTION |
| ~~EV-040~~ | ~~REQ-040~~ | **DEPRECATED 2026-07-20 → EV-043 + EV-044.** Der Alttext belegt die Composite-Natur: „erneuter Start einer gespeicherten Strecke" ist der **Wiederverwendungs**nachweis (→ EV-043), „Gegenüberstellung … Negativtests" der **Vergleichs**nachweis (→ EV-044). Zwei Nachweise mit **unterschiedlichem Blockierungszustand** in einer ID. | — |
| **EV-043** | **REQ-041** (zu AC-042) | Wiederverwendungstest **je Sportart getrennt**: Auswahl und Start einer gespeicherten Route; Abgleich von **Geometrie und Wegpunkten** gegen die gespeicherte Fassung; Erhalt des **sportartspezifischen Routingprofils**; kontrollierter Fehlerfall bei gelöschter oder beschädigter Route. **Nicht von OQ-015 blockiert.** | ASSUMPTION |
| **EV-044** | **REQ-042** (zu AC-043) | Vergleichstest **je Sportart getrennt**: Gegenüberstellung zweier als fachlich vergleichbar erkannter Aktivitäten anhand sportartspezifischer Kennzahlen; Negativtests gegen verkürzte, verlängerte, abgebrochene und geometrisch abweichende Aktivitäten; **Negativtest gegen sportübergreifenden Vergleich**. | ASSUMPTION |
| **EV-041** | **REQ-019** (zu AC-041) | Reproduzierbare, datenschutzkonforme Berechnung der Kennzahl „bestätigte Routenübernahmen je auswertbarer Empfehlung", **getrennt für Run und Bike**, über ein rollierendes 28-Tage-Fenster. Belegt die **Berechenbarkeit**, nicht die Zielerreichung. | MISSING (OQ-012, OQ-014) |
| **EV-042** | **REQ-017 / REQ-027** (zu CONTRA-005) | Nachweis, dass das **Datenmodell Identität und historische Aggregate technisch trennt** (DEC-012, Marke (z) in `docs/EVIDENCE-LEDGER.md`). | EXPLICIT (DEC-012) |

### Evidence-Status der neuen Nachweise

**Projektweite Semantik (Nutzerentscheidung 2026-07-19)** — die Grenze zwischen `planned` und `pending` ist die **Instrumentierung**, nicht die Absicht. Solange kein Code existiert, kann nichts instrumentiert sein; ein Eintrag ohne Code steht **höchstens** auf `planned`.

| Wert | Bedeutung |
|---|---|
| `not-planned` | Es existiert noch **kein Messkonzept**. |
| `planned` | Metrik, Berechnung und zuständiges Gate sind **definiert**, die Instrumentierung fehlt. |
| `pending` | Instrumentierung **implementiert**, aber Messdaten oder Messfenster fehlen noch. |
| `verified` | Zielwert mit ausreichender, dokumentierter Evidenz geprüft. |

| EV | `evidence_status` | Begründung |
|---|---|---|
| EV-037 | **`not-planned`** | Kein Code, keine CI, kein beauftragter Auditor — es existiert kein Messkonzept. **OWNER-BLOCKER** (OQ-002), **Referenzumgebung MISSING** (OQ-003). |
| EV-038 | **`not-planned`** | Kein Code, keine Token-Datei, kein festgelegtes Prüfverfahren. **OWNER-BLOCKER** (OQ-002). |
| EV-039 | **`not-planned`** | **MISSING:** die „definierte Fremd-App" ist nicht benannt (OQ-016) — ohne sie ist AC-039 Kriterium (d) nicht reproduzierbar prüfbar. **Es wird keine App geraten.** |
| **EV-043** | **`not-planned`** | Kein Code und kein Messkonzept — `pending` wäre eine behauptete Instrumentierung. **Ausdrücklich NICHT von OQ-015 blockiert:** alle fünf Bedingungen aus AC-042 sind heute spezifizierbar. **OWNER-BLOCKER** (OQ-002). |
| **EV-044** | **`not-planned`** | **BLOCKER:** ohne die Vergleichs- und Streckenähnlichkeitsdefinition aus **OQ-015** ist kein Testfall **bezifferbar**. Die Negativtests sind benannt, aber ohne Toleranzwert nicht ausführbar. **Es wird keine Toleranz geraten.** **OWNER-BLOCKER** (OQ-002). |
| EV-041 | **`planned`** | Metrik, Berechnung und Gate (B) sind in CAN-130 vollständig **definiert**; allein die Instrumentierung fehlt. Abhängig von OQ-012 und OQ-014. `empirical_result` bleibt **MISSING**. |
| EV-042 | **`blocked`** | Die von DEC-012 **vor** der Schema-Finalisierung geforderte Trennung ist ohne Retentionsfristen (OQ-009) nicht spezifizierbar. Nicht `pending`: das Hindernis ist **kein fehlender Code**, es bliebe auch mit fertigem Code bestehen. |

**`evidence_status = verified` bei keinem einzigen Nachweis.** Der Nenner ist abgeleitet, nicht festgeschrieben: `aktiv(EV)` = **42** (Stand 2026-07-20, Ableitungsweg im Kopf dieses Dokuments). Es existiert kein Code, kein Build, kein Gerätetest und keine CI. Kein Nachweis wird hier als erbracht erklärt.

## Messmodell je Requirement

Jedes **aktive** Requirement (`aktiv(REQ)`, Stand 2026-07-20 aus der Registry abgeleitet: **40**) trägt genau neun Messfelder: `measurement_type`, `signal`, `target_or_pass_condition`, `measurement_window`, `evidence_source`, `source_type`, `owner`, `release_gate`, `rationale`. Requirements vom Typ `RESEARCH_HYPOTHESIS` tragen zusätzlich einen `research_plan` (Hypothese, Plan, Fixtures/reale Testdaten, Entscheidungsschwelle, Konsequenz bei unzureichender Evidenz). Wo ein REQ keinen tragfähigen atomaren Canvas-Anker hat, steht ein `Canvas-BLOCKER`.

**Typen.** `PRODUCT_OUTCOME` = am Nutzer-/Produktwert messbar. `OPERATIONAL_QUALITY` = technische Zuverlässigkeit und Datenqualität; keine künstlichen Engagement-KPIs. `COMPLIANCE_CONTROL` = kontrollierter Nachweis, Pass/Fail beziehungsweise 100-%-Abdeckung; diese REQs brauchen bewusst **kein** Nutzersignal. `RESEARCH_HYPOTHESIS` = noch nicht validierte Systeme; kein produktiver Rollout vor bestandenem Gate, nicht validierte Startwerte bleiben ASSUMPTION.

| Typ | Anzahl | Requirements |
|---:|---:|---|
| OPERATIONAL_QUALITY | 16 | REQ-001…007, REQ-008, REQ-009, REQ-011, REQ-025, REQ-027, REQ-032, **REQ-039**, **REQ-041**, **REQ-042** |
| COMPLIANCE_CONTROL | 10 | REQ-015…018, REQ-030, REQ-034, REQ-035, REQ-036, **REQ-037**, **REQ-038** |
| RESEARCH_HYPOTHESIS | 9 | REQ-012, REQ-021, REQ-023, REQ-024, REQ-026, REQ-028, REQ-029, REQ-031, REQ-033 |
| PRODUCT_OUTCOME | 5 | REQ-010, REQ-013, REQ-019, REQ-020, REQ-022 |
| **Summe** | **40** | stimmt mit `aktiv(REQ)` überein — Stand 2026-07-20, aus `docs/ID-REGISTRY.md` abgeleitet, nicht abgeschrieben |

**Änderung 2026-07-19:** REQ-014 ist aus der COMPLIANCE_CONTROL-Zeile entfernt (deprecated) und durch **REQ-037** und **REQ-038** ersetzt — beide bleiben COMPLIANCE_CONTROL, aber mit **getrennten Prüfverfahren**.

**Änderung 2026-07-20:** **REQ-040 ist aus der OPERATIONAL_QUALITY-Zeile entfernt** (deprecated) und durch **REQ-041** und **REQ-042** ersetzt. Beide bleiben OPERATIONAL_QUALITY, aber mit **getrennten Acceptance Criteria und getrenntem Blockierungszustand**: REQ-041 ist heute vollständig spezifizierbar, REQ-042 nicht. Die Vergleichs**logik** von REQ-042 bleibt davon unberührt `RESEARCH_HYPOTHESIS` bzw. MISSING, solange **OQ-015** offen ist; das Requirement selbst misst Funktionsqualität, nicht eine Forschungsfrage. **REQ-041 erbt diese Einschränkung ausdrücklich nicht** — sie war der Grund, die Composite zu teilen statt sie zu verengen.

**Zwei Querschnittsbefunde, die kein Einzelfeld auflöst:**

1. **Messlücke Telemetrie — für ein Requirement adressiert, für die übrigen offen.** Kein Requirement, kein NFR und kein Canvas-Item beschrieb eine Analytics- oder Telemetrie-Erhebung. Damit sind die `PRODUCT_OUTCOME`-Signale plus die Check-in-Quote aus REQ-012 heute **nicht erhebbar**, und jede Erhebung kollidiert mit CAN-095 (local-first) und REQ-034 (Datensparsamkeit). **Teilweise adressiert seit 2026-07-19:** für **REQ-019** ist mit **CAN-130** eine privacy-minimierte Telemetrie inhaltlich spezifiziert (zulässige Ereignisse, zulässige und **unzulässige** Felder, kein paralleler Tracker) und die verbleibende Entscheidung als **OQ-012** geführt. Für **REQ-010, REQ-012, REQ-013, REQ-020 und REQ-022** bleibt die Messlücke **unverändert offen** — sie wird hier nicht durch eine Annahme geschlossen und **nicht** stillschweigend aus CAN-130 mitgelöst.
2. **Owner.** OQ-002 (finaler Repository-Owner/DRI) ist MISSING. **Jedes** aktive Requirement trägt deshalb einen sichtbaren **OWNER-BLOCKER**. Wo ein Register eine Rolle nennt, ist sie als Owner **der offenen Frage** gekennzeichnet, nie als REQ-Owner. Kein Name wurde erfunden, kein Feld leer gelassen.

**Zielwert = ASSUMPTION bei sechs Requirements** (REQ-010, REQ-012, REQ-013, REQ-019, REQ-020, REQ-022): alle stützen sich auf VIS-006-Zielwerte, die nirgends empirisch hinterlegt sind. **`source_type` = MISSING bei 13 Requirements** (REQ-007, REQ-016, REQ-017, REQ-021, REQ-023, REQ-024, REQ-026, REQ-027, REQ-028, REQ-029, REQ-031, REQ-032, REQ-033), weil die entscheidende quantitative Schwelle in keinem Artefakt existiert. In keinem Fall wurde ein plausibler Wert eingesetzt.

### Nachaudit der 17 `EXPLICIT`-Zeilen (2026-07-19)

Die verbleibenden **17** Requirements trugen `source_type = EXPLICIT`. Sie wurden einzeln gegen dieselbe Beweislatte geprüft, die für die NFRs gilt: **wo ein Zielwert keine belegte Quelle hat, ist EXPLICIT falsch.** Belegfähig sind nur `CONFIRMED`-Canvas-Items, `user-confirmed`-Entscheidungen (DEC-), `SRC-006` oder eine **konkret zitierte** verbindliche externe Regel.

Ergebnis: **1 von 17 hält** (REQ-034, klauselbeschränkt). **16 wurden auf `ASSUMPTION` herabgestuft.**

Die drei tragenden Gründe:

1. **Verkettung auf herabgestufte NFRs.** REQ-002, REQ-003, REQ-004, REQ-005 und das damalige REQ-014 (heute **REQ-037**) beziehen ihre Pass-Bedingung wörtlich aus NFR-001, NFR-002, NFR-003 bzw. NFR-005. Diese vier NFRs sind im NFR-Audit auf `ASSUMPTION` herabgestuft worden. Ein abgeleiteter Wert kann nicht stärker belegt sein als seine Quelle. **REQ-038 fällt ausdrücklich nicht unter diesen Grund** — es hängt an CAN-141, nicht an NFR-005.
2. **Analytische Nullschwelle ≠ belegte Herkunft.** Bei REQ-001, REQ-008, REQ-009, REQ-011, REQ-015, REQ-018, REQ-025, REQ-030, REQ-035 und REQ-036 ist die Pass-Bedingung eine 0-/100-%-Schranke, die logisch aus dem Requirement folgt und deshalb **keine gewählte Zahl** ist. Belegbedürftig **und unbelegt** bleibt die **Anforderung selbst**: sie trug `EXPLICIT` ohne SRC-Angabe oder stützte sich auf SRC-001/SRC-003, die laut `docs/SOURCE-MAP.md` **nicht auffindbar** sind. Dieselbe Logik wie bei NFR-003.
3. **Genannt ≠ zitiert.** REQ-036 beruft sich auf Store-Policies. Plattformvorgaben **wären** eine zulässige EXPLICIT-Quelle — aber nur, wenn sie **konkret zitiert** werden. Weder Policy-Klausel noch Fassung noch Datum sind benannt. Dieselbe Lücke wie bei „WCAG AA" in NFR-005.

⚠️ **Was hier ausdrücklich nicht passiert ist:** Keine Zeile wurde auf `MISSING` oder `BLOCKER` **hoch**gestuft, um Strenge zu demonstrieren, und keine auf `EXPLICIT` belassen, um die Statistik zu schonen. Wo die Pass-Bedingung als vorläufige Prüfbedingung tatsächlich taugt, steht `ASSUMPTION` — das ist die ehrliche Einstufung, nicht die bequeme.

| REQ | `source_type` neu | Grund |
|---|---|---|
| REQ-001 | ASSUMPTION | (2) analytische Nullschwelle, Anforderung ohne belegte Quelle |
| REQ-002 | ASSUMPTION | (1) Pass-Bedingung **ist** NFR-001 (< 3 %) → ASSUMPTION |
| REQ-003 | ASSUMPTION | (1) NFR-003 + NFR-002; die Zelle bezeichnet den Batteriewert **selbst** als „nicht empirisch belegt" |
| REQ-004 | ASSUMPTION | (1) zahlt auf NFR-001 ein; das PRD führt REQ-004 selbst als ASSUMPTION (SRC-005) |
| REQ-005 | ASSUMPTION | (1) Pass-Bedingung **ist** NFR-003 |
| REQ-006 | ASSUMPTION | (2) „zehn reale Szenarien" ist eine **gewählte, unbelegte Zahl**; die Klausel „0 Routing-Provider-Keys" ist EXPLICIT (DEC-005/CAN-092/SRC-006), aber eine **aus NFR-007 entliehene Zusatzkontrolle**, nicht REQ-006s eigener Zielwert |
| REQ-008 | ASSUMPTION | (2) |
| REQ-009 | ASSUMPTION | (2) |
| REQ-011 | ASSUMPTION | (2) |
| ~~REQ-014~~ | ASSUMPTION | (1) Pass-Bedingung **ist** NFR-005; WCAG-Fassung fehlt. **Zeile historisch — REQ-014 ist am 2026-07-19 deprecated.** Der Befund vererbt sich **nicht pauschal**: **REQ-037** übernimmt ihn (`ASSUMPTION`, weil die Rechtsgrundlage weiterhin fehlt — die WCAG-Fassung ist inzwischen mit 2.2 beziffert), **REQ-038** übernimmt ihn **nicht** und trägt `EXPLICIT` über CAN-141, weil das Designprinzip eine ausdrückliche Nutzerangabe ist und nicht an NFR-005 hängt. |
| REQ-015 | ASSUMPTION | (2) Anker CAN-075 trägt `EXPLICIT` via **SRC-001 = nicht auffindbar** |
| REQ-018 | ASSUMPTION | (2) „Profile standardmäßig privat" stammt aus VIS-009, Quelle SRC-001 = nicht auffindbar |
| REQ-025 | ASSUMPTION | (2) |
| REQ-030 | ASSUMPTION | (2); Freigabedauer und Verschleierungsradius bleiben MISSING |
| REQ-034 | **EXPLICIT** (klauselbeschränkt) | **hält** — Kern-Pass-Bedingung durch DEC-005, DEC-011 und DEC-013 gedeckt |
| REQ-035 | ASSUMPTION | (2) Anker CAN-114/CAN-123 tragen `EXPLICIT` via **SRC-003 = nicht auffindbar** |
| REQ-036 | ASSUMPTION | (3) Store-Policies genannt, aber nicht konkret zitiert |

Verteilung nach dem Nachaudit, historischer Stand **2026-07-18** (vor dem Auftau-Schritt 2): `EXPLICIT` **1** · `ASSUMPTION` **22** · `MISSING` **13** · Summe **36**.

**Fortschreibung, abgeleitet — nicht abgeschrieben.** Jede Zeile ist ein Vorgang, keine gesetzte Zahl; die Endzeile wird gegen `aktiv(REQ)` geprüft, nicht gegen ein Literal:

| Vorgang | Datum | `EXPLICIT` | `ASSUMPTION` | `MISSING` | Summe |
|---|---|---:|---:|---:|---:|
| Stand vor Auftau-Schritt 2 | 2026-07-18 | 1 | 22 | 13 | 36 |
| − REQ-014 (deprecated) | 2026-07-19 | 1 | 21 | 13 | 35 |
| + REQ-037 (`ASSUMPTION`) | 2026-07-19 | 1 | 22 | 13 | 36 |
| + REQ-038 (`EXPLICIT`, CAN-141) | 2026-07-19 | 2 | 22 | 13 | 37 |
| + REQ-039 (`ASSUMPTION`) | 2026-07-19 | 2 | 23 | 13 | 38 |
| + REQ-040 (`ASSUMPTION`) | 2026-07-19 | 2 | 24 | 13 | 39 |
| − REQ-040 (deprecated) | **2026-07-20** | 2 | 23 | 13 | 38 |
| + REQ-041 (`ASSUMPTION`) | **2026-07-20** | 2 | 24 | 13 | 39 |
| + REQ-042 (`ASSUMPTION`) | **2026-07-20** | **2** | **25** | **13** | **40** |

Die Endsumme stimmt mit `aktiv(REQ)` überein (Stand 2026-07-20, aus `docs/ID-REGISTRY.md` abgeleitet). **REQ-008** wechselt dabei von `EXPLICIT` auf `ASSUMPTION` — bereits im Nachaudit vom 2026-07-18 vollzogen (Grund 2), durch die Verengung inhaltlich bestätigt, ohne die Zählung erneut zu verändern. **Die Teilung von REQ-040 verschiebt keine Einstufung:** beide Nachfolger erben `ASSUMPTION` aus demselben Grund (Wortlaut aus der Nutzerentscheidung, nicht als Anforderungstext bestätigt) — es wurde **nichts hoch- und nichts herabgestuft**, um die Verteilung zu glätten.

⚠️ **REQ-038 ist die zweite `EXPLICIT`-Zeile und keine Hochstufung zur Statistikpflege.** Sie hält die Beweislatte, weil CAN-141 `source_type EXPLICIT` trägt: das monochrome Designsystem mit den vier zulässigen Farbbedeutungen ist eine **ausdrückliche Nutzerangabe vom 2026-07-19**, kein aus einem nicht auffindbaren SRC abgeleiteter Wert. **Nicht mit hochgezogen:** REQ-037, obwohl es aus derselben Nutzerentscheidung stammt — dort fehlt weiterhin die zitierte Rechtsgrundlage für die Verbindlichkeit von WCAG 2.2 AA.

### REQ-001 — Sportmodus als zentrale Konfiguration

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Konsistenzrate der sportabhängigen Konfiguration: Anteil der Screens, Metriken, Schwellen und Routingprofile, die beim Wechsel Run ↔ Bike vollständig auf das jeweilige SportConfig-Objekt umschalten (Run zeigt Pace, Bike zeigt Geschwindigkeit). Run und Bike werden getrennt durchlaufen. Zusätzlich statisch: Anzahl sportabhängiger Konstanten außerhalb der Konfigurationsobjekte. |
| target_or_pass_condition | AC-001 als Pass/Fail mit 100-%-Abdeckung: alle sportabhängigen Metriken, Schwellen, Labels und Routingprofile wechseln konsistent; 0 sportspezifische Werte hart codiert in Screens. Kein Nutzungs- oder Engagement-Zielwert — REQ-001 ist eine Architektur- und Korrektheitsschranke, kein Nutzerverhalten. |
| measurement_window | Je Gate-A0-Abnahme und bei jeder Versionsänderung eines SportConfig-Objekts; Screen-Checkliste einmal je Plattform (iOS, Android) und je Sportart. |
| evidence_source | EV-001 (Konfigurations-Unit-Tests und Screen-Checkliste für iOS/Android); Mindestklasse laut `docs/traceability.md`: `real-boundary-smoke`, weil die Sportumschaltung eine UI-Eigenschaft auf realen Geräten ist. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — die Pass-Bedingung ist eine analytische 0-/100-%-Schranke aus AC-001 und damit keine gewählte Zahl; belegbedürftig und **unbelegt** bleibt die Anforderung selbst. Anker CAN-047/CAN-028/CAN-013 tragen `EXPLICIT` über SRC-001/SRC-003, die laut `docs/SOURCE-MAP.md` **nicht auffindbar** sind. |
| owner | **OWNER-BLOCKER (MISSING)** — kein benannter DRI; OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. Default bei Nichtauflösung laut `docs/decisions/open-questions.md`: „Umsetzung bleibt organisatorisch unzugeordnet". Rollenreferenz „Engineering/QA" gehört zur gekoppelten Frage OQ-003, nicht zu diesem REQ. |
| release_gate | GATE-A0 |
| rationale | Der Erfolg ist an keiner Nutzerreaktion ablesbar, sondern an der technischen Konsistenz zwischen Sportmodus und Ausgabe; ein Engagement-KPI wäre ein Kategorienfehler. Run/Bike-Trennung ist zwingend, weil genau die Verwechslung der sportspezifischen Kernmetrik (RISK-005: „Bike zeigt falsche Laufmetriken") der Fehlerfall ist, den das REQ verhindern soll. |

Canvas: CAN-047, CAN-028, CAN-013 · Vision: VIS-008

### REQ-002 — Foreground-Tracking

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Getrennt für Run und Bike und je Plattform: Distanzabweichung gegen die Referenzstrecke nach Filter, GPS-Punktqualität (Anteil Punkte oberhalb der Genauigkeitsschwelle), Aktualisierungslücken von Live-Metrik und Live-Karte, Anteil gestarteter Aktivitäten, die technisch abbrechen statt vom Nutzer beendet zu werden. |
| target_or_pass_condition | NFR-001: < 3 % Distanzabweichung auf definierter Referenzstrecke nach Filter, getrennt nachgewiesen für Run und Bike und je Plattform. AC-002 als Pass/Fail: Route und Live-Metriken aktualisieren fortlaufend, die Aktivität ist kontrolliert beendbar. Für die Rate technisch abgebrochener Sessions nennt kein Artefakt einen Zielwert: **MISSING** — der Wert wird gemessen und dokumentiert, aber nicht mit einer erfundenen Schwelle bewertet. |
| measurement_window | Je Referenzstreckenlauf; mindestens ein Lauf je Sportart und je Plattform vor Gate A0; Wiederholung bei jeder Änderung an Sampling, Filter oder Location-Provider. |
| evidence_source | EV-002 (Gerätetest je Sport und Plattform auf Referenzstrecke); Mindestklasse `production-verified`. RISK-002 (GPS-Drift) ist die zugehörige offene Risikoposition. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — die Pass-Bedingung **ist** NFR-001 (< 3 %). NFR-001 ist im NFR-Audit auf `ASSUMPTION` herabgestuft; ein abgeleiteter Wert kann nicht stärker belegt sein als seine Quelle. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Zusätzlich blockierend für die Messung selbst: OQ-003 (Minimum iOS/Android und Referenzgeräte, Owner der Frage „Engineering/QA") ist MISSING — ohne Referenzgeräte ist NFR-001 nicht reproduzierbar messbar. |
| release_gate | GATE-A0 |
| rationale | Foreground-Tracking ist die technische Grundzusage des Produkts; gemessen wird Datenqualität, nicht Nutzerverhalten. Run und Bike getrennt, weil Sampling, Geschwindigkeitsbereich und damit die Driftwirkung sportspezifisch sind. Ein Aktivitäts-Abschluss-KPI als Produktziel gehört zu REQ-013, nicht hierher. |

Canvas: CAN-048, CAN-028, CAN-013, CAN-100 · Vision: VIS-003

### REQ-003 — Background, Pause und Recovery

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Recovery-Rate nach App-Kill und Absturz, Background-Vollständigkeit (Anteil erwarteter GPS-Punkte bei gesperrtem Bildschirm und im Hintergrund), Trefferquote und Falschauslösung der sportabhängigen Auto-Pause getrennt für Run und Bike, Batterieverbrauch pro Stunde. |
| target_or_pass_condition | NFR-003 als binäres Pass/Fail: kein Datenverlust bei App-Kill oder Absturz; Session-Recovery gelingt in 100 % der 30-Minuten-Kill-Tests je Plattform und je Sportart. AC-003: Pausenzeit verfälscht keine Metrik. NFR-002 nennt ein Batterieziel < 10 % pro Stunde, das die Quelle selbst als „Ziel" mit Pflicht zur Messwertdokumentation führt und das für dieses Produkt **nicht empirisch belegt** ist. Für die Auto-Pause-Falschauslösungsrate existiert kein dokumentierter Schwellwert: **MISSING**. |
| measurement_window | 30 Minuten je Kill-/Background-Test, je Plattform und je Sportart (EV-003); Batteriemessung über eine zusammenhängende Stunde (NFR-002); Wiederholung vor jedem Gate ab A0. |
| evidence_source | EV-003 (30-Minuten-Kill-/Background-Test je Plattform und Sport); Mindestklasse `production-verified` — Background-Execution und OS-Scheduler-Verhalten sind mit keinem Fake beweisbar. RISK-001 (OS drosselt/beendet Background-GPS) und RISK-003 (Batterie) sind offen. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — die Pass-Bedingung stützt sich auf NFR-003 und NFR-002, beide `ASSUMPTION`. **Selbstwiderspruch aufgelöst:** dieselbe Zelle bezeichnet den Batteriewert bereits als „nicht empirisch belegt“; `EXPLICIT` war damit mit dem eigenen Zellentext unvereinbar (DIV-5). |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. OQ-003 (Referenzgeräte) ist ebenfalls MISSING; ohne Gerätefestlegung ist der Batteriemesswert nicht vergleichbar. |
| release_gate | GATE-A0 |
| rationale | Zuverlässigkeit im Hintergrund ist reine Betriebsqualität. Getrennte Run-/Bike-Messung ist zwingend, weil Auto-Pause an sportabhängigen Geschwindigkeitsschwellen hängt: eine Bike-Rollphase und ein Run-Stillstand sind unterschiedliche Zustände. Das Batterieziel wird bewusst als hedged Zielwert der Quelle zitiert und nicht als validierter Messwert dargestellt. |

Canvas: CAN-049, CAN-101, CAN-108, CAN-028 · Vision: VIS-005

### REQ-004 — Erweitertes GPS-Datenmodell und Filter

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Klassifikationsverteilung des Filters über reale Drift-, Tunnel-, Sprung- und Hochgeschwindigkeits-Aufzeichnungen (akzeptiert / verworfen / unsicher), Reproduzierbarkeit bei wiederholtem Lauf über dieselbe Fixture, Restfehler in der Distanz nach Filter, Vollständigkeit der Pflichtfelder je Trackpunkt (Position, Zeit, Genauigkeit, verfügbare Bewegungsmetadaten). Run-Fixtures (Drift im Stand, niedrige Geschwindigkeit) und Bike-Fixtures (hohe Geschwindigkeit, lange Geraden) werden getrennt geführt. |
| target_or_pass_condition | AC-004 als Pass/Fail: die Klassifikation ist deterministisch — identische Eingabe erzeugt zu 100 % identische Ausgabe — und jede Entscheidung ist auf eine benannte Regel zurückführbar. Der Restfehler nach Filter zahlt auf NFR-001 (< 3 %) ein. Ein Zielwert für eine zulässige Verwurfsquote existiert in keinem Artefakt: **MISSING**; er wird nicht geraten, sondern dokumentiert. |
| measurement_window | Je Fixture-Suite-Lauf in CI (bei jedem Commit an der Filterlogik); Neuaufnahme realer Fixtures vor jedem Gate ab A0. |
| evidence_source | EV-004 (Drift-, Tunnel-, Sprung- und Hochgeschwindigkeits-Fixtures); Mindestklasse `real-boundary-smoke`: die Fixtures müssen aus realen Aufzeichnungen stammen, sonst prüft der Test nur sich selbst. Hinweis: das PRD führt REQ-004 selbst mit Source Type ASSUMPTION (Herkunft SRC-005) — das betrifft die Herkunft des Requirements, nicht die hier gesetzte Prüfbedingung. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — der Determinismusteil ist analytisch, der Restfehler zahlt jedoch auf NFR-001 (`ASSUMPTION`) ein. Zusätzlich führt das PRD REQ-004 **selbst** mit Source Type ASSUMPTION (Herkunft SRC-005); die Messmodellzeile widersprach damit der Requirement-Zeile. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. |
| release_gate | GATE-A0 |
| rationale | Datenqualität des GPS-Modells ist technische Qualität und Vorbedingung jeder späteren Aussage (Distanz, Score, Territory). Determinismus ist ein prüfbares Pass/Fail; eine Verwurfsquote als Ziel wäre ein erfundener Wert, weil sie von Strecke und Gerät abhängt. |

Canvas: CAN-100, CAN-028, CAN-113 · Vision: VIS-007

### REQ-005 — Robuste lokale Aktivitätsspeicherung

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Datenverlustrate über Schreib-, Kill- und Migrationszyklen, Anteil erfolgreicher Schema-Migrationen über das Fixture-Set, Transaktionsintegrität (Anzahl halb geschriebener oder verwaister Sessions), Schreiblatenz bei langen Tracks. |
| target_or_pass_condition | AC-005 und NFR-003 als Pass/Fail mit Schwelle 0: 0 verlorene Aktivitäten über Kill- und Migrations-Fixtures, 0 inkonsistente Indexe nach Migration, jede Migration ist idempotent wiederholbar. Kein Prozentziel — die geforderte Schwelle ist ausdrücklich null Verlust. |
| measurement_window | Je CI-Lauf der Repository- und Migrations-Tests; zusätzlich ein Kill-Test gegen die echte lokale Datenbank auf dem Gerät vor jedem Gate ab A0. |
| evidence_source | EV-005 (SQLite-Repository-Tests, Kill-Test und Migrations-Fixtures); Mindestklasse `real-boundary-smoke` — Kill-Test und Migration müssen gegen die echte lokale DB auf dem Gerät laufen. ASM-102 (SQLite statt AsyncStorage) ist eine offene Annahme, die durch einen technischen Spike zu bestätigen ist. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — die Pass-Bedingung **ist** NFR-003 (Nullschwelle). Die Schwelle 0 folgt logisch aus „kein Datenverlust“ und ist insoweit nicht belegbedürftig; belegbedürftig und **unbelegt** ist die Anforderung selbst. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. |
| release_gate | GATE-A0 |
| rationale | Persistenz ist Betriebszuverlässigkeit mit harter Nullschwelle; jedes Prozentziel wäre schwächer als die Anforderung selbst. **Sportgetrennte Messung requirement-spezifisch nicht anwendbar:** die Speicherung ist sportneutral und speichert dieselbe Trackpunkt-Struktur für Run und Bike; sportabhängig sind nur die daraus abgeleiteten Metriken (REQ-001). Gilt unter der Local-first-Präzisierung (CAN-095): Aktivitätsdaten bleiben in A0/A1 standardmäßig lokal. |

Canvas: CAN-131, CAN-028 · Vision: VIS-005

### REQ-006 — Routenplanung

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Routing-Erfolgsrate und Routing-Latenz je Sportprofil (der Proxy übersetzt `run` → `foot-walking` und `ride` → `cycling-regular`, CAN-094), API-Timeout- und Fehlerrate des Routing-Proxys, Anteil Planungen, die ohne verständliche Fehlermeldung scheitern, Abweichung zwischen geplanter Zieldistanz und tatsächlicher Routenlänge. Run und Bike getrennt, weil beide Profile unterschiedliche Wegenetze nutzen. |
| target_or_pass_condition | AC-006 als Pass/Fail über zehn reale Routenszenarien je Sport (EV-006): jedes Szenario liefert entweder eine plausible Route mit Distanz oder eine verständliche Fehlermeldung. Zusätzliche harte Kontrolle aus CAN-092 und NFR-007: der Bundle-Scan zeigt 0 Routing-Provider-Keys im App-Bundle. Zielwerte für Erfolgsrate, Latenz und Timeout-Rate sind **MISSING**: OQ-004 (Anbieter und Kostenlimits) ist offen, ohne Anbieter ist kein Latenzziel ableitbar. |
| measurement_window | Zehn reale Routenszenarien je Sportart vor Gate A0; Erfolgs-, Fehler- und Latenzwerte fortlaufend je Proxy-Aufruf erhoben und je Gate ausgewertet. |
| evidence_source | EV-006 (Routing-Service-Tests und zehn reale Routenszenarien je Sport); Mindestklasse `real-boundary-smoke` — ein gemockter Routing-Response verdeckt genau den NFR-007-Pfad. Ergänzend: Proxy-Integrationstest und Bundle-Scan aus ASM-103. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — **klauselweise geprüft:** „zehn reale Routenszenarien je Sport“ ist eine **gewählte, in keinem Artefakt belegte Zahl** (warum zehn und nicht fünf, ist nirgends begründet); Erfolgsrate, Latenz und Timeout sind bereits MISSING. Die Klausel **„0 Routing-Provider-Keys im App-Bundle“ ist EXPLICIT** (DEC-005 `user-confirmed`, CAN-092 `CONFIRMED`, SRC-006) — sie ist aber eine aus NFR-007 **entliehene Zusatzkontrolle**, nicht der eigene Zielwert von REQ-006, und trägt die Zeile deshalb nicht. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Rollenreferenz „Engineering/Product" gehört zur gekoppelten Frage OQ-004, nicht zu diesem REQ. |
| release_gate | GATE-A0 |
| rationale | Routenplanung wird als Betriebsqualität gemessen (Erfolgsrate, Latenz, Fehlerverhalten), nicht als Nutzungsquote; die Übernahme geplanter Routen durch andere Nutzer ist REQ-019 und liegt erst ab Gate B vor. **Statusnachzug:** `docs/traceability.md` führt REQ-006 unter anderem wegen OQ-011 als „blocked" — OQ-011 ist am 2026-07-19 entschieden (`infra/routing-proxy/`), `docs/decisions/open-questions.md` führt ihn noch offen. Der Rest der Blockade (OQ-004, OQ-005, CONTRA-006) besteht fort. |

Canvas: CAN-050, CAN-091…CAN-097, CAN-089 · Vision: VIS-003  
**Canvas-BLOCKER:** CAN-019 (Planungs- und Orientierungsproblem vor der Aktivität) ist `reserved` und inhaltlich MISSING. REQ-006 hat damit keinen atomaren Canvas-Problembezug, sondern nur Capability- und Constraint-Anker; das zählt laut Canvas nicht als erfüllte Canvas-Referenz.

### REQ-007 — Routenbezogener Fortschritt

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Off-Route-Genauigkeit unter realem GPS-Rauschen: Anteil korrekt erkannter Abweichungen, Falschauslösungsrate bei Routentreue, Erkennungslatenz bei Richtungsumkehr und bei Schleifen, Monotonie der Restdistanz entlang der geplanten Geometrie. Run und Bike getrennt: bei Bike bedeutet dieselbe Erkennungslatenz eine deutlich größere zurückgelegte Fehlstrecke. |
| target_or_pass_condition | AC-007 als Pass/Fail: die Restdistanz folgt der geplanten Polyline und ist **nicht** Gesamtdistanz minus gelaufene Distanz; der Fortschritt bleibt monoton plausibel; der Off-Route-Zustand wird sichtbar. ⚠️ **Herkunft dieser Pass-Bedingung korrigiert 2026-07-20.** Die Vorfassung berief sich auf „CAN-051 hält fest, dass die Subtraktion ausdrücklich **verboten** ist" und behandelte das Canvas-Item damit als Autorität. Tragend ist tatsächlich allein **DEC-004**, und DEC-004 steht auf `proposed` (`docs/decisions/decision-log.md`), verbietet also nichts — der Pass/Fail-Charakter ist insoweit **`ASSUMPTION`-gestützt** und bis zur Nutzerbestätigung nicht als belegte Abnahmebedingung verwendbar (Einzelheiten im Herkunftsvermerk unter dieser Tabelle). Numerische Schwellen für Off-Route-Korridor, Hysterese und maximale Erkennungslatenz existieren in keinem Artefakt: **MISSING** — vom DRI vor Gate A0 zu entscheiden, hier wird kein Wert geraten. |
| measurement_window | Je Abweichungs-Testfahrt/-lauf auf der Referenzstrecke, je Sportart und Plattform, vor Gate A0; Polyline-Projektions-Fixtures bei jedem CI-Lauf. |
| evidence_source | EV-007 (Polyline-Projektions-Fixtures und reale Abweichungstests); Mindestklasse `real-boundary-smoke` — die Projektion ist rein, die Off-Route-Erkennung hält aber nur unter realem GPS-Rauschen. RISK-006 (Routenrest bei Abweichungen falsch) ist offen. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Die fehlenden Korridor- und Hysteresewerte brauchen genau diesen DRI. |
| release_gate | GATE-A0 |
| rationale | Routenbezogener Fortschritt ist eine Genauigkeitseigenschaft und wird als solche gemessen. Der entscheidende Zielwert (Korridorbreite und Latenz) fehlt in allen Artefakten, deshalb `source_type` MISSING statt einer plausibel klingenden Zahl. Sportgetrennte Messung ist zwingend, weil Geschwindigkeit direkt in die tolerierbare Latenz eingeht. |

Canvas: CAN-051, CAN-028 · Vision: **MISSING — BLOCKER**  
**Vision-Anker entfernt 2026-07-20 (Nachzug, kein eigener Befund).** Die Vorfassung führte hier „Vision: VIS-003". `docs/traceability.md` (TRC-007) hat den Anker am 2026-07-20 **entfernt, nicht nur kommentiert**, mit belegtem Grund: „Fortschritt" wird in den Quellen durchgehend **longitudinal** gebraucht (Punkte, Ränge, Seasons, „ob sie sich verbessert"), die **aktivitätsinterne** Restdistanz erscheint dort ausschließlich auf funktionaler Ebene — SRC-001 T-02 „geplante vs. verbleibende km", SRC-003 §9 GATE A „verbleibende km korrekt" — **nie auf Vision-Ebene**. Konsistenzgrund: für REQ-006 ist VIS-003 aus demselben Grund entfernt; REQ-006 und REQ-007 sind Planungs- und Durchführungshälfte desselben Modus B. **Kein VIS-Item umgedeutet, keine VIS-ID erfunden**; für routenbezogene Navigation ist nicht einmal eine VIS-ID reserviert — ID-Bedarf gehört dem Registry-Owner. TRC-007 bleibt `broken`.  
**Canvas-BLOCKER:** CAN-019 ist `reserved` und inhaltlich MISSING — kein atomarer Canvas-Problembezug für REQ-007.  
**Rollenkorrektur 2026-07-20:** **CAN-100** ist ein **Risiko-Item** und steht nicht mehr in der Ankerliste, sondern in der Risiko-/Befundzeile (`evidence_source` oben, RISK-006). Nachzug zu `docs/traceability.md` TRC-007, das diese Korrektur bereits vollzogen hat — dieselbe Rollenkorrektur wie bei REQ-004. **Kein Item umgedeutet, keine ID vergeben.**

#### REQ-007 — Herkunftsvermerk (nachgetragen 2026-07-20, Nutzerauftrag Schritt 4)

**REQ-007 bleibt als route-aware Verbesserung vollständig erhalten.** Der Wortlaut ist unverändert; nichts ist verengt, abgeschwächt oder gestrichen. Festgeschrieben wird ausschließlich, **worauf die Anforderung steht**:

1. **Bewusste Abweichung von der einzigen Quelle, die den Rechenweg festlegt — nicht bloß fehlender Beleg.** SRC-004 spezifiziert wörtlich das Gegenteil der REQ-007-Forderung: `remainingDistanceMeters(plannedMeters, coveredMeters)` gibt `Math.max(0, plannedMeters - coveredMeters)` zurück (`docs/sources/SRC-004-…:416`), wird als `it('subtracts covered from planned', …)` getestet (`…:382`) und im Tracking-Screen gegen die zurückgelegte Gesamtdistanz verdrahtet (`…:2360`). SRC-001, SRC-002 und SRC-003 sagen zum Rechenweg **nichts**. Das ist der eigentliche und stärkere Grund für `ASSUMPTION`.
2. **Der Träger der Abweichung ist schwächer als „SRC-005/DEC-004" nahelegt.** **DEC-004** steht auf `proposed`, nicht `user-confirmed` (`docs/decisions/decision-log.md`). **SRC-005** ist laut `docs/SOURCE-MAP.md` ein `consistency-review` und wird dort ausdrücklich zu den „Ableitungen und Nachweisführung über dem Artefaktsatz, **keine Eingangsquellen**" gezählt. REQ-007 stützt sich damit auf **keine Nutzerquelle**. **Status bleibt `ASSUMPTION` bis zur ausdrücklichen Nutzerbestätigung.**
3. **Nicht quellengedeckte Anteile, offengelegt statt entfernt.** Volltextsuche über alle vier Quellen: „routebezogen"/„routenbezogen" **0 Treffer**, „Projektion"/„projiz" **0**, „monoton" **0**, „Korridor" **0**, „Hysterese" **0**, „falsche Richtung" **0**, „Richtungsumkehr" **0**. Betroffen sind damit auch **AC-007** („Fortschritt bleibt **monoton** plausibel … **Off-Route**-Zustand") und **EV-007** („**Polyline-Projektions**-Fixtures"). Beide bleiben im Wortlaut stehen, sind bereits `ASSUMPTION` und **erben** diesen Status aus REQ-007 — sie werden nicht gestrichen und nicht hochgestuft.
4. ⚠️ **Kein `source_type`-Widerspruch — ausdrücklich festgehalten, damit er nicht „aufgelöst" wird.** Die Zeile REQ-007 in der Requirements-Tabelle trägt `ASSUMPTION | SRC-005`, das Feld `source_type` in dieser Messmodell-Tabelle trägt `MISSING`. Das ist **kein Konflikt, sondern zwei verschiedene Fragen**: die Tabellenspalte nennt die Herkunft der **Anforderung**, das Messmodell-Feld die Herkunft des **Zielwerts** (Definition im Abschnitt „Zwei getrennte Achsen"; für Fälle, in denen beide auseinanderfallen, führt dieses PRD bei NFR-006 eigens ein getrenntes `requirement_source_type`). **Beide Werte sind korrekt und bleiben unverändert.** `MISSING` ist hier die wahrheitsgemäße Aussage: Korridorbreite, Hysterese und Latenz existieren in **keinem** Artefakt. Eine Harmonisierung auf `ASSUMPTION` wäre die **Hochstufung eines korrekten Abwesenheitsbefundes** und ist deshalb unterlassen.
5. **Folgestellen mit derselben Herkunft, hier nur gemeldet (fremdes Eigentum, kein Eingriff):** `docs/risks/revyr-risk-register.md` führt **RISK-006** (high, A0) mit der Gegenmaßnahme „Polyline-Projektion, Hysterese, Off-Route-Fixtures" — sämtlich Begriffe mit 0 Treffern in den Quellen. `docs/implementation/revyr-delivery-plan.md` führt „Routeprojektion, Off-Route und **Rückwärtsfall** getestet" als P0-04-Abnahmekriterium. `docs/canvas/…canvas.md` und `docs/ID-REGISTRY.md` führen CAN-051 mit der Präsensbehauptung, DEC-004 „verbiete" die Subtraktion. Alle vier sind als `ASSUMPTION`-abgeleitet nachzuziehen; die Nachzüge gehören ihren jeweiligen Ownern.

### REQ-008 — Verlauf und Detailansicht

> **Verengt am 2026-07-19, nicht deprecated.** GPX-Export → **REQ-039**; Wiederverwendung und Vergleich → seit dem 2026-07-20 **REQ-041** und **REQ-042** (vormals REQ-040, deprecated). Es bleibt dieselbe Anforderung, auf ihren atomaren Kern reduziert; deshalb keine neue ID. Alttitel: „Verlauf, Wiederverwendung und Export".
>
> **Der Scope bleibt verengt.** REQ-008 umfasst **ausschließlich** Verlauf und Detailansicht lokal gespeicherter Aktivitäten. **GPX-Export und Streckenvergleich gehören ausdrücklich nicht dazu** — auch nicht als Nebenbedingung, Testfall oder Messsignal.

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | **Getrennt für Run und Bike:** Ladefehlerrate und Ladezeit von Verlauf und Detailansicht bei wachsender Datenmenge; Anteil regulär abgeschlossener Aktivitäten, die nach einem App-Neustart im Verlauf erscheinen; Anteil Detailansichten, die den korrekten Track laden; Vollständigkeit und **Sportrichtigkeit** der Kernmetrik (Run: Pace; Bike: Geschwindigkeit); Anzahl beschädigter oder unbekannter Aktivitätsdatensätze, die zu einem unkontrollierten Zustand statt zu einem kontrollierten Fehler führen. |
| target_or_pass_condition | AC-008 als Pass/Fail mit Nullschwellen, **Run und Bike getrennt nachgewiesen**: (a) 100 % der regulär abgeschlossenen Aktivitäten erscheinen **nach Neustart** im Verlauf · (b) die Detailansicht lädt in 100 % der Fälle den korrekten Track · (c) **Run zeigt Pace**, (d) **Bike zeigt Geschwindigkeit** — 0 Verwechslungen · (e) **0 Aktivitäten gehen nach regulärem Abschluss verloren** · (f) beschädigte oder unbekannte Aktivitätsdaten führen in 100 % der Fälle zu einem **kontrollierten Zustand**. Eine Nutzungs- oder Wiederverwendungsquote wird **nicht** gesetzt: `docs/traceability.md` hält für REQ-008 ausdrücklich fest, dass kein CAN-009-/VIS-006-Signal existiert — ein solcher Zielwert wäre erfunden. |
| measurement_window | Je Gate-A0-Abnahme und bei jeder Änderung an Datenmodell oder Detailansicht; **je Sportart und je Plattform (iOS, Android) mindestens ein vollständiger Durchlauf einschließlich App-Neustart**. |
| evidence_source | EV-008 (Repository- und UI-Test je Sportart, Neustart-Test, Negativtest auf beschädigte Daten); Mindestklasse `real-boundary-smoke` — Persistenz über einen echten Prozessneustart ist mit keinem Fake beweisbar. |
| source_type | **ASSUMPTION** — zwei Gründe, die unabhängig voneinander tragen: (1) die Pass-Bedingungen sind analytische 0-/100-%-Schranken ohne gewählten Zahlenwert, belegbedürftig und **unbelegt** bleibt die Anforderung selbst (sie trug `EXPLICIT` über SRC-001/SRC-003, die laut `docs/SOURCE-MAP.md` **nicht auffindbar** sind); (2) der **verengte Wortlaut** stammt aus der Nutzerentscheidung vom 2026-07-19, ist aber **nicht ausdrücklich als Anforderungstext bestätigt**. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. |
| release_gate | GATE-A0 |
| rationale | Der prüfbare Kern ist **Verfügbarkeit und Korrektheit der lokal gespeicherten Historie**, nicht Nutzerverhalten. Die Run-/Bike-Trennung ist hier **nicht dekorativ**, sondern der eigentliche Fehlerfall: RISK-005 („Bike zeigt falsche Laufmetriken") wird genau in der Detailansicht sichtbar, weil dort die sportartspezifische Kernmetrik ausgegeben wird. Der naheliegende Produktoutcome — Wiederverwendung gespeicherter Routen — liegt seit dem 2026-07-20 bei **REQ-041** (Vergleich: **REQ-042**) und wird hier nicht mehr mitgemessen. |

Canvas: **CAN-138** (Verlauf und Detailansicht lokal gespeicherter Run- und Bike-Aktivitäten), CAN-030 · Vision: VIS-003

**Kanonischer CAN-138-Wortlaut (verbindlich, 2026-07-20):** „Nutzer können lokal gespeicherte Run- und Bike-Aktivitäten in einem Verlauf anzeigen und eine ausgewählte Aktivität mit Route, Dauer, Distanz und sportartspezifischer Kernmetrik in einer Detailansicht öffnen." (Vorher: „…eine Detailansicht mit **Strecke**, Dauer, Distanz … öffnen" — dieselbe Aussage, präzisierter Wortlaut, **keine** neue ID.) **CAN-138 bleibt ein gemeinsames Item und wird ausdrücklich nicht geteilt** — Begründung in der Migrationstabelle Runde 4.

**Canvas-BLOCKER geschlossen (2026-07-19).** ~~CAN-071 ist `reserved` und inhaltlich MISSING~~ → CAN-071 ist **deprecated** und durch atomare Items ersetzt. REQ-008 hat mit **CAN-138** erstmals einen **vollständig passenden** atomaren Capability-Anker; **CAN-139** trägt den GPX-Export (REQ-039), **CAN-142** und **CAN-143** tragen Wiederverwendung und Vergleich (REQ-041, REQ-042).

⚠️ **CAN-050 als Anker für REQ-008 entfernt (2026-07-20) — Registry §8 Punkt 39.** CAN-050 („Routenplanung **und** gespeicherte Routen") wurde hier bis zum 2026-07-19 als Canvas-Anker geführt, obwohl `docs/ID-REGISTRY.md` es **REQ-006** zuordnet („Trägt REQ-006"). Eine ID mit zwei Bedeutungen in zwei Requirement-Kontexten ist genau der Defekt, gegen den Registry-Regel 5 steht — und er las sich plausibel, weil REQ-008 gespeicherte Aktivitäten anzeigt und CAN-050 gespeicherte Routen nennt. **Es sind zwei verschiedene Gegenstände: gespeicherte *Routen* (Planung, REQ-006, Gate A0) gegen gespeicherte *Aktivitäten* (Verlauf, REQ-008, Gate A0).** Der Anker ist auf **CAN-138** verengt. Dieselbe Fehlzuordnung besteht laut Registry weiterhin in `docs/traceability.md:465`; diese Datei liegt außerhalb der Dateihoheit dieses PRD und wurde hier **nicht** geändert.

⚠️ **BLOCKER, unabhängig davon — CAN-050 ist selbst ein Composite** („Routenplanung" + „gespeicherte Routen") und bleibt es. Die Atomisierung ist eine Nutzerentscheidung und wird hier **nicht** vorweggenommen. Registry §8 Punkt 39.

⚠️ **BLOCKER — CAN-138 ist `source_type ASSUMPTION`,** solange der Wortlaut nicht ausdrücklich nutzerbestätigt ist. Der Anker ist damit vorhanden, aber nicht belegt.

### REQ-009 — Herzfrequenzquellen

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Anteil Aktivitäten mit korrekt gekennzeichneter HF-Quelle (HealthKit, Health Connect oder BLE), HF-Datenlückenrate je Quelle, Verbindungsabbruchrate je BLE-Sensor, Anteil Aktivitäten, in denen fehlende HF das Tracking blockiert. Getrennt erhoben für die Run-typischen Quellen (Watch/HealthKit/Health Connect) und die Bike-typische BLE-Brustgurt-/Sensorstrecke. |
| target_or_pass_condition | AC-009 als Pass/Fail: Quelle und Datenlücken sind in 100 % der aufgezeichneten Aktivitäten sichtbar gekennzeichnet; fehlende HF blockiert das Tracking in 0 % der Fälle. Ein Zielwert für die zulässige Lückenrate je Quelle existiert in keinem Artefakt: **MISSING** — die Lückenrate wird gemessen und dokumentiert (EV-009), aber nicht mit einer erfundenen Schwelle bewertet. |
| measurement_window | Je Aktivität erhoben; Abnahme je Gate A1 mit mindestens einem echten Gerätetest je Plattform und je Quelle (HealthKit, Health Connect, BLE-Gurt). |
| evidence_source | EV-009 (echte Geräte und BLE-Gurt je Plattform); Mindestklasse `production-verified` — reale Lücken- und Quellensemantik entsteht nur am realen Gerät. CAN-086 (Health-Berechtigungen brauchen belastbare Begründung) und RISK-010 (Store-Ablehnung) sind einschlägig. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — 100-%-Kennzeichnung und 0-%-Blockade sind analytische Schranken; die Anforderung selbst ist unbelegt. Die zulässige Lückenrate je Quelle bleibt MISSING. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. OQ-003 (Referenzgeräte) ist MISSING und begrenzt die Aussagekraft der Gerätematrix. |
| release_gate | GATE-A1 |
| rationale | HF-Anbindung ist Datenerfassungsqualität: messbar sind Quellenkennzeichnung, Lücken und Verbindungsstabilität — nicht Nutzerverhalten. Die Trennung nach Sportart folgt der realen Hardwarelage: Bike-Sensorik läuft über BLE, Run typischerweise über Watch/Health-Plattform. |

Canvas: CAN-052, CAN-086, CAN-013 · Vision: VIS-007 · Persona: **USER-004** (sekundär, neben USER-001 und USER-002)

**Persona-Verknüpfung geprüft und hergestellt (2026-07-19) — semantisch, nicht automatisch.** ~~CAN-025 hat im PRD keine USER-ID~~ → **USER-004** ist vergeben. Die Verknüpfung mit REQ-009 **trägt fachlich** und wird deshalb hergestellt:

REQ-009 verlangt das Lesen der Herzfrequenz aus **HealthKit, Health Connect oder unterstützten BLE-Sensoren**. USER-004 ist definiert über genau diese Geräte — Sportuhr (HealthKit/Health Connect), Herzfrequenzgurt und Fahrradsensoren (BLE) — und über die Erwartung, dass vorhandene Signale **ohne Medienbruch** einfließen. REQ-009 **ist** diese Capability; die Deckung ist unmittelbar und nicht bloß thematisch. Die zusätzliche Klausel „Quelle und Datenlücken transparent kennzeichnen" adressiert denselben Bedarf, weil ein Sensorbesitzer erkennen können muss, welches seiner Geräte gerade liefert.

⚠️ **Die Verknüpfung ist damit hergestellt, aber nicht belegt:** USER-004 trägt `source_type` **ASSUMPTION** und ist als Persona unbestätigt. USER-001 und USER-002 bleiben unverändert die primären Personas dieses Requirements; USER-004 tritt **hinzu** und verdrängt sie nicht.

### REQ-010 — Erklärbarer Belastungs-Score mit Confidence

| Feld | Wert |
|---|---|
| measurement_type | **PRODUCT_OUTCOME** |
| signal | Nutzung der Health-Erklärung: Anteil abgeschlossener Aktivitäten, bei denen das Warum-Sheet zum Belastungs-Score geöffnet wird (CAN-126). Als Kontextgröße daneben der Anteil Scores, die mit reduzierter Confidence (Fallback ohne Herzfrequenz) ausgegeben werden, damit eine niedrige Erklärungsnutzung nicht mit fehlender Datenbasis verwechselt wird. Run und Bike getrennt ausgewiesen, weil HF-Verfügbarkeit und damit Confidence-Verteilung sportspezifisch sind. |
| target_or_pass_condition | VIS-006 Zeile A: Öffnungsrate der Score-Erklärung **> 25 %** — **ASSUMPTION**: ein gesetztes Produktziel ohne empirische Grundlage, das nicht als validierte Produktwahrheit dargestellt werden darf. Daneben als harte Kontrolle aus AC-010: der Score nennt in 100 % der Fälle Gründe, Datenbasis, fehlende Signale und Unsicherheit; ohne Herzfrequenz wird ein klar begrenzter Fallback ausgewiesen. |
| measurement_window | Signal je Aktivität erhoben, ausgewertet über eine rollierende 28-Tage-Kohorte ab Gate A1. Das 28-Tage-Fenster ist aus dem Vier-Wochen-Bezug von CAN-124/VIS-006 abgeleitet; für die Öffnungsrate selbst nennt kein Artefakt ein Fenster — das Fenster ist damit **ASSUMPTION**. |
| evidence_source | EV-010 (Formeltests mit und ohne HF, UI-Test des Warum-Sheets); Mindestklasse `real-boundary-smoke`. **MESSLÜCKE:** kein Requirement und kein NFR beschreibt eine Telemetrie-/Analytics-Erhebung. Ohne sie ist die Öffnungsrate nicht erhebbar; zugleich fordern CAN-095 (local-first) und REQ-034 (Datensparsamkeit) Zurückhaltung. OPEN QUESTION für den DRI, berührt OQ-005. |
| source_type | **ASSUMPTION** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Rollenreferenz „Product/Legal" gehört zur gekoppelten Frage OQ-006 (Claims-Whitelist), nicht zu diesem REQ. |
| release_gate | GATE-A1 |
| rationale | Der Produktwert von REQ-010 ist genau, dass die Erklärung genutzt wird — ein echtes Nutzersignal. Der Zielwert stammt aus VIS-006, ist aber nirgends empirisch hinterlegt und deshalb ASSUMPTION. RISK-008 (Score wird als medizinische Aussage verstanden) macht die Erklärkontrolle zur zwingenden Nebenbedingung. |

Canvas: CAN-126, CAN-052, CAN-029, CAN-102 · Vision: VIS-006, VIS-007

### REQ-011 — HF-Zonen und optionale Ansage

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Korrektheit der Zonenberechnung gegen Zonen-Fixtures für geschätzte und manuell korrigierte Werte, Anzahl ausgelöster Live-Zonenhinweise bei deaktivierter Einstellung, Ansage- und Anzeigelatenz am realen Gerät mit Kopfhörer, Anteil Aktivitäten ohne verwertbare Zoneneinstufung. Run und Bike getrennt, weil Belastungsverteilung und damit Zonenverweildauer sportspezifisch sind. |
| target_or_pass_condition | AC-011 als Pass/Fail: Zonen reagieren korrekt auf geschätzte und manuell korrigierte Werte; die Deaktivierung verhindert jede Ansage — 0 Ansagen in 100 % der Deaktivierungstests. Ein Genauigkeitsziel für die Zonenschätzung existiert in keinem Artefakt: **MISSING**. Die verwendete Schätzformel ist zusätzlich an OQ-006 gebunden, weil eine Zonenempfehlung eine Health-Aussage ist. |
| measurement_window | Je CI-Lauf der Zonen-Unit-Tests; Gerätetest mit Kopfhörer je Plattform vor Gate A1; Wiederholung bei jeder Änderung der Schätzformel oder der Ansagelogik. |
| evidence_source | EV-011 (Zonen-Unit-Tests und Kopfhörer-Gerätetest); Mindestklasse `real-boundary-smoke` — Audio-Ansage und vollständige Deaktivierung sind nur über echte Kopfhörer am Gerät prüfbar. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — „0 Ansagen in 100 % der Deaktivierungstests“ ist eine analytische Nullschwelle; die Anforderung selbst ist unbelegt. Das Genauigkeitsziel der Zonenschätzung bleibt MISSING und ist zusätzlich an OQ-006 gebunden. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Rollenreferenz „Product/Legal" gehört zur gekoppelten Frage OQ-006. |
| release_gate | GATE-A1 |
| rationale | Der prüfbare Kern ist die deterministische Zonenberechnung und die vollständige Abschaltbarkeit — Betriebs- und Korrektheitseigenschaft mit Nullschwelle. **Kein Nutzersignal:** eine Nutzungsquote für Zonenhinweise wäre ein erfundener Engagement-KPI; `docs/traceability.md` hält für REQ-011 ausdrücklich fest, dass kein Signal für Zonen oder Audio-Ansage existiert. |

Canvas: CAN-052, CAN-102 · Vision: VIS-007 · Persona: **keine Verknüpfung mit USER-004**

**Persona-Verknüpfung geprüft und BEWUSST NICHT hergestellt (2026-07-19).** Die Vorgabe verlangt eine **semantische** Prüfung und verbietet die automatische Universalverknüpfung. Für REQ-011 fällt sie **anders aus als für REQ-009**:

| Prüfpunkt | Befund |
|---|---|
| Gegenstand des Requirements | Zonen**berechnung**, manuelle **Korrektur** und vollständige **Deaktivierbarkeit** der Ansage — nicht die Anbindung eines Geräts. |
| Definierendes Merkmal von USER-004 | Besitz externer Sensoren **und** deren Einbindung ohne Medienbruch. Diese Capability liefert **REQ-009**, nicht REQ-011. |
| Quellenabhängigkeit | REQ-011 ist gegenüber der HF-**Quelle** neutral: Zonen sind aus jeder verfügbaren Herzfrequenz berechenbar. Das Requirement ist ohne externen Sensor vollständig erfüllbar. |
| Adressatenkreis der Kernklausel | „Live-Zonenhinweise und Audio sind optional und **vollständig deaktivierbar**" richtet sich an **alle** Nutzer, nicht an Sensorbesitzer. |

**Ergebnis: REQ-011 erhält USER-004 nicht als Persona-Anker.** Der Bezug besteht nur **mittelbar** über die Datenabhängigkeit von REQ-009 — und eine mittelbare Abhängigkeit ist kein Zielgruppenanker, sonst wäre jede Anforderung, die irgendwo Herzfrequenz berührt, an USER-004 zu hängen. Genau das ist die untersagte Universalverknüpfung.

**Ausdrücklich nicht mitentschieden:** ob **REQ-010** (Belastungs-Score) an USER-004 gehört. Die Persona-Beschreibung nennt „Belastungsauswertung", was einen Bezug nahelegt; REQ-010 war jedoch **nicht Gegenstand der beauftragten Prüfung** und wird hier nicht stillschweigend mitverknüpft. **OPEN QUESTION** für den DRI.

**Folgebefund für `docs/traceability.md` (außerhalb der Dateihoheit dieses PRD):** dort ist bei REQ-011 „ambitionierte Persona MISSING im PRD" vermerkt. Dieser Vermerk ist ab jetzt in **beiden** Richtungen unzutreffend — die Persona fehlt nicht mehr, und REQ-011 soll sie nach dieser Prüfung auch nicht tragen. Der Vermerk ist zu **entfernen**, nicht durch eine USER-004-Verknüpfung zu ersetzen.

### REQ-012 — Stimmungs-Check-in und Korrelation

| Feld | Wert |
|---|---|
| measurement_type | **RESEARCH_HYPOTHESIS** |
| signal | Zwei getrennte Signale. **(a) Datenerhebung:** Quote der Stimmungs-Check-ins nach einer Aktivität (CAN-125) und die gemessene Check-in-Dauer am Gerät. **(b) Forschung:** Stärke, Stabilität und Unsicherheit der Korrelation zwischen Stimmungs-Check-in und Belastungs-/Trainingsmerkmalen über den erhobenen Korpus, ausgewertet getrennt für Run und Bike, weil Belastungsprofil und Aktivitätsdauer je Sportart systematisch abweichen. |
| target_or_pass_condition | **(a)** VIS-006 Zeile A: Check-in-Quote **> 50 %** — **ASSUMPTION**, gesetztes Produktziel ohne empirische Grundlage. AC-012 setzt zwei explizite Schranken: der Check-in dauert unter zwei Sekunden (Gerätemessung) und Trends werden erst ab mindestens vier Wochen Daten gezeigt, ohne Kausalitätsbehauptung. **(b)** Die Entscheidungsschwelle für die Anzeige einer Korrelation ist **MISSING**: kein Artefakt nennt Mindest-Effektstärke, Mindestfallzahl oder Signifikanzkriterium. Ohne diese Schwelle darf keine Korrelation ausgespielt werden. |
| measurement_window | Check-in-Quote und -Dauer je Aktivität, ausgewertet über eine rollierende 28-Tage-Kohorte. Korrelationsauswertung frühestens über ein Vier-Wochen-Fenster je Nutzer (AC-012), danach rollierend; längere Fenster sind nicht festgelegt (MISSING). |
| evidence_source | EV-012 (Zeitmessung, Fixture-Korrelation und Copy-Review); Mindestklasse `real-boundary-smoke` — die Zwei-Sekunden-Schranke ist eine Gerätemessung, keine Fixture-Aussage. Gleiche MESSLÜCKE wie REQ-010; Stimmungsdaten sind zudem eine besonders sensible Kategorie (REQ-034, CAN-088). |
| source_type | **ASSUMPTION** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Für die Claim-Formulierung der Trendanzeige zusätzlich OQ-006 („Product/Legal") offen. |
| release_gate | GATE-A1 |
| rationale | Der Check-in selbst ist eine einfache Funktion, die auszuwertende Korrelation zwischen Stimmung und Belastung ist dagegen eine unvalidierte Health-Korrelation. Die Check-in-Quote ist hier nicht das Erfolgsziel, sondern die Datenvoraussetzung der Untersuchung; sie wird trotzdem mit ihrem VIS-006-Wert und ASSUMPTION-Markierung mitgeführt, damit das Produktsignal nicht verlorengeht. |

**research_plan** — *Hypothese:* Zwischen dem Stimmungs-Check-in nach einer Aktivität und Belastungs-/Trainingsmerkmalen besteht ein Zusammenhang, der stabil genug ist, um ihn dem Nutzer als Trend zu zeigen — ohne Kausalitätsbehauptung. *Plan:* Stufe 1 Check-in-Erfassung ohne jede Trenddarstellung, Messung von Quote und Dauer. Stufe 2 Auswertung auf einem Korpus mit mindestens vier Wochen je Nutzer, getrennt nach Run und Bike, mit vorab festgelegtem Verfahren und ausgewiesener Unsicherheit. Stufe 3 Copy-Review gegen die Claims-Whitelist (OQ-006), bevor irgendein Trend sichtbar wird. *Fixtures/reale Daten:* reale Check-in-Verläufe über mindestens vier Wochen je Nutzer plus zugehörige Aktivitäts- und Belastungsdaten; Fixture-Korrelationen (EV-012) nur zur Verifikation der Auswertungslogik, nicht als Evidenz für den Zusammenhang selbst. *Entscheidungsschwelle:* **MISSING** — kein Artefakt beziffert Mindestfallzahl, Mindest-Effektstärke oder Unsicherheitsgrenze; vom DRI gemeinsam mit OQ-006 vor Gate A1 zu entscheiden. *Konsequenz bei unzureichender Evidenz:* der Check-in bleibt reine Erfassung ohne Trend- oder Korrelationsanzeige; kein produktiver Rollout vor bestandenem Gate.

Canvas: CAN-125, CAN-052, CAN-029, CAN-102 · Vision: VIS-006, VIS-007

### REQ-013 — Health-Home und Steigerungshinweis

| Feld | Wert |
|---|---|
| measurement_type | **PRODUCT_OUTCOME** |
| signal | Wiedernutzung und Nutzung der Health-Erklärung am Health-Home: W4-Retention aktiver Tracker-Nutzer (CAN-124) und Öffnungsrate der Erklärung zum Wochenzustand (CAN-126). Als Gegenprobe der Anteil Wochen, in denen der Steigerungshinweis ausgelöst wurde, damit Übersteuerung (Hinweis in fast jeder Woche) sichtbar wird. Run und Bike getrennt ausgewiesen, weil Wochenvolumen und Belastungsverlauf sportspezifisch sind. |
| target_or_pass_condition | VIS-006 Zeile A: W4-Retention **> 30 %** und Öffnen der Score-Erklärung **> 25 %** — **ASSUMPTION**, beide Werte sind gesetzte Produktziele ohne empirische Grundlage. AC-013 als begleitende Kontrolle: Aktivitäten, Belastung und Trend sind korrekt, Hinweise verwenden freigegebene Orientierungssprache. Die Schwelle, ab der „deutlich erhöhte Belastung" einen Hinweis auslöst, ist in keinem Artefakt beziffert: **MISSING**; zusätzlich an OQ-006 gebunden, weil der Hinweistext eine Health-Aussage ist. |
| measurement_window | W4-Retention: 28 Tage ab erster Aktivität, rollierende Kohorte. Hinweisauslösung und Wochenzustand: je Kalenderwoche, mit Vier-Wochen-Vergleichsfenster (AC-013). |
| evidence_source | EV-013 (Wochen-Fixtures und Claims-Lint); Mindestklasse `real-boundary-smoke` — Home-Rendering und freigegebene Claim-Sprache müssen am Gerät sichtbar geprüft werden. Gleiche MESSLÜCKE wie REQ-010: keine dokumentierte Telemetrie-Erhebung für Retention; Konflikt mit CAN-095 und REQ-034. |
| source_type | **ASSUMPTION** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. OQ-006 (Claims-Whitelist, „Product/Legal") ist ebenfalls offen und blockiert den Hinweistext. |
| release_gate | GATE-A1 |
| rationale | REQ-013 ist der Ort, an dem sich der Kernnutzen des Trackers im Nutzerverhalten zeigen soll — Wiedernutzung und Nutzung der Erklärung. Die unbezifferte Auslöseschwelle wird ausdrücklich als MISSING geführt statt sie zu erfinden; sie ist die schärfste Claim-Fläche des Produkts, unmittelbar an der Grenze CAN-072 („kein Medizinprodukt"). |

Canvas: CAN-124, CAN-126, CAN-029, CAN-102, CAN-072 · Vision: VIS-006, VIS-007

### ~~REQ-014~~ — deprecated am 2026-07-19

**REQ-014 („Designsystem und Accessibility") ist deprecated und durch zwei atomare Requirements ersetzt: [REQ-037 — Accessibility](#req-037--accessibility) und [REQ-038 — Monochromes tokenbasiertes Designsystem](#req-038--monochromes-tokenbasiertes-designsystem).** Deren Messmodelle stehen am Ende dieses Abschnitts in ID-Reihenfolge. AC-014, EV-014 und TRC-014 sind ebenfalls deprecated (→ AC-037/AC-038, EV-037/EV-038, TRC-037/TRC-038).

**Warum die Composite-Requirement nicht verengt, sondern zerlegt wurde.** Zugänglichkeit und Gestaltungssprache haben **verschiedene Prüfverfahren** (Audit und Screenreader-Durchlauf gegen Token-Inventar), **verschiedene Nachweise** und **verschiedene Gates**, und sie können unabhängig voneinander bestehen oder fallen: ein perfekt monochromes Designsystem kann den WCAG-Audit verfehlen, und eine barrierefreie App kann gegen die Farbregel verstoßen. Eine ID für beides hätte bedeutet, dass ein Zustand zwei unabhängige Wahrheitswerte trägt. **Die Requirement wurde ausdrücklich nicht umgedeutet** — kein stilles Verengen auf eine der beiden Hälften.

**Vision-Anker — der historische Befund bleibt und gilt jetzt nur noch für REQ-037.** REQ-014 hing ursprünglich an **VIS-009 (Privacy Boundary)** — null fachliche Überschneidung mit Accessibility. Die ID war syntaktisch gültig, las sich plausibel und trug die falsche Bedeutung. Die Prüfung VIS-001…VIS-010 (Registry §6.1.1) ergab **kein** fachlich passendes Item; VIS-003 und VIS-007 waren die Beinahe-Treffer und wurden verworfen, weil „verständliche Health-**Auswertung**" und „Datenbasis/Gründe/Unsicherheit **erklären**" den Health-**Inhalt** betreffen, nicht die Wahrnehmbarkeit der Oberfläche. Sie zu nehmen wäre derselbe Fehler wie VIS-009 gewesen. **VIS-011 (Accessibility Boundary)** deckt ausdrücklich **nur die Accessibility-Hälfte** ab — für die Designsystem-Hälfte (REQ-038) existiert bis heute **kein** Vision-Item; `VIS-012` ist reserviert und inhaltlich MISSING.

### REQ-015 — Verdiente Avatar-Progression

| Feld | Wert |
|---|---|
| measurement_type | **COMPLIANCE_CONTROL** |
| signal | Kontrollierter Nachweis: Anzahl leistungsbezogener Items, Teamkleidungs- und Season-Objekte, die auf einem anderen Weg als über eine definierte, verifizierte reale Leistung erreichbar sind; Anzahl Kaufpfade im Item-Katalog; Anzahl Doppel-Unlocks unter Wiederholung und Nebenläufigkeit; Anteil Unlock-Kriterien mit dokumentiertem, verifizierbarem Leistungsnachweis. |
| target_or_pass_condition | AC-015 als Pass/Fail mit Nullschwelle: jedes Item wird genau einmal freigeschaltet; 0 Kaufpfade und 0 Umgehungspfade für leistungsbezogene Items. Deckt zugleich das Non-Goal CAN-075 (kein Verkauf von Leistungsstatus, Boosts oder Spielvorteilen) und die Store-IAP-Prüfung ab. Ein Progressions- oder Engagement-Zielwert wird **nicht** gesetzt: `docs/traceability.md` hält fest, dass CAN-009 und VIS-006 kein Progressionssignal führen — ein solcher Wert wäre erfunden. |
| measurement_window | Vor Gate A2 und danach bei jeder Änderung des Item-Katalogs oder der Unlock-Kriterien; Idempotenz-Fixtures bei jedem CI-Lauf. |
| evidence_source | EV-015 (Idempotenz- und Unlock-Fixtures); Mindestklasse `real-boundary-smoke` — Idempotenz ist Domainlogik, die Nicht-Verfügbarkeit ohne Leistung ist jedoch eine UI-Aussage. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — „0 Kaufpfade, genau einmal“ ist eine analytische Nullschwelle. Der tragende Anker **CAN-075** führt Source Type `EXPLICIT` mit Quelle **SRC-001**, die laut `docs/SOURCE-MAP.md` **nicht im Repository auffindbar ist (BLOCKER)** — ein nicht nachschlagbares Belegdokument trägt kein EXPLICIT. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. |
| release_gate | GATE-A2 (PRD Release A2-B-C; erstmalige Abnahme mit GATE-A2, danach fortlaufend bis GATE-C) |
| rationale | Der harte, verletzbare Kern ist eine Schranke („nicht kaufbar", „genau einmal"), kein Nutzerverhalten. **Kein Nutzersignal, requirement-spezifisch begründet:** ein erfundenes Freischaltungs- oder Nutzungsziel würde genau den Anreiz erzeugen, den CAN-075 verbietet. **Keine Sporttrennung für die Kontrolle selbst:** Unlock-Idempotenz und Kaufpfad-Freiheit sind sportneutrale Katalogeigenschaften; sportabhängig sind allenfalls die Leistungskriterien, die dann je Sportart als eigene Unlock-Definition geprüft werden. |

Canvas: CAN-055, CAN-075, CAN-034 · Vision: VIS-004  
**Canvas-BLOCKER:** CAN-016 (Fortschritts- und Motivationsproblem) ist `reserved` und inhaltlich MISSING — kein atomarer Canvas-Problembezug; Fortschritt erscheint nur als Wertversprechen (CAN-030/CAN-034), nicht als Problem.

### REQ-016 — Recaps, Erfolgskarten und Live-Status

| Feld | Wert |
|---|---|
| measurement_type | **COMPLIANCE_CONTROL** |
| signal | Kontrollierter Nachweis: Anzahl erzeugter Erfolgskarten, Recaps und Live-/Lockscreen-Status, in denen Start- oder Endpunkt rekonstruierbar bleibt; Übereinstimmung der ausgewiesenen Metriken mit der gespeicherten Aktivität; Store-Konformität der Live-Aktivitätsanzeige je Plattform. |
| target_or_pass_condition | AC-016 als Pass/Fail: Metriken stimmen mit der gespeicherten Aktivität überein und sensible Standortdaten sind reduziert — 0 rekonstruierbare Start-/Endpunkte im Privacy-Snapshot-Test. **BEFUND:** die Reduktionsregel selbst (Radius, Zeitversatz, Zuschnitt) ist in keinem Artefakt spezifiziert — **MISSING**; ohne sie ist der Test nicht abschließend definiert. Eine Teilen- oder Nutzungsquote wird nicht gesetzt; sie wäre erfunden. |
| measurement_window | Vor Gate A2 und bei jeder Änderung des Karten-, Widget- oder Erfolgskarten-Renderings; je Plattform. |
| evidence_source | EV-016 (Bildexport-, Widget- und Privacy-Snapshot-Test); Mindestklasse `real-boundary-smoke` — Widgets und Live-Aktivitäten sind OS-Integrationen und nur am realen Gerät darstellbar. Einschlägiges Risiko: CAN-105 / RISK-015 (Standortmissbrauch). |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Die fehlende Reduktionsregel braucht genau diesen DRI, ergänzt um OQ-009 (Datenretention für GPS/Live). |
| release_gate | GATE-A2 |
| rationale | Die bindende, verletzbare Klausel steht im Requirement selbst („ohne sensible Start-/Endpunkte offenzulegen") und ist ein Datenschutz-Kontrollnachweis. **Kein Nutzersignal, requirement-spezifisch begründet:** für Recaps, Erfolgskarten und Live-Status existiert in CAN-124…CAN-129 und VIS-006 kein Erfolgssignal; eine Teilenquote als Ziel wäre ein erfundener Engagement-KPI. `source_type` MISSING, weil der zulässige Grad der Standortreduktion nirgends beziffert ist. |

Canvas: CAN-054, CAN-105, CAN-030 · Vision: VIS-004, VIS-009  
**Canvas-BLOCKER:** CAN-016 ist `reserved` und inhaltlich MISSING — kein atomarer Canvas-Problembezug.

### REQ-017 — Accounts, Auth und Datenmigration

| Feld | Wert |
|---|---|
| measurement_type | **COMPLIANCE_CONTROL** |
| signal | Kontrollierter Nachweis: Anzahl personenbezogener Datensätze, die nach einer vollständigen In-App-Accountlöschung verbleiben; Anzahl verbliebener Verknüpfungen zwischen Historieneinträgen und der gelöschten Person; Anteil verlustfrei migrierter lokaler Aktivitäten; Determinismus des Offline-Sync (identischer Konfliktfall erzeugt identisches Ergebnis); Erfolgsrate von E-Mail-, Apple- und Google-Auth gegen die echten Identitätsanbieter. |
| target_or_pass_condition | AC-017 als Pass/Fail: die Löschung entfernt alle personenbezogenen Daten und Identitätszuordnungen gemäß Retention-Regeln; 100 % der lokalen Aktivitäten migrieren deterministisch, 0 Datenverlust; verbleibende historische Aggregate sind wirksam anonymisiert und nicht rückführbar, sonst gelöscht. **CONTRA-005:** `status: resolved` · `evidence_status: pending` · `blocking: true` (Scope `database-schema-finalization`, `account-release`; `evidence_gate` B) — der frühere Zielkonflikt mit REQ-027 ist inhaltlich geklärt, die Evidence steht aus. **Weiterhin MISSING:** die Retentionsfristen selbst (OQ-009) und ein Prüfverfahren für „wirksam anonymisiert"; ohne beides ist „vollständig gelöscht" nicht abschließend testbar. |
| measurement_window | Vor Gate B und danach bei jeder Änderung von Auth, Sync oder Datenmodell; Löschungsnachweis je Plattform und je Auth-Anbieter. |
| evidence_source | EV-017 (E2E-Flow, Offline-Test, Löschungsnachweis, Nachweis der technischen Trennung von Identität und historischen Aggregaten, Anonymisierungsnachweis); Mindestklasse `production-verified` — Apple-/Google-Sign-in und der Löschungsnachweis sind nur gegen echte IdP- und Backend-Endpunkte belegbar. Store-Relevanz: In-App-Accountlöschung ist Policy-Voraussetzung (REQ-036, CAN-083). |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Zusätzlich offen: OQ-005 („Engineering") und OQ-009 („Privacy/Product") — ohne Retentionsfristen ist „vollständig gelöscht" nicht definierbar. |
| release_gate | GATE-B |
| rationale | Accounts, Migration und Löschung sind Datenschutz- und Store-Kontrollen mit Pass/Fail-Charakter; ein Anmelde- oder Konversionsziel wäre ein erfundener Engagement-KPI. `source_type` MISSING wegen fehlender Retentionsregeln und fehlendem Anonymisierungs-Prüfverfahren. **Sportgetrennte Messung requirement-spezifisch nicht anwendbar:** Auth, Sync und Löschung wirken auf denselben Datenbestand unabhängig von der Sportart; sportabhängig ist nur die Vollständigkeit der migrierten Inhalte, je Sportart stichprobenartig zu belegen. |

Canvas: CAN-056, CAN-084, CAN-088, CAN-014 · Vision: VIS-005, VIS-009

### REQ-018 — Privacy, Sichtbarkeit und Moderation

| Feld | Wert |
|---|---|
| measurement_type | **COMPLIANCE_CONTROL** |
| signal | Kontrollierter Nachweis gegen die Sichtbarkeitsmatrix: Anteil Matrixzellen, für die ein automatisierter Test die tatsächliche Sichtbarkeit belegt; Wirksamkeit des Blockierens (beidseitig, sofort) im Zwei-Account-Test; Anteil Meldungen, die bearbeitbar in der Moderationsqueue ankommen; Anzahl Profile, die entgegen dem Default öffentlich sind. |
| target_or_pass_condition | AC-018 als Pass/Fail mit 100-%-Abdeckung der Sichtbarkeitsmatrix: nur erlaubte Daten sind sichtbar, Blockierung wirkt beidseitig sofort, jede Meldung ist bearbeitbar, Profile sind standardmäßig privat (0 Abweichungen vom Default). Ein Moderations-SLA ist **MISSING** (OQ-010) — ohne ihn bleibt „bearbeitbar" zeitlich unbestimmt. |
| measurement_window | Vor Gate B und danach bei jeder Änderung der Sichtbarkeitsregeln, der RLS-Policies oder der Moderationsflüsse. |
| evidence_source | EV-018 (Sichtbarkeits-Matrix, Zwei-Account- und Moderationstest); Mindestklasse `production-verified` — eine Sichtbarkeitsmatrix ist nur gegen echte Backend-Policies/RLS widerlegbar, ein Mock bestätigt nur die eigene Annahme. RISK-021 (Moderationsaufwand skaliert nicht) ist offen. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — 100-%-Matrixabdeckung und „0 Abweichungen vom Default“ sind analytische Schranken. Die inhaltliche Klausel „Profile standardmäßig privat“ stammt aus **VIS-009**, Quelle **SRC-001 = nicht auffindbar**. Der Moderations-SLA bleibt MISSING (OQ-010). |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Rollenreferenz „Operations" gehört zur gekoppelten Frage OQ-010 (Moderations-SLA und Betrieb). |
| release_gate | GATE-B |
| rationale | Privacy, Sichtbarkeit und Moderation sind klassische kontrollierte Nachweise mit 100-%-Abdeckungsanspruch. **Kein Nutzersignal, requirement-spezifisch begründet:** eine Nutzungsquote von Privacy-Einstellungen könnte die Wirksamkeit der Regeln weder belegen noch widerlegen — entscheidend ist, dass die Matrix hält, auch wenn niemand sie bewusst nutzt. **Keine Sporttrennung:** Sichtbarkeit und Blockierung gelten identisch für Run- und Bike-Inhalte, weil die Regeln am Nutzer und nicht an der Sportart hängen. |

Canvas: CAN-057, CAN-059, CAN-037, CAN-014 · Vision: VIS-009

### REQ-019 — Routenempfehlungen und Feed

| Feld | Wert |
|---|---|
| measurement_type | **PRODUCT_OUTCOME** |
| signal | **Kennzahl (CAN-130):** bestätigte Routenübernahmen ÷ **auswertbare** Routenempfehlungen. **Getrennt ausgewiesen als `run_route_adoptions_per_recommendation` und `bike_route_adoptions_per_recommendation`** — eine Laufroute und eine Radroute haben unterschiedliche Wegenetze und Reichweiten und dürfen nicht gegeneinander verrechnet werden. Ein Gesamtwert darf gezeigt werden, **nie anstelle** der getrennten Sportwerte. Mehrere Nutzer dürfen dieselbe Empfehlung übernehmen — der Durchschnitt kann deshalb > 1,0 liegen. |
| target_or_pass_condition | **> 1,0 bestätigte Routenübernahmen je auswertbarer Empfehlung**, Run und Bike getrennt. Wortlaut der Nutzerentscheidung: *„Eine veröffentlichte und für mindestens einen berechtigten Empfänger sichtbare Routenempfehlung führt im Durchschnitt zu mehr als einer tatsächlichen Routenübernahme."* `target_source_type` **EXPLICIT** (CAN-130, Nutzerentscheidung 2026-07-19), `evidence_status` **planned**, `empirical_result` **MISSING**. Begleitende funktionale Kontrolle aus **AC-019**; die Berechenbarkeit der Kennzahl ist **AC-041**. |
| measurement_window | **Rollierende 28 Tage** (CAN-130). Ersetzt die frühere Angabe „rollierend je Kalenderwoche", die aus keinem Artefakt stammte. |
| evidence_source | **EV-019** (Zwei-Account-E2E-Flow, funktionaler Nachweis zu AC-019; Mindestklasse `real-boundary-smoke`) und **EV-041** (reproduzierbare, datenschutzkonforme Berechnung der Kennzahl zu AC-041, `evidence_status` **planned**). Die beiden Nachweise sind **getrennt** und haben unabhängige Zustände. |
| source_type | **ASSUMPTION** für die Anforderung selbst; **EXPLICIT** für den Zielwert der Kennzahl (CAN-130). Getrennt geführt, weil Anforderung und Zielwert hier unterschiedlich belegt sind. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. Zusätzlich **MISSING:** der Owner der Telemetrie-Instrumentierung (OQ-012). |
| release_gate | GATE-B |
| rationale | Routenübernahme ist das einzige Signal, das den Wert einer Empfehlung direkt misst. **Nebenbefund:** der Feed nähert sich der Vision-Grenze „kein allgemeines soziales Netzwerk"; das REQ definiert keine Obergrenze der Feed-Inhaltstypen (OPEN QUESTION), was bei steigender Übernahmequote relevant wird. |

#### CAN-130 — Nenner, Ausschlüsse und Guardrails

**„Auswertbar" ist eine Empfehlung nur, wenn alle vier Bedingungen erfüllt sind:** erfolgreich veröffentlicht · mindestens ein berechtigter Empfänger · im Messfenster sichtbar sein konnte · nicht vor möglicher Ausspielung gelöscht, blockiert oder moderativ verborgen.

**Nicht in den Nenner:** private Empfehlungen ohne berechtigten Empfänger · technisch nicht ausgelieferte Empfehlungen · vor Ausspielung gelöschte Empfehlungen · durch Blockierung oder Moderation vollständig unsichtbare Empfehlungen · Test- und Seed-Daten.

⚠️ **Korrektur gegenüber der früheren Fassung.** Dieses Messmodell führte datenschutzbedingt unsichtbare Empfehlungen bisher als **„Gegenprobe"**. Das war falsch: eine Gegenprobe wirkt im Nenner. Nach der Nutzerentscheidung sind sie **separat auszuweisen und ausdrücklich nicht in den Nenner zu nehmen** — sonst wird fehlender Zugang fälschlich als mangelndes Nutzerinteresse gelesen. Die Absicht der alten Formulierung war richtig, ihre Umsetzung hätte den Fehler erzeugt, den sie verhindern wollte.

**Guardrail-Signale (begleitend, nicht Teil der Kennzahl):** Anzahl auswertbarer Empfehlungen · Empfehlungen ohne berechtigten Empfänger · technisch fehlgeschlagene Ausspielungen · mediane Zahl berechtigter Empfänger je Empfehlung · Anteil Empfehlungen mit mindestens einer Übernahme · Übernahmen je 100 berechtigten Ausspielungen (sofern datenschutzkonform messbar) · Run/Bike-Verteilung · Lösch-, Blockierungs- und Moderationsanteil.

#### Telemetrie — privacy-minimiert, abschließend begrenzt

| | Werte |
|---|---|
| **Zulässige Ereignisse** | `route_recommendation_published` · `route_recommendation_eligible` · `route_recommendation_exposed` · `route_adopted` · `route_recommendation_deleted` · `route_recommendation_hidden` |
| **Zulässige Felder** | pseudonyme `recommendation_id` · pseudonyme `adoption_id` · `sport` (`run`\|`ride`) · Sichtbarkeitskategorie · grober Zeitstempel/Zeitbucket · Ergebnisstatus · Event-Version |
| **NICHT zulässig** | GPS-Koordinaten · Routengeometrie · Start-/Zieladresse · Health-Daten · Klarnamen · E-Mail · vollständige Gerätekennungen · öffentliche Analytics-Profile · Werbe-/Cross-Service-Tracking |

**Kein paralleler Standort- oder Verhaltenstracker.** Die Kennzahl ist möglichst aus ohnehin nötigen Backend-Ereignissen zu aggregieren.

**Local-first-Abgrenzung.** Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal (CAN-095). Erst **ab Gate B** dürfen für die **ausdrücklich aktivierte** Social-/Empfehlungsfunktion minimierte Metadaten verarbeitet werden. **Rohroute und GPS-Geometrie werden NIE für die Erfolgsmessung verwendet.** Gemessen wird das Ereignis „Empfehlung übernommen", **nicht** die später gelaufene oder gefahrene Strecke.

⚠️ **BLOCKER — OQ-012 (Telemetrie-Entscheidung).** Offen: ob `exposed` client- oder serverseitig erhoben wird · nötige Event-Metadaten · speicherbare Daten · Aufbewahrung der Rohereignisse · ab wann nur Aggregate · ob eine separate Einwilligung nötig ist · Wirkung von Profil-Privacy, Blockierungen und Löschungen · Entfernung oder Anonymisierung gelöschter Accounts aus den Messdaten · Owner der Instrumentierung · verwendete Analytics-/Event-Lösung. **Blockierend für den externen Gate-B-Erfolgsnachweis und für jede Behauptung, CAN-130 sei empirisch validiert. NICHT blockierend für A0/A1 und NICHT für die Dokumentkorrektur.**

⚠️ **MISSING — OQ-014 (Stichprobenregel).** Vor einer endgültigen Bewertung zu definieren: Mindestzahl auswertbarer Empfehlungen · Mindestzahl berechtigter Empfänger · Mindestdauer des Messfensters · Behandlung von Testkonten · Umgang mit Mehrfachübernahmen desselben Nutzers · Umgang mit gelöschten und moderierten Empfehlungen · getrennte Run-/Bike-Auswertung. **Es wird keine Mindestzahl geraten.** Bis dahin bleiben `evidence_status` **planned** und `empirical_result` **MISSING**.

Canvas: **CAN-130** (Erfolgssignal), CAN-058, CAN-105, CAN-032 · Vision: VIS-006, VIS-008

**Canvas-BLOCKER geschlossen (2026-07-19).** ~~CAN-130 ist `reserved` und inhaltlich MISSING~~ → CAN-130 ist `active` und vollständig spezifiziert (Registry §6.3.2). Das Messziel dieses Requirements hängt **nicht mehr allein an der Vision**. **Geschlossen ist die Definition, nicht der Nachweis:** `evidence_status` **planned**, `empirical_result` **MISSING**. Der frühere VIS-006-Zielwert „> 1,0" ist damit nicht validiert, sondern nur präzise definiert — insbesondere ist jetzt bestimmt, **was der Nenner ist**, was zuvor offen war.

### REQ-020 — Teamgründung und Beitritt

| Feld | Wert |
|---|---|
| measurement_type | **PRODUCT_OUTCOME** |
| signal | Teambeitritt: Anteil Nutzer, die 60 Tage nach Registrierung Mitglied mindestens eines Teams sind (CAN-127). Als harte Gegenkontrolle daneben: Anzahl Teams ohne Admin und Anzahl abgelaufener oder deaktivierter Tokens, über die dennoch ein Beitritt gelingt. |
| target_or_pass_condition | VIS-006 Zeile C: Nutzer in einem Team nach 60 Tagen **> 25 %** — **ASSUMPTION**, gesetztes Produktziel ohne empirische Grundlage. Daneben AC-020 als Pass/Fail mit Nullschwelle: 0 Teams ohne Admin zu irgendeinem Zeitpunkt (transaktionale Gründung) und 0 erfolgreiche Beitritte über ungültige Tokens. Die Gültigkeitsdauer von Beitrittslinks und QR-Codes ist in keinem Artefakt beziffert: **MISSING**. |
| measurement_window | 60 Tage ab Registrierung, rollierende Kohorte (Fenster wörtlich aus VIS-006 Zeile C und CAN-127). Transaktions- und Token-Kontrollen bei jedem CI-Lauf und im Zwei-Geräte-Test vor Gate C. |
| evidence_source | EV-020 (Datenbanktransaktions- und Zwei-Geräte-Test); Mindestklasse `real-boundary-smoke` — Deep-Link und QR nutzen Kamera und OS-Link-Handling, die Transaktion läuft gegen die echte Datenbank. |
| source_type | **ASSUMPTION** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. |
| release_gate | GATE-C |
| rationale | Teambeitritt ist mit Fenster und Zielwert in CAN-127/VIS-006 hinterlegt; der Zielwert bleibt unvalidiert. Die transaktionale Admin-Garantie wird als Nullschwellen-Kontrolle mitgeführt, weil sie ein harter Integritätsfall ist und nicht in einer Beitrittsquote aufgehen darf. **Sportgetrennte Messung der Mitgliedschaft requirement-spezifisch nicht anwendbar:** Teams sind laut PRD keine sportgetrennte Einheit — getrennt sind Rankings, Challenges und Rekorde (REQ-023, REQ-025), nicht die Mitgliedschaft selbst. |

Canvas: CAN-127, CAN-060, CAN-032, CAN-015 · Vision: VIS-006, VIS-008

### REQ-021 — Aktive Mitglieder und Teamwachstum

| Feld | Wert |
|---|---|
| measurement_type | **RESEARCH_HYPOTHESIS** |
| signal | Aus Simulation und späterer Feldmessung: Anteil gezählter Mitglieder mit Aktivität im definierten Zeitfenster, Verhältnis von Einladungen zu real integrierten Mitgliedern, Verteilung des Mentorbonus über Teamgrößen, Anteil Teams, deren Stufenaufstieg allein durch Einladungsvolumen erklärbar wäre. Run und Bike werden in der Aktivitätszählung getrennt geführt, damit ein Team nicht durch eine einzige Sportart die Aktivitätsschwelle erfüllt und die andere verdeckt. |
| target_or_pass_condition | Entscheidungsschwelle **MISSING**: kein Artefakt beziffert Kapazitätsgrenzen, Stufenkurve, das „definierte Zeitfenster" der Aktivität oder die Höhe des Mentorbonus. AC-021 gibt nur die qualitative Bedingung vor — nur Mitglieder mit Aktivität im definierten Zeitfenster zählen, der Bonus folgt erst nach nachgewiesener Integration. Ohne beziffertes Aktivitätsfenster ist die Regel nicht prüfbar. Es wird kein Wert geraten. |
| measurement_window | Simulationsläufe vor Gate C über synthetische und reale Teamverläufe; im Feld je Kalenderwoche und je 60-Tage-Kohorte, sobald Teams existieren. Das eigentliche Aktivitätsfenster ist MISSING und muss vor der Messung entschieden werden. |
| evidence_source | EV-021 (Zeitfenster- und Integrations-Fixtures); Mindestklasse `integration-fake` — die Zeitfenster- und Kapazitätsregel ist reine Logik ohne eigene Grenze. Für die Kalibrierung sind reale Teamverläufe erforderlich, keine rein synthetischen. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Die fehlenden Mechanikparameter brauchen einen produktseitigen Entscheider, der nicht benannt ist. |
| release_gate | GATE-C |
| rationale | Kapazität, Stufen und Mentorbonus sind unvalidierte Anreizparameter (Quoren- und Verfallsmodell). Ohne Simulation kann die Mechanik genau das belohnen, was das REQ verhindern soll (bloße Einladungen). `docs/traceability.md` führt REQ-021 zusätzlich als `value-risk`: reine Spielmechanik ohne Health-Beitrag, in Spannung zu CAN-033. |

**research_plan** — *Hypothese:* Kapazitätsgrenzen, Teamstufen und Mentorbonus belohnen aktive, real integrierte Mitglieder stärker als bloßes Einladungsvolumen — ohne die Health-Grundlage zu verdrängen (CAN-033). *Plan:* Stufe 1 Parametersatz (Kapazität, Stufenkurve, Aktivitätsfenster, Bonushöhe) festlegen lassen — heute MISSING. Stufe 2 Szenariosimulation über Teamverläufe mit unterschiedlichen Einladungs-/Aktivitätsmischungen; Kennzahl ist der Anteil des Stufenaufstiegs, der allein durch Einladungen erklärbar ist. Stufe 3 Feldvalidierung über mindestens eine 60-Tage-Kohorte nach Gate C. *Fixtures/reale Daten:* reale Aktivitäts- und Mitgliedschaftsverläufe echter Teams für die Kalibrierung; Zeitfenster- und Integrations-Fixtures (EV-021) nur zur Verifikation der Zähllogik. *Entscheidungsschwelle:* **MISSING** — weder ein zulässiger Anteil einladungsgetriebener Aufstiege noch ein Aktivitätsfenster ist beziffert; vom DRI vor Gate C zu entscheiden. *Konsequenz bei unzureichender Evidenz:* Kapazitätsstufen und Mentorbonus bleiben deaktiviert, Teams funktionieren ohne Wachstumsmechanik; kein produktiver Rollout vor bestandenem Gate.

Canvas: CAN-060, CAN-128, CAN-033 · Vision: VIS-008

### REQ-022 — Gemeinsame Aktivitäten und Events

| Feld | Wert |
|---|---|
| measurement_type | **PRODUCT_OUTCOME** |
| signal | Gemeinsame Aktivität: Anteil Teams mit mindestens einer erkannten realen gemeinsamen Aktivität pro Kalenderwoche (CAN-128). Als Gegenprobe die Falsch-Positiv-Rate der Erkennung im Zwei-Geräte-Test (zufällige räumliche und zeitliche Nähe ohne gemeinsame Aktivität) sowie die Nichterkennungsrate bei tatsächlich gemeinsamer Aktivität. Run und Bike getrennt, weil Gruppendynamik, Abstände und Geschwindigkeitsprofile — und damit die Überschneidungskriterien — sportspezifisch sind. |
| target_or_pass_condition | VIS-006 Zeile C: Teams mit realer gemeinsamer Aktivität pro Woche **> 40 %** — **ASSUMPTION**, gesetztes Produktziel ohne empirische Grundlage. AC-022 als begleitende Kontrolle: echte gemeinsame Aktivität wird erkannt, nicht gemeinsame wird abgelehnt, Eventinhalte sind moderierbar. Zeit- und Distanzschwellen der Überschneidung sowie die zulässige Falsch-Positiv-Rate sind in keinem Artefakt beziffert: **MISSING**. |
| measurement_window | Je Kalenderwoche (Fenster wörtlich aus VIS-006 Zeile C und CAN-128); Erkennungsgüte zusätzlich je Zwei-Geräte-Testlauf vor Gate C. |
| evidence_source | EV-022 (Pure-Function-Fixtures und Zwei-Geräte-Eventtest); Mindestklasse `production-verified` — die Zeit-/Raumkorrelation zweier realer Aktivitäten ist eine Feldbedingung. |
| source_type | **ASSUMPTION** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. |
| release_gate | GATE-C (PRD Release C-D) |
| rationale | Gemeinsame Aktivität ist mit CAN-128/VIS-006 samt Wochenfenster hinterlegt; der Zielwert bleibt unvalidiert. Die Erkennungsgüte wird als Nebenbedingung mitgeführt, weil eine hohe Quote wertlos wäre, wenn sie durch Falsch-Positive entsteht. Die Erkennung erfordert den Vergleich fremder Standortspuren und verschärft damit CAN-105 (Standortmissbrauch). |

Canvas: CAN-128, CAN-067, CAN-015, CAN-105 · Vision: VIS-006, VIS-008

### REQ-023 — Effort-Normalisierung

| Feld | Wert |
|---|---|
| measurement_type | **RESEARCH_HYPOTHESIS** |
| signal | Aus Monte-Carlo- und Szenariosimulation über reale Aktivitätsverteilungen: Verteilung des sportübergreifenden Rangs nach Sportart, systematischer Rangversatz Run gegen Bike, Sensitivität des Ergebnisses gegenüber dem Effort-Faktor, Anteil Wertungen, in denen die verwendete Faktorversion nicht nachvollziehbar dokumentiert ist. Die internen Run- und Bike-Wertungen bleiben getrennt und werden nicht normalisiert — das ist selbst eine Prüfbedingung. |
| target_or_pass_condition | AC-023 qualitativ EXPLICIT: keine Sportart dominiert systematisch, verwendete Version und Faktoren sind nachvollziehbar. Eine numerische Entscheidungsschwelle für „systematische Dominanz" ist **MISSING** — OQ-008 (Effort-, Territory- und Bahngold-Startwerte) ist offen und kein Artefakt beziffert einen zulässigen Rangversatz. Startwerte gelten bis zur bestandenen Simulation als **ASSUMPTION** und dürfen nicht als kalibriert dargestellt werden. |
| measurement_window | Simulationsläufe je Faktorversion vor Gate C; nach Rollout rollierende Auswertung je Wertungsperiode (Periodenlänge ist nicht definiert — MISSING). |
| evidence_source | EV-023 (Monte-Carlo-/Szenariosimulation und Kalibrierungsbericht); Mindestklasse `integration-fake`, mit der ausdrücklichen Auflage, dass der Kalibrierungskorpus aus real aufgezeichneten Aktivitäten bestehen muss und nicht aus synthetischen. RISK-014 (Run/Bike-Effort ist unfair) ist offen. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Rollenreferenz „Product/Data" gehört zur gekoppelten Frage OQ-008. |
| release_gate | GATE-C |
| rationale | Effort-Faktoren sind der Kern der Fairnesszusage und heute unkalibriert; jeder Startwert ist eine Annahme. Sportgetrennte Messung ist hier nicht optional, sondern der Gegenstand der Untersuchung selbst. |

**research_plan** — *Hypothese:* Versionierte, simulierte Effort-Faktoren normalisieren Run und Bike so, dass in sportübergreifenden Team- und Territory-Wertungen keine Sportart systematisch dominiert. *Plan:* Stufe 1 Kalibrierungskorpus aus real aufgezeichneten Run- und Bike-Aktivitäten aufbauen. Stufe 2 Monte-Carlo-/Szenariosimulation über Faktorvarianten; Kennzahl ist der systematische Rangversatz zwischen den Sportarten. Stufe 3 Kalibrierungsbericht mit versionierten Faktoren, Rollout nur mit protokollierter Version je Wertung. Stufe 4 Nachmessung im Feld je Wertungsperiode. *Fixtures/reale Daten:* real aufgezeichnete Aktivitäten beider Sportarten in ausreichender Streuung über Dauer, Distanz und Leistungsniveau; synthetische Verteilungen nur zur Verifikation der Simulationsmechanik. *Entscheidungsschwelle:* **MISSING** — kein zulässiger Rangversatz beziffert, OQ-008 offen; vom DRI zusammen mit OQ-008 vor Gate C zu entscheiden. *Konsequenz bei unzureichender Evidenz:* keine sportübergreifende Wertung; Team- und Territory-Wertungen bleiben sportgetrennt, bis die Simulation eine tragfähige Faktorversion belegt.

Canvas: CAN-062, CAN-033, CAN-036 · Vision: VIS-008  
**Canvas-BLOCKER:** CAN-020 (Fairness- und Manipulationsproblem) ist `reserved` und inhaltlich MISSING — kein atomarer Canvas-Problembezug; Fairness erscheint nur als Wertversprechen (CAN-033/CAN-036) und Risiko (CAN-104/CAN-109).

### REQ-024 — Anti-Cheat mit Confidence-Stufen und minimiertem Signalumfang

| Feld | Wert |
|---|---|
| measurement_type | **RESEARCH_HYPOTHESIS** |
| signal | Über einen realen Aktivitätskorpus, zwingend getrennt für Run und Bike: Falsch-Positiv-Rate je Confidence-Stufe (`verified-high`, `verified-standard`, `low-confidence`, `review-required`, `rejected`), Anteil `review-required` an allen Aktivitäten, Trefferquote gegen bekannte Manipulationsfixtures, Anteil Fälle, in denen allein fehlende Sensoren zu einer Herabstufung führen. Zusätzlich als Datenschutzkontrolle: Anzahl serverseitig empfangener Payloads, die über die in REQ-024 aufgezählten abgeleiteten Signale hinausgehen (Sollwert 0). Die Sporttrennung ist konstitutiv: Geschwindigkeiten, die für Run zwingend Manipulation bedeuten, sind für Bike legitim. |
| target_or_pass_condition | AC-024 qualitativ EXPLICIT: fehlende Sensoren allein führen nicht zur Betrugsannahme (höchstens `low-confidence`, nie automatisch `rejected`); klare Manipulation zählt nicht für den Wettbewerb. Zusätzliche Nullschwelle aus CONTRA-004: 0 Rohsensorserien und 0 vollständige HF-/Schrittverläufe im serverseitigen Standard-Payload. Eine zulässige Falsch-Positiv-Rate ist **MISSING** — kein Artefakt beziffert sie, EV-024 verlangt nur ein False-Positive-Review; Schwellen müssen sportgetrennt entschieden werden. |
| measurement_window | Auswertung je Korpusdurchlauf vor Gate C; nach Rollout laufende Überwachung der Falsch-Positiv-Rate je Kalendermonat und je Sportart. Das Überwachungsintervall ist nicht dokumentiert — ein Vorschlag wäre erfunden, daher offen zu entscheiden. |
| evidence_source | EV-024 (Betrugs-/Grenzfall-Fixtures, False-Positive-Review und Nachweis des minimierten Signalumfangs); Mindestklasse `production-verified` — die Falsch-Positiv-Rate ist erst gegen einen realen Aktivitätskorpus aussagefähig. RISK-013 (Anti-Cheat produziert False Positives) ist offen. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. OQ-009 (Datenretention) ist für die zeitlich begrenzte Einspruchsprüfung zusätzlich offen. |
| release_gate | GATE-C |
| rationale | Anti-Cheat-Schwellen sind unvalidiert. Die entscheidende Größe ist die Fehlbeschuldigung realer Nutzer (CAN-109), nicht die Betrugserkennung allein (CAN-104) — beide Richtungen werden deshalb getrennt gemessen. **CONTRA-004:** `status: resolved` · `evidence_status: pending` · `blocking: true` (Scope `competition-release`, `territory-release`; `evidence_gate` C) — der frühere Widerspruch zur Datenminimierung (REQ-034) ist durch den abschließend aufgezählten Signalumfang geklärt; die Implementierungs-Evidence steht aus. Ohne bezifferte Schwelle darf die Klassifikation keine Wettbewerbswirkung entfalten. **BLOCKER:** RISK-013 verlangt einen Einspruchs-/Appeal-Flow, den kein Requirement beschreibt. |

**research_plan** — *Hypothese:* Serverseitige Plausibilitätsregeln trennen manipulierte von realen Aktivitäten so, dass reale Nutzer nicht fälschlich als Betrug klassifiziert werden — auch ohne vollständige Sensorausstattung und ohne Übertragung von Rohsensorserien. *Plan:* Stufe 1 realen Aktivitätskorpus je Sportart aufbauen, inklusive Grenzfällen (Bahnfahrt, Windschatten, Zugfahrt, Sensorausfall). Stufe 2 Regelsatz gegen den Korpus laufen lassen, Falsch-Positiv- und Falsch-Negativ-Rate je Confidence-Stufe bestimmen. Stufe 3 manuelles False-Positive-Review der Grenzfälle. Stufe 4 Entscheidung über Schwellen; der Umfang übertragener Sensordaten ist durch CONTRA-004 bereits entschieden und nur noch nachzuweisen. *Fixtures/reale Daten:* realer Aktivitätskorpus beider Sportarten plus kuratierte Manipulationsfixtures (Teleport, unplausible Geschwindigkeit, importierte Fremdtracks); rein synthetische Daten reichen für die Falsch-Positiv-Aussage nicht. *Entscheidungsschwelle:* **MISSING** — keine zulässige Falsch-Positiv-Rate beziffert, weder global noch je Sportart; vor Gate C zu entscheiden. *Konsequenz bei unzureichender Evidenz:* keine wettbewerbswirksame Klassifikation; Aktivitäten werden höchstens intern markiert, aber nicht aus Rankings, Challenges oder Territory ausgeschlossen.

Canvas: CAN-063, CAN-104, CAN-109, CAN-036 · Vision: VIS-008  
**Canvas-BLOCKER:** CAN-020 ist `reserved` und inhaltlich MISSING — kein atomarer Canvas-Problembezug.

### REQ-025 — Challenges, Rankings und idempotente Rewards

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Idempotenz und Determinismus: Anzahl doppelt vergebener Rewards unter Nebenläufigkeit und bei Wiedereinspielung derselben Aktivität, Reproduzierbarkeit des Challenge-Fortschritts über deterministische Fixtures, Anteil serverkonfigurierter Challenge-Definitionen, die ohne Client-Release wirksam werden, Anzahl Rankings, in denen Run- und Bike-Ergebnisse vermischt sind. Rankings werden sportgetrennt geführt und getrennt geprüft (VIS-008). |
| target_or_pass_condition | AC-025 als Pass/Fail mit Nullschwelle: der Fortschritt ist korrekt und 0 Rewards werden doppelt vergeben — auch bei Wiederholung und unter Nebenläufigkeit gegen die echte Datenbank mit echten Constraints. 0 sportübergreifend vermischte Rankings. Ein Teilnahme- oder Engagement-Zielwert wird **nicht** gesetzt: `docs/traceability.md` hält fest, dass kein Challenge- oder Ranking-Signal in CAN-009/VIS-006 existiert. |
| measurement_window | Je CI-Lauf der deterministischen Fixtures; Nebenläufigkeits- und Wiederholungstest gegen die echte Datenbank vor Gate C und bei jeder Änderung der Reward-Vergabe. |
| evidence_source | EV-025 (deterministische Fixtures und Wiederholungs-Test); Mindestklasse `real-boundary-smoke` — Idempotenz unter Nebenläufigkeit hält nur gegen die echte Datenbank mit echten Constraints. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — „0 doppelte Rewards, 0 vermischte Rankings“ ist eine analytische Nullschwelle; die Anforderung selbst ist unbelegt. Die Sporttrennung stützt sich auf VIS-008, dessen Quelle ebenfalls SRC-001/SRC-003 ist. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. |
| release_gate | GATE-C |
| rationale | Der prüfbare Kern ist Korrektheit und Idempotenz — Betriebsqualität mit Nullschwelle. **Kein Produktsignal, requirement-spezifisch begründet:** `docs/traceability.md` führt REQ-025 als `value-risk`, weil Rankings und Rewards Wettbewerbsmechanik ohne Health-Beitrag sind und kein Erfolgssignal misst, ob sie den Produktwert bewegen; ein erfundenes Teilnahmeziel würde diese dokumentierte Lücke verdecken statt sie sichtbar zu halten. |

Canvas: CAN-061, CAN-062, CAN-033 · Vision: VIS-004

### REQ-026 — Team-Territory

| Feld | Wert |
|---|---|
| measurement_type | **RESEARCH_HYPOTHESIS** |
| signal | Aus Geo-Fixtures, Simulation und Karten-Lasttest: Determinismus der Eroberungsberechnung bei identischem Eingabeset, Verteilung der Arealwechsel über Quorumsvarianten, Renderzeit und Bildrate des Kartenlayers bei realer Datenmenge (NFR-004), Anzahl Pfade, über die das interne Raster sichtbar wird, Anteil in die Wertung eingehender Beiträge ohne verifizierten Status. Als nachgelagertes Produktsignal nach bestandenem Gate: Season-Teilnahme aktiver Teams (CAN-129). |
| target_or_pass_condition | Quorumswerte, Verfallsmodell und Arealschwellen sind **MISSING** (OQ-008). AC-026 gibt qualitativ vor: Eroberung folgt Formel und Quorum, reale benannte Areale werden dargestellt, das interne Raster ist nie sichtbar — 0 Sichtbarkeitspfade (EXPLICIT, Nullschwelle, entspricht Non-Goal CAN-078). NFR-004 fordert viewportbasierte Kartenlayer und einen Geo-Lasttest vor D, nennt aber keine Millisekunden- oder Bildratenschwelle: **MISSING**. Nachgelagertes Produktziel VIS-006 Zeile D: Season-Teilnahme aktiver Teams > 60 % — **ASSUMPTION**, unvalidiert. |
| measurement_window | Simulations- und Lasttestläufe je Parametervariante vor Gate D; nach Rollout Auswertung je Season-Zyklus — die Länge eines Season-Zyklus ist in keinem Artefakt definiert (MISSING, siehe auch REQ-027). |
| evidence_source | EV-026 (Geo-Fixtures, Simulation und Karten-Lasttest); Mindestklasse `real-boundary-smoke` — Kartenlayer-Performance und Geo-Lasttest brauchen echtes Gerät und echte Datenmenge. RISK-017 (Polygonoperationen inkonsistent oder langsam) ist offen. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Rollenreferenzen „Product/Data" (OQ-008) und „Engineering" (OQ-005) gehören zu den gekoppelten Fragen. |
| release_gate | GATE-D |
| rationale | Territory und Quoren sind unvalidiert und ihre Parameter offen. Die Unsichtbarkeit des internen Rasters wird als harte Nullschwelle mitgeführt, weil sie ein Non-Goal (CAN-078) schützt. **Sportbezug:** die Territory-Wertung ist sportübergreifend und hängt damit unmittelbar an der noch unkalibrierten Effort-Normalisierung aus REQ-023 — solange die fehlt, ist auch die Territory-Fairness nicht bewertbar. |

**research_plan** — *Hypothese:* Nur verifizierte Beiträge und ein Quorum bestimmen reale, benannte Team-Areale; das interne Raster bleibt unsichtbar und die Kartenlayer bleiben unter realer Datenmenge performant filterbar. *Plan:* Stufe 1 Quorum, Verfallsmodell und Arealschwellen entscheiden (heute MISSING, OQ-008). Stufe 2 Simulation über Geo-Fixtures und reale Aktivitätsdichten; Kennzahl ist Determinismus und Stabilität der Arealwechsel. Stufe 3 Karten-Lasttest auf realem Gerät mit realer Datenmenge gegen NFR-004. Stufe 4 Threat-Model für Standortmissbrauch (CAN-105) vor jeder Freischaltung. *Fixtures/reale Daten:* Geo-Fixture-Suite plus reale Aktivitätsdichten aus mindestens einer Stadt; synthetische Gleichverteilungen unterschätzen die Ballung und sind allein nicht ausreichend. *Entscheidungsschwelle:* **MISSING** — Quorumswert, Verfallsrate und Performanceschwelle (NFR-004) unbeziffert; vor Gate D zu entscheiden. *Konsequenz bei unzureichender Evidenz:* kein Territory-Rollout; CAN-079 und CAN-136 halten Territory ohnehin bis Stufe D gesperrt, bei nicht bestandener Simulation bleibt es auch danach deaktiviert.

Canvas: CAN-064, CAN-106, CAN-078, CAN-129, CAN-032 · Vision: VIS-008, VIS-006

### REQ-027 — Seasons und nach Finalisierung fachlich unveränderbare Historie

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Datenintegrität über den Season-Wechsel: Anteil zurückgesetzter Objekte, die tatsächlich zum aktiven Spielfeld gehören; Anzahl veränderter oder verlorener historischer Snapshots, Trophäen und Vereinsheim-Einträge nach zwei Season-Zyklen; Reproduzierbarkeit des Rollovers bei Wiederholung; Anzahl historischer Datensätze, die nach einem Rollover nicht mehr abrufbar sind; Anzahl Historieneinträge eines gelöschten Mitglieds, aus denen sich die Person noch rekonstruieren lässt (Sollwert 0). |
| target_or_pass_condition | AC-027 als Pass/Fail mit Nullschwelle: aktive Besitzstände werden zurückgesetzt, historische Records bleiben vollständig abrufbar und nach Finalisierung fachlich unveränderbar — 0 unzulässige nachträgliche Änderungen im Zwei-Season-Integrationstest. Zulässige Ausnahmen sind ausschließlich Löschung, Anonymisierung und rechtliche Korrektur (CONTRA-005). **CONTRA-005:** `status: resolved` · `evidence_status: pending` · `blocking: true` (Scope `database-schema-finalization`, `account-release`; `evidence_gate` B) — der frühere Widerspruch zu REQ-017 und NFR-006 ist inhaltlich geklärt; die Implementierungs-Evidence steht aus. Die Länge einer Season ist in keinem Artefakt definiert (**MISSING**) — ohne sie ist kein reales Messfenster ableitbar. |
| measurement_window | Zwei vollständige Season-Zyklen im Integrationstest (EV-027); die reale Zyklusdauer ist MISSING und muss vor der Feldmessung entschieden werden. |
| evidence_source | EV-027 (Zwei-Season-Integrationstest, Prüfung der fachlichen Unveränderbarkeit nach Finalisierung und Nachweis, dass Löschung und Anonymisierung als zulässige Ausnahmen korrekt greifen); Mindestklasse `real-boundary-smoke` — Season-Rollover hängt an echten Transaktionen und Constraints. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. OQ-009 (Datenretention) ist für die Ausnahmefälle zusätzlich offen. |
| release_gate | GATE-D |
| rationale | Der prüfbare Kern ist eine Datenintegritätsgarantie — Rücksetzumfang und Unveränderbarkeit nach Finalisierung — und damit Betriebsqualität mit Nullschwelle. Das naheliegende Produktsignal Season-Teilnahme (CAN-129, VIS-006 Zeile D) misst das Territory-/Season-System als Ganzes und wird deshalb bei REQ-026 geführt; ein korrekter Rollover allein kann es weder belegen noch widerlegen. `source_type` MISSING wegen der unbestimmten Seasonlänge. **Sportgetrennte Messung requirement-spezifisch nicht anwendbar:** der Rollover wirkt auf Besitzstände und Snapshots, die selbst keine Sportart tragen; sportgetrennt sind nur die darin gespeicherten Rekorde, je Sportart stichprobenartig zu belegen. |

Canvas: CAN-066, CAN-030 · Vision: VIS-004

### REQ-028 — Deterministische Einzel-Reviere

| Feld | Wert |
|---|---|
| measurement_type | **RESEARCH_HYPOTHESIS** |
| signal | Aus Geo-Fixture-Suite und Property-Tests: Determinismus (identisches Eingabeset erzeugt identische Geometrie und identischen Besitzer), Ablehnungsrate für reale Drift- und Linien-Tracks, Verhalten bei Überlappung, Teilübernahme, Restflächen und Gleichständen, Rechenzeit je Flächenoperation bei realer Track-Länge. Run und Bike getrennt, weil Rundenlänge, Kurvenradien und Geschwindigkeit die Rundenerkennung und die Anfahrtssegmentierung unterschiedlich belasten. |
| target_or_pass_condition | AC-028 qualitativ EXPLICIT: dasselbe Eingabeset erzeugt dieselbe Geometrie und denselben Besitzer; Linien- und Drift-Tracks werden abgelehnt. Numerische Schwellen für Rundenerkennung, Mindestfläche, Toleranzen und Gleichstandsauflösung sind **MISSING** (OQ-008). Zusätzliche Freigabebedingung aus dem REQ selbst: bestandene Simulation **und** Threat-Model — vor beidem kein produktiver Rollout. ASM-104 hält Einzel-Reviere bis Stufe D deaktiviert. |
| measurement_window | Property- und Fixture-Läufe bei jedem CI-Durchlauf; Simulations- und Threat-Model-Abnahme vor Gate D; reale Drift-Tracks je Sportart vor der Freischaltung. |
| evidence_source | EV-028 (Geo-Fixture-Suite, Property-Tests und Threat-Model); Mindestklasse `real-boundary-smoke` — die Geometrie ist deterministisch prüfbar, aber die Ablehnung von Linien-/Drift-Tracks braucht reale Drift-Tracks. RISK-016 (Einzel-Reviere verraten Wohnort und Routine) ist kritisch und offen. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Rollenreferenz „Product/Data" gehört zu OQ-008; das Threat-Model braucht zusätzlich eine Privacy-Verantwortung, die nicht benannt ist. |
| release_gate | GATE-D |
| rationale | Einzel-Reviere und Revier-Geometrie sind unvalidiert. Der Determinismus ist formal prüfbar, aber alle Parameter, die ihn erst definieren, fehlen — deshalb `source_type` MISSING. |

**research_plan** — *Hypothese:* Rundenerkennung, Anfahrtssegmentierung, Übernahmepriorität und Polygon-Union/-Differenz lassen sich so definieren, dass dasselbe Eingabeset immer dieselbe Geometrie und denselben Besitzer erzeugt und Linien-/Drift-Tracks zuverlässig abgelehnt werden. *Plan:* Stufe 1 Geometrie- und Prioritätsregeln vollständig spezifizieren inklusive Gleichstand und Restflächen. Stufe 2 Property-Tests auf Determinismus und Idempotenz über generierte Geometrien. Stufe 3 reale Drift- und Linien-Tracks je Sportart gegen den Ablehnungspfad laufen lassen. Stufe 4 Threat-Model zu Wohnort- und Routinepreisgabe (RISK-016) mit Anonymisierung, Start-/End-Unschärfe und Retention. *Fixtures/reale Daten:* Geo-Fixture-Suite mit generierten Grenzfällen plus reale Aufzeichnungen mit Drift, Tunnelverlust und Linienverhalten je Sportart; ohne reale Drift-Tracks ist die Ablehnungsaussage nicht belastbar. *Entscheidungsschwelle:* **MISSING** — Mindestfläche, Rundenkriterium, Toleranzen und Gleichstandsregel unbeziffert (OQ-008); zusätzlich fehlt eine Schwelle für die zulässige Preisgabe von Wohnumfeldinformationen. *Konsequenz bei unzureichender Evidenz:* Einzel-Reviere bleiben deaktiviert; bei nicht bestandener Simulation oder nicht bestandenem Threat-Model erfolgt keine Freischaltung, auch nicht in Stufe D.

Canvas: CAN-065, CAN-106, CAN-105, CAN-078 · Vision: VIS-008  
**Canvas-BLOCKER (mehrfach):** (1) CAN-021 (Problem hinter Einzel-Revieren und Sportplatz-Challenges) ist `reserved` und inhaltlich MISSING. (2) Keine CAN-003-Nachfolgeklausel deckt Einzel-Reviere — CAN-032 fordert ausdrücklich Gemeinschaft, Einzel-Reviere sind per Definition nicht gemeinsam. (3) Kein Erfolgssignal: CAN-124…CAN-129 kennen kein Einzel-Revier-Signal. Das REQ hängt damit nur an der Capability CAN-065 und an Risiko-Items.

### REQ-029 — Sportplatz-Challenges und Bahngold-Score

| Feld | Wert |
|---|---|
| measurement_type | **RESEARCH_HYPOTHESIS** |
| signal | Aus realem Bahn-Test und OSM-Access-Review: Erkennungsrate vollständiger Runden und Falsch-Positiv-Rate unter realem GPS-Rauschen auf einer echten Bahn, Anteil kuratierter Anlagen mit korrektem Zugangs- und Öffnungsstatus, Anzahl gesperrter oder privater Anlagen, die dennoch als Challenge-Ort erscheinen, sowie der Nachweis über Reward-Fixtures, dass Bahngold weder Effort- noch Territory-Wertung verändert. |
| target_or_pass_condition | AC-029 qualitativ EXPLICIT mit zwei Nullschwellen: 0 geschlossene oder private Anlagen erscheinen als Challenge-Ort, und Bahngold verändert in 0 Fällen eine Effort- oder Territory-Wertung (nicht übertragbarer Progressions-Score, keine Währung). GPS-Toleranz, Rundenkriterium und Bahngold-Startwerte sind **MISSING** (OQ-008). Die **Bike-Anwendbarkeit ist laut `docs/traceability.md` eine OPEN QUESTION** und wird hier ausdrücklich nicht durch eine Annahme geschlossen. RISK-019 (Bahngold fördert gesundheitlich riskantes Grinding) verlangt zusätzlich eine Degressions- und Limitregel, die in keinem Artefakt beziffert ist. |
| measurement_window | Bahn-Testläufe vor Gate D auf mindestens einer realen Anlage; OSM-Access-Review je Kuratierungsdurchlauf; Reward-Fixtures bei jedem CI-Lauf. Ein Überwachungsintervall für den Zugangsstatus kuratierter Anlagen ist nicht dokumentiert — offen zu entscheiden, nicht zu raten. |
| evidence_source | EV-029 (OSM-Access-Review, realer Bahn-Test und Reward-Fixtures); Mindestklasse `production-verified` — GPS-tolerante Rundenerkennung auf einer realen Bahn ist eine Feldmessung. RISK-018 (OSM-Sportplatz ist privat oder falsch) und RISK-019 sind offen. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Rollenreferenz „Product/Data" gehört zu OQ-008; für Kuratierung, Sperrliste und Meldesystem existiert **keine** benannte Betriebsverantwortung. |
| release_gate | GATE-D |
| rationale | Bahngold ist ein unvalidiertes Progressionssystem. Die Wirkungslosigkeit von Bahngold auf Effort und Territory wird als harte Nullschwelle gemessen, weil sie die Fairnesszusage schützt. Die Bike-Anwendbarkeit wird ausdrücklich offen gehalten statt als „nicht relevant" abgetan: eine Bahn ist eine Laufanlage; ob es eine Rad-Entsprechung geben soll, ist eine dokumentierte offene Produktfrage, keine Ableitung. |

**research_plan** — *Hypothese:* Auf kuratierten, öffentlich zugänglichen Sportanlagen lassen sich vollständige Runden GPS-tolerant so validieren, dass nur plausible Runden zählen; Bahngold bleibt dabei ein nicht übertragbarer Progressions-Score ohne Effort- oder Territory-Wirkung. *Plan:* Stufe 1 Kuratierungs- und Sperrlistenprozess samt Access-/Opening-Hours-Auswertung definieren. Stufe 2 realer Bahn-Test mit wiederholten Runden zur Bestimmung von Erkennungs- und Falsch-Positiv-Rate. Stufe 3 Reward-Fixtures, die belegen, dass Bahngold keine andere Wertung beeinflusst. Stufe 4 Degressions-/Limitregel gegen Grinding (RISK-019) festlegen und prüfen. *Fixtures/reale Daten:* reale Rundenaufzeichnungen auf mindestens einer echten Bahn unter unterschiedlichen Empfangsbedingungen; OSM-Daten mit Zugangsattributen; Reward-Fixtures für die Wirkungslosigkeitsprüfung. *Entscheidungsschwelle:* **MISSING** — weder GPS-Toleranz noch Rundenkriterium noch Bahngold-Startwerte noch eine Degressionsregel sind beziffert (OQ-008, RISK-019). *Konsequenz bei unzureichender Evidenz:* Sportplatz-Challenges und Bahngold bleiben deaktiviert; ohne verlässlichen Zugangsstatus wird keine Anlage freigeschaltet.

Canvas: CAN-107, CAN-110, CAN-030 · Vision: VIS-004  
**Canvas-BLOCKER (stärkster im gesamten Requirement-Bestand):** (1) CAN-021 ist `reserved` und inhaltlich MISSING. (2) Es existiert **kein** atomares Capability-Item für Sportplatz-Challenges oder Bahngold — der Capability-Block CAN-047…CAN-070 nennt weder das eine noch das andere (der frühere Bereichsendpunkt CAN-071 ist deprecated; seine wirksamen Nachfolger **CAN-138, CAN-139, CAN-142 und CAN-143** betreffen Verlauf, GPX-Export, Streckenwiederverwendung und Aktivitätsvergleich und ändern diesen Befund nicht — CAN-140 ist am 2026-07-20 selbst deprecated worden); CAN-061 (Challenges) trägt laut Registry REQ-025, nicht REQ-029. (3) Kein Erfolgssignal. Es bleiben nur die beiden Risiko-Items CAN-107/CAN-110 und die schwache Wertklausel CAN-030. Eine Zuordnung wurde nicht erfunden.

### REQ-030 — Live-Map und Beschützer-Modus

| Feld | Wert |
|---|---|
| measurement_type | **COMPLIANCE_CONTROL** |
| signal | Kontrollierter Nachweis über die Endpfad-Matrix: Anteil der Endpfade (reguläres Beenden, Zeitablauf, App-Kill, Netzverlust, Blockierung, Not-Aus, Geräteausfall), in denen die Live-Freigabe nachweislich endet; Anzahl Fälle, in denen unberechtigte oder blockierte Personen Standort sehen; Nachweis der Start- und Endpunktverschleierung; Sichtbarkeit des aktiven Freigabestatus in der App; Anteil Beschützer-Links, die nicht automatisch enden. |
| target_or_pass_condition | AC-030 als Pass/Fail: in jedem Pfad endet die Freigabe — 100 % der Endpfad-Matrix; 0 Standortsichtbarkeit für Unberechtigte und Blockierte; 0 Beschützer-Links ohne automatisches Ende. Der maximal zulässige Freigabezeitraum und der Verschleierungsradius sind in keinem Artefakt beziffert: **MISSING**; OQ-009 (Datenretention für GPS, Health und Live) ist offen. |
| measurement_window | Vor Gate D und danach bei jeder Änderung an Freigabe, Realtime-Zustellung oder Blockierlogik; jede Zeile der Endpfad-Matrix einzeln, je Plattform. Penetrationstest je Release-Stufe ab D. |
| evidence_source | EV-030 (Threat-Model, Endpfad-Matrix und Penetrationstest); Mindestklasse `production-verified` — jeder Endpfad inklusive App-Kill, Netzverlust und Not-Aus ist nur real nachweisbar, ein Fake beweist die Beendigung nicht. RISK-015 (Standortfreigabe ermöglicht Stalking) ist kritisch und offen. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — 100-%-Endpfad-Matrix und die Nullschwellen sind analytisch; die Anforderung selbst ist unbelegt. **Die beiden einzigen bezifferbaren Werte fehlen:** maximal zulässiger Freigabezeitraum und Verschleierungsradius sind MISSING (OQ-009). Ohne sie sind „zeitlich begrenzt“ und „verschleiert“ nicht prüfbar. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Zusätzlich offen: OQ-009 („Privacy/Product") für Freigabedauer und Retention. |
| release_gate | GATE-D |
| rationale | Live-Standortfreigabe ist ein Standortfreigabe- und Security-Kontrollfall. **Kein Nutzersignal, requirement-spezifisch begründet:** eine Nutzungsquote der Live-Freigabe wäre als Ziel sogar schädlich, weil das Produkt keine Anreize zur Standortpreisgabe setzen darf; entscheidend ist ausschließlich, dass jeder Endpfad hält. **Sporttrennung nur mittelbar:** Freigabe, Beendigung und Verschleierung hängen an Aktivität und Kontakt, nicht an der Sportart; die Endpfad-Matrix wird trotzdem einmal je Sportart durchlaufen, weil Aktivitätsdauer und Netzabdeckung bei Bike typischerweise größere Distanzen umfassen. |

Canvas: CAN-068, CAN-105, CAN-037, CAN-031 · Vision: VIS-009  
**Canvas-BLOCKER (doppelt):** (1) CAN-017 (Sicherheitsproblem) ist `reserved` und inhaltlich MISSING — der Canvas nennt kein Sicherheitsproblem, VIS-003 dagegen „sicheren Zugang"; dokumentierte Canvas/Vision-Divergenz. (2) CAN-031 („Trainiere sicherer") lässt laut Canvas offen, ob Trainings- oder Datensicherheit gemeint ist — die Klausel ist bis zur Klärung nicht prüfbar und trägt REQ-030 deshalb nur vorbehaltlich.

### REQ-031 — Sturzerkennung als Assistenz

| Feld | Wert |
|---|---|
| measurement_type | **RESEARCH_HYPOTHESIS** |
| signal | Aus kontrollierten Falltests und späterem Feldbetrieb: Fehlalarmquote pro Aktivitätsstunde, Nichterkennungsrate in kontrollierten Falltests, Anteil Countdowns, die vom Nutzer abgebrochen werden, Anzahl Fälle, in denen ein Kontakt ohne abgelaufenen Countdown informiert wurde. Run und Bike getrennt, weil Sturzsignatur, Beschleunigungsprofil und typische Geschwindigkeit sich erheblich unterscheiden — ein gemeinsamer Schwellwert wäre für mindestens eine der beiden Sportarten falsch. |
| target_or_pass_condition | Kontrollteil EXPLICIT als Pass/Fail: sichtbarer Countdown, jederzeit abbrechbar, Kontakt wird erst danach informiert — 0 vorzeitige Benachrichtigungen. Die Entscheidungsschwelle für die Fehlalarmquote ist **MISSING**: kein Artefakt beziffert eine akzeptable Quote, das REQ verlangt nur ihre Dokumentation. Ohne entschiedene Schwelle darf die Funktion nicht freigeschaltet werden — RISK-020 (Sturzerkennung erzeugt falsche Sicherheit) ist kritisch und CAN-073 hält „keine garantierte Unfallhilfe" als Non-Goal fest. |
| measurement_window | Kontrollierte Falltests je Sportart vor Gate D; Fehlalarmquote fortlaufend je Aktivitätsstunde im Feld erhoben und je Release-Stufe berichtet. |
| evidence_source | EV-031 (kontrollierte Falltests, Fehlalarmstatistik und Claims-Review); Mindestklasse `production-verified` — kontrollierte Falltests und die dokumentierte Fehlalarmquote sind reine Feldnachweise. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Die Entscheidung über eine akzeptable Fehlalarmquote ist zugleich eine Haftungs- und Claim-Entscheidung; OQ-006 („Product/Legal") ist offen. |
| release_gate | GATE-D |
| rationale | Der Detektor ist ein unvalidiertes System mit einer Schwelle, die niemand festgelegt hat — deshalb RESEARCH_HYPOTHESIS und nicht COMPLIANCE_CONTROL, obwohl der Countdown-Teil ein reiner Kontrollnachweis ist. **Kein Nutzersignal, requirement-spezifisch begründet:** eine Nutzungs- oder Auslösequote als Ziel wäre pervers, weil jede Auslösung ein unerwünschtes Ereignis ist. Ohne bezifferte Schwelle bleibt die Funktion aus — das ist die dokumentierte Konsequenz, keine Vertagung. |

**research_plan** — *Hypothese:* Ein Sturzmuster lässt sich aus Sensordaten je Sportart so erkennen, dass die dokumentierte Fehlalarmquote niedrig genug ist, um die Funktion als reine Assistenz ohne Sicherheitsgarantie anzubieten. *Plan:* Stufe 1 akzeptable Fehlalarmquote je Sportart entscheiden lassen (heute MISSING). Stufe 2 kontrollierte Falltests mit dokumentiertem Protokoll je Sportart. Stufe 3 Feldmessung der Fehlalarmquote pro Aktivitätsstunde über eine definierte Beobachtungsperiode. Stufe 4 Claims-Review der Assistenzsprache gegen CAN-073 und RISK-020 vor jeder Freischaltung. *Fixtures/reale Daten:* kontrollierte, protokollierte Sturzversuche je Sportart plus reale Aktivitätsstunden ohne Sturz als Negativkorpus; synthetische Sensordaten reichen weder für die Erkennungs- noch für die Fehlalarmaussage. *Entscheidungsschwelle:* **MISSING** — kein Artefakt beziffert eine akzeptable Fehlalarm- oder Nichterkennungsrate; vor Gate D gemeinsam mit der Claim-Freigabe zu entscheiden. *Konsequenz bei unzureichender Evidenz:* die Sturzerkennung bleibt vollständig deaktiviert; eine Teilaktivierung mit unbekannter Fehlalarmquote ist ausgeschlossen, weil sie genau die Sicherheitserwartung erzeugt, die CAN-073 verbietet.

Canvas: CAN-068, CAN-073, CAN-031 · Vision: VIS-007  
**Canvas-BLOCKER:** CAN-017 ist `reserved` und inhaltlich MISSING — kein atomarer Canvas-Problembezug. CAN-031 trägt nur vorbehaltlich, weil „sicherer" im Canvas undefiniert ist.

### REQ-032 — Wearables und Bike-Sensorik

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | Sync-Konsistenz zwischen Wearable/Sensor und Telefon: Abweichung der Kernmetriken (Dauer, Distanz, Herzfrequenz, bei Bike zusätzlich Trittfrequenz und Geschwindigkeit) zwischen den Geräten, Anteil Start-/Stopp-Kommandos, die auf beiden Seiten denselben Zustand erzeugen, Verbindungsabbruchrate je Gerätekombination, Anzahl im Release freigeschalteter Kombinationen ohne Eintrag in der Kompatibilitätsmatrix. Getrennt geführt: Apple Watch und Wear OS im Run-Fall, Bike-Sensorik im Ride-Fall — die Gerätematrix ist damit selbst sportspezifisch. |
| target_or_pass_condition | AC-032 als Pass/Fail: Status und Messwerte bleiben zwischen Geräten konsistent, nicht unterstützte Kombinationen sind klar benannt, und 0 Kombinationen werden ohne Eintrag in der dokumentierten Kompatibilitätsmatrix freigeschaltet. Eine zulässige numerische Metrikabweichung zwischen Geräten ist **MISSING** — ohne Toleranz ist „konsistent" nicht verifizierbar. OQ-003 (Minimum iOS/Android und Referenzgeräte) ist offen; ohne Gerätefestlegung ist die Matrix nicht abschließbar. |
| measurement_window | Je Gerätekombination mindestens ein vollständiger Aktivitätsdurchlauf vor Gate E; Wiederholung bei jedem OS- oder Firmware-Sprung einer gelisteten Kombination. |
| evidence_source | EV-032 (Gerätematrix und reale Integrationstests); Mindestklasse `production-verified` — Apple Watch, Wear OS und Bike-Sensorik sind ausschließlich mit echter Hardware belegbar. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Rollenreferenz „Engineering/QA" gehört zur gekoppelten Frage OQ-003. |
| release_gate | GATE-E |
| rationale | REQ-032 misst Synchronisationsqualität und Geräteabdeckung, also Betriebsqualität — nicht Wearable-Guidance (das wäre REQ-033, Coach). Deshalb OPERATIONAL_QUALITY statt RESEARCH_HYPOTHESIS. `source_type` MISSING, weil die zulässige Metrikabweichung nirgends beziffert ist und OQ-003 die Geräteliste offen lässt. |

Canvas: **CAN-022** (Problem), CAN-069, CAN-052, CAN-137 · Vision: **MISSING** · Persona: **USER-004** (primär)

**Primäre Verankerung hergestellt (2026-07-19).** REQ-032 ist nach der Nutzerentscheidung primär verankert an **USER-004**, **CAN-022** und einem Vision-Item zu vollständigen und erklärbaren Trainingsdaten. Zwei der drei Anker existieren jetzt, der dritte nicht:

| Anker | Stand |
|---|---|
| Persona **USER-004** | **vorhanden**, `source_type` ASSUMPTION (unbestätigt) |
| Canvas-Problem **CAN-022** | **vorhanden und inhaltlich entschieden**, `source_type` ASSUMPTION |
| Vision-Item „vollständige und erklärbare Trainingsdaten" | **MISSING — BLOCKER** |

**CAN-022 — Canvas-BLOCKER geschlossen.** ~~CAN-022 ist `reserved` und inhaltlich MISSING~~ → `active`, Wortlaut: *„Ohne Anbindung bereits genutzter Sportuhren und externer Sensoren fehlen oder verschlechtern sich zentrale Trainingssignale wie Herzfrequenz, Kadenz, Geschwindigkeit, Leistung und Höheninformationen. Dadurch werden Belastungsanalyse, sportartspezifische Auswertung und erklärbare Empfehlungen weniger vollständig und weniger zuverlässig."* Item Type **PROBLEM** · Anker REQ-032/AC-032 · Release Gate **E** · `source_type` **ASSUMPTION**. Der Wearable-Bezug erscheint damit erstmals als **Problem** und nicht nur als Capability (CAN-069).

**Ausdrücklich NICHT in CAN-022 enthalten:** der Komfortaspekt *„Nutzer müssen zusätzlich das Telefon mitführen"*. Er ist nach der Nutzerentscheidung eine **separate mögliche Convenience-Aussage**, die in diesem Lauf **nicht** angelegt wird und deshalb **keine CAN-ID** erhält. Er wird hier weder stillschweigend in CAN-022 hineingelesen noch als abgedeckt behandelt — **OPEN QUESTION**.

**CAN-025 — Zielgruppen-BLOCKER geschlossen.** ~~CAN-025 ohne PRD-USER-ID~~ → **USER-004** vergeben. Für REQ-032 trägt die Verknüpfung **unmittelbar**: das Requirement handelt von Apple Watch, Wear OS und Bike-Sensorik, USER-004 ist über genau diesen Gerätebesitz definiert.

⚠️ **BLOCKER — kein Vision-Anker.** Kein VIS-Item trägt die Aussage „vollständige und erklärbare Trainingsdaten". Die Prüfung ergab: **VIS-005** (das bisher hier geführte Item) betrifft Gerätezuverlässigkeit, nicht Vollständigkeit und Erklärbarkeit der Trainingsdaten; **VIS-007** betrifft die **Erklärbarkeit der Health-Auswertung**, nicht die **Vollständigkeit der Signalbasis**. Beide sind Beinahe-Treffer und werden **nicht umgedeutet** — das wäre derselbe Defekt wie VIS-009 ↔ REQ-014. Anders als bei REQ-038 und REQ-039 ist für diesen Fall **nicht einmal eine VIS-ID reserviert**; es ist eine **MISSING**-Position, keine reservierte Leerstelle.

⚠️ **BLOCKER — beide vorhandenen Anker sind unbestätigt.** USER-004 und CAN-022 tragen `source_type` **ASSUMPTION**. Die Verankerung ist damit hergestellt, aber nicht belegt.

### REQ-033 — Coach, Recovery, Wetter und Zyklus unter Claims-Gate

| Feld | Wert |
|---|---|
| measurement_type | **RESEARCH_HYPOTHESIS** |
| signal | Vor dem Gate ausschließlich Kontroll- und Forschungssignale, kein Nutzersignal: Anteil erzeugter Empfehlungen, die vollständig auf die freigegebene Claims-Whitelist abbilden (Claims-Lint), Anteil Empfehlungen mit ausgewiesener Datenbasis, Gründen und Grenzen, Anzahl Ausgaben nach einem Opt-out, Vorliegen von Rechtsfreigabe und Privacy-Review als dokumentierte Kontrollnachweise. Nach dem Gate zusätzlich die Regelgüte gegen reale Verlaufsdaten, getrennt für Run und Bike, weil Regenerationsbedarf und Hitze-/Trinkempfehlung an sportspezifischer Belastungsdauer und Intensität hängen. |
| target_or_pass_condition | Freigabebedingung EXPLICIT als Pass/Fail mit Nullschwelle: ohne juristische Claims- und Privacy-Freigabe erscheint keine dieser Funktionen — 0 sichtbare Empfehlungen vor der Freigabe; 0 Ausgaben nach Opt-out. Die Whitelist selbst ist **MISSING** (OQ-006), damit ist die inhaltliche Prüfschwelle heute nicht bezifferbar. **Zusätzlicher offener BLOCKER:** Zyklusdaten sind eine besondere Datenkategorie ohne dokumentierte Rechtsgrundlage im Canvas. |
| measurement_window | Claims-Lint und Opt-out-Kontrolle bei jedem CI-Lauf; Rechtsfreigabe und Privacy-Review je Funktionsgruppe (Recovery, Coach, Hitze/Trinken, Zyklus) einzeln vor Gate E; Regelgüte nach Freischaltung je Vier-Wochen-Fenster. |
| evidence_source | EV-033 (Claims-Lint, Rechtsfreigabe und Privacy-Test); Mindestklasse `real-boundary-smoke` für die regelbasierte Empfehlung samt Wetter-Netzwerkgrenze; die Freigabe selbst bleibt ein separater, dokumentierter Rechtsnachweis. RISK-008 (Health-Score als medizinische Aussage) und RISK-022 (sensitive Health-Daten serverseitig) sind offen. |
| source_type | **MISSING** |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Rollenreferenz „Product/Legal" gehört zur gekoppelten Frage OQ-006. Für Zyklusdaten fehlt zusätzlich eine benannte Privacy-Verantwortung. |
| release_gate | GATE-E |
| rationale | Recovery- und Coach-Regeln sind unvalidiert und zugleich rechtlich gesperrt. **Kein Nutzersignal vor dem Gate, requirement-spezifisch begründet:** solange die Funktionen nicht erscheinen dürfen, kann es definitionsgemäß kein Nutzungssignal geben — ein Zielwert dafür wäre erfunden. `docs/traceability.md` führt REQ-033 bereits als `blocked`. |

**research_plan** — *Hypothese:* Regenerations-, Coach-, Hitze-/Trink- und Zyklusfunktionen lassen sich regelbasiert so formulieren, dass sie erklärbar, optional, vollständig deaktivierbar und juristisch freigegeben sind — ohne die Grenze zum Medizinprodukt (CAN-072) zu überschreiten. *Plan:* Stufe 1 Claims-Whitelist erstellen und rechtlich freigeben lassen (OQ-006). Stufe 2 Regelsatz je Funktionsgruppe gegen reale Verlaufsdaten prüfen, mit ausgewiesener Datenbasis und Unsicherheit. Stufe 3 Privacy-Review je Funktionsgruppe, für Zyklusdaten mit eigener Rechtsgrundlage. Stufe 4 Claims-Lint als CI-Regel, die jede nicht gelistete Formulierung blockiert. *Fixtures/reale Daten:* reale Belastungs-, Health- und Wetterverläufe über mindestens mehrere Wochen je Nutzer, getrennt nach Sportart; Fixture-Fälle für Grenzsituationen (Hitze, Übertraining, Datenlücken). *Entscheidungsschwelle:* **MISSING** — die Claims-Whitelist (OQ-006) existiert nicht, und für die Regelgüte ist keine Schwelle definiert; beides vor Gate E zu entscheiden. *Konsequenz bei unzureichender Evidenz:* alle vier Funktionsgruppen bleiben unsichtbar und deaktiviert; eine Teilfreischaltung ohne Rechtsfreigabe ist ausgeschlossen, CAN-137 sperrt nicht freigegebene medizinische Claims ausdrücklich.

Canvas: CAN-070, CAN-102, CAN-072, CAN-137, CAN-029 · Vision: VIS-007

### REQ-034 — Security, Datenschutz und Datenminimierung

| Feld | Wert |
|---|---|
| measurement_type | **COMPLIANCE_CONTROL** |
| signal | Kontrollierter Nachweis: Anteil Datenzugriffe, die durch Row-Level-Security-Tests abgedeckt sind; Anzahl Endpunkte ohne Rate Limit oder ohne serverseitige Validierung; Nachweis funktionierenden Datenexports und funktionierender Löschung; Anzahl Datenflüsse, in denen Roh-Health-Verläufe ohne nachgewiesene Notwendigkeit das Gerät verlassen; Bundle-Scan auf Secrets im Client, ab A0 einschließlich des Routing-Provider-Keys. Für den A0-Proxy zusätzlich: Anzahl Logeinträge, Traces oder Fehlermeldungen mit Koordinaten, Wegpunktlisten, Routengeometrien oder vollständigen Provider-URLs (Sollwert 0). |
| target_or_pass_condition | AC-034 als Pass/Fail mit 100-%-Abdeckung des Datenflussdiagramms und Nullschwellen: Zugriff folgt Berechtigung und Zweckbindung; 0 Secrets im Client (NFR-007, ab A0 auch für den Routing-Proxy-Key, CAN-092); 0 Endpunkte ohne Rate Limit und serverseitige Validierung; nicht benötigte sensible Daten verlassen das Gerät nicht; 0 Rohsensorserien im serverseitigen Standard-Payload (CONTRA-004); Retention für den Koordinaten-Payload Application 0, Cache 0, Analytics 0 (CONTRA-006). **CONTRA-006** trägt `status: resolved` · `resolution_status: accepted` · `evidence_status: pending` · `blocking: true` (Scope `field-test`, `release`; `evidence_gate` A0) — die Entscheidung ist getroffen, die Evidence (Log-Tests, Rate-Limit-Nachweis, Secret-Scan) steht aus und ist **blockierend** für die A0-Routing-Implementierung. Retentionsfristen im Übrigen sind **MISSING** (OQ-009). |
| measurement_window | Bundle-Scan und Proxy-Kontrollen bei jedem Build ab A0; RLS- und Rate-Limit-Tests bei jedem CI-Lauf ab Stufe B; Security-Review und Datenflussdiagramm vor jedem Gate von A0 bis E; Löschungsnachweis je Release-Stufe mit Accountfunktion; technische Proxy-Logs mit maximal 7 Tagen Aufbewahrung, sofern keine dokumentierte abweichende Notwendigkeit besteht. |
| evidence_source | EV-034 (Security-Review, RLS-Tests, Datenflussdiagramm und Löschungsnachweis); Mindestklasse `production-verified` — RLS, Rate Limits und Löschung sind nur gegen die echte Instanz beweisbar, ein Mock kann keine Policy widerlegen. RISK-007 (Client-API-Key wird missbraucht) und RISK-022 (sensitive Health-Daten serverseitig) sind offen. |
| source_type | **EXPLICIT** (Nachaudit 2026-07-19 **bestätigt** — klauselbeschränkt) — **die einzige der 17 Zeilen, die die Beweislatte hält.** Belegt sind: „0 Secrets im Client“ durch **DEC-005** (`user-confirmed` 2026-07-19), **CAN-092** (`CONFIRMED`) und SRC-006; „0 Rohsensorserien im serverseitigen Standard-Payload“ durch **DEC-011** / CONTRA-004; „Retention Application 0, Cache 0, Analytics 0“ durch **DEC-013** / CONTRA-006. Das ist keine Hochstufung, sondern die Wiedergabe protokollierter Nutzerentscheidungen. **Nicht mit hochgezogen:** Rate-Limit- und Timeout-Werte (MISSING — DEC-013 fordert sie und beziffert keine), Auth-Verfahren (MISSING), RLS (setzt OQ-005 voraus) und die übrigen Retentionsfristen (MISSING, OQ-009). |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Zusätzlich offen: OQ-005 („Engineering") für EU-Hosting und Backend, OQ-009 („Privacy/Product") für Retention. Für den A0-Routing-Proxy existiert **keine benannte Betriebsverantwortung**, obwohl er ab A0 personenbezogene Wegpunkte verarbeitet. |
| release_gate | GATE-A0 (Bundle-Scan, Secret- und Proxy-Kontrollen ab A0) und fortlaufend bis GATE-E |
| rationale | Datenschutz, Secret Management und Security sind Kontrollnachweise; sie brauchen bewusst **kein** Nutzersignal, weil die Wirksamkeit einer Zugriffsregel unabhängig davon ist, wie viele Nutzer sie berühren. **Sportgetrennte Messung der Zugriffsregeln requirement-spezifisch nicht anwendbar:** sie wirken datenbestandsweit — allerdings fällt bei Bike typischerweise mehr Sensorik an (REQ-024), weshalb die Datenminimierungsprüfung dennoch je Sportart einmal durchlaufen wird. |

Canvas: CAN-084, CAN-088, CAN-092, CAN-095, CAN-105 · Vision: VIS-009  
**Canvas-BLOCKER:** CAN-018 (Datenschutzproblem) ist `reserved` und inhaltlich MISSING — kein atomarer Canvas-Problembezug; Datenschutz erscheint nur als Constraint (CAN-088) und Risiko (CAN-105).

**Verhältnis zu REQ-039 (GPX-Export) — REQ-034 ist SEKUNDÄR, nicht primär.** Die Klausel „Datenexport" in REQ-034 wurde bisher stillschweigend so gelesen, als decke sie den Aktivitätsexport ab. Die Nutzerentscheidung vom 2026-07-19 stellt ausdrücklich fest: **REQ-034 ist KEIN ausreichend präziser primärer Anker.** Die Erwähnung „Datenexport" trägt die konkrete Capability „GPX-Datei erzeugen und extern öffnen" **nicht** — sie benennt weder ein Format noch eine Zielanwendung noch eine Prüfbedingung.

| Aspekt | Zuständigkeit |
|---|---|
| GPX erzeugen, Schemakonformität, Öffnen in einer Fremd-App | **REQ-039** (primär) · AC-039 · EV-039 |
| Nutzerkontrolle über den Export, Datenportabilität, Datenminimierung, **keine unbeabsichtigten Zusatzdaten** | **REQ-034** (sekundäre Constraint-Verknüpfung) |

Konkret wirkt REQ-034 auf AC-039 in den Kriterien **(e)** „keine Health-Daten unbeabsichtigt exportiert", **(f)** „der Nutzer sieht vor dem Export, welche Daten enthalten sind" und **(h)** „Export funktioniert ohne Veröffentlichung oder Social-Freigabe". **Es wird ausdrücklich nicht behauptet, REQ-034 allein erfülle den GPX-Export.**

### REQ-035 — Evidence Ledger und Definition of Done

| Feld | Wert |
|---|---|
| measurement_type | **COMPLIANCE_CONTROL** |
| signal | Kontrollierter Nachweis, bewusst ohne Nutzersignal: Anteil auf `done` gesetzter Tasks und Gates mit vollständigem Evidence-Ledger-Eintrag; Anzahl Ledger-Einträge, in denen bei sportabhängigen Requirements Run und Bike getrennt nachgewiesen sind; Anzahl CI-Läufe, in denen die Regel einen echten Verstoß blockiert hat; Anzahl Ledger-Einträge mit offenen Findings, die dennoch auf `done` stehen. |
| target_or_pass_condition | AC-035 als Pass/Fail mit 100-%-Abdeckung: kein Task und kein Gate erhält `done` ohne vollständigen Ledger-Eintrag mit automatisierten Tests, realen Gerätetests, getrenntem Run- und Bike-Nachweis, offenen Punkten und Messwerten; 0 Einträge auf `done` mit unbeantworteten Pflichtfeldern. Die CI-Regel muss in der echten Pipeline mindestens einen echten Verstoß blockiert haben, sonst ist sie unwirksam. |
| measurement_window | Je Task-Abnahme und je Gate, fortlaufend von P0 bis Gate E; CI-Regel bei jedem Pipeline-Lauf. |
| evidence_source | EV-035 (CI-Regel, Ledger-Review und Gate-Checkliste); Mindestklasse `real-boundary-smoke` — die CI-Regel muss in der echten Pipeline einen echten Verstoß blockieren, sonst ist sie nicht wirksam. Datei: `docs/EVIDENCE-LEDGER.md`. **BEFUND:** der Ledger enthält derzeit ausschließlich einen Template-Platzhalter mit REQ-000/AC-000/EV-000; diese sind **keine echten IDs** und müssen als Platzhalter kenntlich bleiben (`docs/ID-REGISTRY.md` §4), sonst erzeugt die Referenzprüfung Fehlalarme oder zählt drei Phantom-Requirements. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — 100-%-Ledger-Abdeckung und „0 Einträge auf `done` mit unbeantworteten Pflichtfeldern“ sind analytische Schranken. Die Anker **CAN-123** und **CAN-114** führen `EXPLICIT` mit Quelle **SRC-003 = nicht auffindbar (BLOCKER)**. Zusatzbefund: die Klausel „die CI-Regel muss mindestens einen echten Verstoß blockiert haben“ ist derzeit nicht erfüllbar — **es existiert keine CI im Repository**. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Gerade dieses REQ ist ohne benannten Abnehmer nicht durchsetzbar, weil `done` eine Personenentscheidung ist. |
| release_gate | GATE-A0 bis GATE-E (PRD Release A0-E), wirksam bereits ab P0 |
| rationale | REQ-035 ist ein Prozess- und Nachweisrequirement; sein Erfolg zeigt sich ausschließlich in kontrollierten Nachweisen. **Kein Nutzersignal, requirement-spezifisch begründet:** REQ-035 hat laut Canvas keinen unmittelbaren Nutzerkontakt und ist eine von genau zwei Prozessanforderungen ohne Nutzerproblem (Anker CAN-123); ein Retentions- oder Nutzungsziel für „Evidence-Ledger-Disziplin" wäre ein Kategorienfehler. **Sport-Nichtanwendbarkeit gilt hier gerade nicht:** der Ledger muss Run und Bike getrennt führen (CAN-114), das ist selbst Prüfgegenstand. |

Canvas: CAN-123, CAN-111, CAN-114, CAN-038 · Vision: VIS-010

### REQ-036 — Store- und Release-Gates

| Feld | Wert |
|---|---|
| measurement_type | **COMPLIANCE_CONTROL** |
| signal | Kontrollierter Nachweis, bewusst ohne Nutzersignal: Anteil Release-Stufen mit vollständig ausgefüllter Policy-Matrix für iOS und Android; Vorliegen der Berechtigungsbegründungen für Background-Location und Health; Vollständigkeit der Datenschutzangaben im Store-Eintrag; Nachweis eines durchlaufenen Testtracks (TestFlight beziehungsweise Play Internal); Vorliegen des Gate-Sign-offs der vorherigen Stufe; Anzahl Store-Ablehnungen und deren Gründe. |
| target_or_pass_condition | AC-036 als Pass/Fail mit 100-%-Abdeckung: kein Release ohne vollständige Nachweise und Policy-Abnahmen; jede Stufe startet erst nach dem Sign-off des vorherigen Gates — 0 übersprungene Gates. Für GATE-A2 zusätzlich blockierend: der finale öffentliche Name ist **MISSING** (OQ-001), CAN-090 verlangt die Markenprüfung vor der Finalisierung. |
| measurement_window | Je Release-Stufe vor Veröffentlichung (A0, A1, A2, B, C, D, E); Policy-Matrix zusätzlich bei jeder Änderung an Berechtigungen oder Datenkategorien. |
| evidence_source | EV-036 (TestFlight-/Internal-Test-Bericht, Policy-Matrix und Gate-Sign-off); Mindestklasse `production-verified` — Testtracks und die Review-Entscheidung sind externe Realbedingungen. RISK-010 (Store lehnt Background-Location/Health/UGC ab) ist kritisch und offen; RISK-011 (Namens-/Markenkollision) ebenfalls. |
| source_type | **ASSUMPTION** (Nachaudit 2026-07-19, vorher EXPLICIT) — **„genannt“ ist nicht „zitiert“.** Store-Policies von Apple und Google **wären** als verbindliche Plattformvorgabe eine zulässige EXPLICIT-Quelle, aber die Beweislatte verlangt eine **konkrete Zitierung**: weder Policy-Klausel noch Fassung noch Abrufdatum sind in irgendeinem Artefakt benannt. Dieselbe Lücke wie bei „WCAG AA“ in NFR-005. Die Pass-Bedingung selbst (100 % Abdeckung, 0 übersprungene Gates) bleibt prüfbar. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Zusätzlich offen: OQ-001 (öffentlicher Name, „Product/Legal") blockiert GATE-A2. Ein Gate-Sign-off ohne benannten Zeichnungsberechtigten ist nicht erteilbar. |
| release_gate | GATE-A0 bis GATE-E (PRD Release A0-E); jede Stufe ist ihr eigener Prüfpunkt |
| rationale | Store- und Release-Gates sind ein klassischer Compliance-Kontrollfall. **Kein Nutzersignal, requirement-spezifisch begründet:** REQ-036 ist die zweite der beiden Prozessanforderungen ohne unmittelbares Nutzerproblem (Anker CAN-083); Downloads oder Bewertungen als Zielwert wären ein Kategorienfehler, weil sie über die Policy-Konformität nichts aussagen. Die Sporttrennung bleibt mittelbar relevant, weil die Gate-Exit-Evidenz laut PRD reale Run- und Bike-Aktivitäten je Plattform verlangt. |

Canvas: CAN-083, CAN-108, CAN-085, CAN-086, CAN-122, CAN-038 · Vision: VIS-010

### REQ-037 — Accessibility

> **Nachfolger 1 von 2 für das deprecatete REQ-014.** Prüft ausschließlich die **Zugänglichkeit**. Die Gestaltungssprache liegt bei REQ-038.

| Feld | Wert |
|---|---|
| measurement_type | **COMPLIANCE_CONTROL** (Item Type: CONSTRAINT / COMPLIANCE_CONTROL) |
| signal | Kontrollierter Nachweis, bewusst ohne Nutzersignal: Anteil ausgelieferter Screens der mobilen App, die die dokumentierte Kontrastprüfung bestehen; Anteil Screens mit vollständiger Screenreader-Bedienbarkeit **getrennt für VoiceOver (iOS) und TalkBack (Android)**; Anteil Screens, die bei aktivem Dynamic Type bzw. Font Scaling ohne Abschneiden oder Überlappung bedienbar bleiben; Anzahl Informationen, die **ausschließlich** durch Farbe transportiert werden; Vollständigkeit und Korrektheit der Fokusführung. ⚠️ **Web-Erstreckung entfernt 2026-07-20** (vorher „…der mobilen App **und aller nutzbaren Web-Auskopplungen**"). Die Messgröße **Fokusführung** bleibt stehen, obwohl sie in keiner der vier Quellen vorkommt — sie ist als `ASSUMPTION`-Anteil offengelegt, nicht gestrichen (Nutzerauftrag Schritt 3). |
| target_or_pass_condition | AC-037 als Pass/Fail mit 100-%-Abdeckung und Nullschwelle — **alle fünf Bedingungen einzeln**: (a) **WCAG-2.2-AA-Audit bestanden** · (b) relevante Screens mit **VoiceOver UND TalkBack** geprüft — beide, nicht „ein Screenreader" · (c) **Dynamic Type** bzw. Font Scaling geprüft · (d) **0** Informationen ausschließlich durch Farbe · (e) **dokumentierte** Kontrastprüfung. Kein Prozentziel unterhalb von 100: die Anforderung ist eine **Schranke, keine Quote**. |
| measurement_window | Kein zeitbasiertes Fenster — vollständige Abdeckungsprüfung je ausgeliefertem Screen. **Accessibility-Basis ab GATE-A0**, **vollständiger Audit spätestens GATE-A2** vor öffentlichem Store-Release; zusätzlich bei jeder Änderung an Navigationsstruktur, Kontrastwerten oder Screenreader-Labels. iOS und Android **getrennt**, Light und Dark Mode **getrennt**. |
| evidence_source | **EV-037** (WCAG-2.2-AA-Audit, VoiceOver- und TalkBack-Durchlauf je Plattform, Dynamic-Type-/Font-Scaling-Prüfung, dokumentierte Kontrastprüfung); Mindestklasse `real-boundary-smoke` — Screenreader, Dynamic Type und Kontrast sind **ausschließlich real** prüfbar, ein Snapshot-Test kann Bedienbarkeit nicht belegen. `evidence_status` **`not-planned`**: es existiert kein Code, keine CI und kein beauftragter Auditor, also noch kein Messkonzept. |
| source_type | **ASSUMPTION.** Die WCAG-**Fassung** ist seit dem 2026-07-19 mit **2.2** beziffert (CAN-099) — die frühere Lücke „WCAG AA ohne Version" ist damit geschlossen und ein Audit überhaupt erst bestehbar. `EXPLICIT` wird trotzdem **nicht** vergeben: die Beweislatte verlangt eine **konkret zitierte** verbindliche externe Regel, und es ist in keinem Artefakt eine **Rechtsgrundlage** benannt, die WCAG 2.2 AA für dieses Produkt verbindlich macht (kein Verweis auf EAA, BFSG oder eine Store-Vorgabe). Zusätzlich ist der Wortlaut des Requirements nicht ausdrücklich nutzerbestätigt. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Für einen externen WCAG-Audit ist zusätzlich **kein Auditor benannt**: MISSING. |
| release_gate | **GATE-A0** (Accessibility-Basis) bis **GATE-A2** (vollständiger Audit, spätestens vor öffentlichem Store-Release) |
| rationale | Accessibility ist ein kontrollierter Nachweis mit fester Schranke. **Kein Nutzersignal, requirement-spezifisch begründet:** eine Nutzungsquote von Screenreader-Nutzern könnte WCAG-Konformität weder belegen noch widerlegen und würde einen falschen Anreiz setzen — Verzicht auf Zugänglichkeit bei kleiner Nutzergruppe. **Run/Bike-Trennung anwendbar:** die sportspezifischen Tracking-Screens zeigen unterschiedliche Labels und Kernmetriken, also sind auch die Screenreader-Ausgaben verschieden und je Sportart zu prüfen. |

Canvas: **CAN-099** (kanonischer Accessibility-Anker) · NFR: **NFR-005** · Vision: **VIS-011** (Accessibility Boundary) — **unbestätigt** · AC-037 · EV-037 · TRC-037

**Kanonischer CAN-099-Wortlaut (verbindlich, 2026-07-20)** — Item Type **CONSTRAINT / VALUE BOUNDARY**, Source Type **EXPLICIT**, `measurement_type` COMPLIANCE_CONTROL, primäres Requirement **REQ-037**:

> „Die mobile Anwendung muss für Menschen mit unterschiedlichen visuellen, motorischen und assistiven Anforderungen bedienbar sein. Dazu gehören WCAG 2.2 AA, Screenreader-Unterstützung, skalierbare Schrift, ausreichende Bedienflächen, nachvollziehbare Fokusführung und die Regel, dass Farbe niemals der einzige Informationsträger ist."

⚠️ **Nachzug 2026-07-20 — dieses Blockzitat ist gekürzt worden, und zwar nur an einer Stelle.** Der Halbsatz „**und ihre nutzbaren Web-Auskopplungen**" ist auf Nutzerauftrag (Schritt 3) entfernt. Alle übrigen Klauseln stehen **unverändert**, einschließlich der vier nicht quellengedeckten Anteile (Fassungsziffer **2.2**, **motorische/assistive Anforderungen**, **Bedienflächen**, **Fokusführung**) — sie bleiben `ASSUMPTION` und werden weder gestrichen noch hochgestuft. **Eigentumsvermerk:** kanonisch geführt wird CAN-099 in `docs/canvas/revyr-endurance-platform.canvas.md`; dieses PRD **zieht nach** und vergibt keine ID. Solange der Canvas-Owner die Kürzung nicht vollzogen hat, ist dieses Zitat **vorlaufend** — das ist offengelegt, nicht als erledigt behandelt. Die Kürzung ist nur dann defektfrei, wenn sie **atomar** über CAN-099, REQ-037, AC-037 (Given), NFR-005/REQ-037-`signal`, EV-037 (`docs/EVIDENCE-LEDGER.md`) und TRC-037 läuft; andernfalls trägt eine dieser Stellen eine Geltungsbereichsklausel ohne Anker. Innerhalb dieses PRD sind alle vier betroffenen Stellen synchron geändert.

**CAN-099 ist AUSSCHLIESSLICH Accessibility.** AC-037 und EV-037 prüfen ausschließlich Zugänglichkeit — **kein** Gestaltungs-, Ästhetik- oder Farbsemantikkriterium. Die Klausel „Farbe ist niemals der einzige Informationsträger" wird seit dem 2026-07-20 **kanonisch hier** geführt und **nicht mehr zusätzlich in CAN-141** (Auflösung der doppelt geführten Pflicht, siehe REQ-038).

**Keine neue CAN-ID vergeben — ausdrücklich gemeldete Abweichung.** Die Nutzeranweisung verlangte wörtlich, für die kanonische Accessibility-Aussage „die nächste tatsächlich freie CAN-ID zu reservieren". Das ist **nicht** geschehen: CAN-099 war bereits `active` und trug dieselbe Pflicht mit derselben Prüfrichtung und denselben Gates; der kanonische Text benennt zusätzlich die Zielgruppe und macht Schriftskalierung und Bedienflächen explizit — eine **Präzisierung derselben Aussage**, keine neue. Eine neue ID hätte eine **Dublette** erzeugt, also genau die Defektklasse, gegen die dieselbe Entscheidung an anderer Stelle die Regel aufstellt („nicht beide aktiv lassen"). Kanonisch entschieden in Registry §6.3.3; **der Nutzer kann die Abweichung überstimmen** — dann wäre CAN-099 zu deprecaten und eine neue ID zu vergeben.

**Trägt CAN-099 den Anker? — Belegprüfung gegen die Quelldokumente (2026-07-20).** Geprüft wurde nicht, ob der Wortlaut plausibel klingt, sondern ob jede Klausel in SRC-001 oder SRC-003 steht.

| Klausel in CAN-099 | Fundstelle | Verdikt |
|---|---|---|
| WCAG AA | SRC-001 §3.5 NFR „Accessibility": „**WCAG AA**-Kontraste…" · SRC-003 §2.4: „**WCAG-AA**-Kontraste…" · SRC-002 §10: „Accessibility (**WCAG AA**)" | **BELEGT** |
| WCAG-Fassung **2.2** | **in keiner Quelle.** Alle drei nennen „WCAG AA" **ohne Fassung** | **UNBELEGT** — bestätigt die bestehende Einstufung `ASSUMPTION`, jetzt quellenseitig statt nur analytisch |
| Screenreader-Unterstützung | SRC-001 §3.5: „Screenreader-Labels" · SRC-003 §2.4: „**VoiceOver/TalkBack**-Labels" · SRC-002 §10 Nachweis: „Screenreader-Check" | **BELEGT** — die Namen VoiceOver und TalkBack stehen wörtlich in SRC-003 |
| skalierbare Schrift | SRC-001 §3.5 und SRC-003 §2.4: „**Dynamic Type/Font Scaling**" | **BELEGT** |
| Farbe niemals einziger Informationsträger | SRC-001 §3.5: „**Farben nie einziger Informationsträger**" (generisch) | **BELEGT.** ⚠️ SRC-003 §2.4 sagt enger „**Teamfarben** nie einziger Informationsträger"; die generische Fassung trägt allein SRC-001 |
| dokumentierte Kontrastprüfung | SRC-001/SRC-003 nennen „Kontraste"; SRC-002 §10 nennt als Nachweis „Design-Token-Review + Screenreader-Check" | **TEILBELEGT** — Kontrast ja, „dokumentiert" ist Projektschärfung |
| ~~„und ihre nutzbaren **Web-Auskopplungen**"~~ **— Klausel am 2026-07-20 entfernt** | **keine Quelle erstreckt die Accessibility-Pflicht auf Web.** SRC-003 §2.1 (`docs/sources/SRC-003-…:83`) erstreckt ausschließlich die **Farbmisch-Regel** auf Web-Auskopplungen; §2.4 (Accessibility) tut das nicht | **UNBELEGT → Klausel gestrichen.** Der Weg „die Farbregel gilt für Web → also gilt Accessibility für Web" ist eine Ableitung über ein Zwischenglied und wird **nicht** gebaut. ⚠️ **Korrektur der früheren Begründung (2026-07-20):** Die Vorfassung stützte sich zusätzlich darauf, SRC-001 §2 führe „kein Web-Client" als Nicht-Ziel. **Dieses Argument trägt nicht und ist zurückgenommen.** Der Satz lautet vollständig „kein Web-Client **(außer Beschützer-Link)**" (`docs/sources/SRC-001-…:132`); die Ausnahme steht im selben Satz, und die Quellen planen das Artefakt ausdrücklich ein: SRC-001 L-03 „Beschützer-Modus: **Web-Link** für Vertrauensperson (ohne Account)" (`…SRC-001-…:238`), SRC-003 §2.1 benennt drei Web-Auskopplungen namentlich („Erfolgskarten-Renderer, **Beschützer-Web-Link**, Marketing-Seiten", `…SRC-003-…:83`). **Die Quellen verneinen den Prüfgegenstand also nicht** — der Defekt ist ein reiner **Belegmangel**, kein Richtungswiderspruch. Die Streichung bleibt davon unberührt; nur ihre Begründung ist korrigiert |
| „motorische… Anforderungen" · „ausreichende Bedienflächen" · „nachvollziehbare Fokusführung" | **in keiner der vier Quellen.** Volltextsuche über `docs/sources/` (2026-07-20, case-insensitiv): *Bedienfl* **0**, *touch target* **0**, *tap target* **0**, *motorisch* **0**, *assistiv* **0**, *barrierefrei* **0**. ⚠️ **Präzisierung 2026-07-20:** die Vorfassung führte auch *Fokus* mit „null Treffer" — das ist **zu weit**. *Fokus* hat **genau einen** Treffer, `docs/sources/SRC-001-…:52` „Leistungs**fokus**" in der Zielgruppenbeschreibung, **ohne** Accessibility-Bezug. Das Ergebnis ändert sich nicht, die Absenzbehauptung ist nur korrekt gefasst | **UNBELEGT** — Standardvokabular der Accessibility-Praxis, das hier als Quellenaussage durchginge. Bleibt im Wortlaut, bleibt `ASSUMPTION` (Nutzerauftrag Schritt 3) |

**Verdikt: CAN-099 trägt REQ-037.** Alle fünf Pass-Bedingungen von AC-037 sind quellenbelegt bis auf die Fassungsziffer „2.2". Der Anker ist damit **sauber verankert** und nicht erschlossen. **Aber der kanonische Wortlaut war an vier Stellen breiter als jede Quelle** (Fassung 2.2, Web-Auskopplungen, Bedienflächen, Fokusführung).

⚠️ **Zwei Sätze dieses Absatzes waren sachlich falsch und sind am 2026-07-20 korrigiert.** Die Vorfassung schloss: *„Diese vier stehen **nicht** in AC-037 und werden folglich auch nicht geprüft — die Überdehnung ist heute folgenlos"* und *„der Wortlaut wird nicht nachträglich gekürzt"*. Beides hält der Nachprüfung im eigenen Dokument nicht stand:

| Überdehnter Anteil | Wo er tatsächlich wirkt | Folge |
|---|---|---|
| **Fassung „2.2"** | steht in der **Then**-Spalte von AC-037, Bedingung (a) „WCAG-2.2-AA-Audit bestanden" — und in `docs/EVIDENCE-LEDGER.md` als EV-037-Marke **[ACC1]**, dort ausdrücklich „vor A2 — **blockierend für den Store-Release**" | **nicht folgenlos** — ein store-release-blockierender Nachweis auf einer Fassungsziffer, die in keiner der vier Quellen steht. Bleibt im Wortlaut, bleibt `ASSUMPTION` |
| **Web-Auskopplungen** | stand in der **Given**-Spalte von AC-037 und im `signal`-Feld dieses Messmodells | **nicht folgenlos** — war Vorbedingung des Akzeptanzkriteriums. **Am 2026-07-20 entfernt** (Nutzerauftrag Schritt 3) |
| **Bedienflächen** · **Fokusführung** | Fokusführung im `signal`-Feld dieses Messmodells; beide in `docs/EVIDENCE-LEDGER.md` als EV-037-Marken **[ACC4]** („keine Bedienfläche darf unerreichbar werden") und **[ACC7]** („**Fokusführung** und Bedienflächengrößen … Mindestgrößen der Trefferflächen je Plattform", fällig vor A2) | **nicht folgenlos** — nachweispflichtig vor A2. Bleiben im Wortlaut, bleiben `ASSUMPTION` |

**Der Satz „die Überdehnung ist heute folgenlos" widersprach zudem diesem Absatz selbst**, der zwei Sätze zuvor einräumt, dass die Fassungsziffer eine Pass-Bedingung von AC-037 ist. Der Befund wird gemeldet, nicht geglättet.

**Was daraus folgt und was nicht.** Gekürzt wurde **ausschließlich** die Web-Erstreckung, und zwar auf ausdrücklichen Nutzerauftrag vom 2026-07-20 — sie ist der einzige der vier Anteile, der den **Geltungsbereich** verändert statt den Detailgrad. Die drei übrigen (2.2, Bedienflächen, Fokusführung) bleiben unverändert im Wortlaut und sind hier als `ASSUMPTION` offengelegt; es wird **nichts hochgestuft und keine Klausel still entfernt**. Die frühere Sperrklausel „der Wortlaut wird nicht nachträglich gekürzt (Nutzerentscheidung, Registry eingefroren)" ist durch die spätere Nutzerentscheidung vom 2026-07-20 **überholt**, soweit sie die Web-Erstreckung betrifft — für alle anderen Klauseln gilt sie fort.

**Nebenbefund zur Belegkraft der Trennung REQ-037 ↔ REQ-038.** SRC-002 §10 verankert Accessibility an **Task 4.1** — demselben Task wie das Designsystem — und nennt als Nachweis **„Design-Token-Review + Screenreader-Check"**. Die Zerlegung in EV-038 (Design-Token-Review) und EV-037 (Screenreader-Check) folgt damit exakt der Zweiteilung, die die Quelle selbst im Nachweisfeld vornimmt. Das ist kein Beleg *für* die Requirement-Trennung, aber es widerspricht ihr auch nicht.

⚠️ **BLOCKER — REQ-037 hat KEINEN `canvas-problem`-Anker, und hier gilt KEINE Nichtanwendbarkeit (Registry §8 Punkt 37).** Die bisherigen Verknüpfungen zu **CAN-013** und **CAN-029** in `docs/traceability.md` beruhten auf der in Registry §6.1.1 **ausdrücklich verbotenen** Schlusskette „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" und sind entfernt. Der Canvas führt **kein Zugänglichkeitsproblem**. Es wird **kein** CAN-Item umgedeutet und **keine** neue Problem-ID vergeben — die reservierten CAN-016…CAN-021 decken die Aussage nicht ab. CAN-099 ist ein **Constraint**, kein Problem-Item, und ersetzt den fehlenden Problembezug nicht.

**Warum REQ-037 ausdrücklich NICHT wie REQ-038 und REQ-039 behandelt wird.** Für jene beiden ist die Nichtanwendbarkeit requirement-spezifisch begründbar. **Für REQ-037 ist sie es nicht, und die Versuchung ist genau hier am größten**, weil sich alle drei formal gleich lesen. Der Unterschied ist inhaltlich: eine Gestaltungssprache ist eine selbstgesetzte Regel und ein Exportformat eine Pflicht — **Zugänglichkeit dagegen adressiert unmittelbar eine Nutzergruppe, die das Produkt sonst nicht benutzen kann.** Das ist ein Nutzerproblem im vollen Sinn; es ist im Canvas nur **nicht aufgeschrieben**. Zusätzlich benennt CAN-099 diese Gruppe selbst („Menschen mit unterschiedlichen visuellen, motorischen und assistiven Anforderungen") — ein Constraint, der seine Zielgruppe nennt, **belegt damit die Existenz des Problems und ersetzt es nicht**. „Kein Problem-Item nötig" wäre hier die syntaktisch gültige, plausibel lesende Aussage, die die Sache nicht trägt. **Der Wert bleibt MISSING — BLOCKER.**

⚠️ **Einschränkung dieses Arguments, nachgetragen 2026-07-20.** Das Zusatzargument „CAN-099 benennt die Gruppe selbst" steht auf einer **nicht quellengedeckten Textstelle**: die Zielgruppenformel ist eine Formulierung des Canvas, keine Quellenaussage. Volltextsuche über alle vier Quellen: „motorisch" **0 Treffer**, „assistiv" **0 Treffer**, „barrierefrei" **0 Treffer**; keine der vier Quellen benennt überhaupt einen Adressatenkreis für Accessibility — sie formulieren ausschließlich Maßnahmen (Kontraste, Font Scaling, Screenreader-Labels; siehe Belegtabelle oben). **Das Argument wird deshalb als tragender Grund zurückgestuft, nicht gestrichen.** Der **BLOCKER bleibt unverändert bestehen**, und zwar aus dem Hauptgrund allein: Zugänglichkeit adressiert unmittelbar eine Nutzergruppe, die das Produkt sonst nicht benutzen kann — das ist ein Nutzerproblem, unabhängig davon, ob CAN-099 es formuliert. Die Zielgruppenformel bleibt im CAN-099-Wortlaut stehen und bleibt `ASSUMPTION` (Nutzerauftrag Schritt 3); sie wird hier nur nicht mehr als Beleg verwendet.

⚠️ **BLOCKER — VIS-011 zählt NICHT als erfüllter Vision-Anker.** `source_type` **ASSUMPTION**: VIS-011 ist neue Produktsubstanz auf Vision-Ebene, inhaltlich aus REQ-014, AC-014 und NFR-005 abgeleitet, vom Nutzer aber **nie als Vision-Aussage bestätigt** (Registry §8 Punkt 15). TRC-037 wird deshalb als `not-linked` geführt.

**Offene Punkte:** **MISSING** Rechtsgrundlage der WCAG-Verbindlichkeit · **MISSING** Screenreader- und Gerätematrix (OQ-003): VoiceOver/TalkBack in welchen OS-Versionen, welche Schriftgrößenstufen, welche Kontrastmessmethode · **MISSING** kein benannter Auditor · **BLOCKER** VIS-011 unbestätigt.

### REQ-038 — Monochromes tokenbasiertes Designsystem

> **Nachfolger 2 von 2 für das deprecatete REQ-014.** Prüft ausschließlich die **Gestaltungssprache**. Die Zugänglichkeit liegt bei REQ-037.

| Feld | Wert |
|---|---|
| measurement_type | **COMPLIANCE_CONTROL** |
| signal | Kontrollierter Nachweis, bewusst ohne Nutzersignal: **Inventar aller im Produkt verwendeten Farbwerte**, jeweils zugeordnet zu einer der vier zulässigen fachlichen Bedeutungen oder als Verstoß markiert; Anzahl Farbwerte außerhalb der Design-Tokens (Inline-Literale); Anzahl Stellen, an denen Run und Bike **ausschließlich** durch Farbe unterschieden werden. |
| target_or_pass_condition | AC-038 als Pass/Fail mit Nullschwellen: (a) Farbe erscheint **ausschließlich** in den vier abschließend definierten fachlichen Bedeutungen — **Health-Status**, **Team- und Revieridentität**, **Sportplatz-Gold**, **bestätigte Feiermomente** — **0** Farbeinsätze außerhalb dieser Liste · (b) **0** Stellen, an denen Run und Bike ausschließlich farblich unterschieden werden · (c) **0** Farbwerte außerhalb der Design-Tokens. Die Liste der vier Bedeutungen ist **abschließend**, nicht beispielhaft. |
| measurement_window | Kein zeitbasiertes Fenster — vollständige Inventarprüfung. Vor jedem Gate von A0 bis A2 und **bei jeder Änderung der Design-Tokens**; zusätzlich bei jedem neu ausgelieferten Screen. |
| evidence_source | **EV-038** (Design-Token-Review: Farbinventar gegen die vier zulässigen Bedeutungen, Run/Bike-Unterscheidbarkeitsprüfung, Prüfung auf Farb-Literale außerhalb der Tokens). `evidence_status` **`not-planned`** — es existiert kein Code, **keine Token-Datei** und kein festgelegtes Prüfverfahren; damit noch kein Messkonzept. |
| source_type | **EXPLICIT** — und zwar belegt, nicht hochgestuft. Der Anker **CAN-141** trägt `source_type EXPLICIT`, weil das monochrome, tokenbasierte Designsystem mit genau diesen vier Farbbedeutungen eine **ausdrückliche Nutzerangabe vom 2026-07-19** ist. Anders als bei REQ-037 hängt die Pass-Bedingung hier **nicht** an NFR-005 und **nicht** an einer externen Norm, deren Verbindlichkeit unbelegt wäre. Sie ist eine produktinterne Designentscheidung, und die ist belegt. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. |
| release_gate | **GATE-A0 bis GATE-A2** (Release A0-A2), erstmalige Abnahme mit GATE-A0 |
| rationale | Die Gestaltungsregel ist eine **Schranke mit Nullschwelle** und braucht bewusst kein Nutzersignal: ob Farbe sparsam eingesetzt wird, ist unabhängig davon messbar, wie viele Nutzer den Screen sehen. Ein Ästhetik- oder Zufriedenheitswert wäre ein Kategorienfehler. **Run/Bike-Trennung ist hier selbst Prüfgegenstand,** nicht nur Kontext: die Regel „Run und Bike werden nicht ausschließlich durch Farbe unterschieden" ist eine der drei Pass-Bedingungen. |

Canvas: **CAN-141** (kanonischer Designsystem-Anker) · Vision: **VIS-012 — reserved, Inhalt MISSING** · AC-038 · EV-038 · TRC-038

**Kanonischer CAN-141-Wortlaut (verbindlich, 2026-07-20)** — Item Type **DESIGN CONSTRAINT / PRODUCT PRINCIPLE**, Source Type **EXPLICIT**, primäres Requirement **REQ-038**:

> „Die Anwendung verwendet ein tokenbasiertes, überwiegend monochromes Designsystem. Farbe wird nur eingesetzt, wenn sie eine definierte fachliche Bedeutung besitzt: Health-Status, Team- und Revieridentität, Sportplatz-Gold sowie bestätigte Feiermomente. Run und Bike werden nicht ausschließlich durch Farbe unterschieden."

**CAN-141 darf NICHT mit Accessibility kombiniert werden.** Wie bei CAN-099 wurde **keine neue CAN-ID** vergeben — CAN-141 war bereits `active` und wortgleich bis auf „nur **dort eingesetzt, wo**" → „nur eingesetzt, **wenn** … **definierte**". Dieselbe ausdrücklich gemeldete Abweichung von der wörtlichen Anweisung wie bei REQ-037, überstimmbar.

**Trägt CAN-141 den Anker? — Belegprüfung gegen die Quelldokumente (2026-07-20).**

| Klausel in CAN-141 | Fundstelle | Verdikt |
|---|---|---|
| überwiegend monochromes Designsystem | SRC-003 §2: „**Designprinzip: „Farbe muss man sich verdienen."** Die App ist **konsequent monochrom** — Farbe existiert nur, wo sie Bedeutung trägt" · SRC-001 M-04: „Schwarz-Weiß-Design-System („Farbe muss man sich verdienen")" | **BELEGT**, nahezu wörtlich |
| **tokenbasiert** | SRC-001 M-04 Akzeptanzkriterium: „**Design-Tokens**; beide Modi; WCAG AA" · SRC-003 Task 4.1: „Design-System `src/config/theme.ts`: **S/W-Token**…" · SRC-002 §10 Nachweis: „**Design-Token-Review**" | **BELEGT** |
| Farbe nur bei definierter fachlicher Bedeutung | SRC-003 §2.1 Zeile „**Bedeutungsfarben (einzige Ausnahmen)**" | **BELEGT** — „einzige Ausnahmen" trägt zugleich die Abschließlichkeit der Liste |
| die **vier** Bedeutungen | ⚠️ **Die Quellen zählen FÜNF.** SRC-001 M-04: „Farbe nur **Team/Einzel-Revier/Sportplatz-Gold/Health-Ampel/Feier**". SRC-003 §2.1 ebenso fünf, als eigene Einträge: Teamfarben · **Einzel-Revier-Farben** · Gold · Health-Ampel · Feier-Momente | **TEILBELEGT** — inhaltsgleich, aber **Team** und **Einzel-Revier** sind in CAN-141 zu „Team- und Revieridentität" **zusammengezogen**. Kein Verlust, aber AC-038 nennt die Vierer-Liste **abschließend**, während beide Quellen fünf Einträge führen |
| Run und Bike nicht **ausschließlich** durch Farbe unterschieden | SRC-003 §2.1 Zeile „**Run-/Bike-Modus**": „bleibt monochrom; unterscheidet sich durch Ikonografie + Typo-Akzent, **nicht durch Farbe**" | **BELEGT** — ⚠️ und zwar **stärker als die Klausel behauptet**: die Quelle verbietet die Farbunterscheidung **ganz**, CAN-141 verbietet nur die **ausschließliche**. Die Abweichung ist eine **Abschwächung** gegenüber der Quelle, keine Erfindung — deshalb offengelegt und nicht stillschweigend verschärft |

**Verdikt: CAN-141 trägt REQ-038 — von den drei Ankern dieser Runde am deutlichsten.** Alle drei Pass-Bedingungen von AC-038 stehen in SRC-001 M-04 und SRC-003 §2/§2.1, überwiegend wortnah. Der `source_type EXPLICIT` ist damit **nicht nur durch die Nutzerentscheidung vom 2026-07-19 gedeckt, sondern zusätzlich quellenseitig** — das ist keine Hochstufung, sondern ein zweiter, unabhängiger Beleg für eine bereits vergebene Einstufung. **Zwei Abweichungen bleiben offen** (Fünf-zu-vier-Zusammenzug, Abschwächung der Run/Bike-Regel); beide sind Wortlautfragen und gehören dem Nutzer, nicht diesem Dokument.

**MISSING (begründet) — REQ-038 braucht kein `canvas-problem`-Item, requirement-spezifisch.** Die bisherige Verknüpfung zu **CAN-029** in `docs/traceability.md` beruhte auf derselben verbotenen Schlusskette wie bei REQ-037 und ist entfernt; die Verknüpfung zu **CAN-013** begründete dort zugleich „kein eigenes Problem-Item — begründete Nichtanwendbarkeit" und widersprach sich damit selbst. **Aufgelöst zugunsten der Nichtanwendbarkeit — und der tragende Grund steht seit dem 2026-07-20 in der Quelle, nicht mehr nur in der Argumentation dieses Dokuments:** SRC-003 §2 überschreibt die gesamte Gestaltungssprache mit **„Designprinzip: ‚Farbe muss man sich verdienen.'"** Ein Prinzip ist eine **selbstgesetzte Regel**, keine Antwort auf eine beschriebene Nutzernot. Keine der vier Quellen nennt ein Gestaltungs-, Ästhetik- oder Reizüberflutungsproblem, das die Monochromie beheben soll; SRC-001 führt M-04 als **Anforderung im Epic M**, SRC-002 als NFR-Verankerung an Task 4.1. **Die Nichtanwendbarkeit gilt genau so weit wie diese Rahmung** — sie ist kein allgemeiner Freibrief für Constraint-Requirements und wird für REQ-037 ausdrücklich **nicht** in Anspruch genommen. CAN-141 ist ein **Constraint**, kein Problem-Item, und wird auch nicht zu einem umgedeutet.

⚠️ **Registry-interne Divergenz, unverändert offen und hier nicht einseitig aufgelöst.** Registry §7.5.5 verlangt für diese Fundstelle den Wert „MISSING (**begründet**)", §8 Punkt 37 zählt REQ-038 dagegen zu den Requirements **ohne** `canvas-problem`-Anker und stuft das als **BLOCKER** ein. Dieses Dokument folgt der feldbezogen spezifischeren Anweisung aus §7.5.5 und führt REQ-038 in der BLOCKER-Zählung **trotzdem** mit, damit die Zahl nicht von der Registry abweicht. Die Registry ist eingefroren; die Auflösung gehört dem Registry-Owner.

⚠️ **BLOCKER — REQ-038 hat KEINEN Vision-Anker.** `VIS-012` ist in der Registry reserviert, der Inhalt ist **MISSING**. Die Prüfung aller bestehenden VIS-Items ergab: **kein** Item trägt ein Designprinzip auf Vision-Ebene. **VIS-011 deckt ausdrücklich nur die Accessibility-Hälfte ab.** Es wird **kein** VIS-Item umgedeutet — das wäre exakt der Defekt VIS-009 ↔ REQ-014. **TRC-038 wird deshalb bewusst als `broken` geführt**, mit sichtbarer Lücke, statt an ein unpassendes Item gehängt zu werden. Ein Designprinzip auf Vision-Ebene wäre neue Produktsubstanz und braucht eine Nutzerentscheidung.

**Abgrenzung zu CAN-099 — die Farbregel ist am 2026-07-20 einseitig aufgelöst worden.**

⚠️ **Die frühere Fassung dieses Absatzes ist aufgehoben.** Sie lautete: „dieselbe Beobachtung, zwei Pflichten" — der Satzteil „Farbe ist nie der einzige Informationsträger" wirke in CAN-099 als Zugänglichkeitsschranke **und** in CAN-141 als Gestaltungsregel. Das war der belegte Defekt: **eine doppelt geführte Pflicht mit zwei Ownern, zwei Nachweisen und keiner Instanz, die entscheidet, welcher gilt.** Die Trennung war zudem einseitig — die Klausel stand wörtlich in CAN-099 und zusätzlich als Vermerk bei CAN-141.

**Entscheidung: CAN-099 trägt die Klausel kanonisch (Registry §6.3.3).** Begründung: die Klausel schützt die **Wahrnehmbarkeit** von Information. Ihr Ausfall trifft Menschen mit Farbfehlsichtigkeit und ist ein **Zugänglichkeitsdefekt, kein Gestaltungsdefekt**. Die beiden Aussagen sind **unabhängig**, nicht dieselbe Beobachtung aus zwei Blickwinkeln — der Nachweis dafür ist, dass sie in beide Richtungen auseinanderfallen: ein **monochromes** Produkt kann die Klausel **verletzen** (zwei Grautöne als einziger Unterschied), ein **farbiges** kann sie **erfüllen** (Farbe plus Symbol plus Text).

**In CAN-141 verbleibt ausschließlich die engere Regel** „Run und Bike werden nicht ausschließlich durch Farbe unterschieden" — ein **konkretes Unterscheidungspaar**, prüfbar gegen die Design-Tokens (AC-038 b), keine allgemeine Wahrnehmbarkeitsschranke. **Es entsteht keine dritte Farbregel.** Die Zerlegung von REQ-014 bleibt davon unberührt: sie trennt Zugänglichkeit von Gestaltungssprache, und genau dieser Schnitt wird hier zu Ende geführt statt an einer Klausel offengelassen.

### REQ-039 — GPX-Export abgeschlossener Aktivitäten

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** (im bestehenden Modell: FUNCTIONAL CONTROL) |
| signal | **Getrennt für Run und Bike:** Erfolgsrate der GPX-Erzeugung aus abgeschlossenen Aktivitäten; Anteil erzeugter Dateien, die gegen das GPX-Schema valide sind; Anteil Dateien mit korrekter Zeitstempel- und Koordinatenreihenfolge; Öffnungserfolg in der definierten Fremd-App; **Anzahl Health-Datenfelder im Export (Sollwert 0)**; Anteil Fälle mit fehlenden oder beschädigten Trackdaten, die zu einem kontrollierten Fehler statt zu einem Absturz oder einer stillen Teildatei führen. |
| target_or_pass_condition | AC-039 als Pass/Fail — **acht einzeln prüfbare Bedingungen**: (a) GPX für abgeschlossene **Run**-Aktivität erzeugt · (b) GPX für abgeschlossene **Bike**-Aktivität erzeugt · (c) **Zeitstempel und Koordinatenreihenfolge korrekt** · (d) Datei in mindestens einer **definierten** kompatiblen Fremd-App öffenbar · (e) **0 Health-Daten unbeabsichtigt exportiert** · (f) der Nutzer sieht **vor** dem Export, welche Daten enthalten sind · (g) fehlende oder beschädigte Trackdaten führen zu einem **kontrollierten Fehler** · (h) der Export funktioniert **ohne** Veröffentlichung oder Social-Freigabe. Eine Nutzungs- oder Exportquote wird **nicht** gesetzt — ein solcher Zielwert wäre erfunden. |
| measurement_window | Vor **GATE-A2**, spätestens vor öffentlichem v1.0-Release; danach bei jeder Änderung am Exportformat, am Datenmodell oder an den exportierten Feldern. **Je Sportart und je Plattform mindestens ein vollständiger Durchlauf**, zusätzlich je ein Negativtest (beschädigte Trackdaten, Health-Daten-Ausschluss). |
| evidence_source | **EV-039** (GPX-Export-Test je Sportart: Erzeugung, Schemakonformität, Zeitstempel- und Koordinatenreihenfolge, Öffnen in einer definierten Fremd-App, Negativtest auf Health-Daten, Fehlerfall bei beschädigten Trackdaten); Mindestklasse `real-boundary-smoke` — **Kompatibilität ist keine Eigenschaft des eigenen Parsers.** Ein Test, der die eigene Datei mit dem eigenen Code wieder einliest, prüft nur sich selbst. `evidence_status` **`not-planned`**. |
| source_type | **ASSUMPTION** — der Wortlaut stammt aus der Nutzerentscheidung vom 2026-07-19, ist aber nicht ausdrücklich als Anforderungstext bestätigt. Die Pass-Bedingungen sind überwiegend analytische Nullschwellen. **„GPX" ist zudem kein konkret zitierter Standard:** weder die **Formatversion** (1.0 / 1.1) noch die Referenzanwendung sind benannt — beides MISSING. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. |
| release_gate | **GATE-A2**, spätestens vor öffentlichem v1.0-Release |
| rationale | Der prüfbare Kern ist **Erzeugbarkeit und Interoperabilität**, nicht Nutzerverhalten — deshalb kein Nutzersignal. Die Run-/Bike-Trennung ist zwingend, weil die exportierten Kernmetriken sportartspezifisch sind und ein Exporter, der nur mit Laufdaten getestet wurde, bei Radaktivitäten stillschweigend falsche oder leere Felder schreiben kann. Der **Negativtest auf Health-Daten** ist keine Nebenbedingung, sondern trägt die Datenminimierung aus REQ-034 in den Export hinein: ein GPX mit eingebetteten Herzfrequenzverläufen verlässt das Gerät unkontrolliert. |

Canvas: **CAN-139** (kanonischer Portabilitäts-Anker) · Vision: **VIS-013 — reserved, Inhalt MISSING** · AC-039 · EV-039 · TRC-039 · sekundär: **REQ-034**

**Kanonischer CAN-139-Wortlaut (verbindlich, 2026-07-20)** — Item Type **VALUE PROMISE / CAPABILITY**, Source Type **EXPLICIT** (vorher ASSUMPTION), `measurement_type` OPERATIONAL_QUALITY, primäres Requirement **REQ-039**:

> „Nutzer behalten Kontrolle über ihre aufgezeichneten Aktivitäten und können eine abgeschlossene Run- oder Bike-Aktivität als standardkonforme GPX-Datei exportieren, ohne sie veröffentlichen oder mit anderen Nutzern teilen zu müssen."

**REQ-034 bleibt AUSSCHLIESSLICH sekundärer Security-/Privacy-/Portabilitäts-Constraint.** Das GPX-Canvas-Item darf **nicht allein über REQ-034 getragen** werden. Auch hier wurde **keine neue CAN-ID** vergeben — dieselbe ausdrücklich gemeldete Abweichung wie bei REQ-037 und REQ-038, überstimmbar.

⚠️ **OPEN QUESTION — die Fremd-App-Klausel ist aus dem Canvas-Wortlaut entfallen, aus AC-039 und EV-039 aber nicht (Registry §8 Punkt 36).** Der frühere CAN-139-Text nannte „…exportieren **und in einer kompatiblen Fremdanwendung öffnen**". Der kanonische Text nennt das **nicht mehr**. **AC-039 Kriterium (d) und EV-039 verlangen den Nachweis weiterhin.** Der Bezug ist über „**standardkonforme** GPX-Datei" tragbar — Interoperabilität ist die operative Probe auf Standardkonformität —, aber er ist **nicht mehr wörtlich belegt**. Das wird **offengelegt statt stillschweigend gedeckt**: es wird weder die AC gestrichen noch der Canvas-Wortlaut nachträglich ergänzt. Zu entscheiden vom Nutzer, zusammen mit OQ-016.

**Trägt CAN-139 den Anker? — Belegprüfung gegen die Quelldokumente (2026-07-20).**

| Klausel in CAN-139 | Fundstelle | Verdikt |
|---|---|---|
| GPX-Export einer abgeschlossenen Aktivität | SRC-001 Epic T **T-06**: „GPX-Export" · SRC-003 Plan **2.8**: „GPX-Export (Share Sheet)" · SRC-002 §3: „T-06 \| GPX-Export \| 2.8 \| v1.0 \| A" | **BELEGT** in allen drei Quellen |
| Portabilität / „Nutzer behalten Kontrolle" | SRC-003 §8 Store-Compliance-Matrix: „Datenexport \| A/2.8 \| **GPX-Export erfüllt Portabilität**" · SRC-001 §3.5 NFR Privacy/DSGVO: „…**Datenexport**…" | **BELEGT** — das Wort „Portabilität" steht wörtlich in SRC-003 |
| **Run und Bike getrennt** | keine Quelle differenziert den Export nach Sportart; die Sporttrennung ist projektweite Regel (SRC-001 §3.5 „Run/Bike getrennt nachgewiesen") | **BELEGT**, aber über die allgemeine Nachweisregel, nicht über T-06 |
| „**standardkonforme** GPX-Datei" | keine Quelle nennt eine **Formatversion** (1.0 / 1.1) oder zitiert den Standard | **UNBELEGT** — bestätigt das bestehende MISSING; es wird keine Version geraten |
| „ohne sie **veröffentlichen oder mit anderen Nutzern teilen** zu müssen" | SRC-001 §2: v1.0-Umfang inkl. GPX-Export ist „**alles lokal, ohne Account**"; §3.1 Ziel (1): „vollwertiger Health-Tracker **ohne Account** ab v1.0". SRC-003 2.8 nennt als Weg das **Share Sheet** (Betriebssystem), nicht einen In-App-Feed | **TEILBELEGT.** Die Quellen **beschreiben eine Architektur**, in der die Klausel zwangsläufig gilt (v1.0 hat weder Account noch soziale Ebene) — sie **fordern sie nirgends als Bedingung**. Der Unterschied wird nicht eingeebnet: aus „es gibt keinen Feed" folgt nicht „der Export darf nie einen voraussetzen" |

**Verdikt: CAN-139 trägt REQ-039.** Der Kern — GPX-Export einer abgeschlossenen Aktivität als Portabilitätsleistung — steht in allen drei Quellen, in SRC-003 §8 sogar mit dem Wort „Portabilität". Der Anker ist sauber verankert, nicht erschlossen.

⚠️ **Befund zur OPEN QUESTION „Fremd-App" (Registry §8 Punkt 36) — die Prämisse ist enger als bisher notiert.** Der bisherige Vermerk lautet, die Klausel „in einer kompatiblen Fremdanwendung öffnen" sei „**nicht mehr wörtlich belegt**". Gegen die Quellen gilt das **nur für den kanonischen CAN-139-Wortlaut**, nicht für die Sache: **SRC-001 T-06** führt als Akzeptanzkriterium wörtlich „**Fremd-App öffnet Datei**", **SRC-003 Plan 2.8** dasselbe. **AC-039 Kriterium (d) und EV-039 sind damit quellenbelegt und stehen nicht ohne Grundlage da** — sie geben das Akzeptanzkriterium der Quelle wieder. Was offen bleibt, ist ausschließlich die **Wortlautfrage**: ob der Canvas-Text die Klausel wieder aufnehmen soll. **Das ist eine Nutzerentscheidung und wird hier nicht getroffen** — es wird weder die AC gestrichen noch der Canvas-Wortlaut ergänzt. **MISSING bleibt**, welche Fremdanwendung die Referenz ist (OQ-016): die Quellen sagen „Fremd-App", benennen aber keine. **Es wird keine App geraten.**

**MISSING (begründet) — REQ-039 braucht kein `canvas-problem`-Item, requirement-spezifisch.** Die bisherige Verknüpfung zu **CAN-013** in `docs/traceability.md` lief über die Variante „Daten, die man nicht mitnehmen kann, bleiben fremdbestimmt" — dieselbe verbotene Schlusskette; das Feld vermerkte den schwachen Bezug bereits selbst und ist entfernt. **Die Nichtanwendbarkeit stützt sich auf die Rahmung der Quellen, und die ist dreifach und einheitlich:** SRC-003 §8 führt den Export als **Zeile der Store-Compliance-Matrix**, SRC-001 §3.5 als **NFR unter Privacy/DSGVO**, SRC-001 T-06 als **funktionale Capability mit rein technischem Akzeptanzkriterium** („Fremd-App öffnet Datei"). Das sind eine **Pflicht**, eine **Pflicht** und eine **Fähigkeit** — **keine** der drei ist eine Nutzernot. Der Canvas führt folgerichtig kein Portabilitäts- oder Lock-in-Problem. CAN-139 ist ein Value-Promise-/Capability-Item, kein Problem-Item, und wird nicht zu einem umgedeutet.

⚠️ **Offengelegter Rest — diese Begründung ist schwächer als die bei REQ-038.** Bei REQ-038 typisiert die Quelle das Requirement selbst als „Designprinzip"; hier sagen die Quellen über ein etwaiges Nutzerproblem **gar nichts**. Ein Lock-in-Problem („meine Daten sitzen in einer App fest") ist denkbar und wäre ein echtes Nutzerproblem — **es steht nur in keiner Quelle und in keinem Canvas-Item.** „Die Quellen rahmen es als Pflicht" belegt daher, dass **hier kein Problembezug erfunden werden darf**, nicht, dass es **keinen geben kann**. Der Unterschied wird ausgewiesen statt weggeglättet; die Entscheidung, ob der Canvas ein Portabilitätsproblem führen soll, gehört dem Nutzer.

⚠️ **BLOCKER — REQ-039 hat KEINEN Vision-Anker.** `VIS-013` (Datenportabilität) ist reserviert, Inhalt **MISSING**. Prüfung aller bestehenden VIS-Items: **VIS-003** nennt Tracking, Health-Auswertung, Fortschrittssignale und Trainingspartner — **keine Portabilität**; **VIS-009** regelt Sichtbarkeit und Werbenutzung, **nicht die Mitnahme** der eigenen Daten. Kein Item wird umgedeutet. **TRC-039 wird bewusst als `broken` geführt.**

⚠️ **MISSING — die Referenz-Fremdanwendung ist nicht benannt (OQ-016).** Ohne sie ist AC-039 Kriterium **(d)** nicht reproduzierbar prüfbar: „öffnet in irgendeiner App" ist keine Bestehensbedingung. **Es wird keine App geraten.** Ebenfalls **MISSING**: die GPX-Formatversion.

**REQ-034 ist sekundär, nicht primär** — Begründung im Messmodell zu REQ-034.

### ~~REQ-040~~ — deprecated am 2026-07-20

> **DEPRECATED → REQ-041 (Wiederverwendung einer gespeicherten Route) und REQ-042 (Vergleich fachlich vergleichbarer Aktivitäten).** REQ-040 war ein **Composite** — wie zuvor REQ-014. Es wurde **nicht auf eine Hälfte verengt**, sondern geteilt. Folge-Deprecations: **AC-040, EV-040, TRC-040** sowie das Canvas-Item **CAN-140**. Neue Referenzen auf REQ-040 sind ein Validierungsfehler. Kanonisch: `docs/ID-REGISTRY.md` §6.3.3, §6.4, §7.5.

**Warum geteilt und nicht verengt.** Die Atomisierungsregel trennt, wenn die Aussagen unabhängig ausgeliefert werden können, unterschiedlichen Gates zugeordnet sind, unterschiedliche Nutzerwerte besitzen, unterschiedliche Acceptance Criteria benötigen **oder** unabhängig bestehen bzw. scheitern können. Bei REQ-040 sind **fünf** dieser Kriterien erfüllt — nicht bloß „der Satz enthält mehrere Verben":

| Kriterium | Wiederverwendung (REQ-041) | Vergleich (REQ-042) |
|---|---|---|
| Nutzerwert | **Vorbereitung** — dieselbe Runde noch einmal laufen oder fahren | **Rückblick** — die eigene Leistung einordnen |
| Handlung | eine gespeicherte Route laden und starten | zwei abgeschlossene Aktivitäten gegenüberstellen |
| Acceptance Criteria | AC-042, fünf Bedingungen, **alle heute spezifizierbar** | AC-043, zwei Bedingungen fest, **vier MISSING** |
| Blockierungszustand | **nicht blockiert** | **blockiert durch OQ-015** |
| Unabhängig lieferbar | ja — braucht nur die gespeicherte Route aus REQ-006 | ja — braucht nur zwei abgeschlossene Aktivitäten aus REQ-008 |

Der vierte Punkt ist der operative: **ein gemeinsames Item hätte den lieferbaren Teil an eine offene Forschungsfrage gekettet.** Genau dieselbe Modellierungsfrage wurde bei AC-019/AC-041 bereits entschieden — zwei IDs, nicht zwei Felder derselben ID.

### REQ-041 — Wiederverwendung einer gespeicherten Route

> **Nachfolger 1 von 2 für das deprecatete REQ-040.** Prüft ausschließlich die **Planungs-/Wiederverwendungsfunktion**. Der Aktivitätsvergleich liegt bei REQ-042.

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** |
| signal | **Getrennt für Run und Bike:** Erfolgsrate des Ladens und Startens einer gespeicherten Route; Anteil geladener Routen, deren **Geometrie und Wegpunkte** exakt der gespeicherten Fassung entsprechen (Abweichungsmaß gegen die persistierte Geometrie); Anteil geladener Routen, bei denen das **sportartspezifische Routingprofil** korrekt erhalten bleibt (`run` → Fußprofil, `ride` → Radprofil, CAN-094); Anzahl gelöschter oder beschädigter gespeicherter Routen, die zu einem **stillen Leerstart** statt zu einem kontrollierten Fehler führen (Sollwert 0); Ladezeit der gespeicherten Route bei wachsender Zahl gespeicherter Routen. |
| target_or_pass_condition | AC-042 als Pass/Fail mit Nullschwellen, **Run und Bike getrennt nachgewiesen** — **fünf Bedingungen, alle heute bestimmbar**: (a) gespeicherte Route für **Run** in 100 % der Fälle wiederverwendbar · (b) gespeicherte Route für **Bike** in 100 % der Fälle wiederverwendbar · (c) **0 Abweichungen** zwischen geladener und gespeicherter Geometrie und Wegpunktliste · (d) **0 Fälle** mit falschem oder verlorenem sportartspezifischem Routingprofil nach dem Laden · (e) gelöschte oder beschädigte Routen führen in 100 % der Fälle zu einem **kontrollierten Fehler**. Eine Wiederverwendungs**quote** wird **nicht** gesetzt — ein solcher Zielwert wäre erfunden und würde außerdem Nutzerverhalten statt Funktionsqualität messen. |
| measurement_window | Vor **GATE-A2**; danach bei jeder Änderung am Routen-Persistenzformat, am Routingprofil-Mapping oder am Planungsflow. **Je Sportart und je Plattform (iOS, Android) mindestens ein vollständiger Durchlauf**, zusätzlich je ein Negativtest (gelöschte Route, beschädigte Route). Fixture-Suite bei jedem CI-Lauf. |
| evidence_source | **EV-043** (Wiederverwendungstest je Sportart: Auswahl und Start einer gespeicherten Route, Abgleich von Geometrie und Wegpunkten gegen die gespeicherte Fassung, Erhalt des sportartspezifischen Routingprofils, kontrollierter Fehlerfall bei gelöschter oder beschädigter Route); Mindestklasse `real-boundary-smoke` — die **Persistenz über einen echten Prozessneustart** ist mit keinem Fake beweisbar, und das Routingprofil-Mapping liegt laut CAN-094 im Proxy, also außerhalb des eigenen Codes. `evidence_status` **`not-planned`** — es existiert kein Code und kein Messkonzept. **Ausdrücklich NICHT durch OQ-015 blockiert.** |
| source_type | **ASSUMPTION** — der Wortlaut stammt aus der Nutzerentscheidung vom 2026-07-20, ist aber **nicht ausdrücklich als Anforderungstext bestätigt**; der Canvas-Anker CAN-142 trägt `source_type ASSUMPTION` aus demselben Grund. Die Pass-Bedingungen selbst sind analytische 0-/100-%-Schranken ohne gewählten Zahlenwert — belegbedürftig **und unbelegt** bleibt die **Anforderung selbst**. Registry §8 Punkt 43. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen, PRD-Kopfzeile „Owner" = MISSING. |
| release_gate | **GATE-A2** |
| rationale | Der prüfbare Kern ist die **verlustfreie Rückgewinnung einer gespeicherten Planungsgrundlage**, nicht Nutzerverhalten — deshalb kein Nutzersignal und keine Wiederverwendungsquote. Die **Run-/Bike-Trennung ist hier nicht dekorativ, sondern der eigentliche Fehlerfall:** eine Route, die als Bike-Route geplant und gespeichert wurde, muss beim erneuten Laden das Radprofil behalten. Fällt das Profil auf einen Standardwert zurück, entsteht eine plausibel aussehende, fachlich falsche Route — dieselbe Fehlerklasse wie RISK-005 („Bike zeigt falsche Laufmetriken"), nur eine Ebene früher. Der Negativtest auf gelöschte Routen adressiert den zweiten realistischen Pfad: Routen sind langlebige Objekte, die zwischen Speichern und Wiederverwenden gelöscht oder beschädigt werden können. |

Canvas: **CAN-142** · Vision: **VIS-014 — reserved, Inhalt MISSING** · AC-042 · EV-043 · TRC-041

**Kanonischer CAN-142-Wortlaut (verbindlich, 2026-07-20):** „Nutzer können eine gespeicherte Route erneut als Grundlage einer geplanten Run- oder Bike-Aktivität verwenden." Release-Stufe **A2**, Source Type **ASSUMPTION**.

⚠️ **BLOCKER — REQ-041 hat KEINEN Vision-Anker (Registry §8 Punkt 38).** `VIS-014` ist reserviert, Inhalt **MISSING**. **Die bestehenden VIS-Items sind einzeln geprüft und alle verworfen:** **VIS-003** nennt verlässliches Tracking, Health-Auswertung, konkrete Fortschrittssignale und sicheren Zugang zu lokalen Trainingspartnern — **keine Wiederverwendung geplanter Strecken**; **VIS-004** nennt Belastung, Progression, lokale Teams und ortsbezogene Spielmechaniken — ebenfalls nicht. Die naheliegende Lesart „Routenplanung hängt doch an VIS-003" stammt aus TRC-006 und ist **dort selbst ungeprüft** (Registry §8 Punkt 40); sie wird hier **nicht übernommen, weil sie existiert**. **TRC-041 wird bewusst als `broken` geführt.**

⚠️ **ABWEICHUNG, ausdrücklich gemeldet — VIS-014 stand nicht auf der Auftragsliste.** Die Anweisung nannte für die Teilung nur neue CAN-, REQ-, AC-, EV- und TRC-IDs. Die VIS-Reservierung ist trotzdem erfolgt, nach dem Präzedenzfall VIS-012/VIS-013, damit die Folgephasen weder eine ID erfinden noch REQ-041 still an VIS-003 hängen. **Überstimmbar** — dann bleibt der Anker ein BLOCKER ohne ID.

⚠️ **BLOCKER — Wortlaut unbestätigt.** REQ-041 und CAN-142 tragen `source_type` **ASSUMPTION** (Registry §8 Punkt 43).

**Warum REQ-041 nicht in REQ-006 aufgeht.** REQ-006 deckt das **Anlegen** einer Route auf **Gate A0** ab („über Wegpunkte oder ein Distanzziel planen, das korrekte Routingprofil verwenden, den Plan vor dem Start prüfen"). REQ-041 deckt die **erneute Verwendung einer bereits gespeicherten Route** auf **Gate A2** ab. Das sind zwei Handlungen auf zwei Gates. **Auch CAN-050 („Routenplanung und gespeicherte Routen") trägt die Aussage nicht** — es trägt laut Registry REQ-006; es dafür zu benutzen wäre die plausible Lesart mit falscher Bedeutung.

### REQ-042 — Vergleich fachlich vergleichbarer Aktivitäten

> **Nachfolger 2 von 2 für das deprecatete REQ-040.** Prüft ausschließlich die **Auswertungs-/Vergleichsfunktion**. Die Wiederverwendung liegt bei REQ-041.

| Feld | Wert |
|---|---|
| measurement_type | **OPERATIONAL_QUALITY** — das Requirement misst **Funktionsqualität** (ist die Vergleichsaussage korrekt?). **Die Vergleichslogik selbst bleibt davon getrennt `RESEARCH_HYPOTHESIS` bzw. MISSING**, solange OQ-015 offen ist. Beides wird bewusst nicht vermischt: *dass* Nutzer vergleichen können sollen, ist eine Produktannahme; *wie* verglichen wird, ist eine offene Untersuchungsfrage. |
| signal | **Strikt getrennt für Run und Bike:** Anteil Aktivitätspaare, die von der Vergleichslogik als vergleichbar eingestuft werden, gegen ein manuell kuratiertes Referenzurteil; Anzahl **falsch-positiver** Vergleiche (geometrisch nicht vergleichbare Aktivitäten werden gegenübergestellt); Anzahl **falsch-negativer** Vergleiche (fachlich vergleichbare Aktivitäten werden nicht erkannt); Anzahl ausgewiesener Bestzeiten bei nicht vergleichbarer Geometrie (**Sollwert 0**); Anzahl sportübergreifender Vergleiche (**Sollwert 0**); Verhalten bei verkürzten, verlängerten und abgebrochenen Aktivitäten. |
| target_or_pass_condition | **Zweigeteilt, weil nur ein Teil heute bestimmbar ist.** **Feststehend und schon jetzt prüfbar (AC-043):** (a) Run und Bike **strikt getrennt** — **0** sportübergreifende Vergleiche · (b) **0** irreführende Bestzeiten bei nicht vergleichbarer Geometrie. **MISSING (OQ-015) und hier ausdrücklich NICHT erfunden:** das Vergleichbarkeitskriterium selbst · die tolerierte Abweichung der **Streckenähnlichkeit** · die verglichenen **Kennzahlen** · die Behandlung **verkürzter, verlängerter und abgebrochener** Aktivitäten. Ohne diese vier Werte sind die Falsch-Positiv- und Falsch-Negativ-Raten **nicht berechenbar**, weil das Referenzurteil selbst undefiniert ist. **AC-043 ist bis zur Entscheidung nicht vollständig prüfbar.** |
| measurement_window | Vor **GATE-A2**; danach bei jeder Änderung der Vergleichslogik oder der Vergleichbarkeitsschwelle. Fixture-Suite bei jedem CI-Lauf, **sobald eine Schwelle existiert** — vorher ist keine Fixture bezifferbar. **Je Sportart getrennt.** |
| evidence_source | **EV-044** (Vergleichstest je Sportart: Gegenüberstellung zweier als fachlich vergleichbar erkannter Aktivitäten anhand sportartspezifischer Kennzahlen; Negativtests gegen verkürzte, verlängerte, abgebrochene und geometrisch abweichende Aktivitäten; Negativtest gegen sportübergreifenden Vergleich); Mindestklasse `real-boundary-smoke` — reale GPS-Spuren derselben Runde weichen voneinander ab, und genau diese Abweichung ist der Prüfgegenstand; synthetisch identische Tracks verdecken ihn. `evidence_status` **`not-planned`**. **BLOCKER:** ohne die Definition aus **OQ-015** ist **kein Testfall bezifferbar** — die Negativtests sind benannt, aber ohne Toleranzwert nicht ausführbar. **Es wird keine Toleranz geraten.** |
| source_type | **ASSUMPTION** für das Requirement — der Wortlaut stammt aus der Nutzerentscheidung vom 2026-07-20 und ist **nicht ausdrücklich als Anforderungstext bestätigt**; CAN-143 trägt `ASSUMPTION` aus demselben Grund. **Der Zielwert der Vergleichslogik ist davon getrennt MISSING** (OQ-015) — er ist in **keinem** Artefakt beziffert. Registry §8 Punkte 28 und 43. |
| owner | **OWNER-BLOCKER (MISSING)** — OQ-002 offen. Die Vergleichbarkeitsdefinition (OQ-015) hat ebenfalls **keinen benannten Entscheider**. |
| release_gate | **GATE-A2** |
| rationale | Der prüfbare Kern ist die **Korrektheit der Vergleichsaussage**, nicht deren Nutzung — deshalb kein Nutzersignal und keine Vergleichsquote. Die **strikte Sporttrennung** ist keine Formalie: eine Radfahrt und ein Lauf über dieselbe Geometrie sind physikalisch unvergleichbar, und ein sportübergreifender „Rekord" wäre eine falsche Produktaussage. Die Nullschwelle für irreführende Bestzeiten adressiert denselben Fehlerfall **innerhalb** einer Sportart: **eine Bestzeit über eine nur scheinbar identische Strecke ist schlimmer als gar keine Bestzeit**, weil der Nutzer ihr vertraut. Dass die beiden Nullschwellen schon heute feststehen, während das Vergleichbarkeitskriterium fehlt, ist kein Widerspruch — sie sind **Schranken gegen falsche Aussagen** und unabhängig davon gültig, wie „vergleichbar" definiert wird. |

Canvas: **CAN-143** · Vision: **VIS-003** — *zu prüfende Annahme des Traceability-Owners, keine Feststellung dieses PRD* · AC-043 · EV-044 · TRC-042

**Kanonischer CAN-143-Wortlaut (verbindlich, 2026-07-20):** „Nutzer können fachlich vergleichbare Aktivitäten auf derselben oder hinreichend ähnlichen Strecke anhand sportartspezifischer Kennzahlen miteinander vergleichen." Release-Stufe **A2**, Source Type **ASSUMPTION**, **benötigt zusätzliche Regeln zur Streckenähnlichkeit**.

⚠️ **BLOCKER — OQ-015 (Vergleichbarkeitsdefinition) ist offen.** Zu entscheiden: wann zwei Strecken als **vergleichbar** gelten · **tolerierte Abweichung** der Streckenähnlichkeit · welche **Kennzahlen** verglichen werden · Behandlung verkürzter, verlängerter und abgebrochener Aktivitäten · Sicherstellung, dass bei nicht vergleichbarer Geometrie **keine irreführende Bestzeit** entsteht. `blocked_gates: [A2]` · `blocked_activities: [implementation]` — **A0 und A1 sind nicht blockiert, und REQ-041 ist es ebenfalls nicht.**

⚠️ **BEFUND — OQ-015 ist auf REQ-042 übergegangen, die Registry führt aber noch die Vorgänger-IDs.** `docs/ID-REGISTRY.md` nennt in der OQ-015-Definitionszeile und in §8 Punkt 28 weiterhin **REQ-040, AC-040, EV-040 und CAN-140** — alle vier sind in derselben Runde deprecated worden. Die wirksamen Adressaten sind **REQ-042, AC-043, EV-044 und CAN-143**. Dieses PRD zieht darauf nach und meldet die Abweichung; die Registry ist eingefroren, die Korrektur liegt beim Registry-Owner.

⚠️ **OPEN QUESTION — der Vision-Anker VIS-003 ist ungeprüft und wird NICHT hochgestuft.** Er ist unverändert aus TRC-040 übernommen. VIS-003 nennt „konkrete Fortschrittssignale", was einen Aktivitätsvergleich **plausibel trägt**; ob es ihn **trägt**, ist ungeprüft. Es ist dieselbe Lesart, die für REQ-041 ausdrücklich **verworfen** wurde — sie wird hier nicht deshalb akzeptiert, weil sie schon einmal in einer Zeile stand. TRC-042 gilt damit **nicht** als `linked`, sondern als `linked-partial`. Registry §8 Punkt 40 stellt dieselbe Frage für TRC-006.

⚠️ **BLOCKER — Wortlaut unbestätigt.** REQ-042 und CAN-143 tragen `source_type` **ASSUMPTION** (Registry §8 Punkt 43).

**Warum REQ-042 nicht in REQ-006/REQ-007/REQ-008 aufgeht.** REQ-006 (Routenplanung) und REQ-007 (routenbezogener Fortschritt) betreffen die **Planung und Durchführung** einer Route; REQ-008 betrifft **Verlauf und Detailansicht** einer einzelnen Aktivität. REQ-042 betrifft den **Vergleich zweier abgeschlossener Aktivitäten** — eine Aussage, die ausschließlich als Teilklausel im Composite REQ-008 und danach in CAN-140/REQ-040 stand. Die Prüfung aller aktiven CAN- und REQ-Items ergab **keine** Deckung.


## Release Gates

| Gate | Requirements | Exit Evidence |
|---|---|---|
| GATE-A0 | REQ-001–REQ-008, **REQ-037** (Accessibility-Basis), **REQ-038**, REQ-034–REQ-036 soweit anwendbar | reale Run/Bike-Aktivität iOS/Android, Background/Kill, Route-Fortschritt, Batterie, Persistenz, **Verlauf und Detailansicht mit sportrichtiger Kernmetrik**, Accessibility-Basis, Design-Token-Review |
| GATE-A1 | REQ-009–REQ-013 | echte Health-Daten, Score mit/ohne HF, Claims-Lint, Check-in/Trend |
| GATE-A2 / v1.0 | REQ-015–REQ-016, **REQ-037** (vollständiger WCAG-2.2-AA-Audit), **REQ-038**, **REQ-039** (GPX-Export), **REQ-041** (Wiederverwendung einer gespeicherten Route), **REQ-042** (Aktivitätsvergleich) plus Store-Readiness | Store-Testtracks, Datenschutz, Widgets, **GPX-Export je Sportart in definierter Fremd-App geöffnet**, **gespeicherte Route je Sportart erneut geladen und gestartet**, **fachlich valider Aktivitätsvergleich**, vollständiger Accessibility-Audit, finaler öffentlicher Name |
| GATE-B | REQ-017–REQ-019 | Auth/Offline/Löschung, Privacy-Matrix, Moderation und Routenübernahme |
| GATE-C | REQ-020–REQ-025 | Teams, gemeinsame Aktivität, Effort-Simulation, Anti-Cheat und idempotente Rewards |
| GATE-D | REQ-026–REQ-031 | Territory-Simulation, Geo-Fixtures, Sportplatzprüfung, Threat-Model, Live-Endpfade und Safety-Evidence |
| GATE-E | REQ-032–REQ-033 | Wearable-Matrix, Claims-/Privacy-Freigabe und echte Gerätetests |

## Links

- ID-Registry (kanonisch für alle IDs, eingefroren): `docs/ID-REGISTRY.md`
- Entscheidungs- und Widerspruchs-Ledger: `docs/decisions/decision-log.md`
- Offene Fragen (kanonisch): `docs/decisions/open-questions.md`
- Vision: `docs/vision/revyr-endurance-platform.vision.md`
- Canvas: `docs/canvas/revyr-endurance-platform.canvas.md`
- Traceability: `docs/traceability.md`
- Delivery Plan: `docs/implementation/revyr-delivery-plan.md`
- Target Architecture: `docs/architecture/revyr-target-architecture.md`
- Risk Register: `docs/risks/revyr-risk-register.md`
- Evidence Ledger: `docs/EVIDENCE-LEDGER.md`

## User Confirmation Required

Die Assistenz bestätigt dieses PRD nicht im Namen des Nutzers.
