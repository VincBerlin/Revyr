# EVIDENCE LEDGER

Status: empty-template-for-implementation  
Ergänzt: 2026-07-20 (**Runde 6**: erster Eintrag mit tatsächlich erbrachten Nachweisen — sie
betreffen ausschließlich **Quellenintegrität und Werkzeugkette**, kein Requirement, kein Gate.
Siehe „[2026-07-20] Governance / Werkzeugkette" unten)  
Ergänzt: 2026-07-20 (kanonische Trennung **EV-008 / EV-039**; Nachweisbedingungen für die beiden
CAN-140-Nachfolger **EV-043** und **EV-044** ergänzt; **EV-040** als `deprecated` nachgezogen;
`blocking`-Hilfsfeld aus dem NFR-Abschnitt [N8] entfernt — der `NFR-`Raum führt kein `blocking`;
Gate-Summary A0 und A2 nachgezogen)  
Ergänzt: 2026-07-19 (A0-Routing-Evidenzliste; Platzhalter-Notation korrigiert;
NFR-Nachweisbedingungen NFR-001 … NFR-008 aus dem NFR-Audit ergänzt;
unzulässiger `status`-Wert `DESIGN-RESOLVED / EVIDENCE-PENDING` für CONTRA-006 beseitigt;
Nachweisbedingungen für **GPX-Export (EV-039)**, **Accessibility-Audit WCAG 2.2 AA (EV-037)** und
**CAN-130-Telemetrie (EV-041)** ergänzt; entfallenes Feld `blocking_scope` auf `blocked_gates` +
`blocked_activities` umgestellt; deprecateter Verweis EV-014 → EV-037 nachgezogen)

**Kein Nachweis dieses Dokuments ist erbracht.** Zum Stand 2026-07-19 existiert kein Code, kein
Build, keine AWS-Ressource, keine Instrumentierung und kein ausgeführter Test. Kein Gate-Status
wurde verändert; alle stehen unverändert auf `pending`. Nichts ist auf `verified` gesetzt.

**Präzisierung 2026-07-20 (Runde 6) — der Satz oben bleibt für Produktnachweise gültig.** Am
2026-07-20 sind erstmals Prüfungen **tatsächlich ausgeführt** worden: Prüfsummenvergleich der
vier Quelldokumente, Äquivalenzvergleich fünf geänderter Werkzeugkopien und ein vollständiger
Lauf der Validatorkette. Sie betreffen **ausschließlich Quellenintegrität und Werkzeugkette** und
sind unten als eigener Eintrag geführt. **Für das Produkt ändert sich nichts:** es existiert
weiterhin kein Code, kein Build, keine AWS-Ressource, keine Instrumentierung und kein
Gerätetest; kein `EV-`Nachweis ist dadurch erbracht, kein Requirement erfüllt, kein Gate-Status
verändert.

**Semantik von `evidence_status`** (projektweit, Nutzerentscheidung 2026-07-19):
`not-planned` = es existiert noch kein Messkonzept · `planned` = Metrik, Berechnung und Gate sind
definiert, **Instrumentierung fehlt** · `pending` = **Instrumentierung implementiert**, Messdaten
oder Messfenster fehlen · `verified` = Zielwert mit ausreichender, dokumentierter Evidenz geprüft ·
`not-required` = requirement-spezifisch begründete Nichtanwendbarkeit, **nie pauschal** ·
`failed` = Nachweis versucht und gescheitert · `blocked` = Nachweis durch einen anderen offenen
Punkt versperrt. Die Grenze zwischen `planned` und `pending` ist die **Instrumentierung**, nicht
die Absicht — solange kein Code existiert, steht ein Eintrag höchstens auf `planned`.

## Usage Rule

Kein Requirement, Task oder Gate erhält `done`, bevor ein Eintrag mit konkreten Nachweisen
existiert. Neueste Einträge stehen oben.

**Ein nicht ausgeführter Test ist nicht bestanden.** Er wird als `nicht erbracht` geführt,
nicht als `n.a.`, nicht als `ok` und nicht durch eine Plausibilitätsannahme ersetzt. Run und
Bike werden getrennt verifiziert.

## Eintragsvorlage

> **Hinweis zur Notation (geändert 2026-07-19).** Die Vorlage führte zuvor `REQ-000`, `AC-000`
> und `EV-000` als Beispielwerte. Das erzeugte drei Phantom-IDs: jede Referenzprüfung meldete
> entweder „unbekannte ID" oder zählte — schlimmer — drei Requirements, die es nicht gibt.
> `docs/ID-REGISTRY.md` §4 führt die drei deshalb als `template-placeholder` und empfiehlt dem
> Owner dieser Datei ausdrücklich die Umstellung auf eine Nicht-ID-Notation. Das ist hiermit
> umgesetzt: die Vorlage verwendet spitze Klammern, die kein gültiges ID-Format sind
> (`<PREFIX>-<3 Ziffern>`) und daher von keiner Prüfung als ID gelesen werden können.
>
> **Nachzug in der Registry erforderlich (Registry-Owner, Registry ist eingefroren):**
> Registry §4 beschreibt weiterhin, diese Datei führe `REQ-000`/`AC-000`/`EV-000` als
> Beispielwerte. Nach dieser Änderung trifft das nicht mehr zu. Die drei Einträge dürfen
> **nicht** gelöscht werden (Regel 6: Nummern bleiben belegt), sind aber als „historisch,
> Vorlage inzwischen umgestellt" zu kennzeichnen. Dieser Schritt ändert die Registry nicht.

## [YYYY-MM-DD] &lt;Task / Gate&gt; — &lt;Titel&gt;

| Feld | Wert |
|---|---|
| Requirement IDs | &lt;REQ-ID&gt; |
| Acceptance Criteria | &lt;AC-ID&gt; |
| Evidence IDs | &lt;EV-ID&gt; |
| Commit / Build | MISSING |
| Unit / Property Tests | MISSING |
| Integration / E2E | MISSING |
| iOS Gerät + OS | MISSING |
| Android Gerät + OS | MISSING |
| Run geprüft | MISSING |
| Bike geprüft | MISSING |
| GPS Referenz Soll/Ist | MISSING / n.a. |
| Background / App-Kill | MISSING / n.a. |
| Batterie Start/Ende/Dauer | MISSING / n.a. |
| Accessibility | MISSING / n.a. |
| Privacy / Claims Review | MISSING / n.a. |
| Result | pending |
| Open Findings | MISSING |

## [2026-07-20] Governance / Werkzeugkette — Überführung der Quellen und Validatoren ins Repository

**Neuester Eintrag.** Er steht hier, weil die Usage Rule „neueste Einträge oben" verlangt; er ist
der **erste** Eintrag dieses Ledgers, der tatsächlich erbrachte Nachweise führt.

> ⚠️ **Dies ist kein Requirement-Nachweis.** Der Eintrag belegt Quellenintegrität und
> Werkzeugreproduzierbarkeit — nicht die Erfüllung einer Anforderung. Er ist **keine Freigabe**,
> **kein Gate-Verdikt** und **kein Beleg für irgendeine Produktaussage**. Gesamtstatus bleibt
> `BLOCKED_TRACEABILITY`.

| Feld | Wert |
|---|---|
| Requirement IDs | **keine** — governance-/tooling-bezogen, an kein REQ gebunden |
| Acceptance Criteria | **keine** |
| Evidence IDs | **keine — BLOCKER.** `docs/ID-REGISTRY.md` ist eingefroren und reserviert keine EV-ID über EV-044 hinaus; EV-001…EV-036 sind 1:1 an REQ-001…REQ-036 gebunden. Nach Registry-Regel 3 wird eine fehlende ID **gemeldet, nicht erfunden**. Dieser Eintrag hat deshalb **keine EV-ID** und ist über sein Datum zu referenzieren |
| Commit / Build | **MISSING** — das Repository steht nicht unter Versionskontrolle (am 2026-07-20 gemessen: kein `.git`-Verzeichnis). Es gibt keinen Commit, auf den verwiesen werden könnte |
| Unit / Property Tests | **MISSING** (Produktcode existiert nicht). Ausgeführt wurde die **Validatorkette**, nicht eine Testsuite — siehe „Was erbracht wurde", Punkt 3 |
| Integration / E2E | **MISSING** |
| iOS Gerät + OS | **MISSING** — kein Gerätetest, keine Referenzgeräte benannt |
| Android Gerät + OS | **MISSING** — kein Gerätetest, keine Referenzgeräte benannt |
| Run geprüft | **MISSING** |
| Bike geprüft | **MISSING** |
| GPS Referenz Soll/Ist | **MISSING** |
| Background / App-Kill | **MISSING** |
| Batterie Start/Ende/Dauer | **MISSING** |
| Accessibility | **MISSING** |
| Privacy / Claims Review | **MISSING** |
| `wired-in-prod?` | **no** |
| `evidence-class` | **none** |
| Result | **pending** — kein Gate-Status verändert; alle Gates stehen unverändert auf `pending` |
| Open Findings | siehe „Was ausdrücklich NICHT nachgewiesen ist" unten (8 Punkte) |

### Was erbracht wurde — drei Nachweise, einzeln

**1. Prüfsummengleichheit der vier Quelldokumente.** `SRC-001`…`SRC-004` liegen zusätzlich unter
`docs/sources/`. Verglichen wurden je drei Werte: Original unter `~/Desktop/docs/`, Repo-Kopie und
Soll-Summe aus `docs/SOURCE-MAP.md` §1.1. **Alle drei sind je Quelle identisch**, Bytegrößen
ebenfalls (24.585 / 10.525 / 61.117 / 78.355). Der Kopiervorgang hat den Inhalt nicht angetastet;
**Zeilennummern sind gegen beide Fundorte stabil**, weshalb alle Fundstellenangaben der
Belegprüfung gültig bleiben. Vollständige Tabelle in `docs/SOURCE-MAP.md` §1.6 und
`scripts/validation/HASHES.md`.

**2. Äquivalenz der geänderten Werkzeugkopien.** Von 15 übernommenen Werkzeug- und Datendateien
sind **zehn byte-identisch** (`cmp` bestätigt). **Fünf** wurden geändert — ausschließlich das
hartkodierte Repo-Pfad-Literal, ersetzt durch Auflösung aus dem Skriptort bzw. `REVYR_REPO`:
`xcheck.py`, `verify.py`, `verify_canvas.py`, `oq_check.py`, `AUDIT_points.py`. Für alle fünf ist
byte-genau (`cmp -s`, nicht textnormalisiert) nachgewiesen: **stdout SAME, stderr SAME,
Exit-Code gleich**. Der Exit-Code war nicht Teil des Auftrags, wurde aber miterhoben, weil gleiche
Ausgabe bei ungleichem Exit-Code die Gleichwertigkeit widerlegt hätte. Es gab **keine**
Abweichung. Belege in `scripts/validation/EQUIVALENCE.md` (inklusive vollständiger Diffs).

**3. Ausgeführter Lauf der Validatorkette.** `scripts/validation/run_all.sh`, Python 3.14.2,
Laufzeit **7:14 min**, Exit-Code **1**, Ergebnis **`PASS=6  FAIL=4  INFO/SKIP=1`**:

| Werkzeug | Verdikt | | Werkzeug | Verdikt |
|---|---|---|---|---|
| `registry_model.py` | PASS | | `verify.py` | **FAIL** (`FAILS=1`) |
| `validate_schema.py` | PASS | | `verify_canvas.py` | **FAIL** (rc=1) |
| `validate_intake.py` | **FAIL** (rc=1) | | `oq_check.py` | **FAIL** (rc=1) |
| `validate_trace.py` | PASS | | `AUDIT_points.py` | INFO (kein Bestehensbegriff) |
| `check_prd.py` | PASS | | `selftest_validator.py` | PASS |
| `xcheck.py` | PASS (alle Abweichungslisten leer) | | | |

**Exit-Code 1 ist der erwartete Stand, kein Regressionsbefund.** Drei der vier FAILs sind
aktenkundige **Werkzeugdefekte** und reproduzieren in der Repo-Kopie unverändert — genau das ist
der Zweck des Äquivalenznachweises: `verify.py` vergleicht gegen ein veraltetes hartkodiertes
`claim`-Literal (Dokument aktuell, Werkzeug falsch), `verify_canvas.py` honoriert maskierte Pipes
nicht und meldet `TABLE@187` falsch, `oq_check.py` kennt `OQ-012`…`OQ-016` nicht und wirft sie in
`UNCLASSIFIED` — der Folgebefund „eine Entscheidung wird von mehr als einer OQ-ID bezeichnet" ist
daraus abgeleitet und **nicht belastbar**. Keiner der drei wurde korrigiert (Freeze).

### Was ausdrücklich NICHT nachgewiesen ist

1. **Kein Code, kein Build, kein Gerät.** Es existiert kein Produktcode, keine
   AWS-Ressource, keine Instrumentierung, kein iOS- und kein Android-Gerätetest. **Run und Bike
   sind nicht — auch nicht teilweise — verifiziert.** `wired-in-prod? = no`,
   `evidence-class = none`.
2. **Kein Verdikt der Belegprüfung ist besser geworden.** Die Existenz einer Quelle im Repository
   belegt so wenig eine konkrete Aussage wie ihre Existenz auf dem Desktop. Es wurde **keine
   Zelle hochgestuft**; die Nachprüfung derselben Runde hat vier zuvor als BELEGT geführte Zellen
   **herabgestuft** (CAN-119, VIS-003, CAN-024 → TEILBELEGT; CAN-109 → UNBELEGT).
3. **Ein grüner Lauf wäre kein unabhängiger Nachweis.** Die Werkzeuge sind in diesem Vorhaben
   selbst verfasst; sie prüfen Artefakte desselben Vorhabens. Der tatsächliche Lauf endet
   ohnehin mit Exit-Code 1.
4. **Die Äquivalenz belegt nicht, dass die Werkzeuge korrekt prüfen** — nur, dass die Kopie
   denselben Defekt unverändert reproduziert. Sie ist zudem **an genau diesem Ort gemessen**: sie
   sagt nichts darüber, ob die Werkzeuge anderswo gleich liefen.
5. **Das Repository steht nicht unter Versionskontrolle.** „Im Repository" heißt **nicht**
   „versioniert"; eine Kopie in einem unversionierten Verzeichnis kann spurlos geändert werden.
   Einzige Integritätsanker sind die SHA-256-Summen. Das ist eine echte Einschränkung, keine
   Formalie — und der Grund, warum die Originale weiter mitgeführt werden.
6. **Zwei Werkzeuge folgen einem Klon nicht.** `selftest_validator.py:22` und `gen_intake.py:19`
   sind **nicht** pfad-überschreibbar (kein `argv`, kein `environ`). Am Klon gemessen nimmt
   `selftest_validator.py` dort die Werkzeuge des Klons, prüft sie aber **lautlos gegen die
   Dokumente des Originalrepositorys**. Die Zusage „läuft aus jedem Klon" gilt nur mit dieser
   Einschränkung. Beide wurden auftragsgemäß byte-identisch kopiert und **nicht** angefasst.
7. **`scripts/validation/src-verification.json` ist inhaltlich veraltet.** Byte-identisch
   übernommen; es führt weiterhin `109 BELEGT / 17 TEILBELEGT / 5 UNBELEGT` statt `105 / 20 / 6`
   und in `quellen[*].pfad` die Desktop-Pfade. Es **widerspricht** der Verdikttabelle in
   `SOURCE-MAP.md` §1.3. **BLOCKER**, hier nicht behoben.
8. **Zwei Bezugsdokumente sind nicht überführt.** `scratchpad/semantic-review.md` (Grundlage der
   23 `trägt-teilweise`) und `scratchpad/id-migration.json` stehen auf der Ausschlussliste in
   `scripts/validation/HASHES.md`. Jede Zahl und jede Regel, die sich auf sie stützt — namentlich
   die Wesentlichkeitsregel im Decision Log — bleibt **nicht referenzierbar belegt**.

**Registry §8 Punkt 13 und Punkt 33 bleiben OFFEN.** Dieser Eintrag entkräftet zwar die bisherige
Begründung ihres Offenbleibens („kein Validator ausgeführt, kein Ergebnis reproduziert, keine
Äquivalenz geprüft" — Registry §13.2), aber ob sie dadurch schließen, entscheidet der Owner der
eingefrorenen Registry, **nicht dieser Eintrag**.

**Kein Gate-Status wurde verändert.** P0, A0, A1, A2, B, C, D und E stehen unverändert auf
`pending` (Gate Summary am Dateiende). Freigegeben ist ausschließlich der Start von **P0-02** und
**P0-03** als technische Spikes — beide sind **nicht abnehmbar** (P0-03 zusätzlich über
**EV-042 = `blocked`** strukturell blockiert). Einzelheiten in
`docs/decisions/decision-log.md`, Abschnitt „Was dieser Lauf freigibt — und was ausdrücklich
nicht".

## Geforderte Evidence: A0-Routing-Proxy (DEC-013 / CONTRA-006)

**Sämtliche Nachweise dieser Liste sind offen — `nicht erbracht`.** Es wurde in diesem Lauf
kein Code geschrieben, kein Verzeichnis `infra/routing-proxy/` angelegt, keine AWS-Ressource
erzeugt und kein Test ausgeführt. Diese Liste ist eine **Anforderung an künftige Nachweise**,
kein Nachweis.

CONTRA-006 trägt nach dem Statusmodell (Registry §3.1, Ledger `docs/decisions/decision-log.md`)
`status = resolved`, `evidence_status = pending`, `blocked_gates = [A0]`,
`blocked_activities = [field-test, release]`, `evidence_gate = A0`, `blocking = true`
(berechnet: `A0` ∈ `blocked_gates`). Das frühere Feld `blocking_scope` ist projektweit entfallen;
es mischte Gates und Tätigkeiten in einer Liste und lieferte für jeden gegateten Eintrag
fälschlich `false`. Der frühere Mischwert
`DESIGN-RESOLVED / EVIDENCE-PENDING` ist als `status` unzulässig und hier beseitigt. Die
Entscheidung ist getroffen; der Nachweis ist es nicht. CONTRA-006 blockiert die
A0-Routing-Implementierung weiterhin, bis die als `blockierend` markierten Zeilen erbracht sind.

> **BLOCKER — ID-Vergabe nicht möglich.** `docs/ID-REGISTRY.md` ist ab Phase 2 eingefroren und
> reserviert **keine** EV-ID über EV-036 hinaus; EV-001…EV-036 sind 1:1 an REQ-001…REQ-036
> gebunden (Registry §6.7). Nach Registry-Regel 3 meldet ein Agent außerhalb Phase 1 eine
> fehlende ID als BLOCKER, statt sie zu erfinden. Nur zwei bestehende EV-IDs decken Teile
> dieser Liste inhaltlich ab; alle übrigen Zeilen haben **keine EV-ID**. Die Marken (a)…(n)
> sind reine abschnittslokale Lesemarken, **keine IDs**.

| Marke (keine ID) | Geforderter Nachweis | Art des Nachweises | Bestehende EV-ID | Fällig | Result |
|---|---|---|---|---|---|
| (a) | Kein Routing-Provider-Key im gebauten App-Bundle und im Repository | Secret-Scan des Release-Bundles + Repo-Scan, in CI verankert | EV-034 (teilweise: Security-Review) | vor A0-Routing-Implementierung — **blockierend** | nicht erbracht |
| (b) | Request-/Response-Bodies erscheinen nicht in Logs, Traces oder Fehlermeldungen | automatisierter Test gegen die tatsächliche Logausgabe, mit Negativfällen (Latitude, Longitude, Wegpunktliste, Provider-URL, Routengeometrie) | keine | vor A0-Routing-Implementierung — **blockierend** | nicht erbracht |
| (c) | Nur die zulässigen Logfelder werden geschrieben (Request-ID, Zeitstempel, Status, Dauer, Profil, Wegpunktzahl, Fehlerkategorie, Provider-Latenz, Rate-Limit-Ereignis) | Allowlist-Test der Logfelder | keine | vor A0-Routing-Implementierung — **blockierend** | nicht erbracht |
| (d) | Retention 0 für den Koordinaten-Payload: keine Persistenz in Application, Cache oder Analytics | Code- und Infrastruktur-Review + Datenflussdiagramm | EV-034 (teilweise: Datenflussdiagramm) | vor A0-Routing-Implementierung — **blockierend** | nicht erbracht |
| (e) | Technische Logs ermöglichen keine Standortrekonstruktion | manuelle Kontrollprüfung eines realen Logauszugs durch Privacy-Review | keine | vor erstem externem Feldtest — **blockierend** | nicht erbracht |
| (f) | Logaufbewahrung ≤ 7 Tage | Konfigurationsnachweis (Log-Retention-Einstellung) | keine | vor erstem externem Feldtest | nicht erbracht |
| (g) | Rate Limit, Size-Limit, maximale Wegpunktzahl, Timeout und Kill Switch greifen | Negativ-/Lasttest je Kontrolle; zusätzlich Nachweis, dass keine Kontrolle Koordinaten dauerhaft speichert | keine | vor A0-Routing-Implementierung — **blockierend** | nicht erbracht |
| (h) | Fehlerantworten enthalten keine Provider-Secrets, internen URLs, Koordinaten, vollständigen Providerantworten oder Stack Traces | Fehlerfall-Test über alle Fehlerkategorien | keine | vor A0-Routing-Implementierung — **blockierend** | nicht erbracht |
| (i) | Nur HTTPS/TLS; kein unverschlüsselter Endpunkt erreichbar | Endpunkt-Scan | keine | vor erstem externem Feldtest — **blockierend** | nicht erbracht |
| (j) | Secrets in AWS Secrets Manager oder verschlüsselter Lambda-Env, restriktive IAM, Rotation und Widerruf erprobt | Infrastruktur-Review + durchgeführter Rotationstest | keine | vor erstem externem Feldtest | nicht erbracht |
| (k) | Lambda und API Gateway laufen in `eu-central-1` | Infrastruktur-Nachweis (Region der deployten Ressourcen) | keine | vor erstem externem Feldtest | nicht erbracht |
| (l) | Providername und Providerantwort erscheinen nicht in Domain- oder UI-Code; App kennt nur Proxy-Basis-URL, `RoutingPort` und `RoutingClient` | statische Prüfung von `src/domain/` und `src/app/` gegen Provider-Bezeichner | keine | vor A0-Routing-Implementierung — **blockierend** | nicht erbracht |
| (m) | Profilübersetzung `run → foot-walking` und `ride → cycling-regular` liegt im Proxy und ist je Sportart verifiziert | Unit-Test im Proxy + reale Routenszenarien **getrennt für Run und Bike** | EV-006 (Routing-Service-Tests, zehn reale Routenszenarien je Sport) | vor A0-Routing-Implementierung — **blockierend** | nicht erbracht |
| (n) | IP-Adressen werden nicht dauerhaft gespeichert und nicht mit Routenanfragen verknüpft | Konfigurations- und Code-Review, separat dokumentiert | keine | vor erstem externem Feldtest — **blockierend** | nicht erbracht |

### Rechts- und Transparenznachweise (Dokumentnachweis, kein Test)

Diese Zeilen sind **vor dem ersten externen Feldtest** zu erbringen und korrespondieren 1:1 mit
den offenen Punkten (a)…(g) in `docs/decisions/open-questions.md`. Sie haben ebenfalls keine
EV-ID.

| Marke (keine ID) | Geforderter Nachweis | Result |
|---|---|---|
| (o) | Verarbeitungsregion des Routinganbieters dokumentiert | nicht erbracht |
| (p) | Feststellung, ob Daten den EWR verlassen; Sprachregelung für „EU-Proxy" entsprechend angepasst | nicht erbracht |
| (q) | Unterauftragsverarbeiter benannt | nicht erbracht |
| (r) | Transfergrundlage dokumentiert | nicht erbracht |
| (s) | Auftragsverarbeitungsvertrag geschlossen, inkl. Rollenverteilung Controller/Processor, Provider-Retention, Ausschluss eigener Werbe-/Profiling-/Trainingszwecke, Lösch- und Sicherheitsregeln | nicht erbracht |
| (t) | Rechtsgrundlage und Betroffeneninformationen vollständig (Verantwortlicher, Zweck, Empfänger, Übermittlungsregionen, Speicherdauer, Betroffenenrechte, Datenschutzkontakt) | nicht erbracht |
| (u) | Datenschutzerklärung mit dem verbindlichen Routing-Absatz veröffentlicht und **vor** Nutzung der Routenplanung erreichbar | nicht erbracht |

**Konsequenz bei Nichterfüllung:** Ein Routinganbieter, der (o)…(s) nicht erfüllt, darf nicht
für produktive oder externe A0-Tests eingesetzt werden. Ohne (t) und (u) wird die Routenplanung
nicht freigeschaltet.

## Offene Evidence aus DEC-011 und DEC-012

Beide Widersprüche sind als **Grundsatzentscheidung** aufgelöst; die Implementierungs-Evidence
steht vollständig aus. Auch hier existiert keine reservierte EV-ID für die neuen Nachweise.

| Marke (keine ID) | Geforderter Nachweis | Bestehende EV-ID | Fällig | Result |
|---|---|---|---|---|
| (v) | Der Server empfängt ausschließlich die in DEC-011 aufgezählten minimierten Plausibilitätssignale — vollständige HF-, Schritt- und Rohsensorverläufe verlassen das Gerät nicht | EV-024, EV-034 (teilweise) | vor Stufe C | nicht erbracht |
| (w) | Fehlende Sensoren führen zu `low-confidence`, nie automatisch zu `rejected`; Teleport und physikalisch unmögliche Geschwindigkeit führen zu `review-required`/`rejected` | EV-024 (Betrugs-/Grenzfall-Fixtures, False-Positive-Review) | vor Stufe C | nicht erbracht |
| (x) | Accountlöschung entfernt alle in DEC-012 aufgezählten personenbezogenen Daten und Identitätszuordnungen | EV-017 (Löschungsnachweis), EV-034 | vor Stufe B | nicht erbracht |
| (y) | Überlebende historische Team-/Season-Daten sind wirksam anonymisiert; keine Rückführung auf die gelöschte Person möglich — sonst gelöscht | EV-027 (teilweise) | vor Stufe D | nicht erbracht |
| (z) | Datenmodell trennt Identität und historische Aggregate technisch | keine | **vor Finalisierung des Datenbankschemas** | nicht erbracht |

**Hinweis zu EV-027.** EV-027 lautet „Zwei-Season-Integrationstest und
Unveränderlichkeitsprüfung". Der Begriff „Unveränderlichkeit" ist durch DEC-012 überholt: zu
prüfen ist künftig „nach Finalisierung fachlich unveränderbar, außer aufgrund Löschung,
Anonymisierung oder rechtlicher Korrektur". Die Umformulierung von EV-027 liegt beim Owner des
PRD (`canonical_file` laut Registry §6.7) und ist hier nicht vorgenommen.

## Geforderte Evidence: Verlauf/Detailansicht, GPX-Export, Accessibility-Audit und CAN-130-Telemetrie

**Sämtliche Nachweise dieses Abschnitts sind offen — `nicht erbracht`.** Es existiert kein Code,
kein Build, keine Instrumentierung, kein Gerätetest und keine Messreihe. Kein Test dieses
Abschnitts wurde ausgeführt; keiner ist bestanden. Dieser Abschnitt ist eine **Anforderung an
künftige Nachweise**, kein Nachweis.

> **Erstmals mit echten EV-IDs.** Anders als die Abschnitte oben verwendet dieser Abschnitt
> reservierte EV-IDs: **EV-037** (Accessibility), **EV-039** (GPX-Export) und **EV-041**
> (CAN-130-Kennzahl) wurden in Phase 1, Auftau-Schritt 2 (2026-07-19) in `docs/ID-REGISTRY.md`
> reserviert. Dieser Schritt vergibt **keine** ID.
>
> **Nachzug ausstehend (Registry §7.4.4).** `canonical_file` dieser EV-IDs ist
> `docs/prd/revyr-endurance-platform.prd.md`; dort sind sie noch **nicht** eingetragen. Sie sind
> als zulässige Waisen im Nachzugsfenster geführt — bekannt und terminiert, nicht übersehen. Der
> PRD-Owner zieht nach.

### Kanonische Trennung EV-008 / EV-039 (Nutzerentscheidung 2026-07-20)

**Verbindlich, und in beide Richtungen zu prüfen:**

| ID | Gegenstand — ausschließlich | Enthält ausdrücklich **nicht** |
|---|---|---|
| **EV-008** | Verlauf und Detailansicht lokal gespeicherter Aktivitäten (REQ-008 / AC-008 / CAN-138) | GPX-, Export-, Portabilitäts- oder Fremd-App-Nachweis |
| **EV-039** | GPX-Kompatibilitäts- und Exportnachweis (REQ-039 / AC-039 / CAN-139) | Verlauf und Detailansicht |

**Wer einen GPX-Nachweis unter EV-008 findet oder einen Verlaufsnachweis unter EV-039, hat einen
Validierungsfehler gefunden** — keinen Grenzfall.

**Woher der Defekt kam.** `docs/ID-REGISTRY.md` führte EV-008 bis zum 2026-07-20 mit dem Alttitel
„Repository-, UI- und **GPX-Kompatibilitätstest**", obwohl das PRD den GPX-Anteil bereits am
2026-07-19 nach EV-039 ausgelagert hatte. Die Registry ist nach §1 die kanonische Quelle — die
**veraltete** Definition hätte deshalb bei jeder Prüfung gewonnen und denselben Nachweis unter
zwei IDs geführt. Beide IDs existierten, beide lasen sich plausibel, und keine Existenzprüfung
hätte etwas gemeldet. Die Überlappung lief also nicht über das PRD, sondern über die Registry.

### EV-008 — Verlauf und Detailansicht (REQ-008 / AC-008 / CAN-138), Release Gate A0

Kanonischer Umfang von CAN-138 (Nutzerentscheidung 2026-07-20): „Nutzer können lokal gespeicherte
Run- und Bike-Aktivitäten in einem Verlauf anzeigen und eine ausgewählte Aktivität mit Route,
Dauer, Distanz und sportartspezifischer Kernmetrik in einer Detailansicht öffnen."

**CAN-138 ist ausdrücklich NICHT geteilt worden** — Verlauf und Detailansicht gehören zum selben
A0-Nutzerfluss, werden gemeinsam durch REQ-008 ausgeliefert und teilen Gate und Datenmodell. Für
diesen Ledger folgt daraus: **EV-008 ist ein Nachweis, nicht zwei.** Ein Verlauf ohne öffenbare
Detailansicht erfüllt ihn nicht.

`evidence_status: not-planned` · `release_gate: A0` · Owner: **MISSING (OQ-002)**

| Marke (keine ID) | Geforderter Nachweis | Art des Nachweises | Result |
|---|---|---|---|
| [H1] | Abgeschlossene **Run**-Aktivitäten erscheinen im Verlauf | Repository- und UI-Test + reale Aktivität auf realem Gerät | nicht erbracht |
| [H2] | Abgeschlossene **Bike**-Aktivitäten erscheinen im Verlauf | Repository- und UI-Test + reale Aktivität auf realem Gerät | nicht erbracht |
| [H3] | Die Detailansicht zeigt **Route, Dauer und Distanz** der ausgewählten Aktivität | UI-Verhaltenstest gegen die gespeicherten Werte, nicht gegen neu berechnete | nicht erbracht |
| [H4] | Die **sportartspezifische Kernmetrik** ist korrekt: Run zeigt Pace (min/km), Bike zeigt Geschwindigkeit (km/h) | Darstellungstest je Sportart + Negativtest, dass keine Sportart die Metrik der anderen zeigt | nicht erbracht |
| [H5] | Verlauf und Detailansicht überstehen einen **App-Neustart** | Persistenztest über Prozessende hinweg | nicht erbracht |
| [H6] | **Beschädigte oder unbekannte** Aktivitätsdaten führen zu einem kontrollierten Fehler | Negativtest mit defekten und teilweise geschriebenen Fixtures — kein Absturz, keine stille Leeransicht | nicht erbracht |

**Run und Bike werden getrennt verifiziert.** [H1] und [H2] sind zwei Nachweise; [H4] ist der Test,
der die Sportart-Duplizierung ausschließt.

**Ausdrücklich nicht Teil von EV-008:** GPX-Export ([G1]…[G8], EV-039), Wiederverwendung einer
gespeicherten Route ([RU1]…[RU6], EV-043) und Aktivitätsvergleich ([VG1]…[VG6], EV-044). Alle drei
sind **A2**, EV-008 ist **A0**.

**MISSING** — Gerätematrix und OS-Versionen (**OQ-003**). **BLOCKER** — Owner (**OQ-002**).

### EV-039 — GPX-Export (REQ-039 / AC-039), Release Gate A2

Neue atomare Capability aus der Nutzerentscheidung vom 2026-07-19: „Nutzer können eine
abgeschlossene Run- oder Bike-Aktivität als standardkonforme GPX-Datei exportieren und in einer
kompatiblen Fremdanwendung öffnen." REQ-034 (Datenminimierung, Nutzerkontrolle, Portabilität)
bleibt eine **sekundäre** Constraint-Verknüpfung — REQ-034 allein erfüllt den GPX-Export **nicht**.

> **BEFUND 2026-07-20 — der kanonische Canvas-Wortlaut nennt die Fremd-App-Klausel nicht mehr.**
> CAN-139 lautet seit der Nutzerentscheidung vom 2026-07-20: „Nutzer behalten Kontrolle über ihre
> aufgezeichneten Aktivitäten und können eine abgeschlossene Run- oder Bike-Aktivität als
> standardkonforme GPX-Datei exportieren, **ohne sie veröffentlichen oder mit anderen Nutzern
> teilen zu müssen**." Die Klausel „und in einer kompatiblen Fremdanwendung öffnen" ist damit
> **aus dem Wortlaut entfallen** — AC-039 (d) und der Nachweis **[G4]** verlangen sie weiterhin.
> Der Bezug ist über „**standardkonforme** GPX-Datei" tragbar (Interoperabilität ist die operative
> Probe auf Standardkonformität), aber **nicht mehr wörtlich belegt**. Das wird hier offengelegt
> statt stillschweigend gedeckt: [G4] bleibt gefordert, seine Herleitung ist eine Auslegung.
> Zu entscheiden vom Nutzer — entweder trägt der kanonische Wortlaut die Klausel wieder
> ausdrücklich, oder [G4] und AC-039 (d) entfallen. **Beides wird hier nicht gewählt.**
> Der neu hinzugekommene Halbsatz „ohne veröffentlichen oder teilen" ist dagegen bereits durch
> **[G8]** abgedeckt.

`evidence_status: not-planned` · `blocked_gates: [A2]` · fällig **spätestens vor dem öffentlichen
v1.0-Release** · Owner: **MISSING (OQ-002)**

| Marke (keine ID) | Geforderter Nachweis | Art des Nachweises | Result |
|---|---|---|---|
| [G1] | GPX-Datei wird für eine abgeschlossene **Run**-Aktivität erzeugt | Integrationstest + reale Aktivität auf realem Gerät | nicht erbracht |
| [G2] | GPX-Datei wird für eine abgeschlossene **Bike**-Aktivität erzeugt | Integrationstest + reale Aktivität auf realem Gerät | nicht erbracht |
| [G3] | Zeitstempel und Koordinatenreihenfolge sind korrekt | Schema- und Reihenfolgeprüfung gegen die GPX-Spezifikation, mit Negativfällen | nicht erbracht |
| [G4] | Datei ist in **mindestens einer definierten** kompatiblen Fremdanwendung öffenbar | manueller Öffnungstest in der festgelegten Referenz-App | nicht erbracht — **BLOCKER, nicht prüfbar**: die Referenz-App ist nicht festgelegt (**OQ-016**). Es wird keine App geraten |
| [G5] | Es werden **keine Health-Daten** unbeabsichtigt exportiert | Feld-Allowlist-Test der erzeugten Datei, mit Negativfällen (HF, Schritte, Health-Metriken) | nicht erbracht |
| [G6] | Der Nutzer sieht **vor** dem Export, welche Daten enthalten sind | UI-Verhaltenstest des Export-Screens | nicht erbracht |
| [G7] | Fehlende oder beschädigte Trackdaten führen zu einem **kontrollierten Fehler** | Negativtest mit defekten und unvollständigen Fixtures — kein Absturz, keine Teil-Datei ohne Hinweis | nicht erbracht |
| [G8] | Export funktioniert **ohne** Veröffentlichung oder Social-Freigabe | Test bei deaktivierter Social-Funktion; der Export darf keine Backend-Interaktion voraussetzen | nicht erbracht |

**Run und Bike werden getrennt verifiziert.** [G1] und [G2] sind zwei Nachweise, nicht einer; ein
Lauf darf nicht auf die andere Sportart übertragen werden.

**MISSING** — Gerätematrix und OS-Versionen für [G1], [G2] und [G4] (**OQ-003**). **MISSING** —
ob [G4] je Plattform (iOS und Android) zu erbringen ist, ist nicht festgelegt.

### EV-037 — Accessibility-Audit WCAG 2.2 AA (REQ-037 / AC-037 / CAN-099)

Aus der Nutzerentscheidung vom 2026-07-19: CAN-099 ist **ausschließlich** Accessibility. „Die
mobile Anwendung und alle nutzbaren Web-Auskopplungen erfüllen WCAG 2.2 AA. Schriftgrößen,
Screenreader, Fokusführung, Kontraste und Bedienflächen werden auf iOS und Android nachgewiesen.
Farbe ist niemals der einzige Informationsträger." Das monochrome Designsystem ist **nicht** Teil
dieses Nachweises — es ist REQ-038 / EV-038 (CAN-141).

`measurement_type: COMPLIANCE_CONTROL` · `evidence_status: not-planned` ·
**Accessibility-Basis ab Gate A0**, **vollständiger Audit spätestens Gate A2 vor dem öffentlichen
Store-Release** · Owner: **MISSING (OQ-002)**

| Marke (keine ID) | Geforderter Nachweis | Art des Nachweises | Fällig | Result |
|---|---|---|---|---|
| [ACC1] | WCAG-2.2-AA-Audit bestanden | dokumentierter Audit gegen die Erfolgskriterien der Fassung **2.2 AA** | vor A2 — **blockierend für den Store-Release** | nicht erbracht |
| [ACC2] | Relevante Screens mit **VoiceOver** geprüft (iOS) | manueller Screenreader-Durchlauf je Screen, protokolliert | Basis ab A0, vollständig vor A2 | nicht erbracht |
| [ACC3] | Relevante Screens mit **TalkBack** geprüft (Android) | manueller Screenreader-Durchlauf je Screen, protokolliert | Basis ab A0, vollständig vor A2 | nicht erbracht |
| [ACC4] | **Dynamic Type** (iOS) und **Font Scaling** (Android) geprüft | Darstellungstest über die definierten Schriftgrößenstufen, kein Textabschnitt und keine Bedienfläche darf unerreichbar werden | Basis ab A0, vollständig vor A2 | nicht erbracht |
| [ACC5] | **Keine Information ausschließlich durch Farbe** | Zustandsinventar aller farbcodierten Zustände + Prüfung auf zweiten, nicht-farblichen Träger (Text, Form, Symbol, Position); Nullschwelle: 0 rein farbcodierte Zustände | Basis ab A0, vollständig vor A2 | nicht erbracht |
| [ACC6] | **Dokumentierte Kontrastprüfung** | Messung nach dokumentierter Methode, in Light **und** Dark Mode | Basis ab A0, vollständig vor A2 | nicht erbracht |
| [ACC7] | **Fokusführung** und Bedienflächengrößen | Tastatur-/Schalter-Steuerung und Mindestgrößen der Trefferflächen je Plattform | vor A2 | nicht erbracht |

**iOS und Android werden getrennt verifiziert.** [ACC2] und [ACC3] sind zwei Nachweise; VoiceOver
ersetzt TalkBack nicht und umgekehrt.

**Was sich gegenüber dem NFR-Audit geändert hat.** Der Abschnitt [N5] unten führte die
**WCAG-Fassung** als BLOCKER („2.0 AA, 2.1 AA und 2.2 AA haben unterschiedliche
Erfolgskriterien"). Dieser BLOCKER ist durch die Nutzerentscheidung vom 2026-07-19 **geschlossen**:
die Fassung ist **2.2 AA**. Insoweit ist der Zielwert jetzt `EXPLICIT`.

**Was sich ausdrücklich nicht geändert hat.** **MISSING** — die **Rechtsgrundlage der
Verbindlichkeit** ist weiterhin in keinem Artefakt zitiert (kein Verweis auf EAA, BFSG oder eine
Store-Vorgabe). Die Festlegung einer Fassung macht die Norm nicht rechtsverbindlich; beides wird
nicht vermischt. **MISSING** — Screenreader- und Gerätematrix: welche OS-Versionen, welche
Schriftgrößenstufen, welche Kontrastmessmethode (**OQ-003**). **BLOCKER** — Owner (**OQ-002**).

### EV-041 — Berechenbarkeit der CAN-130-Übernahmekennzahl (REQ-019 / AC-041)

AC-019 ist durch die Nutzerentscheidung vom 2026-07-19 in **zwei** Kriterien geteilt. Die
Trennung ist für diesen Ledger tragend, weil die beiden Kriterien **unabhängig** bestehen können:

| Kriterium | Inhalt | Nachweis |
|---|---|---|
| **AC-019** (funktional) | „Ein berechtigter Nutzer kann eine sichtbare Routenempfehlung übernehmen. Die übernommene Route wird in seiner Planung verfügbar, ohne dass private Daten des Empfehlenden offengelegt werden." | EV-019 |
| **AC-041** (Messkriterium) | „Für Gate B kann die Zahl bestätigter Übernahmen je auswertbarer Empfehlung datenschutzkonform, sportartspezifisch und reproduzierbar berechnet werden." | **EV-041** |

**Das funktionale Kriterium kann bestanden sein, während die Produktkennzahl noch keine
ausreichende Stichprobe hat.** Ein Nachweis zu AC-019 ist deshalb **kein** Nachweis zu AC-041 und
umgekehrt.

`evidence_status: planned` — Metrik, Berechnung und zuständiges Gate sind definiert, die
**Instrumentierung fehlt** · `release_gate: B` · `measurement_window`: rollierende 28 Tage ·
`target_or_pass_condition`: **> 1,0** bestätigte Routenübernahmen je auswertbarer Empfehlung ·
`empirical_result`: **MISSING** · `target_source_type`: `EXPLICIT` · Owner: **MISSING (OQ-002)**

| Marke (keine ID) | Geforderter Nachweis | Art des Nachweises | Result |
|---|---|---|---|
| [T1] | Die Kennzahl ist **reproduzierbar** berechenbar: bestätigte Routenübernahmen / auswertbare Routenempfehlungen | Berechnungsspezifikation + Testdatensatz mit erwartetem Ergebnis; zwei unabhängige Läufe auf demselben Datensatz ergeben denselben Wert | nicht erbracht |
| [T2] | Die Nennerdefinition ist implementiert: „auswertbar" nur bei erfolgreicher Veröffentlichung, mindestens einem berechtigten Empfänger, möglicher Sichtbarkeit im Messfenster und ohne Löschung/Blockierung/moderative Verbergung vor möglicher Ausspielung | Abgrenzungstests je Ausschlussgrund, mit Negativfällen | nicht erbracht |
| [T3] | Ausgeschlossen sind: private Empfehlungen ohne berechtigten Empfänger, technisch nicht ausgelieferte, vor Ausspielung gelöschte, durch Blockierung/Moderation vollständig unsichtbare sowie **Test- und Seed-Daten** | Ausschlusstest je Kategorie; Testkonten-Erkennung nachgewiesen | nicht erbracht |
| [T4] | **Getrennte** Ausweisung `run_route_adoptions_per_recommendation` und `bike_route_adoptions_per_recommendation`; ein Gesamtwert darf gezeigt werden, aber **nie anstelle** der getrennten Sportwerte | Auswertungstest je Sportart + Prüfung, dass kein Report nur den Gesamtwert liefert | nicht erbracht |
| [T5] | Mehrfachübernahmen: mehrere Nutzer dürfen dieselbe Empfehlung übernehmen — der Durchschnitt kann **> 1,0** sein; eine Deckelung auf 1 wäre ein Rechenfehler | Rechentest mit Mehrfachübernahmen | nicht erbracht |
| [T6] | **Guardrail-Signale** werden miterhoben: Zahl auswertbarer Empfehlungen · Empfehlungen ohne berechtigten Empfänger · technisch fehlgeschlagene Ausspielungen · mediane Zahl berechtigter Empfänger je Empfehlung · Anteil Empfehlungen mit mindestens einer Übernahme · Übernahmen je 100 berechtigten Ausspielungen (sofern datenschutzkonform messbar) · Run/Bike-Verteilung · Lösch-, Blockierungs- und Moderationsanteil | Vollständigkeitsprüfung der Guardrail-Ausgabe | nicht erbracht |
| [T7] | **Datenschutzbedingt unsichtbare** Empfehlungen werden **separat ausgewiesen** und gehen **nicht** als Gegenprobe in den Nenner ein | Prüfung der Nennerbildung + separater Ausweis; Negativtest, dass sie den Quotienten nicht senken | nicht erbracht |
| [T8] | Die Erhebung hält die Feld-Allowlist ein: zulässig sind pseudonyme `recommendation_id`, pseudonyme `adoption_id`, `sport`, Sichtbarkeitskategorie, grober Zeitstempel/Zeitbucket, Ergebnisstatus, `event_version` | Allowlist-Test der tatsächlich gesendeten Felder, mit Negativfällen | nicht erbracht |
| [T9] | **Unzulässige Felder erscheinen nicht**: GPS-Koordinaten, Routengeometrie, Start-/Zieladresse, Health-Daten, Klarnamen, E-Mail, vollständige Gerätekennungen, öffentliche Analytics-Profile, Werbe-/Cross-Service-Tracking | Negativtest je Kategorie gegen die tatsächliche Ereignisausgabe | nicht erbracht |
| [T10] | **Kein paralleler Standort- oder Verhaltenstracker**; die Kennzahl wird möglichst aus ohnehin nötigen Backend-Ereignissen aggregiert | Architektur-Review + Inventar der erhebenden Komponenten | nicht erbracht |
| [T11] | **Rohroute und GPS-Geometrie werden nie für die Erfolgsmessung verwendet**; gemessen wird das Ereignis „Empfehlung übernommen", nicht die später gelaufene oder gefahrene Strecke | Datenfluss-Review + Negativtest | nicht erbracht |
| [T12] | **Gelöschte Accounts** werden aus den Messdaten entfernt oder wirksam anonymisiert, ohne bereits gebildete Aggregate zu verfälschen | Löschtest über Telemetrie-Rohereignisse; gemeinsam mit EV-017 zu prüfen | nicht erbracht — **blockiert durch OQ-012 Punkt 8** |

**BLOCKER — [T1] … [T12] sind derzeit nicht erbringbar.** **OQ-012** (privacy-minimierte
Telemetrie) ist offen: unentschieden sind Erhebungsort, Event-Metadaten, speicherbare Daten,
Aufbewahrung der Rohereignisse, Aggregationszeitpunkt, Einwilligungsbedarf, Wirkung von
Profil-Privacy/Blockierungen/Löschungen, Löschbehandlung, Owner und Analytics-Lösung. Solange das
offen ist, existiert keine zulässige Instrumentierung.

**BLOCKER — die Bewertung ist zusätzlich ohne OQ-014 nicht abschließbar.** Mindestzahl
auswertbarer Empfehlungen, Mindestzahl berechtigter Empfänger, Mindestdauer des Messfensters,
Behandlung von Testkonten, Umgang mit Mehrfachübernahmen desselben Nutzers, Umgang mit gelöschten
und moderierten Empfehlungen sowie die getrennte Run-/Bike-Auswertung sind **nicht festgelegt**.
**Es wird keine Mindestzahl geraten.**

**Ausdrücklich festgehalten:** EV-041 belegt die **Berechenbarkeit**, nicht die **Zielerreichung**.
Selbst ein vollständig bestandenes [T1] … [T12] ist **kein** Beleg dafür, dass der Zielwert > 1,0
erreicht wird. `empirical_result` bleibt **MISSING**, und **jede Behauptung, CAN-130 sei empirisch
validiert, ist bis zum Schluss von OQ-012 und OQ-014 unzulässig.**

### EV-043 — Wiederverwendung einer gespeicherten Route (REQ-041 / AC-042 / CAN-142), Release Gate A2

**Nachfolger 1 von 2 für das am 2026-07-20 deprecatete EV-040.** Kanonischer Umfang von CAN-142:
„Nutzer können eine gespeicherte Route erneut als Grundlage einer geplanten Run- oder
Bike-Aktivität verwenden."

`evidence_status: not-planned` · `release_gate: A2` · Owner: **MISSING (OQ-002)** ·
**nicht durch OQ-015 blockiert**

| Marke (keine ID) | Geforderter Nachweis | Art des Nachweises | Result |
|---|---|---|---|
| [RU1] | Eine gespeicherte **Run**-Route ist als Grundlage einer neuen geplanten Aktivität auswählbar und startbar | Integrationstest + reale Nutzung auf realem Gerät | nicht erbracht |
| [RU2] | Eine gespeicherte **Bike**-Route ist als Grundlage einer neuen geplanten Aktivität auswählbar und startbar | Integrationstest + reale Nutzung auf realem Gerät | nicht erbracht |
| [RU3] | **Geometrie und Wegpunkte** der geladenen Route stimmen mit der gespeicherten Fassung überein | Abgleich gegen die gespeicherte Fassung, nicht gegen eine neu berechnete Route; mit Negativfall (manipulierter Datensatz) | nicht erbracht |
| [RU4] | Das **sportartspezifische Routingprofil** bleibt beim Laden korrekt (`run → foot-walking`, `ride → cycling-regular`) | Vertragstest gegen den Routing-Proxy; Negativtest, dass eine Run-Route nicht als Bike-Route geladen wird | nicht erbracht |
| [RU5] | Eine **gelöschte oder beschädigte** gespeicherte Route führt zu einem kontrollierten Fehler | Negativtest — kein Absturz und **kein stiller Leerstart** einer Aktivität ohne Route | nicht erbracht |
| [RU6] | Die Wiederverwendung setzt **keine Veröffentlichung und keine Backend-Interaktion** voraus (außer dem Routing-Proxy) | Test bei deaktivierter Social-Funktion | nicht erbracht |

**Run und Bike werden getrennt verifiziert.** [RU1] und [RU2] sind zwei Nachweise.

**Warum dieser Nachweis von EV-044 getrennt ist.** [RU1]…[RU6] sind **heute vollständig
spezifizierbar** — jeder Punkt hat eine Pass-Bedingung, die ohne offene Produktentscheidung
prüfbar ist. Genau das ist der operative Grund für die Teilung von EV-040: eine gemeinsame ID
hätte diesen erbringbaren Nachweis an den blockierten Vergleichsnachweis gekettet.

**MISSING** — Gerätematrix und OS-Versionen (**OQ-003**). **BLOCKER** — Owner (**OQ-002**).
**BLOCKER** — REQ-041 hat **keinen** Vision-Anker: VIS-014 ist reserviert, Inhalt **MISSING**,
TRC-041 ist `broken`. Der Nachweis ist erbringbar; die Zeile, die ihn an die Produktvision bindet,
ist es nicht.

### EV-044 — Vergleich fachlich vergleichbarer Aktivitäten (REQ-042 / AC-043 / CAN-143), Release Gate A2

**Nachfolger 2 von 2 für EV-040.** Kanonischer Umfang von CAN-143: „Nutzer können fachlich
vergleichbare Aktivitäten auf derselben oder hinreichend ähnlichen Strecke anhand
sportartspezifischer Kennzahlen miteinander vergleichen."

`evidence_status: not-planned` · `release_gate: A2` · Owner: **MISSING (OQ-002)** ·
**blockiert durch OQ-015** (`blocked_gates [A2]`, `blocked_activities [implementation]`)

| Marke (keine ID) | Geforderter Nachweis | Art des Nachweises | Result |
|---|---|---|---|
| [VG1] | Zwei als fachlich vergleichbar erkannte **Run**-Aktivitäten werden anhand sportartspezifischer Kennzahlen gegenübergestellt | Integrationstest + reale Aktivitäten | nicht erbracht — **nicht bezifferbar**, siehe BLOCKER |
| [VG2] | Zwei als fachlich vergleichbar erkannte **Bike**-Aktivitäten werden gegenübergestellt | Integrationstest + reale Aktivitäten | nicht erbracht — **nicht bezifferbar** |
| [VG3] | **Kein sportartübergreifender Vergleich**: eine Run- und eine Bike-Aktivität werden nie gegenübergestellt | Negativtest je Richtung | nicht erbracht — **heute prüfbar**, sobald Code existiert |
| [VG4] | **Keine irreführende Bestzeit bei nicht vergleichbarer Geometrie** | Negativtest mit geometrisch abweichenden Aktivitäten | nicht erbracht — **nicht bezifferbar**: „nicht vergleichbar" ist undefiniert |
| [VG5] | **Verkürzte, verlängerte und abgebrochene** Aktivitäten werden nach einer definierten Regel behandelt | Negativtest je Kategorie | nicht erbracht — **nicht bezifferbar**: die Regel existiert nicht |
| [VG6] | Die **Streckenähnlichkeit** wird nach einer dokumentierten, reproduzierbaren Methode bestimmt; zwei Läufe auf demselben Datensatz ergeben dasselbe Ergebnis | Spezifikation + Testdatensatz mit erwartetem Ergebnis | nicht erbracht — **nicht bezifferbar**: es existiert keine Methode |

**BLOCKER — [VG1], [VG2], [VG4], [VG5] und [VG6] sind derzeit nicht einmal als Testfall
formulierbar.** **OQ-015** ist offen: wann zwei Strecken als vergleichbar gelten, die tolerierte
Abweichung der Streckenähnlichkeit, die verglichenen Kennzahlen und die Behandlung verkürzter,
verlängerter und abgebrochener Aktivitäten sind **nicht festgelegt**. **Es wird keine
Vergleichstoleranz und keine Ähnlichkeitsschwelle geraten.** Ein Test ohne Schwellwert ist kein
Test, sondern eine Absichtserklärung.

**[VG3] ist die Ausnahme** und ausdrücklich benannt, damit die Blockade nicht pauschal wirkt: die
strikte Trennung von Run und Bike steht fest und ist unabhängig von OQ-015 prüfbar.

**Run und Bike werden getrennt verifiziert.**

### EV-038 und EV-042 — reserviert, hier nur verzeichnet

Diese zwei EV-IDs stammen aus dem Auftau-Schritt vom 2026-07-19, gehören aber nicht zu den oben
ausformulierten Nachweisen. Sie werden hier verzeichnet, damit sie nicht unbemerkt bleiben; ihre
Nachweisbedingungen sind **nicht** ausformuliert.

| EV-ID | Gegenstand | evidence_status | Offen |
|---|---|---|---|
| EV-038 | Monochromes tokenbasiertes Designsystem (REQ-038 / AC-038 / CAN-141) | `not-planned` | Farbe erscheint ausschließlich in den festgelegten fachlichen Bedeutungen (Health-Status, Team-/Revieridentität, Sportplatz-Gold, bestätigte Feiermomente); Run und Bike werden **nicht** ausschließlich durch Farbe unterschieden. **BLOCKER** — TRC-038 ist `broken`: REQ-038 hat **keinen** Vision-Anker (VIS-012 reserviert, Inhalt MISSING). **Änderung 2026-07-20:** die Klausel „Farbe ist niemals der einzige Informationsträger" wird **nicht** hier nachgewiesen, sondern kanonisch unter EV-037 / [ACC5] — siehe Abgrenzung unten |
| EV-042 | Datenmodell trennt Identität und historische Aggregate (CONTRA-005 / REQ-017 / REQ-027) | `blocked` | Löst die frühere Marke (z) als ID-Frage ab. **BLOCKER** — Retentionsfristen (**OQ-009**) fehlen; das Schema ist ohne sie nicht belastbar entwerfbar |

**Abgrenzung EV-037 ↔ EV-038 zur Farbregel (Nutzerentscheidung 2026-07-20).** Die Klausel „Farbe
ist niemals der einzige Informationsträger" stand zuvor in **beiden** Canvas-Items (CAN-099 und
CAN-141) und wurde dadurch als **doppelte Pflicht** geführt. Kanonischer Träger ist **CAN-099 →
REQ-037 → EV-037 [ACC5]**. Begründung: die Klausel schützt **Wahrnehmbarkeit**; ihr Ausfall ist
ein Zugänglichkeits-, kein Gestaltungsdefekt. Ein monochromes Produkt kann sie verletzen (zwei
Grautöne ohne zweiten Träger), ein farbiges sie erfüllen — die beiden Aussagen sind unabhängig.
In EV-038 verbleibt ausschließlich die Designregel „Run und Bike werden nicht ausschließlich
durch Farbe unterschieden". **Ein Nachweis unter EV-038 ersetzt [ACC5] nicht.**

### EV-040 — deprecated 2026-07-20

| Alt-ID | deprecated_at | replacement_id | Grund |
|---|---|---|---|
| ~~EV-040~~ | 2026-07-20 | **EV-043, EV-044** | Composite: ein Nachweis für zwei Funktionen mit **unterschiedlichem Blockierungszustand**. EV-043 ist heute vollständig spezifizierbar, EV-044 ohne OQ-015 nicht einmal bezifferbar. Eine gemeinsame ID hätte entweder die lieferbare Hälfte mitblockiert oder die blockierte über die lieferbare als erledigt gelten lassen |

Die Zeile bleibt als Migrationsbeleg stehen. **Neue Referenzen auf EV-040 sind ein
Validierungsfehler**; dasselbe gilt für REQ-040, AC-040, CAN-140 und TRC-040.

**Hinweis zur Marke (z).** Der Abschnitt „Offene Evidence aus DEC-011 und DEC-012" oben führt die
Zeile (z) noch mit „keine EV-ID". Das ist seit dem 2026-07-19 überholt: die ID ist **EV-042**. Der
Nachweis selbst bleibt unverändert `nicht erbracht` — die ID-Frage ist geschlossen, die
Evidenzfrage nicht.

## Geforderte Evidence: NFR-001 … NFR-008 (Nachweisbedingungen aus dem NFR-Audit)

**Sämtliche Nachweise dieses Abschnitts sind offen — `nicht erbracht`.** Es existiert kein Code,
kein Build, kein Gerätetest und keine Messreihe. Kein Test dieses Abschnitts wurde ausgeführt;
keiner ist bestanden. Dieser Abschnitt ist eine **Anforderung an künftige Nachweise**, kein
Nachweis.

> **BLOCKER — keine EV-ID für NFR-Nachweise.** `docs/ID-REGISTRY.md` ist eingefroren; EV-001…EV-036
> sind 1:1 an REQ-001…REQ-036 gebunden (Registry §6.7) und der `NFR-`Raum ist überhaupt nicht
> registry-verwaltet. Für die NFR-Nachweise existiert daher **keine reservierte EV-ID**. Nach
> Registry-Regel 3 wird das als BLOCKER gemeldet, statt eine ID zu erfinden. Wo unten eine EV-ID
> steht, ist sie einem REQ entliehen und deckt den NFR nur **teilweise**. Die Marken `[N1]`…`[N8]`
> sind reine abschnittslokale Lesemarken, **keine IDs**, und entsprechen keinem ID-Format.

> **BLOCKER — drei referenzierte ID-Räume sind registry-fremd.** Eine Direktprüfung der
> Registry-Zeilen am 2026-07-19 ergibt, dass `docs/ID-REGISTRY.md` ausschließlich die Präfixe
> `AC`, `ASM`, `CAN`, `CONTRA`, `EV`, `OQ`, `REQ`, `RISK`, `TRC` und `VIS` führt (347 Zeilen-IDs).
> Die in diesem Abschnitt referenzierten Präfixe **`NFR-`, `DEC-` und `SRC-` sind darin nicht
> enthalten**. Sie existieren in ihren eigenen kanonischen Dateien (`…prd.md`,
> `docs/decisions/decision-log.md`, `docs/SOURCE-MAP.md`), unterliegen aber **keiner
> Kollisionskontrolle**. Das ist dasselbe Defektmuster, das CONTRA-003 für die OQ-IDs bereits
> nachgewiesen hat. Es wird gemeldet, nicht durch eigenmächtige ID-Vergabe geheilt — die Registry
> ist eingefroren.

**Zwei getrennte Achsen.** `source_type` beantwortet „woher stammt der Zielwert?",
`evidence_status` beantwortet „ist die Erfüllung nachgewiesen?". Sie werden nicht vermischt;
`EXPLICIT` + `pending` ist eine gültige Kombination (nur NFR-007). Keine automatische Vererbung:
eine qualitative Vision-Absicht macht einen quantitativen Zielwert **nicht** `EXPLICIT`.

| Marke (keine ID) | NFR | source_type | evidence_status | Bestehende EV-ID (entliehen) | Fällig | Result |
|---|---|---|---|---|---|---|
| [N1] | NFR-001 Distanzgenauigkeit | ASSUMPTION | pending | EV-002, EV-004 (teilweise) | vor Gate A0 — **blockierend** für Feldtest und Release | nicht erbracht |
| [N2] | NFR-002 Batterie | ASSUMPTION | pending | **keine** für die Stundenmessung; EV-003 deckt nur Background-Verhalten | vor Gate A0 — **blockierend** für Feldtest und Release | nicht erbracht |
| [N3] | NFR-003 Zuverlässigkeit | ASSUMPTION | pending | EV-003, EV-005 | vor Gate A0 — **blockierend** | nicht erbracht |
| [N4] | NFR-004 Performance | **BLOCKER** | **blocked** | EV-026 (nur Territory-Anteil ab D); für „Tracking-UI flüssig" **keine** | Schwelle vor Gate D; A0-Klausel ohne Fälligkeit | nicht erbracht — **nicht erbringbar** |
| [N5] | NFR-005 Accessibility | **EXPLICIT** für die Fassung (WCAG **2.2 AA**, Nutzerentscheidung 2026-07-19); ASSUMPTION für die übrigen Klauseln | `not-planned` | **EV-037** (EV-014 deprecated) | vor Gate A0 (Basis), vollständiger Audit vor A2 — **blockierend** | nicht erbracht |
| [N6] | NFR-006 Datenschutz | **BLOCKER** | **blocked** | EV-017, EV-034, EV-027 (teilweise) | vor Finalisierung des Datenbankschemas und vor Gate B | nicht erbracht — teilweise **nicht erbringbar** |
| [N7] | NFR-007 Sicherheit | EXPLICIT (nur Klausel „keine Secrets im Client") | pending | ASM-103, EV-034, EV-006 | ab Gate A0 fortlaufend bis E — **blockierend** | nicht erbracht |
| [N8] | NFR-008 Wartbarkeit | MISSING | **not-planned** | **keine** | **MISSING — kein Gate referenziert NFR-008** | kein Nachweis vorgesehen |

`blocked` ist bei [N4] und [N6] ausdrücklich **nicht** dasselbe wie `pending`: dort fehlt nicht
der Code, sondern die Bestehensbedingung. Der Nachweis bliebe auch mit fertiger Implementierung
unentscheidbar. `not-planned` bei [N8] ist ebenfalls nicht `pending`: es steht nichts aus, weil
nichts geplant ist.

### [N2] NFR-002 Batterie — verbindliche Messbedingungen

Der Zielwert `< 10 % Ladungsabnahme pro Stunde bei aktivem Tracking` ist **ASSUMPTION**: das PRD
nennt ihn ohne Quelle und bezeichnet ihn an anderer Stelle selbst als „für dieses Produkt nicht
empirisch belegt". Er wird als vorläufiges Engineering-Ziel geführt. `EXPLICIT` erst nach
ausdrücklicher Nutzerbestätigung oder belastbarer Quelle.

Eine Batteriemessung ohne dokumentierten Gerätezustand ist **wertlos** — allein Display an/aus
verändert das Ergebnis stärker als die 10-%-Schwelle selbst. Ein Messlauf, der die folgenden
Bedingungen nicht vollständig dokumentiert, zählt **nicht** als Nachweis und ist als
`nicht erbracht` zu führen:

| # | Bedingung | Anforderung | Status |
|---|---|---|---|
| 1 | **Referenzgeräte** | Namentlich festgelegte Geräteliste mit OS-Version je Gerät. Ohne sie ist der Wert nicht vergleichbar — derselbe Code ergibt auf unterschiedlichen Geräten stark abweichende Werte. | **BLOCKER — MISSING (OQ-003 offen)** |
| 2 | **Displayzustand** | Zustand (an/aus) und, bei „an", die Helligkeitsstufe sind je Messlauf zu protokollieren; zusätzlich, ob die Kartendarstellung aktiv war. | zu dokumentieren |
| 3 | **Netzwerkzustand** | WLAN / Mobilfunk / Flugmodus — je Messlauf protokolliert. | zu dokumentieren |
| 4 | **GPS-Sampling** | Eingestellte Sampling-Rate und Genauigkeitsstufe der Standortabfrage, je Sportart (Run und Bike verwenden laut Architektur unterschiedliche Konfigurationen). | zu dokumentieren |
| 5 | **Background aktiv** | Background-Tracking muss über die gesamte Messdauer aktiv sein. Eine Messung im Vordergrund ist kein Nachweis für NFR-002. | zu dokumentieren |
| 6 | **Messfenster** | Eine **zusammenhängende Stunde** aktives Tracking. Teilmessungen werden nicht hochgerechnet. | festgelegt |
| 7 | **Messläufe** | Mindestens **ein Messlauf je Sport und je Plattform** — also mindestens vier: Run/iOS, Run/Android, Bike/iOS, Bike/Android. Run und Bike werden getrennt verifiziert, iOS und Android werden getrennt verifiziert. Ein Lauf darf **nicht** auf die andere Sportart oder Plattform übertragen werden. | festgelegt |
| 8 | **Ausgangsladestand** | Ladestand bei Messbeginn und bei Messende, jeweils in Prozentpunkten. | zu dokumentieren |
| 9 | **Umgebungstemperatur** | Zu protokollieren; Akkuverhalten ist temperaturabhängig. | zu dokumentieren |
| 10 | **Wiederholung** | Wiederholung vor jedem Gate ab A0. | festgelegt |

**Nicht erbracht.** Keiner der mindestens vier geforderten Messläufe wurde durchgeführt. Es
existiert kein Code, kein Build und kein festgelegtes Referenzgerät.

**MISSING — keine eigene EV-ID.** EV-003 (30-Minuten-Kill-/Background-Test) deckt das
Background-Verhalten ab, **nicht** die Stundenmessung. Für die Batteriemessung selbst benennt kein
Artefakt eine EV-ID. Die Canvas-Annahme CAN-116 („Batterietests") existiert, ist aber keine EV-ID.

**CONTRADICTION.** Das PRD führt NFR-002 an einer Stelle als `EXPLICIT` und hält an anderer Stelle
fest, der Wert sei „nicht empirisch belegt". Der stärkere Wert wurde **nicht** still übernommen;
die Klassifikation bleibt ASSUMPTION.

### [N1] NFR-001 Distanzgenauigkeit — Nachweisbedingungen

Zielwert `< 3 % Abweichung` gegenüber einer definierten Referenzstrecke, **ASSUMPTION** (keine
Quelle auffindbar; die Zeichenfolge erscheint im Repo ausschließlich als Wiederholung des
PRD-Werts). Testmethode: realer Feldtest auf einer Referenzstrecke bekannter Länge, Vergleich der
gefilterten Trackdistanz gegen die Referenzlänge. Mindestklasse `production-verified` — im Labor
nicht nachweisbar. Getrennt für Run und Bike, getrennt für iOS und Android.

Offen: **MISSING** — die Referenzstrecke ist in keinem Artefakt benannt oder vermessen.
**MISSING** — die Mindestanzahl Wiederholungen je Sport-/Plattform-Kombination ist nirgends
festgelegt; ohne sie ist kein Konfidenzintervall bestimmbar und ein Einzellauf kann den Wert
zufällig treffen. **MISSING** — zulässige Verwurfsquote des GPS-Filters. **BLOCKER** —
Referenzgeräte (OQ-003). `verified` erst nach realen Referenzstreckentests auf festgelegten
Referenzgeräten.

### [N3] NFR-003 Zuverlässigkeit — Nachweisbedingungen

Nullschwelle: 0 verlorene Aktivitäten über Kill- und Migrations-Fixtures, 0 inkonsistente Indexe
nach Migration, jede Migration idempotent wiederholbar; Session-Recovery gelingt in 100 % der
30-Minuten-Kill-Tests je Plattform und je Sportart. Die Nullschwelle selbst ist die logische
Übersetzung der Anforderung („kein Datenverlust" = 0) und insoweit nicht belegbedürftig;
`ASSUMPTION` bezieht sich auf die Anforderung selbst und auf die Operationalisierung „30 Minuten",
„je Plattform", „je Sportart", die in einem abgeleiteten Artefakt gesetzt wurde.

Offen: **MISSING** — Begründung des 30-Minuten-Fensters (warum nicht 60?). **MISSING** —
Auto-Pause-Falschauslösungsrate ohne Schwellwert. **MISSING** — Rate technisch abgebrochener
Sessions wird gemessen und dokumentiert, aber ohne Zielwert bewertet. **BLOCKER** — Referenzgeräte
und OS-Versionen (OQ-003); das Kill-Verhalten ist versionsabhängig (RISK-001, Severity critical).

### [N4] NFR-004 Performance — nicht erbringbar, `blocked`

NFR-004 ist der schwächste der acht: **keine Metrik, keine Einheit, keine Schwelle, kein
Messfenster, keine Testdatenbasis.** „Flüssig" ist kein Zielwert, sondern ein Adjektiv. Es wurde
ausdrücklich **kein** plausibler Wert eingesetzt — weder 60 fps noch 16 ms noch ein Perzentil;
jede solche Zahl wäre erfunden.

Der Geo-Lasttest ist als Pflicht vor Gate D festgeschrieben, hat aber keine Pass/Fail-Bedingung.
**Ein Test ohne Bestehensgrenze kann nicht bestanden werden — er kann nur behauptet werden.**
Deshalb `blocked` statt `pending`: der Nachweis scheitert nicht am fehlenden Code, und das bliebe
auch mit fertigem Code so.

Offen: **BLOCKER** — Performanceschwelle (Metrik, Einheit, Wert), vor Gate D zu entscheiden.
**MISSING** — keine EV-ID für die A0-Klausel „Tracking-UI flüssig", und für diese Klausel
existiert nicht einmal ein Fälligkeitszeitpunkt. **MISSING** — reale Aktivitätsdichten als
Testdatenbasis; synthetische Gleichverteilungen unterschätzen die Ballung und reichen laut PRD
allein nicht aus.

### [N5] NFR-005 Accessibility — Nachweisbedingungen

Pass-Bedingung: 100 % der ausgelieferten Screens bestehen Kontrast-, Dynamic-Type- und
Screenreader-Prüfung in Light **und** Dark Mode; 0 Zustände, die allein über Farbe unterschieden
werden. Kein Prozentziel unterhalb von 100 — die Anforderung ist eine Schranke, keine Quote.

**Aktualisiert 2026-07-19 — die Fassungsfrage ist geschlossen.** Der frühere Befund lautete:
`ASSUMPTION` statt `EXPLICIT`, weil mit „WCAG AA" zwar eine Norm im Text stand, die **Fassung**
aber fehlte (2.0 AA, 2.1 AA und 2.2 AA haben unterschiedliche Erfolgskriterien). Durch die
Nutzerentscheidung zu CAN-099 ist die Fassung festgelegt: **WCAG 2.2 AA**. Der BLOCKER
„WCAG-Version" ist damit **geschlossen**, und für diese eine Klausel gilt `EXPLICIT`.

**Nicht mitgeschlossen — die Verbindlichkeit.** In keinem Artefakt wird eine **Rechtsgrundlage**
zitiert, die WCAG 2.2 AA für dieses Produkt verbindlich macht — kein Verweis auf EAA, BFSG oder
eine Store-Vorgabe. Die Festlegung einer Fassung ist **keine** Rechtsverbindlichkeit; beides wird
nicht vermischt und die stärkere Aussage nicht still übernommen.

Folge für den Nachweis: die prüfbaren Klauseln (100 % Abdeckung, 0 farbcodierte Zustände) sind
jetzt formulierbar und gegen 2.2 AA prüfbar — aber **nicht geprüft**. `evidence_status` steht auf
`not-planned` und **nicht** auf `pending`: es existiert kein Code, also auch keine
Instrumentierung und kein Audit-Aufbau. Die Nachweisbedingungen sind oben unter **EV-037**
([ACC1] … [ACC7]) ausformuliert; sämtliche sieben Zeilen stehen auf `nicht erbracht`.

Offen: **MISSING** — Rechtsgrundlage der Verbindlichkeit. **MISSING** — Screenreader- und
Gerätematrix (VoiceOver/TalkBack in welchen OS-Versionen, welche Schriftgrößenstufen, welche
Kontrastmessmethode; **OQ-003**). **BLOCKER** — VIS-011 als Vision-Anker ist unbestätigt und zählt
bis zur Nutzerbestätigung nicht als erfüllter Anker. **BLOCKER** — Owner (**OQ-002**).

**ID-Nachzug.** NFR-005 verwies bis zum 2026-07-19 auf **EV-014**. EV-014 ist seit der
Aufspaltung von REQ-014 **deprecated** (Nachfolger: EV-037 Accessibility, EV-038 monochromes
Designsystem) und darf nicht wiederverwendet werden. Der Verweis ist hier auf **EV-037**
umgestellt. Die Aufspaltung ist inhaltlich tragend: der Designsystem-Nachweis ist **kein**
Accessibility-Nachweis — ein monochromes System kann WCAG-konform oder -widrig sein.

### [N6] NFR-006 Datenschutz — teilweise nicht erbringbar, `blocked`

Der Requirement-Kern ist durch zwei belegte Nutzerentscheidungen gedeckt (DEC-012 Löschumfang,
DEC-013 A0-Proxy-Baseline, geführt als SRC-006). Der **Zielwert** ist es nicht.

Bestimmt: Löschumfang abschließend aufgezählt; historische Daten überleben nur wirksam
anonymisiert, sonst Löschung; für den A0-Routing-Proxy Retention 0 für den Koordinaten-Payload,
technische Logs max. 7 Tage, `eu-central-1`.

Unbestimmt und damit blockierend: **BLOCKER** — Aufbewahrungsfristen für GPS-, Health- und
Live-Daten (OQ-009). Sie blockieren die von DEC-012 **vor** der Schema-Finalisierung geforderte
technische Trennung von Identität und historischen Aggregaten; das Schema kann ohne sie nicht
belastbar entworfen werden. **BLOCKER** — es existiert **kein Prüfverfahren für „wirksam
anonymisiert"** (Befund B6 des Validierungsberichts); ohne definiertes Verfahren ist
Anonymisierungswirksamkeit nicht prüfbar. **BLOCKER** — für „Datenmodell trennt Identität und
historische Aggregate" existiert keine EV-ID (siehe Marke (z) oben). **MISSING** — Backend und
Hosting-Region (OQ-005). **MISSING** — Verarbeitungsregion, Unterauftragsverarbeiter und
Transfergrundlage des Routing-Anbieters.

**OPEN QUESTION** — „EU-orientiertes Hosting" ist als Formulierung kein prüfbarer Zielwert. Er
steht zudem im Spannungsverhältnis zum Vorbehalt aus DEC-013, wonach die Bezeichnung „EU-Proxy"
nicht den Eindruck erwecken darf, die gesamte Verarbeitung liege in der EU, wenn der nachgelagerte
Anbieter außerhalb verarbeitet.

### [N7] NFR-007 Sicherheit — Nachweisbedingungen

**Der einzige der acht NFRs, bei dem die Beweislatte für `EXPLICIT` erreicht wird — und zwar nur
für eine von fünf Klauseln.** Die Klausel „keine Secrets im Client" ist durch eine belegte
Nutzerentscheidung gedeckt: DEC-005 (`user-confirmed`), CAN-092 (`CONFIRMED`), CONTRA-002
(`resolved`), SRC-006. Die technische Begründung ist konkret und nachprüfbar: `EXPO_PUBLIC_*` wird
ins JS-Bundle inlined und ist aus jedem Build extrahierbar. Die Einstufung ist keine Hochstufung,
sondern die Wiedergabe einer protokollierten Nutzerentscheidung.

Die übrigen vier Klauseln werden ausdrücklich **nicht** mitgezogen:

| Klausel | source_type | Quelle |
|---|---|---|
| keine Secrets im Client | **EXPLICIT** | DEC-005, CAN-092, CONTRA-002, SRC-006 |
| sichere Auth | ASSUMPTION | keine — kein Verfahren, kein Standard, keine Schwelle benannt |
| Row-Level-Security | ASSUMPTION | keine — setzt zudem den offenen Backend-Entscheid OQ-005 voraus |
| Rate Limits | **MISSING** | keine — kein Artefakt nennt einen Zahlenwert |
| serverseitige Validierung | ASSUMPTION | keine — Nullschwelle stammt aus einem abgeleiteten Artefakt |

Pass-Bedingung, bestimmt: 0 Routing-Provider-Keys im App-Bundle (ab A0 auch für den
Proxy-Key), 0 Endpunkte ohne Rate Limit, 0 Endpunkte ohne serverseitige Validierung. Testmethode:
Bundle-Scan des ausgelieferten JS-Bundles, Proxy-Integrationstest, Security-Review, RLS-Tests,
Endpunkt-Inventar. Mindestklasse `real-boundary-smoke` — **ein gemockter Routing-Response verdeckt
genau den NFR-007-Pfad** und zählt nicht als Nachweis. NFR-007 gilt laut DEC-005 ab A0 bis E,
nicht erst ab Stufe B.

`pending` und nicht `blocked`, weil die Pass-Bedingung der Kernklausel eindeutig ist und
ausschließlich der Gegenstand fehlt: kein Code, kein Build, kein Bundle. Die Klausel „Rate Limits"
ist dagegen ohne Zahlenwert nicht prüfbar und insoweit blockiert — **MISSING**: DEC-013 fordert
„Rate Limit, Size-Limit, maximale Wegpunktzahl, Timeout, Kill Switch" und beziffert **keinen**
dieser Werte.

### [N8] NFR-008 Wartbarkeit — verwaist, `not-planned`

**Befund: NFR-008 ist wirkungslos.** Kein Requirement, kein AC, keine EV-ID, kein Gate und kein
Risiko referenziert NFR-008. Die Gate-Tabelle nennt es nicht.

> **Präzisierung der Zählung (korrigiert 2026-07-19).** Das NFR-Audit hielt fest, die Zeichenfolge
> „NFR-008" erscheine im gesamten Repository **genau einmal** — in der Definitionszeile
> `prd.md:201`. Das traf zum Zeitpunkt des Audits zu, ist **inzwischen aber überholt**: eine
> Nachzählung am 2026-07-19 ergibt 31 Fundstellen (`docs/traceability.md` 12,
> `docs/prd/…prd.md` 10, diese Datei 9). Die Aussage wird hier korrigiert statt weitergetragen.
>
> **Der Befund selbst ändert sich dadurch nicht.** Sämtliche neuen Fundstellen sind
> **Dokumentation über die Verwaisung** — die Audit-Auswertung im PRD, die Traceability-Zeilen
> dazu und dieser Abschnitt. Keine einzige davon ist eine **funktionale** Referenz: kein
> Requirement leitet aus NFR-008 ab, kein Gate prüft es, keine EV-ID weist es nach. Ein
> Qualitätsziel wird nicht dadurch wirksam, dass man seine Wirkungslosigkeit dokumentiert.
>
> Die Zahl ist volatil: parallel arbeitende Agenten schreiben denselben Befund derzeit in weitere
> Dateien. Belastbar ist nicht die Fundstellenzahl, sondern das Fehlen jeder funktionalen
> Referenz.

`evidence_status = not-planned` ist bewusst nicht `pending`: es steht nichts aus, weil nichts
geplant ist.

> **Korrektur 2026-07-20 — `blocking` entfällt für NFR-008, der Befund bleibt.** Die frühere
> Fassung führte hier `blocking = false` als „abgeleitet, nicht gesetzt". Das war nicht haltbar:
> die `blocking`-Achsen (`status`, `resolution_status`, `blocked_gates`, `blocked_activities`)
> sind nach Registry §3.1 auf `OQ-` und `CONTRA-` beschränkt, und die Achse `status`
> (`open`/`resolved`) beantwortet „Ist die Grundsatzfrage entschieden?". **Ein NFR ist keine
> Entscheidung, sondern eine Anforderung** — es benutzt die Achse `active`/`deprecated`/`reserved`.
> Wendet man die Formel trotzdem an, liefert `status NOT IN [resolved]` für **alle acht** NFRs
> `blocking = true`: syntaktisch gültig, mechanisch reproduzierbar, fachlich bedeutungslos.
> **Nutzerentscheidung 2026-07-20: der `NFR-`Raum führt kein `blocking`.** Die Achsen werden
> **nicht** auf `NFR-` erweitert — keine Metamodell-Erweiterung.
>
> **Die tragende Information geht dabei nicht verloren**, sie steht in den Feldern, die es im
> eingefrorenen Modell schon gibt: `evidence_gate = MISSING` (kein Gate fordert NFR-008 ein) und
> `evidence_status = not-planned` (kein Messkonzept). Ein `blocking = false`, das niemand
> nachrechnet, ist genau die Sorte Wert, die eine Prüfung passiert, ohne etwas auszusagen.

**Der Befund ist unverändert und wird durch den Wegfall des Feldes nicht kleiner:** NFR-008 wird
an **keiner** Stelle wirksam — kein Gate fordert es ein, kein Messkonzept existiert, keine CI
könnte die vier Zusagen durchsetzen. **Dass ein Must-artiges Qualitätsziel wirkungslos ist, ist
der eigentliche Befund, nicht seine Unbedenklichkeit.** Das bleibt so bis **OQ-013**.

**BLOCKER, außerhalb dieser Datei:** `docs/prd/revyr-endurance-platform.prd.md:302-311` führt eine
Spalte `blocking` mit **acht hartkodierten NFR-Werten**. Sie sind zu **entfernen**, nicht
umzurechnen — für `NFR-` gibt es keine Formel, aus der sich ein Wert ableiten ließe. Diese acht
sind genau die zuvor gemeldeten „8 von 14 ungeprüften `blocking`-Werten" des Projekts. Der
PRD-Owner zieht nach; diese Datei ändert das PRD nicht.

**BLOCKER, außerhalb dieser Datei:** `prd.md:311` führt NFR-008 mit `source_type = EXPLICIT`,
`docs/ID-REGISTRY.md` mit **MISSING**. Nach Registry §1 gilt die Registry; der Nachzug liegt beim
PRD-Owner.

Offen: **BLOCKER** — NFR-008 ist verwaist. **MISSING** — Testabdeckungsquote und alle übrigen
Schwellen; keine der vier Zusagen (TypeScript strict, reine Domainmodule, versionierte Schemas,
automatisierte Tests) hat eine Schwelle. **MISSING** — es existiert keine CI im Repository, die
sie durchsetzen könnte. `measurement_type` ist als `PROCESS_CONTROL` geführt, weil keine der vier
im Repo verwendeten Klassen passt; die Ergänzung wird offengelegt statt eine Fehlzuordnung
vorzunehmen.

### Querschnittliche offene Punkte aller acht NFRs

- **OWNER-BLOCKER (OQ-002).** Für **keinen** der acht NFRs existiert ein benannter Owner. OQ-002
  (finaler Repository-Owner/DRI) ist offen; die in den Artefakten genannten Zuständigkeiten
  („Engineering/QA", „Privacy/Product") sind Rollen, keine Personen. Ein Nachweis ohne Owner hat
  niemanden, der ihn erbringt oder verantwortet.
- **BLOCKER — Referenzgeräte (OQ-003).** Fünf der acht NFRs (NFR-001, -002, -003, -004, -005)
  fordern eine Referenzumgebung, die nirgends definiert ist.
- **Keine automatische Vererbung aus der Vision.** Die Vision führt für **keinen** NFR einen
  Zielwert; das wurde je Abschnitt nachgesehen, nicht angenommen. Ein Vision-Item wie „Tracking
  muss präzise sein" macht `< 3 %` **nicht** `EXPLICIT`.
- **`EXPLICIT` bedeutet in `docs/traceability.md` etwas anderes** — dort nur „steht wörtlich
  irgendwo". Wer beide Bedeutungen gleichsetzt, stuft still hoch. Die Klassifikation dieses
  Abschnitts folgt der Audit-Definition, nicht der Traceability-Definition.

## Gate Summary

| Gate | Status | Evidence Entry | Blocking Findings |
|---|---|---|---|
| P0 | pending | MISSING | MISSING |
| A0 | pending | MISSING | A0-Routing-Evidence (a)…(n) nicht erbracht; CONTRA-006 `evidence_status = pending`, `blocked_gates [A0]`, `blocking = true`; NFR-001, NFR-002, NFR-003, NFR-005, NFR-007 nicht erbracht; NFR-004 und NFR-006 `blocked` (keine Pass-Bedingung); Accessibility-**Basis** EV-037 [ACC2]…[ACC6] nicht erbracht; **EV-008** Verlauf und Detailansicht [H1]…[H6] nicht erbracht (Run und Bike getrennt); **EV-038** Designsystem-Erstabnahme nicht erbracht — TRC-038 `broken` |
| A1 | pending | MISSING | NFR-005 [N5] fortlaufend nicht erbracht; NFR-006 [N6] `blocked`; NFR-007 [N7] nicht erbracht; EV-037 fortlaufend nicht erbracht |
| A2 | pending | MISSING | NFR-005 [N5] Abnahme über A0–A2 nicht erbracht; NFR-006 [N6] `blocked`; NFR-007 [N7] nicht erbracht; **EV-037** vollständiger WCAG-2.2-AA-Audit [ACC1]…[ACC7] nicht erbracht (VoiceOver **und** TalkBack getrennt); **EV-039** GPX-Export [G1]…[G8] nicht erbracht — [G4] zusätzlich **nicht prüfbar** (Referenz-App MISSING, OQ-016) und im kanonischen CAN-139-Wortlaut nicht mehr wörtlich gedeckt; **EV-043** Streckenwiederverwendung [RU1]…[RU6] nicht erbracht (nicht blockiert, aber TRC-041 `broken` — Vision-Anker VIS-014 MISSING); **EV-044** Aktivitätsvergleich [VG1]…[VG6] nicht erbracht und **[VG1], [VG2], [VG4], [VG5], [VG6] nicht einmal bezifferbar** (OQ-015) |
| B | pending | MISSING | Löschungsnachweis (x) nicht erbracht; NFR-006 [N6] `blocked` — Retentionsfristen (OQ-009) und Prüfverfahren „wirksam anonymisiert" fehlen; Schema-Trennung **EV-042** `blocked`; **EV-041** CAN-130-Kennzahl [T1]…[T12] nicht erbracht — Instrumentierung durch **OQ-012** versperrt, abschließende Bewertung zusätzlich durch **OQ-014**; `empirical_result` MISSING — CAN-130 gilt **nicht** als empirisch validiert |
| C | pending | MISSING | Anti-Cheat-Datenminimierung (v), (w) nicht erbracht; CONTRA-004 `evidence_status = pending`, `blocking = true` |
| D | pending | MISSING | Anonymisierungsnachweis (y) nicht erbracht; NFR-004 [N4] `blocked` — Geo-Lasttest ohne Pass/Fail-Bedingung |
| E | pending | MISSING | NFR-007 [N7] gilt bis E und ist nicht erbracht |

Ein Gate besteht nur, wenn alle REQs seiner Version ✅ sind. Kein Gate-Status wurde in diesem
Lauf verändert; alle stehen unverändert auf `pending`.
