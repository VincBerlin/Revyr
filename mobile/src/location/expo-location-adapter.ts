// mobile/src/location/expo-location-adapter.ts
//
// Produktions-Adapter fuer expo-location. Wird in Jest gemockt (__mocks__).

import * as Location from 'expo-location';
import type {
  LocationPort,
  LocationSample,
  LocationSubscription,
} from './ports';

const DEFAULT_OPTIONS: Location.LocationOptions = {
  // BestForNavigation ist die praeziseste Klasse; passt fuer Sport-Tracking.
  // Bewusst KEIN distanceInterval, kein deferredUpdatesInterval — Filtern
  // erfolgt spaeter in einer eigenen Filterstufe (REQ-004 zweite Haelfte),
  // nicht auf der Empfangsgrenze.
  accuracy: Location.Accuracy.BestForNavigation,
  timeInterval: 1000,
  distanceInterval: 0,
};

export function createExpoLocationPort(): LocationPort {
  return {
    async requestForegroundPermission(): Promise<boolean> {
      const { status } = await Location.requestForegroundPermissionsAsync();
      return status === Location.PermissionStatus.GRANTED;
    },
    async watch(
      onSample: (sample: LocationSample) => void,
    ): Promise<LocationSubscription> {
      const sub = await Location.watchPositionAsync(DEFAULT_OPTIONS, (loc) => {
        onSample({
          latitude: loc.coords.latitude,
          longitude: loc.coords.longitude,
          timestampMs: loc.timestamp,
          accuracyMeters: loc.coords.accuracy ?? null,
          altitudeMeters: loc.coords.altitude ?? null,
          speedMps: loc.coords.speed ?? null,
          headingDegrees: loc.coords.heading ?? null,
          // mocked ist nur Android; iOS liefert undefined.
          isMocked:
            typeof loc.mocked === 'boolean' ? loc.mocked : null,
        });
      });
      return { cancel: (): void => sub.remove() };
    },
  };
}
