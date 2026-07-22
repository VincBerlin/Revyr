// mobile/src/services/fake-app-state-source.ts
//
// Test- und Dev-Fake fuer AppStateSource. Kein react-native-Import — die Tests
// koennen den Fake ohne Jest-Mocking laden.

import type { AppLifecycle, AppStateSource } from './app-state-bridge';

export interface FakeAppStateSource extends AppStateSource {
  set(state: AppLifecycle): void;
  listenerCount(): number;
}

export function createFakeAppStateSource(initial: AppLifecycle = 'active'): FakeAppStateSource {
  const listeners = new Set<(s: AppLifecycle) => void>();
  let current: AppLifecycle = initial;
  return {
    addChangeListener(fn: (s: AppLifecycle) => void): () => void {
      listeners.add(fn);
      return (): void => {
        listeners.delete(fn);
      };
    },
    currentState(): AppLifecycle {
      return current;
    },
    set(state: AppLifecycle): void {
      current = state;
      for (const l of listeners) l(state);
    },
    listenerCount(): number {
      return listeners.size;
    },
  };
}
