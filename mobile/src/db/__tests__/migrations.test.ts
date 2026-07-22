// mobile/src/db/__tests__/migrations.test.ts
import { openTestDatabase } from '../test-adapter';
import {
  CURRENT_SCHEMA_VERSION,
  appliedVersions,
  currentSchemaVersion,
  migrateToLatest,
  migrateToV1,
  migrateToV2,
} from '../migrations';
import { startActivity, finalizeActivity } from '../activity-repo';

const NOW = (): string => '2026-07-20T14:00:00Z';

describe('migrateToV1', () => {
  test('erstellt schema_versions und meldet Version 0 vor Migration', () => {
    const db = openTestDatabase();
    expect(currentSchemaVersion(db)).toBe(0);
    db.closeSync();
  });

  test('erster Aufruf migriert (return true), zweiter ist No-Op (return false)', () => {
    const db = openTestDatabase();
    expect(migrateToV1(db, NOW)).toBe(true);
    expect(migrateToV1(db, NOW)).toBe(false);
    expect(migrateToV1(db, NOW)).toBe(false);
    db.closeSync();
  });

  test('schema_versions haelt exakt EINE Zeile fuer Version 1', () => {
    const db = openTestDatabase();
    migrateToV1(db, NOW);
    migrateToV1(db, NOW);
    migrateToV1(db, NOW);
    expect(appliedVersions(db)).toEqual([CURRENT_SCHEMA_VERSION]);
    db.closeSync();
  });

  test('nach Migration existieren activities und track_point_chunks', () => {
    const db = openTestDatabase();
    migrateToV1(db, NOW);
    const tables = db.getAllSync<{ name: string }>(
      `SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name`,
    ).map((t) => t.name);
    expect(tables).toContain('activities');
    expect(tables).toContain('track_point_chunks');
    expect(tables).toContain('schema_versions');
    db.closeSync();
  });

  test('CHECK-Constraint auf sport verhindert ungueltige Werte', () => {
    const db = openTestDatabase();
    migrateToV1(db, NOW);
    expect(() =>
      db.runSync(
        `INSERT INTO activities (sport, started_at) VALUES (?, ?)`,
        ['skibike', NOW()],
      ),
    ).toThrow();
    db.closeSync();
  });

  test('CURRENT_SCHEMA_VERSION ist 2 (Aktivzeit-Segmente)', () => {
    expect(CURRENT_SCHEMA_VERSION).toBe(2);
  });

  test('PRIMARY KEY (activity_id, chunk_id) verhindert Duplikate', () => {
    const db = openTestDatabase();
    migrateToV1(db, NOW);
    db.runSync(
      `INSERT INTO activities (sport, started_at) VALUES (?, ?)`,
      ['run', NOW()],
    );
    const aid = db.getFirstSync<{ id: number }>(`SELECT MAX(id) AS id FROM activities`)!.id;
    db.runSync(
      `INSERT INTO track_point_chunks
         (activity_id, chunk_id, points_json, points_count, written_at)
       VALUES (?, ?, ?, ?, ?)`,
      [aid, 0, '[]', 0, NOW()],
    );
    // Ohne INSERT OR IGNORE muss ein zweites INSERT mit gleichem PK werfen.
    expect(() =>
      db.runSync(
        `INSERT INTO track_point_chunks
           (activity_id, chunk_id, points_json, points_count, written_at)
         VALUES (?, ?, ?, ?, ?)`,
        [aid, 0, '[]', 0, NOW()],
      ),
    ).toThrow();
    db.closeSync();
  });
});

describe('migrateToV2', () => {
  test('idempotent — zweiter Aufruf ist No-Op', () => {
    const db = openTestDatabase();
    migrateToV1(db, NOW);
    expect(migrateToV2(db, NOW)).toBe(true);
    expect(migrateToV2(db, NOW)).toBe(false);
    expect(appliedVersions(db)).toEqual([1, 2]);
    db.closeSync();
  });

  test('erstellt activity_segments-Tabelle', () => {
    const db = openTestDatabase();
    migrateToV2(db, NOW);
    const tables = db.getAllSync<{ name: string }>(
      `SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name`,
    ).map((t) => t.name);
    expect(tables).toContain('activity_segments');
    db.closeSync();
  });

  test('backfillt EIN Segment pro existierender Aktivitaet', () => {
    const db = openTestDatabase();
    // Erst V1 anwenden, Aktivitaeten anlegen (unfinalisierte + finalisierte)
    migrateToV1(db, NOW);
    const a1 = startActivity(db, 'run', '2026-07-20T10:00:00Z');
    const a2 = startActivity(db, 'ride', '2026-07-20T11:00:00Z');
    finalizeActivity(db, a2.id, '2026-07-20T11:30:00Z');
    // Dann V2
    migrateToV2(db, NOW);
    const segs = db.getAllSync<{ activity_id: number; started_at: string; ended_at: string | null }>(
      `SELECT activity_id, started_at, ended_at FROM activity_segments ORDER BY activity_id`,
    );
    expect(segs).toHaveLength(2);
    // a1 (unfinalisiert): open segment
    expect(segs[0].activity_id).toBe(a1.id);
    expect(segs[0].started_at).toBe('2026-07-20T10:00:00Z');
    expect(segs[0].ended_at).toBeNull();
    // a2 (finalisiert): geschlossenes Segment
    expect(segs[1].activity_id).toBe(a2.id);
    expect(segs[1].started_at).toBe('2026-07-20T11:00:00Z');
    expect(segs[1].ended_at).toBe('2026-07-20T11:30:00Z');
    db.closeSync();
  });

  test('migrateToV2 ruft V1 zuerst auf, wenn V1 fehlt', () => {
    const db = openTestDatabase();
    // Direkt V2 aufrufen ohne vorher V1
    expect(migrateToV2(db, NOW)).toBe(true);
    expect(appliedVersions(db)).toEqual([1, 2]);
    db.closeSync();
  });
});

describe('migrateToLatest', () => {
  test('frischer Lauf: true, beide Migrationen laufen', () => {
    const db = openTestDatabase();
    expect(migrateToLatest(db, NOW)).toBe(true);
    expect(appliedVersions(db)).toEqual([1, 2]);
    db.closeSync();
  });

  test('bereits auf latest: false', () => {
    const db = openTestDatabase();
    migrateToLatest(db, NOW);
    expect(migrateToLatest(db, NOW)).toBe(false);
    db.closeSync();
  });
});
