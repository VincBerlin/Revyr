// mobile/src/services/quality/__tests__/filters.test.ts
import {
  accuracyFilter,
  stalenessFilter,
  jumpFilter,
  speedFilter,
} from '../filters';
import type { LocationSample } from '../../../location/ports';

const base: LocationSample = {
  latitude: 52.5, longitude: 13.4, timestampMs: 1729000000000,
  accuracyMeters: 5, altitudeMeters: null, speedMps: 3, headingDegrees: 0, isMocked: false,
};

describe('accuracyFilter', () => {
  const f = accuracyFilter({ acceptedBelowM: 20, rejectAboveM: 100 });

  test('accepted bei kleiner accuracy', () => {
    expect(f.evaluate({ ...base, accuracyMeters: 5 }, null).quality).toBe('accepted');
    expect(f.evaluate({ ...base, accuracyMeters: 19.9 }, null).quality).toBe('accepted');
  });

  test('low-confidence bei accuracy zwischen den Schwellen', () => {
    expect(f.evaluate({ ...base, accuracyMeters: 20.1 }, null).quality).toBe('low-confidence');
    expect(f.evaluate({ ...base, accuracyMeters: 99 }, null).quality).toBe('low-confidence');
  });

  test('rejected bei accuracy ueber der oberen Schwelle', () => {
    expect(f.evaluate({ ...base, accuracyMeters: 100.1 }, null).quality).toBe('rejected');
    expect(f.evaluate({ ...base, accuracyMeters: 500 }, null).quality).toBe('rejected');
  });

  test('null accuracy -> low-confidence (nicht rejected)', () => {
    const v = f.evaluate({ ...base, accuracyMeters: null }, null);
    expect(v.quality).toBe('low-confidence');
    expect(v.reason).toContain('accuracy=null');
  });

  test('wirft bei ungueltigen Optionen', () => {
    expect(() => accuracyFilter({ acceptedBelowM: 0, rejectAboveM: 10 })).toThrow();
    expect(() => accuracyFilter({ acceptedBelowM: 10, rejectAboveM: 5 })).toThrow();
    expect(() => accuracyFilter({ acceptedBelowM: 10, rejectAboveM: 10 })).toThrow();
  });
});

describe('stalenessFilter', () => {
  const now = 1729000060000; // 60s nach base.timestampMs
  const f = stalenessFilter({ maxAgeMs: 30000, nowMs: () => now });

  test('rejected, wenn Sample zu alt', () => {
    // base timestamp ist 60s alt -> ueber 30s
    expect(f.evaluate(base, null).quality).toBe('rejected');
  });

  test('accepted, wenn Sample frisch', () => {
    expect(f.evaluate({ ...base, timestampMs: now - 10000 }, null).quality).toBe('accepted');
    expect(f.evaluate({ ...base, timestampMs: now }, null).quality).toBe('accepted');
  });

  test('rejected, wenn Zeitstempel weit in der Zukunft (Geraeteuhr defekt)', () => {
    expect(f.evaluate({ ...base, timestampMs: now + 60000 }, null).quality).toBe('rejected');
  });

  test('wirft bei ungueltiger Option', () => {
    expect(() => stalenessFilter({ maxAgeMs: 0, nowMs: () => 0 })).toThrow();
  });
});

describe('jumpFilter', () => {
  const f = jumpFilter({ rejectAboveM: 500, rejectAboveMps: 25 });

  test('accepted ohne Vorgaenger', () => {
    expect(f.evaluate(base, null).quality).toBe('accepted');
  });

  test('accepted bei plausibler Distanz + Zeit', () => {
    // 10 m in 1 s -> 10 m/s < 25 m/s
    const next: LocationSample = {
      ...base,
      timestampMs: base.timestampMs + 1000,
      latitude: base.latitude + 0.00009, // ~ 10 m Nord
    };
    expect(f.evaluate(next, base).quality).toBe('accepted');
  });

  test('rejected bei Distanz ueber Absolutschwelle', () => {
    const next: LocationSample = {
      ...base,
      timestampMs: base.timestampMs + 10000,
      latitude: base.latitude + 0.01, // ~ 1,1 km
    };
    expect(f.evaluate(next, base).quality).toBe('rejected');
  });

  test('rejected bei implizit zu hoher Geschwindigkeit', () => {
    // 100 m in 1 s -> 100 m/s -> ueber 25 m/s
    const next: LocationSample = {
      ...base,
      timestampMs: base.timestampMs + 1000,
      latitude: base.latitude + 0.0009,
    };
    expect(f.evaluate(next, base).quality).toBe('rejected');
  });

  test('low-confidence bei nicht-fortschreitender Zeit', () => {
    const same: LocationSample = { ...base, timestampMs: base.timestampMs };
    expect(f.evaluate(same, base).quality).toBe('low-confidence');
    const back: LocationSample = { ...base, timestampMs: base.timestampMs - 1000 };
    expect(f.evaluate(back, base).quality).toBe('low-confidence');
  });
});

describe('speedFilter', () => {
  const f = speedFilter({ rejectAboveMps: 25 });

  test('accepted bei plausibler Geschwindigkeit', () => {
    expect(f.evaluate({ ...base, speedMps: 5 }, null).quality).toBe('accepted');
    expect(f.evaluate({ ...base, speedMps: 24.9 }, null).quality).toBe('accepted');
  });

  test('rejected bei Geschwindigkeit ueber Schwelle', () => {
    expect(f.evaluate({ ...base, speedMps: 25.1 }, null).quality).toBe('rejected');
    expect(f.evaluate({ ...base, speedMps: 100 }, null).quality).toBe('rejected');
  });

  test('rejected bei negativer Geschwindigkeit', () => {
    expect(f.evaluate({ ...base, speedMps: -1 }, null).quality).toBe('rejected');
  });

  test('null speed default erlaubt (accepted)', () => {
    expect(f.evaluate({ ...base, speedMps: null }, null).quality).toBe('accepted');
  });

  test('null speed mit allowNull=false -> low-confidence', () => {
    const strict = speedFilter({ rejectAboveMps: 25, allowNull: false });
    expect(strict.evaluate({ ...base, speedMps: null }, null).quality).toBe('low-confidence');
  });
});
