// mobile/src/ui/screens/HomeScreen.tsx
//
// Startbildschirm der Dev-A0-App. Zeigt:
//   - Unfinalisierte Aktivitaeten (Recovery-Kandidaten) mit Fortsetzen-Knopf
//   - Verlaufsliste finalisierter Aktivitaeten
//   - Grossen Knopf 'Neue Aktivitaet'
//
// Dumb-Component: bekommt alles ueber Props.

import { StyleSheet, Text, View, ScrollView, Pressable } from 'react-native';
import type { Activity } from '../../db/activity-repo';
import type { RecoveryReport } from '../../db/bootstrap';

export interface HomeScreenProps {
  recovery: readonly RecoveryReport[];
  finalized: readonly Activity[];
  onNewActivity(): void;
  onResume(rec: RecoveryReport, acknowledgeGaps: boolean): void;
  onOpenDetail(activityId: number): void;
}

export function HomeScreen(props: HomeScreenProps): React.JSX.Element {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>REVYR-Dev</Text>
      <Text style={styles.subtitle}>Phase 0 — nur lokal, kein Backend.</Text>

      <Pressable style={styles.primary} onPress={props.onNewActivity}>
        <Text style={styles.primaryText}>+ Neue Aktivitaet</Text>
      </Pressable>

      {props.recovery.length > 0 && (
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>
            Unfinalisierte Aktivitaeten
          </Text>
          {props.recovery.map((rec) => (
            <View key={rec.activity.id} style={styles.recoveryCard}>
              <Text style={styles.cardHeader}>
                {rec.activity.sport === 'run' ? 'Lauf' : 'Radfahrt'} · #{rec.activity.id}
              </Text>
              <Text style={styles.cardMeta}>
                Chunks: {rec.chunkCount}
                {rec.gaps.length > 0
                  ? ` · Luecken: [${rec.gaps.join(',')}]`
                  : ' · keine Luecken'}
              </Text>
              <View style={styles.buttonRow}>
                <Pressable
                  style={[styles.button, styles.buttonGood]}
                  onPress={(): void => props.onResume(rec, false)}
                >
                  <Text style={styles.buttonText}>Sauber fortsetzen</Text>
                </Pressable>
                {rec.gaps.length > 0 && (
                  <Pressable
                    style={[styles.button, styles.buttonWarn]}
                    onPress={(): void => props.onResume(rec, true)}
                  >
                    <Text style={styles.buttonText}>Trotz Luecken</Text>
                  </Pressable>
                )}
              </View>
            </View>
          ))}
        </View>
      )}

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>
          Verlauf ({props.finalized.length})
        </Text>
        {props.finalized.length === 0 ? (
          <Text style={styles.empty}>Noch keine abgeschlossenen Aktivitaeten.</Text>
        ) : (
          props.finalized.map((a) => (
            <Pressable
              key={a.id}
              style={styles.historyRow}
              onPress={(): void => props.onOpenDetail(a.id)}
            >
              <Text style={styles.historyPrimary}>
                {a.sport === 'run' ? 'Lauf' : 'Radfahrt'} #{a.id}
              </Text>
              <Text style={styles.historySecondary}>
                {formatDateTime(a.startedAt)}
                {a.finalizedAt ? ` → ${formatDateTime(a.finalizedAt)}` : ''}
              </Text>
            </Pressable>
          ))
        )}
      </View>
    </ScrollView>
  );
}

function formatDateTime(iso: string): string {
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return iso;
  const pad = (n: number): string => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

const styles = StyleSheet.create({
  container: { padding: 16, paddingTop: 60, backgroundColor: '#fff' },
  title: { fontSize: 28, fontWeight: '700', marginBottom: 4 },
  subtitle: { fontSize: 13, color: '#666', marginBottom: 20 },
  primary: {
    padding: 20,
    backgroundColor: '#111',
    borderRadius: 8,
    alignItems: 'center',
  },
  primaryText: { color: '#fff', fontSize: 18, fontWeight: '600' },
  section: { marginTop: 24 },
  sectionTitle: { fontSize: 14, fontWeight: '600', marginBottom: 10, color: '#444' },
  empty: { color: '#888', fontStyle: 'italic' },
  recoveryCard: {
    padding: 12,
    backgroundColor: '#fff8e1',
    borderRadius: 8,
    marginBottom: 8,
  },
  cardHeader: { fontSize: 15, fontWeight: '600' },
  cardMeta: { fontSize: 12, color: '#555', marginTop: 4 },
  buttonRow: { flexDirection: 'row', gap: 8, marginTop: 8, flexWrap: 'wrap' },
  button: { paddingHorizontal: 12, paddingVertical: 8, borderRadius: 6 },
  buttonGood: { backgroundColor: '#222' },
  buttonWarn: { backgroundColor: '#a33' },
  buttonText: { color: '#fff', fontSize: 13, fontWeight: '600' },
  historyRow: {
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#eee',
  },
  historyPrimary: { fontSize: 15, fontWeight: '600' },
  historySecondary: { fontSize: 12, color: '#666', marginTop: 2 },
});
