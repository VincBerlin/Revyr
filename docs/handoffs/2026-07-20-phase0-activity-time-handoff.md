# Phase-0 · Aktivzeit-Modell — Handoff

Erstellt am: 2026-07-20 (Ende der Runde 11)
Handoff-Typ: WIP — nicht verifiziert, nicht release-fähig.
Grund: Sandbox-Erschöpfung wärend der Verifikation (Disk 94 % voll, Jest-Läufe
ohne Ausgabe abgebrochen). Der Nutzer hat ausdrücklich "sichern ohne weitere
Analyse" angeordnet.

---

## 1. Repository-Zustand

| Feld | Wert |
|---|---|
| Repo-Root | `/Users/vincentschnetzer/Documents/Run&Bike` |
| Branch bei Handoff-Erstellung | `main` |
| Handoff-Branch (nach Commit) | `wip/phase0-activity-time-handoff` |
| Letzter verifizierter Commit auf `main` | **`4de1199`** — `feat(mobile): Diagnostics-Screen + ErrorBoundary + Android-Prebuild + Runtime-Fehler` |
| Remote | keiner konfiguriert (`git init`-lokal seit Runde 6) |

Letzte 6 Commits auf `main`:

```
4de1199 feat(mobile): Diagnostics-Screen + ErrorBoundary + Android-Prebuild + Runtime-Fehler
71c6909 feat(mobile): Recording-App mit Home/Sport/Recording/Detail + Background-Flush
748ae6d feat(mobile): Quality-Pipeline + AppState-Bridge + dispose + Dev-Build
2e7024b feat(mobile): LocationPort + RecordingCoordinator + Gap-Guard + Smoke-Test-Vorbereitung
9405f48 feat(mobile): Activity-Persistence-Flow — Bootstrap, SessionService, Dev-UI
091706e chore: gitignore tool-generated .claude/ and .claude-flow/ under mobile/
```

## 2. Uncommitted Änderungen (Runde 11)

### 2.1 Modified — 19 Dateien

```
 M mobile/bun.lock
 M mobile/jest.config.js
 M mobile/package.json
 M mobile/src/db/__tests__/activity-repo.test.ts
 M mobile/src/db/__tests__/bootstrap.test.ts
 M mobile/src/db/__tests__/chunk-repo.test.ts
 M mobile/src/db/__tests__/migrations.test.ts
 M mobile/src/db/__tests__/recovery.test.ts
 M mobile/src/db/bootstrap.ts
 M mobile/src/db/migrations.ts
 M mobile/src/services/__tests__/activity-session.test.ts
 M mobile/src/services/__tests__/app-state-bridge.test.ts
 M mobile/src/services/__tests__/background-flush.test.ts
 M mobile/src/services/__tests__/recording-coordinator.test.ts
 M mobile/src/services/__tests__/restart-recovery.test.ts
 M mobile/src/services/activity-session.ts
 M mobile/src/services/recording-coordinator.ts
 M mobile/src/ui/screens/DetailScreen.tsx
 M mobile/src/ui/screens/RecordingScreen.tsx
```

### 2.2 Untracked — 5 gewollt + 2 iCloud-Duplikate (ausgeschlossen)

Gewollt (in Commit aufgenommen):

```
mobile/src/__mocks__/react-native.tsx
mobile/src/db/__tests__/segment-repo.test.ts
mobile/src/db/segment-repo.ts
mobile/src/ui/__tests__/DiagnosticsScreen.test.tsx
mobile/src/ui/__tests__/ErrorBoundary.test.tsx
```

**NICHT** in Commit aufgenommen (iCloud-/Finder-Sync-Duplikate, wahrscheinlich
durch versehentliche Datei-Duplizierung im Finder entstanden):

```
mobile/app 2.json
mobile/src/db/__tests__/activity-repo.test 2.ts
```

Diese zwei Dateien mit ` 2`-Suffix bleiben untracked. Der Nutzer entscheidet,
ob sie zu löschen oder Änderungen daraus zu übernehmen sind.

## 3. Was inhaltlich umgesetzt wurde

### Aktivzeit-Modell (persistent, Neustart-fest)

- **Migration V1 → V2** (`mobile/src/db/migrations.ts`): neue Tabelle
  `activity_segments (activity_id, segment_index, started_at, ended_at)`
  mit Backfill (ein Segment pro existierender Aktivität). `CURRENT_SCHEMA_VERSION`
  auf 2 gehoben; `migrateToLatest()` als Einstiegspunkt.
- **`mobile/src/db/segment-repo.ts`** (neu): `startSegment`, `closeOpenSegment`,
  `listSegments`, `findOpenSegment`, `closedActiveMs`.
- **Bootstrap** (`mobile/src/db/bootstrap.ts`): ruft `migrateToLatest` und
  `closeOrphanedSegments` auf; `RecoveryReport` um `activeMs` erweitert;
  `BootstrapReport` um `orphansClosed` erweitert.
- **ActivitySessionService** (`mobile/src/services/activity-session.ts`): `start`
  öffnet Segment 0; `pauseSession`/`resumeSession` neu; `finalize` schließt offenes
  Segment; `getClosedActiveMs`, `hasOpenSegment` neu.
- **RecordingCoordinator** (`mobile/src/services/recording-coordinator.ts`):
  `RecordingStatus.activeMs` neu; interner `closedActiveMsCache` +
  `openSegmentStartMs`; `pause`/`resume`/`finalize` schließen/öffnen Segmente
  über den Service; `resumeFrom` übernimmt bereits akkumulierte Aktivzeit.
- **UI**: `RecordingScreen` zeigt Aktivzeit (statt Wall-Clock);
  `DetailScreen` zeigt Aktivzeit + Gesamtzeit + Segment-Anzahl.

### Neue Tests (nicht verifiziert lauffähig)

- `mobile/src/db/__tests__/segment-repo.test.ts` — Segment-CRUD, `closedActiveMs`
- `mobile/src/db/__tests__/migrations.test.ts` — V2 + `migrateToLatest`
- `mobile/src/db/__tests__/bootstrap.test.ts` — `closeOrphanedSegments`
- `mobile/src/services/__tests__/activity-session.test.ts` — Segment-Lifecycle
- `mobile/src/services/__tests__/recording-coordinator.test.ts` — `activeMs`
- `mobile/src/services/__tests__/restart-recovery.test.ts` — Aktivzeit über Restart
- `mobile/src/ui/__tests__/ErrorBoundary.test.tsx` (neu, Component-Test)
- `mobile/src/ui/__tests__/DiagnosticsScreen.test.tsx` (neu, Component-Test)

### Test-Infrastruktur

- `react-test-renderer@19` + `@types/react-test-renderer` als devDependencies
- `mobile/src/__mocks__/react-native.tsx` — Passthrough-Mock für Component-Tests
- `jest.config.js` — testMatch um `*.test.tsx` erweitert; `react-native` in
  `moduleNameMapper`
- `package.json` — `test` ohne `--forceExit`, neu `test:force` als Diagnose

### sed-Umstellung der Test-Helper

`migrateToV1(` → `migrateToLatest(` in 8 Test-Dateien (jede Test-Suite braucht
V2, weil `sessionService.start` jetzt die `activity_segments`-Tabelle beschreibt).

## 4. Verifikationsstand

| Prüfung | Ergebnis |
|---|---|
| **TypeScript** (`tsc --noEmit --skipLibCheck`) | **grün** — EXIT 0, zweifach bestätigt (einmal nach anfänglichen zwei TS-2367-Fehlern in den Component-Tests, die auf `n.type === 'Pressable'` → `typeof n.props.onPress === 'function'` umgestellt wurden). |
| **Jest** (`bun run test`) | **nicht abgeschlossen / nicht verifiziert** — mehrere Läufe ohne Testausgabe abgebrochen. Grund: Disk 94 % voll, kein persistenter ts-jest-Cache. |
| **expo-doctor** | **nicht ausgeführt** |
| **expo install --check** | **nicht ausgeführt** |
| **expo export --platform ios** | **nicht ausgeführt in dieser Runde** (letzter grüner Bundle-Smoke: Runde 10, 725 Module) |
| **expo export --platform android** | **nicht ausgeführt in dieser Runde** (letzter grüner Bundle-Smoke: Runde 10) |
| **Simulator/Geräte-Lauf** | **strukturell blockiert** (kein Xcode.app, kein CocoaPods, kein Android SDK, kein Java in dieser Sandbox — Blocker aus Runde 10 unverändert) |

## 5. Offene Gaps

1. **Jest-Läufe verifizieren.** Die 20+ neuen Tests sind nie durchgelaufen — die
   Implementierung ist ungeprüft gegen ihre eigenen Tests.
2. **Konsistenz zwischen Coordinator-Cache und DB-Segmenten.** `RecordingCoordinator.pause()`
   schließt das Segment via `sessionService.pauseSession(this.session)`; ein
   möglicher Fehlerfall (DB-Wurf) würde den `closedActiveMsCache` und den
   DB-Zustand desynchronisieren. Kein Test deckt das ab.
2a. **`resumeFrom` erwartet, dass Bootstrap Orphans bereits geschlossen hat.**
    Wenn ein Aufrufer `sessionService.resume()` direkt ruft (ohne den
    `initializeDatabase`-Fluss), könnte ein offenes Segment aus einem früheren
    Lauf existieren. `resumeSession` würde dann ein weiteres Segment öffnen —
    zwei parallele offene Segmente pro Aktivität. Kein Test.
3. **`iCloud`-Duplikate** (`app 2.json`, `activity-repo.test 2.ts`) — vom Nutzer
   zu klären.
4. **`expo-doctor` / `expo install --check`** noch nicht gelaufen; könnten
   Version-Drift-Warnungen aufdecken.
5. **Restart-Recovery-Test** in `restart-recovery.test.ts` nutzt eine ungewöhnliche
   Struktur (return einer Promise-Kette aus einer sync `test`-Funktion). Auf
   TypeScript-Ebene akzeptiert, aber die Testlaufzeit-Semantik ist nicht
   verifiziert.

## 6. Nächster sicherer Schritt

Nach diesem Handoff (bevor `main`-Merge):

1. **Auf einer Umgebung mit gesundem Disk-Free-Space** den Branch
   `wip/phase0-activity-time-handoff` auschecken.
2. `cd mobile && bun install` (installiert die neuen devDependencies).
3. `bun run test` — die neuen Suiten müssen grün laufen. Bei Fehlern:
   Fixes im WIP-Branch, dann neuer Commit.
4. `bunx expo-doctor` + `bunx expo install --check` — Version-Drift beheben.
5. `bunx expo export --platform ios` und `--platform android` — Bundle-Smoke.
6. Erst nach 3–5 grün: Merge in `main`.
7. `mobile/app 2.json` und `mobile/src/db/__tests__/activity-repo.test 2.ts`:
   entscheiden, ob löschen oder Inhalt übernehmen. **Nicht** blind hinzufügen.

## 7. Sandbox-Kontext (zur Wiederherstellung nützlich)

- **Disk-Auslastung** (Ende Runde 11): 94 % voll (`/dev/disk3s3s1`, 12 GiB used
  / 6 GiB free). Ist möglicherweise die primäre Ursache für Jest-Hänger.
- **`node_modules/.cache`** wurde in einem früheren Aufruf gelöscht (`rm -rf`),
  wodurch ts-jest jeden Testlauf komplett neu transpilieren muss.
- **Kein Xcode.app**, kein CocoaPods, kein Android SDK, kein Java in der Sandbox.
