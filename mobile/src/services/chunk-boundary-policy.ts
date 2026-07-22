// mobile/src/services/chunk-boundary-policy.ts
//
// Chunk-Grenzen als injizierbare Policy. Lehre G5 aus dem P0-03-Spike:
// die Wahl der Chunk-Groesse ist ein Batterie/Recovery-Trade-off und eine
// Produktentscheidung — dieses Modul entscheidet sie NICHT.
//
// Dieses Modul liefert:
//  - das Interface ChunkBoundaryPolicy
//  - drei Beispiel-Policies als BEISPIELE, KEINE Defaults
//    Ein Aufrufer, der eine Policy braucht, muss sich fuer eine Zahl entscheiden.

export interface ChunkBoundaryDecision {
  /** true, wenn der Puffer JETZT geflusht werden soll. */
  readonly shouldFlush: boolean;
  /** Menschenlesbarer Grund fuer Logs — hilft der Dev-UI und dem Feldtest. */
  readonly reason: string;
}

export interface ChunkBoundaryPolicy {
  /**
   * Wird nach jedem Sample UND vor finalize aufgerufen.
   * @param bufferSize     aktuelle Anzahl Samples im Puffer
   * @param msSinceLastFlush Zeit seit letztem Flush (ms)
   */
  shouldFlush(bufferSize: number, msSinceLastFlush: number): ChunkBoundaryDecision;
  /** Kurzer Bezeichner fuer Logs. */
  readonly name: string;
}

// Beispiel 1: Anzahl-basiert. "Flush, wenn Puffer >= n Samples."
export function everyNSamples(n: number): ChunkBoundaryPolicy {
  if (n <= 0) throw new Error('everyNSamples: n muss > 0 sein');
  return {
    name: `everyNSamples(${n})`,
    shouldFlush(bufferSize: number): ChunkBoundaryDecision {
      return bufferSize >= n
        ? { shouldFlush: true, reason: `bufferSize=${bufferSize} >= ${n}` }
        : { shouldFlush: false, reason: `bufferSize=${bufferSize} < ${n}` };
    },
  };
}

// Beispiel 2: Zeit-basiert. "Flush, wenn seit letztem Flush >= ms."
export function everyMs(ms: number): ChunkBoundaryPolicy {
  if (ms <= 0) throw new Error('everyMs: ms muss > 0 sein');
  return {
    name: `everyMs(${ms})`,
    shouldFlush(_bufferSize: number, msSinceLastFlush: number): ChunkBoundaryDecision {
      return msSinceLastFlush >= ms
        ? { shouldFlush: true, reason: `msSinceLastFlush=${msSinceLastFlush} >= ${ms}` }
        : { shouldFlush: false, reason: `msSinceLastFlush=${msSinceLastFlush} < ${ms}` };
    },
  };
}

// Beispiel 3: "Was zuerst kommt". Erlaubt Batterie- und Recovery-Balance.
export function samplesOrMs(
  nSamples: number,
  ms: number,
): ChunkBoundaryPolicy {
  const bySamples = everyNSamples(nSamples);
  const byTime = everyMs(ms);
  return {
    name: `samplesOrMs(${nSamples}, ${ms})`,
    shouldFlush(bufferSize: number, msSinceLastFlush: number): ChunkBoundaryDecision {
      const s = bySamples.shouldFlush(bufferSize, msSinceLastFlush);
      if (s.shouldFlush) return { shouldFlush: true, reason: `samples: ${s.reason}` };
      const t = byTime.shouldFlush(bufferSize, msSinceLastFlush);
      if (t.shouldFlush) return { shouldFlush: true, reason: `time: ${t.reason}` };
      return {
        shouldFlush: false,
        reason: `beide unter Schwelle (samples ${bufferSize}/${nSamples}, ms ${msSinceLastFlush}/${ms})`,
      };
    },
  };
}
