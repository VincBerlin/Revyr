# Product Canvas: REVYR Endurance Platform

Status: ready-for-user-confirmation  
Feature Slug: `revyr-endurance-platform`  
Public Brand: MISSING – REVYR ist vorläufiger Arbeitstitel

| Section | ID | Value | Source Type | Source |
|---|---|---|---|---|
| Problem | CAN-001 | Bestehende Tracker liefern häufig Daten ohne verständliche Bedeutung, soziale Interaktion ohne lokale Bindung und zu wenig Anlass für echte gemeinsame Aktivität. | EXPLICIT | SRC-001 |
| Users / Customers | CAN-002 | Freizeit- und ambitionierte Läufer:innen und Radfahrer:innen sowie lokale Sportgruppen und Vereine. | EXPLICIT | SRC-001 |
| Value Promise | CAN-003 | Verstehe deine Belastung, erkenne deinen Fortschritt, trainiere sicherer und finde reale lokale Gemeinschaft – ohne dass Spielmechaniken die Health-Grundlage verdrängen. | ASSUMPTION | SRC-001/SRC-005 |
| Current Alternatives | CAN-004 | Strava, Garmin Connect, Apple Fitness, Google/Fitbit, Whoop, Lauf- und Radsportvereine, WhatsApp-Gruppen und lokale Event-Plattformen. | EXPLICIT | SRC-001/SRC-003 |
| Key Capabilities | CAN-005 | Robustes Run/Bike-Tracking, geplante Routen, erklärbare Health-Auswertung, Progression, Accounts, lokale Teams, Challenges, Territory, Live-Safety und Wearable-Anbindung in gestuften Releases. | EXPLICIT | SRC-001/SRC-003 |
| Non-Goals | CAN-006 | Kein Medizinprodukt, kein Chat-Messenger, keine kaufbaren Leistungs-Boosts, keine Indoor-/Gym-Plattform, kein vollwertiger Web-Client und keine Territory-Systeme im ersten Release. | EXPLICIT | SRC-001 |
| Constraints | CAN-007 | Eine iOS-/Android-Codebasis; deutsche Launch-Sprache mit i18n-Vorbereitung; Store-Policies, DSGVO, Background-Location, Health-Berechtigungen und reale Gerätetests sind verbindlich. | EXPLICIT | SRC-001/SRC-003 |
| Risks | CAN-008 | GPS-Drift, Batterieverbrauch, falsche Health-Claims, Namenskollision, Betrug, Standortmissbrauch, Geo-Komplexität, OSM-Qualität und Store-Ablehnung. | EXPLICIT | SRC-003 |
| Success Signal | CAN-009 | Der Health-Tracker hält Nutzer nach vier Wochen, Health-Erklärungen werden genutzt und spätere Community-Systeme erhöhen reale gemeinsame Aktivitäten. | EXPLICIT | SRC-001 |
| Evidence | CAN-010 | Unit-/Integrationstests, Referenzstrecken, Batterie- und Kill-Tests, Health-Gerätetests, Privacy-Matrizen, Simulationen, Store-Testtracks und ein Evidence Ledger. | EXPLICIT | SRC-003 |
| Allowed Scope | CAN-011 | Öffentliche v1.0 umfasst ausschließlich nachgewiesene Tracking-, Health- und Basis-Erlebnisfunktionen; Accounts ab v2, Teams ab v3, Territory/Live ab v4, Coach/Wearables ab v5. | ASSUMPTION | SRC-003/SRC-005 |
| Unresolved Questions | CAN-012 | Öffentlicher Name, Geschäftsmodell, Backend, Karten-/Routinganbieter, Health-Claim-Whitelist, unterstützte Geräte/OS-Versionen und finale Spielwerte. | EXPLICIT | SRC-001/SRC-003 |

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

## Allowed Scope

| Stufe | Erlaubter Scope | Nicht erlaubt vor Gate |
|---|---|---|
| A0 | robustes Tracking, Planung, Verlauf, Persistenz, Designbasis | Health-Behauptungen, Social, Territory |
| A1 | Health-Basis und erklärbarer Score | Community- und Wettbewerbssysteme |
| A2 / v1.0 | Rückblicke, Export, Avatarbasis, Widgets, Store-Release | Accounts und öffentlicher UGC |
| B / v2 | Accounts, Profile, Empfehlungen, Feed, Moderation | Teams/Territory ohne Anti-Cheat |
| C / v3 | Teams, Rankings, Challenges, Anti-Cheat | Territory/Live ohne Simulation/Threat-Model |
| D / v4 | Territory, Seasons, Events, Live-Safety | Coach-/Recovery-Claims ohne Freigabe |
| E / v5 | Wearables, Coach, Recovery, Wetter, Zyklus | nicht freigegebene medizinische Claims |

## Unresolved Questions

| ID | Question | Needed By | Source Type |
|---|---|---|---|
| OQ-001 | Welcher öffentliche Name wird markenrechtlich freigegeben? | vor Store-Metadaten / Gate A2 | MISSING |
| OQ-002 | Welches Backend besteht Geo-, Realtime-, Auth- und EU-Hosting-Prototyp? | vor Stufe B | MISSING |
| OQ-003 | Welche Karten-/Routinganbieter und Kostenlimits gelten? | vor öffentlichem A2/B | MISSING |
| OQ-004 | Welche Health-Formulierungen werden freigegeben? | vor A1 Public Beta und E | MISSING |
| OQ-005 | Welche OS-/Geräteversionen werden unterstützt? | vor A0 Feldtest | MISSING |
| OQ-006 | Welches Geschäftsmodell trägt Karten-, Realtime- und Moderationskosten? | vor Stufe C | MISSING |

## User Confirmation

Die Assistenz bestätigt diesen Canvas nicht im Namen des Nutzers.
