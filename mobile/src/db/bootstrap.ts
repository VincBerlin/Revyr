// mobile/src/db/bootstrap.ts
//
// DB-Bootstrap fuer den App-Start.
//  1. Oeffnet die Datenbank ueber eine injizierte Fabrik (expo-adapter in Produktion,
//     test-adapter in Jest).
//  2. Fuehrt die aktuelle Migration aus (idempotent).
//  3. Erhebt einen Recovery-Bericht: welche Aktivitaeten sind nicht finalisiert,
//     wieviele Chunks sind je Aktivitaet persistiert, welche Chunk-IDs fehlen.
//
// KEINE Auto-Reparatur, keine Auto-Finalisierung — dieser Modul BERICHTET,
// der ActivitySessionService (oder ein spaeterer Recovery-Fluss) entscheidet.

import { migrateToLatest } from './migrations';
import { findUnfinalized, type Activity } from './activity-repo';
import { findGaps, highestChunkId } from './chunk-repo';
import { closedActiveMs } from './segment-repo';
import type { SQLiteBinding } from './ports';

export interface BootstrapOptions {
  openDatabase: () => SQLiteBinding;
  now?: () => string;
}

export interface RecoveryReport {
  activity: Activity;
  chunkCount: number;
  highestChunkId: number | null;
  gaps: readonly number[];
  /** Bereits akkumulierte Aktivzeit aus geschlossenen Segmenten. */
  activeMs: number;
}

export interface BootstrapReport {
  db: SQLiteBinding;
  freshlyMigrated: boolean;
  /** Anzahl verwaister Segmente, die der Bootstrap geschlossen hat. */
  orphansClosed: number;
  recovery: readonly RecoveryReport[];
}

export function initializeDatabase(opts: BootstrapOptions): BootstrapReport {
  const now = opts.now ?? ((): string => new Date().toISOString());
  const db = opts.openDatabase();
  const freshlyMigrated = migrateToLatest(db, now);
  const orphansClosed = closeOrphanedSegments(db);
  const recovery = collectRecovery(db);
  return { db, freshlyMigrated, orphansClosed, recovery };
}

// Nach einem App-Crash koennen offene Segmente zurueckbleiben. Wir schliessen
// sie deterministisch auf den letzten bekannten Zeitpunkt der Aktivitaet:
//   - letzter written_at des juengsten Chunks, falls > segment.started_at
//   - sonst segment.started_at selbst (0 aktive Zeit — konservativ)
//
// Damit sind KEINE offenen Segmente aus Vorlaeufen mehr im DB-State — jede
// neue resume-Session oeffnet ein FRISCHES Segment.
export function closeOrphanedSegments(db: SQLiteBinding): number {
  const rows = db.getAllSync<{
    activity_id: number;
    segment_index: number;
    started_at: string;
    last_chunk_written_at: string | null;
  }>(
    `SELECT s.activity_id,
            s.segment_index,
            s.started_at,
            (SELECT tc.written_at
               FROM track_point_chunks tc
              WHERE tc.activity_id = s.activity_id
              ORDER BY tc.chunk_id DESC
              LIMIT 1) AS last_chunk_written_at
       FROM activity_segments s
       JOIN activities a ON a.id = s.activity_id
      WHERE s.ended_at IS NULL`,
  );
  let closed = 0;
  for (const r of rows) {
    const candidate = r.last_chunk_written_at;
    const endedAt =
      candidate !== null && candidate > r.started_at
        ? candidate
        : r.started_at;
    db.runSync(
      `UPDATE activity_segments
          SET ended_at = ?
        WHERE activity_id = ? AND segment_index = ?`,
      [endedAt, r.activity_id, r.segment_index],
    );
    closed += 1;
  }
  return closed;
}

// Eigenstaendig aufrufbar — etwa fuer einen expliziten "Recovery-Refresh"-Knopf
// in der Dev-Oberflaeche oder fuer einen spaeteren Retry.
export function collectRecovery(db: SQLiteBinding): readonly RecoveryReport[] {
  const unfinalized = findUnfinalized(db);
  return unfinalized.map((activity) => {
    const chunks = db.getAllSync<{ n: number }>(
      `SELECT COUNT(*) AS n FROM track_point_chunks WHERE activity_id = ?`,
      [activity.id],
    );
    return {
      activity,
      chunkCount: chunks[0]?.n ?? 0,
      highestChunkId: highestChunkId(db, activity.id),
      gaps: findGaps(db, activity.id),
      activeMs: closedActiveMs(db, activity.id),
    };
  });
}
