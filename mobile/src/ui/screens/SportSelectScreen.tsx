// mobile/src/ui/screens/SportSelectScreen.tsx
import { Pressable, StyleSheet, Text, View } from 'react-native';
import type { Sport } from '../../db/activity-repo';

export interface SportSelectScreenProps {
  onSelect(sport: Sport): void;
  onBack(): void;
}

export function SportSelectScreen(props: SportSelectScreenProps): React.JSX.Element {
  return (
    <View style={styles.container}>
      <Pressable onPress={props.onBack} style={styles.back}>
        <Text style={styles.backText}>← zurueck</Text>
      </Pressable>
      <Text style={styles.title}>Sportart waehlen</Text>

      <Pressable
        style={[styles.tile, styles.tileRun]}
        onPress={(): void => props.onSelect('run')}
      >
        <Text style={styles.tileTitle}>Lauf</Text>
        <Text style={styles.tileHint}>Pace in min/km</Text>
      </Pressable>

      <Pressable
        style={[styles.tile, styles.tileBike]}
        onPress={(): void => props.onSelect('ride')}
      >
        <Text style={styles.tileTitle}>Radfahrt</Text>
        <Text style={styles.tileHint}>Geschwindigkeit in km/h</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, paddingTop: 60, backgroundColor: '#fff' },
  back: { marginBottom: 12 },
  backText: { fontSize: 14, color: '#333' },
  title: { fontSize: 22, fontWeight: '700', marginBottom: 24 },
  tile: {
    padding: 32,
    borderRadius: 12,
    marginBottom: 16,
    alignItems: 'center',
  },
  tileRun: { backgroundColor: '#f0f0f0' },
  tileBike: { backgroundColor: '#e0e8f0' },
  tileTitle: { fontSize: 24, fontWeight: '700' },
  tileHint: { fontSize: 12, color: '#666', marginTop: 6 },
});
