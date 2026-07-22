// mobile/src/ui/__tests__/DiagnosticsScreen.test.tsx
import React from 'react';
import TestRenderer from 'react-test-renderer';
import { DiagnosticsScreen } from '../screens/DiagnosticsScreen';
import type { RecordingStatus } from '../../services/recording-coordinator';

// Wir mocken den Coordinator komplett — DiagnosticsScreen kennt nur die
// status()-Methode. Kein DB, keine Subscription, kein Timer im Test noetig.
function makeStubCoordinator(status: Partial<RecordingStatus> = {}) {
  const full: RecordingStatus = {
    state: 'recording',
    session: { activityId: 1, sport: 'run', startedAt: '2026-07-20T15:00:00Z', nextChunkId: 0, finalized: false },
    bufferSize: 0,
    chunksWritten: 0,
    samplesAccepted: 0,
    samplesDropped: 0,
    lastFlushReason: null,
    policyName: 'everyNSamples(5)',
    totalDistanceM: 0,
    latestSample: null,
    lastVerdict: null,
    activeMs: 0,
    ...status,
  };
  return {
    status: (): RecordingStatus => full,
    // Wir simulieren die Coordinator-Klasse; DiagnosticsScreen ruft nur status().
  } as unknown as import('../../services/recording-coordinator').RecordingCoordinator;
}

describe('DiagnosticsScreen', () => {
  test('zeigt Leerzustand, wenn kein Coordinator uebergeben', () => {
    const tree = TestRenderer.create(
      <DiagnosticsScreen coordinator={null} onBack={(): void => undefined} />,
    );
    const rendered = JSON.stringify(tree.toJSON());
    expect(rendered).toContain('Keine aktive Aufzeichnung');
    tree.unmount();
  });

  test('zeigt Policy-Name und Session-Kennzahlen aus dem Coordinator', () => {
    const coord = makeStubCoordinator({
      policyName: 'everyNSamples(20)',
      samplesAccepted: 42,
      samplesDropped: 3,
      chunksWritten: 5,
      bufferSize: 7,
      totalDistanceM: 1234,
    });
    const tree = TestRenderer.create(
      <DiagnosticsScreen coordinator={coord} onBack={(): void => undefined} />,
    );
    const rendered = JSON.stringify(tree.toJSON());
    expect(rendered).toContain('everyNSamples(20)');
    expect(rendered).toContain('42'); // samples accepted
    expect(rendered).toContain('3');  // samples dropped
    expect(rendered).toContain('5');  // chunks
    expect(rendered).toContain('7');  // buffer
    expect(rendered).toContain('1.23 km'); // 1234 m
    tree.unmount();
  });

  test('zeigt latest Sample mit Rohwerten', () => {
    const coord = makeStubCoordinator({
      latestSample: {
        latitude: 52.5163,
        longitude: 13.3777,
        timestampMs: Date.parse('2026-07-20T15:00:00Z'),
        accuracyMeters: 4.2,
        altitudeMeters: 120.5,
        speedMps: 3.1,
        headingDegrees: 90,
        isMocked: false,
      },
    });
    const tree = TestRenderer.create(
      <DiagnosticsScreen coordinator={coord} onBack={(): void => undefined} />,
    );
    const rendered = JSON.stringify(tree.toJSON());
    expect(rendered).toContain('52.516300');
    expect(rendered).toContain('13.377700');
    expect(rendered).toContain('4.2 m');
    expect(rendered).toContain('120.5 m');
    tree.unmount();
  });

  test('zeigt Filter-Verdikt mit Grund', () => {
    const coord = makeStubCoordinator({
      lastVerdict: {
        quality: 'rejected',
        filter: 'accuracy(acc<20m,rej>100m)',
        reason: 'accuracy 200.0m > 100m',
      },
    });
    const tree = TestRenderer.create(
      <DiagnosticsScreen coordinator={coord} onBack={(): void => undefined} />,
    );
    const rendered = JSON.stringify(tree.toJSON());
    expect(rendered).toContain('rejected');
    expect(rendered).toContain('accuracy(acc<20m,rej>100m)');
    expect(rendered).toContain('accuracy 200.0m > 100m');
    tree.unmount();
  });

  test('onBack wird ausgeloest', () => {
    const onBack = jest.fn();
    const coord = makeStubCoordinator();
    const tree = TestRenderer.create(
      <DiagnosticsScreen coordinator={coord} onBack={onBack} />,
    );
    const backPressables = tree.root.findAll(
      (n) => typeof (n.props as { onPress?: unknown }).onPress === 'function',
    );
    // Das erste Pressable ist der zurueck-Knopf.
    expect(backPressables.length).toBeGreaterThan(0);
    backPressables[0].props.onPress();
    expect(onBack).toHaveBeenCalled();
    tree.unmount();
  });
});
