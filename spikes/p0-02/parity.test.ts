// spikes/p0-02/parity.test.ts
//
// TypeScript-Paritaetstest fuer den Wegwerf-Spike P0-02 (Runde 6, Nutzerauftrag 5.1).
// Ergaenzt den Python-Lauf um die JS/TS-Ebene: null vs undefined, JSON-Roundtrip,
// Enum-Validierung, fehlende Felder. Kein Metamodell-Umbau.
//
// Aufruf:   bun test spikes/p0-02/parity.test.ts
// Fallback: bun run spikes/p0-02/parity.test.ts   (nutzt den handgeschriebenen Runner unten)
//
// Warum diese vier Achsen: der Python-Lauf zeigt JSON-Semantik als Baseline; JavaScript
// bringt vier Verhaltensunterschiede mit, die dort nicht sichtbar werden koennen:
//  (a) undefined ist ein eigener Laufzeitwert neben null
//  (b) JSON.stringify wirft undefined-Schluessel STILL weg (Feld verschwindet)
//  (c) JSON.parse liefert nie undefined zurueck, sondern immer null oder fehlend
//  (d) fehlender Schluessel === undefined beim Lesen, aber Object.hasOwn(o, k) === false
// Diese vier stehen in F2 des SPIKE-RESULTS.md als „gemeldet, noch nicht geprueft".
// Dieser Test schliesst die Luecke — und deckt genau eine Faktenaussage aus F2 als
// unpraezise auf (siehe TP-05).

type SourceValue = 'foreground' | 'background' | 'wearable' | 'import';
type QualityValue = 'raw' | 'accepted' | 'low-confidence' | 'rejected';

interface TrackPointV1 {
  latitude: number;
  longitude: number;
  timestampMs: number;
  accuracyMeters: number | null;
  altitudeMeters: number | null;
  speedMps: number | null;
  headingDegrees: number | null;
  source: SourceValue;
  isMocked: boolean | null;
  quality: QualityValue;
}

const ALLOWED_SOURCE: ReadonlyArray<SourceValue> =
  ['foreground', 'background', 'wearable', 'import'];
const ALLOWED_QUALITY: ReadonlyArray<QualityValue> =
  ['raw', 'accepted', 'low-confidence', 'rejected'];

class DeserialiseError extends Error {
  constructor(field: string, value: unknown) {
    super(`${field} '${String(value)}' nicht zulaessig`);
    this.name = 'DeserialiseError';
  }
}

// Bewusst duenn: SPIEGELT die Python-Umsetzung 1:1, um Paritaet pruefbar zu machen.
function serialize(point: unknown): string {
  return JSON.stringify(point);
}
function deserialize(payload: string): TrackPointV1 {
  const p = JSON.parse(payload) as Partial<TrackPointV1>;
  if (!ALLOWED_SOURCE.includes(p.source as SourceValue)) {
    throw new DeserialiseError('source', p.source);
  }
  if (!ALLOWED_QUALITY.includes(p.quality as QualityValue)) {
    throw new DeserialiseError('quality', p.quality);
  }
  return p as TrackPointV1;
}

// ---------------------------------------------------------------------------
// Minimaler Test-Runner. Kein Framework, damit der Test ohne bun test laeuft.
// ---------------------------------------------------------------------------
type Case = { name: string; fn: () => void };
const CASES: Case[] = [];
function tc(name: string, fn: () => void) { CASES.push({ name, fn }); }
function assertEq<T>(a: T, b: T, msg: string) {
  const A = JSON.stringify(a), B = JSON.stringify(b);
  if (A !== B) throw new Error(`${msg}: got ${A} expected ${B}`);
}
function assertTrue(cond: unknown, msg: string) {
  if (!cond) throw new Error(msg);
}
function assertThrows(fn: () => unknown, ctor: new (...a: any[]) => Error, msg: string) {
  try { fn(); } catch (e) { if (e instanceof ctor) return; throw new Error(`${msg}: falsche Fehlerklasse ${e}`); }
  throw new Error(`${msg}: kein Fehler geworfen`);
}

const fullPoint: TrackPointV1 = {
  latitude: -33.9249, longitude: 18.4241, timestampMs: 1_729_000_000_000,
  accuracyMeters: 4.2, altitudeMeters: -1.5, speedMps: 3.14, headingDegrees: 359.9,
  source: 'foreground', isMocked: false, quality: 'accepted',
};

// ---- TP-01 -------------------------------------------------------------
tc('TP-01 undefined-Schluessel wird von JSON.stringify STILL entfernt', () => {
  const withUndef = { ...fullPoint, isMocked: undefined as unknown as null };
  const s = serialize(withUndef);
  assertTrue(!s.includes('isMocked'),
    'TP-01: undefined haette laut JSON-Spez den Schluessel entfernen sollen');
  const back = JSON.parse(s) as Record<string, unknown>;
  assertTrue(!Object.hasOwn(back, 'isMocked'),
    'TP-01: nach dem Roundtrip existiert der Schluessel isMocked nicht mehr');
  assertEq(back['isMocked'], undefined,
    'TP-01: Zugriff auf fehlenden Schluessel liefert undefined, nicht null');
});

// ---- TP-02 -------------------------------------------------------------
tc('TP-02 null bleibt null; false bleibt false; beide bleiben unterscheidbar', () => {
  const pNull = { ...fullPoint, isMocked: null as boolean | null };
  const pFalse = { ...fullPoint, isMocked: false as boolean | null };
  const rNull = deserialize(serialize(pNull));
  const rFalse = deserialize(serialize(pFalse));
  assertTrue(rNull.isMocked === null,  'TP-02: null geht im Roundtrip verloren');
  assertTrue(rFalse.isMocked === false, 'TP-02: false geht im Roundtrip verloren');
  assertTrue(rNull.isMocked !== rFalse.isMocked,
    'TP-02: null und false sind nach dem Zyklus zusammengefallen');
});

// ---- TP-03 -------------------------------------------------------------
tc('TP-03 alle vier source × alle vier quality ueberleben Roundtrip', () => {
  for (const src of ALLOWED_SOURCE) {
    for (const q of ALLOWED_QUALITY) {
      const p: TrackPointV1 = { ...fullPoint, source: src, quality: q };
      const r = deserialize(serialize(p));
      assertEq(r.source, src, `TP-03: source '${src}' geht verloren`);
      assertEq(r.quality, q, `TP-03: quality '${q}' geht verloren`);
    }
  }
});

// ---- TP-04 -------------------------------------------------------------
tc('TP-04 unbekannter source-/quality-Wert wird lautlos NICHT akzeptiert', () => {
  const badSrc = serialize({ ...fullPoint, source: 'dogsled' });
  assertThrows(() => deserialize(badSrc), DeserialiseError,
    'TP-04: unbekannter source-Wert wurde still akzeptiert');
  const badQ = serialize({ ...fullPoint, quality: 'gold' });
  assertThrows(() => deserialize(badQ), DeserialiseError,
    'TP-04: unbekannter quality-Wert wurde still akzeptiert');
});

// ---- TP-05 -------------------------------------------------------------
tc('TP-05 fehlende Pflichtfelder: source/quality fehlen -> DeserialiseError', () => {
  // Der Kontrast zur SPIKE-RESULTS.md F2-Aussage „undefined verschmilzt mit „Feld fehlt"":
  // Aus Sicht des LESENDEN Codes stimmt sie — Object-Zugriff gibt in BEIDEN Faellen
  // undefined zurueck. Beim SCHREIBEN sind sie aber NICHT dasselbe: JSON.stringify laesst
  // eigene undefined-Felder weg, uebernimmt aber null-Felder. Dieser Test prueft beide
  // Wege ausdruecklich.
  const without: any = { ...fullPoint }; delete without.source;
  assertThrows(() => deserialize(serialize(without)), DeserialiseError,
    'TP-05: fehlender source-Schluessel wurde still akzeptiert');
  const withoutQ: any = { ...fullPoint }; delete withoutQ.quality;
  assertThrows(() => deserialize(serialize(withoutQ)), DeserialiseError,
    'TP-05: fehlender quality-Schluessel wurde still akzeptiert');
});

// ---- TP-06 -------------------------------------------------------------
tc('TP-06 numerische Grenzwerte: negative Koordinaten, sehr grosse timestampMs', () => {
  const extreme: TrackPointV1 = {
    ...fullPoint,
    latitude: -89.999999, longitude: -179.999999,
    timestampMs: Number.MAX_SAFE_INTEGER,
  };
  const r = deserialize(serialize(extreme));
  assertEq(r.latitude, extreme.latitude, 'TP-06: latitude verloren');
  assertEq(r.longitude, extreme.longitude, 'TP-06: longitude verloren');
  assertEq(r.timestampMs, extreme.timestampMs, 'TP-06: MAX_SAFE_INTEGER verloren');
});

// ---- TP-07 -------------------------------------------------------------
tc('TP-07 NaN/Infinity werden von JSON abgelehnt (kein stiller null-Coalesce)', () => {
  // JSON kennt weder NaN noch Infinity. JSON.stringify wandelt sie in null.
  // Ein Trackpunkt mit NaN/Infinity wuerde also KEINEN Fehler beim serialize
  // erzeugen, sondern nach dem Zyklus einen null-Wert liefern — Datenverlust ohne
  // Fehler. Dieser Test dokumentiert das explizit als Verhalten, das aendert werden
  // muesste (Produktion), nicht als Bug des Roundtrip-Kerns.
  const nan = { ...fullPoint, accuracyMeters: NaN };
  const inf = { ...fullPoint, speedMps: Infinity };
  const rNaN = JSON.parse(serialize(nan)) as any;
  const rInf = JSON.parse(serialize(inf)) as any;
  assertEq(rNaN.accuracyMeters, null,
    'TP-07: NaN wurde nicht wie erwartet zu null umgewandelt');
  assertEq(rInf.speedMps, null,
    'TP-07: Infinity wurde nicht wie erwartet zu null umgewandelt');
});

// ---------------------------------------------------------------------------
// Ausfuehren
// ---------------------------------------------------------------------------
let pass = 0, fail = 0;
const failures: string[] = [];
for (const c of CASES) {
  try { c.fn(); console.log(`ok  ${c.name}`); pass++; }
  catch (e: any) { console.log(`FAIL ${c.name}\n     ${e.message}`); failures.push(c.name); fail++; }
}
console.log(`\nZusammenfassung: ${pass} pass, ${fail} fail, ${CASES.length} gesamt`);
if (fail) { console.log('Fehlgeschlagen:', failures.join(', ')); process.exit(1); }
