// mobile/src/ui/__tests__/format.test.ts
import {
  formatDistance,
  formatDurationMs,
  formatGpsStatus,
  formatPace,
  formatSpeed,
  humanErrorMessage,
} from '../format';

describe('formatDurationMs', () => {
  test('gibt "—" fuer null/undefined/negativ/NaN/Infinity', () => {
    expect(formatDurationMs(null)).toBe('—');
    expect(formatDurationMs(undefined)).toBe('—');
    expect(formatDurationMs(-1)).toBe('—');
    expect(formatDurationMs(NaN)).toBe('—');
    expect(formatDurationMs(Infinity)).toBe('—');
  });

  test('MM:SS unter 1 h', () => {
    expect(formatDurationMs(0)).toBe('00:00');
    expect(formatDurationMs(1000)).toBe('00:01');
    expect(formatDurationMs(65 * 1000)).toBe('01:05');
    expect(formatDurationMs(59 * 60 * 1000 + 59 * 1000)).toBe('59:59');
  });

  test('HH:MM:SS ab 1 h', () => {
    expect(formatDurationMs(60 * 60 * 1000)).toBe('01:00:00');
    expect(formatDurationMs(2 * 3600 * 1000 + 30 * 60 * 1000 + 15 * 1000)).toBe('02:30:15');
  });
});

describe('formatDistance', () => {
  test('gibt "—" fuer null/negativ/NaN/Infinity', () => {
    expect(formatDistance(null)).toBe('—');
    expect(formatDistance(-1)).toBe('—');
    expect(formatDistance(NaN)).toBe('—');
    expect(formatDistance(Infinity)).toBe('—');
  });

  test('Meter unter 1 km', () => {
    expect(formatDistance(0)).toBe('0 m');
    expect(formatDistance(1)).toBe('1 m');
    expect(formatDistance(999)).toBe('999 m');
  });

  test('Kilometer ab 1 km', () => {
    expect(formatDistance(1000)).toBe('1.00 km');
    expect(formatDistance(1234)).toBe('1.23 km');
    expect(formatDistance(12345)).toBe('12.35 km');
  });
});

describe('formatPace', () => {
  test('null/negativ/0 -> "—"', () => {
    expect(formatPace(null)).toBe('—');
    expect(formatPace(0)).toBe('—');
    expect(formatPace(-1)).toBe('—');
    expect(formatPace(NaN)).toBe('—');
  });

  test('konkrete Werte', () => {
    // 3 m/s -> 1000 / (3*60) = 5,555 min/km -> 5:33
    expect(formatPace(3)).toBe('5:33 /km');
    // 4 m/s -> 4:10
    expect(formatPace(4)).toBe('4:10 /km');
  });

  test('60-Sekunden-Uebertrag', () => {
    // Sekunden werden gerundet; wenn Rundung 60 ergibt, um 1 min anheben
    // 1000 / (60*0.16667) = 100 min/km ist zu langsam (> 99) -> '—'
    // Suche einen Wert, wo sec.round == 60:
    // 1/(x*60) * 1000 = 5.9999... -> sec = round((5.9999-5)*60) = round(59.99) = 60
    // speedMps = 1000/(5.9999*60) ~ 2.7778...
    const s = 1000 / (6 * 60); // exakt 6:00
    expect(formatPace(s)).toBe('6:00 /km');
    // Etwas darunter -> gerundet zu 6:00
    const s2 = 1000 / ((6 - 0.0001 / 60) * 60);
    expect(formatPace(s2)).toBe('6:00 /km');
  });

  test('zu langsam (>99 min/km) -> "—"', () => {
    expect(formatPace(0.001)).toBe('—');
  });
});

describe('formatSpeed', () => {
  test('null/negativ -> "—"', () => {
    expect(formatSpeed(null)).toBe('—');
    expect(formatSpeed(-1)).toBe('—');
  });

  test('konkrete Werte', () => {
    expect(formatSpeed(0)).toBe('0.0 km/h');
    expect(formatSpeed(10)).toBe('36.0 km/h');
    expect(formatSpeed(2.777778)).toBe('10.0 km/h');
  });
});

describe('formatGpsStatus', () => {
  test('kompaktes Format Qualitaet + Accuracy', () => {
    expect(formatGpsStatus(5, 'accepted')).toBe('accepted · ±5m');
    expect(formatGpsStatus(50, 'low-confidence')).toBe('low-confidence · ±50m');
  });

  test('null-Accuracy -> ±–', () => {
    expect(formatGpsStatus(null, 'raw')).toBe('raw · ±–');
    expect(formatGpsStatus(undefined, null)).toBe('raw · ±–');
  });
});

describe('humanErrorMessage', () => {
  test('erkennt Standort-Berechtigung', () => {
    expect(humanErrorMessage(new Error('start: Standort-Berechtigung wurde verweigert')))
      .toContain('Systemeinstellungen');
  });

  test('erkennt finalisierte Aktivitaet', () => {
    expect(humanErrorMessage(new Error('resume: Aktivitaet 3 ist bereits finalisiert')))
      .toContain('bereits abgeschlossen');
  });

  test('erkennt Uebergangsfehler', () => {
    expect(humanErrorMessage(new Error('Uebergang nur aus recording zulaessig')))
      .toContain('nicht moeglich');
  });

  test('erkennt Chunk-Luecken', () => {
    expect(humanErrorMessage(new Error('resume: Aktivitaet 3 hat Chunk-Luecken [1,2]')))
      .toContain('Bestaetigung');
  });

  test('unbekannter Fehler -> Nachricht durchgereicht', () => {
    expect(humanErrorMessage(new Error('etwas anderes'))).toBe('etwas anderes');
  });

  test('non-Error -> String()', () => {
    expect(humanErrorMessage('einfach ein string')).toBe('einfach ein string');
    expect(humanErrorMessage(42)).toBe('42');
  });
});
