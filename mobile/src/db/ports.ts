// mobile/src/db/ports.ts
//
// Port-Interface fuer die synchrone SQLite-Grenze. Zwei Adapter erfuellen es:
//  - expo-adapter.ts (Produktion, expo-sqlite)
//  - test-adapter.ts (Tests, better-sqlite3)
//
// Die Semantik ist der Schnittmengen-API der beiden Bindings entnommen und
// bewusst KLEIN gehalten. Wo ein Adapter ueber die Schnittmenge hinausgeht,
// bleibt das im Adapter, nicht im Port.

export interface RunResult {
  changes: number;
}

export interface SQLiteBinding {
  execSync(sql: string): void;
  runSync(sql: string, params?: readonly unknown[]): RunResult;
  getFirstSync<T>(sql: string, params?: readonly unknown[]): T | null;
  getAllSync<T>(sql: string, params?: readonly unknown[]): T[];
  withTransactionSync(fn: () => void): void;
  closeSync(): void;
}
