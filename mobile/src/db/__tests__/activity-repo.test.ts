// mobile/src/db/__tests__/activity-repo.test.ts
import { openTestDatabase } from '../test-adapter';
import { migrateToLatest } from '../migrations';
import {
  finalizeActivity,
  findUnfinalized,
  getActivity,
  listFinalizedActivities,
  startActivity,
} from '../activity-repo';

const NOW = (): string => '2026-07-20T14:00:00Z';
const LATER = (): string => '2026-07-20T14:30:00Z';

function freshDb() {
  const db = openTestDatabase();
  migrateToLatest(db, NOW);
  return db;
}

describe('activity-repo', () => {
  test('startActivity liefert ID + Startzeit + finalizedAt=null', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    expect(act.id).toBeGreaterThan(0);
    expect(act.sport).toBe('run');
    expect(act.startedAt).toBe(NOW());
    expect(act.finalizedAt).toBeNull();
    db.closeSync();
  });

  test('getActivity liefert dieselbe Aktivitaet zurueck', () => {
    const db = freshDb();
    const act = startActivity(db, 'ride', NOW());
    expect(getActivity(db, act.id)).toEqual(act);
    db.closeSync();
  });

  test('getActivity fuer unbekannte ID liefert null', () => {
    const db = freshDb();
    expect(getActivity(db, 99999)).toBeNull();
    db.closeSync();
  });

  test('finalizeActivity setzt finalizedAt', () => {
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    finalizeActivity(db, act.id, LATER());
    const updated = getActivity(db, act.id);
    expect(updated?.finalizedAt).toBe(LATER());
    db.closeSync();
  });

  test('finalizeActivity ist NICHT idempotent bei zweiter Finalisierung', () => {
    // Zweite Finalisierung deutet auf einen App-Bug hin — sichtbar melden, nicht schlucken.
    const db = freshDb();
    const act = startActivity(db, 'run', NOW());
    finalizeActivity(db, act.id, LATER());
    expect(() => finalizeActivity(db, act.id, LATER())).toThrow();
    db.closeSync();
  });

  test('findUnfinalized meldet nur nicht-finalisierte Aktivitaeten', () => {
    const db = freshDb();
    const a1 = startActivity(db, 'run', NOW());
    const a2 = startActivity(db, 'ride', NOW());
    const a3 = startActivity(db, 'run', NOW());
    finalizeActivity(db, a2.id, LATER());
    const unfin = findUnfinalized(db).map((a) => a.id);
    expect(unfin).toEqual([a1.id, a3.id]);
    db.closeSync();
  });
});

describe('listFinalizedActivities', () => {
  test('liefert nur finalisierte Aktivitaeten, neueste zuerst', () => {
    const db = freshDb();
    const a1 = startActivity(db, 'run', NOW());
    const a2 = startActivity(db, 'ride', NOW());
    const a3 = startActivity(db, 'run', NOW());
    // a3 zuerst finalisieren, dann a1 spaeter -> a1 sollte vor a3 stehen
    finalizeActivity(db, a3.id, '2026-07-20T10:00:00Z');
    finalizeActivity(db, a1.id, '2026-07-20T11:00:00Z');
    // a2 bleibt unfinalisiert
    const list = listFinalizedActivities(db).map((a) => a.id);
    expect(list).toEqual([a1.id, a3.id]);
    db.closeSync();
  });

  test('leere Liste, wenn nichts finalisiert', () => {
    const db = freshDb();
    startActivity(db, 'run', NOW());
    expect(listFinalizedActivities(db)).toEqual([]);
    db.closeSync();
  });

  test('respektiert limit', () => {
    const db = freshDb();
    for (let i = 0; i < 5; i++) {
      const a = startActivity(db, 'run', NOW());
      finalizeActivity(db, a.id, `2026-07-20T${String(i).padStart(2, '0')}:00:00Z`);
    }
    expect(listFinalizedActivities(db, 3)).toHaveLength(3);
    expect(listFinalizedActivities(db, 100)).toHaveLength(5);
    expect(listFinalizedActivities(db, 0)).toEqual([]);
    db.closeSync();
  });
});
