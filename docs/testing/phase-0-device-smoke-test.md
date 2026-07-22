# Phase-0 · Device Smoke-Test — VORBEREITUNG

Datum der Vorbereitung: 2026-07-20 (Runde 7 initial, Runde 8 erweitert um
Quality-Pipeline, AppState und Dev-Build-Workflow, Runde 10 um reproduzierbare
Simulator-Schritte und Diagnostics-Ansicht)
Status dieses Dokuments: **Testablauf beschrieben, NICHT ausgefuehrt.**
`evidence_status` fuer EV-004 und EV-005: **`pending`** — unveraendert.
`evidence_class` — dieser Ablauf, WENN er einmal auf einem benannten
Referenzgeraet gelaufen ist, ist die kleinste Stufe `real-boundary-smoke`.
**Nichts hier ist Evidence, bevor das Ergebnis-Protokoll (siehe §6) mit realem
Geraetemodell, OS-Version, Uhrzeit und Ergebnis ausgefuellt und im
`docs/EVIDENCE-LEDGER.md` referenziert ist.**

Diese Datei ist die **Vorbereitung**. Sie darf nicht als bestandener Test
interpretiert werden, solange kein Nutzer sie auf einem benannten Geraet
tatsaechlich abgearbeitet und das Ergebnis eingetragen hat.

---

## 0. Vorbedingungen — muessen erfuellt sein, sonst NICHT starten

- [ ] `OQ-002` (Owner/DRI) benannt. Ohne benannten Abnehmenden ist auch ein grüner
      Testlauf keine Abnahme, nur eine Behauptung des Ausfuehrenden.
- [ ] `OQ-003` (Referenzgeraete) benannt. Ohne benanntes Geraetemodell und
      Mindest-OS ist der Lauf ein Ergebnis **auf einem** Geraet, nicht ein
      Beleg **fuer die Referenzklasse**. **Diese Bedingung ist derzeit MISSING**
      (siehe validation-report §5, Zeile P0/A0). Das Dokument beschreibt den
      Ablauf trotzdem; die Ausfuehrung ist erst nach Klaerung zulaessig.
- [ ] Repo auschecken, Node & Bun installiert (siehe `mobile/package.json`).
- [ ] `cd mobile && bun install` erfolgreich.

## 1. Aufbau — zwei Wege

**Runde 8 hat einen Dev-Client-Weg vorbereitet, weil `expo-location`, `expo-sqlite`
und `expo-dev-client` mittelfristig Native-Konfiguration brauchen, die Expo Go
nicht traegt.** Der Dev-Client-Weg ist der empfohlene fuer den echten
Foreground-Aufzeichnungstest; der Expo-Go-Weg funktioniert aktuell noch, wird aber
mit weiteren nativen Modulen brechen.

### Weg 0 — Sandbox-Vor-Smoke (in dieser Runde als bindend hinzugefuegt)

Bevor Weg A auf einem Menschen-Geraet laeuft, sollen diese drei Schritte auf
dem Bauhost gruen sein. Sie ersetzen KEIN Geraet, aber sie schliessen alle
Fehler aus, die man dort noch nicht sehen wuerde.

```bash
cd mobile
bun install
bunx tsc --noEmit --skipLibCheck        # (a) Typecheck
bun run test                            # (b) Jest (aktuell 185+)
bunx expo export --platform ios --output-dir /tmp/revyr-export
                                        # (c) Metro-Bundle
```

Alle drei muessen EXIT 0 liefern; das Bundle muss mindestens ein `.hbc` unter
`_expo/static/js/ios/` erzeugen. Erst danach ist Weg A sinnvoll.

### Weg A — Dev-Client (empfohlen, real-boundary-tauglich)

1. **Repository lokal auschecken.** `cd mobile && bun install`.
2. **Native-Projekte generieren:**
   ```bash
   bunx expo prebuild --platform ios    # macOS + Xcode
   bunx expo prebuild --platform android
   ```
   Ergebnis: `mobile/ios/` bzw. `mobile/android/` — beide sind **gitignored**
   und werden bei jedem Aufruf neu erzeugt.
3. **Native Build laufen lassen** (schneller Weg, kein EAS-Account):
   ```bash
   bun run ios        # oeffnet Xcode-Build + installiert im Simulator/Geraet
   bun run android    # gradle assembleDebug + adb install
   ```
   Oder via EAS Build (verlangt EAS-Konto und Anmeldung):
   ```bash
   bun run build:dev:ios       # eas build --profile development --platform ios --local
   bun run build:dev:android   # dito Android
   ```
4. **App auf dem Geraet oeffnen.** Der Dev-Client verbindet sich mit dem
   Metro-Bundler (`bun run start`).

### Weg B — Expo Go (Uebergangsweg, verliert bei weiteren nativen Modulen die Deckung)

1. `cd mobile && bun install`.
2. `bun run start` (falls Weg-A-Scripts vorher liefen, sind die Scripts jetzt auf
   `expo run:*` gemappt — dann `bunx expo start` direkt).
3. QR-Code mit „Expo Go" scannen (iOS: Kamera; Android: Expo-Go-App).

**Geraet dokumentieren:** Modell, OS-Version, Sprache, Zeitzone. In §6 eintragen.
**Weg dokumentieren:** A oder B. Bei A: `simulator` oder `physical device`.

## 2. Start der Dev-UI

```bash
cd mobile
bun run start           # bzw. bun run ios / bun run android
```

- QR-Code mit „Expo Go" scannen (iOS: Kamera; Android: Expo-Go-App).
- Beim Start erscheint der Bildschirm **„REVYR · Phase-0 Dev-UI"**.

## 3. Testfaelle

**Toggle „Fake-Location" bleibt OFF, solange die App auf einem echten Geraet mit GPS-Zugriff laeuft.** Nur im Simulator ohne simulierte Route: auf ON stellen.

### T1 — Frischer Lauf: DB legt an, kein Recovery

**Voraussetzung:** App noch nicht installiert oder Datenbank geloescht (Neustart mit
frischer DB).

**Aktion:** App starten.

**Erwartung:**
- Bootstrap-Sektion: `freshlyMigrated=true`.
- Recovery-Sektion: „Keine unfinalisierte Aktivitaet."
- Log meldet Bootstrap-Zeile mit `Recovery=0`.

**Beleg — was der Test zeigt:** Bootstrap + Migration laufen auf dem Geraet, das
`schema_versions` und die beiden Kern-Tabellen werden angelegt.
**Beleg — was der Test NICHT zeigt:** GPS-Genauigkeit, Batterieverbrauch,
Recovery-Verhalten nach Kill.

### T2 — Kurze Aktivitaet, sauberer Ablauf

**Voraussetzung:** T1 erfolgreich; Standort-Berechtigung noch nicht erteilt.

**Aktion:**
1. „Start (Run)" druecken. Berechtigungsdialog erscheint. **Genehmigen.**
2. **Bewegen** (Gehen, ~60 Sekunden). Beobachten:
   - `samples accepted` steigt.
   - `bufferSize` steigt bis 5 (Policy `everyNSamples(5)`), faellt danach auf 0,
     `chunksWritten` steigt um 1.
3. „Finalize" druecken.

**Erwartung:**
- `state` durchlaeuft `recording → finalized`.
- Am Ende: `chunksWritten` >= 1 (i. d. R. mehrere).
- `lastFlush` in Log enthaelt `bufferSize=5 >= 5` oder `finalize: Restpuffer`.

**Beleg — was der Test zeigt:** RecordingCoordinator schreibt echte GPS-Samples,
Chunk-Boundary-Policy loest Flushes aus, `finalize` schreibt Restpuffer.
**Beleg — was der Test NICHT zeigt:** GPS-Filter-Qualitaet (nicht Gegenstand),
Distanzgenauigkeit (NFR-001 braucht Referenzstrecke, siehe [N1]-Ledger).

### T3 — App-Neustart mit unfinalisierter Aktivitaet

**Voraussetzung:** T2 erfolgreich; App laeuft und ist NICHT finalisiert.

**Aktion:**
1. „Start (Run)" druecken (zweite Aktivitaet).
2. **Bewegen**, mindestens 2 Chunks entstehen lassen (`chunksWritten >= 2`).
3. **App gewaltsam beenden** (iOS: App-Switcher → hochwischen; Android: Recent-Apps → wegwischen).
4. **App neu starten**.

**Erwartung:**
- Bootstrap-Sektion: `freshlyMigrated=false`.
- Recovery-Sektion zeigt **eine Zeile** mit der Aktivitaet aus Schritt 1–3;
  `chunkCount >= 2`, `gaps=[]`.
- „Sauber fortsetzen" druecken. Log: „Aktivitaet X aufgenommen · nextChunkId=…".
- **Weiter bewegen**, ein bis zwei weitere Chunks entstehen lassen.
- „Finalize" druecken.
- Recovery-Sektion aktualisiert sich: die Aktivitaet ist weg.

**Beleg — was der Test zeigt:** Die Persistenz-Kette (Bootstrap → Recovery-Bericht
→ `resume` → weiter aufzeichnen → finalize) traegt ueber einen App-Kill hinweg.
**Beleg — was der Test NICHT zeigt:** Verhalten unter OS-Backgrounding (App wird
vom OS entladen, nicht vom Nutzer gewaltsam beendet). Das ist ein eigenes Ticket.

### T4 — Standort-Berechtigung verweigern

**Voraussetzung:** In den Geraeteinstellungen fuer die Expo-Go-App den
Standort-Zugriff auf „Verweigert" setzen (oder App-Daten loeschen und beim
Dialog in T2 „Verweigern" waehlen).

**Aktion:** „Start (Run)" druecken.

**Erwartung:** Fehlermeldung im Log: „Start-Fehler: … Standort-Berechtigung wurde verweigert".
`state` bleibt `idle`. Keine Aktivitaet in der DB.

**Beleg — was der Test zeigt:** Fehlerpfad des Adapters greift.
**Beleg — was der Test NICHT zeigt:** Wiederherstellungsfluss nach spaeter erteilter Berechtigung.

### T5 — Pause und Resume

**Voraussetzung:** T2 laeuft.

**Aktion:**
1. „Start (Run)". Ein paar Samples eintreffen lassen.
2. „Pause". `state=paused`. Weiter **bewegen**, aber `samples accepted` steigt NICHT.
3. „Resume". `state=recording`. Weiter bewegen, `samples accepted` steigt wieder.
4. „Finalize".

**Erwartung:** Wie in Text; keine Samples werden waehrend der Pause aufgezeichnet.

**Beleg — was der Test zeigt:** Subscription wird beim Pause tatsaechlich
entfernt (iOS: Standort-Icon in der Statusleiste verschwindet).
**Beleg — was der Test NICHT zeigt:** Background-Location-Verhalten waehrend Pause
(gibt es gar nicht in dieser Version).

### T7 — Quality-Pipeline auf realem GPS

**Voraussetzung:** T2 erfolgreich; „Filter aktiv"-Schalter ON.

**Aktion:** Aufnahme starten. Auf einem Balkon oder unter freiem Himmel starten
(guter Fix). Dann **in ein Gebaeude** oder in eine Tiefgarage gehen (schlechter
Fix, hohe accuracyMeters-Werte). Wieder herauskommen.

**Erwartung:**
- Vor dem Gebaeude: `samples accepted` steigt kontinuierlich; im Chunk-JSON
  tragen die Punkte `quality: 'accepted'`.
- Im Gebaeude: `samples dropped` steigt. Im `lastFlush`-Feld erscheint der
  Filter-Grund („verworfen (accuracy…): accuracy 200m > 100m").
- Zurueck im Freien: `samples accepted` steigt wieder.

**Beleg — was der Test zeigt:** Pipeline greift auf realem GPS.
**Beleg — was der Test NICHT zeigt:** dass die Schwellen produktiv richtig
gesetzt sind (`accepted<20m`, `reject>100m` sind Dev-Werte, nicht kalibriert).

### T-DIAG — Diagnostics-/Calibration-Ansicht

**Voraussetzung:** T2 oder T7 laeuft (Aufnahme aktiv).

**Aktion:**
1. Wahrend `state=recording`: rechts oben auf **„Diagnostics"** tippen.
2. Ansicht zeigt live: `latestSample` (Lat/Lng/Zeitstempel/accuracy/altitude/
   speed/heading/isMocked), `lastVerdict` (quality/filter/reason), Session-Kenn­
   zahlen und die letzten 12 Verdikte in einer Historie.
3. Erwarte, dass jedes eintreffende Sample einen neuen History-Eintrag erzeugt.
   Bewege dich; bei ruhigem Halten sollten immer haeufiger `accuracy`-Verbes­
   serungen sichtbar werden. Notiere:
   - Typische `accuracy` im Freien
   - Typische `accuracy` in Gebaeuden
   - Anteil `rejected` vs `low-confidence` vs `accepted` in einer Minute
4. „zurueck" fuehrt in die Aufzeichnung zurueck; die Aufnahme laeuft ununter­
   brochen weiter.

**Beleg — was der Test zeigt:** Kalibrierungsgrundlage. Roh­daten und Filter­
verdikte laufen live, ohne Persistenzumweg. Der Bildschirm setzt KEINE
Schwellen fest — er zeigt sie nur.
**Beleg — was der Test NICHT zeigt:** die richtigen Werte. Die Kalibrierungs­
entscheidung folgt aus dieser Beobachtung, sie ist ihr Ergebnis, nicht ihr
Bestandteil.

### T-ERR — ErrorBoundary faengt Renderer-Fehler

**Voraussetzung:** Weg A oder B, App laeuft.

**Aktion (kunstlich):** Ein Debugger-Snippet einfuegen, das aus einem Screen
`throw new Error('BOOM')` waehrend des Renderns wirft — z. B. temporaer in
`RecordingScreen.tsx` vor dem `return`.

**Erwartung:**
- Der rote React-Native-Redbox erscheint NICHT.
- Stattdessen: Fallback-Screen „Etwas ist schiefgelaufen" mit Fehlerbox und
  „Zurueck zum Start"-Knopf.
- Der Text sagt ausdruecklich, dass die Aufzeichnung nicht beendet ist und
  auf dem Startbildschirm fortgesetzt werden kann.
- Nach dem Klick landet die App wieder auf Home; die Aktivitaet ist im
  Recovery-Bericht zu finden.

**Beleg — was der Test zeigt:** Renderer-Ausnahmen entwerten keine Session.
Aufzeichnung bleibt in der DB, die App kehrt kontrolliert zum Start zurueck.

### T8 — AppState-Backgrounding

**Voraussetzung:** Weg A (Dev-Client); Real-Location; Filter aktiv oder aus.

**Aktion:**
1. „Start (Run)" druecken. Ein paar Samples eintreffen lassen.
2. **App in den Hintergrund schicken** (Home-Button, App-Switcher — NICHT
   force-quit). Bildschirm sperren geht auch.
3. Log-Zeile ansehen (spaeter via `bun run start` und Console).
4. Wieder in den Vordergrund holen.
5. Nutzer entscheidet: „Resume" oder „Finalize".

**Erwartung:**
- Beim Backgrounding: Log-Zeile „AppState · background: pause() aufgerufen, buffer=N".
- Coordinator-State ist `paused`; `activeSubscriptions` = 0.
- Beim Rueckkehr: Log-Zeile „AppState · active: Coordinator=paused (Nutzer muss Resume druecken)".
- **KEIN Auto-Resume** — das ist ausdruecklich so.

**Beleg — was der Test zeigt:** AppStateBridge greift; Buffer wird beim
Backgrounding gehalten (Coordinator geht nur in `paused`, nicht `idle`).
**Beleg — was der Test NICHT zeigt:** was passiert, wenn iOS die App im
Hintergrund tatsaechlich beendet (Memory-Pressure). Das ist der uebernaechste
Test und braucht laenger als 5 Minuten Warten.

### T6 — Chunk-Luecke: Resume verlangt Bestaetigung

**Aufwand:** Nur mit Fake-Location praktikabel, weil eine Luecke kunstlich erzeugt
werden muss. Auf „Fake-Location" umschalten.

**Aktion:**
1. „Start (Run)". „Fake-Sample einspeisen" **6-mal** druecken → 1 Chunk (5 Samples) +
   1 Sample im Puffer.
2. Ueber den Debug-Zugang (adb bzw. Xcode-Filestore) manuell in die SQLite-DB
   (`revyr.db`) einen Chunk mit `chunk_id=3` einfuegen. **In der Dev-UI selbst
   ist das nicht vorgesehen; dieser Test ist realistischer im Emulator.**
3. App gewaltsam beenden und neu starten.

**Erwartung:**
- Recovery-Sektion zeigt die Aktivitaet mit `gaps=[1,2]` (oder aehnlich).
- Zwei Buttons: „Sauber fortsetzen" (blau) und **„Trotz Luecken fortsetzen"** (rot).
- „Sauber fortsetzen" → Log: „Resume blockiert (Luecken [1,2]) — Nutzerentscheidung noetig".
- „Trotz Luecken fortsetzen" → Log: „Aktivitaet X aufgenommen · … ackGaps=true".

**Beleg — was der Test zeigt:** Der Gap-Guard greift auf dem Geraet. Ein stiller
Resume bei Luecken ist nicht moeglich.
**Beleg — was der Test NICHT zeigt:** Automatische Nachzugsstrategie fuer die
fehlenden Chunks (bewusst nicht implementiert).

## 4. Was gilt AUCH nach bestandenem Ablauf NICHT als geloest

- **P02-a** (Vokabular `quality` ↔ AC-004-Klassen). Wird nur getestet, dass Werte
  `raw` in der DB landen; die Zuordnungsfrage bleibt offen.
- **P03-a** („ohne Datenverlust" ohne Bezugsgroesse). Der Test misst nicht die
  Nullschwelle; er zeigt nur, dass Chunks nach Kill wiederkommen.
- **Chunk-Groesse** (G5). Die Dev-Policy `everyNSamples(5)` ist kein
  Produktvorschlag; sie ist so klein, weil ein Feldtest mit `everyNSamples(600)`
  Minuten braucht, bis ueberhaupt ein Chunk entsteht.
- **NFR-001** (Distanzabweichung < 3 %). Verlangt Referenzstrecke, siehe Ledger [N1].
- **NFR-003** („0 verlorene Aktivitaeten"). Der T3-Ablauf ist ein Einzelfall; die
  Nullschwelle ist eine `production-verified`-Aussage, kein Smoke-Beleg.

## 5. Grenze zur Reality-Ledger-Regel

Ein bestandener Ablauf dieses Dokuments belegt AUSSCHLIESSLICH:

- Der Aufzeichnungsfluss laeuft auf **dem** getesteten Geraet
  in der **dort** getesteten OS-Version.
- Der Recovery-Fluss laeuft auf **dem** getesteten Geraet.

Das ist `real-boundary-smoke` **fuer diese Kombination**, nicht fuer die
Referenzklasse. Der Uebergang von `pending → verified` in
`docs/EVIDENCE-LEDGER.md` verlangt zusaetzlich:

1. **OQ-003 gesetzt** — sonst „auf diesem Geraet" statt „auf Referenzgeraet".
2. **Run und Bike getrennt** (bislang nur Run-Testfall; Bike braucht eigenes T2/T3).
3. **Zwei Plattformen** — iOS UND Android, nicht eine.
4. **Owner-Signatur** (OQ-002) — nicht die des Ausfuehrenden.

## 6. Ergebnisprotokoll (leer — ausfuellen, sonst KEIN Evidence)

Fuer jeden Testlauf eine eigene Zeile. Ohne diese Zeile ist der Test nicht gelaufen.

| Datum | Weg | Geraet + OS | Tester | Weg 0 | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T-DIAG | T-ERR | Auffaelligkeiten |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _—_ | _A_ | _iPhone 15 iOS 18.0_ | _—_ | – | – | – | – | – | – | – | – | – | – | – | _—_ |
| _—_ | _A_ | _Pixel 8 Android 14_ | _—_ | – | – | – | – | – | – | – | – | – | – | – | _—_ |

Legende: ✅ bestanden · ❌ fehlgeschlagen · ⏭ uebersprungen (mit Grund in
„Auffaelligkeiten").

## 7. Wenn ein Test fehlschlaegt

- **Nicht schoen faerben.** Ein ❌ ist ein Ergebnis, nicht ein Grund fuer einen
  zweiten Versuch, bis er ✅ wird.
- Auffaelligkeiten aufschreiben (Screenshot, Log-Zeile, Reproschritte).
- Wenn der Fehler die Kette blockiert: als Blocker in `validation-report.md` §5
  aufnehmen. Der `evidence_status` bleibt `pending` (nicht `failed`, weil `failed`
  einen Deployment-Kontext hat, den der Smoke-Test nicht liefert).

## 8. Was dieses Dokument NICHT ist

- **Kein Produkt-Testplan.** Der kommt spaeter aus dem PRD.
- **Kein Automat.** Alles hier laeuft **manuell**; niemand pretendiert, es sei ein
  End-to-End-Test-Framework.
- **Kein Abnahmedokument.** Ein bestandener Ablauf ist eine Voraussetzung fuer
  Abnahme, nicht die Abnahme selbst.
