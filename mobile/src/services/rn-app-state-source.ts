// mobile/src/services/rn-app-state-source.ts
//
// Produktions-Adapter fuer den AppStateSource-Port. Nur hier greift react-native.
// Wird in Jest gemockt (jest.config.js moduleNameMapper).

import { AppState, type AppStateStatus } from 'react-native';
import type { AppLifecycle, AppStateSource } from './app-state-bridge';

function normalize(s: AppStateStatus): AppLifecycle {
  if (s === 'active') return 'active';
  if (s === 'background') return 'background';
  return 'inactive';
}

export function createRnAppStateSource(): AppStateSource {
  return {
    addChangeListener(fn: (state: AppLifecycle) => void): () => void {
      const sub = AppState.addEventListener('change', (s) => fn(normalize(s)));
      return () => sub.remove();
    },
    currentState(): AppLifecycle {
      return normalize(AppState.currentState);
    },
  };
}
