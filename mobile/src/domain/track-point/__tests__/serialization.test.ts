// mobile/src/domain/track-point/__tests__/serialization.test.ts

import {
  serializeTrackPoint,
  deserializeTrackPoint,
  serializePoints,
  deserializePoints,
  SerializationError,
} from '../serialization';
import { TrackPointValidationError, type TrackPointV1 } from '../track-point';

const p: TrackPointV1 = {
  latitude: -33.9249,
  longitude: 18.4241,
  timestampMs: 1729000000000,
  accuracyMeters: 4.2,
  altitudeMeters: null,
  speedMps: 3.14,
  headingDegrees: 359.9,
  source: 'foreground',
  isMocked: false,
  quality: 'accepted',
};

describe('serializeTrackPoint / deserializeTrackPoint', () => {
  test('Roundtrip erhaelt alle Felder', () => {
    expect(deserializeTrackPoint(serializeTrackPoint(p))).toEqual(p);
  });

  test('Schluesselreihenfolge ist deterministisch', () => {
    const p2 = { ...p };
    // Reorder-Versuch: Serializer muss trotzdem stabile Reihenfolge liefern
    const shuffled: any = {};
    Object.entries(p2).reverse().forEach(([k, v]) => (shuffled[k] = v));
    expect(serializeTrackPoint(shuffled)).toBe(serializeTrackPoint(p));
  });

  test('lehnt ungueltiges JSON ab', () => {
    expect(() => deserializeTrackPoint('nicht json')).toThrow(SerializationError);
    expect(() => deserializeTrackPoint('{"unclosed')).toThrow(SerializationError);
  });

  test('lehnt gueltiges JSON mit ungueltigem Punkt ab', () => {
    expect(() => deserializeTrackPoint('{"latitude": 200}')).toThrow(TrackPointValidationError);
  });

  test('lehnt Payload mit NaN-Marker ab (JSON hat kein NaN)', () => {
    // Manuell konstruiert, wie es JSON.stringify(NaN) tut: 'null'.
    // Der Roundtrip wuerde einen null-Wert liefern; die Validierung lehnt den
    // Missing-required-Fall latitude=null nicht — latitude hat null NICHT als
    // Zulassung. Der Test dokumentiert die Vorteilhaftigkeit der Schema-Strenge.
    expect(() => deserializeTrackPoint('{"latitude": null}')).toThrow(TrackPointValidationError);
  });

  test('serializePoints / deserializePoints als JSONL', () => {
    const points: TrackPointV1[] = [p, { ...p, timestampMs: p.timestampMs + 1000 }];
    const payload = serializePoints(points);
    expect(payload.split('\n')).toHaveLength(2);
    expect(deserializePoints(payload)).toEqual(points);
  });

  test('deserializePoints tolerantiert leere Zeilen und leeren Payload', () => {
    expect(deserializePoints('')).toEqual([]);
    expect(deserializePoints('\n\n')).toEqual([]);
    const payload = `${serializeTrackPoint(p)}\n\n${serializeTrackPoint(p)}\n`;
    expect(deserializePoints(payload)).toHaveLength(2);
  });
});
