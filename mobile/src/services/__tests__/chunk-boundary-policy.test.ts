// mobile/src/services/__tests__/chunk-boundary-policy.test.ts
import {
  everyMs,
  everyNSamples,
  samplesOrMs,
} from '../chunk-boundary-policy';

describe('everyNSamples', () => {
  test('flusht, wenn bufferSize >= n', () => {
    const p = everyNSamples(3);
    expect(p.shouldFlush(0, 0).shouldFlush).toBe(false);
    expect(p.shouldFlush(2, 0).shouldFlush).toBe(false);
    expect(p.shouldFlush(3, 0).shouldFlush).toBe(true);
    expect(p.shouldFlush(4, 0).shouldFlush).toBe(true);
  });

  test('name enthaelt Parameter', () => {
    expect(everyNSamples(7).name).toBe('everyNSamples(7)');
  });

  test('reason ist nachvollziehbar', () => {
    expect(everyNSamples(3).shouldFlush(3, 0).reason).toContain('>= 3');
  });

  test('wirft bei n <= 0', () => {
    expect(() => everyNSamples(0)).toThrow();
    expect(() => everyNSamples(-1)).toThrow();
  });
});

describe('everyMs', () => {
  test('flusht, wenn msSinceLastFlush >= ms', () => {
    const p = everyMs(1000);
    expect(p.shouldFlush(0, 0).shouldFlush).toBe(false);
    expect(p.shouldFlush(999, 999).shouldFlush).toBe(false);
    expect(p.shouldFlush(0, 1000).shouldFlush).toBe(true);
    expect(p.shouldFlush(0, 1500).shouldFlush).toBe(true);
  });

  test('wirft bei ms <= 0', () => {
    expect(() => everyMs(0)).toThrow();
  });
});

describe('samplesOrMs', () => {
  test('flusht, wenn EINE Bedingung erfuellt ist', () => {
    const p = samplesOrMs(10, 5000);
    expect(p.shouldFlush(0, 0).shouldFlush).toBe(false);
    expect(p.shouldFlush(10, 0).shouldFlush).toBe(true); // samples-Grenze
    expect(p.shouldFlush(0, 5000).shouldFlush).toBe(true); // time-Grenze
  });

  test('reason nennt die ausloesende Grenze', () => {
    const p = samplesOrMs(10, 5000);
    expect(p.shouldFlush(10, 0).reason).toMatch(/samples/);
    expect(p.shouldFlush(0, 5000).reason).toMatch(/time/);
    expect(p.shouldFlush(2, 200).reason).toMatch(/unter Schwelle/);
  });
});
