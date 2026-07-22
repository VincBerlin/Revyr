// mobile/src/db/activity-repo.ts
//
// Repository-Pattern fuer activities. Duenne SQL-Wrapper; keine Domain-Logik.

import type { SQLiteBinding } from './ports';

export type Sport = 'run' | 'ride';

export interface Activity {
  id: number;
  sport: Sport;
  startedAt: string;      // ISO-8601
  finalizedAt: string | null;
}

interface ActivityRow {
  id: number;
  sport: Sport;
  started_at: string;
  finalized_at: string | null;
}

function toActivity(row: ActivityRow): Activity {
  return {
    id: row.id,
    sport: row.sport,
    startedAt: row.started_at,
    finalizedAt: row.finalized_at,
  };
}

export function startActivity(
  db: SQLiteBinding,
  sport: Sport,
  startedAt: string,
): Activity {
  db.runSync(
    `INSERT INTO activities (sport, started_at) VALUES (?, ?)`,
    [sport, startedAt],
  );
  const row = db.getFirstSync<ActivityRow>(
    `SELECT id, sport, started_at, finalized_at
       FROM activities
       ORDER BY id DESC LIMIT 1`,
  );
  if (row === null) {
    throw new Error('startActivity: INSERT succeeded but SELECT returned nothing');
  }
  return toActivity(row);
}

export function finalizeActivity(
  db: SQLiteBinding,
  id: number,
  finalizedAt: string,
): void {
  const result = db.runSync(
    `UPDATE activities SET finalized_at = ? WHERE id = ? AND finalized_at IS NULL`,
    [finalizedAt, id],
  );
  if (result.changes === 0) {
    throw new Error(
      `finalizeActivity: aktivitaet ${id} existiert nicht oder ist bereits finalisiert`,
    );
  }
}

export function getActivity(db: SQLiteBinding, id: number): Activity | null {
  const row = db.getFirstSync<ActivityRow>(
    `SELECT id, sport, started_at, finalized_at FROM activities WHERE id = ?`,
    [id],
  );
  return row === null ? null : toActivity(row);
}

// Recovery: welche Aktivitaeten sind nicht finalisiert (App-Kill wahrscheinlich)?
export function findUnfinalized(db: SQLiteBinding): Activity[] {
  return db.getAllSync<ActivityRow>(
    `SELECT id, sport, started_at, finalized_at
       FROM activities
       WHERE finalized_at IS NULL
       ORDER BY id ASC`,
  ).map(toActivity);
}

// Verlaufsliste: finalisierte Aktivitaeten, neueste zuerst.
// limit deckt die Dev-UI ab — noch keine Paginierung; braucht Produktentscheidung.
export function listFinalizedActivities(
  db: SQLiteBinding,
  limit: number = 50,
): Activity[] {
  if (limit <= 0) return [];
  return db.getAllSync<ActivityRow>(
    `SELECT id, sport, started_at, finalized_at
       FROM activities
       WHERE finalized_at IS NOT NULL
       ORDER BY finalized_at DESC
       LIMIT ?`,
    [limit],
  ).map(toActivity);
}
