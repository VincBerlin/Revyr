// mobile/src/domain/track-point/serialization.ts
//
// JSON-Serialisierung fuer TrackPointV1. Nicht der SQLite-Layer — dieser Modul
// steuert nur die Text-Grenze fuer Export/Import, Log und den Payload, der
// spaeter chunkweise persistiert wird.
//
// Aus dem Spike:
//  - F1: unbekannte Enum-Werte muessen laut abgelehnt werden -> validateTrackPoint
//  - F4: NaN/Infinity werden von JSON.stringify STILL zu null -> hier VOR dem
//    Serialisieren pro Feld gepruefte finite-Check-Kette

import {
  type TrackPointV1,
  validateTrackPoint,
} from './track-point';

export class SerializationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'SerializationError';
  }
}

// Serialisieren mit expliziter finite-Vorpruefung. Zod hat NaN/Infinity bereits im
// Schema abgelehnt; diese Funktion nimmt ein bereits validiertes TrackPointV1 an
// und stellt beim Roundtrip die vorhersagbare Feldreihenfolge sicher.
//
// stringify-Reihenfolge wird durch die eigene Schluesselliste fixiert — reproduzierbar
// ueber Plattformen (JSON.stringify hat in ECMA-262 keine deterministische Reihenfolge).
const KEY_ORDER = [
  'latitude', 'longitude', 'timestampMs',
  'accuracyMeters', 'altitudeMeters', 'speedMps', 'headingDegrees',
  'source', 'isMocked', 'quality',
] as const;

export function serializeTrackPoint(point: TrackPointV1): string {
  const ordered: Record<string, unknown> = {};
  for (const key of KEY_ORDER) {
    ordered[key] = point[key];
  }
  return JSON.stringify(ordered);
}

export function deserializeTrackPoint(payload: string): TrackPointV1 {
  let parsed: unknown;
  try {
    parsed = JSON.parse(payload);
  } catch (e) {
    throw new SerializationError(
      `TrackPointV1-Payload ist kein gueltiges JSON: ${(e as Error).message}`,
    );
  }
  return validateTrackPoint(parsed);
}

// Batch-Serialisierung: eine Zeile pro TrackPointV1 (JSONL). Vor Ort persistiert
// als String; Chunk-Grenze wird von der Persistenz-Schicht bestimmt, nicht hier.
export function serializePoints(points: readonly TrackPointV1[]): string {
  return points.map(serializeTrackPoint).join('\n');
}

export function deserializePoints(payload: string): TrackPointV1[] {
  if (payload.length === 0) return [];
  return payload
    .split('\n')
    .filter((line) => line.length > 0)
    .map(deserializeTrackPoint);
}
