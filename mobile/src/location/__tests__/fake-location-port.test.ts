// mobile/src/location/__tests__/fake-location-port.test.ts
import { createFakeLocationPort } from '../fake-location-port';
import type { LocationSample } from '../ports';

function sample(overrides: Partial<LocationSample> = {}): LocationSample {
  return {
    latitude: 52.5,
    longitude: 13.4,
    timestampMs: Date.parse('2026-07-20T15:00:00Z'),
    accuracyMeters: 4.2,
    altitudeMeters: null,
    speedMps: 3.1,
    headingDegrees: 90,
    isMocked: true,
    ...overrides,
  };
}

describe('FakeLocationPort', () => {
  test('requestForegroundPermission liefert steuerbaren Wert', async () => {
    const port = createFakeLocationPort();
    expect(await port.requestForegroundPermission()).toBe(true);
    port.setPermissionGranted(false);
    expect(await port.requestForegroundPermission()).toBe(false);
  });

  test('watch registriert einen Listener; cancel entfernt ihn', async () => {
    const port = createFakeLocationPort();
    const received: LocationSample[] = [];
    const sub = await port.watch((s) => received.push(s));
    expect(port.activeSubscriptions()).toBe(1);
    port.emit(sample());
    port.emit(sample({ latitude: 51 }));
    expect(received).toHaveLength(2);
    sub.cancel();
    expect(port.activeSubscriptions()).toBe(0);
    port.emit(sample()); // nach cancel keine Zustellung mehr
    expect(received).toHaveLength(2);
  });

  test('mehrere watch-Aufrufe: alle Listener bekommen jedes Sample', async () => {
    const port = createFakeLocationPort();
    const a: LocationSample[] = [];
    const b: LocationSample[] = [];
    await port.watch((s) => a.push(s));
    await port.watch((s) => b.push(s));
    port.emit(sample());
    expect(a).toHaveLength(1);
    expect(b).toHaveLength(1);
    expect(port.activeSubscriptions()).toBe(2);
  });
});
