# P0-02 — Spike-Ergebnisse (Wegwerf, konsolidiert Runde 6 · 2026-07-20)

Requirement: **REQ-004** · Acceptance: **AC-004** · Evidence: **EV-004** · Gate: **GATE-A0**
Status: **`SPIKE_STARTED` (Runde 5) → akzeptiert als erfolgreicher Lern-Spike (Runde 6)**
`evidence_status`: **`pending`** — dieser Bericht ist kein Ledger-Eintrag `verified`.
`owner`: **OWNER-BLOCKER (MISSING; OQ-002)** · Reference: `docs/plans/2026-07-20-p0-spikes.md` §2

---

## 1. Läufe (repo-relativ, reproduzierbar)

```
# Python-Kern (T1..T6)
cd spikes/p0-02 && python3 -m unittest test_track_point_v1.py
→ Ran 6 tests · OK (skipped=1) · EXIT 0

# TypeScript-Parität (TP-01..TP-07, Runde 6)
bun run spikes/p0-02/parity.test.ts
→ 7 pass, 0 fail · EXIT 0

# Rot-Nachweis TDD (T6-Defekt-Fang, aus Session-Historie belegt)
Naive-Umsetzung ohne Enum-Prüfung: T6 FAIL („DeserialiseError not raised") — Ziel-Defekt gefangen.
```

## 2. Kombinierte Test-Matrix

| Fall | Was | Verdikt |
|---|---|---|
| **T1** | Alle nullbaren Felder auf `null` — Roundtrip erhält | ✅ pass (Python) |
| **T2** | Alle Felder belegt, negative Lat/Lon | ✅ pass (Python) |
| **T3** | 4×4 `source`×`quality`-Kombinationen | ✅ pass (Python) |
| **T4** | `isMocked=null` ≠ `isMocked=false` nach Zyklus | ✅ pass (Python) |
| **T5** | Round-Trip über reale Aufzeichnung | ⏭ **skipped** — OQ-003 MISSING (kein Referenzgerät, keine Fixture); Detailplan §2.5 verbietet synthetischen Ersatz |
| **T6** | Unbekannte Enum-Werte → `DeserialiseError`, nicht stiller Default | ✅ pass (Python) — gefangen; naive Fassung würde failen |
| **TP-01** | `JSON.stringify` löscht `undefined`-Schlüssel STILL | ✅ pass (TS) — belegt F5 empirisch |
| **TP-02** | JS-Ebene: `null`/`false` Roundtrip-unterscheidbar | ✅ pass (TS) |
| **TP-03** | JS-Ebene: 4×4 Enum-Kombinationen | ✅ pass (TS) |
| **TP-04** | JS-Ebene: unbekannte Enum-Werte → `DeserialiseError` | ✅ pass (TS) |
| **TP-05** | Fehlende Pflichtfelder (Schlüssel nicht vorhanden) → `DeserialiseError` | ✅ pass (TS) |
| **TP-06** | Numerische Grenzwerte: negative Präzision, `MAX_SAFE_INTEGER` | ✅ pass (TS) |
| **TP-07** | `NaN`/`Infinity` in numerischen Feldern | ✅ pass (TS) — dokumentiert **stille Umwandlung zu `null`** als F4 |

## 3. Antworten auf die drei Detailplan-§2.1-Fragen

| Frage | Antwort |
|---|---|
| Verlustfreie Serialisierungsgrenze? | **JSON-Ebene: ja** (T1-T3, TP-01, TP-03, TP-06). **JS-Feinheiten dokumentiert:** F4 `NaN`/`Infinity` → `null`, F5 `undefined`-Präzisierung. Hermes-spezifisches Verhalten unter React Native **nicht** geprüft. |
| `quality` ↔ AC-004-Klassen abbildbar? | **P02-a bleibt offen.** Der Spike verlangt via T6/TP-04 nur laute Ablehnung unbekannter Werte; die Zuordnung `raw` → („noch nicht klassifiziert") bleibt plausibel und **unbelegt**. |
| Reichen reale Aufzeichnungen für die vier Fixture-Arten? | **Nicht beantwortbar in dieser Umgebung.** T5 skip; ohne OQ-003 kein Referenzgerät, ohne Tunnel-Ort keine Signal-Abriss-Fixture. |

## 4. Findings

- **F1 — Naives JSON validiert Enum-Werte nicht.** T6 empirisch nachgewiesen (naive Fassung FAIL). Für Produktion **nicht** ausreichend: die Zielstruktur ist ein TypeScript-Interface (Architektur §4), Runtime-Schema-Prüfung (`zod`/`io-ts`/generierter Runtime-Guard) ist zu entscheiden.
- **F2 — Sprachwechsel macht die JS-`undefined`-Frage sichtbar.** Python-Tests treffen `undefined`-Semantik nicht (Python kennt es nicht); die Bun-Läufe schließen die Lücke.
- **F3 — T5 ist der wirtschaftlich teure Test und der einzige, der wirklich zählt.** T1–T4 und T6 laufen am Schreibtisch; die vier EV-004-Fixture-Arten (Drift, Tunnel, Sprung, Hochgeschwindigkeit) verlangen echte Aufzeichnungen. Der Spike kann sie nicht simulieren.
- **F4 — JSON verliert `NaN`/`Infinity` STILL** (belegt durch TP-07). `JSON.stringify(NaN)` → `"null"`. Ein GPS-Punkt mit Overflow-Wert überlebt den Roundtrip **ohne Fehlermeldung**, verliert aber seinen Zahlenwert. **Für Produktion:** numerische Felder vor Serialisierung auf `Number.isFinite` prüfen. Wegwerf-Spike ändert deshalb **nichts** — Verhalten festgehalten.
- **F5 — Präzisierung von F2:** „`undefined` verschmilzt mit ‚Feld fehlt'" trifft **nur die Leseseite** (Object-Zugriff liefert in beiden Fällen `undefined`). Beim Schreiben ist `JSON.stringify` präzise: `undefined`-Werte werden **verworfen**, `null`-Werte **erhalten**. Ein `Object.hasOwn`-Check auf Empfängerseite **funktioniert**.

## 5. Abweichungen — offengelegt

- **A1 — Python statt TypeScript in T1..T6.** TS-Parität in TP-01..TP-07 nachgeholt (Runde 6, Bun 1.3.13). „Grün in Bun" ≠ „grün in Hermes" — Hermes-Verifikation nicht durchgeführt.
- **A2 — JSON statt SQLite.** JSON-Grenze ist die zwischen In-Memory und Persistenz. SQLite-Grenze prüft P0-03.
- **A3 — Kein Fixture-Ordner angelegt.** T5 skippt sauber; ein leerer Ordner wäre die stille Vorbereitung einer Ersatz-Fixture.

## 6. Evidence-Status — bewusst pending

`docs/EVIDENCE-LEDGER.md` unverändert. Kein `verified`-Eintrag.

```
EV-004 · REQ-004 · evidence_class geplant: real-boundary-smoke · evidence_status: pending
Erreicht: unit-fake (Python-JSON-Roundtrip + Enum-Härtung) + integration-fake (TS/JS-Parität).
Übergang pending → verified braucht:
  (a) OQ-002 benannt (Owner/DRI)
  (b) OQ-003 benannt (Referenzgeräte) + reale Run- und Bike-Aufzeichnung inkl. Tunnel-Ort
```

## 7. Was NICHT geschehen ist

- Kein Produktionscode, kein `mobile/`, kein Gate-Übergang, keine Blocker-Auflösung außerhalb §5.3 des Validierungsreports, keine Auflösung von P02-a, kein Hermes-Test, kein npm/Expo/RN-Setup, kein Fixture-Ordner mit Platzhaltern, keine Ledger-Zeile `verified`.
