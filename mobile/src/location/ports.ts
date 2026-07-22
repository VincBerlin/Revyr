// mobile/src/location/ports.ts
//
// Port-Interface fuer die Standort-Grenze. Zwei Adapter:
//  - expo-location-adapter.ts (Produktion)
//  - fake-location-port.ts (Tests + Dev-UI-Modus)
//
// LocationSample ist bewusst PORT-lokal und NICHT gleich TrackPointV1:
// TrackPointV1 hat zusaetzlich source, isMocked, quality — Felder, die der
// RecordingCoordinator ableitet, nicht der Port.

export interface LocationSample {
  readonly latitude: number;
  readonly longitude: number;
  readonly timestampMs: number;
  readonly accuracyMeters: number | null;
  readonly altitudeMeters: number | null;
  readonly speedMps: number | null;
  readonly headingDegrees: number | null;
  // Mocked-Flag ist optional: expo-location liefert es nur auf Android; auf iOS
  // ist es undefined. Wir sagen "wissen wir nicht" mit null im Domain-Objekt.
  readonly isMocked: boolean | null;
}

export interface LocationSubscription {
  cancel(): void;
}

export interface LocationPort {
  requestForegroundPermission(): Promise<boolean>;
  watch(onSample: (sample: LocationSample) => void): Promise<LocationSubscription>;
}
