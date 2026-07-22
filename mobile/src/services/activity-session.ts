// mobile/src/services/activity-session.ts
//
// ActivitySessionService — der oberste Anwendungsdienst fuer den Tracking-Fluss.
// Kapselt Repository-Aufrufe hinter einer Session-Wert-orientierten API.
//
// Immutabilitaet: ActivitySession ist ein reiner Wert. appendChunk gibt einen
// NEUEN Session-Wert mit inkrementiertem nextChunkId zurueck; der Aufrufer
// ersetzt seine Referenz. Kein internal-state-Mutation.
//
// Anti-Drift-Regel: nextChunkId wird NIE erfunden. Beim start/resume wird er aus
// highestChunkId + 1 gebildet (Recovery-fest). Beim append wird der zurueckgegebene
// Wert benutzt, nicht ein rein in-memory hochgezaehlter Zaehler.

import {
  finalizeActivity,
  getActivity,
  startActivity as repoStartActivity,
  type Activity,
  type Sport,
} from '../db/activity-repo';
import {
  buildChunk,
  findGaps,
  highestChunkId,
  writeChunk,
  type WriteChunkResult,
} from '../db/chunk-repo';
import {
  closeOpenSegment,
  closedActiveMs,
  findOpenSegment,
  startSegment,
} from '../db/segment-repo';
import type { SQLiteBinding } from '../db/ports';
import type { TrackPointV1 } from '../domain/track-point';

export interface ActivitySession {
  readonly activityId: number;
  readonly sport: Sport;
  readonly startedAt: string;
  readonly nextChunkId: number;
  readonly finalized: boolean;
}

export interface AppendChunkOutcome {
  readonly session: ActivitySession;
  readonly write: WriteChunkResult;
  readonly pointsCount: number;
}

export class ActivitySessionError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'ActivitySessionError';
  }
}

// Erhoben, wenn resume() ohne acknowledgeGaps auf eine Aktivitaet trifft, deren
// Chunk-Kette Luecken hat. Traegt die betroffenen Chunk-IDs, damit die UI sie
// dem Nutzer zeigen kann — kein stilles Weitergehen.
export class ResumeWithGapsError extends ActivitySessionError {
  readonly gaps: readonly number[];
  readonly activityId: number;
  constructor(activityId: number, gaps: readonly number[]) {
    super(
      `resume: Aktivitaet ${activityId} hat Chunk-Luecken [${gaps.join(',')}]. ` +
      `Explizite Bestaetigung noetig (acknowledgeGaps: true).`,
    );
    this.name = 'ResumeWithGapsError';
    this.gaps = gaps;
    this.activityId = activityId;
  }
}

export interface ResumeOptions {
  /**
   * Muss ausdruecklich true sein, wenn die Aktivitaet Chunk-Luecken hat.
   * Fehlt der Flag, wirft resume() eine ResumeWithGapsError — kein stilles
   * Fortsetzen einer moeglicherweise defekten Kette.
   *
   * Ein UI-Aufrufer, der acknowledgeGaps=true setzt, DOKUMENTIERT damit die
   * Nutzerentscheidung. Der Aufruf ist die Bestaetigung.
   */
  readonly acknowledgeGaps?: boolean;
}

export class ActivitySessionService {
  constructor(
    private readonly db: SQLiteBinding,
    private readonly clock: () => string = () => new Date().toISOString(),
  ) {}

  start(sport: Sport): ActivitySession {
    const startedAt = this.clock();
    const activity = repoStartActivity(this.db, sport, startedAt);
    // Erstes Aktivzeit-Segment mit demselben Zeitstempel wie die Aktivitaet
    // (0 ms Differenz — Aktivitaet und Aufzeichnung starten gemeinsam).
    startSegment(this.db, activity.id, startedAt);
    return this.toSession(activity, 0);
  }

  // Pausiert die Session persistiert: schliesst das offene Segment auf now.
  // Idempotent: wenn kein Segment offen ist (z. B. weil der Bootstrap es
  // schon geschlossen hat), tut die Methode nichts.
  pauseSession(session: ActivitySession): void {
    closeOpenSegment(this.db, session.activityId, this.clock());
  }

  // Nimmt eine pausierte Session persistiert wieder auf: oeffnet ein neues
  // Segment. Erwartet, dass KEIN Segment mehr offen ist — der Aufrufer
  // (Coordinator) ist dafuer zustaendig.
  resumeSession(session: ActivitySession): void {
    startSegment(this.db, session.activityId, this.clock());
  }

  // Summe der geschlossenen Aktivzeit-Segmente. Bei einer LAUFENDEN Session
  // muss der Aufrufer die Zeit des offenen Segments (now - segment.started_at)
  // selbst dazu addieren; das macht der Coordinator im Status.
  getClosedActiveMs(activityId: number): number {
    return closedActiveMs(this.db, activityId);
  }

  // Nimmt eine bestehende, nicht finalisierte Aktivitaet auf. Bootstrapping-fest,
  // weil nextChunkId aus der DB rekonstruiert wird (highestChunkId + 1).
  //
  // Wenn die Kette Chunk-Luecken hat (z. B. weil ein Batch-Kill Chunks 3 und 4
  // rausgerollt hat, aber 5 dank spaeteren Retry existiert), wirft resume() eine
  // ResumeWithGapsError. Ein explizites acknowledgeGaps=true erlaubt den
  // Uebergang — als dokumentierte Nutzerentscheidung, nicht als stiller Default.
  resume(activityId: number, opts: ResumeOptions = {}): ActivitySession {
    const activity = getActivity(this.db, activityId);
    if (activity === null) {
      throw new ActivitySessionError(
        `resume: Aktivitaet ${activityId} existiert nicht`,
      );
    }
    if (activity.finalizedAt !== null) {
      throw new ActivitySessionError(
        `resume: Aktivitaet ${activityId} ist bereits finalisiert`,
      );
    }
    const gaps = findGaps(this.db, activityId);
    if (gaps.length > 0 && opts.acknowledgeGaps !== true) {
      throw new ResumeWithGapsError(activityId, gaps);
    }
    const high = highestChunkId(this.db, activityId);
    const next = high === null ? 0 : high + 1;
    return this.toSession(activity, next);
  }

  // Schreibt EINEN Chunk und liefert eine neue Session mit nextChunkId + 1.
  // Wirft, wenn die Session bereits finalisiert ist.
  appendChunk(
    session: ActivitySession,
    points: readonly TrackPointV1[],
  ): AppendChunkOutcome {
    if (session.finalized) {
      throw new ActivitySessionError(
        `appendChunk: Aktivitaet ${session.activityId} ist bereits finalisiert`,
      );
    }
    const chunk = buildChunk(session.activityId, session.nextChunkId, points);
    const result = writeChunk(this.db, chunk, this.clock());
    const nextSession: ActivitySession = {
      ...session,
      nextChunkId: session.nextChunkId + 1,
    };
    return { session: nextSession, write: result, pointsCount: points.length };
  }

  finalize(session: ActivitySession): ActivitySession {
    if (session.finalized) {
      throw new ActivitySessionError(
        `finalize: Aktivitaet ${session.activityId} ist bereits finalisiert`,
      );
    }
    const now = this.clock();
    // Falls noch ein Segment offen ist (Coordinator hat es nicht geschlossen),
    // hier schliessen. Idempotent auf 'nichts offen'.
    closeOpenSegment(this.db, session.activityId, now);
    finalizeActivity(this.db, session.activityId, now);
    return { ...session, finalized: true };
  }

  // Fuer Tests + Bootstrap-Diagnose: gibt zurueck, ob ein offenes Segment
  // fuer diese Aktivitaet existiert.
  hasOpenSegment(activityId: number): boolean {
    return findOpenSegment(this.db, activityId) !== null;
  }

  private toSession(activity: Activity, nextChunkId: number): ActivitySession {
    return {
      activityId: activity.id,
      sport: activity.sport,
      startedAt: activity.startedAt,
      nextChunkId,
      finalized: activity.finalizedAt !== null,
    };
  }
}
