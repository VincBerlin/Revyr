// mobile/src/domain/track-point/track-point.ts
//
// Domain-Kern fuer TrackPointV1. Rein deklarativ, keine RN-, Expo- oder DB-Abhaengigkeit.
//
// Struktur nach docs/architecture/revyr-target-architecture.md §4.
//
// Lehren aus dem Wegwerf-Spike spikes/p0-02/:
//  - F1: naives JSON validiert Enum-Werte nicht -> hier Zod-Enum
//  - F4: JSON.stringify(NaN|Infinity) === "null" (stiller Datenverlust) -> hier .finite()
//  - F5: JSON.stringify wirft undefined-Schluessel STILL weg -> hier .nullable() statt .optional()

import { z } from 'zod';

// Vokabulare aus AC-004 bzw. Architektur §4. OFFEN (P02-a): Abbildung der vier
// quality-Werte auf die drei AC-004-Klassen. Der Wert 'raw' bleibt hier bewusst
// erhalten; die Zuordnung ist eine Produktentscheidung, die dieses Modul NICHT trifft.
export const TRACK_POINT_SOURCE_VALUES = [
  'foreground',
  'background',
  'wearable',
  'import',
] as const;

export const TRACK_POINT_QUALITY_VALUES = [
  'raw',
  'accepted',
  'low-confidence',
  'rejected',
] as const;

export type TrackPointSource = (typeof TRACK_POINT_SOURCE_VALUES)[number];
export type TrackPointQuality = (typeof TRACK_POINT_QUALITY_VALUES)[number];

// Zod-Schema. .finite() rejectet BEIDES: NaN UND Infinity.
// .nullable() ohne .optional() heisst: der Schluessel MUSS vorhanden sein und darf
// null sein — Missing-Key wird abgelehnt (vermeidet den F5-Fall, dass ein fehlender
// Schluessel beim Lesen mit undefined verschmilzt).
const finiteNumber = z.number().finite();
const nullableFiniteNumber = finiteNumber.nullable();

// Fuer latitude/longitude zusaetzliche Bereichsgrenzen (WGS84 Grad).
const latitude = finiteNumber.min(-90).max(90);
const longitude = finiteNumber.min(-180).max(180);
// timestampMs: nichtnegativ (Unix-Zeit vor 1970 ist im Sport-Kontext irrelevant).
const timestampMs = z.number().finite().int().nonnegative();

export const TrackPointV1Schema = z.object({
  latitude,
  longitude,
  timestampMs,
  accuracyMeters: nullableFiniteNumber,
  altitudeMeters: nullableFiniteNumber,
  speedMps: nullableFiniteNumber,
  headingDegrees: nullableFiniteNumber,
  source: z.enum(TRACK_POINT_SOURCE_VALUES),
  isMocked: z.boolean().nullable(),
  quality: z.enum(TRACK_POINT_QUALITY_VALUES),
});

export type TrackPointV1 = z.infer<typeof TrackPointV1Schema>;

// Validierungs-Fehler mit erkennbarem Namen (nicht ZodError, damit Aufrufer nicht
// die Zod-Detail-API kennen muss).
export class TrackPointValidationError extends Error {
  readonly issues: readonly z.ZodIssue[];
  constructor(issues: readonly z.ZodIssue[]) {
    super(`TrackPointV1 ungueltig: ${issues.length} Verletzung(en) — ` +
          issues.map((i) => `${i.path.join('.')}:${i.code}`).join(', '));
    this.name = 'TrackPointValidationError';
    this.issues = issues;
  }
}

export function validateTrackPoint(input: unknown): TrackPointV1 {
  const result = TrackPointV1Schema.safeParse(input);
  if (!result.success) {
    throw new TrackPointValidationError(result.error.issues);
  }
  return result.data;
}

// Explizite finite-number-Pruefung fuer Aufrufer, die einen Wert vor Uebergabe an
// die Struktur ableiten. Sicherer als "value ?? null" — undefined wuerde beim
// JSON-Serialisieren still verschwinden (F5), NaN/Infinity waeren still null (F4).
export function toFiniteOrNull(value: number | null | undefined): number | null {
  if (value === null || value === undefined) return null;
  return Number.isFinite(value) ? value : null;
}
