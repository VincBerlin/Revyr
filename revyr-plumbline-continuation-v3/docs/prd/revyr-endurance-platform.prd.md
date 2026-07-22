# PRD: REVYR Endurance Platform

Status: ready-for-user-confirmation  
Feature Slug: `revyr-endurance-platform`  
Owner: MISSING – im Repository zu benennen  
Public Brand: MISSING – REVYR ist vorläufiger Arbeitstitel  
User Confirmation Required: yes

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

| ID | Assumption | Source Type | Validation |
|---|---|---|---|
| ASM-001 | Der öffentliche v1.0-Release wird intern in A0, A1 und A2 geteilt. | ASSUMPTION | Ressourcen- und Release-Review |
| ASM-002 | SQLite beziehungsweise eine transaktionale lokale Datenbank ersetzt die vollständige Track-Speicherung in AsyncStorage. | ASSUMPTION | technischer Spike |
| ASM-003 | Ein backendseitiger Proxy oder gleichwertiger Schutz wird vor Produktionsrouting verwendet. | ASSUMPTION | Karten-/Routing-ADR |
| ASM-004 | Einzel-Reviere und Bahngold bleiben bis Stufe D deaktiviert. | ASSUMPTION | Scope-Bestätigung |

## Open Questions

| ID | Question | Owner | Needed By | Source Type |
|---|---|---|---|---|
| OQ-001 | Finaler öffentlicher Name und Marke? | Product/Legal | Gate A2 | MISSING |
| OQ-002 | Backendentscheidung nach Geo/Auth/Realtime-Prototyp? | Engineering | vor B | MISSING |
| OQ-003 | Karten-/Routinganbieter und API-Key-/Kostenstrategie? | Engineering/Product | vor A2/B | MISSING |
| OQ-004 | Health-Claims-Whitelist? | Product/Legal | vor A1 Public Beta | MISSING |
| OQ-005 | Minimum iOS/Android und Referenzgeräte? | Engineering/QA | vor A0 Feldtest | MISSING |
| OQ-006 | Monetarisierungsmodell? | Product/Business | vor C | MISSING |

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
| REQ-008 | **Verlauf, Wiederverwendung und Export:** Abgeschlossene Aktivitäten MÜSSEN in Verlauf und Detailansicht verfügbar sein; gespeicherte Routen, Streckenvergleich und GPX-Export werden unterstützt. | Must | A0 | EXPLICIT | SRC-001/SRC-003 |
| REQ-009 | **Herzfrequenzquellen:** Die App MUSS Herzfrequenz aus HealthKit, Health Connect oder unterstützten BLE-Sensoren lesen können und Quelle sowie Datenlücken transparent kennzeichnen. | Must | A1 | EXPLICIT | SRC-001/SRC-003 |
| REQ-010 | **Erklärbarer Belastungs-Score mit Confidence:** Nach jeder Aktivität MUSS ein Belastungs-Score mit Gründen, verwendeten Signalen und Confidence-Stufe angezeigt werden; ohne Herzfrequenz wird ein klar begrenzter Fallback verwendet. | Must | A1 | ASSUMPTION | SRC-001/SRC-005 |
| REQ-011 | **HF-Zonen und optionale Ansage:** HF-Zonen MÜSSEN schätzbar und manuell korrigierbar sein; Live-Zonenhinweise und Audio sind optional und vollständig deaktivierbar. | Should | A1 | EXPLICIT | SRC-001/SRC-003 |
| REQ-012 | **Stimmungs-Check-in und Korrelation:** Nach einer Aktivität SOLL ein kurzer Stimmungs-Check-in möglich sein; Korrelationen werden erst nach ausreichender Datenmenge und mit Unsicherheit dargestellt. | Should | A1 | EXPLICIT | SRC-001 |
| REQ-013 | **Health-Home und Steigerungshinweis:** Home MUSS den aktuellen Wochenzustand zeigen und bei deutlich erhöhter Belastung einen orientierenden, nicht diagnostischen Hinweis ausgeben. | Must | A1 | EXPLICIT | SRC-001/SRC-003 |
| REQ-014 | **Designsystem und Accessibility:** Alle Screens MÜSSEN ein tokenbasiertes monochromes Designsystem, Dynamic Type, Screenreader-Labels, WCAG-AA-Kontraste und zusätzliche Symbole statt alleiniger Farbcodierung verwenden. | Must | A0-A2 | EXPLICIT | SRC-003 |
| REQ-015 | **Verdiente Avatar-Progression:** Basis-Avatare dürfen frei angepasst werden; leistungsbezogene Items, Teamkleidung und Season-Objekte dürfen nur durch definierte reale Leistungen freigeschaltet und nicht gekauft werden. | Should | A2-B-C | EXPLICIT | SRC-001/SRC-003 |
| REQ-016 | **Recaps, Erfolgskarten und Live-Status:** Die App SOLL Wochenrückblicke, teilbare Erfolgskarten und plattformgerechte Live-Aktivitätsanzeigen bereitstellen, ohne sensible Start-/Endpunkte offenzulegen. | Should | A2 | EXPLICIT | SRC-001/SRC-003 |
| REQ-017 | **Accounts, Auth und Datenmigration:** Ab v2 MÜSSEN E-Mail, Apple und Google Auth, Offline-Sync, Migration lokaler Aktivitäten und vollständige In-App-Accountlöschung unterstützt werden. | Must | B | EXPLICIT | SRC-001/SRC-003 |
| REQ-018 | **Privacy, Sichtbarkeit und Moderation:** Profile sind standardmäßig privat; Follow-Anfragen, Blockieren, Melden, Moderationsqueue, Regeln und Sichtbarkeitsmatrix MÜSSEN ab der ersten Social-Version vollständig funktionieren. | Must | B | EXPLICIT | SRC-001/SRC-003 |
| REQ-019 | **Routenempfehlungen und Feed:** Nutzer SOLLEN neue Routen erkennen, mit strukturierten Hinweisen empfehlen und von berechtigten Followern mit einem Tipp übernehmen lassen können. | Should | B | EXPLICIT | SRC-001/SRC-003 |
| REQ-020 | **Teamgründung und Beitritt:** Teams MÜSSEN transaktional mit Admin entstehen; Beitritt erfolgt über kontrollierbare Links oder QR-Codes mit Ablauf und Deaktivierung. | Must | C | EXPLICIT | SRC-001/SRC-003 |
| REQ-021 | **Aktive Mitglieder und Teamwachstum:** Teamkapazität, Stufen und Mentorbonus MÜSSEN aktive Mitglieder und echte Integration statt bloßer Einladungen belohnen. | Must | C | EXPLICIT | SRC-001/SRC-003 |
| REQ-022 | **Gemeinsame Aktivitäten und Events:** Gemeinsame Aktivitäten MÜSSEN aus Zeit- und räumlicher Überschneidung deterministisch erkannt werden; geplante Gruppenaktivitäten und Events nutzen dieselbe Logik und Moderation. | Must | C-D | EXPLICIT | SRC-001/SRC-003 |
| REQ-023 | **Effort-Normalisierung:** Sportübergreifende Team- oder Territory-Wertungen MÜSSEN versionierte, simulierte Effort-Faktoren verwenden; interne Run- und Bike-Wertungen bleiben in echten sportbezogenen Metriken getrennt. | Must | C | EXPLICIT | SRC-001/SRC-003 |
| REQ-024 | **Anti-Cheat mit Confidence-Stufen:** Aktivitäten MÜSSEN serverseitig auf Geschwindigkeit, Teleports und verfügbare Sensorplausibilität geprüft und als verified-high, verified-standard, low-confidence, review-required oder rejected klassifiziert werden. | Must | C | ASSUMPTION | SRC-003/SRC-005 |
| REQ-025 | **Challenges, Rankings und idempotente Rewards:** Wochen-Challenges, sportgetrennte Rankings, Meilensteine und Rewards MÜSSEN serverkonfigurierbar, nachvollziehbar und idempotent sein. | Must | C | EXPLICIT | SRC-001/SRC-003 |
| REQ-026 | **Team-Territory:** Ab v4 dürfen nur verifizierte Beiträge und ein Quorum reale, benannte Team-Areale beeinflussen; internes Raster bleibt unsichtbar und Kartenlayer müssen performant filterbar sein. | Must | D | EXPLICIT | SRC-001/SRC-003 |
| REQ-027 | **Seasons und unveränderliche Historie:** Seasons MÜSSEN nur das aktive Spielfeld zurücksetzen; Snapshots, Trophäen, Vereinsheim und Zeitreise bleiben unveränderlich erhalten. | Must | D | EXPLICIT | SRC-001/SRC-003 |
| REQ-028 | **Deterministische Einzel-Reviere:** Einzel-Reviere dürfen erst nach Simulation und Threat-Model freigeschaltet werden; Rundenerkennung, Anfahrtssegmentierung, Übernahmepriorität, Polygon-Union/-Differenz, Restflächen und Gleichstände MÜSSEN deterministisch definiert sein. | Must | D | ASSUMPTION | SRC-003/SRC-005 |
| REQ-029 | **Sportplatz-Challenges und Bahngold-Score:** Freigegebene öffentliche Sportanlagen dürfen als goldene Challenge-Orte erscheinen; Runden und Rekorde werden GPS-tolerant validiert. Bahngold ist ein nicht übertragbarer Progressions-Score, keine Währung und beeinflusst kein Territory. | Should | D | ASSUMPTION | SRC-003/SRC-005 |
| REQ-030 | **Live-Map und Beschützer-Modus:** Live-Standort MUSS pro Aktivität explizit aktiviert, zeitlich begrenzt, sichtbar angezeigt, notabschaltbar und start-/endpunktverschleiert sein; Beschützer-Links enden automatisch. | Must | D | EXPLICIT | SRC-001/SRC-003 |
| REQ-031 | **Sturzerkennung als Assistenz:** Sturzerkennung darf nur als Assistenzfunktion mit Countdown, Abbruchmöglichkeit, dokumentierter Fehlalarmquote und ohne Sicherheitsgarantie angeboten werden. | Should | D | EXPLICIT | SRC-001/SRC-003 |
| REQ-032 | **Wearables und Bike-Sensorik:** Apple Watch, Wear OS und unterstützte Bike-Sensoren dürfen erst nach dokumentierter Kompatibilitätsmatrix freigeschaltet werden; Start/Stopp und Kernmetriken müssen konsistent synchronisieren. | Should | E | EXPLICIT | SRC-001/SRC-003 |
| REQ-033 | **Coach, Recovery, Wetter und Zyklus unter Claims-Gate:** Regenerations-, Coach-, Hitze-/Trink- und Zyklusfunktionen dürfen erst nach juristischer Claims- und Privacy-Freigabe erscheinen und müssen regelbasiert, erklärbar, optional und deaktivierbar sein. | Should | E | EXPLICIT | SRC-001/SRC-003 |
| REQ-034 | **Security, Datenschutz und Datenminimierung:** Das System MUSS EU-orientiertes Hosting, sichere Auth, Row-Level-Security, Rate Limits, serverseitige Validierung, Datenexport, Löschung und Datensparsamkeit umsetzen; Roh-Health-Verläufe werden nur bei nachgewiesener Notwendigkeit übertragen. | Must | A0-E | EXPLICIT | SRC-001/SRC-003 |
| REQ-035 | **Evidence Ledger und Definition of Done:** Kein Task oder Gate darf als abgeschlossen gelten, bevor automatisierte Tests, reale Gerätetests, Run/Bike-Nachweise, offene Punkte und Messwerte im Evidence Ledger dokumentiert sind. | Must | A0-E | EXPLICIT | SRC-003 |
| REQ-036 | **Store- und Release-Gates:** Jede Release-Stufe MUSS die zugehörigen iOS-/Android-Policies, Berechtigungsbegründungen, Datenschutzangaben und Testtracks vor Veröffentlichung bestehen; spätere Stufen starten erst nach dem vorherigen Gate. | Must | A0-E | EXPLICIT | SRC-003 |

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
| AC-008 | REQ-008 | Mindestens eine Aktivität wurde abgeschlossen. | Der Nutzer Verlauf, Detail, Wiederholen oder Export öffnet. | Die korrekten sportbezogenen Daten und die aufgezeichnete Route sind verfügbar und exportierbar. | EXPLICIT |
| AC-009 | REQ-009 | Eine kompatible Datenquelle ist freigegeben oder verbunden. | Eine Aktivität aufgezeichnet wird. | Live-/Verlaufs-HF und Quelle werden korrekt dargestellt; fehlende HF blockiert Tracking nicht. | EXPLICIT |
| AC-010 | REQ-010 | Eine Aktivität mit vollständigen oder unvollständigen Health-Daten endet. | Der Score berechnet und geöffnet wird. | Nutzer sehen Score, konkrete Gründe, Datenbasis, fehlende Signale und die Unsicherheit der Aussage. | ASSUMPTION |
| AC-011 | REQ-011 | HF-Daten und Zonen sind verfügbar. | Der Nutzer trainiert oder Einstellungen ändert. | Zonen und Hinweise reagieren korrekt; Deaktivierung verhindert jede Ansage. | EXPLICIT |
| AC-012 | REQ-012 | Eine Aktivität endet. | Der Nutzer einen Check-in abgibt und mindestens vier Wochen Daten vorliegen. | Der Check-in dauert unter zwei Sekunden und Trends werden ohne Kausalitätsbehauptung angezeigt. | EXPLICIT |
| AC-013 | REQ-013 | Wochen- und Vier-Wochen-Daten liegen vor. | Home geöffnet oder die Schwelle überschritten wird. | Aktivitäten, Belastung und Trend sind korrekt; Hinweise verwenden freigegebene Orientierungssprache. | EXPLICIT |
| AC-014 | REQ-014 | Ein Screen oder Status wird gerendert. | Dark/Light Mode, größere Schrift oder Screenreader verwendet werden. | Inhalt bleibt verständlich, bedienbar und kontrastreich; Farbe ist nie der einzige Träger. | EXPLICIT |
| AC-015 | REQ-015 | Ein Unlock-Kriterium ist definiert. | Die zugehörige verifizierte Leistung erreicht wird. | Das Item wird genau einmal freigeschaltet; ohne Leistung oder Kauf ist es nicht verfügbar. | EXPLICIT |
| AC-016 | REQ-016 | Eine Aktivität oder Woche abgeschlossen ist. | Ein Rückblick, Export oder Lockscreen-Status erzeugt wird. | Metriken sind korrekt, exportierbar und sensible Standortdaten sind reduziert. | EXPLICIT |
| AC-017 | REQ-017 | Lokale Daten existieren oder ein Account wird erstellt. | Der Nutzer sich anmeldet, offline trainiert oder sein Konto löscht. | Daten migrieren/synchronisieren deterministisch; Löschung entfernt alle personenbezogenen Daten gemäß Retention-Regeln. | EXPLICIT |
| AC-018 | REQ-018 | Zwei Nutzer und Social-Inhalte existieren. | Sichtbarkeit geändert, blockiert oder gemeldet wird. | Nur erlaubte Daten sind sichtbar; Blockierung wirkt beidseitig sofort und Meldungen sind bearbeitbar. | EXPLICIT |
| AC-019 | REQ-019 | Eine Route ist neu und der Nutzer darf posten. | Eine Empfehlung erstellt oder übernommen wird. | Feed-Sichtbarkeit, Routendaten und Übernahme entsprechen den Privacy-Regeln. | EXPLICIT |
| AC-020 | REQ-020 | Berechtigte Nutzer gründen oder betreten ein Team. | Gründung, Scan, Ablauf oder Deaktivierung ausgeführt wird. | Es existiert nie ein Team ohne Admin und ungültige Tokens gewähren keinen Zugang. | EXPLICIT |
| AC-021 | REQ-021 | Ein Team hat neue, aktive und inaktive Mitglieder. | Kapazität, Stufe oder Mentorbonus berechnet wird. | Nur Mitglieder mit Aktivität im definierten Zeitfenster zählen; Bonus folgt erst nach nachgewiesener Integration. | EXPLICIT |
| AC-022 | REQ-022 | Mindestens zwei freigegebene Aktivitäten oder ein Event vorliegen. | Nähe, Zeit und Teilnahme ausgewertet werden. | Echte gemeinsame Aktivität wird erkannt, nicht gemeinsame wird abgelehnt und Eventinhalte sind moderierbar. | EXPLICIT |
| AC-023 | REQ-023 | Run- und Bike-Aktivitäten fließen in eine gemeinsame Mechanik. | Effort und Rang berechnet werden. | Keine Sportart dominiert systematisch; verwendete Version und Faktoren sind nachvollziehbar. | EXPLICIT |
| AC-024 | REQ-024 | Eine Aktivität synchronisiert wird. | Plausibilitätsregeln angewendet werden. | Fehlende Sensoren allein führen nicht zur Betrugsannahme; klare Manipulation zählt nicht für Wettbewerb. | ASSUMPTION |
| AC-025 | REQ-025 | Challenge-Definitionen und verifizierte Aktivitäten vorliegen. | Fortschritt oder Reward verarbeitet wird. | Fortschritt ist korrekt und kein Reward wird doppelt vergeben. | EXPLICIT |
| AC-026 | REQ-026 | Territory-Simulation und Geo-Daten sind freigegeben. | Teams Beiträge leisten oder Layer umschalten. | Eroberung folgt Formel und Quorum, reale Areale werden dargestellt und das interne Raster ist nie sichtbar. | EXPLICIT |
| AC-027 | REQ-027 | Eine Season endet. | Der Season-Abschluss ausgeführt wird. | Aktive Besitzstände werden zurückgesetzt und historische Records bleiben vollständig abrufbar. | EXPLICIT |
| AC-028 | REQ-028 | Eine zielgebundene, verifizierte Aktivität eine Fläche umschließt. | Einnahme, Überlappung, Teilübernahme oder Gleichstand berechnet wird. | Dasselbe Eingabeset erzeugt dieselbe Geometrie und denselben Besitzer; Linien-/Drift-Tracks werden abgelehnt. | ASSUMPTION |
| AC-029 | REQ-029 | Ein zugänglicher, kuratierter Sportplatz existiert. | Vollständige Runden oder Rekorde erkannt werden. | Nur plausible Runden zählen; geschlossene/private Anlagen bleiben gesperrt und Bahngold verändert keine Effort- oder Territory-Wertung. | ASSUMPTION |
| AC-030 | REQ-030 | Ein Nutzer eine Live-Freigabe startet. | Freigabe endet, App beendet, blockiert oder Not-Aus ausgelöst wird. | In jedem Pfad endet die Freigabe; unberechtigte und blockierte Personen sehen keinen Standort. | EXPLICIT |
| AC-031 | REQ-031 | Sturzähnliche Sensordaten auftreten. | Das Muster erkannt wird. | Ein sichtbarer Countdown startet, kann abgebrochen werden und nur danach wird der definierte Kontakt informiert. | EXPLICIT |
| AC-032 | REQ-032 | Ein unterstütztes Wearable oder Sensor gekoppelt ist. | Aktivität gestartet, pausiert oder beendet wird. | Status und Messwerte bleiben zwischen Geräten konsistent und nicht unterstützte Kombinationen sind klar benannt. | EXPLICIT |
| AC-033 | REQ-033 | Claims-Whitelist und Privacy-Review sind freigegeben. | Eine Empfehlung erzeugt wird. | Empfehlung nennt Gründe, Grenzen und Datenbasis; sensible Funktionen sind Opt-in und vollständig deaktivierbar. | EXPLICIT |
| AC-034 | REQ-034 | Personen-, Health- oder Standortdaten verarbeitet werden. | Daten gespeichert, synchronisiert, exportiert oder gelöscht werden. | Zugriff folgt Berechtigung und Zweckbindung; nicht benötigte sensible Daten verlassen das Gerät nicht. | EXPLICIT |
| AC-035 | REQ-035 | Ein Task oder Release-Gate zur Abnahme vorgelegt wird. | Die Definition of Done geprüft wird. | Status wird nur bei vollständiger Evidence auf done gesetzt; fehlende Nachweise bleiben sichtbar. | EXPLICIT |
| AC-036 | REQ-036 | Eine Release-Stufe zur Veröffentlichung vorgesehen ist. | Gate und Store-Readiness geprüft werden. | Kein Release wird ohne vollständige Nachweise und Policy-Abnahmen veröffentlicht. | EXPLICIT |

## Non-Functional Requirements

| ID | Requirement | Target | Source Type |
|---|---|---|---|
| NFR-001 | Distanzgenauigkeit | < 3 % Abweichung auf definierter Referenzstrecke nach Filter | EXPLICIT |
| NFR-002 | Batterie | Ziel < 10 % pro Stunde auf definierten Referenzgeräten; Messwert dokumentieren | EXPLICIT |
| NFR-003 | Zuverlässigkeit | kein Datenverlust bei App-Kill/Absturz; Session-Recovery verpflichtend | EXPLICIT |
| NFR-004 | Performance | Tracking-UI flüssig; Kartenlayer viewportbasiert; Geo-Lasttest vor D | EXPLICIT |
| NFR-005 | Accessibility | WCAG AA, Dynamic Type, Screenreader und keine reine Farbcodierung | EXPLICIT |
| NFR-006 | Datenschutz | Privacy by default, EU-orientiertes Hosting, Export/Löschung und Datenminimierung | EXPLICIT |
| NFR-007 | Sicherheit | keine Secrets im Client, sichere Auth, RLS, Rate Limits, serverseitige Validierung | EXPLICIT |
| NFR-008 | Wartbarkeit | TypeScript strict, reine Domainmodule, versionierte Schemas, automatisierte Tests | EXPLICIT |

## Risks

Verbindliches Register: `docs/risks/revyr-risk-register.md`.

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
| EV-008 | REQ-008 | Repository-, UI- und GPX-Kompatibilitätstest. | EXPLICIT |
| EV-009 | REQ-009 | Echte Geräte und BLE-Gurt je Plattform. | EXPLICIT |
| EV-010 | REQ-010 | Formeltests mit/ohne HF und UI-Test des Warum-Sheets. | ASSUMPTION |
| EV-011 | REQ-011 | Zonen-Unit-Tests und Kopfhörer-Gerätetest. | EXPLICIT |
| EV-012 | REQ-012 | Zeitmessung, Fixture-Korrelation und Copy-Review. | EXPLICIT |
| EV-013 | REQ-013 | Wochen-Fixtures und Claims-Lint. | EXPLICIT |
| EV-014 | REQ-014 | Token-Review, Accessibility- und Screenreader-Check. | EXPLICIT |
| EV-015 | REQ-015 | Idempotenz- und Unlock-Fixtures. | EXPLICIT |
| EV-016 | REQ-016 | Bildexport-, Widget- und Privacy-Snapshot-Test. | EXPLICIT |
| EV-017 | REQ-017 | E2E-Flow, Offline-Test und Löschungsnachweis. | EXPLICIT |
| EV-018 | REQ-018 | Sichtbarkeits-Matrix, Zwei-Account- und Moderationstest. | EXPLICIT |
| EV-019 | REQ-019 | Zwei-Account-E2E-Flow. | EXPLICIT |
| EV-020 | REQ-020 | Datenbanktransaktions- und Zwei-Geräte-Test. | EXPLICIT |
| EV-021 | REQ-021 | Zeitfenster- und Integrations-Fixtures. | EXPLICIT |
| EV-022 | REQ-022 | Pure-Function-Fixtures und Zwei-Geräte-Eventtest. | EXPLICIT |
| EV-023 | REQ-023 | Monte-Carlo-/Szenariosimulation und Kalibrierungsbericht. | EXPLICIT |
| EV-024 | REQ-024 | Betrugs-/Grenzfall-Fixtures und False-Positive-Review. | ASSUMPTION |
| EV-025 | REQ-025 | Deterministische Fixtures und Wiederholungs-Test. | EXPLICIT |
| EV-026 | REQ-026 | Geo-Fixtures, Simulation und Karten-Lasttest. | EXPLICIT |
| EV-027 | REQ-027 | Zwei-Season-Integrationstest und Unveränderlichkeitsprüfung. | EXPLICIT |
| EV-028 | REQ-028 | Geo-Fixture-Suite, Property-Tests und Threat-Model. | ASSUMPTION |
| EV-029 | REQ-029 | OSM-Access-Review, realer Bahn-Test und Reward-Fixtures. | ASSUMPTION |
| EV-030 | REQ-030 | Threat-Model, Endpfad-Matrix und Penetrationstest. | EXPLICIT |
| EV-031 | REQ-031 | Kontrollierte Falltests, Fehlalarmstatistik und Claims-Review. | EXPLICIT |
| EV-032 | REQ-032 | Gerätematrix und reale Integrationstests. | EXPLICIT |
| EV-033 | REQ-033 | Claims-Lint, Rechtsfreigabe und Privacy-Test. | EXPLICIT |
| EV-034 | REQ-034 | Security-Review, RLS-Tests, Datenflussdiagramm und Löschungsnachweis. | EXPLICIT |
| EV-035 | REQ-035 | CI-Regel, Ledger-Review und Gate-Checkliste. | EXPLICIT |
| EV-036 | REQ-036 | TestFlight/Internal-Test-Bericht, Policy-Matrix und Gate-Sign-off. | EXPLICIT |

## Release Gates

| Gate | Requirements | Exit Evidence |
|---|---|---|
| GATE-A0 | REQ-001–REQ-008, REQ-014, REQ-034–REQ-036 soweit anwendbar | reale Run/Bike-Aktivität iOS/Android, Background/Kill, Route-Fortschritt, Batterie, Persistenz, Accessibility |
| GATE-A1 | REQ-009–REQ-013 | echte Health-Daten, Score mit/ohne HF, Claims-Lint, Check-in/Trend |
| GATE-A2 / v1.0 | REQ-015–REQ-016 plus Store-Readiness | Store-Testtracks, Datenschutz, Widgets/Export, finaler öffentlicher Name |
| GATE-B | REQ-017–REQ-019 | Auth/Offline/Löschung, Privacy-Matrix, Moderation und Routenübernahme |
| GATE-C | REQ-020–REQ-025 | Teams, gemeinsame Aktivität, Effort-Simulation, Anti-Cheat und idempotente Rewards |
| GATE-D | REQ-026–REQ-031 | Territory-Simulation, Geo-Fixtures, Sportplatzprüfung, Threat-Model, Live-Endpfade und Safety-Evidence |
| GATE-E | REQ-032–REQ-033 | Wearable-Matrix, Claims-/Privacy-Freigabe und echte Gerätetests |

## Links

- Vision: `docs/vision/revyr-endurance-platform.vision.md`
- Canvas: `docs/canvas/revyr-endurance-platform.canvas.md`
- Traceability: `docs/traceability.md`
- Delivery Plan: `docs/implementation/revyr-delivery-plan.md`
- Target Architecture: `docs/architecture/revyr-target-architecture.md`
- Risk Register: `docs/risks/revyr-risk-register.md`
- Evidence Ledger: `docs/EVIDENCE-LEDGER.md`

## User Confirmation Required

Die Assistenz bestätigt dieses PRD nicht im Namen des Nutzers.
