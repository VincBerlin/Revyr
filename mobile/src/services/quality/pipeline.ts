// mobile/src/services/quality/pipeline.ts
//
// Quality-Pipeline: klassifiziert LocationSample -> QualityVerdict.
// Injizierbar in den RecordingCoordinator. Ohne Pipeline: alle Samples 'raw'.
//
// Zusammensetzung: eine Kette von QualityFilter. Regel:
//  - Erstes 'rejected' beendet die Kette; Verdict ist dieser Filter.
//  - 'low-confidence' und 'accepted' propagieren; das WEAKEST-Verdict gewinnt.
//    (accepted x low-confidence -> low-confidence; low-confidence x accepted -> low-confidence.)
//  - Alle Verdikte tragen den Filter-Namen, damit der Grund im Log nachvollziehbar ist.

import type { LocationSample } from '../../location/ports';

export type QualityLabel = 'accepted' | 'low-confidence' | 'rejected';

export interface FilterVerdict {
  readonly quality: QualityLabel;
  readonly reason: string;
  readonly filter: string;
}

export interface QualityFilter {
  readonly name: string;
  evaluate(current: LocationSample, previous: LocationSample | null): FilterVerdict;
}

export interface QualityPipeline {
  readonly filters: readonly QualityFilter[];
  classify(current: LocationSample, previous: LocationSample | null): FilterVerdict;
}

// Faktor: baut aus einer Filter-Liste eine Pipeline.
// Leere Filter-Liste -> jedes Sample ist 'accepted' (Pipeline wirkt neutral).
export function pipeline(...filters: QualityFilter[]): QualityPipeline {
  return {
    filters,
    classify(current, previous): FilterVerdict {
      let worst: FilterVerdict = {
        quality: 'accepted',
        reason: 'ok',
        filter: 'pipeline',
      };
      for (const f of filters) {
        const v = f.evaluate(current, previous);
        if (v.quality === 'rejected') return v; // Early-exit
        if (v.quality === 'low-confidence' && worst.quality === 'accepted') {
          worst = v;
        }
      }
      return worst;
    },
  };
}
