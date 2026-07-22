// mobile/src/ui/format.ts
//
// Reine Formatierungshelfer fuer die Recording-UI. Kein State, keine RN-,
// Zod- oder DB-Abhaengigkeit. Voll testbar.
//
// Regeln:
//  - Duration als HH:MM:SS wenn >= 1h, sonst MM:SS.
//  - Distanz in km mit 2 Nachkommastellen ueber 1 km, in m unter 1 km.
//  - Pace nur fuer Run (min:sec / km). speedMps <= 0 -> '—' (nicht rechenbar).
//  - Speed nur fuer Bike (km/h mit einer Nachkommastelle).
//  - Alle Formatter geben '—' bei null/undefined/NaN/Infinity zurueck.

export function isFiniteNumber(n: unknown): n is number {
  return typeof n === 'number' && Number.isFinite(n);
}

export function formatDurationMs(ms: number | null | undefined): string {
  if (!isFiniteNumber(ms) || ms < 0) return '—';
  const total = Math.floor(ms / 1000);
  const hours = Math.floor(total / 3600);
  const minutes = Math.floor((total % 3600) / 60);
  const seconds = total % 60;
  const mm = String(minutes).padStart(2, '0');
  const ss = String(seconds).padStart(2, '0');
  if (hours > 0) {
    const hh = String(hours).padStart(2, '0');
    return `${hh}:${mm}:${ss}`;
  }
  return `${mm}:${ss}`;
}

export function formatDistance(meters: number | null | undefined): string {
  if (!isFiniteNumber(meters) || meters < 0) return '—';
  if (meters < 1000) return `${Math.round(meters)} m`;
  return `${(meters / 1000).toFixed(2)} km`;
}

// Pace: min:sec / km. Nur fuer Run sinnvoll.
export function formatPace(speedMps: number | null | undefined): string {
  if (!isFiniteNumber(speedMps) || speedMps <= 0) return '—';
  const minPerKm = 1000 / (speedMps * 60);
  if (!Number.isFinite(minPerKm) || minPerKm > 99) return '—'; // langsamer als 99 min/km = Gehen im Stand
  const min = Math.floor(minPerKm);
  const sec = Math.round((minPerKm - min) * 60);
  // 60-Sekunden-Uebertrag
  const carry = sec === 60 ? 1 : 0;
  const secDisplay = carry ? 0 : sec;
  return `${min + carry}:${String(secDisplay).padStart(2, '0')} /km`;
}

// Speed: km/h. Nur fuer Bike sinnvoll.
export function formatSpeed(speedMps: number | null | undefined): string {
  if (!isFiniteNumber(speedMps) || speedMps < 0) return '—';
  const kmh = speedMps * 3.6;
  return `${kmh.toFixed(1)} km/h`;
}

// GPS-Qualitaetsstatus fuer die UI. Nimmt latest accuracy und optional Verdict.
export function formatGpsStatus(
  accuracyMeters: number | null | undefined,
  verdictQuality: string | null | undefined,
): string {
  const acc = isFiniteNumber(accuracyMeters) ? `±${Math.round(accuracyMeters)}m` : '±–';
  const q = verdictQuality ?? 'raw';
  return `${q} · ${acc}`;
}

// Menschlicher Fehler-Cast fuer die UI. Nimmt einen Error und mappt auf einen
// Kurzsatz, der Nutzern etwas sagt. Fallback: der Fehler-Text selbst.
export function humanErrorMessage(error: unknown): string {
  if (!(error instanceof Error)) return String(error);
  const msg = error.message;
  if (msg.includes('Standort-Berechtigung')) {
    return 'Standort-Berechtigung wurde nicht erteilt. Bitte in den Systemeinstellungen aktivieren.';
  }
  if (msg.includes('bereits finalisiert')) {
    return 'Diese Aktivitaet ist bereits abgeschlossen.';
  }
  if (msg.includes('Uebergang')) {
    return `Aktion in diesem Zustand nicht moeglich (${msg}).`;
  }
  if (msg.includes('Chunk-Luecken')) {
    return `Diese Aktivitaet hat Luecken. Fortsetzen erfordert eine ausdrueckliche Bestaetigung.`;
  }
  return msg;
}
