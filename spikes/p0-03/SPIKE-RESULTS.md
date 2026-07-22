# P0-03 — Spike-Ergebnisse (Wegwerf, TypeScript + SQLite · 2026-07-20)

Requirement: **REQ-005** *(zusätzliche Requirements laut Delivery Plan: **REQ-017**, **REQ-027** — hier nicht mitgenommen; Detailplan §3 Kopfzeile)*
Acceptance: **AC-005** · Evidence: **EV-005** (+ EV-042 für CONTRA-005-Anteil)
Gate: **GATE-A0** · Status: **`SPIKE_STARTED` (Runde 6)** — läuft isoliert.
`evidence_status`: **`pending`** — synthetische Fixtures, laut Nutzerauftrag Runde 6 Punkt 4 **kein** real-boundary-Nachweis.
`owner`: **OWNER-BLOCKER (MISSING; OQ-002)**
Reference: `docs/plans/2026-07-20-p0-spikes.md` §3

---

## 1. Umgebung — bewusster Ersatz für Expo-SQLite

- **Runtime:** Bun 1.3.13 (macOS arm64), TypeScript nativ.
- **SQLite:** `bun:sqlite` (Bun eingebaut, WAL-fähig, dieselbe C-Library wie andere SQLite-Bindings).
- **Warum nicht `expo-sqlite`:** verlangt React-Native-Laufzeit; ein isolierter Spike ist damit nicht möglich.
- **Semantik-Äquivalenz:** ACID, PRIMARY KEY-Constraints, `INSERT OR IGNORE`, `db.transaction()`-Rollback bei Throw — sind SQLite-Kernverhalten und nicht Bindings-spezifisch. Die verhaltensrelevanten Aussagen dieses Spikes übertragen sich auf `expo-sqlite`.
- **Ausdrücklich nicht geprüft:** Hermes-JS-Engine, iOS/Android-spezifische SQLite-Builds, Datei-System-Sync-Verhalten unter iOS-Backgrounding.

## 2. Läufe (repo-relativ, reproduzierbar)

```
# TDD-Rot (Umsetzung entfernt)
bun run spikes/p0-03/persistence.test.ts    → error: Cannot find module './persistence.ts'  · EXIT ≠ 0

# TDD-Grün (minimale Umsetzung)
bun run spikes/p0-03/persistence.test.ts    → 6 pass, 0 fail · EXIT 0

# Defekt-Nachweis für SP-02 (naive Kill-Batch)
bun run spikes/p0-03/naive-kill-demo.ts     → Chunk 2 überlebt Kill · [0,1,2] statt [0,1]
                                            → SP-02 würde in naiver Fassung failen
```

## 3. Test-Matrix

| Fall | Was | Verdikt |
|---|---|---|
| **SP-01** | Chunk schreiben, wieder lesen — Round-Trip erhält Punkte, `chunk_id`, `points_count` | ✅ pass |
| **SP-02** | Prozessabbruch mitten in Batch — Recovery zeigt NUR committete Chunks (transactionaler Rollback) | ✅ pass; naive Autocommit-Fassung durch `naive-kill-demo.ts` **empirisch als defekt widerlegt** |
| **SP-03** | Doppelte Writes desselben `(activity_id, chunk_id)` — idempotent, keine Duplikate, kein Fehler | ✅ pass (`INSERT OR IGNORE` + `changes` als Rückgabe) |
| **SP-04** | Idempotente Migration — 2. und 3. Aufruf sind No-Ops, `schema_versions` hat genau eine V1-Zeile | ✅ pass |
| **SP-05** | Langer Track: 10.000 Punkte in 100 Chunks — Vollständigkeit + keine Lücken | ✅ pass · **13,6 ms** (in-memory, protokolliert nicht bewertet) |
| **SP-06** | `findGaps` meldet Lücken korrekt | ✅ pass |

**Gesamtverdikt Grün-Lauf: 6 pass · 0 fail · EXIT 0.**

## 4. Antworten auf die drei Detailplan-§3.1-Fragen

| Frage | Antwort |
|---|---|
| Überlebt eine laufende Session einen App-Kill ohne Verlust — was ist „ohne Verlust"? | **P03-a bleibt offen.** SP-02 zeigt: **transaktionale** Chunk-Batches sind atomisch; ein Kill mitten drin verliert die gesamte Batch. **Ob das die richtige Semantik ist, ist eine Produktentscheidung** — wer eine Minute GPS lieber nachträglich rekonstruiert als sich auf einen halben Chunk verlässt, will Transaktionen; wer keine Sekunde verlieren will, will Autocommit. Der Spike **entscheidet nicht**; er zeigt beide Verhaltensweisen empirisch. |
| Ist Migration idempotent wiederholbar und lässt sie Indexe konsistent? | **Ja** (SP-04). Migration V0→V1 nutzt sowohl `CREATE TABLE IF NOT EXISTS` (Crash-Schutz) als auch eine Versions-Guard (`schema_versions.version`). Wiederholte Aufrufe sind No-Ops mit `return false`. |
| Trägt die Chunk-Persistenz lange Tracks? | **Bis 10.000 Punkte / 100 Chunks messbar** (SP-05): 13,6 ms in-memory. **Kein Zielwert vorhanden** (Detailplan §1.4: „Chunk-Größe der Trackpunkt-Persistenz — MISSING"); der Spike **schlägt keine Chunk-Größe vor**. |

## 5. Findings

- **G1 — SQLite-Rollback trägt das Kill-Sicherheitsversprechen genau dann, wenn Chunks in einer expliziten Transaktion gruppiert sind.** Autocommit-Fassungen leaken halb geschriebene Batches. Direkt belegt durch `naive-kill-demo.ts`: naive Fassung persistiert Chunk 2 vor dem Throw, transaktionale Fassung rollt ihn zurück.
- **G2 — Chunk-Idempotenz braucht kein Anwendungs-Locking.** `PRIMARY KEY (activity_id, chunk_id)` + `INSERT OR IGNORE` reicht (SP-03). Der Aufrufer bekommt über `info.changes` mitgeteilt, ob tatsächlich eingefügt wurde — kein Rate-Limit oder Applikationsmutex nötig.
- **G3 — Migrations-Idempotenz braucht BEIDE Schichten:** `IF NOT EXISTS` schützt gegen Crash-mid-Migration-Zwischenzustände, die `schema_versions`-Guard schützt gegen Semantikwechsel bei einer späteren V1'-Neudefinition. Nur eines von beiden reicht nicht.
- **G4 — Ein Kill-Test ohne echten OS-Level-SIGKILL ist ein Rollback-Test.** Der Spike simuliert den Kill durch Throw mitten in `db.transaction()`. Für echten OS-Kill (Prozess durch iOS beendet, kein `finally`) müsste die Prüfung auf dem Gerät laufen — synthetische Simulation ist nicht real-boundary.
- **G5 — Chunk-Größe ist keine Datenmodell-Frage, sondern eine Batterie-/Recovery-Frage.** Der Spike belegt: Schreiben ist billig (13,6 ms/10.000 Punkte in-memory). Der Kostenpunkt ist nicht die Schreiblatenz, sondern das Trade-off zwischen langer Batch (Batterie gut, Verlust bei Kill groß) und häufigem Commit (Batterie schlechter, Verlust klein). Diese Entscheidung ist **nicht** in diesem Spike.

## 6. Abweichungen — offengelegt

- **A1 — Bun statt Expo-SQLite.** Begründet oben (§1). Verhaltensrelevantes SQLite-Kernverhalten ist übertragbar; iOS/Android-plattformspezifisches Sync-Verhalten nicht getestet.
- **A2 — In-Memory `:memory:` und File-DB `tmpdir` — beides synthetisch.** Laut Nutzerauftrag Runde 6 Punkt 4 explizit erlaubt, zählt **nicht** als `real-boundary`.
- **A3 — Kill-Simulation via Throw.** Rollback-Semantik reicht für den Wegwerf-Spike; echter OS-Kill braucht Hardware und OQ-003.
- **A4 — CONTRA-005-Anteil (EV-042) NICHT abgedeckt.** Der Delivery Plan verlangt zusätzlich Identität/historische-Aggregate-Trennung (REQ-017, REQ-027). Der Spike bleibt beim REQ-005-Kern; die Trennung ist Schema-Entscheidung und gehört an einen späteren Schritt.

## 7. Evidence-Status — pending

```
EV-005 · REQ-005 · evidence_class geplant: real-boundary-smoke · evidence_status: pending
Erreicht: integration-fake (bun:sqlite In-Memory + tmpfile, transaktionaler Rollback belegt).
Übergang pending → verified braucht:
  (a) OQ-002 benannt (Owner/DRI)
  (b) OQ-003 benannt (Referenzgeräte) + Kill-Test auf echter lokaler DB am Gerät
  (c) Migration-Idempotenz auf einem Fixture-Set einer echten Datenbank (nicht in-memory)

EV-042 (CONTRA-005-Anteil) · Identität ↔ historische Aggregate getrennt · evidence_status: pending
Erreicht: NICHTS. Der Spike hat diesen Anteil bewusst nicht mitgenommen.
```

## 8. Was NICHT geschehen ist

- Kein Produktionscode, kein `mobile/`, kein `mobile/src/db/`, kein finales DB-Schema (das im Spike entstandene ist minimal; SP-05 nutzt es aber tut es keinen Anspruch als produktionsfertig).
- Kein OS-Level-SIGKILL, kein iOS-Backgrounding-Test, kein Retention-Handling, keine Sync-Queue.
- Keine Chunk-Größen-Empfehlung, kein Journaling-Intervall-Wert (Detailplan §1.4 hält beides als MISSING).
- Keine Auflösung von P03-a („ohne Datenverlust" ohne Bezugsgröße).
- Keine Auflösung eines Blockers, kein Gate-Übergang, keine Ledger-Zeile `verified`.
- Keine Aufnahme von REQ-017 und REQ-027 in den Spike-Scope (siehe A4).

## 9. Dateien in `spikes/p0-03/`

```
persistence.ts          Wegwerf-Umsetzung: Migration + Chunk-CRUD + Batch-Kill (transaktional)
persistence.test.ts     SP-01..SP-06, Bun-Testrunner
naive-kill-demo.ts      One-off-Nachweis für G1 (naive Batch verliert Rollback)
SPIKE-RESULTS.md        Dieser Bericht
```

Nichts davon ist Produktionscode. Nach der Nutzerprüfung wird `spikes/p0-03/` entweder
gelöscht oder — nur die _Erkenntnisse_, nicht der Code — in die eigentliche
Zielarchitektur (`mobile/src/db/`) überführt.
