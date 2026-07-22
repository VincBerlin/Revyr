# REVYR — Gegenüberstellung und korrigierte Gap-Analyse

Readiness-Level: `BLOCKED_CONTRADICTION`  
Mode: `DRAFT_FROM_RAW_INPUT`  
Feature Slug: `revyr-endurance-platform`

## 1. Executive Decision

Die bereitgestellten Vision-, Canvas- und PRD-Dateien bleiben die kanonische Produktbasis. Sie werden nicht durch eine neue Produktidee ersetzt und nicht in ein Greenfield-Konzept umgeschrieben.

Die richtige Fortsetzung ist:

1. Produktbaseline unverändert sichern.
2. Den von Claude hinterlassenen A0-/Phase-0-Codebestand reproduzierbar prüfen.
3. Aktivzeit-, Segment- und SQLite-Evidence schließen.
4. Den Widerspruch beim Background-Tracking beheben.
5. Erst danach Routing, Verlauf/Export und die übrigen A0-Gates abschließen.
6. A1 Health beginnt erst nach bestandenem A0-Gate.

## 2. Source Map

| Source ID | Quelle | Rolle | Source Type |
|---|---|---|---|
| SRC-001 | bereitgestellte Product Vision | Produktabsicht, Zielgruppe, Wert, Grenzen und Erfolgssignale | EXPLICIT |
| SRC-002 | bereitgestellter Product Canvas | Problem, Nutzer, Value Promise, Scope, Risiken und Gates | EXPLICIT |
| SRC-003 | bereitgestelltes PRD; beide hochgeladenen PRD-Dateien sind inhaltsgleich | 36 Requirements, 36 Acceptance Criteria und 36 Evidence-Einträge | EXPLICIT |
| SRC-004 | bisherige Claude-/Terminal-Session | Handoff-Stand `5acbcc0`, TypeScript damals gemeldet grün, Aktivzeit-/Segment-Jest nicht abgeschlossen | EXPLICIT |
| SRC-005 | bisherige Claude-/Terminal-Session | Berichteter Background-Code pausiert beim App-Hintergrund statt weiterzuzeichnen | EXPLICIT |
| SRC-006 | Plumbline-Regeln | Artefakttrennung, Source Types, Traceability und Bestätigungsgate | EXPLICIT |

## 3. Korrektur der früheren Gap-Analyse

| Frühere Aussage | Prüfung gegen die bereitgestellten Dateien | Korrektur |
|---|---|---|
| Es existieren 39 Requirements. | Das kanonische PRD enthält exakt `REQ-001` bis `REQ-036`. | Verbindlich sind 36 Requirements. |
| `REQ-037` und `REQ-039` werden als Gaps referenziert. | Diese IDs existieren im bereitgestellten PRD nicht. | Alle Verweise auf `REQ-037`–`REQ-039` werden entfernt. |
| Readiness war `READY_FOR_USER_CONFIRMATION`, obwohl kritische Blocker und eine Contradiction gelistet waren. | Plumbline erlaubt keine Ready-Einstufung bei einem ungelösten Widerspruch. | Gesamtstatus ist `BLOCKED_CONTRADICTION`. |
| Der Handoff wurde teilweise wie eine bestätigte Implementierung behandelt. | TypeScript war nur in der alten Session gemeldet; Jest und native Evidence fehlen. | Handoff-Aussagen gelten als `EXPLICIT` berichtet, aber nicht als bestandene Evidence. |
| C0 wurde teilweise mit Produktanforderungen vermischt. | C0 ist kein neues Produktfeature. | C0 wird ausschließlich als Delivery-/Recovery-Gate geführt. |
| Traceability wurde mit 39 Zeilen beschrieben. | Das PRD besitzt 36 REQs, ACs und EVs. | Die korrigierte Matrix enthält exakt 36 Zeilen. |

## 4. Alte Planung gegen aktuellen Handoff

| Bereich | Kanonische Planung | Berichteter Stand bei Claude-Handoff | Gap-Typ | Verbindliche Entscheidung |
|---|---|---|---|---|
| Produktvision | Health-first, danach Community, Teams, Territory und Safety in gestuften Gates | Kein Hinweis, dass die Vision fachlich verworfen wurde | kein Produkt-Gap | Vision bleibt unverändert |
| Zielgruppe und Problem | Läufer:innen, Radfahrer:innen, Gruppen und Vereine; Trackingdaten müssen verständlich werden | nicht implementierungsabhängig | kein Produkt-Gap | keine Neuplanung |
| `REQ-001` SportConfig | Run/Bike zentral konfigurieren; keine duplizierte Screenlogik | teilweise umgesetzt oder unbestätigt | MISSING | Codeinventar und Tests gegen SportConfig durchführen |
| `REQ-002` Foreground-Tracking | Start, GPS, Dauer, Distanz, Karte und sportgerechte Kernmetrik | Recording- und Aktivzeitcode vorhanden gemeldet | BLOCKER | gezielte Unit-/Integrationstests und realer Smoke-Test |
| `REQ-003` Background/Pause/Recovery | Background-Tracking muss weiterlaufen; Pause/Resume und Recovery sind Pflicht | AppState-Hintergrund soll flushen und pausieren | CONTRADICTION | Produktanforderung bleibt; Implementierung wird korrigiert |
| `REQ-004` GPS-Modell/Filter | Qualitätsmetadaten und deterministische Filter | teilweise vorhanden oder unbestätigt | MISSING | Datenmodell, Filter-Fixtures und Grenzfälle prüfen |
| `REQ-005` lokale Speicherung | versionierte, transaktionale SQLite-Persistenz | SQLite und Aktivzeitsegmente vorhanden gemeldet; Migration/Tests unbestätigt | BLOCKER | Migration V2, Segment-Lifecycle und Restart-Stabilität verifizieren |
| `REQ-006` Routenplanung | Wegpunkte/Distanzziel und sportgerechtes Routing | nicht als abgeschlossen belegt | MISSING | nach Trackingstabilisierung umsetzen |
| `REQ-007` Routenfortschritt | Fortschritt entlang Geometrie, Off-Route und falsche Richtung | nicht als abgeschlossen belegt | MISSING | Projection-/Off-Route-Domainlogik mit Fixtures |
| `REQ-008` Verlauf/Export | Verlauf, Detail, Wiederverwendung und GPX | teilweise vorhanden oder unbestätigt | MISSING | Repository-, UI- und Exporttests |
| `REQ-014` Accessibility | Tokens, Dynamic Type, Screenreader, AA-Kontraste | keine aktuelle Evidence | MISSING | A0-Audit und Gerätetest |
| `REQ-034` Security/Privacy | keine Secrets im Client, Datenminimierung und sichere Grenzen | Anbieter-/Proxyentscheidung offen | MISSING | keine Produktionssecrets im Client; ADR vor Routing-Release |
| `REQ-035` Evidence | kein Done ohne Tests und reale Gerätedaten | jüngste Evidence unvollständig | BLOCKER | Ledger auf tatsächlich ausgeführte Nachweise zurücksetzen |
| `REQ-036` Release Gates | iOS/Android, Policies und Testtracks pro Stufe | native Builds nicht belegt | BLOCKER | beide Plattformen bauen und smoke-testen |
| `REQ-009`–`REQ-013` Health | A1 nach A0 | noch nicht maßgeblich | kein aktueller Defekt | nicht vorziehen |
| `REQ-015`–`REQ-033` spätere Stufen | A2 bis E | nicht maßgeblich für aktuellen Recovery-Schritt | kein aktueller Defekt | nicht als A0-Lücke fehlinterpretieren |

## 5. Kritische Gaps

| Gap ID | Gap | Marker | Betroffene IDs | Exit Condition |
|---|---|---|---|---|
| GAP-001 | Aktivzeit-/Segment-Jest-Läufe wurden nicht erfolgreich abgeschlossen. | BLOCKER | REQ-002, REQ-005, AC-002, AC-005, EV-002, EV-005 | gezielte und vollständige Jest-Suite reproduzierbar grün, ohne `--forceExit` |
| GAP-002 | Der aktuelle `Revyr-clean`-Checkout wurde nach dem Archivieren nicht neu kompiliert. | MISSING | REQ-035 | TypeScript-Befehl mit gespeichertem Exitcode und Log |
| GAP-003 | Background-Implementierung widerspricht `REQ-003`. | CONTRADICTION | REQ-003, AC-003, EV-003 | aktive Session zeichnet im zulässigen Hintergrundmodell weiter; manuelle/Auto-Pause allein stoppt Aktivzeit |
| GAP-004 | Migration V2, Segmente und Orphan-Cleanup sind nicht belastbar nachgewiesen. | BLOCKER | REQ-005, AC-005, EV-005 | Migrations-, Lifecycle-, Restart- und Cleanup-Tests grün |
| GAP-005 | iOS- und Android-Native-Baseline fehlt. | BLOCKER | REQ-003, REQ-036 | Build und Kern-Smoke auf beiden Plattformen dokumentiert |
| GAP-006 | `App-Kill` in `AC-003` unterscheidet nicht zwischen Crash/OS-Termination und bewusstem Force-Quit. | MISSING | REQ-003, AC-003 | technische Acceptance-Matrix definiert erreichbares Verhalten je Beendigungsart |
| GAP-007 | Routing und routebezogener Fortschritt sind nicht abgenommen. | MISSING | REQ-006, REQ-007 | Domain-Fixtures, Provider-ADR und reale Routenszenarien bestanden |
| GAP-008 | Evidence Ledger kann ältere Berichtsaussagen mit bestandener Evidence vermischen. | BLOCKER | REQ-035, alle EV | jeder Eintrag besitzt `pending`, `reported-unverified`, `passed`, `failed` oder `blocked` plus Log-/Testreferenz |
| GAP-009 | Product Owner und Referenzgeräte fehlen. | MISSING | OQ-003, OQ-005 | DRI vor Gate-Abnahme; Gerätematrix vor Feldtest |
| GAP-010 | Name, Backend, Routinganbieter, Claims und Geschäftsmodell sind offen. | MISSING | OQ-001–OQ-006 | an ihren späteren Gates entscheiden; blockiert nicht C0-Kern |

## 6. Scope Decision

### Jetzt erlaubt

- Handoff inventarisieren und reproduzieren.
- Tests reparieren, ohne Erwartungen künstlich abzuschwächen.
- Aktivzeit-, Segment-, SQLite- und Recovery-Logik stabilisieren.
- Background-Tracking gemäß `REQ-003` entwerfen und umsetzen.
- iOS-/Android-Baseline herstellen.
- A0-Traceability und Evidence aktualisieren.

### Jetzt nicht erlaubt

- Vision, Canvas oder PRD neu erfinden.
- neue konkurrierende Requirement-IDs anlegen.
- A1 Health, Social, Teams oder Territory vorziehen.
- fehlende Tests mit `skip`, `only`, `--forceExit` oder gelockerten Assertions kaschieren.
- Secrets im Client ablegen.
- Builds oder Tests als bestanden markieren, wenn nur Code gelesen wurde.

## 7. Readiness Decision

- **Produktdefinition:** vollständig genug für Fortsetzung und Nutzerprüfung.
- **Strukturelle Traceability:** 36/36 Requirements sind verknüpfbar.
- **Implementierungsstand:** wegen `REQ-003` und fehlender A0-Evidence blockiert.
- **Gesamtstatus:** `BLOCKED_CONTRADICTION`.
