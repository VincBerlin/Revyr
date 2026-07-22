// mobile/src/services/quality/__tests__/pipeline.test.ts
import { pipeline, type QualityFilter, type FilterVerdict } from '../pipeline';
import type { LocationSample } from '../../../location/ports';

const sample: LocationSample = {
  latitude: 52.5, longitude: 13.4, timestampMs: 1729000000000,
  accuracyMeters: 5, altitudeMeters: null, speedMps: 3, headingDegrees: 0, isMocked: false,
};

function verdict(quality: FilterVerdict['quality'], name = 'test'): QualityFilter {
  return {
    name,
    evaluate: (): FilterVerdict => ({ quality, reason: quality, filter: name }),
  };
}

describe('pipeline', () => {
  test('leere Filterliste liefert accepted', () => {
    const p = pipeline();
    expect(p.classify(sample, null).quality).toBe('accepted');
    expect(p.classify(sample, null).filter).toBe('pipeline');
  });

  test('alle accepted -> accepted', () => {
    const p = pipeline(verdict('accepted', 'a'), verdict('accepted', 'b'));
    expect(p.classify(sample, null).quality).toBe('accepted');
  });

  test('irgendein low-confidence -> low-confidence', () => {
    const p = pipeline(verdict('accepted', 'a'), verdict('low-confidence', 'b'), verdict('accepted', 'c'));
    const v = p.classify(sample, null);
    expect(v.quality).toBe('low-confidence');
    expect(v.filter).toBe('b');
  });

  test('erstes rejected beendet die Kette (early exit)', () => {
    const later = jest.fn();
    const laterFilter: QualityFilter = { name: 'later', evaluate: later };
    const p = pipeline(verdict('accepted', 'a'), verdict('rejected', 'b'), laterFilter);
    const v = p.classify(sample, null);
    expect(v.quality).toBe('rejected');
    expect(v.filter).toBe('b');
    expect(later).not.toHaveBeenCalled();
  });

  test('low-confidence gefolgt von rejected wird zu rejected', () => {
    const p = pipeline(verdict('low-confidence', 'a'), verdict('rejected', 'b'));
    expect(p.classify(sample, null).quality).toBe('rejected');
  });

  test('erste low-confidence wird gemeldet (nicht die zweite)', () => {
    const p = pipeline(verdict('low-confidence', 'first'), verdict('low-confidence', 'second'));
    expect(p.classify(sample, null).filter).toBe('first');
  });
});
