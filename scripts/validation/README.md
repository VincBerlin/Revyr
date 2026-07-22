# REVYR Validatorkette

Stand: 2026-07-20. **Gesamtstatus bleibt `BLOCKED_TRACEABILITY`.** Nichts in diesem
Verzeichnis ist eine Freigabe oder ein Gate-Verdikt. Ein grüner Lauf von `run_all.sh`
wäre keine Bestätigung — er sagt nur, dass kein Werkzeug FAIL meldet.

## Aufruf

```bash
"/Users/vincentschnetzer/Documents/Run&Bike/scripts/validation/run_all.sh"
```

Aus einem Klon heraus genauso — der Repo-Pfad wird aus dem Skriptort aufgelöst
(`scripts/validation/` → zwei Ebenen aufwärts). Überschreibbar:

```bash
REVYR_REPO="/pfad/zum/klon" scripts/validation/run_all.sh
REVYR_SKIP_SELFTEST=1 scripts/validation/run_all.sh   # ohne den ~5-min-Selbsttest
```

⚠️ Der Repo-Pfad enthält ein kaufmännisches Und (`Run&Bike`). **Jede** Pfadangabe
gehört in Anführungszeichen.

Exit-Code `0` = kein Werkzeug meldet FAIL. Exit-Code `1` = mindestens eines meldet FAIL.
Beim gegenwärtigen Stand ist `1` das **erwartete** Ergebnis (siehe unten).

## Was die Kette prüft

| Werkzeug | Prüft | Verdikt aus |
|---|---|---|
| `registry_model.py` | ID-Registry lesbar, Duplikate, Zählungen je Präfix | Exit-Code |
| `validate_schema.py` | `intake-package.json` gegen `intake-package.schema.json` | Exit-Code |
| `validate_intake.py` | Hauptvalidator: 38 Kriterien C1…C38 über PRD, Traceability, Registry, Decision-Log | Exit-Code |
| `validate_trace.py` | `docs/traceability.md` gegen die eingefrorene Registry | Exit-Code |
| `check_prd.py` | PRD: Messmodell-Felder, Achsenvokabular, blocking-Formel, Personas | Exit-Code |
| `xcheck.py` | Kreuzabgleich Registry ↔ Canvas (aktiv/deprecated/reserved) | JSON-Inhalt |
| `verify.py` | `traceability.md`: Tabellenstruktur, abgeleitete Zählungen, Status-Tally | Zeile `FAILS: N` |
| `verify_canvas.py` | Canvas: Tabellenintegrität, Definitionszeilen | Exit-Code |
| `oq_check.py` | Jede OQ-ID bezeichnet genau eine Entscheidung, über vier Artefakte | Exit-Code |
| `AUDIT_points.py` | Offene §8-Punkte der Registry gegen den Validation-Report | — (Bericht) |
| `selftest_validator.py` | Negativkontrolle: reagiert jede Prüfung auf ihren Defekt? (13 Fälle) | Exit-Code |

`blocking_model.py` und `registry_model.py` sind **Modelle**. `blocking_model.py` hat
kein `__main__` und wird nur importiert; `registry_model.py` ist zusätzlich direkt
aufrufbar und wird deshalb als erster Schritt informativ ausgeführt.

### Drei Werkzeuge setzen keinen Exit-Code

`verify.py`, `xcheck.py` und `AUDIT_points.py` enthalten **kein** `sys.exit`. Sie
beenden sich immer mit `0`, auch wenn sie Befunde melden. `run_all.sh` leitet das
Verdikt deshalb aus der Ausgabe ab:

- `verify.py` → Zeile `FAILS: N`; FAIL bei `N > 0`.
- `xcheck.py` → PASS nur, wenn alle vier Abweichungslisten im JSON leer sind.
- `AUDIT_points.py` → **kein** Bestehensbegriff. Läuft als `INFO`, nicht als Gate.

Das ist eine Interpretation **im Wrapper**, keine Änderung am Werkzeug. Sie ist hier
offengelegt, damit niemand sie für eine Werkzeugeigenschaft hält.

## Tatsächliche Ausgabe (2026-07-20, vollständiger Lauf)

Wörtlich mitgeschrieben, nicht nachgetippt. Laufzeit **7:14 min**, Exit-Code **1**.

```
REVYR Validatorkette
Repo:      /Users/vincentschnetzer/Documents/Run&Bike
Werkzeuge: /Users/vincentschnetzer/Documents/Run&Bike/scripts/validation
Logs:      /var/folders/2x/ly396np91xl0rsp0nprfw_f40000gn/T//revyr-validation-81396
Python:    Python 3.14.2
------------------------------------------------------------
registry_model.py        PASS   rc=0
validate_schema.py       PASS   rc=0
validate_intake.py       FAIL   rc=1  (siehe .../validate_intake.py.log)
validate_trace.py        PASS   rc=0
check_prd.py             PASS   rc=0
xcheck.py                PASS   alle Abweichungslisten leer (kein eigener Exit-Code)
verify.py                FAIL   FAILS=1 (kein eigener Exit-Code; bekannter Werkzeugdefekt)
verify_canvas.py         FAIL   rc=1  (siehe .../verify_canvas.py.log)
oq_check.py              FAIL   rc=1  (siehe .../oq_check.py.log)
AUDIT_points.py          INFO   Bericht ohne Bestehensbegriff (siehe Log)
selftest_validator.py    PASS   rc=0
------------------------------------------------------------
ZUSAMMENFASSUNG: PASS=6  FAIL=4  INFO/SKIP=1
FEHLGESCHLAGEN: validate_intake.py verify.py verify_canvas.py oq_check.py
Gesamtstatus bleibt BLOCKED_TRACEABILITY. Dieser Lauf ist keine Freigabe.
```

`selftest_validator.py` meldet im Volltext **„SCHARF: 13/13
Werkzeug-Negativkontrollen"** und **„ERGEBNIS: alle Pruefungen sind scharf (jede
reagiert auf ihren Defekt)"** — der Selbsttest allein braucht 4:47 min der 7:14.

Mit `REVYR_SKIP_SELFTEST=1` lautet die Zusammenfassung `PASS=5 FAIL=4 INFO/SKIP=2`,
Exit-Code unverändert **1**; die vier FAILs sind dieselben.

`validate_intake.py` meldet **32/38 bestanden, 6 fehlgeschlagen**. Darunter C7 („Reale
Testausführung gegen laufenden Code"), das ein Dokumentenlauf nicht bestehen **kann**,
weil kein Code existiert — es wird ausdrücklich als nicht erfüllt geführt, nicht als
bestanden. Die vier FAILs sind damit nicht alle gleichartig: einer ist ein echter
Befundstand, drei sind Werkzeugdefekte.

## Bekannte Werkzeugdefekte

Aktenkundig und **unverändert übernommen**. Die Werkzeuge sind eingefroren; ein Defekt
im Werkzeug wird nicht durch Umschreiben des Dokuments „behoben".

- **`verify.py`**: Der D-Tally vergleicht gegen ein **hartkodiertes `claim`-Literal, das
  veraltet ist**. Dokument ist aktuell, Werkzeug ist falsch. `FAILS 1`. Nicht
  umgeschrieben (Freeze).
- **`verify_canvas.py`**: Der Spaltenzähler **honoriert maskierte Pipes nicht** und
  meldet `TABLE@187` falsch. Das Markdown ist korrekt. Werkzeug-Falschmeldung.
- **`oq_check.py`**: Der Themenklassifikator **kennt `OQ-012`…`OQ-016` nicht** und wirft
  sie in `UNCLASSIFIED`. Der Folgebefund „eine Entscheidung wird von mehr als einer
  OQ-ID bezeichnet" ist daraus **abgeleitet und NICHT belastbar**.

Nebenbeobachtung, nur gemeldet, nicht zu einem Befund erhoben: `verify.py` maskiert
Pipes in seiner `cells()`-Funktion (`s.replace("\\|", "\x00")`), `verify_canvas.py`
nicht. Der Unterschied ist im Quelltext beider Dateien sichtbar und deckt sich mit dem
zweiten Defekt oben. Daraus folgt **keine** Aussage darüber, wie er zu beheben wäre.

## Nachträglich aufgenommen

**`gen_intake.py`** stand nicht auf der Übernahmeliste, wird aber zur **Laufzeit**
gebraucht:

- `selftest_validator.py:31` führt es in `TOOLS`; `stage()` kopiert jede Datei aus
  `TOOLS` mit `shutil.copy(os.path.join(HERE, f), …)` — **ohne** `isfile`-Prüfung.
  Fehlt die Datei, bricht der Selbsttest mit `FileNotFoundError` ab, bevor er einen
  einzigen Fall prüft.
- `validate_intake.py:2425` nimmt es in `tool_files` (Prüfung C14) und `:2437` in
  `count_tool_files` (C26) auf. Beide Prüfungen überspringen fehlende Dateien
  (`validate_intake.py:1627`), melden dann aber eine kleinere Grundgesamtheit.

Es wird deshalb **mitgeführt, aber nicht ausgeführt**: `gen_intake.py` ist ein
**Generator** und schreibt nach `os.path.join(REPO, "intake-package.json")`
(`gen_intake.py:19-20`). Ein Aufruf innerhalb der Prüfkette würde das Artefakt
überschreiben, das die Kette gerade prüft. `run_all.sh` ruft es nicht auf.

## Ausschlussliste — bewusst NICHT übernommen

Das Quellverzeichnis enthält 100 Einträge (`ls -A | wc -l`). Übernommen wurden 15
benannte Dateien plus `gen_intake.py`, zusammen 16. Nicht übernommen und warum:

| Gruppe | Beispiele | Grund |
|---|---|---|
| Generatoren | `gen_canvas.py`, `gen_registry.py`, `gen_trace.py` | Erzeugen Artefakte, prüfen sie nicht. Gehören nicht in eine Prüfkette; ein Lauf würde `docs/` überschreiben. `gen_intake.py` ist die begründete Ausnahme (siehe oben) und wird nicht ausgeführt. |
| Einmal-Skripte / Zwischenstände | `atoms.py`, `req_split.py`, `req4041.py`, `fix_umlauts.py`, `patch_source_types.py`, `strip_blocking.py`, `derive_counts.py`, `audit_parse.py`, `parse_registry.py`, `blocks.py`, `nums.py`, `prd.py`, `refs.py`, `sample.py`, `build-verification.py` | Werkzeuge einer zurückliegenden Umbaurunde. Nicht Teil der aktiven Kette; von keinem übernommenen Werkzeug importiert (per Import-Durchsicht geprüft). |
| Teil-Audits | `AUDIT_gates.py`, `AUDIT_p0src.py` | Nicht im Auftrag benannt. `AUDIT_points.py` war ausdrücklich benannt und ist übernommen. **Nicht stillschweigend ergänzt** — falls sie zur Kette gehören sollen, ist das eine Entscheidung des Nutzers, keine des Ausführenden. |
| Daten-Zwischenstände | `derived.json`, `refs.json` (1,5 MB), `registry.json`, `trc.json`, `measurement-model.json`, `id-migration*.json`, `nfr-audit.json`, `FINAL.json`, `result.json`, `NEW_step*.json`, `OLD_*.json`, `open_points.json`, `defs.json`, `req_gates.json`, `source_type_rows.json` | Caches und Läufe von vor Runde 4. `registry_model.py:14-19` hält ausdrücklich fest, dass der Cache-Weg aufgegeben wurde: „EIN Parser, zur LAUFZEIT aus `docs/ID-REGISTRY.md`. Kein Cache." Ein Mitkopieren würde einen überholten Stand wiederbeleben. |
| Laufprotokolle / Textausgaben | `*.txt` (u. a. `BASELINE_intake.txt`, `NEW_run.txt`, `run_verify.txt`, `final_run.txt`, `nichtauffindbar.txt`, `term-search-*.txt`, `headers.txt`, `allowed.txt`, `blocked.txt`, `bad.txt`, `ok.txt`, `one.txt`, `myids.txt`) | Ausgaben vergangener Läufe, keine Eingaben. Reproduzierbar über `run_all.sh`. |
| Zwischenberichte (Markdown) | `canvas-proposals.md`, `semantic-review.md` | Arbeitsstände, keine Werkzeuge. Ein anderer Schritt zieht die Dokumente nach. |
| `__pycache__/` | — | Bytecode-Artefakt. |

Jede dieser Auslassungen ist hier benannt. Es wurde nichts weggelassen, ohne es
aufzuführen.

## Lauf aus einem Klon

Geprüft am 2026-07-20: Repository nach
`…/scratchpad/clone-test/RevyrClone` kopiert, `run_all.sh` von dort gestartet. Die
Auflösung greift, das Werkzeugverzeichnis und der Repo-Pfad zeigen auf den Klon,
Verdikte identisch (`PASS=5 FAIL=4 INFO/SKIP=2`).

### ⚠️ Einschränkung: zwei Werkzeuge folgen dem Klon NICHT

Der Auftrag ging von **fünf** Werkzeugen mit hartkodiertem Repo-Pfad aus. Tatsächlich
enthalten **zehn** Dateien das Literal:

| Datei | Zeile | Überschreibbar? |
|---|---:|---|
| `xcheck.py` | — | **geändert** → Skriptort / `REVYR_REPO` |
| `verify.py` | — | **geändert** |
| `verify_canvas.py` | — | **geändert** |
| `oq_check.py` | — | **geändert** |
| `AUDIT_points.py` | — | **geändert** |
| `registry_model.py` | 27 | ja — `DEFAULT_REPO`, via `load(repo)` / `registry_path(repo)` |
| `validate_trace.py` | 48 | ja — `DEFAULT_REPO`, via `sys.argv[1]` |
| `check_prd.py` | 43 | ja — `DEFAULT_REPO`, via `sys.argv[1]` |
| `selftest_validator.py` | 22 | **nein** |
| `gen_intake.py` | 19 | **nein** |

Die drei `DEFAULT_REPO`-Fälle sind unkritisch: `run_all.sh` übergibt den aufgelösten
Pfad explizit, der Default kommt nie zum Tragen.

`selftest_validator.py:22` und `gen_intake.py:19` sind **nicht** überschreibbar — kein
`argv`, kein `environ`. Sie wurden auftragsgemäß byte-identisch kopiert und **nicht**
angefasst. Folge, am Klon gemessen statt vermutet:

```
HERE  = …/clone-test/RevyrClone/scripts/validation
REPO  = /Users/vincentschnetzer/Documents/Run&Bike
REPO points at clone? False
```

`selftest_validator.py` nimmt in einem Klon also die **Werkzeuge des Klons**, prüft sie
aber gegen die **Dokumente des Originalrepositorys** — lautlos, ohne Fehlermeldung.
Solange Klon und Original denselben `docs/`-Stand haben, fällt das nicht auf; sobald
sie auseinanderlaufen, misst der Selbsttest etwas anderes, als der Aufrufer annimmt.
`gen_intake.py` schriebe entsprechend in das Originalrepository — es wird von
`run_all.sh` nicht ausgeführt.

**Die Aussage „`run_all.sh` funktioniert aus jedem Klon" gilt daher mit dieser
Einschränkung**, nicht uneingeschränkt. Sie ist nicht geglättet worden, weil die
Korrektur eine Änderung an eingefrorenen Werkzeugen wäre — und die war nicht
beauftragt.

## Messfehler im eigenen Lauf

Offengelegt, weil er das Ergebnis verfälscht hätte: Eine erste Messung der Exit-Codes
von `validate_trace.py` und `check_prd.py` ergab `rc=2` und wurde als Auffälligkeit
notiert. Ursache war eine **unquotierte Variable im Messkommando** (`python3 $c` mit
einem Pfad, der `&` enthält) — also ein Fehler der Messung, nicht der Werkzeuge. Bei
korrekt quotiertem Aufruf liefern beide `rc=0` bei `FAILS: 0` bzw. `FAILURES: 0`. Genau
davor warnt die Repo-Regel zum kaufmännischen Und.

Zweite Beobachtung, ebenfalls nur gemeldet: `validate_trace.py` schreibt seinen
gesamten Bericht nach **stderr**, nicht nach stdout. Wer nur stdout abgreift, sieht von
diesem Werkzeug nichts. `run_all.sh` fängt beide Ströme.

## Umgebung

Gemessen mit **Python 3.14.2** (macOS, Darwin 25.5.0). Keine Drittbibliothek nötig —
alle Importe der Kette sind Standardbibliothek; per Import-Durchsicht aller zwölf
Werkzeuge geprüft. `validate_schema.py` bringt seinen eigenen JSON-Schema-Prüfer mit,
weil `jsonschema` in dieser Umgebung nicht installiert ist, und meldet nicht
unterstützte Schlüsselwörter ausdrücklich (`x_schema_change_log`), statt sie
stillschweigend zu übergehen.
