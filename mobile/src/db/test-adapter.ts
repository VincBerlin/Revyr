// mobile/src/db/test-adapter.ts
//
// Test-Adapter: better-sqlite3 (nur devDependency, laeuft in Node/Jest).
// Bringt die exakt selben SQLite-Kern-Semantiken (ACID, PRIMARY KEY,
// INSERT OR IGNORE, transaktionaler Rollback) — Adapter-Wechsel ist damit
// nicht Semantik-, sondern nur API-Wechsel.
//
// Diese Datei wird in Produktions-Builds NICHT eingezogen (nur in Tests).

import Database from 'better-sqlite3';
import type { RunResult, SQLiteBinding } from './ports';

export function openTestDatabase(pathOrMemory: string = ':memory:'): SQLiteBinding {
  const db = new Database(pathOrMemory);
  return {
    execSync(sql: string): void {
      db.exec(sql);
    },
    runSync(sql: string, params: readonly unknown[] = []): RunResult {
      const stmt = db.prepare(sql);
      const info = stmt.run(...(params as any[]));
      return { changes: info.changes };
    },
    getFirstSync<T>(sql: string, params: readonly unknown[] = []): T | null {
      const stmt = db.prepare(sql);
      const row = stmt.get(...(params as any[]));
      return (row as T | undefined) ?? null;
    },
    getAllSync<T>(sql: string, params: readonly unknown[] = []): T[] {
      const stmt = db.prepare(sql);
      return stmt.all(...(params as any[])) as T[];
    },
    withTransactionSync(fn: () => void): void {
      const tx = db.transaction(fn);
      tx();
    },
    closeSync(): void {
      db.close();
    },
  };
}
