// App.tsx — REVYR-Dev A0 Recording-App.
//
// Screens: home / sport-select / recording / detail.
// Wire-up: DB-Bootstrap + ActivitySessionService + RecordingCoordinator + AppStateBridge.
// Kein Routing, Backend, Social, Territory. Kein produktives Design.

import { StatusBar } from 'expo-status-bar';
import { useCallback, useEffect, useState } from 'react';
import { Pressable, StyleSheet, Text, View } from 'react-native';

import { DB_NAME } from './src/config/database';
import { openExpoDatabase } from './src/db/expo-adapter';
import {
  collectRecovery,
  initializeDatabase,
  type BootstrapReport,
  type RecoveryReport,
} from './src/db/bootstrap';
import { listFinalizedActivities, type Activity, type Sport } from './src/db/activity-repo';
import { ActivitySessionService } from './src/services/activity-session';
import { RecordingCoordinator } from './src/services/recording-coordinator';
import { everyNSamples } from './src/services/chunk-boundary-policy';
import {
  accuracyFilter,
  jumpFilter,
  pipeline,
  speedFilter,
  stalenessFilter,
} from './src/services/quality';
import { AppStateBridge } from './src/services/app-state-bridge';
import { createRnAppStateSource } from './src/services/rn-app-state-source';
import { createExpoLocationPort } from './src/location/expo-location-adapter';

import { HomeScreen } from './src/ui/screens/HomeScreen';
import { SportSelectScreen } from './src/ui/screens/SportSelectScreen';
import { RecordingScreen } from './src/ui/screens/RecordingScreen';
import { DetailScreen } from './src/ui/screens/DetailScreen';
import { DiagnosticsScreen } from './src/ui/screens/DiagnosticsScreen';
import { ErrorBoundary } from './src/ui/ErrorBoundary';
import { humanErrorMessage } from './src/ui/format';

// Dev-Policy — ausdruecklich KEIN Produkt-Default (G5 offen).
const DEV_POLICY = everyNSamples(20);

// Dev-Quality-Pipeline — Schwellen nicht kalibriert. Kalibrierung ist A0.1.
function makeDevPipeline(): ReturnType<typeof pipeline> {
  return pipeline(
    accuracyFilter({ acceptedBelowM: 20, rejectAboveM: 100 }),
    stalenessFilter({ maxAgeMs: 30_000, nowMs: () => Date.now() }),
    speedFilter({ rejectAboveMps: 25 }),
    jumpFilter({ rejectAboveM: 500, rejectAboveMps: 25 }),
  );
}

type Screen =
  | { kind: 'home' }
  | { kind: 'sport-select' }
  | { kind: 'recording'; sport: Sport }
  | { kind: 'diagnostics'; sport: Sport }
  | { kind: 'detail'; activityId: number };

export default function App(): React.JSX.Element {
  const [boot, setBoot] = useState<BootstrapReport | null>(null);
  const [sessionSvc, setSessionSvc] = useState<ActivitySessionService | null>(null);
  const [coord, setCoord] = useState<RecordingCoordinator | null>(null);
  const [bridge, setBridge] = useState<AppStateBridge | null>(null);
  const [screen, setScreen] = useState<Screen>({ kind: 'home' });
  const [recovery, setRecovery] = useState<readonly RecoveryReport[]>([]);
  const [finalized, setFinalized] = useState<readonly Activity[]>([]);
  const [error, setError] = useState<string | null>(null);

  // Bootstrap einmal beim App-Start.
  useEffect(() => {
    try {
      const b = initializeDatabase({
        openDatabase: () => openExpoDatabase(DB_NAME),
      });
      setBoot(b);
      setSessionSvc(new ActivitySessionService(b.db));
      setRecovery(b.recovery);
      setFinalized(listFinalizedActivities(b.db));
    } catch (e) {
      setError(humanErrorMessage(e));
    }
  }, []);

  const refreshLists = useCallback((): void => {
    if (boot === null) return;
    setRecovery(collectRecovery(boot.db));
    setFinalized(listFinalizedActivities(boot.db));
  }, [boot]);

  const teardownRecording = useCallback((): void => {
    if (bridge !== null) bridge.detach();
    if (coord !== null) coord.dispose();
    setBridge(null);
    setCoord(null);
  }, [bridge, coord]);

  const createRecordingContext = useCallback((): RecordingCoordinator | null => {
    if (sessionSvc === null) return null;
    const c = new RecordingCoordinator({
      session: sessionSvc,
      location: createExpoLocationPort(),
      policy: DEV_POLICY,
      qualityPipeline: makeDevPipeline(),
    });
    const b = new AppStateBridge({
      coordinator: c,
      source: createRnAppStateSource(),
      onEvent: (msg) => console.log(`[AppState] ${msg}`),
    });
    b.attach();
    setCoord(c);
    setBridge(b);
    return c;
  }, [sessionSvc]);

  const onNewActivity = (): void => {
    setError(null);
    setScreen({ kind: 'sport-select' });
  };

  const onSportSelected = async (sport: Sport): Promise<void> => {
    const c = createRecordingContext();
    if (c === null) {
      setError('Interner Fehler: Services nicht initialisiert.');
      return;
    }
    try {
      await c.start(sport);
      setScreen({ kind: 'recording', sport });
    } catch (e) {
      teardownRecording();
      setError(humanErrorMessage(e));
      setScreen({ kind: 'home' });
    }
  };

  const onResumeRecovery = async (
    rec: RecoveryReport,
    acknowledgeGaps: boolean,
  ): Promise<void> => {
    if (sessionSvc === null) {
      setError('Interner Fehler: Services nicht initialisiert.');
      return;
    }
    try {
      const session = sessionSvc.resume(rec.activity.id, { acknowledgeGaps });
      const c = createRecordingContext();
      if (c === null) return;
      await c.resumeFrom(session);
      setScreen({ kind: 'recording', sport: rec.activity.sport });
    } catch (e) {
      teardownRecording();
      setError(humanErrorMessage(e));
    }
  };

  const onRecordingStopped = (): void => {
    teardownRecording();
    refreshLists();
    setScreen({ kind: 'home' });
  };

  const onRecordingError = (msg: string): void => {
    setError(msg);
  };

  const onOpenDetail = (activityId: number): void => {
    setError(null);
    setScreen({ kind: 'detail', activityId });
  };

  const onBackToHome = (): void => {
    setError(null);
    refreshLists();
    setScreen({ kind: 'home' });
  };

  // Fehler wird oben ueber allen Screens gezeigt.
  const errorBanner = error !== null ? (
    <View style={styles.error}>
      <Text style={styles.errorText}>{error}</Text>
      <Pressable onPress={(): void => setError(null)}>
        <Text style={styles.errorDismiss}>schliessen</Text>
      </Pressable>
    </View>
  ) : null;

  if (boot === null) {
    return (
      <View style={styles.center}>
        <StatusBar style="auto" />
        {errorBanner}
        <Text>Initialisiere…</Text>
      </View>
    );
  }

  const onOpenDiagnostics = (sport: Sport): void => {
    setScreen({ kind: 'diagnostics', sport });
  };
  const onBackToRecording = (sport: Sport): void => {
    setScreen({ kind: 'recording', sport });
  };

  return (
    <ErrorBoundary onError={(e): void => setError(humanErrorMessage(e))}>
      <View style={styles.root}>
        <StatusBar style="auto" />
        {errorBanner}
        {screen.kind === 'home' && (
          <HomeScreen
            recovery={recovery}
            finalized={finalized}
            onNewActivity={onNewActivity}
            onResume={onResumeRecovery}
            onOpenDetail={onOpenDetail}
          />
        )}
        {screen.kind === 'sport-select' && (
          <SportSelectScreen
            onSelect={onSportSelected}
            onBack={onBackToHome}
          />
        )}
        {screen.kind === 'recording' && coord !== null && (
          <RecordingScreen
            sport={screen.sport}
            coordinator={coord}
            onStop={onRecordingStopped}
            onError={onRecordingError}
            onOpenDiagnostics={(): void => onOpenDiagnostics(screen.sport)}
          />
        )}
        {screen.kind === 'diagnostics' && (
          <DiagnosticsScreen
            coordinator={coord}
            onBack={(): void => onBackToRecording(screen.sport)}
          />
        )}
        {screen.kind === 'detail' && (
          <DetailScreen
            db={boot.db}
            activityId={screen.activityId}
            onBack={onBackToHome}
          />
        )}
      </View>
    </ErrorBoundary>
  );
}

const styles = StyleSheet.create({
  root: { flex: 1, backgroundColor: '#fff' },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center', backgroundColor: '#fff' },
  error: {
    backgroundColor: '#a33',
    paddingHorizontal: 16,
    paddingVertical: 12,
    paddingTop: 50,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  errorText: { color: '#fff', flex: 1, marginRight: 12 },
  errorDismiss: { color: '#fff', fontWeight: '600' },
});
