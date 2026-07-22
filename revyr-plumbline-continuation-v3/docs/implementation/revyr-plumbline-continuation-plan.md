# REVYR — Präziser Plumbline-Fortsetzungsplan

Readiness-Level: `BLOCKED_CONTRADICTION`  
Mode: `DRAFT_FROM_RAW_INPUT`  
Primary Goal: Den vorhandenen Claude-Handoff stabilisieren und `GATE-A0` evidenzbasiert abschließen, ohne die Produktplanung neu zu beginnen.

## 1. Führungsprinzipien

1. Vision, Canvas und PRD bleiben kanonisch.
2. C0 ist ein technisches Recovery-Gate, keine neue Produktphase.
3. Jede Codeänderung muss einer bestehenden `REQ-*`, `AC-*` und `EV-*` zugeordnet werden.
4. Ein Bericht aus der alten Session ist keine bestandene Evidence.
5. Keine Folgephase beginnt, bevor das vorherige Gate nachweisbar bestanden ist.
6. Der kleinste sichere nächste Schritt hat Vorrang vor paralleler Feature-Entwicklung.

## 2. Zielzustand der Fortsetzung

Nach Abschluss dieses Plans liegt vor:

- reproduzierbar grüner TypeScript-Check;
- reproduzierbar grüne Unit-/Integrationstests für Aktivzeit, Segmente und SQLite;
- eindeutige Background-/Recovery-Architektur für iOS und Android;
- native Builds und dokumentierte Kern-Smokes;
- verifizierter Run-/Bike-Recording-Flow;
- belastbare Evidence für `REQ-001`–`REQ-005`;
- ein klarer Backlog für `REQ-006`–`REQ-008`;
- aktualisierte Traceability ohne neue oder doppelte IDs;
- kein falscher Done-Status.

## 3. Workstream C0 — Handoff Recovery

### C0-01 Baseline und Repository-Inventar

**Requirements:** REQ-035  
**Aufgaben:**

- aktuelle Arbeitskopie, Git-Status, Branch/HEAD und Dateibaum erfassen;
- `CLAUDE.md`, README, Handoff, `intake-package.json`, kanonische Docs und Package-Skripte lesen;
- Node-, Package-Manager-, Expo-, React-Native-, TypeScript- und Jest-Versionen dokumentieren;
- Lockfile und Installationsweg bestimmen;
- native Ordner, App-Konfiguration, Berechtigungen und Datenbankschema inventarisieren;
- keine Dateien löschen oder umbenennen, bevor Duplikate und Referenzen geklärt sind.

**Exit:**

- `docs/handoffs/current-baseline-report.md`;
- exakte Befehlsliste für Compile, Tests und Builds;
- keine unaufgelösten Annahmen über den Checkout.

### C0-02 Reproduzierbare Toolchain

**Requirements:** REQ-035, REQ-036  
**Aufgaben:**

- Abhängigkeiten ausschließlich über vorhandenes Lockfile installieren;
- TypeScript ausführen und vollständigen Exitcode dokumentieren;
- Expo-/Dependency-Diagnose ausführen;
- gezielte Jest-Suite zuerst seriell starten;
- bei Hänger offene Handles, Timer, DB-Verbindungen und Watcher messen;
- anschließend vollständige Jest-Suite ausführen;
- `--forceExit`, ausgelassene Tests oder gelockerte Assertions sind kein zulässiger Fix.

**Exit:**

- Compile- und Testlogs;
- Root Cause für jeden Fehler/Hänger;
- Evidence-Status `passed`, `failed` oder `blocked`.

### C0-03 Aktivzeit- und Segmentintegrität

**Requirements:** REQ-002, REQ-005  
**Prüffälle:**

- Start erzeugt genau ein offenes Aktivsegment;
- Pause schließt das offene Segment;
- Resume öffnet ein neues Segment;
- Stop schließt das letzte Segment;
- doppelte Start-/Pause-/Resume-Aktionen erzeugen keine ungültigen Segmente;
- Aktivzeit ist Summe geschlossener Segmente plus laufendes Segment;
- Pausenzeit zählt nicht;
- App-Restart verändert gespeicherte Aktivzeit nicht;
- Migration V2 ist idempotent;
- Orphan-Segmente werden deterministisch behandelt;
- DB-Verbindungen, Timer und Subscriptions werden geschlossen.

**Exit:**

- grüne Unit-/Repository-/Migrationstests;
- keine Datenkorruption bei Restart-Fixtures;
- `EV-002` und `EV-005` mit tatsächlichen Logreferenzen aktualisiert.

### C0-04 Evidence-Reset

**Requirements:** REQ-035  
**Aufgaben:**

- alle alten Evidence-Einträge klassifizieren:
  - `reported-unverified`
  - `pending`
  - `passed`
  - `failed`
  - `blocked`
- nur aktuelle, reproduzierte Ergebnisse auf `passed` setzen;
- jede Evidence erhält Befehl, Datum, Plattform, Ergebnis und Artefaktpfad;
- Traceability-Status wird aus Evidence abgeleitet, nicht manuell optimistisch gesetzt.

**Exit:**

- belastbares `docs/EVIDENCE-LEDGER.md`;
- keine ungestützte Done-Aussage.

## 4. Workstream A0 — Tracking Foundation

### A0-01 SportConfig und Foreground Recording

**Requirements:** REQ-001, REQ-002, REQ-004  
**Aufgaben:**

- Run/Bike-Konfiguration auf eine zentrale Source of Truth prüfen;
- harte Screen-spezifische Schwellen und Labels entfernen;
- GPS-Pipeline, Qualitätsfilter und Distanzberechnung isoliert testen;
- Start/Pause/Resume/Stop für beide Sportarten smoke-testen;
- Run zeigt Pace, Bike zeigt Geschwindigkeit.

**Exit:**

- AC-001, AC-002 und AC-004 automatisiert und auf Gerät belegt.

### A0-02 Background, Pause und Recovery

**Requirements:** REQ-003  
**Verbindliche Produktentscheidung:**

Der Wechsel der App in den Hintergrund darf eine aktive Session nicht automatisch pausieren. Pause entsteht nur durch Nutzeraktion oder definierte Auto-Pause.

**Aufgaben:**

- bestehendes AppState-Verhalten lokalisieren;
- Background-Location-Architektur je Plattform dokumentieren;
- persistente Schreibpipeline für Background-Punkte herstellen;
- Session-State-Machine von UI-Lifecycle entkoppeln;
- Berechtigungs- und Statusanzeigen implementieren;
- Recovery-Matrix für Crash, OS-Termination und bewusstes Force-Quit definieren;
- 30-Minuten-Background-/Lockscreen-Test für Run und Bike durchführen.

**Exit:**

- kein automatischer Aktivzeitstopp beim normalen Background-Wechsel;
- Session ist nach unterstützter Prozessunterbrechung wiederherstellbar;
- `EV-003` enthält reale iOS-/Android-Nachweise;
- GAP-003 ist geschlossen.

### A0-03 Native Baseline

**Requirements:** REQ-003, REQ-014, REQ-036  
**Aufgaben:**

- iOS Build;
- Android Build;
- Standortberechtigungen und Background-Modi prüfen;
- Start/Pause/Resume/Stop/History-Smoke;
- größere Schrift, Screenreader-Labels und Kontrast-Stichprobe;
- Fehler getrennt nach Code, Toolchain, Signing und Gerät dokumentieren.

**Exit:**

- beide Plattformen bauen oder besitzen einen präzisen externen Blocker;
- keine Plattform wird durch Simulator-only-Evidence als fertig erklärt.

### A0-04 Routenplanung und Fortschritt

**Requirements:** REQ-006, REQ-007  
**Reihenfolge:**

1. Provider-/Kosten-/Secret-ADR.
2. Wegpunkte und Distanzziel.
3. sportabhängiges Routingprofil.
4. Polyline-Projektion.
5. verbleibende Distanz entlang Route.
6. Off-Route, falsche Richtung, Schleifen und Umkehr.
7. reale Szenarien je Sport.

**Exit:**

- AC-006 und AC-007 mit Domain-Fixtures und Feldnachweisen.

### A0-05 Verlauf, Wiederverwendung und Export

**Requirements:** REQ-008  
**Aufgaben:**

- Abschluss schreibt eine vollständige Aktivität;
- Verlauf und Detail lesen dieselbe persistierte Quelle;
- gespeicherte Route kann erneut gestartet werden;
- GPX-Export enthält korrekte Zeit-/Positionsdaten;
- sensible Felder werden beim Teilen reduziert.

**Exit:**

- AC-008 und EV-008 bestanden.

### A0-06 Security, Accessibility und Release Gate

**Requirements:** REQ-014, REQ-034, REQ-035, REQ-036  
**Aufgaben:**

- keine produktiven Secrets im Client;
- Datenfluss und lokale/synchrone Grenzen dokumentieren;
- Accessibility-Audit;
- Distanz-, Batterie-, Kill-/Recovery- und Run/Bike-Feldtest;
- Store-Berechtigungsbegründungen vorbereiten;
- A0-Gate-Review gegen jede betroffene Requirement-Zeile.

**Exit:**

- `GATE-A0` ist entweder evidenzbasiert bestanden oder präzise blockiert;
- kein A1-Start ohne bestandenen Gate-Bericht.

## 5. Priorisierte Reihenfolge

| Reihenfolge | Paket | Warum jetzt |
|---:|---|---|
| 1 | C0-01 Baseline | verhindert Arbeit auf falschen Annahmen |
| 2 | C0-02 Toolchain | macht Fehler reproduzierbar |
| 3 | C0-03 Segmente | schließt die Stelle, an der Claude aufgehört hat |
| 4 | C0-04 Evidence | verhindert falsche Done-Claims |
| 5 | A0-01 Foreground | stabilisiert Kernflow |
| 6 | A0-02 Background | schließt die zentrale Contradiction |
| 7 | A0-03 Native Baseline | beweist Plattformfähigkeit |
| 8 | A0-04 Routing | nächster funktionaler A0-Block |
| 9 | A0-05 Verlauf/Export | komplettiert Nutzerflow |
| 10 | A0-06 Gate | entscheidet über A1-Freigabe |

## 6. Definition of Done pro Arbeitspaket

Ein Paket ist nur `done`, wenn:

- Code und Dokumentation dieselbe Requirement-Bedeutung verwenden;
- zugehörige automatisierte Tests grün sind;
- erforderliche reale Gerätetests dokumentiert sind;
- Traceability und Evidence aktualisiert sind;
- keine neue Contradiction erzeugt wurde;
- kein Test übersprungen oder künstlich beendet wurde;
- offene Risiken und externe Blocker sichtbar bleiben.

## 7. Stop Conditions

Plumbline stoppt die konkrete Änderung und meldet einen Blocker, wenn:

- Datenmigration oder Recovery Datenverlust riskieren;
- die einzige Lösung einen produktiven Secret im Client erfordert;
- Background-Berechtigungen ohne nachvollziehbare Nutzerfunktion aktiviert würden;
- iOS und Android semantisch unterschiedliche Aktivzeit berechnen;
- Tests nur durch Abschwächung der Acceptance Criteria grün werden;
- eine bestehende `REQ-*` semantisch umgeschrieben werden müsste;
- eine Repo-, Remote-, Reset-, Force- oder Push-Aktion erforderlich wäre, aber nicht freigegeben ist.

## 8. Nächster ausführbarer Schritt

Plumbline beginnt mit `C0-01`, geht unmittelbar in `C0-02` und arbeitet danach `C0-03` vollständig ab. Die Session darf nicht nach einer reinen Gap-Analyse enden. Der erste Codefokus ist die reproduzierbare Aktivzeit-/Segment-Teststrecke, weil dort der vorige Claude-Handoff endete.
