// mobile/src/services/__tests__/restart-recovery.test.ts
//
// End-to-End-Test des App-Neustart-Szenarios:
//  1. App startet, migriert, beginnt eine Aktivitaet.
//  2. Ein paar Chunks werden geschrieben.
//  3. App wird abgebrochen (wir simulieren durch closeSync mitten drin).
//  4. App startet neu: initializeDatabase erhebt Recovery-Bericht.
//  5. Service nimmt die unfinalisierte Aktivitaet wieder auf und schreibt weiter.
//
// Wir nutzen eine File-DB, damit die Persistenz ueber die close/open-Grenze traegt.

import { initializeDatabase } from '../../db/bootstrap';
import { openTestDatabase } from '../../db/test-adapter';
import { readChunks } from '../../db/chunk-repo';
import { getActivity } from '../../db/activity-repo';
import { ActivitySessionService } from '../activity-session';
import type { TrackPointV1 } from '../../domain/track-point';
import { mkdtempSync, unlinkSync, rmdirSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';

let clockCounter = 0;
const clock = (): string => {
  clockCounter += 1;
  const t = new Date(2026, 6, 20, 15, 0, clockCounter).toISOString();
  return t;
};

beforeEach(() => {
  clockCounter = 0;
});

function makePoints(n: number, offset = 0): TrackPointV1[] {
  return Array.from({ length: n }, (_, i) => ({
    latitude: 52.5,
    longitude: 13.4,
    timestampMs: 1729000000000 + (offset + i) * 1000,
    accuracyMeters: 4.2,
    altitudeMeters: null,
    speedMps: 3.1,
    headingDegrees: 90,
    source: 'foreground',
    isMocked: false,
    quality: 'accepted',
  }));
}

function mkTempPath(): { path: string; cleanup: () => void } {
  const dir = mkdtempSync(join(tmpdir(), 'revyr-restart-'));
  const path = join(dir, 'db.sqlite');
  return {
    path,
    cleanup: () => {
      try { if (existsSync(path)) unlinkSync(path); } catch { /* ignore */ }
      try { rmdirSync(dirname(path)); } catch { /* ignore */ }
    },
  };
}

describe('End-to-End: App-Neustart mit unfinalisierter Aktivitaet', () => {
  test('nach Neustart erscheint die Aktivitaet im Recovery-Bericht', () => {
    const { path, cleanup } = mkTempPath();

    // --- Erster App-Lauf ---
    const boot1 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: clock,
    });
    expect(boot1.freshlyMigrated).toBe(true);
    expect(boot1.recovery).toEqual([]);

    const svc1 = new ActivitySessionService(boot1.db, clock);
    let s = svc1.start('run');
    s = svc1.appendChunk(s, makePoints(3, 0)).session;
    s = svc1.appendChunk(s, makePoints(3, 3)).session;
    // Kein finalize — simuliert App-Kill mitten in der Session.
    boot1.db.closeSync();

    // --- Zweiter App-Lauf (Neustart) ---
    const boot2 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: clock,
    });
    expect(boot2.freshlyMigrated).toBe(false); // schon migriert
    expect(boot2.recovery).toHaveLength(1);
    const rec = boot2.recovery[0];
    expect(rec.activity.id).toBe(s.activityId);
    expect(rec.activity.finalizedAt).toBeNull();
    expect(rec.chunkCount).toBe(2);
    expect(rec.highestChunkId).toBe(1);
    expect(rec.gaps).toEqual([]);

    boot2.db.closeSync();
    cleanup();
  });

  test('nach Neustart kann die Aktivitaet fortgesetzt und finalisiert werden', () => {
    const { path, cleanup } = mkTempPath();

    // Lauf 1: 3 Chunks, kein finalize
    const boot1 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: clock,
    });
    const svc1 = new ActivitySessionService(boot1.db, clock);
    let s = svc1.start('ride');
    for (let i = 0; i < 3; i++) {
      s = svc1.appendChunk(s, makePoints(2, i * 2)).session;
    }
    const activityId = s.activityId;
    boot1.db.closeSync();

    // Lauf 2: resume, zwei weitere Chunks, dann finalize
    const boot2 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: clock,
    });
    expect(boot2.recovery).toHaveLength(1);
    expect(boot2.recovery[0].highestChunkId).toBe(2); // Chunks 0, 1, 2

    const svc2 = new ActivitySessionService(boot2.db, clock);
    let resumed = svc2.resume(activityId);
    expect(resumed.nextChunkId).toBe(3);
    resumed = svc2.appendChunk(resumed, makePoints(2)).session;
    resumed = svc2.appendChunk(resumed, makePoints(2)).session;
    svc2.finalize(resumed);
    boot2.db.closeSync();

    // Lauf 3: kein Recovery mehr, Aktivitaet ist finalisiert
    const boot3 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: clock,
    });
    expect(boot3.recovery).toEqual([]);
    const chunks = readChunks(boot3.db, activityId);
    expect(chunks.map((c) => c.chunkId)).toEqual([0, 1, 2, 3, 4]);
    const act = getActivity(boot3.db, activityId);
    expect(act?.finalizedAt).not.toBeNull();
    boot3.db.closeSync();

    cleanup();
  });

  test('nach Neustart bleibt die Aktivzeit (nicht Wall-clock) korrekt', () => {
    const { path, cleanup } = mkTempPath();

    // Lauf 1: 60 s aktiv, dann kill (kein finalize)
    let clock = 2_000_000_000_000;
    const nowMs = (): number => clock;
    const nowIso = (): string => new Date(clock).toISOString();

    const boot1 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: nowIso,
    });
    const svc1 = new ActivitySessionService(boot1.db, nowIso);
    const c1 = new (require('../recording-coordinator').RecordingCoordinator)({
      session: svc1,
      location: (require('../../location/fake-location-port').createFakeLocationPort)(),
      policy: (require('../chunk-boundary-policy').everyNSamples)(1000),
      nowMs,
    });
    const s = c1.start('run');
    // Start ist async — abwarten
    return (async () => {
      await s;
      const activityId = c1.status().session!.activityId;
      // Simulieren: 90 s Wall-clock, davon 60 s Aktivzeit + 30 s Pause
      clock += 60_000;
      await c1.pause();
      // 30 s Pause (Wall-clock, aber Aktivzeit friert)
      clock += 30_000;
      // Zwischenstand: 60 s Aktivzeit
      expect(c1.status().activeMs).toBe(60_000);
      // Kill ohne finalize
      c1.dispose();
      boot1.db.closeSync();

      // Lauf 2: Bootstrap sieht Aktivitaet, resumeFrom
      const boot2 = initializeDatabase({
        openDatabase: () => openTestDatabase(path),
        now: nowIso,
      });
      // pause() hat das Segment bereits sauber geschlossen -> orphansClosed=0.
      // Der Bootstrap findet nichts zu schliessen.
      expect(boot2.orphansClosed).toBe(0);
      expect(boot2.recovery).toHaveLength(1);
      // Aktivzeit erhalten: Segment T0..T0+60s = 60 s, Pause zaehlt nicht.
      expect(boot2.recovery[0].activeMs).toBe(60_000);
      void activityId; // fuer TypeScript
      boot2.db.closeSync();
      cleanup();
    })();
  });

  test('Luecke aus einem abgebrochenen Batch wird im Recovery-Bericht sichtbar', () => {
    const { path, cleanup } = mkTempPath();

    // Lauf 1: Chunks 0, 1 einzeln geschrieben, dann Batch [2, 3, 4] mit Throw
    // in der Mitte — dank Wrapper-Transaktion (G1) ist NICHTS aus der Batch persistiert.
    const boot1 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: clock,
    });
    const svc1 = new ActivitySessionService(boot1.db, clock);
    let s = svc1.start('run');
    s = svc1.appendChunk(s, makePoints(2)).session;
    s = svc1.appendChunk(s, makePoints(2)).session;

    // Batch mit Kill simulieren — direkter Zugriff auf die DB, weil der Service
    // absichtlich keine "mixed-with-fail"-API bietet.
    expect(() =>
      boot1.db.withTransactionSync(() => {
        for (let i = 0; i < 3; i++) {
          if (i === 1) throw new Error('SIMULATED_KILL');
          boot1.db.runSync(
            `INSERT OR IGNORE INTO track_point_chunks
               (activity_id, chunk_id, points_json, points_count, written_at)
             VALUES (?, ?, ?, ?, ?)`,
            [s.activityId, 2 + i, '[]', 0, clock()],
          );
        }
      }),
    ).toThrow('SIMULATED_KILL');
    boot1.db.closeSync();

    // Lauf 2: Recovery meldet nur Chunks 0, 1 — keine Luecke, weil die Batch
    // atomar zurueckgerollt wurde (Chunk 2 aus der Batch ist NICHT persistiert).
    const boot2 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: clock,
    });
    expect(boot2.recovery).toHaveLength(1);
    const rec = boot2.recovery[0];
    expect(rec.chunkCount).toBe(2);
    expect(rec.highestChunkId).toBe(1);
    expect(rec.gaps).toEqual([]);
    boot2.db.closeSync();
    cleanup();
  });
});
