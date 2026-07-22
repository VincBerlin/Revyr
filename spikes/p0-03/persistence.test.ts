// spikes/p0-03/persistence.test.ts
//
// SP-01..SP-05 nach Nutzerauftrag Runde 6 Punkt 3:
//   Chunk-Schreiben, Prozessabbruch, Recovery, doppelte Writes, idempotente Migration.
//
// Aufruf: bun run spikes/p0-03/persistence.test.ts
// Der Test nutzt eine In-Memory-DB pro Fall (:memory:) und, wo Persistenz noetig ist,
// eine File-DB im os.tmpdir() — beides SYNTHETISCH und laut Nutzerauftrag Runde 6
// Punkt 4 KEIN real-boundary Nachweis. Evidence bleibt pending.

import { Database } from 'bun:sqlite';
import { unlinkSync, existsSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import {
  migrateToV1, currentVersion, startActivity, writeChunk,
  writeChunkBatchKill, readChunks, findGaps,
  type Chunk,
} from './persistence.ts';

const NOW = () => '2026-07-20T14:00:00Z';

// -------- Test-Runner ------------------------------------------------------
type Case = { name: string; fn: () => void };
const CASES: Case[] = [];
function tc(name: string, fn: () => void) { CASES.push({ name, fn }); }
function assertEq<T>(a: T, b: T, msg: string) {
  const A = JSON.stringify(a), B = JSON.stringify(b);
  if (A !== B) throw new Error(`${msg}: got ${A} expected ${B}`);
}
function assertTrue(cond: unknown, msg: string) {
  if (!cond) throw new Error(msg);
}
function assertThrows(fn: () => unknown, msg: string) {
  try { fn(); } catch { return; }
  throw new Error(`${msg}: kein Fehler geworfen`);
}

// -------- Hilfen -----------------------------------------------------------
function makeChunk(activityId: number, chunkId: number, count = 100): Chunk {
  const points = Array.from({ length: count }, (_, i) => ({
    latitude: 52.5 + i * 0.00001,
    longitude: 13.4 + i * 0.00001,
    timestampMs: 1_729_000_000_000 + i * 1000,
    accuracyMeters: 4.2,
    altitudeMeters: null,
    speedMps: 3.1,
    headingDegrees: 90,
    source: 'foreground',
    isMocked: false,
    quality: 'accepted',
  }));
  return {
    activity_id: activityId,
    chunk_id: chunkId,
    points_json: JSON.stringify(points),
    points_count: count,
  };
}

function freshDb(): Database {
  const db = new Database(':memory:');
  migrateToV1(db, NOW);
  return db;
}

function freshFileDb(): { db: Database; path: string; cleanup: () => void } {
  const dir = mkdtempSync(join(tmpdir(), 'p0-03-'));
  const path = join(dir, 'spike.sqlite');
  let db = new Database(path);
  migrateToV1(db, NOW);
  return {
    db, path,
    cleanup: () => { db.close(); if (existsSync(path)) unlinkSync(path); },
  };
}

// ---------------------------------------------------------------------------
// SP-01: Chunk schreiben und wieder lesen — Round-Trip erhaelt Punkte
// ---------------------------------------------------------------------------
tc('SP-01 write chunk und read back — Round-Trip erhaelt Punkte', () => {
  const db = freshDb();
  const aid = startActivity(db, 'run', NOW());
  const chunk = makeChunk(aid, 0, 50);
  const res = writeChunk(db, chunk, NOW());
  assertTrue(res.inserted, 'SP-01: erster Chunk sollte inserted=true melden');

  const back = readChunks(db, aid);
  assertEq(back.length, 1, 'SP-01: erwartet ein Chunk gelesen');
  assertEq(back[0].chunk_id, 0, 'SP-01: chunk_id verloren');
  assertEq(back[0].points_count, 50, 'SP-01: points_count verloren');

  const pointsBack = JSON.parse(back[0].points_json);
  assertEq(pointsBack.length, 50, 'SP-01: points-array-Laenge verloren');
  assertEq(pointsBack[0].latitude, 52.5, 'SP-01: erster Punkt latitude verloren');
});

// ---------------------------------------------------------------------------
// SP-02: Prozessabbruch mitten in einer Chunk-Batch — Recovery zeigt NUR
// committete Chunks (SQLite-Transaktion rollt zurueck).
// ---------------------------------------------------------------------------
tc('SP-02 Prozessabbruch mitten in Batch — Recovery zeigt nur committete Chunks', () => {
  const { db, path, cleanup } = freshFileDb();
  try {
    const aid = startActivity(db, 'run', NOW());
    // Zuerst 2 Chunks in ihren EIGENEN Transaktionen (writeChunk) — die sind committet.
    writeChunk(db, makeChunk(aid, 0, 100), NOW());
    writeChunk(db, makeChunk(aid, 1, 100), NOW());
    // Dann eine BATCH aus 3 Chunks (2, 3, 4), Kill VOR Chunk 3.
    // writeChunkBatchKill wickelt die drei in EINER Transaktion; nach dem Throw
    // wird die gesamte Batch zurueckgerollt — auch Chunk 2 ist danach nicht persistiert.
    assertThrows(
      () => writeChunkBatchKill(db,
        [makeChunk(aid, 2, 100), makeChunk(aid, 3, 100), makeChunk(aid, 4, 100)],
        NOW(), /*killBeforeChunkIndex=*/1),
      'SP-02: Batch-Kill sollte werfen'
    );
    db.close();

    // Reopen simuliert Prozessabbruch: neuer DB-Handle auf dieselbe Datei.
    const reopened = new Database(path);
    const back = readChunks(reopened, aid);
    reopened.close();

    // Erwartet: nur Chunk 0 und 1 sind committet; 2, 3, 4 sind weg (Rollback).
    assertEq(back.length, 2, 'SP-02: erwartet exakt zwei committete Chunks');
    assertEq(back.map(c => c.chunk_id), [0, 1],
             'SP-02: Chunk 2 haette gerollt werden muessen, ist aber persistiert');
  } finally {
    cleanup();
  }
});

// ---------------------------------------------------------------------------
// SP-03: Doppelte Writes desselben (activity_id, chunk_id) — idempotent,
// kein Duplikat, kein Fehler.
// ---------------------------------------------------------------------------
tc('SP-03 doppelte Writes — idempotent, ohne Duplikat, ohne Fehler', () => {
  const db = freshDb();
  const aid = startActivity(db, 'run', NOW());
  const chunk = makeChunk(aid, 0, 10);
  const r1 = writeChunk(db, chunk, NOW());
  const r2 = writeChunk(db, chunk, NOW());   // exakt derselbe chunk_id
  assertTrue(r1.inserted, 'SP-03: erster Write sollte inserted=true melden');
  assertTrue(!r2.inserted, 'SP-03: zweiter Write sollte inserted=false melden (kein Duplikat)');

  const back = readChunks(db, aid);
  assertEq(back.length, 1, 'SP-03: erwartet nur eine Zeile trotz doppeltem Write');
});

// ---------------------------------------------------------------------------
// SP-04: Idempotente Migration — zweiter Aufruf ist No-Op.
// ---------------------------------------------------------------------------
tc('SP-04 Migration ist idempotent — zweiter Aufruf ist No-Op', () => {
  const db = new Database(':memory:');
  const first = migrateToV1(db, NOW);
  const second = migrateToV1(db, NOW);
  const third = migrateToV1(db, NOW);
  assertTrue(first, 'SP-04: erster Aufruf sollte migrieren (return true)');
  assertTrue(!second, 'SP-04: zweiter Aufruf sollte No-Op sein (return false)');
  assertTrue(!third, 'SP-04: dritter Aufruf sollte No-Op sein (return false)');

  // schema_versions haelt genau EINE Zeile fuer V1.
  const rows = db.prepare(`SELECT version FROM schema_versions ORDER BY version`)
                  .all() as { version: number }[];
  assertEq(rows.length, 1, 'SP-04: schema_versions haette genau einen Eintrag haben muessen');
  assertEq(rows[0].version, 1, 'SP-04: eingetragene Version ist nicht 1');

  // Grundtabellen existieren.
  const tables = db.prepare(
    `SELECT name FROM sqlite_master WHERE type='table' ORDER BY name`
  ).all() as { name: string }[];
  const names = tables.map(t => t.name);
  assertTrue(names.includes('activities'), 'SP-04: Tabelle activities fehlt');
  assertTrue(names.includes('track_point_chunks'), 'SP-04: Tabelle track_point_chunks fehlt');
});

// ---------------------------------------------------------------------------
// SP-05: Langer Track — 10.000 Punkte in 100 Chunks. Schreiblatenz protokolliert,
// nicht bewertet (Detailplan §3.1: „messen und protokollieren, nicht bewerten").
// Recovery-Nebenprobe: findGaps() findet Luecken zuverlaessig.
// ---------------------------------------------------------------------------
tc('SP-05 langer Track — 10000 Punkte in 100 Chunks, kein Datenverlust, keine Luecke', () => {
  const db = freshDb();
  const aid = startActivity(db, 'run', NOW());
  const CHUNK_COUNT = 100;
  const POINTS_PER_CHUNK = 100;
  const t0 = performance.now();
  for (let i = 0; i < CHUNK_COUNT; i++) {
    writeChunk(db, makeChunk(aid, i, POINTS_PER_CHUNK), NOW());
  }
  const elapsedMs = performance.now() - t0;

  const back = readChunks(db, aid);
  assertEq(back.length, CHUNK_COUNT, 'SP-05: nicht alle Chunks persistiert');
  const totalPoints = back.reduce((s, c) => s + c.points_count, 0);
  assertEq(totalPoints, CHUNK_COUNT * POINTS_PER_CHUNK,
           'SP-05: points_count-Summe stimmt nicht');
  assertEq(findGaps(db, aid), [], 'SP-05: unerwartete Luecken im Chunk-Verlauf');

  // Nur protokollieren — kein Zielwert (P03-relevante MISSING).
  console.log(`     [SP-05 Info] 100 Chunks × 100 Punkte = 10.000 Punkte in ${elapsedMs.toFixed(1)}ms (bun:sqlite in-memory).`);
});

// ---------------------------------------------------------------------------
// SP-06: Gap-Detection funktioniert bei Luecken
// ---------------------------------------------------------------------------
tc('SP-06 findGaps meldet Luecken korrekt', () => {
  const db = freshDb();
  const aid = startActivity(db, 'run', NOW());
  writeChunk(db, makeChunk(aid, 0, 10), NOW());
  writeChunk(db, makeChunk(aid, 1, 10), NOW());
  writeChunk(db, makeChunk(aid, 3, 10), NOW());  // Chunk 2 fehlt
  writeChunk(db, makeChunk(aid, 5, 10), NOW());  // 4 fehlt
  assertEq(findGaps(db, aid), [2, 4], 'SP-06: erwartete Luecken [2, 4] nicht gefunden');
});

// ---------------------------------------------------------------------------
// Ausfuehren
// ---------------------------------------------------------------------------
let pass = 0, fail = 0;
const failures: string[] = [];
for (const c of CASES) {
  try { c.fn(); console.log(`ok  ${c.name}`); pass++; }
  catch (e: any) { console.log(`FAIL ${c.name}\n     ${e.message}`); failures.push(c.name); fail++; }
}
console.log(`\nZusammenfassung: ${pass} pass, ${fail} fail, ${CASES.length} gesamt`);
if (fail) { console.log('Fehlgeschlagen:', failures.join(', ')); process.exit(1); }
