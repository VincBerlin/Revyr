// spikes/p0-03/naive-kill-demo.ts
//
// Direkter Nachweis, dass SP-02 einen realen Defekt faengt.
// NICHT Teil der Testkette. Nur fuer den One-off-Beweis.
//
// Aufruf: bun run spikes/p0-03/naive-kill-demo.ts

import { Database } from 'bun:sqlite';
import { unlinkSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { migrateToV1, startActivity, writeChunk, readChunks, type Chunk } from './persistence.ts';

const NOW = () => '2026-07-20T14:00:00Z';

function makeChunk(activityId: number, chunkId: number, count: number): Chunk {
  return {
    activity_id: activityId, chunk_id: chunkId,
    points_json: JSON.stringify(Array.from({ length: count }, () => ({}))),
    points_count: count,
  };
}

// NAIVE Kill-Batch: KEIN Wrapper-Transaction, jeder INSERT autocommit.
function writeChunkBatchKillNaive(
  db: Database, chunks: Chunk[], writtenAt: string, killBeforeIndex: number
): void {
  for (let i = 0; i < chunks.length; i++) {
    if (i === killBeforeIndex) throw new Error(`SIMULATED_KILL vor Index ${i}`);
    const c = chunks[i];
    db.prepare(
      `INSERT OR IGNORE INTO track_point_chunks
         (activity_id, chunk_id, points_json, points_count, written_at)
       VALUES (?, ?, ?, ?, ?)`
    ).run(c.activity_id, c.chunk_id, c.points_json, c.points_count, writtenAt);
  }
}

const dir = mkdtempSync(join(tmpdir(), 'p0-03-naive-'));
const path = join(dir, 'spike.sqlite');

let db = new Database(path);
migrateToV1(db, NOW);
const aid = startActivity(db, 'run', NOW());
writeChunk(db, makeChunk(aid, 0, 10), NOW());
writeChunk(db, makeChunk(aid, 1, 10), NOW());

// Batch aus 3 Chunks (2, 3, 4), Kill VOR Chunk-Index 1 (also Chunk-ID 3).
// Chunk-ID 2 wird durch autocommit persistiert, bevor der Throw kommt.
try {
  writeChunkBatchKillNaive(db,
    [makeChunk(aid, 2, 10), makeChunk(aid, 3, 10), makeChunk(aid, 4, 10)],
    NOW(), /*killBeforeIndex=*/1);
} catch (e) {
  console.log(`Simulierter Kill: ${(e as Error).message}`);
}
db.close();

// Reopen: was ueberlebt?
const reopened = new Database(path);
const chunks = readChunks(reopened, aid);
reopened.close();
unlinkSync(path);

console.log(`Nach Reopen (NAIVE): ${chunks.length} Chunks persistiert:`,
            chunks.map(c => c.chunk_id));
console.log(`Erwartung TRANSACTIONAL (aktuelle Umsetzung): [0, 1]`);
console.log(`Ergebnis NAIVE (autocommit): [0, 1, 2] — Chunk 2 hat den Kill ueberlebt.`);

if (chunks.map(c => c.chunk_id).includes(2)) {
  console.log(`\nNACHGEWIESEN: die naive Fassung hinterlaesst Chunk 2 halb-persistiert.`);
  console.log(`SP-02 wuerde damit fehlschlagen (erwartet: nur 2 Chunks).`);
} else {
  console.log(`\nNICHT nachgewiesen: unerwartetes Ergebnis.`);
  process.exit(1);
}
