// mobile/src/ui/screens/DetailScreen.tsx
import { useEffect, useState } from 'react';
import { Pressable, ScrollView, StyleSheet, Text, View } from 'react-native';
import { getActivity, type Activity } from '../../db/activity-repo';
import { readChunks, type Chunk } from '../../db/chunk-repo';
import { closedActiveMs, listSegments, type Segment } from '../../db/segment-repo';
import type { SQLiteBinding } from '../../db/ports';
import { deserializePoints } from '../../domain/track-point';
import { haversineDistanceM } from '../../services/quality/geo';
import { formatDistance, formatDurationMs } from '../format';

export interface DetailScreenProps {
  db: SQLiteBinding;
  activityId: number;
  onBack(): void;
}

interface DetailData {
  activity: Activity | null;
  chunks: readonly Chunk[];
  segments: readonly Segment[];
  totalPoints: number;
  totalDistanceM: number;
  activeMs: number;
}

function loadDetail(db: SQLiteBinding, activityId: number): DetailData {
  const activity = getActivity(db, activityId);
  const chunks = readChunks(db, activityId);
  const segments = listSegments(db, activityId);
  let totalPoints = 0;
  let totalDistanceM = 0;
  let last: { latitude: number; longitude: number } | null = null;
  for (const c of chunks) {
    totalPoints += c.pointsCount;
    for (const p of deserializePoints(c.pointsJson)) {
      if (last !== null) {
        totalDistanceM += haversineDistanceM(last, p);
      }
      last = p;
    }
  }
  return {
    activity,
    chunks,
    segments,
    totalPoints,
    totalDistanceM,
    activeMs: closedActiveMs(db, activityId),
  };
}

export function DetailScreen(props: DetailScreenProps): React.JSX.Element {
  const [data, setData] = useState<DetailData | null>(null);

  useEffect(() => {
    setData(loadDetail(props.db, props.activityId));
  }, [props.db, props.activityId]);

  if (data === null) {
    return (
      <View style={styles.container}>
        <Text>Laedt…</Text>
      </View>
    );
  }

  if (data.activity === null) {
    return (
      <View style={styles.container}>
        <Pressable onPress={props.onBack} style={styles.back}>
          <Text style={styles.backText}>← zurueck</Text>
        </Pressable>
        <Text style={styles.title}>Aktivitaet nicht gefunden</Text>
      </View>
    );
  }

  const a = data.activity;
  const startedMs = Date.parse(a.startedAt);
  const finalizedMs = a.finalizedAt !== null ? Date.parse(a.finalizedAt) : null;
  const totalDurationMs = finalizedMs !== null && Number.isFinite(startedMs)
    ? finalizedMs - startedMs
    : null;

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Pressable onPress={props.onBack} style={styles.back}>
        <Text style={styles.backText}>← zurueck</Text>
      </Pressable>
      <Text style={styles.title}>
        {a.sport === 'run' ? 'Lauf' : 'Radfahrt'} #{a.id}
      </Text>
      <Text style={styles.meta}>Start: {a.startedAt}</Text>
      <Text style={styles.meta}>
        Ende: {a.finalizedAt ?? '— (unfinalisiert)'}
      </Text>

      <View style={styles.metricRow}>
        <Metric label="Aktive Dauer" value={formatDurationMs(data.activeMs)} />
        <Metric label="Distanz" value={formatDistance(data.totalDistanceM)} />
      </View>
      <View style={styles.metricRow}>
        <Metric label="Gesamtzeit" value={formatDurationMs(totalDurationMs)} />
        <Metric label="Segmente" value={String(data.segments.length)} />
      </View>
      <View style={styles.metricRow}>
        <Metric label="Chunks" value={String(data.chunks.length)} />
        <Metric label="Punkte" value={String(data.totalPoints)} />
      </View>

      <Text style={styles.sectionTitle}>Chunks</Text>
      {data.chunks.length === 0 ? (
        <Text style={styles.empty}>Keine Chunks — Aktivitaet ohne Samples.</Text>
      ) : (
        data.chunks.map((c) => (
          <View key={c.chunkId} style={styles.chunkRow}>
            <Text style={styles.chunkPrimary}>Chunk #{c.chunkId}</Text>
            <Text style={styles.chunkSecondary}>{c.pointsCount} Punkte</Text>
          </View>
        ))
      )}
    </ScrollView>
  );
}

function Metric(props: { label: string; value: string }): React.JSX.Element {
  return (
    <View style={styles.metric}>
      <Text style={styles.metricLabel}>{props.label}</Text>
      <Text style={styles.metricValue}>{props.value}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 16, paddingTop: 60, backgroundColor: '#fff' },
  back: { marginBottom: 12 },
  backText: { fontSize: 14, color: '#333' },
  title: { fontSize: 22, fontWeight: '700', marginBottom: 6 },
  meta: { fontSize: 12, color: '#555', marginBottom: 2 },
  metricRow: { flexDirection: 'row', gap: 12, marginTop: 12 },
  metric: {
    flex: 1,
    padding: 12,
    backgroundColor: '#f4f4f4',
    borderRadius: 8,
  },
  metricLabel: { fontSize: 11, color: '#666', textTransform: 'uppercase' },
  metricValue: { fontSize: 24, fontWeight: '600', fontVariant: ['tabular-nums'] },
  sectionTitle: { fontSize: 14, fontWeight: '600', marginTop: 20, marginBottom: 8 },
  empty: { color: '#888', fontStyle: 'italic' },
  chunkRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#eee',
  },
  chunkPrimary: { fontSize: 13, fontWeight: '500' },
  chunkSecondary: { fontSize: 12, color: '#666' },
});
