// mobile/src/db/__tests__/bootstrap.test.ts
import { openTestDatabase } from '../test-adapter';
import { closeOrphanedSegments, initializeDatabase, collectRecovery } from '../bootstrap';
import { startActivity } from '../activity-repo';
import { buildChunk, writeChunk } from '../chunk-repo';
import { migrateToLatest } from '../migrations';
import { closedActiveMs, findOpenSegment, startSegment } from '../segment-repo';

const NOW = (): string => '2026-07-20T15:00:00Z';

describe('initializeDatabase', () => {
  test('frischer Lauf: freshlyMigrated=true, keine Recovery-Faelle', () => {
    const boot = initializeDatabase({
      openDatabase: () => openTestDatabase(),
      now: NOW,
    });
    expect(boot.freshlyMigrated).toBe(true);
    expect(boot.recovery).toEqual([]);
    boot.db.closeSync();
  });

  test('zweiter Lauf gegen dieselbe DB: freshlyMigrated=false', () => {
    // Emuliert App-Neustart: eine Persistenz-DB (File) wird zwei Mal geoeffnet.
    const path = require('node:path').join(
      require('node:fs').mkdtempSync(require('node:path').join(require('node:os').tmpdir(), 'boot-')),
      'boot.sqlite',
    );

    const boot1 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: NOW,
    });
    expect(boot1.freshlyMigrated).toBe(true);
    boot1.db.closeSync();

    const boot2 = initializeDatabase({
      openDatabase: () => openTestDatabase(path),
      now: NOW,
    });
    expect(boot2.freshlyMigrated).toBe(false);
    boot2.db.closeSync();

    require('node:fs').unlinkSync(path);
  });
});

describe('collectRecovery', () => {
  function withMigratedDb<T>(fn: (db: ReturnType<typeof openTestDatabase>) => T): T {
    const db = openTestDatabase();
    migrateToLatest(db, NOW);
    try {
      return fn(db);
    } finally {
      db.closeSync();
    }
  }

  test('leere Recovery, wenn keine Aktivitaeten existieren', () => {
    withMigratedDb((db) => {
      expect(collectRecovery(db)).toEqual([]);
    });
  });

  test('unfinalisierte Aktivitaet ohne Chunks erscheint mit chunkCount=0, gaps=[]', () => {
    withMigratedDb((db) => {
      const act = startActivity(db, 'run', NOW());
      const rec = collectRecovery(db);
      expect(rec).toHaveLength(1);
      expect(rec[0].activity.id).toBe(act.id);
      expect(rec[0].chunkCount).toBe(0);
      expect(rec[0].highestChunkId).toBeNull();
      expect(rec[0].gaps).toEqual([]);
    });
  });

  test('unfinalisierte Aktivitaet mit Chunks + Luecke wird korrekt gemeldet', () => {
    withMigratedDb((db) => {
      const act = startActivity(db, 'ride', NOW());
      // Chunks 0, 1, 3 schreiben -> Luecke bei 2
      writeChunk(db, buildChunk(act.id, 0, []), NOW());
      writeChunk(db, buildChunk(act.id, 1, []), NOW());
      writeChunk(db, buildChunk(act.id, 3, []), NOW());
      const rec = collectRecovery(db);
      expect(rec).toHaveLength(1);
      expect(rec[0].chunkCount).toBe(3);
      expect(rec[0].highestChunkId).toBe(3);
      expect(rec[0].gaps).toEqual([2]);
    });
  });

  test('finalisierte Aktivitaet erscheint NICHT im Recovery-Bericht', () => {
    withMigratedDb((db) => {
      const act = startActivity(db, 'run', NOW());
      writeChunk(db, buildChunk(act.id, 0, []), NOW());
      db.runSync(
        `UPDATE activities SET finalized_at = ? WHERE id = ?`,
        [NOW(), act.id],
      );
      expect(collectRecovery(db)).toEqual([]);
    });
  });

  test('mehrere unfinalisierte Aktivitaeten erscheinen in Start-Reihenfolge', () => {
    withMigratedDb((db) => {
      const a1 = startActivity(db, 'run', NOW());
      const a2 = startActivity(db, 'ride', NOW());
      const a3 = startActivity(db, 'run', NOW());
      const rec = collectRecovery(db);
      expect(rec.map((r) => r.activity.id)).toEqual([a1.id, a2.id, a3.id]);
    });
  });

  test('activeMs wird pro Aktivitaet aus geschlossenen Segmenten aggregiert', () => {
    withMigratedDb((db) => {
      const a = startActivity(db, 'run', '2026-07-20T10:00:00Z');
      startSegment(db, a.id, '2026-07-20T10:00:00Z');
      db.runSync(
        `UPDATE activity_segments SET ended_at = ? WHERE activity_id = ? AND segment_index = 0`,
        ['2026-07-20T10:15:00Z', a.id],
      );
      startSegment(db, a.id, '2026-07-20T10:20:00Z');
      db.runSync(
        `UPDATE activity_segments SET ended_at = ? WHERE activity_id = ? AND segment_index = 1`,
        ['2026-07-20T10:25:00Z', a.id],
      );
      const rec = collectRecovery(db);
      expect(rec).toHaveLength(1);
      expect(rec[0].activeMs).toBe((15 + 5) * 60 * 1000);
    });
  });
});

describe('closeOrphanedSegments', () => {
  function freshDb() {
    const db = openTestDatabase();
    migrateToLatest(db, NOW);
    return db;
  }

  test('kein offenes Segment vorhanden -> 0 geschlossen', () => {
    const db = freshDb();
    expect(closeOrphanedSegments(db)).toBe(0);
    db.closeSync();
  });

  test('offenes Segment ohne Chunks wird auf started_at geschlossen (0 Aktivzeit)', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', '2026-07-20T10:00:00Z');
    startSegment(db, a.id, '2026-07-20T10:00:00Z');
    expect(closeOrphanedSegments(db)).toBe(1);
    const open = findOpenSegment(db, a.id);
    expect(open).toBeNull();
    // Aktivzeit aus dem geschlossenen Segment = 0 (ended_at == started_at)
    expect(closedActiveMs(db, a.id)).toBe(0);
    db.closeSync();
  });

  test('offenes Segment mit Chunks wird auf last_chunk.written_at geschlossen', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', '2026-07-20T10:00:00Z');
    startSegment(db, a.id, '2026-07-20T10:00:00Z');
    writeChunk(db, buildChunk(a.id, 0, []), '2026-07-20T10:05:00Z');
    writeChunk(db, buildChunk(a.id, 1, []), '2026-07-20T10:10:00Z');
    expect(closeOrphanedSegments(db)).toBe(1);
    // 10 min Aktivzeit
    expect(closedActiveMs(db, a.id)).toBe(10 * 60 * 1000);
    db.closeSync();
  });

  test('zweiter Aufruf ist idempotent (keine offenen Segmente mehr)', () => {
    const db = freshDb();
    const a = startActivity(db, 'run', '2026-07-20T10:00:00Z');
    startSegment(db, a.id, '2026-07-20T10:00:00Z');
    closeOrphanedSegments(db);
    expect(closeOrphanedSegments(db)).toBe(0);
    db.closeSync();
  });

  test('initializeDatabase ruft closeOrphanedSegments und meldet die Zahl', () => {
    const path = require('node:path').join(
      require('node:fs').mkdtempSync(require('node:path').join(require('node:os').tmpdir(), 'orphan-')),
      'db.sqlite',
    );
    // Lauf 1: Aktivitaet mit offenem Segment simulieren
    const boot1 = initializeDatabase({ openDatabase: () => openTestDatabase(path), now: NOW });
    expect(boot1.orphansClosed).toBe(0); // frischer DB, nichts zu schliessen
    const a = startActivity(boot1.db, 'run', '2026-07-20T10:00:00Z');
    startSegment(boot1.db, a.id, '2026-07-20T10:00:00Z');
    boot1.db.closeSync();

    // Lauf 2: Bootstrap sieht das offene Segment und schliesst es
    const boot2 = initializeDatabase({ openDatabase: () => openTestDatabase(path), now: NOW });
    expect(boot2.orphansClosed).toBe(1);
    // Dritter Bootstrap: keine mehr
    boot2.db.closeSync();
    const boot3 = initializeDatabase({ openDatabase: () => openTestDatabase(path), now: NOW });
    expect(boot3.orphansClosed).toBe(0);
    boot3.db.closeSync();
    require('node:fs').unlinkSync(path);
  });
});
