// mobile/src/services/__tests__/app-state-bridge.test.ts
import { openTestDatabase } from '../../db/test-adapter';
import { migrateToLatest } from '../../db/migrations';
import { ActivitySessionService } from '../activity-session';
import { RecordingCoordinator } from '../recording-coordinator';
import { everyNSamples } from '../chunk-boundary-policy';
import { createFakeLocationPort } from '../../location/fake-location-port';
import { AppStateBridge } from '../app-state-bridge';
import { createFakeAppStateSource } from '../fake-app-state-source';

const NOW = (): string => '2026-07-20T15:00:00Z';

function setup() {
  const db = openTestDatabase();
  migrateToLatest(db, NOW);
  const location = createFakeLocationPort();
  const coord = new RecordingCoordinator({
    session: new ActivitySessionService(db, NOW),
    location,
    policy: everyNSamples(1000),
  });
  const source = createFakeAppStateSource();
  const events: string[] = [];
  const bridge = new AppStateBridge({
    coordinator: coord,
    source,
    onEvent: (msg) => events.push(msg),
  });
  return { db, coord, location, source, bridge, events };
}

describe('AppStateBridge', () => {
  test('attach registriert Listener; detach entfernt ihn', () => {
    const { db, coord, source, bridge } = setup();
    expect(bridge.isAttached()).toBe(false);
    expect(source.listenerCount()).toBe(0);
    bridge.attach();
    expect(bridge.isAttached()).toBe(true);
    expect(source.listenerCount()).toBe(1);
    bridge.detach();
    expect(bridge.isAttached()).toBe(false);
    expect(source.listenerCount()).toBe(0);
    coord.dispose();
    db.closeSync();
  });

  test('doppelter attach ist Idempotent (kein Zweit-Listener)', () => {
    const { db, coord, source, bridge } = setup();
    bridge.attach();
    bridge.attach();
    expect(source.listenerCount()).toBe(1);
    bridge.detach();
    coord.dispose();
    db.closeSync();
  });

  test('background waehrend recording -> pause() wird ausgeloest', async () => {
    const { db, coord, location, source, bridge, events } = setup();
    bridge.attach();
    await coord.start('run');
    expect(coord.status().state).toBe('recording');
    expect(location.activeSubscriptions()).toBe(1);
    source.set('background');
    // pause() ist async — kurz warten
    await new Promise((r) => setTimeout(r, 10));
    expect(coord.status().state).toBe('paused');
    expect(location.activeSubscriptions()).toBe(0);
    expect(events.some((e) => e.includes('pause()'))).toBe(true);
    await coord.finalize();
    bridge.detach();
    coord.dispose();
    db.closeSync();
  });

  test('background waehrend idle -> Log, aber keine Aktion', () => {
    const { db, coord, source, bridge, events } = setup();
    bridge.attach();
    source.set('background');
    expect(events.some((e) => e.includes('keine Aktion'))).toBe(true);
    bridge.detach();
    coord.dispose();
    db.closeSync();
  });

  test('active nach background -> nur Log, kein Auto-Resume', async () => {
    const { db, coord, location, source, bridge, events } = setup();
    bridge.attach();
    await coord.start('run');
    source.set('background');
    await new Promise((r) => setTimeout(r, 10));
    expect(coord.status().state).toBe('paused');
    events.length = 0; // Log leeren
    source.set('active');
    expect(coord.status().state).toBe('paused'); // KEIN Auto-Resume
    expect(location.activeSubscriptions()).toBe(0);
    expect(events.some((e) => e.includes('Nutzer muss Resume'))).toBe(true);
    await coord.resume();
    await coord.finalize();
    bridge.detach();
    coord.dispose();
    db.closeSync();
  });

  test('inactive -> keine Aktion und kein Log', () => {
    const { db, coord, source, bridge, events } = setup();
    bridge.attach();
    source.set('inactive');
    expect(events).toEqual([]);
    bridge.detach();
    coord.dispose();
    db.closeSync();
  });
});
