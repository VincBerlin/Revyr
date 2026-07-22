// mobile/src/services/recording-coordinator.ts
//
// RecordingCoordinator — orchestriert den Aufzeichnungsfluss auf oberer Ebene:
//
//   IDLE ---start(sport)---> RECORDING <---resume---
//                              |          |         |
//                          location       |     ----+ (pause)
//                          samples        |    |
//                              |          v    ^
//                              |        PAUSED |
//                              v          |    |
//                          buffer         |    |
//                              |          |
//   [flush per policy] -> writeChunk    finalize
//                              |          |
//                              v          v
//                           FINALIZED (endzustand)
//
// Der Coordinator besitzt WEDER die DB noch den LocationPort — beide werden
// eingespritzt. Er haelt in-memory:
//   - state
//   - session (aus dem ActivitySessionService)
//   - buffer (TrackPointV1[])
//   - lastFlushMs (fuer Zeit-basierte ChunkBoundaryPolicy)
//   - LocationSubscription (nur waehrend RECORDING)
//
// Kein Auto-Repair. Kein Auto-Resume. Kein GPS-Filter.
// Fehlerhafte Samples (NaN, ausserhalb WGS84) werden VERWORFEN und im Log gezaehlt —
// nicht in die Persistenz gefuettert.

import { TrackPointV1Schema, type TrackPointV1 } from '../domain/track-point';
import type { LocationPort, LocationSample, LocationSubscription } from '../location/ports';
import type { ActivitySessionService, ActivitySession } from './activity-session';
import type { ChunkBoundaryPolicy } from './chunk-boundary-policy';
import type { Sport } from '../db/activity-repo';
import { haversineDistanceM } from './quality/geo';
import type { FilterVerdict } from './quality/pipeline';

export type RecordingState = 'idle' | 'recording' | 'paused' | 'finalized';

export interface RecordingStatus {
  readonly state: RecordingState;
  readonly session: ActivitySession | null;
  readonly bufferSize: number;
  readonly chunksWritten: number;
  readonly samplesAccepted: number;
  readonly samplesDropped: number;
  readonly lastFlushReason: string | null;
  readonly policyName: string;
  /** Kumulierte Distanz (m) ueber alle akzeptierten Samples der Session. */
  readonly totalDistanceM: number;
  /** Letzter empfangener Sample (nicht filter-abhaengig) — fuer UI-Anzeige. */
  readonly latestSample: LocationSample | null;
  /** Letzter Pipeline-Verdict — null, wenn keine Pipeline aktiv. */
  readonly lastVerdict: FilterVerdict | null;
  /**
   * Aktive Trainingsdauer in ms — SUMME der Aktivsegmente ohne Pause- und
   * Background-Zeit. Bei state=recording wird die Dauer des OFFENEN Segments
   * (now - segmentStartMs) dazu addiert.
   */
  readonly activeMs: number;
}

export class RecordingCoordinatorError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'RecordingCoordinatorError';
  }
}

export interface RecordingCoordinatorDeps {
  readonly session: ActivitySessionService;
  readonly location: LocationPort;
  readonly policy: ChunkBoundaryPolicy;
  /**
   * Optionale Quality-Pipeline. Ohne Pipeline traegt jedes Sample 'raw' und
   * wird persistiert (Verhalten vor Runde 8). Mit Pipeline wird die Verdict-
   * Quality (accepted/low-confidence/rejected) uebernommen; rejected Samples
   * werden NICHT persistiert (samplesDropped++).
   */
  readonly qualityPipeline?: import('./quality/pipeline').QualityPipeline;
  /** Liefert Unix-ms. Injizierbar fuer deterministische Tests. */
  readonly nowMs?: () => number;
}

export class RecordingCoordinator {
  private state: RecordingState = 'idle';
  private session: ActivitySession | null = null;
  private buffer: TrackPointV1[] = [];
  private lastFlushMs = 0;
  private chunksWritten = 0;
  private samplesAccepted = 0;
  private samplesDropped = 0;
  private lastFlushReason: string | null = null;
  private subscription: LocationSubscription | null = null;
  private disposed = false;
  private previousSample: LocationSample | null = null;
  private previousAcceptedSample: LocationSample | null = null;
  private totalDistanceM = 0;
  private latestSample: LocationSample | null = null;
  private lastVerdict: FilterVerdict | null = null;
  // Aktivzeit-Bilanz:
  //  - closedActiveMsCache: Summe der bereits geschlossenen Segmente
  //  - openSegmentStartMs: Startzeitpunkt des aktuell offenen Segments
  //    (null waehrend paused/finalized/idle)
  private closedActiveMsCache = 0;
  private openSegmentStartMs: number | null = null;

  constructor(private readonly deps: RecordingCoordinatorDeps) {}

  // Idempotenter Teardown. Kann jederzeit aufgerufen werden, auch mehrfach.
  // Loest die Subscription — den einzigen externen Ressourcen-Handle, den der
  // Coordinator selbst haelt. Finalisiert die Aktivitaet ABSICHTLICH NICHT:
  // eine unfinalisierte Aktivitaet ist ein legitimer Zustand, den der Recovery-
  // Fluss beim naechsten Bootstrap wieder aufnimmt.
  dispose(): void {
    if (this.disposed) return;
    this.disposed = true;
    this.unsubscribe();
  }

  isDisposed(): boolean {
    return this.disposed;
  }

  status(): RecordingStatus {
    const openMs =
      this.openSegmentStartMs !== null ? this.now() - this.openSegmentStartMs : 0;
    return {
      state: this.state,
      session: this.session,
      bufferSize: this.buffer.length,
      chunksWritten: this.chunksWritten,
      samplesAccepted: this.samplesAccepted,
      samplesDropped: this.samplesDropped,
      lastFlushReason: this.lastFlushReason,
      policyName: this.deps.policy.name,
      totalDistanceM: this.totalDistanceM,
      latestSample: this.latestSample,
      lastVerdict: this.lastVerdict,
      activeMs: this.closedActiveMsCache + Math.max(0, openMs),
    };
  }

  // Oeffentlich ausserhalb der Zustandsmaschine: Buffer transaktional in die
  // DB schieben, ohne den State zu aendern. Fuer AppStateBridge (Background)
  // und fuer explizite „jetzt flushen"-UI-Aktionen.
  //
  // Bricht durch (wirft) wenn der DB-Schreibvorgang fehlschlaegt — der Aufrufer
  // (Bridge oder UI) entscheidet, ob er trotzdem pausiert.
  flushBuffer(reason: string): void {
    this.assertNotDisposed();
    if (this.buffer.length === 0 || this.session === null) return;
    this.flush(reason);
  }

  // ------ Zustandswechsel --------------------------------------------------

  async start(sport: Sport): Promise<RecordingStatus> {
    this.assertNotDisposed();
    this.assertState('idle');
    const granted = await this.deps.location.requestForegroundPermission();
    if (!granted) {
      throw new RecordingCoordinatorError(
        'start: Standort-Berechtigung wurde verweigert',
      );
    }
    this.resetInternal();
    // sessionService.start oeffnet bereits das erste Segment; sein Zeitstempel
    // ist activity.startedAt (dieselbe Uhr in der Service-Instanz).
    this.session = this.deps.session.start(sport);
    // Fuer die Live-Anzeige merken wir uns denselben Startzeitpunkt (Wall-clock).
    this.openSegmentStartMs = this.now();
    await this.subscribe();
    this.state = 'recording';
    return this.status();
  }

  // Setzt den Coordinator auf eine BESTEHENDE Aktivitaets-Session — der
  // Recovery-Weg (nach App-Neustart). Die Session muss vom Aufrufer per
  // ActivitySessionService.resume(id, opts) besorgt worden sein.
  async resumeFrom(session: ActivitySession): Promise<RecordingStatus> {
    this.assertNotDisposed();
    this.assertState('idle');
    if (session.finalized) {
      throw new RecordingCoordinatorError(
        `resumeFrom: Session ${session.activityId} ist bereits finalisiert`,
      );
    }
    const granted = await this.deps.location.requestForegroundPermission();
    if (!granted) {
      throw new RecordingCoordinatorError(
        'resumeFrom: Standort-Berechtigung wurde verweigert',
      );
    }
    this.resetInternal();
    this.session = session;
    // Bereits vor App-Neustart akkumulierte Aktivzeit uebernehmen.
    this.closedActiveMsCache = this.deps.session.getClosedActiveMs(session.activityId);
    // Neues Segment fuer diesen Fortsetzungslauf oeffnen (in DB).
    this.deps.session.resumeSession(session);
    this.openSegmentStartMs = this.now();
    await this.subscribe();
    this.state = 'recording';
    return this.status();
  }

  private resetInternal(): void {
    this.session = null;
    this.buffer = [];
    this.lastFlushMs = this.now();
    this.chunksWritten = 0;
    this.samplesAccepted = 0;
    this.samplesDropped = 0;
    this.lastFlushReason = null;
    this.previousSample = null;
    this.previousAcceptedSample = null;
    this.totalDistanceM = 0;
    this.latestSample = null;
    this.lastVerdict = null;
    this.closedActiveMsCache = 0;
    this.openSegmentStartMs = null;
  }

  async pause(): Promise<RecordingStatus> {
    this.assertNotDisposed();
    this.assertState('recording');
    // Zuerst Subscription trennen — waehrend pause DUERFEN keine Samples mehr
    // eintreffen. Falls die Subscription-Kuendigung wirft, ist der Coordinator
    // dennoch nicht im Zombiezustand: state bleibt 'recording'.
    this.unsubscribe();
    // Aktivzeit-Bilanz vor dem Zustandswechsel schliessen — sowohl im
    // Speicher als auch persistent (DB-Segment schliessen).
    this.closeOpenActiveSegment();
    this.state = 'paused';
    return this.status();
  }

  async resume(): Promise<RecordingStatus> {
    this.assertNotDisposed();
    this.assertState('paused');
    // Neu-Subscription VOR dem Zustandswechsel. Falls subscribe() wirft
    // (z. B. Berechtigung wurde in den Systemeinstellungen entzogen), bleibt
    // der Coordinator in 'paused' und der Fehler propagiert.
    await this.subscribe();
    // Neues Aktivzeit-Segment oeffnen — persistent + Speicher.
    if (this.session !== null) {
      this.deps.session.resumeSession(this.session);
    }
    this.openSegmentStartMs = this.now();
    this.state = 'recording';
    return this.status();
  }

  // Bilanz sauber ziehen: offenes Segment schliessen, closedActiveMsCache um
  // die soeben abgelaufene Live-Dauer erhoehen und Persistenz nachziehen.
  private closeOpenActiveSegment(): void {
    if (this.openSegmentStartMs === null) return;
    const elapsed = Math.max(0, this.now() - this.openSegmentStartMs);
    this.closedActiveMsCache += elapsed;
    this.openSegmentStartMs = null;
    if (this.session !== null) {
      this.deps.session.pauseSession(this.session);
    }
  }

  async finalize(): Promise<RecordingStatus> {
    this.assertNotDisposed();
    if (this.state !== 'recording' && this.state !== 'paused') {
      throw new RecordingCoordinatorError(
        `finalize: nur aus 'recording' oder 'paused' zulaessig (aktuell: ${this.state})`,
      );
    }
    this.unsubscribe();
    // Falls noch ein offenes Segment existiert (Zustand 'recording'), es hier
    // vor dem finalize schliessen — sonst passiert es im Service noch mal, was
    // in Ordnung waere, aber unser Cache waere veraltet.
    this.closeOpenActiveSegment();
    // Restpuffer vor dem Finalisieren rausschreiben. Ausdrueckliches Ignorieren
    // der Policy — beim Finalisieren wollen wir keinen Rest verlieren.
    if (this.buffer.length > 0) {
      this.flush('finalize: Restpuffer');
    }
    if (this.session !== null) {
      this.session = this.deps.session.finalize(this.session);
    }
    this.state = 'finalized';
    return this.status();
  }

  // ------ Interne Sample-Behandlung ---------------------------------------

  private async subscribe(): Promise<void> {
    this.subscription = await this.deps.location.watch((sample) => {
      this.onSample(sample);
    });
  }

  private unsubscribe(): void {
    if (this.subscription !== null) {
      this.subscription.cancel();
      this.subscription = null;
    }
  }

  private onSample(sample: LocationSample): void {
    if (this.session === null || this.disposed) return;
    this.latestSample = sample;
    // Erst die Quality-Pipeline (falls injiziert) klassifiziert; dann
    // schema-validiert und in TrackPointV1 verpackt.
    const filterVerdict = this.deps.qualityPipeline?.classify(sample, this.previousSample);
    this.lastVerdict = filterVerdict ?? null;
    const qualityLabel = filterVerdict?.quality ?? 'raw';
    if (qualityLabel === 'rejected') {
      // Rejected Samples werden NICHT persistiert und schieben den previousSample
      // NICHT vor. Sonst wuerde ein einzelner Rausch-Spike als neue Baseline
      // stehen und alle folgenden Samples relativ zum Rausch als weitere
      // Spruenge erscheinen — Kaskade.
      this.samplesDropped += 1;
      this.lastFlushReason = filterVerdict
        ? `verworfen (${filterVerdict.filter}): ${filterVerdict.reason}`
        : this.lastFlushReason;
      return;
    }
    const point = this.toTrackPoint(sample, qualityLabel);
    if (point === null) {
      // Schema-Verletzung. Fuer die Zuordnung zu einer AC-004-Klasse ist das
      // ein separates Signal von filter-basierter Verwerfung, aber landet
      // in derselben Zaehler-Kategorie 'dropped'.
      this.samplesDropped += 1;
      return;
    }
    // Distanz-Inkrement: nur zwischen zwei aufeinanderfolgend AKZEPTIERTEN
    // Samples. Vermeidet dass grosse Luecken (Pause / rejected-Serie) als
    // Sprung ins Distanz-Total wandern.
    if (this.previousAcceptedSample !== null) {
      this.totalDistanceM += haversineDistanceM(
        this.previousAcceptedSample,
        sample,
      );
    }
    this.previousAcceptedSample = sample;
    this.buffer.push(point);
    this.samplesAccepted += 1;
    this.previousSample = sample;
    const decision = this.deps.policy.shouldFlush(
      this.buffer.length,
      this.now() - this.lastFlushMs,
    );
    if (decision.shouldFlush) {
      this.flush(decision.reason);
    }
  }

  private flush(reason: string): void {
    if (this.session === null || this.buffer.length === 0) return;
    const toWrite = this.buffer;
    this.buffer = [];
    const out = this.deps.session.appendChunk(this.session, toWrite);
    this.session = out.session;
    this.chunksWritten += 1;
    this.lastFlushMs = this.now();
    this.lastFlushReason = reason;
  }

  private toTrackPoint(
    sample: LocationSample,
    quality: TrackPointV1['quality'],
  ): TrackPointV1 | null {
    // source: 'foreground' — Background-Tracking ist NICHT in dieser Runde.
    // quality: aus der Pipeline (oder 'raw' als Default ohne Pipeline).
    const draft = {
      latitude: sample.latitude,
      longitude: sample.longitude,
      timestampMs: sample.timestampMs,
      accuracyMeters: sample.accuracyMeters,
      altitudeMeters: sample.altitudeMeters,
      speedMps: sample.speedMps,
      headingDegrees: sample.headingDegrees,
      source: 'foreground' as const,
      isMocked: sample.isMocked,
      quality,
    };
    const parsed = TrackPointV1Schema.safeParse(draft);
    if (!parsed.success) {
      return null; // Sample verworfen — validierungs-Kette liegt in TrackPointV1.
    }
    return parsed.data;
  }

  private assertState(expected: RecordingState): void {
    if (this.state !== expected) {
      throw new RecordingCoordinatorError(
        `Uebergang nur aus '${expected}' zulaessig (aktuell: ${this.state})`,
      );
    }
  }

  private assertNotDisposed(): void {
    if (this.disposed) {
      throw new RecordingCoordinatorError(
        'Coordinator ist disposed — keine weiteren Uebergaenge zulaessig',
      );
    }
  }

  private now(): number {
    return (this.deps.nowMs ?? Date.now)();
  }
}

