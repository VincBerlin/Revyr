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
| User Need | VIS-003 | Nutzer benötigen verlässliches Tracking, verständliche statt abstrakte Health-Auswertung, konkrete Fortschrittssignale und einen sicheren Zugang zu lokalen Trainingspartnern. | EXPLICIT | SRC-001 | no |
| Product Value | VIS-004 | Die Plattform verbindet erklärbare Trainingsbelastung, verdiente Progression, lokale Teams und reale ortsbezogene Spielmechaniken in einem konsistenten Run/Bike-Produkt. | EXPLICIT | SRC-001/SRC-003 | no |
| Project Goal | VIS-005 | Zuerst einen belastbaren Health-Tracker etablieren; danach Accounts, Community, Teams und erst nach nachgewiesener Datenqualität Territory- und Live-Systeme freischalten. | EXPLICIT | SRC-003 | no |
| Success Signal | VIS-006 | W4-Retention >30 %, Check-in-Quote >50 %, Warum-Aufrufe >25 %; später Teambeitritt, gemeinsame Aktivitäten und Season-Teilnahme als stufenbezogene Signale. | EXPLICIT | SRC-001 | no |
| Health-first Boundary | VIS-007 | Health-Ausgaben sind Orientierung, keine Diagnose. Score und Empfehlungen müssen Datenbasis, Gründe und Unsicherheit erklären. | EXPLICIT | SRC-001/SRC-003 | no |
| Fairness Boundary | VIS-008 | Run und Bike besitzen getrennte Metriken, Ziele und interne Wertungen; sportübergreifender Effort wird nur mit simulierten und versionierten Faktoren verwendet. | EXPLICIT | SRC-003 | no |
| Privacy Boundary | VIS-009 | Profile sind standardmäßig privat; Live-Standort ist pro Aktivität Opt-in, zeitlich begrenzt und start-/endpunktverschleiert; Health-Daten werden nicht für Werbung genutzt. | EXPLICIT | SRC-001/SRC-003 | no |
| Delivery Principle | VIS-010 | Kein komplexes Community-, Territory- oder Safety-System wird vor dem Evidence-Gate der vorherigen Stufe veröffentlicht. | EXPLICIT | SRC-003 | no |

## Target Group

- Primär: Freizeit-Läufer:innen und Radfahrer:innen mit 1–4 Aktivitäten pro Woche.
- Sekundär: ambitionierte Ausdauersportler:innen mit Strecken-, Sensor- und Leistungsfokus.
- Organisationen: Laufgruppen, Radsportgruppen und Vereine, die ein lokales digitales Zuhause benötigen.

## User Needs

1. Aktivitäten zuverlässig aufzeichnen und wiederfinden.
2. Belastung und Fortschritt verständlich statt als Blackbox interpretieren.
3. Run und Bike als gleichwertige, aber metrisch getrennte Sportwelten nutzen.
4. Lokale Trainingspartner und Gruppen sicher finden.
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

## Boundaries

- Kein Medizinprodukt und keine Diagnose.
- Kein Chat-Messenger und kein allgemeines soziales Netzwerk.
- Keine kaufbaren Leistungswerte, Boosts oder notwendigen Avatar-Items.
- Kein Territory, keine öffentliche Live-Map und keine Sturzerkennung vor den jeweiligen Safety-Gates.
- Der Arbeitstitel darf nicht ungeprüft in finale Bundle IDs, Domains oder öffentliche Store-Metadaten eingebrannt werden.

## Assumptions

| ID | Assumption | Source Type | Validation |
|---|---|---|---|
| ASM-001 | Eine gestufte öffentliche v1.0 aus A0/A1/A2 reduziert Risiko gegenüber einem einzigen überladenen MVP. | ASSUMPTION | Release- und Ressourcenschätzung |
| ASM-002 | Ein Health-Score mit sichtbarer Confidence ist verständlicher und rechtlich robuster als ein einzelner absoluter Score. | ASSUMPTION | Nutzer- und Claims-Test |
| ASM-003 | Der technische Slug kann vorläufig stabil bleiben, auch wenn der öffentliche Name wechselt. | ASSUMPTION | Repo-/Release-Entscheidung |

## Missing Items

| ID | Item | Source Type | Impact |
|---|---|---|---|
| OQ-001 | Finaler öffentlicher Name und markenrechtliche Freigabe | MISSING | Blockiert öffentliche Store-/Domain-Festlegung, nicht die interne Produktplanung |
| OQ-002 | Geschäftsmodell und Preislogik | MISSING | Muss vor kostenintensiver Skalierung, spätestens vor v3, entschieden werden |
| OQ-003 | Finaler Owner/DRI im Repository | MISSING | Vor Umsetzung im Projekt-README benennen |

## Confirmation Status

`pending-user-confirmation`

Die Assistenz bestätigt diese Vision nicht im Namen des Nutzers.
