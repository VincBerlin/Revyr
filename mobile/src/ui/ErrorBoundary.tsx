// mobile/src/ui/ErrorBoundary.tsx
//
// Faengt Rendering- und Lifecycle-Fehler unterhalb dieser Komponente ab, damit
// die App nicht mit einer roten React-Native-Redbox stehen bleibt. Zeigt eine
// menschliche Fehlermeldung und einen Neustart-Knopf (setzt lokalen State zurueck).
//
// componentDidCatch faengt KEINE async-Fehler oder Fehler in Event-Handlern —
// die werden weiterhin ueber setError/humanErrorMessage vom App-Ausser­rand aus
// behandelt. Hier geht es um Renderer-Ausnahmen.

import { Component, type ErrorInfo, type ReactNode } from 'react';
import { Pressable, ScrollView, StyleSheet, Text, View } from 'react-native';

interface ErrorBoundaryState {
  readonly error: Error | null;
  readonly info: ErrorInfo | null;
}

export interface ErrorBoundaryProps {
  readonly children: ReactNode;
  /** Optional: externer Hook fuer Telemetrie/Logging. */
  readonly onError?: (error: Error, info: ErrorInfo) => void;
}

export class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  constructor(props: ErrorBoundaryProps) {
    super(props);
    this.state = { error: null, info: null };
    this.handleReset = this.handleReset.bind(this);
  }

  static getDerivedStateFromError(error: Error): Partial<ErrorBoundaryState> {
    return { error };
  }

  componentDidCatch(error: Error, info: ErrorInfo): void {
    this.setState({ info });
    if (this.props.onError) this.props.onError(error, info);
    // Console-Log ist absichtlich; in Dev-Client landet das im Metro-Log.
    // In Produktion wuerden wir das an eine Telemetrie-Senke geben.

    console.error('[ErrorBoundary]', error, info.componentStack);
  }

  handleReset(): void {
    this.setState({ error: null, info: null });
  }

  render(): ReactNode {
    if (this.state.error === null) {
      return this.props.children;
    }
    return (
      <ScrollView contentContainerStyle={styles.container}>
        <Text style={styles.title}>Etwas ist schiefgelaufen.</Text>
        <Text style={styles.subtitle}>
          Die Aufzeichnung wurde nicht beendet — sie liegt als unfinalisierte
          Aktivitaet im Recovery-Bericht und kann auf dem Startbildschirm
          fortgesetzt werden.
        </Text>
        <View style={styles.errorBox}>
          <Text style={styles.errorLabel}>Fehler</Text>
          <Text style={styles.errorText}>{this.state.error.message}</Text>
          {this.state.info?.componentStack && (
            <>
              <Text style={styles.errorLabel}>Stack (Kurzform)</Text>
              <Text style={styles.errorStack}>
                {shortStack(this.state.info.componentStack)}
              </Text>
            </>
          )}
        </View>
        <Pressable style={styles.button} onPress={this.handleReset}>
          <Text style={styles.buttonText}>Zurueck zum Start</Text>
        </Pressable>
      </ScrollView>
    );
  }
}

function shortStack(stack: string, maxLines = 8): string {
  return stack.split('\n').filter((l) => l.trim().length > 0).slice(0, maxLines).join('\n');
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
    paddingTop: 60,
    backgroundColor: '#fff',
    flexGrow: 1,
  },
  title: { fontSize: 22, fontWeight: '700', marginBottom: 8 },
  subtitle: { fontSize: 13, color: '#555', marginBottom: 20 },
  errorBox: {
    padding: 12,
    backgroundColor: '#fdecea',
    borderRadius: 8,
    marginBottom: 20,
  },
  errorLabel: { fontSize: 11, color: '#a33', fontWeight: '700', marginTop: 8 },
  errorText: { fontSize: 13, color: '#333', marginTop: 2 },
  errorStack: {
    fontSize: 11,
    color: '#666',
    fontFamily: 'Courier',
    marginTop: 4,
  },
  button: {
    padding: 16,
    backgroundColor: '#111',
    borderRadius: 8,
    alignItems: 'center',
  },
  buttonText: { color: '#fff', fontSize: 15, fontWeight: '600' },
});
