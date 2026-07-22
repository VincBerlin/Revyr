// mobile/src/db/migrations.ts
//
// Idempotente Migrationen. Lehre aus dem P0-03-Spike (G3):
// BEIDE Schichten braucht die Idempotenz — CREATE TABLE IF NOT EXISTS gegen
// Crash-mid-Migration-Zwischenzustaende, plus eine Version-Guard gegen
// Semantikwechsel bei einer spaeteren V1'-Neudefinition.

import type { SQLiteBinding } from './ports';

export const CURRENT_SCHEMA_VERSION = 2;

interface SchemaVersionRow {
  version: number;
}

export function currentSchemaVersion(db: SQLiteBinding): number {
  db.execSync(`CREATE TABLE IF NOT EXISTS schema_versions (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL
  )`);
  const row = db.getFirstSync<{ v: number | null }>(
    `SELECT MAX(version) AS v FROM schema_versions`,
  );
  return row?.v ?? 0;
}

// Wendet die Migration V0->V1 an. Wiederholte Aufrufe sind No-Op (return false).
// Nutzt ISO-8601-String fuer applied_at; die Zeitquelle ist injizierbar, damit
// Tests deterministisch sind.
export function migrateToV1(
  db: SQLiteBinding,
  now: () => string = () => new Date().toISOString(),
): boolean {
  const v = currentSchemaVersion(db);
  if (v >= 1) return false;

  db.withTransactionSync(() => {
    db.execSync(`CREATE TABLE IF NOT EXISTS activities (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      sport TEXT NOT NULL CHECK (sport IN ('run','ride')),
      started_at TEXT NOT NULL,
      finalized_at TEXT
    )`);
    db.execSync(`CREATE INDEX IF NOT EXISTS idx_activities_started_at
                 ON activities (started_at DESC)`);
    db.execSync(`CREATE TABLE IF NOT EXISTS track_point_chunks (
      activity_id INTEGER NOT NULL REFERENCES activities(id),
      chunk_id INTEGER NOT NULL,
      points_json TEXT NOT NULL,
      points_count INTEGER NOT NULL CHECK (points_count >= 0),
      written_at TEXT NOT NULL,
      PRIMARY KEY (activity_id, chunk_id)
    )`);
    db.execSync(`CREATE INDEX IF NOT EXISTS idx_chunks_by_activity
                 ON track_point_chunks (activity_id, chunk_id)`);
    db.runSync(
      `INSERT INTO schema_versions (version, applied_at) VALUES (?, ?)`,
      [1, now()],
    );
  });
  return true;
}

// Liest alle applied Versionen — nuetzlich fuer Tests und Recovery-Diagnose.
export function appliedVersions(db: SQLiteBinding): number[] {
  currentSchemaVersion(db); // stellt sicher, dass schema_versions existiert
  return db.getAllSync<SchemaVersionRow>(
    `SELECT version FROM schema_versions ORDER BY version ASC`,
  ).map((r) => r.version);
}

// V1 -> V2: Aktivzeit-Segmente einfuehren.
// Backfill: fuer jede existierende Aktivitaet wird EIN Segment angelegt
// (started_at aus activities.started_at, ended_at aus activities.finalized_at).
// Unfinalisierte Aktivitaeten bekommen ein OFFENES Segment; der Bootstrap
// schliesst es beim naechsten Start (closeOrphanedSegments).
export function migrateToV2(
  db: SQLiteBinding,
  now: () => string = () => new Date().toISOString(),
): boolean {
  const v = currentSchemaVersion(db);
  if (v >= 2) return false;
  if (v < 1) migrateToV1(db, now);

  db.withTransactionSync(() => {
    db.execSync(`CREATE TABLE IF NOT EXISTS activity_segments (
      activity_id INTEGER NOT NULL REFERENCES activities(id),
      segment_index INTEGER NOT NULL,
      started_at TEXT NOT NULL,
      ended_at TEXT,
      PRIMARY KEY (activity_id, segment_index)
    )`);
    db.execSync(`CREATE INDEX IF NOT EXISTS idx_segments_open
                 ON activity_segments (activity_id) WHERE ended_at IS NULL`);
    // Backfill je Aktivitaet (falls schon welche existieren)
    const rows = db.getAllSync<{ id: number; started_at: string; finalized_at: string | null }>(
      `SELECT id, started_at, finalized_at FROM activities`,
    );
    for (const a of rows) {
      db.runSync(
        `INSERT INTO activity_segments (activity_id, segment_index, started_at, ended_at)
         VALUES (?, 0, ?, ?)`,
        [a.id, a.started_at, a.finalized_at],
      );
    }
    db.runSync(
      `INSERT INTO schema_versions (version, applied_at) VALUES (2, ?)`,
      [now()],
    );
  });
  return true;
}

// Bequeme Ein-Aufruf-Migration fuer den Bootstrap. Rueckgabe true = mindestens
// eine Migration lief in diesem Aufruf.
export function migrateToLatest(
  db: SQLiteBinding,
  now: () => string = () => new Date().toISOString(),
): boolean {
  let anyRan = false;
  if (migrateToV1(db, now)) anyRan = true;
  if (migrateToV2(db, now)) anyRan = true;
  return anyRan;
}
