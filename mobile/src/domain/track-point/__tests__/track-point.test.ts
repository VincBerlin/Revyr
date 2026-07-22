// mobile/src/domain/track-point/__tests__/track-point.test.ts
//
// TDD-Tests fuer den TrackPointV1-Domainkern. Colocated in __tests__/ pro Modul.
// Ableitungsquelle: spikes/p0-02/ (Python-Kern + TS-Paritaet), aber jeder Fall
// hier ist eigenstaendig geprueft und trifft die produktive Zod-Schema-Semantik.

import {
  TRACK_POINT_SOURCE_VALUES,
  TRACK_POINT_QUALITY_VALUES,
  TrackPointValidationError,
  validateTrackPoint,
  toFiniteOrNull,
  type TrackPointV1,
} from '../track-point';

const validPoint: TrackPointV1 = {
  latitude: -33.9249,
  longitude: 18.4241,
  timestampMs: 1729000000000,
  accuracyMeters: 4.2,
  altitudeMeters: -1.5,
  speedMps: 3.14,
  headingDegrees: 359.9,
  source: 'foreground',
  isMocked: false,
  quality: 'accepted',
};

describe('validateTrackPoint', () => {
  test('akzeptiert einen vollstaendig belegten Punkt', () => {
    expect(validateTrackPoint(validPoint)).toEqual(validPoint);
  });

  test('akzeptiert null in allen nullbaren Feldern', () => {
    const nulled = {
      ...validPoint,
      accuracyMeters: null,
      altitudeMeters: null,
      speedMps: null,
      headingDegrees: null,
      isMocked: null,
    };
    expect(validateTrackPoint(nulled)).toEqual(nulled);
  });

  test.each(TRACK_POINT_SOURCE_VALUES)('akzeptiert source %s', (src) => {
    expect(validateTrackPoint({ ...validPoint, source: src }).source).toBe(src);
  });

  test.each(TRACK_POINT_QUALITY_VALUES)('akzeptiert quality %s', (q) => {
    expect(validateTrackPoint({ ...validPoint, quality: q }).quality).toBe(q);
  });

  test('lehnt unbekannten source-Wert ab', () => {
    expect(() => validateTrackPoint({ ...validPoint, source: 'dogsled' }))
      .toThrow(TrackPointValidationError);
  });

  test('lehnt unbekannten quality-Wert ab', () => {
    expect(() => validateTrackPoint({ ...validPoint, quality: 'gold' }))
      .toThrow(TrackPointValidationError);
  });

  test('lehnt fehlendes source ab (kein optionaler Schluessel)', () => {
    const { source: _drop, ...rest } = validPoint;
    void _drop;
    expect(() => validateTrackPoint(rest)).toThrow(TrackPointValidationError);
  });

  test('lehnt undefined statt null ab', () => {
    // undefined im JSON verschwindet still (F5). Zod-.nullable() ohne .optional()
    // besteht auf entweder einem Wert oder ausdruecklich null.
    const withUndef = { ...validPoint, isMocked: undefined };
    expect(() => validateTrackPoint(withUndef)).toThrow(TrackPointValidationError);
  });

  test('lehnt NaN in numerischen Feldern ab (F4)', () => {
    expect(() => validateTrackPoint({ ...validPoint, accuracyMeters: NaN }))
      .toThrow(TrackPointValidationError);
    expect(() => validateTrackPoint({ ...validPoint, latitude: NaN }))
      .toThrow(TrackPointValidationError);
  });

  test('lehnt Infinity in numerischen Feldern ab (F4)', () => {
    expect(() => validateTrackPoint({ ...validPoint, speedMps: Infinity }))
      .toThrow(TrackPointValidationError);
    expect(() => validateTrackPoint({ ...validPoint, speedMps: -Infinity }))
      .toThrow(TrackPointValidationError);
  });

  test('lehnt latitude ausserhalb [-90, 90] ab', () => {
    expect(() => validateTrackPoint({ ...validPoint, latitude: 90.0001 }))
      .toThrow(TrackPointValidationError);
    expect(() => validateTrackPoint({ ...validPoint, latitude: -90.0001 }))
      .toThrow(TrackPointValidationError);
  });

  test('lehnt longitude ausserhalb [-180, 180] ab', () => {
    expect(() => validateTrackPoint({ ...validPoint, longitude: 181 }))
      .toThrow(TrackPointValidationError);
  });

  test('lehnt negativen timestampMs ab', () => {
    expect(() => validateTrackPoint({ ...validPoint, timestampMs: -1 }))
      .toThrow(TrackPointValidationError);
  });

  test('lehnt nicht-integer timestampMs ab', () => {
    expect(() => validateTrackPoint({ ...validPoint, timestampMs: 1.5 }))
      .toThrow(TrackPointValidationError);
  });

  test('null ist NICHT gleich false in isMocked (F4)', () => {
    const nullPoint = validateTrackPoint({ ...validPoint, isMocked: null });
    const falsePoint = validateTrackPoint({ ...validPoint, isMocked: false });
    expect(nullPoint.isMocked).toBeNull();
    expect(falsePoint.isMocked).toBe(false);
    expect(nullPoint.isMocked === falsePoint.isMocked).toBe(false);
  });

  test('TrackPointValidationError meldet Anzahl und Feldpfade der Verletzungen', () => {
    try {
      validateTrackPoint({ ...validPoint, source: 'x', quality: 'y' });
      throw new Error('sollte gescheitert sein');
    } catch (e) {
      expect(e).toBeInstanceOf(TrackPointValidationError);
      const err = e as TrackPointValidationError;
      expect(err.issues).toHaveLength(2);
      expect(err.message).toContain('source');
      expect(err.message).toContain('quality');
    }
  });
});

describe('toFiniteOrNull', () => {
  test('gibt null fuer null und undefined', () => {
    expect(toFiniteOrNull(null)).toBeNull();
    expect(toFiniteOrNull(undefined)).toBeNull();
  });

  test('gibt null fuer NaN und Infinity', () => {
    expect(toFiniteOrNull(NaN)).toBeNull();
    expect(toFiniteOrNull(Infinity)).toBeNull();
    expect(toFiniteOrNull(-Infinity)).toBeNull();
  });

  test('gibt endliche Zahlen unveraendert zurueck', () => {
    expect(toFiniteOrNull(0)).toBe(0);
    expect(toFiniteOrNull(-1.5)).toBe(-1.5);
    expect(toFiniteOrNull(Number.MAX_SAFE_INTEGER)).toBe(Number.MAX_SAFE_INTEGER);
  });

  test('macht 0 nicht zu null (kein falsy-Fallback)', () => {
    expect(toFiniteOrNull(0)).toBe(0);
    expect(toFiniteOrNull(-0)).toBe(-0);
  });
});
