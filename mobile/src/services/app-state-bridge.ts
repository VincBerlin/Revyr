// mobile/src/services/app-state-bridge.ts
//
// Bruecke zwischen React Natives AppState und dem RecordingCoordinator.
// Kein direkter Import von 'react-native' hier — der Modul kennt nur einen
// eigenen Port; der RN-Adapter lebt in rn-app-state-source.ts.
//
// Regel A0:
//   active -> ("wieder da") : NUR Log; kein Auto-Resume. Nutzer entscheidet.
//   background -> RecordingCoordinator ist 'recording' : pause() + Log
//   background -> Coordinator ist anders : Log
//   inactive  : ignoriert (kurze Uebergangsphase, kein Aktions-Trigger)

import type { RecordingCoordinator } from './recording-coordinator';

export type AppLifecycle = 'active' | 'background' | 'inactive';

export interface AppStateSource {
  addChangeListener(fn: (state: AppLifecycle) => void): () => void;
  currentState(): AppLifecycle;
}

export interface AppStateBridgeDeps {
  readonly coordinator: RecordingCoordinator;
  readonly source: AppStateSource;
  /** Optional: nachvollziehbares Log fuer Dev-UI + Tests. */
  readonly onEvent?: (msg: string) => void;
}

export class AppStateBridge {
  private unsubscribe: (() => void) | null = null;
  private attached = false;

  constructor(private readonly deps: AppStateBridgeDeps) {}

  attach(): void {
    if (this.attached) return;
    this.unsubscribe = this.deps.source.addChangeListener((state) =>
      this.handle(state),
    );
    this.attached = true;
  }

  detach(): void {
    if (!this.attached) return;
    if (this.unsubscribe !== null) this.unsubscribe();
    this.unsubscribe = null;
    this.attached = false;
  }

  isAttached(): boolean {
    return this.attached;
  }

  private handle(state: AppLifecycle): void {
    const status = this.deps.coordinator.status();
    switch (state) {
      case 'background': {
        if (status.state === 'recording') {
          // Reihenfolge: erst flushBuffer (synchron, transaktional), dann pause.
          // Grund: pause() zieht die Location-Subscription; ein hier noch offener
          // Chunk waere sonst nur in-memory und wuerde bei OS-driven-Kill
          // (Memory-Pressure im Hintergrund) verloren.
          const beforeChunks = status.chunksWritten;
          const beforeBuffer = status.bufferSize;
          try {
            this.deps.coordinator.flushBuffer('AppState: background');
          } catch (e) {
            this.emit(`background: flushBuffer FEHLER: ${(e as Error).message}`);
            // pause trotzdem versuchen — Subscription muss weg, auch wenn der
            // Flush scheiterte. Der Fehler ist damit sichtbar, nicht schweigend.
          }
          const afterChunks = this.deps.coordinator.status().chunksWritten;
          const flushed = afterChunks - beforeChunks;
          this.deps.coordinator.pause().then(
            () =>
              this.emit(
                `background: pause() aufgerufen, buffer=${beforeBuffer} ` +
                `(${flushed > 0 ? `${flushed} Chunk(s) geflusht` : 'nichts zu flushen'})`,
              ),
            (err: Error) =>
              this.emit(`background: pause() FEHLER: ${err.message}`),
          );
        } else {
          this.emit(`background: keine Aktion (state=${status.state})`);
        }
        break;
      }
      case 'active': {
        // Kein Auto-Resume. Wir dokumentieren nur.
        this.emit(`active: Coordinator=${status.state}${
          status.state === 'paused' ? ' (Nutzer muss Resume druecken)' : ''
        }`);
        break;
      }
      case 'inactive':
        // Kurze Uebergangsphase, keine Aktion.
        break;
    }
  }

  private emit(msg: string): void {
    if (this.deps.onEvent) this.deps.onEvent(msg);
  }
}
