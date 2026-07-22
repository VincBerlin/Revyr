# NEXT SESSION — PLUMBLINE CONTINUATION PROMPT

Primärer Modus: `DRAFT_FROM_RAW_INPUT`  
Readiness-Level: `BLOCKED_CONTRADICTION`

Du arbeitest im bestehenden REVYR-Projekt weiter. Dies ist kein Greenfield-Neustart und keine neue Produktplanung.

## Kanonische Produktartefakte

- `docs/vision/revyr-endurance-platform.vision.md`
- `docs/canvas/revyr-endurance-platform.canvas.md`
- `docs/prd/revyr-endurance-platform.prd.md`
- `docs/traceability.md`

Lies zusätzlich vollständig:

- `CLAUDE.md`
- `README.md`
- `intake-package.json`, falls vorhanden
- `docs/handoffs/2026-07-20-phase0-activity-time-handoff.md`
- `docs/gaps/revyr-continuation-gap-analysis.md`
- `docs/implementation/revyr-plumbline-continuation-plan.md`
- `docs/EVIDENCE-LEDGER.md`, falls vorhanden
- Package-, TypeScript-, Jest-, Expo- und Native-Konfiguration
- SQLite-Schema, Migrationen, Activity Repository, Tracking State und Tests

## Verbindliche Ausgangslage

- Das bereitgestellte PRD enthält exakt `REQ-001` bis `REQ-036`.
- Es dürfen keine `REQ-037`–`REQ-039` erfunden oder referenziert werden.
- Die zwei früher hochgeladenen PRD-Dateien waren identisch; es gibt nur eine kanonische PRD-Datei.
- Der frühere Handoff wurde unter Commit `5acbcc0` dokumentiert.
- TypeScript war in der alten Session gemeldet grün, ist im aktuellen Checkout aber neu zu reproduzieren.
- Aktivzeit-/Segment-Jest wurde nicht erfolgreich abgeschlossen.
- SQLite-, Segment- und Migration-V2-Arbeit ist vorhanden gemeldet, aber noch nicht als Evidence bestätigt.
- Der berichtete Code pausiert beim App-Hintergrund. Das widerspricht `REQ-003`.
- Produktentscheidung: Eine aktive Session darf beim normalen Wechsel in den Hintergrund nicht automatisch pausieren.
- iOS- und Android-Native-Evidence fehlt.
- Vision, Canvas und PRD werden nicht neu erfunden und nicht dupliziert.
- Bestehende IDs bleiben stabil.
- Keine Planning-Readiness ohne menschliche User Confirmation.
- Keine Git-Remote-, Push-, Reset-, Force-, Branch- oder Löschaktion ohne ausdrückliche Freigabe.

## Arbeitsauftrag

### Schritt 1 — C0-01 Baseline

Inventarisiere den tatsächlichen Checkout und schreibe:

`docs/handoffs/current-baseline-report.md`

Der Bericht muss enthalten:

- aktueller Pfad, Git-Status und HEAD, soweit Git vorhanden ist;
- Dateibaum und relevante Konfiguration;
- Node-/Package-Manager-/Expo-/TypeScript-/Jest-Versionen;
- vorhandene Scripts;
- SQLite-Schema und Migrationen;
- relevante Activity-/Segment-/Tracking-Dateien;
- exakte Befehle für Compile, gezielte Tests, Gesamttests und native Checks;
- Abweichungen zum alten Handoff.

### Schritt 2 — C0-02 Reproduzierbarkeit

Führe die exakten Checks aus. Beginne mit:

1. TypeScript;
2. gezielte Aktivzeit-/Segment-/Repository-Tests seriell;
3. vollständige Jest-Suite;
4. Expo-/Dependency-Diagnose.

Bei Hängern:

- offene Handles, Timer, DB-Verbindungen, Listener und Watcher messen;
- Root Cause beheben;
- nicht `--forceExit` als Lösung verwenden;
- keine Tests überspringen;
- keine Assertions abschwächen, um Grün zu erzeugen.

### Schritt 3 — C0-03 Aktivzeit/Segmente

Prüfe und korrigiere:

- genau ein offenes Segment;
- Start/Pause/Resume/Stop;
- ungültige doppelte Übergänge;
- Aktivzeit ohne Pausen;
- Restart-Stabilität;
- Migration V2;
- Orphan-Cleanup;
- Schließen aller DB-/Timer-/Subscription-Ressourcen.

Aktualisiere ausschließlich auf Basis realer Ergebnisse:

- `docs/EVIDENCE-LEDGER.md`
- `docs/traceability.md`
- `docs/gaps/revyr-continuation-gap-analysis.md`

### Schritt 4 — A0-02 Background Contradiction

Erst nach stabilen Segmenttests:

- lokalisiere das automatische Pause-on-background-Verhalten;
- entkopple Tracking-State vom UI-/AppState-Lifecycle;
- dokumentiere die Plattformarchitektur;
- implementiere zulässiges Background-Tracking;
- definiere eine Acceptance-Matrix für Background, Lockscreen, Crash, OS-Termination und bewusstes Force-Quit;
- teste Run und Bike auf iOS und Android;
- ändere `REQ-003` nicht stillschweigend.

### Schritt 5 — A0 weiterführen

Nach Schließung der Contradiction:

- native Baseline;
- Foreground Run/Bike Smoke;
- GPS-Qualität;
- Routing und routebezogener Fortschritt;
- Verlauf/Export;
- Accessibility, Security und A0-Gate.

## Ausführungsregeln

- Stoppe nicht nach Analyse oder Inventar.
- Implementiere nach der Diagnose den kleinsten sicheren Fix.
- Zeige nach jedem Arbeitspaket:
  - geänderte Dateien;
  - ausgeführte Befehle;
  - Resultate;
  - zugeordnete REQ/AC/EV;
  - verbleibende Blocker.
- Behaupte keinen bestandenen Test oder Build ohne tatsächlichen Exitcode.
- Markiere spätere Anforderungen `REQ-009`–`REQ-033` nicht als A0-Defekte; sie bleiben planmäßig spätere Stufen.
- Kein A1-Start, solange GATE-A0 nicht evidenzbasiert bestanden ist.

Beginne jetzt mit `C0-01`, fahre direkt mit `C0-02` fort und arbeite danach `C0-03` bis zu einem reproduzierbaren Ergebnis ab.
