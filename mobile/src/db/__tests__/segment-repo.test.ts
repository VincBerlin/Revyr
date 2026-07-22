// mobile/src/db/__tests__/segment-repo.test.ts
import { openTestDatabase } from '../test-adapter';
import { migrateToLatest } from '../migrations';
import { startActivity } from '../activity-repo';
import {
  closeOpenSegment,
  closedActiveMs,
  findOpenSegment,
  listSegments,
  startSegment,
} from '../segment-repo';

const NOW = (): string => '2026-07-20T15:00:00Z';

function freshDb() {
  const db = openTestDatabase();
  migrateToLatest(db, NOW);
  return db;
}

describe('startSegment / closeOpenSegment / listSegments', () => {
  test('startSegment vergibt segment_index 0 als ersten', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', NOW());
    const s = startSegment(db, a.id, '2026-07-20T15:00:00Z');
    expect(s.segmentIndex).toBe(0);
    expect(s.startedAt).toBe('2026-07-20T15:00:00Z');
    expect(s.endedAt).toBeNull();
    db.closeSync();
  });

  test('startSegment inkrementiert segment_index', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', NOW());
    startSegment(db, a.id, '2026-07-20T15:00:00Z');
    closeOpenSegment(db, a.id, '2026-07-20T15:05:00Z');
    const s2 = startSegment(db, a.id, '2026-07-20T15:10:00Z');
    expect(s2.segmentIndex).toBe(1);
    db.closeSync();
  });

  test('closeOpenSegment gibt true zurueck, wenn ein Segment geschlossen wurde', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', NOW());
    startSegment(db, a.id, '2026-07-20T15:00:00Z');
    expect(closeOpenSegment(db, a.id, '2026-07-20T15:05:00Z')).toBe(true);
    // Zweiter Aufruf: kein offenes Segment mehr -> false (idempotent)
    expect(closeOpenSegment(db, a.id, '2026-07-20T15:05:00Z')).toBe(false);
    db.closeSync();
  });

  test('closeOpenSegment ist Idempotent bei "nichts offen"', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', NOW());
    expect(closeOpenSegment(db, a.id, NOW())).toBe(false);
    db.closeSync();
  });

  test('findOpenSegment liefert das juengste offene Segment oder null', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', NOW());
    expect(findOpenSegment(db, a.id)).toBeNull();
    startSegment(db, a.id, '2026-07-20T15:00:00Z');
    const open = findOpenSegment(db, a.id);
    expect(open?.segmentIndex).toBe(0);
    closeOpenSegment(db, a.id, '2026-07-20T15:05:00Z');
    expect(findOpenSegment(db, a.id)).toBeNull();
    db.closeSync();
  });

  test('listSegments liefert alle Segmente in segment_index-Reihenfolge', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', NOW());
    startSegment(db, a.id, '2026-07-20T15:00:00Z');
    closeOpenSegment(db, a.id, '2026-07-20T15:05:00Z');
    startSegment(db, a.id, '2026-07-20T15:10:00Z');
    closeOpenSegment(db, a.id, '2026-07-20T15:15:00Z');
    startSegment(db, a.id, '2026-07-20T15:20:00Z');
    const segs = listSegments(db, a.id);
    expect(segs.map((s) => s.segmentIndex)).toEqual([0, 1, 2]);
    expect(segs.map((s) => s.endedAt !== null)).toEqual([true, true, false]);
    db.closeSync();
  });
});

describe('closedActiveMs', () => {
  test('0, wenn keine Segmente', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', NOW());
    expect(closedActiveMs(db, a.id)).toBe(0);
    db.closeSync();
  });

  test('summiert nur GESCHLOSSENE Segmente', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', NOW());
    // 5 min geschlossen
    startSegment(db, a.id, '2026-07-20T15:00:00Z');
    closeOpenSegment(db, a.id, '2026-07-20T15:05:00Z');
    // 3 min geschlossen
    startSegment(db, a.id, '2026-07-20T15:10:00Z');
    closeOpenSegment(db, a.id, '2026-07-20T15:13:00Z');
    // Offen — soll NICHT gezaehlt werden
    startSegment(db, a.id, '2026-07-20T15:20:00Z');
    expect(closedActiveMs(db, a.id)).toBe((5 + 3) * 60 * 1000);
    db.closeSync();
  });

  test('ignoriert negative Zeitdifferenzen (defensiv)', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', NOW());
    // manuell einen Datensatz mit ended_at < started_at anlegen
    db.runSync(
      `INSERT INTO activity_segments (activity_id, segment_index, started_at, ended_at)
       VALUES (?, 0, ?, ?)`,
      [a.id, '2026-07-20T15:10:00Z', '2026-07-20T15:00:00Z'],
    );
    expect(closedActiveMs(db, a.id)).toBe(0);
    db.closeSync();
  });

  test('ignoriert ungueltige ISO-Zeitstempel (defensiv)', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', NOW());
    db.runSync(
      `INSERT INTO activity_segments (activity_id, segment_index, started_at, ended_at)
       VALUES (?, 0, ?, ?)`,
      [a.id, 'not-a-date', 'also-not'],
    );
    expect(closedActiveMs(db, a.id)).toBe(0);
    db.closeSync();
  });
});
