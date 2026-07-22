// mobile/src/services/quality/__tests__/geo.test.ts
import { haversineDistanceM } from '../geo';

describe('haversineDistanceM', () => {
  test('gleicher Punkt -> 0', () => {
    const p = { latitude: 52.5, longitude: 13.4 };
    expect(haversineDistanceM(p, p)).toBe(0);
  });

  test('bekannte Distanz Berlin (Brandenburger Tor) -> Alexanderplatz ~2,2 km', () => {
    const brandenburgerTor = { latitude: 52.5163, longitude: 13.3777 };
    const alexanderplatz = { latitude: 52.5219, longitude: 13.4132 };
    const d = haversineDistanceM(brandenburgerTor, alexanderplatz);
    expect(d).toBeGreaterThan(2400);
    expect(d).toBeLessThan(2500);
  });

  test('1 Grad Latitude ~ 111 km', () => {
    const a = { latitude: 0, longitude: 0 };
    const b = { latitude: 1, longitude: 0 };
    const d = haversineDistanceM(a, b);
    expect(d).toBeGreaterThan(111_000);
    expect(d).toBeLessThan(111_500);
  });

  test('symmetrisch', () => {
    const a = { latitude: 40, longitude: -74 };
    const b = { latitude: 51, longitude: 0 };
    expect(haversineDistanceM(a, b)).toBeCloseTo(haversineDistanceM(b, a), 6);
  });
});
