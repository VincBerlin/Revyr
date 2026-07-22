// mobile/src/db/chunk-repo.ts
//
// Chunk-Persistenz. Lehren aus dem P0-03-Spike:
//  G1: SQLite-Rollback traegt Kill-Sicherheit NUR bei expliziter Transaktion.
//      writeChunkBatch nutzt daher withTransactionSync.
//  G2: Idempotenz per PRIMARY KEY + INSERT OR IGNORE. Rueckgabe informiert
//      Aufrufer, ob tatsaechlich eingefuegt wurde.
//  G5: Chunk-Groesse ist eine Batterie/Recovery-Trade-off-Frage — hier NICHT entschieden.
//      Der Aufrufer bestimmt die Chunk-Groesse.

import type { SQLiteBinding } from './ports';
import { serializePoints, type TrackPointV1 } from '../domain/track-point';

export interface Chunk {
  activityId: number;
  chunkId: number;
  pointsJson: string;
  pointsCount: number;
}

export interface WriteChunkResult {
  inserted: boolean;
  activityId: number;
  chunkId: number;
}

interface ChunkRow {
  activity_id: number;
  chunk_id: number;
  points_json: string;
  points_count: number;
}

function toChunk(row: ChunkRow): Chunk {
  return {
    activityId: row.activity_id,
    chunkId: row.chunk_id,
    pointsJson: row.points_json,
    pointsCount: row.points_count,
  };
}

// Hilfsfunktion: baut aus einer TrackPointV1-Liste einen Chunk (JSONL-Body).
// Bewusst KEIN JSON-Array — JSONL erlaubt streamendes Anhaengen ohne
// Neuparse des ganzen Payloads (fuer spaeteres Sync).
export function buildChunk(
  activityId: number,
  chunkId: number,
  points: readonly TrackPointV1[],
): Chunk {
  return {
    activityId,
    chunkId,
    pointsJson: serializePoints(points),
    pointsCount: points.length,
  };
}

// Einzel-Schreiben: eigene Transaktion. Idempotent auf (activityId, chunkId).
export function writeChunk(
  db: SQLiteBinding,
  chunk: Chunk,
  writtenAt: string,
): WriteChunkResult {
  let inserted = false;
  db.withTransactionSync(() => {
    const result = db.runSync(
      `INSERT OR IGNORE INTO track_point_chunks
         (activity_id, chunk_id, points_json, points_count, written_at)
       VALUES (?, ?, ?, ?, ?)`,
      [chunk.activityId, chunk.chunkId, chunk.pointsJson,
       chunk.pointsCount, writtenAt],
    );
    inserted = result.changes > 0;
  });
  return { inserted, activityId: chunk.activityId, chunkId: chunk.chunkId };
}

// Batch: EINE Transaktion fuer alle Chunks. Ein Throw mitten drin rollt die
// gesamte Batch zurueck (G1). Die Wahl ist konservativ — wer eine feinere
// Persistenzgarantie will, ruft writeChunk N-mal einzeln auf.
export function writeChunkBatch(
  db: SQLiteBinding,
  chunks: readonly Chunk[],
  writtenAt: string,
): WriteChunkResult[] {
  const results: WriteChunkResult[] = [];
  db.withTransactionSync(() => {
    for (const chunk of chunks) {
      const result = db.runSync(
        `INSERT OR IGNORE INTO track_point_chunks
           (activity_id, chunk_id, points_json, points_count, written_at)
         VALUES (?, ?, ?, ?, ?)`,
        [chunk.activityId, chunk.chunkId, chunk.pointsJson,
         chunk.pointsCount, writtenAt],
      );
      results.push({
        inserted: result.changes > 0,
        activityId: chunk.activityId,
        chunkId: chunk.chunkId,
      });
    }
  });
  return results;
}

export function readChunks(db: SQLiteBinding, activityId: number): Chunk[] {
  return db.getAllSync<ChunkRow>(
    `SELECT activity_id, chunk_id, points_json, points_count
       FROM track_point_chunks
       WHERE activity_id = ?
       ORDER BY chunk_id ASC`,
    [activityId],
  ).map(toChunk);
}

// Recovery-Hilfe: welche Chunk-IDs fehlen im monotonen Verlauf?
// Nuetzlich beim Wiederanlauf nach Kill, um zu erkennen, welche Chunks nachgereicht
// werden muessen (falls die App eine In-Memory-Puffer-Strategie faehrt).
export function findGaps(db: SQLiteBinding, activityId: number): number[] {
  const rows = db.getAllSync<{ chunk_id: number }>(
    `SELECT chunk_id FROM track_point_chunks
       WHERE activity_id = ? ORDER BY chunk_id ASC`,
    [activityId],
  );
  const gaps: number[] = [];
  let expected = 0;
  for (const r of rows) {
    while (expected < r.chunk_id) {
      gaps.push(expected);
      expected++;
    }
    expected = r.chunk_id + 1;
  }
  return gaps;
}

// Recovery-Hilfe: hoechste geschriebene chunk_id pro Aktivitaet, oder null wenn keine.
export function highestChunkId(db: SQLiteBinding, activityId: number): number | null {
  const row = db.getFirstSync<{ max_id: number | null }>(
    `SELECT MAX(chunk_id) AS max_id FROM track_point_chunks WHERE activity_id = ?`,
    [activityId],
  );
  return row?.max_id ?? null;
}
