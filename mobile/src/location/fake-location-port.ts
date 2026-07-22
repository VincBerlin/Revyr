// mobile/src/location/fake-location-port.ts
//
// Test- und Dev-Fake fuer LocationPort. Erlaubt es dem Test/der Dev-UI, Samples
// synchron zu triggern und Berechtigung zu simulieren.
//
// Kein echter GPS-Zugriff. In der Dev-UI wird diese Instanz nie eingezogen,
// sofern die App auf einem Geraet laeuft; sie ist eine explizite Test-Alternative.

import type {
  LocationPort,
  LocationSample,
  LocationSubscription,
} from './ports';

export interface FakeLocationPort extends LocationPort {
  /** Manuell einen Sample einspeisen (nur Test/Dev). */
  emit(sample: LocationSample): void;
  /** Anzahl aktiver Subscriptions (zur Verifikation von pause/resume). */
  activeSubscriptions(): number;
  /** Steuert das Ergebnis von requestForegroundPermission. */
  setPermissionGranted(granted: boolean): void;
}

export function createFakeLocationPort(): FakeLocationPort {
  const listeners = new Set<(sample: LocationSample) => void>();
  let permissionGranted = true;

  return {
    async requestForegroundPermission(): Promise<boolean> {
      return permissionGranted;
    },
    async watch(
      onSample: (sample: LocationSample) => void,
    ): Promise<LocationSubscription> {
      listeners.add(onSample);
      return {
        cancel(): void {
          listeners.delete(onSample);
        },
      };
    },
    emit(sample: LocationSample): void {
      for (const l of listeners) l(sample);
    },
    activeSubscriptions(): number {
      return listeners.size;
    },
    setPermissionGranted(granted: boolean): void {
      permissionGranted = granted;
    },
  };
}
