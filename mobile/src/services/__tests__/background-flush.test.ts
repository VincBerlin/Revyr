// mobile/src/services/__tests__/background-flush.test.ts
//
// End-to-End: AppStateBridge auf 'background' waehrend recording ->
// Buffer wird VOR pause() transaktional geflusht -> DB schliessen ->
// DB neu oeffnen -> geflushter Chunk ist da.

import { initializeDatabase } from '../../db/bootstrap';
import { openTestDatabase } from '../../db/test-adapter';
import { readChunks } from '../../db/chunk-repo';
import { getActivity } from '../../db/activity-repo';
import { ActivitySessionService } from '../activity-session';
import { RecordingCoordinator } from '../recording-coordinator';
import { everyNSamples } from '../chunk-boundary-policy';
import { createFakeLocationPort } from '../../location/fake-location-port';
import { AppStateBridge } from '../app-state-bridge';
import { createFakeAppStateSource } from '../fake-app-state-source';
import type { LocationSample } from '../../location/ports';
import { mkdtempSync, unlinkSync, rmdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';

const NOW = (): string => '2026-07-20T15:00:00Z';

function goodSample(overrides: Partial<LocationSample> = {}): LocationSample {
  return {
    latitude: 52.5,
    longitude: 13.4,
    timestampMs: 1729000000000,
    accuracyMeters: 4.2,
    altitudeMeters: null,
    speedMps: 3.1,
    headingDegrees: 90,
    isMocked: true,
    ...overrides,
  };
}

function mkTempPath(): { path: string; cleanup: () => void } {
  const dir = mkdtempSync(join(tmpdir(), 'revyr-bg-flush-'));
  const path = join(dir, 'bg.sqlite');
  return {
    path,
    cleanup: () => {
      try { unlinkSync(path); } catch { /* ignore */ }
      try { rmdirSync(dirname(path)); } catch { /* ignore */ }
    },
  };
}

describe('Background-Wechsel flusht Buffer transaktional vor pause()', () => {
  test('offener Chunk landet vor pause() in der DB', async () => {
    const { db, session, location } = (() => {
      const d = openTestDatabase();
      require('../../db/migrations').migrateToLatest(d, NOW);
      return { db: d, session: new ActivitySessionService(d, NOW), location: createFakeLocationPort() };
    })();
    // Grosse Policy, sodass ohne Background-Flush KEIN Chunk geschrieben wuerde
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1000),
    });
    const source = createFakeAppStateSource();
    const events: string[] = [];
    const bridge = new AppStateBridge({
      coordinator: coord, source, onEvent: (m) => events.push(m),
    });
    bridge.attach();

    const s = await coord.start('run');
    location.emit(goodSample());
    location.emit(goodSample());
    location.emit(goodSample());
    expect(coord.status().bufferSize).toBe(3);
    expect(coord.status().chunksWritten).toBe(0);

    source.set('background');
    await new Promise((r) => setTimeout(r, 10));

    // pause() ist gelaufen; Subscription weg
    expect(coord.status().state).toBe('paused');
    // ABER: der Buffer ist VOR pause() geflusht worden
    expect(coord.status().bufferSize).toBe(0);
    expect(coord.status().chunksWritten).toBe(1);
    // Event log dokumentiert den Flush
    expect(events.some((e) => e.includes('1 Chunk(s) geflusht'))).toBe(true);
    // In der DB liegt der Chunk
    const chunks = readChunks(db, s.session!.activityId);
    expect(chunks).toHaveLength(1);
    expect(chunks[0].pointsCount).toBe(3);

    await coord.finalize();
    bridge.detach();
    coord.dispose();
    db.closeSync();
  });

  test('leerer Buffer: nichts wird geflusht, Log meldet "nichts zu flushen"', async () => {
    const db = openTestDatabase();
    require('../../db/migrations').migrateToLatest(db, NOW);
    const coord = new RecordingCoordinator({
      session: new ActivitySessionService(db, NOW),
      location: createFakeLocationPort(),
      policy: everyNSamples(1000),
    });
    const source = createFakeAppStateSource();
    const events: string[] = [];
    const bridge = new AppStateBridge({
      coordinator: coord, source, onEvent: (m) => events.push(m),
    });
    bridge.attach();

    await coord.start('run');
    // KEINE Samples eingespeist
    source.set('background');
    await new Promise((r) => setTimeout(r, 10));

    expect(coord.status().state).toBe('paused');
    expect(coord.status().chunksWritten).toBe(0);
    expect(events.some((e) => e.includes('nichts zu flushen'))).toBe(true);

    await coord.finalize();
    bridge.detach();
    coord.dispose();
    db.closeSync();
  });

  test('kill/reopen: nach Background-Flush ist der Chunk in einer neuen DB-Instanz sichtbar', async () => {
    const { path, cleanup } = mkTempPath();

    // ---- App-Lauf 1: recording + background + close ----
    const boot1 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: NOW,
    });
    const svc1 = new ActivitySessionService(boot1.db, NOW);
    const coord1 = new RecordingCoordinator({
      session: svc1,
      location: createFakeLocationPort(),
      policy: everyNSamples(1000),
    });
    const source1 = createFakeAppStateSource();
    const events: string[] = [];
    const bridge1 = new AppStateBridge({
      coordinator: coord1, source: source1, onEvent: (m) => events.push(m),
    });
    bridge1.attach();

    const s = await coord1.start('run');
    const activityId = s.session!.activityId;
    const loc1 = (coord1 as any).deps.location as ReturnType<typeof createFakeLocationPort>;
    loc1.emit(goodSample());
    loc1.emit(goodSample());
    expect(coord1.status().bufferSize).toBe(2);
    expect(coord1.status().chunksWritten).toBe(0);

    source1.set('background');
    await new Promise((r) => setTimeout(r, 10));
    expect(coord1.status().chunksWritten).toBe(1);

    // Simulierter App-Kill: dispose + close DB, ohne finalize
    bridge1.detach();
    coord1.dispose();
    boot1.db.closeSync();

    // ---- App-Lauf 2: reopen ----
    const boot2 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: NOW,
    });
    expect(boot2.freshlyMigrated).toBe(false);
    // Recovery-Bericht muss die Aktivitaet mit 1 Chunk zeigen
    expect(boot2.recovery).toHaveLength(1);
    expect(boot2.recovery[0].chunkCount).toBe(1);
    // Chunk ist in der DB
    const chunks = readChunks(boot2.db, activityId);
    expect(chunks).toHaveLength(1);
    expect(chunks[0].pointsCount).toBe(2);
    // Aktivitaet ist noch nicht finalisiert
    expect(getActivity(boot2.db, activityId)?.finalizedAt).toBeNull();
    boot2.db.closeSync();
    cleanup();
  });
});
