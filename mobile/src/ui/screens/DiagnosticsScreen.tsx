// mobile/src/ui/screens/DiagnosticsScreen.tsx
//
// Diagnostics/Calibration-Ansicht: live Rohsample, Filter-Verdikt, Accuracy,
// Speed, Reject-Grund. NUR fuer Kalibrierung — KEIN produktives Feature-UI.
//
// Legt selbst KEINE Schwellen fest. Zeigt die aktuell konfigurierte Pipeline
// und deren Verdikte. Der Nutzer beobachtet, notiert und entscheidet spaeter.

import { useEffect, useState } from 'react';
import { Pressable, ScrollView, StyleSheet, Text, View } from 'react-native';
import type { RecordingCoordinator, RecordingStatus } from '../../services/recording-coordinator';
import type { LocationSample } from '../../location/ports';
import type { FilterVerdict } from '../../services/quality/pipeline';
import { formatDistance, formatSpeed, isFiniteNumber } from '../format';

export interface DiagnosticsScreenProps {
  coordinator: RecordingCoordinator | null;
  onBack(): void;
}

// Kleiner Ring-Buffer fuer die letzten N Verdicts, damit man Muster sieht.
const HISTORY_SIZE = 12;

export function DiagnosticsScreen(props: DiagnosticsScreenProps): React.JSX.Element {
  const [status, setStatus] = useState<RecordingStatus | null>(
    () => props.coordinator?.status() ?? null,
  );
  const [history, setHistory] = useState<
    ReadonlyArray<{ ts: number; sample: LocationSample | null; verdict: FilterVerdict | null }>
  >([]);

  useEffect(() => {
    if (props.coordinator === null) return;
    const id = setInterval(() => {
      const s = props.coordinator!.status();
      setStatus(s);
      setHistory((prev) => {
        // Nur bei neuem Sample eintragen (Zeitstempel-Vergleich).
        const lastTs = prev[0]?.sample?.timestampMs ?? -1;
        const curTs = s.latestSample?.timestampMs ?? -1;
        if (curTs === lastTs) return prev;
        return [
          { ts: Date.now(), sample: s.latestSample, verdict: s.lastVerdict },
          ...prev,
        ].slice(0, HISTORY_SIZE);
      });
    }, 250);
    return (): void => clearInterval(id);
  }, [props.coordinator]);

  if (props.coordinator === null || status === null) {
    return (
      <ScrollView contentContainerStyle={styles.container}>
        <Pressable onPress={props.onBack} style={styles.back}>
          <Text style={styles.backText}>← zurueck</Text>
        </Pressable>
        <Text style={styles.title}>Diagnostics</Text>
        <Text style={styles.empty}>
          Keine aktive Aufzeichnung — starte eine, um live Samples zu sehen.
        </Text>
      </ScrollView>
    );
  }

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Pressable onPress={props.onBack} style={styles.back}>
        <Text style={styles.backText}>← zurueck</Text>
      </Pressable>
      <Text style={styles.title}>Diagnostics</Text>
      <Text style={styles.subtitle}>
        Live-Rohdaten + Pipeline-Verdikte. Keine Schwellen werden hier
        festgelegt — Kalibrierung erfolgt getrennt (A0.1).
      </Text>

      <Section title="Pipeline">
        <KV label="Policy" value={status.policyName} />
        <KV
          label="Filter aktiv"
          value={status.lastVerdict !== null ? 'ja' : 'nein (raw)'}
        />
      </Section>

      <Section title="Letzter Sample">
        {status.latestSample === null ? (
          <Text style={styles.hint}>—</Text>
        ) : (
          <>
            <KV
              label="Lat / Lng"
              value={`${status.latestSample.latitude.toFixed(6)}, ${status.latestSample.longitude.toFixed(6)}`}
            />
            <KV
              label="timestamp"
              value={new Date(status.latestSample.timestampMs).toISOString()}
            />
            <KV
              label="accuracy"
              value={
                isFiniteNumber(status.latestSample.accuracyMeters)
                  ? `${status.latestSample.accuracyMeters.toFixed(1)} m`
                  : '—'
              }
            />
            <KV label="altitude" value={fmtOrDash(status.latestSample.altitudeMeters, 1, ' m')} />
            <KV label="speed" value={formatSpeed(status.latestSample.speedMps)} />
            <KV
              label="heading"
              value={
                isFiniteNumber(status.latestSample.headingDegrees)
                  ? `${status.latestSample.headingDegrees.toFixed(0)}°`
                  : '—'
              }
            />
            <KV
              label="isMocked"
              value={String(status.latestSample.isMocked)}
            />
          </>
        )}
      </Section>

      <Section title="Letzter Filter-Verdikt">
        {status.lastVerdict === null ? (
          <Text style={styles.hint}>keine Pipeline aktiv</Text>
        ) : (
          <>
            <KV label="quality" value={status.lastVerdict.quality} />
            <KV label="filter" value={status.lastVerdict.filter} />
            <KV label="reason" value={status.lastVerdict.reason} />
          </>
        )}
      </Section>

      <Section title="Session-Kennzahlen">
        <KV label="samples akzeptiert" value={String(status.samplesAccepted)} />
        <KV label="samples verworfen" value={String(status.samplesDropped)} />
        <KV label="chunks geschrieben" value={String(status.chunksWritten)} />
        <KV label="puffer" value={String(status.bufferSize)} />
        <KV label="totalDistance" value={formatDistance(status.totalDistanceM)} />
        <KV label="lastFlushReason" value={status.lastFlushReason ?? '—'} />
      </Section>

      <Section title={`Verdikt-Historie (letzte ${HISTORY_SIZE})`}>
        {history.length === 0 ? (
          <Text style={styles.hint}>noch keine Samples eingetroffen</Text>
        ) : (
          history.map((h, i) => (
            <View key={i} style={styles.historyRow}>
              <Text style={styles.historyTime}>
                {new Date(h.ts).toLocaleTimeString('de-DE')}
              </Text>
              <Text
                style={[styles.historyQuality, qualityStyle(h.verdict?.quality)]}
              >
                {h.verdict?.quality ?? 'raw'}
              </Text>
              <Text style={styles.historyReason}>
                {h.verdict?.reason ?? '—'}
              </Text>
            </View>
          ))
        )}
      </Section>
    </ScrollView>
  );
}

function fmtOrDash(
  v: number | null | undefined,
  decimals: number,
  unit: string,
): string {
  if (!isFiniteNumber(v)) return '—';
  return `${v.toFixed(decimals)}${unit}`;
}

function qualityStyle(
  q: string | undefined,
): { color: string } {
  switch (q) {
    case 'accepted': return { color: '#2a7' };
    case 'low-confidence': return { color: '#c80' };
    case 'rejected': return { color: '#a33' };
    default: return { color: '#666' };
  }
}

function Section(props: { title: string; children: React.ReactNode }): React.JSX.Element {
  return (
    <View style={styles.section}>
      <Text style={styles.sectionTitle}>{props.title}</Text>
      {props.children}
    </View>
  );
}

function KV(props: { label: string; value: string }): React.JSX.Element {
  return (
    <View style={styles.kv}>
      <Text style={styles.kvLabel}>{props.label}</Text>
      <Text style={styles.kvValue}>{props.value}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 16, paddingTop: 60, backgroundColor: '#fff' },
  back: { marginBottom: 12 },
  backText: { fontSize: 14, color: '#333' },
  title: { fontSize: 22, fontWeight: '700', marginBottom: 4 },
  subtitle: { fontSize: 12, color: '#666', marginBottom: 16 },
  empty: { color: '#888', fontStyle: 'italic' },
  hint: { color: '#888', fontSize: 12 },
  section: {
    marginBottom: 16,
    padding: 12,
    backgroundColor: '#f4f4f4',
    borderRadius: 8,
  },
  sectionTitle: { fontSize: 13, fontWeight: '700', marginBottom: 8, color: '#333' },
  kv: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 3,
  },
  kvLabel: { fontSize: 12, color: '#555' },
  kvValue: { fontSize: 12, color: '#111', fontFamily: 'Courier' },
  historyRow: {
    flexDirection: 'row',
    gap: 8,
    paddingVertical: 4,
    borderBottomWidth: 1,
    borderBottomColor: '#e8e8e8',
  },
  historyTime: { fontSize: 11, color: '#666', fontFamily: 'Courier', width: 90 },
  historyQuality: { fontSize: 11, fontWeight: '700', width: 100 },
  historyReason: { fontSize: 11, color: '#555', flex: 1 },
});
