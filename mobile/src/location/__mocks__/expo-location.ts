// Jest-Mock fuer expo-location. Analog zum expo-sqlite-Mock:
// Wird nur greifen, wenn ein Testfile expo-location-adapter.ts (oder expo-location
// direkt) importiert. Aktuelle Tests nutzen den FakeLocationPort und beruehren
// dieses Mock nicht.
export const Accuracy = {
  BestForNavigation: 6,
} as const;

export const PermissionStatus = {
  GRANTED: 'granted',
  DENIED: 'denied',
  UNDETERMINED: 'undetermined',
} as const;

export function requestForegroundPermissionsAsync(): never {
  throw new Error(
    'expo-location ist in Jest gemockt. Tests muessen fake-location-port.ts nutzen. ' +
    'Fuer Geraetetests siehe docs/testing/phase-0-device-smoke-test.md.',
  );
}

export function watchPositionAsync(): never {
  throw new Error(
    'expo-location ist in Jest gemockt. Tests muessen fake-location-port.ts nutzen.',
  );
}
