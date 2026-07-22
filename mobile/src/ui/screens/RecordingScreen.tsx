// mobile/src/ui/screens/RecordingScreen.tsx
//
// Der Live-Aufzeichnungsschirm. Zeigt Dauer, Distanz, Pace/Speed, GPS-Status,
// steuert Pause/Resume/Stop. Fehlerzustaende sind menschlich formuliert.

import { useEffect, useState } from 'react';
import { Pressable, StyleSheet, Text, View } from 'react-native';
import type { Sport } from '../../db/activity-repo';
import type { RecordingCoordinator, RecordingStatus } from '../../services/recording-coordinator';
import {
  formatDistance,
  formatDurationMs,
  formatGpsStatus,
  formatPace,
  formatSpeed,
  humanErrorMessage,
} from '../format';

export interface RecordingScreenProps {
  sport: Sport;
  coordinator: RecordingCoordinator;
  onStop(): void;
  onError(msg: string): void;
  onOpenDiagnostics?(): void;
}

export function RecordingScreen(props: RecordingScreenProps): React.JSX.Element {
  const [status, setStatus] = useState<RecordingStatus>(() =>
    props.coordinator.status(),
  );

  useEffect(() => {
    const id = setInterval(() => {
      setStatus(props.coordinator.status());
    }, 500);
    return (): void => clearInterval(id);
  }, [props.coordinator]);

  // Aktivzeit (Pausen + Background NICHT enthalten) — Coordinator berechnet.
  const activeDurationMs: number = status.activeMs;

  const speedMps = status.latestSample?.speedMps ?? null;
  const perfDisplay = props.sport === 'run' ? formatPace(speedMps) : formatSpeed(speedMps);

  const onPause = (): void => {
    props.coordinator.pause().catch((e: Error) =>
      props.onError(humanErrorMessage(e)),
    );
  };
  const onResume = (): void => {
    props.coordinator.resume().catch((e: Error) =>
      props.onError(humanErrorMessage(e)),
    );
  };
  const onStop = (): void => {
    props.coordinator.finalize().then(
      () => props.onStop(),
      (e: Error) => props.onError(humanErrorMessage(e)),
    );
  };

  const canPause = status.state === 'recording';
  const canResume = status.state === 'paused';
  const canStop = status.state === 'recording' || status.state === 'paused';

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <View style={{ flex: 1 }}>
          <Text style={styles.sport}>
            {props.sport === 'run' ? 'Lauf' : 'Radfahrt'}
            {status.session !== null ? ` · #${status.session.activityId}` : ''}
          </Text>
          <Text style={styles.state}>Zustand: {germanState(status.state)}</Text>
        </View>
        {props.onOpenDiagnostics !== undefined && (
          <Pressable style={styles.diagButton} onPress={props.onOpenDiagnostics}>
            <Text style={styles.diagButtonText}>Diagnostics</Text>
          </Pressable>
        )}
      </View>

      <View style={styles.big}>
        <Text style={styles.bigLabel}>Aktive Dauer</Text>
        <Text style={styles.bigValue}>{formatDurationMs(activeDurationMs)}</Text>
        <Text style={styles.bigHint}>Pausen und Background zaehlen nicht.</Text>
      </View>

      <View style={styles.big}>
        <Text style={styles.bigLabel}>Distanz</Text>
        <Text style={styles.bigValue}>{formatDistance(status.totalDistanceM)}</Text>
      </View>

      <View style={styles.big}>
        <Text style={styles.bigLabel}>
          {props.sport === 'run' ? 'Pace' : 'Geschwindigkeit'}
        </Text>
        <Text style={styles.bigValue}>{perfDisplay}</Text>
      </View>

      <View style={styles.meta}>
        <Text style={styles.metaLine}>
          GPS: {formatGpsStatus(status.latestSample?.accuracyMeters ?? null,
                               status.lastVerdict?.quality ?? null)}
        </Text>
        <Text style={styles.metaLine}>
          Samples: {status.samplesAccepted} akzeptiert · {status.samplesDropped} verworfen
        </Text>
        <Text style={styles.metaLine}>
          Chunks geschrieben: {status.chunksWritten} · Puffer: {status.bufferSize}
        </Text>
        {status.lastVerdict !== null && status.lastVerdict.quality !== 'accepted' && (
          <Text style={styles.metaWarn}>
            Filter: {status.lastVerdict.filter} — {status.lastVerdict.reason}
          </Text>
        )}
      </View>

      <View style={styles.buttonRow}>
        {canPause && (
          <Pressable style={[styles.btn, styles.btnPause]} onPress={onPause}>
            <Text style={styles.btnText}>Pause</Text>
          </Pressable>
        )}
        {canResume && (
          <Pressable style={[styles.btn, styles.btnResume]} onPress={onResume}>
            <Text style={styles.btnText}>Fortsetzen</Text>
          </Pressable>
        )}
        {canStop && (
          <Pressable style={[styles.btn, styles.btnStop]} onPress={onStop}>
            <Text style={styles.btnText}>Stopp</Text>
          </Pressable>
        )}
      </View>
    </View>
  );
}

function germanState(s: RecordingStatus['state']): string {
  switch (s) {
    case 'idle': return 'bereit';
    case 'recording': return 'laeuft';
    case 'paused': return 'pausiert';
    case 'finalized': return 'abgeschlossen';
  }
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, paddingTop: 60, backgroundColor: '#fff' },
  header: { flexDirection: 'row', alignItems: 'center', marginBottom: 20 },
  sport: { fontSize: 20, fontWeight: '700', marginBottom: 2 },
  state: { fontSize: 12, color: '#666' },
  diagButton: {
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderWidth: 1,
    borderColor: '#333',
    borderRadius: 6,
  },
  diagButtonText: { fontSize: 12, color: '#333' },
  big: { marginBottom: 16 },
  bigLabel: { fontSize: 12, color: '#666', textTransform: 'uppercase' },
  bigValue: { fontSize: 42, fontWeight: '600', fontVariant: ['tabular-nums'] },
  bigHint: { fontSize: 11, color: '#888', marginTop: 2 },
  meta: {
    marginTop: 12,
    padding: 12,
    backgroundColor: '#f4f4f4',
    borderRadius: 8,
  },
  metaLine: { fontSize: 12, color: '#333', marginVertical: 2 },
  metaWarn: { fontSize: 12, color: '#a33', marginTop: 4 },
  buttonRow: { flexDirection: 'row', gap: 12, marginTop: 24, flexWrap: 'wrap' },
  btn: { paddingHorizontal: 20, paddingVertical: 14, borderRadius: 8 },
  btnPause: { backgroundColor: '#666' },
  btnResume: { backgroundColor: '#2a7' },
  btnStop: { backgroundColor: '#a33' },
  btnText: { color: '#fff', fontSize: 15, fontWeight: '600' },
});
