// mobile/src/services/quality/filters.ts
//
// Vier Filter fuer die Quality-Pipeline. Jeder Filter ist ein reiner Wert-
// Funktions-Wrapper mit Namen und evaluate(). Filter halten KEINEN Zustand;
// Vorgaenger wird vom Coordinator gereicht.
//
// Schwellen sind PARAMETER, keine Defaults. Wer einen Filter benutzt, entscheidet
// die Schwelle — Runde-8-Auftrag Nr. 4 gilt sinngemaess auch hier.

import type { LocationSample } from '../../location/ports';
import { haversineDistanceM } from './geo';
import type { FilterVerdict, QualityFilter } from './pipeline';

// ------------------------------------------------------------------
// 1. Genauigkeit (GPS accuracy in Metern)
// ------------------------------------------------------------------
export interface AccuracyFilterOptions {
  /** Ueber diesem Wert -> low-confidence. */
  readonly acceptedBelowM: number;
  /** Ueber diesem Wert -> rejected. */
  readonly rejectAboveM: number;
}

export function accuracyFilter(opts: AccuracyFilterOptions): QualityFilter {
  if (opts.acceptedBelowM <= 0) throw new Error('acceptedBelowM muss > 0 sein');
  if (opts.rejectAboveM <= opts.acceptedBelowM) {
    throw new Error('rejectAboveM muss > acceptedBelowM sein');
  }
  const name = `accuracy(acc<${opts.acceptedBelowM}m,rej>${opts.rejectAboveM}m)`;
  return {
    name,
    evaluate(current): FilterVerdict {
      // accuracy === null bedeutet: das Geraet meldet keinen Wert. Wir sagen
      // 'low-confidence' — kein Verwerfen, weil sonst gaenzlich fehlende
      // Accuracy-Meldung (manche Android-Geraete) alles rausfiltern wuerde.
      if (current.accuracyMeters === null) {
        return { quality: 'low-confidence', reason: 'accuracy=null', filter: name };
      }
      if (current.accuracyMeters > opts.rejectAboveM) {
        return {
          quality: 'rejected',
          reason: `accuracy ${current.accuracyMeters.toFixed(1)}m > ${opts.rejectAboveM}m`,
          filter: name,
        };
      }
      if (current.accuracyMeters > opts.acceptedBelowM) {
        return {
          quality: 'low-confidence',
          reason: `accuracy ${current.accuracyMeters.toFixed(1)}m > ${opts.acceptedBelowM}m`,
          filter: name,
        };
      }
      return { quality: 'accepted', reason: 'accuracy ok', filter: name };
    },
  };
}

// ------------------------------------------------------------------
// 2. Veraltete Zeitstempel (staleness)
// ------------------------------------------------------------------
export interface StalenessFilterOptions {
  readonly maxAgeMs: number;
  readonly nowMs: () => number;
}

export function stalenessFilter(opts: StalenessFilterOptions): QualityFilter {
  if (opts.maxAgeMs <= 0) throw new Error('maxAgeMs muss > 0 sein');
  const name = `staleness(<${opts.maxAgeMs}ms)`;
  return {
    name,
    evaluate(current): FilterVerdict {
      const now = opts.nowMs();
      const age = now - current.timestampMs;
      if (age > opts.maxAgeMs) {
        return {
          quality: 'rejected',
          reason: `age ${age}ms > ${opts.maxAgeMs}ms`,
          filter: name,
        };
      }
      if (age < -opts.maxAgeMs) {
        // Zeitstempel liegt weit in der Zukunft — Geraeteuhr defekt.
        return {
          quality: 'rejected',
          reason: `age ${age}ms < -${opts.maxAgeMs}ms (Zukunft)`,
          filter: name,
        };
      }
      return { quality: 'accepted', reason: `age ${age}ms`, filter: name };
    },
  };
}

// ------------------------------------------------------------------
// 3. Unmoegliche Spruenge (jump distance vs. time delta)
// ------------------------------------------------------------------
export interface JumpFilterOptions {
  /** Absoluter Maximalsprung ohne Zeitpruefung, z. B. 500 m. */
  readonly rejectAboveM: number;
  /** Impliziter Maximaltempo (m/s) fuer die Zeit-Sprung-Kombination. */
  readonly rejectAboveMps: number;
}

export function jumpFilter(opts: JumpFilterOptions): QualityFilter {
  if (opts.rejectAboveM <= 0) throw new Error('rejectAboveM muss > 0 sein');
  if (opts.rejectAboveMps <= 0) throw new Error('rejectAboveMps muss > 0 sein');
  const name = `jump(>${opts.rejectAboveM}m OR >${opts.rejectAboveMps}m/s)`;
  return {
    name,
    evaluate(current, previous): FilterVerdict {
      if (previous === null) {
        // Erster Sample einer Session — kein Sprung berechenbar.
        return { quality: 'accepted', reason: 'kein Vorgaenger', filter: name };
      }
      const dt = current.timestampMs - previous.timestampMs;
      if (dt <= 0) {
        // Zeitstempel steht oder ruecklauefig — Jump-Berechnung nicht moeglich,
        // aber verdaechtig genug fuer 'low-confidence'.
        return {
          quality: 'low-confidence',
          reason: `dt ${dt}ms <= 0`,
          filter: name,
        };
      }
      const distM = haversineDistanceM(previous, current);
      if (distM > opts.rejectAboveM) {
        return {
          quality: 'rejected',
          reason: `distance ${distM.toFixed(0)}m > ${opts.rejectAboveM}m`,
          filter: name,
        };
      }
      const impliedMps = distM / (dt / 1000);
      if (impliedMps > opts.rejectAboveMps) {
        return {
          quality: 'rejected',
          reason: `implied ${impliedMps.toFixed(1)}m/s > ${opts.rejectAboveMps}m/s`,
          filter: name,
        };
      }
      return {
        quality: 'accepted',
        reason: `${distM.toFixed(0)}m in ${dt}ms (${impliedMps.toFixed(1)}m/s)`,
        filter: name,
      };
    },
  };
}

// ------------------------------------------------------------------
// 4. Ungueltige Geschwindigkeit (device-reported speed)
// ------------------------------------------------------------------
export interface SpeedFilterOptions {
  readonly rejectAboveMps: number;
  /** true erlaubt speedMps === null (Geraet meldet keine Geschwindigkeit). */
  readonly allowNull?: boolean;
}

export function speedFilter(opts: SpeedFilterOptions): QualityFilter {
  if (opts.rejectAboveMps <= 0) throw new Error('rejectAboveMps muss > 0 sein');
  const name = `speed(<${opts.rejectAboveMps}m/s)`;
  const allowNull = opts.allowNull ?? true;
  return {
    name,
    evaluate(current): FilterVerdict {
      if (current.speedMps === null) {
        return allowNull
          ? { quality: 'accepted', reason: 'speed=null erlaubt', filter: name }
          : { quality: 'low-confidence', reason: 'speed=null nicht erlaubt', filter: name };
      }
      // Negative Geschwindigkeit ist per GPS-Konvention „unbekannt" — auf null
      // abbilden ist Aufgabe des Adapters; hier reicht ein Reject.
      if (current.speedMps < 0) {
        return {
          quality: 'rejected',
          reason: `speed ${current.speedMps}m/s < 0`,
          filter: name,
        };
      }
      if (current.speedMps > opts.rejectAboveMps) {
        return {
          quality: 'rejected',
          reason: `speed ${current.speedMps.toFixed(1)}m/s > ${opts.rejectAboveMps}m/s`,
          filter: name,
        };
      }
      return { quality: 'accepted', reason: `speed ${current.speedMps.toFixed(1)}m/s`, filter: name };
    },
  };
}
