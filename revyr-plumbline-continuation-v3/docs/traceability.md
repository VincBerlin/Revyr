# Traceability Matrix: REVYR Endurance Platform

Feature Slug: `revyr-endurance-platform`  
Status: blocked

## Scope

Diese Matrix verwendet exakt die 36 kanonischen Requirements aus dem bereitgestellten PRD. Die Struktur ist vollständig verknüpft; der Ausführungsstatus bleibt wegen ungeklärter Implementierungs-Evidence blockiert.

| Trace ID | Vision Item ID | Canvas Item ID | Requirement ID | Acceptance Criteria ID | Evidence Needed | Status | Source Type |
|---|---|---|---|---|---|---|---|
| TRC-001 | VIS-005 | CAN-005 | REQ-001 | AC-001 | Konfigurations-Unit-Tests und Screen-Checkliste für iOS/Android. | draft | EXPLICIT |
| TRC-002 | VIS-005 | CAN-005 | REQ-002 | AC-002 | Gerätetest je Sport und Plattform auf Referenzstrecke. | blocked | BLOCKER |
| TRC-003 | VIS-005 | CAN-005 | REQ-003 | AC-003 | 30-Minuten-Kill-/Background-Test je Plattform und Sport. | contradiction | CONTRADICTION |
| TRC-004 | VIS-005 | CAN-005 | REQ-004 | AC-004 | Drift-, Tunnel-, Sprung- und Hochgeschwindigkeits-Fixtures. | draft | ASSUMPTION |
| TRC-005 | VIS-005 | CAN-005 | REQ-005 | AC-005 | SQLite-Repository-Tests, Kill-Test und Migrations-Fixtures. | blocked | BLOCKER |
| TRC-006 | VIS-005 | CAN-005 | REQ-006 | AC-006 | Routing-Service-Tests und zehn reale Routenszenarien je Sport. | draft | EXPLICIT |
| TRC-007 | VIS-005 | CAN-005 | REQ-007 | AC-007 | Polyline-Projektions-Fixtures und reale Abweichungstests. | draft | ASSUMPTION |
| TRC-008 | VIS-005 | CAN-005 | REQ-008 | AC-008 | Repository-, UI- und GPX-Kompatibilitätstest. | draft | EXPLICIT |
| TRC-009 | VIS-003 | CAN-003 | REQ-009 | AC-009 | Echte Geräte und BLE-Gurt je Plattform. | draft | EXPLICIT |
| TRC-010 | VIS-003 | CAN-003 | REQ-010 | AC-010 | Formeltests mit/ohne HF und UI-Test des Warum-Sheets. | draft | ASSUMPTION |
| TRC-011 | VIS-003 | CAN-003 | REQ-011 | AC-011 | Zonen-Unit-Tests und Kopfhörer-Gerätetest. | draft | EXPLICIT |
| TRC-012 | VIS-003 | CAN-003 | REQ-012 | AC-012 | Zeitmessung, Fixture-Korrelation und Copy-Review. | draft | EXPLICIT |
| TRC-013 | VIS-003 | CAN-003 | REQ-013 | AC-013 | Wochen-Fixtures und Claims-Lint. | draft | EXPLICIT |
| TRC-014 | VIS-005 | CAN-007 | REQ-014 | AC-014 | Token-Review, Accessibility- und Screenreader-Check. | draft | EXPLICIT |
| TRC-015 | VIS-004 | CAN-005 | REQ-015 | AC-015 | Idempotenz- und Unlock-Fixtures. | draft | EXPLICIT |
| TRC-016 | VIS-004 | CAN-005 | REQ-016 | AC-016 | Bildexport-, Widget- und Privacy-Snapshot-Test. | draft | EXPLICIT |
| TRC-017 | VIS-009 | CAN-011 | REQ-017 | AC-017 | E2E-Flow, Offline-Test und Löschungsnachweis. | draft | EXPLICIT |
| TRC-018 | VIS-009 | CAN-011 | REQ-018 | AC-018 | Sichtbarkeits-Matrix, Zwei-Account- und Moderationstest. | draft | EXPLICIT |
| TRC-019 | VIS-009 | CAN-011 | REQ-019 | AC-019 | Zwei-Account-E2E-Flow. | draft | EXPLICIT |
| TRC-020 | VIS-008 | CAN-005 | REQ-020 | AC-020 | Datenbanktransaktions- und Zwei-Geräte-Test. | draft | EXPLICIT |
| TRC-021 | VIS-008 | CAN-005 | REQ-021 | AC-021 | Zeitfenster- und Integrations-Fixtures. | draft | EXPLICIT |
| TRC-022 | VIS-008 | CAN-005 | REQ-022 | AC-022 | Pure-Function-Fixtures und Zwei-Geräte-Eventtest. | draft | EXPLICIT |
| TRC-023 | VIS-008 | CAN-005 | REQ-023 | AC-023 | Monte-Carlo-/Szenariosimulation und Kalibrierungsbericht. | draft | EXPLICIT |
| TRC-024 | VIS-008 | CAN-005 | REQ-024 | AC-024 | Betrugs-/Grenzfall-Fixtures und False-Positive-Review. | draft | ASSUMPTION |
| TRC-025 | VIS-008 | CAN-005 | REQ-025 | AC-025 | Deterministische Fixtures und Wiederholungs-Test. | draft | EXPLICIT |
| TRC-026 | VIS-010 | CAN-011 | REQ-026 | AC-026 | Geo-Fixtures, Simulation und Karten-Lasttest. | draft | EXPLICIT |
| TRC-027 | VIS-010 | CAN-011 | REQ-027 | AC-027 | Zwei-Season-Integrationstest und Unveränderlichkeitsprüfung. | draft | EXPLICIT |
| TRC-028 | VIS-010 | CAN-011 | REQ-028 | AC-028 | Geo-Fixture-Suite, Property-Tests und Threat-Model. | draft | ASSUMPTION |
| TRC-029 | VIS-010 | CAN-011 | REQ-029 | AC-029 | OSM-Access-Review, realer Bahn-Test und Reward-Fixtures. | draft | ASSUMPTION |
| TRC-030 | VIS-009 | CAN-008 | REQ-030 | AC-030 | Threat-Model, Endpfad-Matrix und Penetrationstest. | draft | EXPLICIT |
| TRC-031 | VIS-009 | CAN-008 | REQ-031 | AC-031 | Kontrollierte Falltests, Fehlalarmstatistik und Claims-Review. | draft | EXPLICIT |
| TRC-032 | VIS-007 | CAN-005 | REQ-032 | AC-032 | Gerätematrix und reale Integrationstests. | draft | EXPLICIT |
| TRC-033 | VIS-007 | CAN-005 | REQ-033 | AC-033 | Claims-Lint, Rechtsfreigabe und Privacy-Test. | draft | EXPLICIT |
| TRC-034 | VIS-009 | CAN-007 | REQ-034 | AC-034 | Security-Review, RLS-Tests, Datenflussdiagramm und Löschungsnachweis. | draft | EXPLICIT |
| TRC-035 | VIS-010 | CAN-010 | REQ-035 | AC-035 | CI-Regel, Ledger-Review und Gate-Checkliste. | draft | EXPLICIT |
| TRC-036 | VIS-010 | CAN-007 | REQ-036 | AC-036 | TestFlight/Internal-Test-Bericht, Policy-Matrix und Gate-Sign-off. | draft | EXPLICIT |

## Status Interpretation

- `contradiction`: Produktanforderung und berichteter aktueller Codezustand widersprechen sich.
- `blocked`: Requirement ist im aktuellen A0-Handoff betroffen, aber die benötigte Evidence fehlt.
- `draft`: strukturell vollständig verknüpft, jedoch noch nicht als implementiert oder bestanden nachgewiesen.

## Validation Rule

Jede `REQ-*` aus `docs/prd/revyr-endurance-platform.prd.md` erscheint genau einmal in dieser Matrix.
