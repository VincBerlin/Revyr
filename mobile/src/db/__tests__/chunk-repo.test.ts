// mobile/src/db/__tests__/chunk-repo.test.ts
import { openTestDatabase } from '../test-adapter';
import { migrateToLatest } from '../migrations';
import { startActivity } from '../activity-repo';
import {
  buildChunk,
  findGaps,
  highestChunkId,
  readChunks,
  writeChunk,
  writeChunkBatch,
  type Chunk,
} from '../chunk-repo';
import type { TrackPointV1 } from '../../domain/track-point';

const NOW = (): string => '2026-07-20T14:00:00Z';

function freshDb() {
  const db = openTestDatabase();
  migrateToLatest(db, NOW);
  return db;
}

function makePoint(i: number): TrackPointV1 {
  return {
    latitude: 52.5 + i * 0.00001,
    longitude: 13.4 + i * 0.00001,
    timestampMs: 1729000000000 + i * 1000,
    accuracyMeters: 4.2,
    altitudeMeters: null,
    speedMps: 3.1,
    headingDegrees: 90,
    source: 'foreground',
    isMocked: false,
    quality: 'accepted',
  };
}

function makeChunk(activityId: number, chunkId: number, count = 10): Chunk {
  const points = Array.from({ length: count }, (_, i) => makePoint(i));
  return buildChunk(activityId, chunkId, points);
}

describe('writeChunk / readChunks', () => {
  test('schreibt einen Chunk und liest ihn zurueck', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    const chunk = makeChunk(act.id, 0, 5);
    const res = writeChunk(db, chunk, NOW());
    expect(res.inserted).toBe(true);

    const back = readChunks(db, act.id);
    expect(back).toHaveLength(1);
    expect(back[0].chunkId).toBe(0);
    expect(back[0].pointsCount).toBe(5);
    // JSONL: eine Zeile pro Punkt
    expect(back[0].pointsJson.split('\n')).toHaveLength(5);
    db.closeSync();
  });

  test('doppelter Write desselben (activityId, chunkId) ist idempotent (G2)', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    const chunk = makeChunk(act.id, 0);
    const r1 = writeChunk(db, chunk, NOW());
    const r2 = writeChunk(db, chunk, NOW());
    expect(r1.inserted).toBe(true);
    expect(r2.inserted).toBe(false);
    expect(readChunks(db, act.id)).toHaveLength(1);
    db.closeSync();
  });

  test('readChunks liefert Chunks in chunkId-Reihenfolge', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    // Absichtlich verkehrt schreiben
    writeChunk(db, makeChunk(act.id, 2), NOW());
    writeChunk(db, makeChunk(act.id, 0), NOW());
    writeChunk(db, makeChunk(act.id, 1), NOW());
    const back = readChunks(db, act.id).map((c) => c.chunkId);
    expect(back).toEqual([0, 1, 2]);
    db.closeSync();
  });
});

describe('writeChunkBatch (transaktional, G1)', () => {
  test('schreibt alle Chunks bei erfolgreicher Batch', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    const chunks = [0, 1, 2].map((i) => makeChunk(act.id, i));
    const results = writeChunkBatch(db, chunks, NOW());
    expect(results.every((r) => r.inserted)).toBe(true);
    expect(readChunks(db, act.id)).toHaveLength(3);
    db.closeSync();
  });

  test('Batch ist idempotent auf existierenden Chunk-IDs', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    writeChunk(db, makeChunk(act.id, 0), NOW());
    // Batch schreibt Chunk 0 (dupliziert) + Chunk 1 (neu)
    const results = writeChunkBatch(
      db,
      [makeChunk(act.id, 0), makeChunk(act.id, 1)],
      NOW(),
    );
    expect(results[0].inserted).toBe(false);
    expect(results[1].inserted).toBe(true);
    expect(readChunks(db, act.id)).toHaveLength(2);
    db.closeSync();
  });
});

describe('findGaps und highestChunkId (Recovery-Hilfen)', () => {
  test('findGaps meldet leere Liste, wenn keine Luecken', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    writeChunkBatch(db, [0, 1, 2, 3].map((i) => makeChunk(act.id, i)), NOW());
    expect(findGaps(db, act.id)).toEqual([]);
    db.closeSync();
  });

  test('findGaps meldet fehlende Chunk-IDs im monotonen Verlauf', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    writeChunk(db, makeChunk(act.id, 0), NOW());
    writeChunk(db, makeChunk(act.id, 1), NOW());
    writeChunk(db, makeChunk(act.id, 4), NOW()); // 2, 3 fehlen
    writeChunk(db, makeChunk(act.id, 6), NOW()); // 5 fehlt
    expect(findGaps(db, act.id)).toEqual([2, 3, 5]);
    db.closeSync();
  });

  test('highestChunkId liefert null, wenn keine Chunks', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    expect(highestChunkId(db, act.id)).toBeNull();
    db.closeSync();
  });

  test('highestChunkId liefert die groesste Chunk-ID', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    writeChunkBatch(db, [0, 1, 5].map((i) => makeChunk(act.id, i)), NOW());
    expect(highestChunkId(db, act.id)).toBe(5);
    db.closeSync();
  });
});

describe('SP-05-Aequivalent: langer Track', () => {
  test('100 Chunks × 100 Punkte werden vollstaendig persistiert', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    const CHUNK_COUNT = 100;
    const POINTS_PER_CHUNK = 100;
    for (let i = 0; i < CHUNK_COUNT; i++) {
      writeChunk(db, makeChunk(act.id, i, POINTS_PER_CHUNK), NOW());
    }
    const back = readChunks(db, act.id);
    expect(back).toHaveLength(CHUNK_COUNT);
    const totalPoints = back.reduce((s, c) => s + c.pointsCount, 0);
    expect(totalPoints).toBe(CHUNK_COUNT * POINTS_PER_CHUNK);
    expect(findGaps(db, act.id)).toEqual([]);
    db.closeSync();
  });
});
