// mobile/src/db/expo-adapter.ts
//
// Produktions-Adapter: expo-sqlite.
// Diese Datei wird beim Import in Jest gemockt (siehe Jest-Konfiguration); die
// wirklichen expo-sqlite-Symbole werden erst auf einem Geraet geladen.

import * as SQLite from 'expo-sqlite';
import type { RunResult, SQLiteBinding } from './ports';

export function openExpoDatabase(name: string): SQLiteBinding {
  const db = SQLite.openDatabaseSync(name);
  return {
    execSync(sql: string): void {
      db.execSync(sql);
    },
    runSync(sql: string, params: readonly unknown[] = []): RunResult {
      const result = db.runSync(sql, params as SQLite.SQLiteBindValue[]);
      return { changes: result.changes };
    },
    getFirstSync<T>(sql: string, params: readonly unknown[] = []): T | null {
      const row = db.getFirstSync(sql, params as SQLite.SQLiteBindValue[]);
      return (row as T | null) ?? null;
    },
    getAllSync<T>(sql: string, params: readonly unknown[] = []): T[] {
      return db.getAllSync(sql, params as SQLite.SQLiteBindValue[]) as T[];
    },
    withTransactionSync(fn: () => void): void {
      db.withTransactionSync(fn);
    },
    closeSync(): void {
      db.closeSync();
    },
  };
}
