// spikes/p0-03/persistence.ts
//
// Wegwerf-Umsetzung fuer den Spike P0-03. TypeScript + bun:sqlite.
// Kein Produktionscode. Kleinstmoegliche Struktur, um die Tests SP-01..SP-05 zu tragen.
//
// Wahl bun:sqlite statt expo-sqlite: expo-sqlite verlangt eine React-Native-Laufzeit;
// bun:sqlite bietet dieselbe SQLite-Semantik (ACID, WAL, synchronous-Level) isoliert.
// Ein in Produktion in expo-sqlite umzustellendes Modul haette dieselben Semantikbeuge —
// die verhaltensrelevanten Aussagen dieses Spikes uebertragen sich.

import { Database } from 'bun:sqlite';

export type Sport = 'run' | 'ride';

export interface Chunk {
  activity_id: number;
  chunk_id: number;        // monoton pro activity, startet bei 0
  points_json: string;     // JSON-Array von TrackPointV1
  points_count: number;
}

export interface WriteResult {
  inserted: boolean;       // true = neuer Datensatz, false = Duplikat unterdrueckt
  activity_id: number;
  chunk_id: number;
}

// -------- Migration ---------------------------------------------------------
export function currentVersion(db: Database): number {
  db.exec(`CREATE TABLE IF NOT EXISTS schema_versions (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL
  )`);
  const row = db.prepare(`SELECT MAX(version) as v FROM schema_versions`).get() as { v: number | null };
  return row.v ?? 0;
}

// Idempotente Migration V0->V1. Wiederholte Anwendung ist ein No-Op.
// Wir verwenden CREATE TABLE IF NOT EXISTS UND die Version-Guard. Beides ist Absicht:
// die Version-Guard schuetzt vor Semantikwechseln, das IF NOT EXISTS schuetzt vor
// crash-mid-migration-Zwischenzustaenden.
export function migrateToV1(db: Database, now: () => string = () => new Date().toISOString()): boolean {
  const v = currentVersion(db);
  if (v >= 1) return false;    // No-Op
  db.transaction(() => {
    db.exec(`CREATE TABLE IF NOT EXISTS activities (
      id INTEGER PRIMARY KEY,
      sport TEXT NOT NULL CHECK (sport IN ('run','ride')),
      started_at TEXT NOT NULL,
      finalized_at TEXT
    )`);
    db.exec(`CREATE TABLE IF NOT EXISTS track_point_chunks (
      activity_id INTEGER NOT NULL REFERENCES activities(id),
      chunk_id INTEGER NOT NULL,
      points_json TEXT NOT NULL,
      points_count INTEGER NOT NULL,
      written_at TEXT NOT NULL,
      PRIMARY KEY (activity_id, chunk_id)
    )`);
    db.exec(`CREATE INDEX IF NOT EXISTS idx_chunks_by_activity
             ON track_point_chunks (activity_id, chunk_id)`);
    db.prepare(`INSERT INTO schema_versions (version, applied_at) VALUES (1, ?)`).run(now());
  })();
  return true;
}

// -------- Aktivitaeten ------------------------------------------------------
export function startActivity(db: Database, sport: Sport, startedAt: string): number {
  const info = db.prepare(
    `INSERT INTO activities (sport, started_at) VALUES (?, ?)`
  ).run(sport, startedAt);
  return Number(info.lastInsertRowid);
}

// -------- Chunks: Schreiben mit expliziter Transaktion ---------------------
// writeChunk laeuft in einer eigenen Transaktion. Bei einem Throw MITTEN drin
// rollt SQLite auf den letzten COMMIT zurueck — der halb geschriebene Chunk ist weg.
// Wichtig: writeChunk ist idempotent auf (activity_id, chunk_id). Zweitschreiben
// desselben chunk_id liefert inserted=false ohne Fehler.
export function writeChunk(db: Database, chunk: Chunk, writtenAt: string): WriteResult {
  const tx = db.transaction(() => {
    const info = db.prepare(
      `INSERT OR IGNORE INTO track_point_chunks
         (activity_id, chunk_id, points_json, points_count, written_at)
       VALUES (?, ?, ?, ?, ?)`
    ).run(chunk.activity_id, chunk.chunk_id, chunk.points_json,
          chunk.points_count, writtenAt);
    return info.changes > 0;
  });
  const inserted = tx();
  return { inserted, activity_id: chunk.activity_id, chunk_id: chunk.chunk_id };
}

// Bewusst NAIVE Variante fuer den Kill-Nachweis. Nutzt keine explizite Transaktion,
// wirft aber MITTEN im Schreibvorgang. Beim ersten Statement zeigt sich SQLite-ACID
// bereits: das eine INSERT-Statement ist atomar. Der eigentliche Kill-Fall betrifft
// eine LOGISCHE Batch aus mehreren Chunks — dafuer nutzen wir writeChunkBatchKill.
export function writeChunkBatchKill(
  db: Database, chunks: Chunk[], writtenAt: string, killBeforeChunkIndex: number
): void {
  const tx = db.transaction(() => {
    for (let i = 0; i < chunks.length; i++) {
      if (i === killBeforeChunkIndex) {
        throw new Error(`SIMULATED_KILL vor Chunk-Index ${i}`);
      }
      const c = chunks[i];
      db.prepare(
        `INSERT OR IGNORE INTO track_point_chunks
           (activity_id, chunk_id, points_json, points_count, written_at)
         VALUES (?, ?, ?, ?, ?)`
      ).run(c.activity_id, c.chunk_id, c.points_json, c.points_count, writtenAt);
    }
  });
  tx();
}

// Lesen: reine Read-Only-Operation, keine Transaktion noetig.
export function readChunks(db: Database, activityId: number): Chunk[] {
  return db.prepare(
    `SELECT activity_id, chunk_id, points_json, points_count
       FROM track_point_chunks
       WHERE activity_id = ?
       ORDER BY chunk_id ASC`
  ).all(activityId) as Chunk[];
}

// Recovery-Hilfe: welche Chunks fehlen im monotonen Verlauf?
// (In der Zielarchitektur waere das ein „gap detection" beim Recovery.)
export function findGaps(db: Database, activityId: number): number[] {
  const rows = db.prepare(
    `SELECT chunk_id FROM track_point_chunks WHERE activity_id = ? ORDER BY chunk_id`
  ).all(activityId) as { chunk_id: number }[];
  const gaps: number[] = [];
  let expected = 0;
  for (const r of rows) {
    while (expected < r.chunk_id) { gaps.push(expected); expected++; }
    expected = r.chunk_id + 1;
  }
  return gaps;
}
