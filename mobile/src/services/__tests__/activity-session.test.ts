// mobile/src/services/__tests__/activity-session.test.ts
import { openTestDatabase } from '../../db/test-adapter';
import { migrateToLatest } from '../../db/migrations';
import { readChunks, highestChunkId, writeChunk, buildChunk } from '../../db/chunk-repo';
import { getActivity } from '../../db/activity-repo';
import {
  ActivitySessionError,
  ActivitySessionService,
  ResumeWithGapsError,
} from '../activity-session';
import type { TrackPointV1 } from '../../domain/track-point';
import type { SQLiteBinding } from '../../db/ports';

const NOW = (): string => '2026-07-20T15:00:00Z';

function freshService(): { db: SQLiteBinding; svc: ActivitySessionService } {
  const db = openTestDatabase();
  migrateToLatest(db, NOW);
  return { db, svc: new ActivitySessionService(db, NOW) };
}

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

describe('ActivitySessionService.start / appendChunk / finalize', () => {
  test('start liefert Session mit nextChunkId=0, nicht finalisiert', () => {
    const { db, svc } = freshService();
    const s = svc.start('run');
    expect(s.activityId).toBeGreaterThan(0);
    expect(s.sport).toBe('run');
    expect(s.nextChunkId).toBe(0);
    expect(s.finalized).toBe(false);
    db.closeSync();
  });

  test('appendChunk gibt neue Session mit nextChunkId+1 zurueck (immutable)', () => {
    const { db, svc } = freshService();
    const s0 = svc.start('run');
    const { session: s1 } = svc.appendChunk(s0, makePoints(3));
    // Original-Session unveraendert (Immutability-Regel)
    expect(s0.nextChunkId).toBe(0);
    expect(s1.nextChunkId).toBe(1);
    // Und der Chunk landet mit ID 0 in der DB
    expect(highestChunkId(db, s0.activityId)).toBe(0);
    db.closeSync();
  });

  test('drei Chunks schreiben ergibt drei Chunks in DB, nextChunkId=3', () => {
    const { db, svc } = freshService();
    let s = svc.start('run');
    for (let i = 0; i < 3; i++) {
      const out = svc.appendChunk(s, makePoints(2, i * 2));
      s = out.session;
      expect(out.write.inserted).toBe(true);
    }
    expect(s.nextChunkId).toBe(3);
    const chunks = readChunks(db, s.activityId);
    expect(chunks.map((c) => c.chunkId)).toEqual([0, 1, 2]);
    db.closeSync();
  });

  test('appendChunk auf finalisierte Session wirft', () => {
    const { db, svc } = freshService();
    const s0 = svc.start('run');
    const s1 = svc.finalize(s0);
    expect(() => svc.appendChunk(s1, makePoints(1))).toThrow(ActivitySessionError);
    db.closeSync();
  });

  test('finalize auf bereits finalisierte Session wirft', () => {
    const { db, svc } = freshService();
    const s0 = svc.start('run');
    const s1 = svc.finalize(s0);
    expect(() => svc.finalize(s1)).toThrow(ActivitySessionError);
    db.closeSync();
  });

  test('finalize schreibt finalized_at in DB', () => {
    const { db, svc } = freshService();
    const s0 = svc.start('run');
    svc.finalize(s0);
    const act = getActivity(db, s0.activityId);
    expect(act?.finalizedAt).toBe(NOW());
    db.closeSync();
  });
});

describe('ActivitySessionService.resume', () => {
  test('resume liefert Session mit nextChunkId = highestChunkId + 1', () => {
    const { db, svc } = freshService();
    let s = svc.start('run');
    s = svc.appendChunk(s, makePoints(2)).session;
    s = svc.appendChunk(s, makePoints(2)).session;
    s = svc.appendChunk(s, makePoints(2)).session;
    // nextChunkId ist 3, dh. highest ist 2

    // Neue Service-Instanz simuliert App-Neustart mit derselben DB
    const svc2 = new ActivitySessionService(db, NOW);
    const resumed = svc2.resume(s.activityId);
    expect(resumed.nextChunkId).toBe(3);
    expect(resumed.finalized).toBe(false);
    db.closeSync();
  });

  test('resume auf Aktivitaet ohne Chunks liefert nextChunkId=0', () => {
    const { db, svc } = freshService();
    const s = svc.start('run');
    const svc2 = new ActivitySessionService(db, NOW);
    const resumed = svc2.resume(s.activityId);
    expect(resumed.nextChunkId).toBe(0);
    db.closeSync();
  });

  test('resume auf unbekannte ID wirft', () => {
    const { db, svc } = freshService();
    void svc; // silence unused
    const svc2 = new ActivitySessionService(db, NOW);
    expect(() => svc2.resume(99999)).toThrow(ActivitySessionError);
    db.closeSync();
  });

  test('resume auf finalisierte Aktivitaet wirft', () => {
    const { db, svc } = freshService();
    const s = svc.start('run');
    svc.finalize(s);
    const svc2 = new ActivitySessionService(db, NOW);
    expect(() => svc2.resume(s.activityId)).toThrow(ActivitySessionError);
    db.closeSync();
  });
});

describe('ActivitySessionService — Segment-Lifecycle', () => {
  function fixedClock() {
    let ms = Date.parse('2026-07-20T10:00:00Z');
    return {
      clock: (): string => new Date(ms).toISOString(),
      advance: (deltaMs: number): void => { ms += deltaMs; },
    };
  }

  test('start oeffnet Segment 0 mit demselben Zeitstempel wie die Aktivitaet', () => {
    const db = openTestDatabase();
    require('../../db/migrations').migrateToLatest(db, NOW);
    const svc = new ActivitySessionService(db, NOW);
    const s = svc.start('run');
    expect(svc.hasOpenSegment(s.activityId)).toBe(true);
    db.closeSync();
  });

  test('pauseSession schliesst offenes Segment; resumeSession oeffnet ein neues', () => {
    const { clock, advance } = fixedClock();
    const db = openTestDatabase();
    require('../../db/migrations').migrateToLatest(db, clock);
    const svc = new ActivitySessionService(db, clock);
    const s = svc.start('run');
    advance(60_000);
    svc.pauseSession(s);
    expect(svc.hasOpenSegment(s.activityId)).toBe(false);
    expect(svc.getClosedActiveMs(s.activityId)).toBe(60_000);
    advance(120_000); // Pause: 2 min sollen NICHT als Aktivzeit zaehlen
    svc.resumeSession(s);
    expect(svc.hasOpenSegment(s.activityId)).toBe(true);
    advance(30_000);
    svc.pauseSession(s);
    expect(svc.getClosedActiveMs(s.activityId)).toBe(60_000 + 30_000);
    db.closeSync();
  });

  test('finalize schliesst noch offenes Segment mit', () => {
    const { clock, advance } = fixedClock();
    const db = openTestDatabase();
    require('../../db/migrations').migrateToLatest(db, clock);
    const svc = new ActivitySessionService(db, clock);
    const s = svc.start('run');
    advance(45_000);
    svc.finalize(s);
    expect(svc.hasOpenSegment(s.activityId)).toBe(false);
    expect(svc.getClosedActiveMs(s.activityId)).toBe(45_000);
    db.closeSync();
  });

  test('doppelte pauseSession ist idempotent (schliesst nichts, kein Fehler)', () => {
    const { clock } = fixedClock();
    const db = openTestDatabase();
    require('../../db/migrations').migrateToLatest(db, clock);
    const svc = new ActivitySessionService(db, clock);
    const s = svc.start('run');
    svc.pauseSession(s);
    svc.pauseSession(s);
    svc.pauseSession(s);
    expect(svc.hasOpenSegment(s.activityId)).toBe(false);
    db.closeSync();
  });
});

describe('ActivitySessionService.resume — Gap-Guard', () => {
  // Kunstlich Luecke erzeugen: Chunks 0, 1, 3 schreiben (2 fehlt).
  function withGap(): { db: ReturnType<typeof openTestDatabase>; activityId: number; svc: ActivitySessionService } {
    const { db, svc } = freshService();
    const s = svc.start('run');
    writeChunk(db, buildChunk(s.activityId, 0, []), NOW());
    writeChunk(db, buildChunk(s.activityId, 1, []), NOW());
    writeChunk(db, buildChunk(s.activityId, 3, []), NOW());
    return { db, activityId: s.activityId, svc: new ActivitySessionService(db, NOW) };
  }

  test('resume ohne acknowledgeGaps wirft ResumeWithGapsError, wenn Luecken existieren', () => {
    const { db, activityId, svc } = withGap();
    try {
      svc.resume(activityId);
      throw new Error('sollte gescheitert sein');
    } catch (e) {
      expect(e).toBeInstanceOf(ResumeWithGapsError);
      const err = e as ResumeWithGapsError;
      expect(err.activityId).toBe(activityId);
      expect(err.gaps).toEqual([2]);
      expect(err.message).toContain('Luecken');
    }
    db.closeSync();
  });

  test('resume mit acknowledgeGaps=true erlaubt Uebergang trotz Luecken', () => {
    const { db, activityId, svc } = withGap();
    const s = svc.resume(activityId, { acknowledgeGaps: true });
    // highest ist 3 -> nextChunkId 4
    expect(s.nextChunkId).toBe(4);
    db.closeSync();
  });

  test('resume mit acknowledgeGaps=false wirft ebenfalls (kein truthy-Trick)', () => {
    const { db, activityId, svc } = withGap();
    expect(() => svc.resume(activityId, { acknowledgeGaps: false }))
      .toThrow(ResumeWithGapsError);
    db.closeSync();
  });

  test('resume mit acknowledgeGaps ist irrelevant, wenn keine Luecken existieren', () => {
    const { db, svc } = freshService();
    const s = svc.start('run');
    writeChunk(db, buildChunk(s.activityId, 0, []), NOW());
    writeChunk(db, buildChunk(s.activityId, 1, []), NOW());
    const resumed = svc.resume(s.activityId); // OHNE opts
    expect(resumed.nextChunkId).toBe(2);
    db.closeSync();
  });
});
