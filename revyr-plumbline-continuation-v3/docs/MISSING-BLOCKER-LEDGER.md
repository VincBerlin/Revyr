# Missing / Assumption / Blocker Ledger

Readiness-Level: `BLOCKED_CONTRADICTION`

| ID | Field | Source Type | Severity | Reason | Blocks |
|---|---|---|---|---|---|
| BLK-001 | Background-Tracking | CONTRADICTION | blocker | berichteter Code pausiert beim Background-Wechsel, PRD verlangt fortlaufendes Tracking | GATE-A0 |
| BLK-002 | Aktivzeit-/Segmenttests | BLOCKER | blocker | Jest-Lauf wurde nicht erfolgreich abgeschlossen | REQ-002, REQ-005 |
| BLK-003 | Migration/Restart-Evidence | BLOCKER | blocker | Migration V2, Orphan-Cleanup und Restart-Stabilität sind unbestätigt | REQ-005 |
| BLK-004 | Native iOS-/Android-Evidence | BLOCKER | blocker | Builds und reale Kern-Smokes fehlen | REQ-003, REQ-036 |
| BLK-005 | Evidence Ledger | BLOCKER | blocker | alte Berichtsaussagen dürfen nicht als bestandene Evidence gelten | REQ-035 |
| MISS-001 | aktueller TypeScript-/Teststatus | MISSING | warning | neuer archivierter Checkout wurde noch nicht reproduziert | C0 |
| MISS-002 | App-Kill-Semantik | MISSING | warning | Crash/OS-Termination und Force-Quit benötigen getrennte Acceptance | REQ-003 |
| MISS-003 | Product Owner/DRI | MISSING | warning | vor Gate-Abnahme benennen | Governance |
| MISS-004 | Referenzgeräte/OS | MISSING | warning | vor Feldtests festlegen | GATE-A0 |
| MISS-005 | öffentlicher Name | MISSING | info | blockiert erst Store-/Domain-Freigabe | GATE-A2 |
| MISS-006 | Backend/Routing/Claims/Business | MISSING | info | an späteren Gates entscheiden | B–E |
| ASM-001 | C0 Recovery Gate | ASSUMPTION | info | Delivery-Gate zur sicheren Wiederaufnahme; kein Produktfeature | none |
