// mobile/src/db/segment-repo.ts
//
// Aktivzeit-Segmente einer Aktivitaet. Jedes recording/paused-Segment ist eine
// Zeile in activity_segments. Ein offenes Segment (ended_at IS NULL) existiert
// nur, waehrend der Coordinator im Zustand 'recording' ist. Pause/Finalize
// schliesst es; Resume oeffnet ein neues.
//
// Bootstrap-Grenze: verwaiste offene Segmente (aus einem App-Crash) werden vom
// Bootstrap geschlossen — siehe closeOrphanedSegments in bootstrap.ts.

import type { SQLiteBinding } from './ports';

export interface Segment {
  readonly activityId: number;
  readonly segmentIndex: number;
  readonly startedAt: string;   // ISO
  readonly endedAt: string | null;
}

interface SegmentRow {
  activity_id: number;
  segment_index: number;
  started_at: string;
  ended_at: string | null;
}

function toSegment(row: SegmentRow): Segment {
  return {
    activityId: row.activity_id,
    segmentIndex: row.segment_index,
    startedAt: row.started_at,
    endedAt: row.ended_at,
  };
}

export function startSegment(
  db: SQLiteBinding,
  activityId: number,
  startedAt: string,
): Segment {
  const row = db.getFirstSync<{ max_idx: number | null }>(
    `SELECT MAX(segment_index) AS max_idx FROM activity_segments WHERE activity_id = ?`,
    [activityId],
  );
  const nextIdx = (row?.max_idx ?? -1) + 1;
  db.runSync(
    `INSERT INTO activity_segments (activity_id, segment_index, started_at, ended_at)
     VALUES (?, ?, ?, NULL)`,
    [activityId, nextIdx, startedAt],
  );
  return { activityId, segmentIndex: nextIdx, startedAt, endedAt: null };
}

// Schliesst das offene Segment (falls eines existiert). Idempotent auf 'keins offen'.
// Rueckgabe: true, wenn tatsaechlich ein Segment geschlossen wurde.
export function closeOpenSegment(
  db: SQLiteBinding,
  activityId: number,
  endedAt: string,
): boolean {
  const result = db.runSync(
    `UPDATE activity_segments
        SET ended_at = ?
      WHERE activity_id = ? AND ended_at IS NULL`,
    [endedAt, activityId],
  );
  return result.changes > 0;
}

export function listSegments(db: SQLiteBinding, activityId: number): Segment[] {
  return db.getAllSync<SegmentRow>(
    `SELECT activity_id, segment_index, started_at, ended_at
       FROM activity_segments
      WHERE activity_id = ?
      ORDER BY segment_index ASC`,
    [activityId],
  ).map(toSegment);
}

export function findOpenSegment(
  db: SQLiteBinding,
  activityId: number,
): Segment | null {
  const row = db.getFirstSync<SegmentRow>(
    `SELECT activity_id, segment_index, started_at, ended_at
       FROM activity_segments
      WHERE activity_id = ? AND ended_at IS NULL
      ORDER BY segment_index DESC
      LIMIT 1`,
    [activityId],
  );
  return row === null ? null : toSegment(row);
}

// Summe der Dauern aller GESCHLOSSENEN Segmente in ms. Offene werden ignoriert;
// wer die Live-Dauer will, addiert (now - openSegment.started_at) selbst.
export function closedActiveMs(db: SQLiteBinding, activityId: number): number {
  const segs = listSegments(db, activityId);
  let sum = 0;
  for (const s of segs) {
    if (s.endedAt === null) continue;
    const startMs = Date.parse(s.startedAt);
    const endMs = Date.parse(s.endedAt);
    if (!Number.isFinite(startMs) || !Number.isFinite(endMs)) continue;
    const delta = endMs - startMs;
    if (delta > 0) sum += delta;
  }
  return sum;
}
