// mobile/src/services/__tests__/recording-coordinator.test.ts
//
// Integrationstests fuer den RecordingCoordinator gegen echte SQLite (test-adapter)
// und FakeLocationPort. Diese Tests verifizieren:
//  - Zustandsmaschine (idle -> recording -> paused -> recording -> finalized)
//  - Berechtigungsabfrage blockiert start bei denied
//  - Chunks werden per Policy geflusht
//  - Restpuffer wird beim finalize geflusht
//  - Pause haelt die Subscription an, resume nimmt sie wieder auf
//  - Ungueltige Samples werden verworfen, nicht persistiert

import { openTestDatabase } from '../../db/test-adapter';
import { migrateToLatest } from '../../db/migrations';
import { readChunks } from '../../db/chunk-repo';
import { ActivitySessionService } from '../activity-session';
import { RecordingCoordinator, RecordingCoordinatorError } from '../recording-coordinator';
import { everyNSamples, samplesOrMs } from '../chunk-boundary-policy';
import { createFakeLocationPort } from '../../location/fake-location-port';
import type { LocationSample } from '../../location/ports';
import type { SQLiteBinding } from '../../db/ports';
import { deserializePoints } from '../../domain/track-point';
import {
  accuracyFilter,
  jumpFilter,
  pipeline,
  speedFilter,
  stalenessFilter,
} from '../quality';

const NOW = (): string => '2026-07-20T15:00:00Z';

function setup(): {
  db: SQLiteBinding;
  session: ActivitySessionService;
  location: ReturnType<typeof createFakeLocationPort>;
} {
  const db = openTestDatabase();
  migrateToLatest(db, NOW);
  return {
    db,
    session: new ActivitySessionService(db, NOW),
    location: createFakeLocationPort(),
  };
}

// afterEach-Hilfe: sichere Aufraeumen aller Test-Ressourcen (dispose + close).
function teardown(
  db: SQLiteBinding,
  ...coords: RecordingCoordinator[]
): void {
  for (const c of coords) {
    try { c.dispose(); } catch { /* ignore */ }
  }
  try { db.closeSync(); } catch { /* ignore */ }
}

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

describe('RecordingCoordinator — Zustandsmaschine', () => {
  test('idle -> recording via start; permission granted', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(2),
    });
    expect(coord.status().state).toBe('idle');
    await coord.start('run');
    expect(coord.status().state).toBe('recording');
    expect(location.activeSubscriptions()).toBe(1);
    await coord.finalize();
    db.closeSync();
  });

  test('start wirft, wenn permission denied', async () => {
    const { db, session, location } = setup();
    location.setPermissionGranted(false);
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(2),
    });
    await expect(coord.start('run')).rejects.toThrow(RecordingCoordinatorError);
    expect(coord.status().state).toBe('idle');
    expect(location.activeSubscriptions()).toBe(0);
    db.closeSync();
  });

  test('pause storniert Subscription; resume nimmt sie wieder auf', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
    });
    await coord.start('run');
    expect(location.activeSubscriptions()).toBe(1);
    await coord.pause();
    expect(coord.status().state).toBe('paused');
    expect(location.activeSubscriptions()).toBe(0);
    await coord.resume();
    expect(coord.status().state).toBe('recording');
    expect(location.activeSubscriptions()).toBe(1);
    await coord.finalize();
    db.closeSync();
  });

  test('unerlaubte Uebergaenge werfen (idle-Doppelstart, resume-ohne-pause)', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
    });
    await coord.start('run');
    await expect(coord.start('run')).rejects.toThrow(RecordingCoordinatorError);
    await expect(coord.resume()).rejects.toThrow(RecordingCoordinatorError);
    await coord.finalize();
    await expect(coord.pause()).rejects.toThrow(RecordingCoordinatorError);
    db.closeSync();
  });
});

describe('RecordingCoordinator — Sample-Verarbeitung und Flush', () => {
  test('Policy everyNSamples(3): jedes dritte Sample loest Chunk aus', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(3),
    });
    const s = await coord.start('run');
    const activityId = s.session!.activityId;

    location.emit(goodSample({ timestampMs: 1729000000000 }));
    location.emit(goodSample({ timestampMs: 1729000001000 }));
    expect(coord.status().chunksWritten).toBe(0);
    expect(coord.status().bufferSize).toBe(2);

    location.emit(goodSample({ timestampMs: 1729000002000 }));
    expect(coord.status().chunksWritten).toBe(1);
    expect(coord.status().bufferSize).toBe(0);

    // Zwei weitere Chunks
    for (let i = 0; i < 6; i++) {
      location.emit(goodSample({ timestampMs: 1729000003000 + i * 1000 }));
    }
    expect(coord.status().chunksWritten).toBe(3);

    await coord.finalize();
    // Beim finalize war Buffer leer -> kein Extra-Chunk.
    expect(coord.status().chunksWritten).toBe(3);

    const chunks = readChunks(db, activityId);
    expect(chunks.map((c) => c.chunkId)).toEqual([0, 1, 2]);
    expect(chunks.every((c) => c.pointsCount === 3)).toBe(true);
    db.closeSync();
  });

  test('finalize flusht Restpuffer als eigenen Chunk (Policy erlaubt Flush nicht)', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1000), // grosser Puffer
    });
    const s = await coord.start('run');
    const activityId = s.session!.activityId;

    // Nur 3 Samples — Policy wuerde nicht flushen
    location.emit(goodSample({ timestampMs: 1729000000000 }));
    location.emit(goodSample({ timestampMs: 1729000001000 }));
    location.emit(goodSample({ timestampMs: 1729000002000 }));
    expect(coord.status().chunksWritten).toBe(0);
    expect(coord.status().bufferSize).toBe(3);

    await coord.finalize();
    expect(coord.status().chunksWritten).toBe(1);
    expect(coord.status().bufferSize).toBe(0);
    expect(coord.status().lastFlushReason).toContain('finalize');
    const chunks = readChunks(db, activityId);
    expect(chunks).toHaveLength(1);
    expect(chunks[0].pointsCount).toBe(3);
    db.closeSync();
  });

  test('Policy samplesOrMs: Zeitgrenze loest Flush aus, wenn Sample-Grenze nicht erreicht', async () => {
    const { db, session, location } = setup();
    let clock = 1_000_000;
    const coord = new RecordingCoordinator({
      session, location,
      policy: samplesOrMs(1000, 2000),
      nowMs: () => clock,
    });
    await coord.start('run');
    location.emit(goodSample({ timestampMs: clock }));
    expect(coord.status().chunksWritten).toBe(0);
    clock += 2500; // Zeitgrenze knacken
    location.emit(goodSample({ timestampMs: clock }));
    expect(coord.status().chunksWritten).toBe(1);
    expect(coord.status().lastFlushReason).toMatch(/time/);
    await coord.finalize();
    db.closeSync();
  });

  test('Samples waehrend paused werden NICHT verarbeitet (Subscription weg)', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1),
    });
    await coord.start('run');
    location.emit(goodSample());
    expect(coord.status().samplesAccepted).toBe(1);
    await coord.pause();
    // Nach pause ist der Fake-Listener entfernt; emit hat keinen Effekt.
    location.emit(goodSample());
    location.emit(goodSample());
    expect(coord.status().samplesAccepted).toBe(1);
    await coord.resume();
    location.emit(goodSample());
    expect(coord.status().samplesAccepted).toBe(2);
    await coord.finalize();
    db.closeSync();
  });

  test('ungueltige Samples werden verworfen (NaN, ausserhalb WGS84)', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(10),
    });
    await coord.start('run');
    location.emit(goodSample());
    location.emit(goodSample({ latitude: NaN })); // NaN
    location.emit(goodSample({ longitude: 250 })); // ausserhalb [-180,180]
    location.emit(goodSample({ accuracyMeters: Infinity }));
    location.emit(goodSample());
    expect(coord.status().samplesAccepted).toBe(2);
    expect(coord.status().samplesDropped).toBe(3);
    await coord.finalize();
    db.closeSync();
  });

  test('Chunk enthaelt Samples in Empfangsreihenfolge und ist deserialisierbar', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(3),
    });
    const s = await coord.start('run');
    const activityId = s.session!.activityId;
    for (let i = 0; i < 3; i++) {
      location.emit(goodSample({
        timestampMs: 1729000000000 + i * 1000,
        latitude: 52.5 + i * 0.001,
      }));
    }
    await coord.finalize();
    const chunks = readChunks(db, activityId);
    const points = deserializePoints(chunks[0].pointsJson);
    expect(points.map((p) => p.timestampMs)).toEqual([
      1729000000000, 1729000001000, 1729000002000,
    ]);
    expect(points.every((p) => p.source === 'foreground')).toBe(true);
    expect(points.every((p) => p.quality === 'raw')).toBe(true);
    teardown(db, coord);
  });
});

describe('RecordingCoordinator — dispose', () => {
  test('dispose vor start ist ein No-Op-Zustandswechsel', () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1),
    });
    expect(coord.isDisposed()).toBe(false);
    coord.dispose();
    expect(coord.isDisposed()).toBe(true);
    // Idempotent
    coord.dispose();
    coord.dispose();
    expect(coord.isDisposed()).toBe(true);
    db.closeSync();
  });

  test('dispose waehrend recording storniert die Subscription', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
    });
    await coord.start('run');
    expect(location.activeSubscriptions()).toBe(1);
    coord.dispose();
    expect(location.activeSubscriptions()).toBe(0);
    expect(coord.isDisposed()).toBe(true);
    db.closeSync();
  });

  test('nach dispose werfen start/pause/resume/finalize', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1),
    });
    coord.dispose();
    await expect(coord.start('run')).rejects.toThrow(RecordingCoordinatorError);
    await expect(coord.pause()).rejects.toThrow(RecordingCoordinatorError);
    await expect(coord.resume()).rejects.toThrow(RecordingCoordinatorError);
    await expect(coord.finalize()).rejects.toThrow(RecordingCoordinatorError);
    db.closeSync();
  });

  test('dispose finalisiert die Aktivitaet NICHT (bleibt Recovery-Fall)', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
    });
    const st = await coord.start('run');
    coord.dispose();
    // Aktivitaet ist noch unfinalisiert -> Recovery beim naechsten Bootstrap
    const svc = new ActivitySessionService(db, NOW);
    const resumed = svc.resume(st.session!.activityId);
    expect(resumed.finalized).toBe(false);
    svc.finalize(resumed);
    db.closeSync();
  });
});

describe('RecordingCoordinator — Subscription-Lifecycle', () => {
  test('pause/resume-Zyklus: activeSubscriptions bleibt konsistent', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1000),
    });
    await coord.start('run');
    for (let i = 0; i < 5; i++) {
      expect(location.activeSubscriptions()).toBe(1);
      await coord.pause();
      expect(location.activeSubscriptions()).toBe(0);
      await coord.resume();
    }
    await coord.finalize();
    expect(location.activeSubscriptions()).toBe(0);
    teardown(db, coord);
  });

  test('doppelter pause wirft; Subscription bleibt gekuendigt', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1000),
    });
    await coord.start('run');
    await coord.pause();
    await expect(coord.pause()).rejects.toThrow(RecordingCoordinatorError);
    expect(location.activeSubscriptions()).toBe(0);
    await coord.resume();
    await coord.finalize();
    teardown(db, coord);
  });

  test('finalize aus paused: Subscription bleibt gekuendigt', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1000),
    });
    await coord.start('run');
    location.emit(goodSample());
    await coord.pause();
    await coord.finalize();
    expect(location.activeSubscriptions()).toBe(0);
    expect(coord.status().chunksWritten).toBe(1); // Restpuffer
    teardown(db, coord);
  });
});

describe('RecordingCoordinator — flushBuffer / Distanz / latestSample / lastVerdict', () => {
  test('flushBuffer schreibt bufferSize>0 raus, ohne Zustandswechsel', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
    });
    await coord.start('run');
    location.emit(goodSample());
    location.emit(goodSample());
    expect(coord.status().bufferSize).toBe(2);
    expect(coord.status().chunksWritten).toBe(0);
    coord.flushBuffer('test');
    expect(coord.status().bufferSize).toBe(0);
    expect(coord.status().chunksWritten).toBe(1);
    expect(coord.status().lastFlushReason).toBe('test');
    expect(coord.status().state).toBe('recording');
    await coord.finalize();
    teardown(db, coord);
  });

  test('flushBuffer bei leerem Buffer ist No-Op (kein leerer Chunk)', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
    });
    await coord.start('run');
    coord.flushBuffer('test'); // Buffer leer
    expect(coord.status().chunksWritten).toBe(0);
    await coord.finalize();
    teardown(db, coord);
  });

  test('flushBuffer auf disposed Coordinator wirft', () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1),
    });
    coord.dispose();
    expect(() => coord.flushBuffer('test')).toThrow(RecordingCoordinatorError);
    db.closeSync();
  });

  test('totalDistanceM akkumuliert haversine-Distanz zwischen akzeptierten Samples', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
    });
    await coord.start('run');
    location.emit(goodSample({ latitude: 52.5, longitude: 13.4 }));
    expect(coord.status().totalDistanceM).toBe(0); // erster Sample: keine Distanz
    // Etwa 111 m Nord
    location.emit(goodSample({ latitude: 52.501, longitude: 13.4, timestampMs: 1729000001000 }));
    const d1 = coord.status().totalDistanceM;
    expect(d1).toBeGreaterThan(100);
    expect(d1).toBeLessThan(120);
    // Weitere ~111 m Nord
    location.emit(goodSample({ latitude: 52.502, longitude: 13.4, timestampMs: 1729000002000 }));
    const d2 = coord.status().totalDistanceM;
    expect(d2).toBeGreaterThan(d1);
    expect(d2 - d1).toBeGreaterThan(100);
    expect(d2 - d1).toBeLessThan(120);
    await coord.finalize();
    teardown(db, coord);
  });

  test('rejected Sample fliesst NICHT in totalDistanceM ein', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
      qualityPipeline: pipeline(speedFilter({ rejectAboveMps: 25 })),
    });
    await coord.start('run');
    location.emit(goodSample({ latitude: 52.5, speedMps: 5 }));
    // rejected wegen speed
    location.emit(goodSample({ latitude: 52.6, speedMps: 100 }));
    expect(coord.status().totalDistanceM).toBe(0);
    // akzeptiert; Distanz ab dem ersten Sample (nicht dem verworfenen)
    location.emit(goodSample({ latitude: 52.501, speedMps: 5, timestampMs: 1729000010000 }));
    const d = coord.status().totalDistanceM;
    expect(d).toBeGreaterThan(100);
    expect(d).toBeLessThan(120);
    await coord.finalize();
    teardown(db, coord);
  });

  test('latestSample wird immer geschrieben, auch bei rejected', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
      qualityPipeline: pipeline(speedFilter({ rejectAboveMps: 25 })),
    });
    await coord.start('run');
    location.emit(goodSample({ speedMps: 5 }));
    expect(coord.status().latestSample?.speedMps).toBe(5);
    location.emit(goodSample({ speedMps: 100 })); // rejected
    expect(coord.status().latestSample?.speedMps).toBe(100);
    await coord.finalize();
    teardown(db, coord);
  });

  test('lastVerdict spiegelt den Ergebnis des letzten Pipeline-Laufs', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
      qualityPipeline: pipeline(accuracyFilter({ acceptedBelowM: 20, rejectAboveM: 100 })),
    });
    await coord.start('run');
    location.emit(goodSample({ accuracyMeters: 5 }));
    expect(coord.status().lastVerdict?.quality).toBe('accepted');
    location.emit(goodSample({ accuracyMeters: 50 }));
    expect(coord.status().lastVerdict?.quality).toBe('low-confidence');
    location.emit(goodSample({ accuracyMeters: 500 }));
    expect(coord.status().lastVerdict?.quality).toBe('rejected');
    await coord.finalize();
    teardown(db, coord);
  });

  test('ohne Pipeline: lastVerdict bleibt null', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(100),
    });
    await coord.start('run');
    location.emit(goodSample());
    expect(coord.status().lastVerdict).toBeNull();
    await coord.finalize();
    teardown(db, coord);
  });
});

describe('RecordingCoordinator — Aktivzeit (activeMs)', () => {
  test('activeMs waechst waehrend recording und friert bei pause ein', async () => {
    const { db, session, location } = setup();
    let clock = 1_000_000;
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1000),
      nowMs: () => clock,
    });
    await coord.start('run');
    expect(coord.status().activeMs).toBe(0);
    clock += 60_000;
    expect(coord.status().activeMs).toBe(60_000);
    await coord.pause();
    expect(coord.status().activeMs).toBe(60_000);
    // Pause: 5 min sollten NICHT dazuzaehlen
    clock += 5 * 60_000;
    expect(coord.status().activeMs).toBe(60_000);
    await coord.resume();
    clock += 30_000;
    expect(coord.status().activeMs).toBe(90_000);
    await coord.finalize();
    // Nach finalize aendert sich activeMs nicht mehr
    const after = coord.status().activeMs;
    clock += 10_000;
    expect(coord.status().activeMs).toBe(after);
    teardown(db, coord);
  });

  test('activeMs wird beim start einer neuen Session zurueckgesetzt', async () => {
    // Zwei aufeinanderfolgende Aktivitaeten in derselben DB, zwei Coordinator-
    // Instanzen (Produktionsmuster: pro Recording ein frischer Coordinator).
    const { db, session } = setup();
    let clock = 1_000_000;
    const location1 = createFakeLocationPort();
    const c1 = new RecordingCoordinator({
      session, location: location1, policy: everyNSamples(1000),
      nowMs: () => clock,
    });
    await c1.start('run');
    clock += 60_000;
    await c1.finalize();
    expect(c1.status().activeMs).toBe(60_000);
    c1.dispose();

    const location2 = createFakeLocationPort();
    const c2 = new RecordingCoordinator({
      session, location: location2, policy: everyNSamples(1000),
      nowMs: () => clock,
    });
    await c2.start('ride');
    // Frische Session -> activeMs bei 0
    expect(c2.status().activeMs).toBe(0);
    clock += 30_000;
    expect(c2.status().activeMs).toBe(30_000);
    await c2.finalize();
    teardown(db, c2);
  });

  test('resumeFrom uebernimmt bereits akkumulierte Aktivzeit aus der DB', async () => {
    const db = openTestDatabase();
    require('../../db/migrations').migrateToLatest(db, NOW);
    const svc = new ActivitySessionService(db, NOW);

    // Coordinator 1: 45 s aktiv, dann pause
    let clock = 1_000_000;
    const c1 = new RecordingCoordinator({
      session: svc, location: createFakeLocationPort(),
      policy: everyNSamples(1000), nowMs: () => clock,
    });
    const s = await c1.start('run');
    const activityId = s.session!.activityId;
    clock += 45_000;
    await c1.pause();
    c1.dispose();

    // Coordinator 2: resumeFrom mit derselben Session
    const c2 = new RecordingCoordinator({
      session: svc, location: createFakeLocationPort(),
      policy: everyNSamples(1000), nowMs: () => clock,
    });
    const resumed = svc.resume(activityId);
    await c2.resumeFrom(resumed);
    // Direkt nach resumeFrom sind 45 s aus dem geschlossenen Segment da,
    // neues offenes Segment liefert 0 zusaetzliche ms.
    expect(c2.status().activeMs).toBe(45_000);
    clock += 30_000;
    expect(c2.status().activeMs).toBe(75_000);
    await c2.finalize();
    teardown(db, c2);
  });
});

describe('RecordingCoordinator — Quality-Pipeline-Integration', () => {
  test('ohne Pipeline: alle Samples tragen quality=raw', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1),
    });
    const s = await coord.start('run');
    location.emit(goodSample());
    await coord.finalize();
    const chunks = readChunks(db, s.session!.activityId);
    const points = deserializePoints(chunks[0].pointsJson);
    expect(points[0].quality).toBe('raw');
    teardown(db, coord);
  });

  test('mit accuracy-Filter: high accuracy -> low-confidence, ueber Schwelle -> rejected', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1),
      qualityPipeline: pipeline(accuracyFilter({ acceptedBelowM: 20, rejectAboveM: 100 })),
    });
    const s = await coord.start('run');
    location.emit(goodSample({ accuracyMeters: 5 }));   // accepted
    location.emit(goodSample({ accuracyMeters: 50 }));  // low-confidence
    location.emit(goodSample({ accuracyMeters: 200 })); // rejected -> dropped
    await coord.finalize();
    expect(coord.status().samplesAccepted).toBe(2);
    expect(coord.status().samplesDropped).toBe(1);
    const chunks = readChunks(db, s.session!.activityId);
    const allPoints = chunks.flatMap((c) => deserializePoints(c.pointsJson));
    expect(allPoints.map((p) => p.quality)).toEqual(['accepted', 'low-confidence']);
    teardown(db, coord);
  });

  test('speedFilter: unmoegliche Geschwindigkeit fuehrt zu Verwerfung', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1),
      qualityPipeline: pipeline(speedFilter({ rejectAboveMps: 25 })),
    });
    await coord.start('run');
    location.emit(goodSample({ speedMps: 5 }));   // ok
    location.emit(goodSample({ speedMps: 50 }));  // rejected
    await coord.finalize();
    expect(coord.status().samplesAccepted).toBe(1);
    expect(coord.status().samplesDropped).toBe(1);
    teardown(db, coord);
  });

  test('jumpFilter: rejected Sample schiebt Vorgaenger NICHT vor (kein Cascade-Rausch)', async () => {
    const { db, session, location } = setup();
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1),
      qualityPipeline: pipeline(jumpFilter({ rejectAboveM: 500, rejectAboveMps: 25 })),
    });
    await coord.start('run');
    // 1. Sample: kein Vorgaenger, accepted.
    location.emit(goodSample({ timestampMs: 1729000000000, latitude: 52.5 }));
    // 2. Sample: 1,1 km Sprung in 1 s -> rejected.
    location.emit(goodSample({ timestampMs: 1729000001000, latitude: 52.51 }));
    // 3. Sample: kleiner Schritt vom URSPRUNGSpunkt 52.5 (nicht vom Rausch-Spike),
    //    weil der rejected Sample den Vorgaenger nicht vorschieben durfte.
    location.emit(goodSample({ timestampMs: 1729000010000, latitude: 52.500009 }));
    await coord.finalize();
    expect(coord.status().samplesAccepted).toBe(2);
    expect(coord.status().samplesDropped).toBe(1);
    teardown(db, coord);
  });

  test('stalenessFilter: veralteter Zeitstempel wird verworfen', async () => {
    const { db, session, location } = setup();
    const now = 1729000060000;
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1),
      qualityPipeline: pipeline(stalenessFilter({ maxAgeMs: 30000, nowMs: () => now })),
    });
    await coord.start('run');
    location.emit(goodSample({ timestampMs: now - 10000 })); // fresh
    location.emit(goodSample({ timestampMs: now - 60000 })); // stale -> rejected
    await coord.finalize();
    expect(coord.status().samplesAccepted).toBe(1);
    expect(coord.status().samplesDropped).toBe(1);
    teardown(db, coord);
  });

  test('kombinierte Pipeline: mehrere Filter greifen zusammen', async () => {
    const { db, session, location } = setup();
    const now = 1729000060000;
    const coord = new RecordingCoordinator({
      session, location, policy: everyNSamples(1),
      qualityPipeline: pipeline(
        stalenessFilter({ maxAgeMs: 30000, nowMs: () => now }),
        accuracyFilter({ acceptedBelowM: 20, rejectAboveM: 100 }),
        speedFilter({ rejectAboveMps: 25 }),
      ),
    });
    await coord.start('run');
    // ok
    location.emit(goodSample({ timestampMs: now, accuracyMeters: 5, speedMps: 5 }));
    // low-confidence (accuracy)
    location.emit(goodSample({ timestampMs: now, accuracyMeters: 50, speedMps: 5 }));
    // rejected (staleness) — wuerde auch accuracy rejecten, aber staleness kommt zuerst
    location.emit(goodSample({ timestampMs: now - 60000, accuracyMeters: 5, speedMps: 5 }));
    // rejected (speed)
    location.emit(goodSample({ timestampMs: now, accuracyMeters: 5, speedMps: 50 }));
    await coord.finalize();
    expect(coord.status().samplesAccepted).toBe(2); // accepted + low-confidence
    expect(coord.status().samplesDropped).toBe(2);
    teardown(db, coord);
  });
});
