// Jest-Mock fuer expo-sqlite.
// Wird nur greifen, wenn ein Testfile expo-adapter.ts (oder expo-sqlite direkt) importiert.
// Aktuelle Tests nutzen test-adapter.ts und beruehren dieses Mock nicht.
export function openDatabaseSync(): unknown {
  throw new Error(
    'expo-sqlite ist in Jest gemockt. Tests muessen test-adapter.ts nutzen, ' +
    'nicht expo-adapter.ts. Fuer Geraetetests siehe P0-03-Ledger.',
  );
}
export type SQLiteBindValue = string | number | null | Uint8Array;
