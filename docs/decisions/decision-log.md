# Decision Log

Status: proposed – pending-user-confirmation

| Decision ID | Decision | Status | Rationale | Revisit |
|---|---|---|---|---|
| DEC-001 | `revyr-endurance-platform` ist nur interner Feature-Slug; öffentlicher Name bleibt offen. | proposed | verhindert, dass ein riskanter Markenname in Produktwahrheit umgedeutet wird | Gate A2 |
| DEC-002 | Der erste öffentliche Release wird intern in A0 Tracking, A1 Health und A2 Experience geteilt. | proposed | reduziert parallele native, Health- und UX-Risiken | nach A0 |
| DEC-003 | Vollständige Aktivitäten und Trackpunkte werden in SQLite statt als AsyncStorage-JSON gespeichert. | proposed | Recovery, Migration, große Tracks und transaktionale Konsistenz | P0-Spike |
| DEC-004 | Route-Fortschritt basiert auf Polyline-Projektion und Off-Route-Logik. | proposed | einfache Distanzsubtraktion ist fachlich falsch | nach Feldtest |
| DEC-005 | Routing verwendet keinen ungeschützten Client-Secret-Key. **Präzisiert 2026-07-19:** ein minimaler serverseitiger Routing-Proxy existiert bereits ab A0 — nicht erst ab „Produktionsrouting". | user-confirmed (2026-07-19) | `EXPO_PUBLIC_*` wird ins JS-Bundle inlined und ist aus jedem Build extrahierbar; REQ-006/007 liegen in A0, NFR-007 gilt ab A0-E | Provider-ADR |
| DEC-006 | Health-Score besitzt Fallback und Confidence. | proposed | fehlende Hardware darf Tracking nicht entwerten; Unsicherheit muss sichtbar sein | Claims-Test |
| DEC-007 | Anti-Cheat verwendet mehrstufige Verifikation statt binär Betrug/nicht Betrug. | proposed | reduziert False Positives und diskriminiert fehlende Sensoren nicht automatisch | Simulation C |
| DEC-008 | Einzel-Reviere starten nicht vor Stufe D und benötigen separate Geo-Spezifikation. | proposed | Polygon- und Privacy-Komplexität ist nicht MVP-tauglich | Gate D |
| DEC-009 | Bahngold ist ein nicht übertragbarer Progressions-Score, keine Währung. | proposed | verhindert wirtschaftliche/store-bezogene Fehlinterpretation | vor D |
| DEC-010 | Sportplatz-Challenges benötigen Access-/Öffnungsprüfung und Kuratierung. | proposed | OSM-Vorhandensein bedeutet nicht öffentliche Zugänglichkeit | vor D |
| DEC-011 | Anti-Cheat und Wettbewerb erhalten serverseitig **ausschließlich minimierte, abgeleitete Plausibilitätssignale**. Rohsensorverläufe bleiben standardmäßig lokal auf dem Gerät. Details in §CONTRA-004. | entschieden (Nutzer 2026-07-19) — Implementierungs-Evidence ausstehend | löst CONTRA-004 auf, ohne REQ-034/Datenminimierung zu brechen; fehlende Sensoren senken die Beweiskraft, begründen aber keinen Betrugsverdacht | vor Stufe C |
| DEC-012 | Accountlöschung entfernt alle personenbezogenen Daten und Identitätszuordnungen. Historische Team-/Season-Daten überleben **nur wirksam anonymisiert**. Der Begriff „unveränderliche Historie" wird projektweit ersetzt. Details in §CONTRA-005. | entschieden (Nutzer 2026-07-19) — Implementierungs-Evidence ausstehend | löst CONTRA-005 auf; Identität und historische Aggregate müssen technisch getrennt werden — **vor** Erstellung des Datenbankschemas, nicht erst zu Stufe D | vor Datenmodell/Schema |
| DEC-013 | Für den A0-Routing-Proxy gilt eine verbindliche **Privacy-Baseline**: rein transiente Koordinatenverarbeitung, Retention 0, Body-Logging-Verbot, Zweckbindung, TLS-only, serverseitige Secrets, `eu-central-1`, technische Logs max. 7 Tage. Details in §CONTRA-006. | entschieden (Nutzer 2026-07-19) — **Design**; Evidence ausstehend und blockierend | macht die durch DEC-005 entstandene Privacy-Fläche kontrollierbar; die Baseline ist Voraussetzung, nicht Nachweis | vor A0-Routing-Implementierung, erneut vor erstem externem Feldtest |
| DEC-014 | **Klausel-scharfe Belegkorrektur Runde 6 (2026-07-20).** Fünf Zellen klausel-scharf getrennt: (a) **CAN-024** „Freizeit- und Rennradfahrer:innen" → „Radfahrer:innen (Rangstufe primär)"; „Renn-" entfernt, weil SRC-001:52 nur „**Ambitionierte** Rennradfahrer" führt (gehört zu CAN-025). Kern bleibt EXPLICIT. (b) **CAN-099** „mobile Anwendung und ihre Web-Auskopplungen … Bedienflächen … Fokusführung … motorische Anforderungen" → nur „mobile Anwendung … WCAG 2.2 AA, Screenreader, skalierbare Schrift, Farbregel"; Web-Auskopplungen entfernt (SRC-003 §2.1 erstreckt nur die Farbmisch-Regel dorthin), drei nicht-belegte Zusatzklauseln als **ASSUMPTION-A099-01/02/03** getrennt geführt. Kern bleibt EXPLICIT. (c) **CAN-109** „Anti-Cheat-Fehler (False Positives gegen reale Nutzer)" **EXPLICIT → ASSUMPTION**; Wortlaut unverändert. Grund: abgeleitetes Risiko aus SRC-003:265/559 („Fehlende Sensoren allein sind kein Betrug"), keine eigene Risikozeile in irgendeiner Quelle. (d) **CAN-119** „Privacy-Matrix und Privacy-Review" → „Sichtbarkeits-Matrix (Testtabelle Plan 7)"; Kern EXPLICIT (SRC-003:363/522/683), „Privacy-Review"-Anteil klausel-scharf als ASSUMPTION getrennt. (e) **VIS-003** „verlässliches Tracking … sicherer Zugang zu Trainingspartnern" verengt auf „Tracking … Anschluss an lokale Sportler:innen und Teams"; die Qualitätsqualifizierer „verlässlich" und „sicher" als ASSUMPTION getrennt (Volltextsuche auf Vision-Ebene: null Treffer). **Zusätzlich Werkzeug- und Quellenkette:** vier Quelldokumente (`docs/sources/SRC-001…SRC-004`) mit SHA-256-Prüfsummen in `scripts/validation/HASHES.md` und `tests/validation/HASHES.md` dauerhaft im Repository; 11 Prüfwerkzeuge + Wrapper unter `scripts/validation/` und `tests/validation/`; Ausführung über `scripts/validation/run_all.sh` bzw. `tests/validation/run_selftest.sh`. **Keine Werkzeuglogik geändert.** | entschieden (Nutzer 2026-07-20 Runde 6) — Bestätigung des konsolidierten Runde-5-Berichts weiterhin ausstehend | verhindert, dass eine als BELEGT geführte Zelle die eigene Belegdefinition verletzt; asymmetrische Anwendung des Maßstabs (Gegenprobe Runde 5) beseitigt; Werkzeugkette wird außerhalb des Scratchpads reproduzierbar | vor globaler User Confirmation |

### Hinweis zu DEC-011 … DEC-014

**Provenienz.** Die Auflösungen zu CONTRA-004, CONTRA-005 und CONTRA-006 wurden als wörtliche
Nutzeranweisung vom 2026-07-19 an diesen Schritt weitergereicht. Sie sind hier als
Nutzerentscheidung protokolliert, **nicht** von der Assistenz bestätigt. Der Dokumentstatus
bleibt `proposed – pending-user-confirmation`; kein Eintrag wird in fremdem Namen auf
`user-confirmed` gesetzt (RISK-024).

**ID-Raum.** `DEC-` wird von `docs/ID-REGISTRY.md` ausdrücklich **nicht** verwaltet
(Registry §5; offener Punkt 11 in Registry §8). Die Nummern DEC-011 … DEC-013 sind daher in
dieser — der kanonischen — Datei fortlaufend vergeben, aber **nicht kollisionsgeschützt**.
Solange der DEC-Raum außerhalb der Registry liegt, besteht genau das Defektmuster, das
CONTRA-003 für die OQ-IDs und Registry §6.9 für die ASM-IDs bereits nachgewiesen hat.

## Nutzerentscheidungen 2026-07-20 (Runde 4) — Protokoll

**Provenienz.** Die folgenden Entscheidungen wurden am 2026-07-20 als wörtliche Nutzeranweisung
weitergereicht. Sie sind hier **protokolliert, nicht bestätigt**. Der Dokumentstatus bleibt
`proposed – pending-user-confirmation`; kein Eintrag wird in fremdem Namen auf `user-confirmed`
gesetzt (RISK-024). Gesamtstatus unverändert **BLOCKED_TRACEABILITY**, `true-line-status`
`pending-watcher`.

> **BLOCKER — diese Entscheidungen haben keine DEC-ID.** Der `DEC-`Raum wird von
> `docs/ID-REGISTRY.md` ausdrücklich **nicht** verwaltet (Registry §5; offener Punkt 11), und
> dieser Schritt darf **keine ID vergeben** — auch keine DEC-ID. Die Marken **(D4-a) … (D4-i)**
> unten sind abschnittslokale Lesemarken, **keine IDs**, und dürfen nicht als solche referenziert
> werden. Sobald der DEC-Raum registriert oder die Registry entfroren ist, sind hier echte
> DEC-IDs zu vergeben — die nächste freie ist dann zu **prüfen**, nicht aus dieser Notiz
> abzuleiten. Genau dieses Muster hat CONTRA-003 für den OQ-Raum bereits als Defekt nachgewiesen.

| Marke (keine ID) | Entscheidung | Wirkung |
|---|---|---|
| (D4-a) | **Drei kanonische Canvas-Anker** mit verbindlichem Wortlaut: Accessibility (CONSTRAINT / VALUE BOUNDARY, primär REQ-037), monochromes Designsystem (DESIGN CONSTRAINT / PRODUCT PRINCIPLE, primär REQ-038), Datenportabilität und GPX-Export (VALUE PROMISE / CAPABILITY, primär REQ-039) | Phase 1 hat sie auf die **vorhandenen aktiven** Items CAN-099, CAN-141 und CAN-139 gezogen statt drei neue IDs zu vergeben — siehe Abweichung (D4-h) |
| (D4-b) | **Farbregel genau einmal.** „Farbe ist niemals der einzige Informationsträger" wird kanonisch von **CAN-099 → REQ-037 → EV-037 [ACC5]** getragen und ist aus CAN-141 entfernt | Beendet eine **doppelt geführte Pflicht**: die Klausel stand zuvor in beiden Items. Begründung: sie schützt **Wahrnehmbarkeit** — ihr Ausfall ist ein Zugänglichkeits-, kein Gestaltungsdefekt. Ein monochromes Produkt kann sie verletzen, ein farbiges sie erfüllen; die Aussagen sind unabhängig, nicht „dieselbe Beobachtung aus zwei Blickwinkeln". In CAN-141 verbleibt nur „Run und Bike nicht ausschließlich durch Farbe". **Keine dritte Farbregel** |
| (D4-c) | **CAN-138 bleibt ungeteilt** (Verlauf **und** Detailansicht) | Fünf Gründe: selber A0-Nutzerfluss · Detailansicht ist die unmittelbare Vertiefung des Verlaufs · gemeinsame Auslieferung über REQ-008 · gleiches Gate · gleiches lokales Aktivitätsmodell. **Kein Trennkriterium erfüllt** — mehrere Verben allein trennen nicht. REQ-008 bleibt auf diesen Umfang **verengt**; GPX-Export und Streckenvergleich gehören nicht dazu |
| (D4-d) | **CAN-140 wird geteilt** in Planungs- und Auswertungsfunktion | Deprecations 2026-07-20: **CAN-140 → CAN-142, CAN-143** · **REQ-040 → REQ-041, REQ-042** · **AC-040 → AC-042, AC-043** · **EV-040 → EV-043, EV-044** · **TRC-040 → TRC-041, TRC-042**. Tragender Grund: **REQ-041 ist heute vollständig spezifizierbar, REQ-042 ohne OQ-015 nicht.** Eine gemeinsame ID hätte die lieferbare Hälfte mitblockiert — oder die blockierte über die lieferbare als erledigt gelten lassen |
| (D4-e) | **Semantisch falsche Vision-Anker entfernt.** TRC-019 → VIS-003 · TRC-020 → VIS-004 · TRC-021 → VIS-004 · TRC-022 → VIS-003 (VIS-004 **einzeln geprüft und verworfen**) | VIS-008 ist die *Fairness Boundary* (getrennte Run-/Bike-Metriken) und trägt **keine** Community-Aussage. Vier Requirements hingen daran: syntaktisch gültig, plausibel lesbar, falsche Bedeutung — dieselbe Defektklasse wie VIS-009 ↔ REQ-014. **Keine Verknüpfung allein deshalb, weil die ID existiert** |
| (D4-f) | **Die verbotene Schlusskette „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" darf kein Anker sein** | Belegte Fundstellen: `traceability.md:1488`, `:1546` (REQ-037), `:1547` (REQ-038); gleiche Defektklasse zusätzlich `:1489`, `:1490` (REQ-039), `:1491` (REQ-040). **Folge: REQ-037, REQ-038 und REQ-039 haben keinen canvas-problem-Anker mehr** — das ist ein **BLOCKER**, kein zu füllendes Feld. Es wird kein CAN-Item umgedeutet und keine Problem-ID erfunden |
| (D4-g) | **EV-008 / EV-039 kanonisch getrennt** | EV-008 = **ausschließlich** Verlauf und Detailansicht · EV-039 = **ausschließlich** GPX-Kompatibilitäts- und Exportnachweis. Die Registry führte EV-008 noch mit „GPX-Kompatibilitätstest"; nach §1 hätte die **veraltete Registry-Definition** gewonnen und denselben Nachweis doppelt geführt. In `docs/EVIDENCE-LEDGER.md` nachgezogen |
| (D4-h) | **`NFR-`Einträge führen kein `blocking`**; die Achsen bleiben auf `OQ-`/`CONTRA-` beschränkt. **NFR-008 wird nicht deprecatet** | Keine Metamodell-Erweiterung. Die acht hartkodierten `blocking`-Werte in `prd.md:302-311` sind zu **entfernen**, nicht umzurechnen — sie waren genau die zuvor gemeldeten „8 von 14 ungeprüften" Werten. Die tragende Information steht in `evidence_gate = MISSING` und `evidence_status = not-planned` |
| (D4-i) | **Zählstände ausschließlich aus der Registry ableiten**; aktiv zählen, deprecated ausschließen, reserviert getrennt ausweisen. **Kein Validator darf die Literale 36 oder 39 verbieten oder erwarten** — weder als Erwartungs- noch als Verbotswert | Gilt für VIS, CAN, AC, TRC, EV, NFR, OQ, CONTRA. Ein Werkzeug, das einen Zählstand hartkodiert, bindet die Prüfung an einen Stand statt an die Quelle |

### Gemeldete Abweichungen von der wörtlichen Anweisung (Phase 1, überstimmbar)

Sie werden hier protokolliert, damit der Nutzer sie überstimmen kann; **nichts wurde still
uminterpretiert**.

| # | Wörtliche Anweisung | Was Phase 1 stattdessen getan hat | Begründung |
|---|---|---|---|
| 1–3 | „reserviere jeweils die nächste tatsächlich freie CAN-ID" für Accessibility, monochromes Design und GPX-Export | **Keine neue ID.** Der Wortlaut wurde auf die vorhandenen aktiven Items **CAN-099**, **CAN-141** und **CAN-139** gezogen | Für alle drei Aussagen existierten bereits aktive Items aus Runde 3. Drei neue IDs hätten drei **Dubletten** erzeugt — genau die Defektklasse, gegen die Abschnitt 3C derselben Nutzerentscheidung die Regel aufstellt („nicht beide aktiv lassen, eine ID als kanonisch bestimmen"). Wird die Abweichung überstimmt, sind CAN-099/139/141 zu deprecaten und drei neue IDs zu vergeben |
| 4 | Auftragsliste nannte nur neue **CAN-, REQ-, AC-, EV- und TRC-**IDs | Zusätzlich **VIS-014** reserviert (`reserved`, Inhalt **MISSING**) | REQ-041 hätte sonst keine reservierte Zieladresse und wäre in Phase 2/3 still an VIS-003 gehängt worden. `traceability.md:1702` hält bereits fest, dass für die Streckenwiederverwendung „kein Vision-Anker und keine reservierte VIS-ID" existiert. Präzedenzfall: VIS-012/VIS-013. Wird die Abweichung überstimmt, bleibt der Anker ein **BLOCKER ohne ID** |
| 5 | „Neue offene Fragen aus der Teilung mit den in Phase 1 **reservierten OQ-IDs**" anlegen | **Keine neue OQ-ID.** OQ-015 wandert vollständig auf REQ-042/AC-043/EV-044/CAN-143 und wurde im Wortlaut um „Streckenähnlichkeit" präzisiert | **Phase 1 hat in Runde 4 keine OQ-ID reserviert.** Die Registry führt keine OQ-ID über OQ-016 hinaus und ist eingefroren. Die Streckenähnlichkeit **ist** der Gegenstand von OQ-015 — eine zweite Frage wäre eine Dublette. Zwei ID-lose Punkte sind als Marken (h) und (i) in `docs/decisions/open-questions.md` geführt. Details dort |

## Nutzerentscheidungen 2026-07-20 (Runde 6) — Protokoll

**Provenienz.** Die folgenden Entscheidungen wurden als wörtliche Nutzeranweisung an diesen
Schritt weitergereicht. Sie sind hier **protokolliert, nicht bestätigt**. Der Dokumentstatus
bleibt `proposed – pending-user-confirmation`; kein Eintrag wird in fremdem Namen auf
`user-confirmed` gesetzt (RISK-024). Gesamtstatus unverändert **BLOCKED_TRACEABILITY**.

> **Mangel am Auftragstext selbst — nicht geglättet.** Der an diesen Schritt weitergereichte
> Auftrag nennt sowohl das Datum als auch den Repository-Pfad als **nicht interpolierten
> Platzhalter** (`undefined`, jeweils mehrfach). Gearbeitet wurde am Pfad
> `/Users/vincentschnetzer/Documents/Run&Bike`; als Laufdatum wird das **Systemdatum
> 2026-07-20** geführt. **Der Auftrag trägt damit kein prüfbares Eigendatum.** Für eine
> Entscheidungsspur ist das ein Mangel: die Datierung unten stammt aus der Laufumgebung, nicht
> aus der Anweisung. Sie wird hier festgehalten, **nicht** durch ein plausibles Datum ersetzt.

> **Verhältnis zu `DEC-014` — nachgetragen, nicht geglättet.** Ein **parallel laufender Schritt
> desselben Laufs** hat für Runde 6 die Nummer `DEC-014` vergeben (Zeile 20 oben). Sie deckt die
> Marken **(D6-d) … (D6-i)** sowie Teile von (D6-a)/(D6-b) inhaltlich ab. Die Marken **(D6-a) …
> (D6-k)** unten sind trotzdem **keine IDs**, sondern abschnittslokale Lesemarken; wo sie mit
> `DEC-014` überlappen, beschreiben sie dieselbe Entscheidung feiner aufgeschlüsselt. **Nicht von
> `DEC-014` gedeckt sind (D6-c)** (Pfadauflösung mit Äquivalenznachweis — `DEC-014` schreibt
> stattdessen „Keine Werkzeuglogik geändert", was für die Prüflogik zutrifft, für das
> Pfad-Literal aber nicht), **(D6-j)** (Freeze-Fortschreibung) und **(D6-k)**
> (Wesentlichkeitsregel).
>
> **BLOCKER, fortbestehend — der `DEC-`Raum ist weiterhin nicht verwaltet.** `docs/ID-REGISTRY.md`
> führt ihn ausdrücklich **nicht** (Registry §5; offener Punkt 11). `DEC-014` ist damit — wie
> DEC-011 … DEC-013 — in dieser Datei fortlaufend vergeben, aber **nicht kollisionsgeschützt**.
> Dass in derselben Runde ein Schritt eine DEC-Nummer vergibt und ein anderer Marken benutzt, ist
> genau das Defektmuster, das CONTRA-003 für den OQ-Raum bereits nachgewiesen hat. Der Befund hat
> sich **fortgesetzt**, nicht aufgelöst.
>
> **Zwei Sachangaben in `DEC-014` weichen von der Messung dieses Schritts ab** und sind vom Owner
> zu prüfen, nicht von hier aus zu korrigieren: (1) „11 Prüfwerkzeuge + Wrapper unter
> `scripts/validation/` **und** `tests/validation/`" — `tests/validation/` enthält am 2026-07-20
> gemessen **kein** Werkzeug, sondern drei Dateien (`HASHES.md`, `README.md`,
> `run_selftest.sh`); die Kette selbst liegt vollständig unter `scripts/validation/` (15
> übernommene Werkzeug- und Datendateien plus vier hier verfasste). (2) „**Keine Werkzeuglogik geändert**" trifft für Prüflogik,
> Schwellwerte, Ausgabetexte und Reihenfolge zu, **nicht** für das Repo-Pfad-Literal in fünf
> Dateien — siehe (D6-c) und `scripts/validation/EQUIVALENCE.md`.

| Marke (keine ID) | Entscheidung | Wirkung |
|---|---|---|
| (D6-a) | **Überführung der vier Upstream-Quellen ins Repository.** `SRC-001`…`SRC-004` liegen zusätzlich unter `docs/sources/` | Die Originale unter `~/Desktop/docs/` bestehen fort; beide Fundorte sind am 2026-07-20 als **byte- und SHA-256-identisch** gemessen (`docs/SOURCE-MAP.md` §1.6). **Keine SRC-ID vergeben, keine umgedeutet** — ergänzt ist ausschließlich ein zweiter, repo-relativer Fundort. **Welcher Fundort kanonisch ist, ist nicht entschieden** (OPEN QUESTION an den Nutzer, `SOURCE-MAP.md` §5) |
| (D6-b) | **Überführung der Validatorkette ins Repository.** Unter `scripts/validation/`: 15 übernommene Werkzeug- und Datendateien, dazu neu verfasst `run_all.sh`, `README.md`, `HASHES.md`, `EQUIVALENCE.md` (19 Dateien, mit `__pycache__/` 20 Einträge — selbst gezählt am 2026-07-20) | Registry §13.3 Nr. 4 führt genau diese Überführung als **Auftaugrund** des Werkzeug-Freezes. Sie ist hier als ausdrücklich beauftragter Schritt ausgeführt; der Freeze wird unten (D6-j) fortgeschrieben, nicht aufgehoben |
| (D6-c) | **Pfadauflösung von fünf Werkzeugen** (`xcheck.py`, `verify.py`, `verify_canvas.py`, `oq_check.py`, `AUDIT_points.py`): hartkodiertes Repo-Pfad-Literal → Auflösung aus dem Skriptort bzw. `REVYR_REPO` | Prüflogik, Schwellwerte, Ausgabetexte und Reihenfolge **nicht** angetastet. Äquivalenz byte-genau nachgewiesen (`scripts/validation/EQUIVALENCE.md`): stdout, stderr und Exit-Code aller fünf **identisch**. Die Äquivalenz belegt **nicht**, dass die Werkzeuge korrekt prüfen — sie belegt, dass die Kopie **denselben Defekt** unverändert reproduziert |
| (D6-d) | **CAN-119 klauselscharf getrennt.** Belegter Kern „Sichtbarkeits-Matrix (Testtabelle Plan 7)" bleibt `EXPLICIT`; „Privacy-Review" als eigenständiger Nachweisvorgang wird als `ASSUMPTION` geführt | Die Benennung „Privacy-Matrix" ist in keiner der vier Quellen gedeckt (`privacy[- ]?matrix`, `privacy[- ]?review`, `datenschutz`: **je 0 Treffer**). **Die Richtung der Aufspaltung ist strittig und nicht entschieden** — eine Prüflinse hält den *Review* für das herkunftsechte Glied (Canvas-Ursprungstext „Claims-, Privacy- und Threat-Model-Reviews.") und die Matrix für ein Zweitexemplar von EV-018. Der Streit ist in `SOURCE-MAP.md` §1.3.1 offengelegt, nicht geschlossen |
| (D6-e) | **VIS-003 verengt.** Kern (Tracking, verständliche statt abstrakte Auswertung, Fortschritt, Anschluss an lokale Sportler:innen und Teams) bleibt `EXPLICIT`; die Qualifizierer **„verlässlich"** (Tracking) und **„sicher"** (Zugang) werden abgetrennt und als `ASSUMPTION` geführt | „Trainingspartner", „Zugang", „verlässl", „Fortschrittssignal": **je 0 Treffer** über alle vier Quellen. Das Altverdikt hatte aus drei Fundstellen eine Verbundaussage gebaut. **Keine neue VIS-ID vergeben, kein Vision-Item umgedeutet.** Folgen für `CAN-017`, `CAN-028`, `CAN-031`, `TRC-004`, `TRC-022` sind als Nachzug offen — insbesondere ist **CAN-017 nicht aufzulösen**, es behält eine eigene Quellengrundlage |
| (D6-f) | **CAN-109 herabgestuft:** Source Type `EXPLICIT` → `ASSUMPTION`. Der Wortlaut bleibt unverändert | Die Quellen stellen eine **Urteilsregel** auf („Fehlende Sensoren allein sind kein Betrug, senken aber die Beweiskraft"), kein Risiko der Fehlklassifikation. Das Risikoregister von SRC-003 enthält keine entsprechende Zeile. Herabgestuft wird der Source Type, **nicht** die Aussage; es wurde nichts gelöscht und nichts umgedeutet |
| (D6-g) | **CAN-024 verengt** auf „Radfahrer:innen (Rangstufe primär)". Source Type `EXPLICIT` bleibt | „Renn-" steht in SRC-001 ausschließlich im **sekundären** Aufzählungspunkt und dort untrennbar mit „Ambitionierte"; „Freizeit-" ist orthographisch nur an „Läufer:innen" gebunden. Der Rangzusatz ist tragend: ohne ihn umfasst das Atom begrifflich die ambitionierten Rennradfahrenden und überschneidet sich mit CAN-025. **Folge, offen:** REQ-032 verliert damit seinen belegten Anker für den **Bike-Sensorik**-Bedarf; der verbleibende Träger CAN-025 → USER-004 ist `ASSUMPTION` mit ausdrücklichem BLOCKER |
| (D6-h) | **CAN-099: die Erstreckung auf „nutzbare Web-Auskopplungen" ist aus dem Wortlaut entfernt.** Source Type wird gespalten geführt: `EXPLICIT` für den belegten Kern, `ASSUMPTION` für die benannten Details | Kein Accessibility-Abschnitt der vier Quellen nennt Web; die vier „Web-Auskopplung"-Fundstellen betreffen ausschließlich die CSS-Farbmisch-Regel. **Ausdrücklich nicht als Begründung übernommen:** „widerspricht der Quelle in der Richtung" — SRC-001 nimmt den Beschützer-Link vom Nicht-Ziel ausdrücklich aus. Es ist ein **Belegmangel, kein Widerspruch**. Weiterhin nicht quellengedeckt und als `ASSUMPTION` mitgeführt: Fassungsziffer **2.2**, „ausreichende Bedienflächen", „nachvollziehbare Fokusführung", „motorische/assistive Anforderungen" |
| (D6-i) | **REQ-007 bleibt `ASSUMPTION` bis zur ausdrücklichen Nutzerbestätigung.** Wortlaut unverändert, nichts verengt, nichts abgeschwächt | REQ-007 ist keine Ableitung, sondern eine **bewusste Abweichung von SRC-004**, das die einfache Distanzsubtraktion wörtlich spezifiziert und als Sollverhalten testet. Alleiniger Träger ist SRC-005/**DEC-004**, und DEC-004 steht in dieser Datei auf `proposed`. SRC-005 ist laut `SOURCE-MAP.md` ein interner Befundsatz, **keine Nutzerquelle**. Die numerischen Schwellen (Korridor, Hysterese, Latenz) fehlen in allen vier Quellen — der `MISSING`-Wert im Messmodell betrifft den **Zielwert** und ist davon unberührt |
| (D6-j) | **Freeze von Quellenmodell, Registry und Validatoren fortgeschrieben** (eigener Abschnitt unten) | Der Freeze wird **nicht** aufgehoben. Ersetzt wird ausschließlich der `location_caveat` — und nur so weit, wie der Import es belegt |

### (D6-k) Wesentlichkeitsregel für „trägt-teilweise" — Berichtsstufe, **kein** Eingang der Blocking-Formel

Die Regel ist als Vorschlag protokolliert und **nicht in Kraft gesetzt**; ihre Verortung ist
`docs/ID-REGISTRY.md` §3.2, und die Registry ist eingefroren. Diese Datei ändert sie nicht.

Vorab die Feststellung, die den Zuschnitt bestimmt: **keiner der drei Marker ist heute ein
Eingang der kanonischen Blocking-Formel.** `blocking` gilt ausschließlich für `OQ-` und
`CONTRA-` (Registry §3.1, Abschnitt „Geltungsbereich" oben). `TEILBELEGT` bewertet Zellen,
`linked-partial` bewertet Traceability-Zeilen, `trägt-teilweise` bewertet Anker — keine dieser
Kennungen führt das Feld `blocking`. Die Regel kann die Formel deshalb **nicht entlasten**; sie
steuert allein, ob ein Teilbefund als BLOCKER oder als Nachzug berichtet wird.

Ein teilbelegter Befund wird als **BLOCKER** geführt, wenn mindestens eine Bedingung erfüllt ist:

- **W1** — der nicht getragene Teil erscheint im Wortlaut des Akzeptanzkriteriums des tragenden
  Requirements.
- **W1b** — hilfsweise für Items ohne eigenes AC: er erscheint im AC eines Requirements, das das
  Item ausdrücklich als Anker führt. **W1b ist die schwächste Bedingung** (sie nutzt ein
  Zwischenglied) und bei jeder Anwendung als solche zu kennzeichnen.
- **W2** — er ist selbst eine Vorbedingung („erst nach…", „nur wenn…", „MUSS vor…") oder
  begründet eine Nachweispflicht mit `EV-`Eintrag.
- **W3** — er erweitert den Geltungsbereich auf eine **Plattform, Nutzergruppe, Datenart oder
  Artefaktklasse**, die sonst nicht umfasst wäre. Eine Erweiterung des bloßen *Funktionsbereichs*
  genügt **nicht**.
- **Ausschluss** — ist der Teil in einer der vier Quellen wortnah belegt und nur die SRC-Angabe
  falsch, ist der Fall unabhängig von W1–W3 ein **Quellennachzug**, kein Wesentlichkeitsbefund.

Probeanwendung auf die 17 `TEILBELEGT`-Fälle: **13 bleiben, 4 werden entblockt**; ohne W1b
**11 bleiben, 6 werden entblockt**. Ausdrücklich kontrafaktisch — von den 17 ist heute genau
**einer** repo-seitig als BLOCKER geführt (CAN-051), zwei als Nachzug, **13 überhaupt nicht**.

**Zwingende Nebenpflicht.** Trifft die Regel mehrere Zellen derselben fortgepflanzten Lücke
ungleich (etwa „versioniert" in VIS-008, REQ-023, REQ-001), ist die Lücke **als Kette**
weiterzuführen, auch wenn einzelne Glieder herabgestuft werden. Eine Kette darf nicht dadurch
verschwinden, dass ihre Glieder einzeln unwesentlich sind. **Vorbehalt:** die Regel macht
AC-Wortlaute zum Maßstab, und mehrere AC sind selbst `TEILBELEGT`. Sie heilt das nicht.

> **BLOCKER — die Regel steht auf nicht referenzierbaren Bezugsdokumenten.** Die 23
> `trägt-teilweise` stammen aus `scratchpad/semantic-review.md`, das **nicht** ins Repository
> überführt wurde (Ausschlussliste in `scripts/validation/HASHES.md`). `src-verification.json`
> liegt inzwischen unter `scripts/validation/`, ist dort aber **byte-identisch und damit
> inhaltlich veraltet** (`109/17/5` statt `105/20/6`). Jede Zahl dieser Regel erbt beide Defekte.

### Fortbestehender BLOCKER — die **vierte** Entscheidungstranche hat keine SRC-ID

Die Entscheidungen (D6-a) … (D6-k) bilden eine **vierte, inhaltlich getrennte Tranche** von
Nutzerentscheidungen. Sie ist weder in `SRC-006` enthalten noch anderweitig referenzierbar.

**Das ist ein fortbestehender, kein gelöster Blocker.** `docs/SOURCE-MAP.md` §2.1 führt dieselbe
Lage für die **zweite** Tranche (2026-07-19, Auftau-Schritt 2), §2.2 für die **dritte**
(2026-07-20, Runde 4). Der Stand lautet damit: **vier Tranchen, eine ID.** Wer `SRC-006`
referenziert, meint die erste; drei Tranchen sind überhaupt nicht referenzierbar.

Es wurde **erneut keine SRC-ID vergeben und `SRC-006` nicht erweitert** — aus den beiden in
`SOURCE-MAP.md` §2.1 ausgeschriebenen Gründen, die hier unverändert gelten: eine Erweiterung
wäre eine stille Umdeutung einer bestehenden ID, eine neue Nummer eine ID-Vergabe außerhalb des
dafür vorgesehenen Schritts. Es wird hier auch **keine konkrete Nummer genannt**.

Verschärfend gegenüber Runde 4: der Schaden ist jetzt nicht mehr auf hochgestufte Canvas-Items
beschränkt. **Auch die Herabstufungen und Verengungen (D6-d) … (D6-i) stützen sich auf diese
Tranche.** Eine spätere Prüfung, warum CAN-109 auf `ASSUMPTION` steht oder warum CAN-099 die
Web-Erstreckung verloren hat, findet als Beleg einen Freitext und keine ID.

**Zu entscheiden vom Nutzer:** je eine SRC-ID für die zweite, dritte und vierte Tranche vergeben
— oder den Geltungsbereich von `SRC-006` ausdrücklich und **datiert** erweitern.

## Freeze — Quellenmodell, Registry und Validatoren (Fortschreibung 2026-07-20, Runde 6)

**Dieser Abschnitt hebt keinen Freeze auf und vergibt keine ID.** Kanonische Quelle des Freezes
bleibt `docs/ID-REGISTRY.md` §13; diese Datei hält fest, was der Lauf vom 2026-07-20 daran
belegt hat — und was nicht. Bei Abweichung gilt die Registry (§1).

### Was eingefroren bleibt

| Gegenstand | Umfang |
|---|---|
| **Quellenmodell** | `SRC-001`…`SRC-008`, ihre Bedeutung und ihre Zuordnung. Der Import hat **einen zweiten Fundort** ergänzt, nicht das Modell geändert |
| **Metamodell** | Achsen und Vokabulare (`source_type`, `measurement_type`, `evidence_status`, `item_type`, Release-Stufen), die Blocking-Formel `status NOT IN ['resolved']` (fail-closed), die Beschränkung von `blocking` auf `OQ-`/`CONTRA-`, die Zählregel |
| **Registry** | der ID-Bestand aller zwölf verwalteten Präfixe |
| **Validatorkette** | `validate_intake.py`, `validate_trace.py`, `check_prd.py`, `validate_schema.py`, `selftest_validator.py`, `verify.py`, `verify_canvas.py`, `xcheck.py`, `oq_check.py`, `blocking_model.py`, `registry_model.py`, `intake-package.schema.json` |
| **Ankersemantik** | wird **nicht** maschinell geführt; ausschließlich review-geführt. Es wird **kein** neuer Semantikvalidator gebaut |

**Nicht eingefroren:** Dokumentinhalte, die Auflösung von Blockern, die Vergabe von IDs durch den
Nutzer, die manuelle Ankerreview.

### Der `location_caveat` ist erledigt — und nur so weit, wie der Import ihn erledigt

Der bisherige Vermerk in `intake-package.json` → `tooling_freeze.location_caveat` lautet:

> „KRITISCH: `blocking_model.py` und die uebrigen Werkzeuge liegen im SCRATCHPAD, NICHT im
> Repository. Ein Freeze aendert daran nichts. Ausserhalb dieser Session sind sie NICHT
> verfuegbar und jedes hier berichtete Ergebnis ist dann nicht reproduzierbar. Registry §8
> Punkt 13 und Punkt 33 bleiben deshalb OFFEN und werden durch die Scratchpad-Werkzeuge NICHT
> geschlossen."

**Seine erste Hälfte ist durch (D6-b) tatsächlich überholt.** Am 2026-07-20 im Repository
verifiziert: `scripts/validation/` führt die gesamte Kette einschließlich `blocking_model.py`,
`intake-package.schema.json` und `src-verification.json`; `docs/sources/` führt SRC-001…SRC-004.
Die Werkzeuge sind damit **außerhalb der Ursprungssession verfügbar** und die Kette ist über
`run_all.sh` aufrufbar. **Seine zweite Hälfte ist nicht überholt** — dazu unten.

Ersatzwortlaut, den der Owner von `intake-package.json` einzutragen hat (diese Datei ändert die
JSON **nicht**; sie gehört einem anderen Owner):

> Die Werkzeuge liegen seit dem 2026-07-20 unter `scripts/validation/`, die Quellen unter
> `docs/sources/`. Der frühere Scratchpad-Vorbehalt ist damit erledigt. **Drei Einschränkungen
> bleiben:** (1) das Repository steht **nicht unter Versionskontrolle** — am 2026-07-20 gemessen:
> kein `.git`-Verzeichnis; „im Repository" heißt **nicht** „versioniert", einzige
> Integritätsanker sind die SHA-256-Summen in `scripts/validation/HASHES.md`. (2)
> `selftest_validator.py:22` und `gen_intake.py:19` sind **nicht** pfad-überschreibbar (kein
> `argv`, kein `environ`); am Klon gemessen nimmt `selftest_validator.py` dort die Werkzeuge des
> Klons, prüft sie aber **lautlos gegen die Dokumente des Originalrepositorys**. Die Zusage
> „läuft aus jedem Klon" gilt nur mit dieser Einschränkung. (3) `src-verification.json` ist
> byte-identisch übernommen und damit **inhaltlich veraltet** (`109/17/5` statt `105/20/6`,
> Desktop-Pfade in `quellen[*].pfad`).

**Registry §8 Punkt 13 und Punkt 33 werden hier NICHT auf geschlossen gesetzt.** Der Freeze ist
kein Ablageort, und ein Ablageortwechsel ist kein Ausführungsnachweis — das hat Registry §13.2
bereits festgehalten. Was dieser Lauf **zusätzlich** erbracht hat, ist beides: ein
**ausgeführter** Kettenlauf (`run_all.sh`, 7:14 min, Exit-Code 1, `PASS=6 FAIL=4 INFO/SKIP=1`)
und ein **byte-genauer Äquivalenznachweis** für die fünf geänderten Werkzeuge. Damit ist die in
§13.2 genannte Begründung für das Offenbleiben („kein Validator ausgeführt, kein Ergebnis
reproduziert, keine Äquivalenz geprüft") überholt. **Ob die beiden Punkte dadurch schließen,
entscheidet der Owner der Registry — nicht dieser Schritt**, und die Registry ist eingefroren.
Bis dahin bleiben beide **OFFEN**.

### Bedingungen fürs Auftauen

Ein Auftauen ist **nur** durch eine ausdrückliche Nutzerentscheidung möglich, und nur bei einem
dieser Anlässe (unverändert aus Registry §13.3, ergänzt um Nr. 5):

1. Eine **neue oder geänderte SRC-Quelle** — SRC-001…SRC-004 ändern sich (nachweisbar über die
   SHA-256-Summen in `SOURCE-MAP.md` §1.1/§1.6), oder
   `RUNNING_CYCLING_APP_KONZEPT_CHAT_ZUSAMMENFASSUNG.md` wird als Quelle aufgenommen.
2. Eine **neue ID-Klasse** oder ein **neues Achsenvokabular**.
3. Eine **Nutzerentscheidung, die eine bestehende Achse umdefiniert** (etwa die Blocking-Formel
   oder die Release-Stufen).
4. Die **Überführung der Werkzeuge ins Repository** — in Runde 6 als (D6-b) ausgeführt und damit
   für diesen Anlass **verbraucht**. Ein erneutes Auftauen aus diesem Grund erfordert einen
   neuen Anlass, nicht die Wiederholung dieses Arguments.
5. **Neu:** die **Vergabe der fehlenden SRC-IDs** für die zweite, dritte und vierte
   Entscheidungstranche. Sie berührt das Quellenmodell und ist ohne Auftauen nicht durchführbar.

Ausdrücklich **kein** Auftaugrund: ein fehlgeschlagener Check. Ein Fehlschlag ist ein **Befund**
und wird am Dokument behoben, **nicht** am Werkzeug. Die drei aktenkundigen
Werkzeug-Falschmeldungen (`verify.py` D-Tally mit veraltetem hartkodiertem Literal, `verify_canvas.py` ohne
Honorierung maskierter Pipes, `oq_check.py` mit unvollständigem Themenklassifikator)
reproduzieren in der Repo-Kopie **unverändert** und sind in `scripts/validation/README.md`
offengelegt. Sie wurden **nicht** korrigiert.

Ebenfalls **kein** Auftaugrund: die Pfadauflösung (D6-c). Sie war beauftragt, ist auf fünf
Dateien begrenzt und byte-genau äquivalenzbelegt; Prüflogik, Schwellwerte und Ausgaben blieben
unangetastet. Die beiden nicht überschreibbaren Werkzeuge wurden deshalb **nicht** angefasst —
ihre Korrektur wäre ein Eingriff in eingefrorenen Bestand und war nicht beauftragt.

## Was dieser Lauf freigibt — und was ausdrücklich nicht

**Freigegeben ist ausschließlich der Start von P0-02 und P0-03 als technische Spikes.**

| | |
|---|---|
| **P0-02** | `TrackPointV1` (REQ-004) — als **technischer Spike** |
| **P0-03** | Lokale Persistenz (REQ-005; der Delivery Plan führt zusätzlich REQ-017 und REQ-027) — als **technischer Spike** |

**Nicht freigegeben, ausdrücklich und einzeln:**

- **Keine Gate-Abnahme.** Kein Gate-Status wurde verändert; P0, A0, A1, A2, B, C, D und E stehen
  unverändert auf `pending` (`docs/EVIDENCE-LEDGER.md`, Gate Summary).
- **Keine weitere Produktimplementierung** außerhalb dieser beiden Spikes.
- **Keine Abnahme der beiden Spikes selbst.** Beide sind lauffähig planbar, aber **nicht
  abnehmbar**: für P0-02 deckt die Task-Acceptance („Schema + Fixtures + Serialisierungstest")
  den von AC-004 verlangten Klassifikationsnachweis nicht ab; für P0-03 ist die zweite Hälfte
  der Task-Acceptance (Trennung Identität ↔ historische Aggregate, CONTRA-005) über
  **EV-042 = `blocked`** strukturell nicht abnehmbar, solange OQ-009 offen ist.
- **P0-03 darf kein Schema finalisieren.** Die Zeitpunktregel zu CONTRA-005 verlangt die Trennung
  **vor** der Finalisierung; wer den Spike danach als erledigt führte, ließe die blockierte
  Hälfte über die lieferbare gelten.
- **Kein A0-Routing.** CONTRA-006 trägt `blocked_gates = [A0]`, `blocking = true`; die
  A0-Routing-Evidence (a)…(n) ist vollständig `nicht erbracht`.

Beide Spikes stehen zusätzlich unter zwei ungelösten Vorbehalten, die hier **nicht** geschlossen
werden: **kein benannter Owner/DRI** und **Referenzgeräte MISSING** — damit ist die für EV-004
und EV-005 geforderte Mindestklasse `real-boundary-smoke` nicht erreichbar.

## Contradiction Ledger

Widersprüche dürfen nicht stillschweigend weitergetragen und nur durch eine vom Nutzer bestätigte Auflösung geschlossen werden — nicht durch Agent-Konsens, „bekannte Einschränkung" oder Abschlussdruck.

Ein `resolved` in diesem Ledger bezeichnet eine **entschiedene Grundsatzfrage**, nicht einen
erbrachten Nachweis. Die Implementierungs-Evidence zu CONTRA-004, CONTRA-005 und CONTRA-006
steht vollständig aus und ist in `docs/EVIDENCE-LEDGER.md` als offen geführt.

### Statusmodell je CONTRA-ID (Nutzerentscheidung 2026-07-19, Felder nach Registry §3.1)

Bis zum 2026-07-19 trug die Spalte „Status" zwei unabhängige Fragen zugleich — „ist der
Widerspruch entschieden?" und „ist die Erfüllung nachgewiesen?". Daraus entstand für CONTRA-006
der Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING`, der als `status` **unzulässig** ist
(Registry §3.1) und in keiner Prüfung auswertbar war. Die beiden Fragen haben jetzt getrennte
Felder.

**Kanonische Quelle der Feldwerte ist `docs/ID-REGISTRY.md` §6.11.1.** Die folgende Tabelle ist
mit ihr wortgleich zu halten; bei Abweichung gilt die Registry. Die Spalte „Status" der
Widerspruchstabelle unten führt ab jetzt **ausschließlich** `open` | `resolved`.

### Semantik von `evidence_status` (projektweit, Nutzerentscheidung 2026-07-19)

| Wert | Bedeutung |
|---|---|
| `not-planned` | Es existiert noch **kein Messkonzept**. |
| `planned` | Metrik, Berechnung und zuständiges Gate sind definiert, die **Instrumentierung fehlt**. |
| `pending` | **Instrumentierung implementiert**, aber Messdaten oder Messfenster fehlen noch. |
| `verified` | Zielwert mit ausreichender, dokumentierter Evidenz geprüft. |
| `not-required` | Requirement-spezifisch begründete Nichtanwendbarkeit — **nie pauschal**. |
| `failed` | Nachweis versucht und gescheitert. |
| `blocked` | Nachweis durch einen anderen offenen Punkt versperrt. |

Die Grenze zwischen `planned` und `pending` ist die **Instrumentierung**, nicht die Absicht.

**BEFUND — die Semantik trägt die CONTRA-Einträge nicht (neu, 2026-07-19).** Die vier Stufen sind
über *Instrumentierung* definiert und damit auf **Code-Evidenz** zugeschnitten. Daraus folgt für
diese Datei ein ungelöster Widerspruch, der hier festgehalten und **nicht** durch eine stille
Umwertung geglättet wird:

- CONTRA-002, -003, -004, -005 und -006 tragen `evidence_status = pending`. Das ist die
  ausdrückliche Nutzervorgabe vom 2026-07-19 und wird deshalb **unverändert geführt**.
- Zugleich existiert im Repository **kein Code** — nichts kann instrumentiert sein. Nach der
  wörtlichen Semantik stünde ein Eintrag ohne Code höchstens auf `planned`.
- Ein Teil der betroffenen Nachweise ist überdies **gar keine Instrumentierung**: die
  CONTRA-006-Belege (o)…(u) sind Auftragsverarbeitungsvertrag, Transfergrundlage und
  Datenschutzerklärung — Dokumentnachweise, für die „Instrumentierung implementiert" keine
  sinnvolle Bedingung ist.

**Zu entscheiden vom Nutzer:** entweder wird `pending` für nicht-instrumentierbare Evidenz
(Rechts-, Vertrags- und Auditnachweise) ausdrücklich zugelassen, oder die CONTRA-Werte werden auf
`planned` bzw. `not-planned` korrigiert. Bis dahin gilt die ausdrückliche Vorgabe (`pending`), und
die Abweichung ist dokumentiert statt umgeschrieben. Der Widerspruch berührt **kein**
`blocking`-Ergebnis: alle fünf Einträge sind bereits über `blocked_gates`/`blocked_activities`
blockierend, und `planned` wie `pending` lösen für sich genommen ohnehin keine Blockade aus.

### Feldwechsel `blocking_scope` → `blocked_gates` + `blocked_activities` (C16, Nutzerentscheidung 2026-07-19)

Das Feld `blocking_scope` ist **projektweit entfallen**. Es mischte Release-Gates und Tätigkeiten
in einer Liste; die Vokabulare sind disjunkt, weshalb die wörtliche Lesart der Formel für jeden
gegateten Eintrag `false` lieferte — die Blockade verschwand genau dann, wenn gegen ein Gate
geprüft wurde. Ersatz sind **zwei getrennte Felder** mit **abgeschlossenen, disjunkten**
Wertebereichen:

- `blocked_gates` ∈ { `P0`, `A0`, `A1`, `A2`, `B`, `C`, `D`, `E` }
- `blocked_activities` ∈ { `documentation`, `planning`, `implementation`, `field-test`,
  `release`, `store-submission`, `database-schema-finalization`, `account-release`,
  `competition-release`, `territory-release` }

**Kanonische Berechnung** (normativ, Registry §3.1 / `blocking_model`):

```
blocking = status            NOT IN ['resolved']
        OR resolution_status NOT IN ['accepted']
        OR evidence_status   IN ['failed','blocked']
        OR current_gate      IN blocked_gates
        OR current_activity  IN blocked_activities
```

**Wortlaut verbindlich, präzisiert 2026-07-20.** Die erste Klausel lautet `status NOT IN
['resolved']` — **ausdrücklich nicht** `status == 'open'`. Für die beiden gültigen Werte sind
beide Fassungen äquivalent; für einen **fehlenden, leeren oder ungültigen** `status` sind sie es
nicht: `status == 'open'` liefert dann `false` (nicht blockierend), `status NOT IN ['resolved']`
liefert `true`. **Die Berechnung ist `fail-closed`** — ein Eintrag ohne `status` blockiert und ist
zusätzlich ein **Validierungsfehler**, kein Toleranzfall. Frühere Berichte zitierten die Formel
als „`status == open`"; **Wortlaut und jede spätere Implementierung folgen dieser Fassung, nicht
umgekehrt.** Ein Prüfwerkzeug, das die verbotene Fassung implementiert, meldet für genau die
Einträge `false`, deren Daten unvollständig sind — also dort, wo eine Blockade am nötigsten wäre.

**Geltungsbereich: `OQ-` und `CONTRA-`.** Andere ID-Räume führen **kein** `blocking`; siehe die
Entscheidung zum `NFR-`Raum im Protokoll vom 2026-07-20 unten.

`current_gate` wird **ausschließlich** gegen `blocked_gates` geprüft, `current_activity`
**ausschließlich** gegen `blocked_activities`. Gate-Bezeichner und Tätigkeitsbezeichner werden
**niemals** miteinander verglichen. Ist eines von beiden nicht gesetzt, entfällt nur die
zugehörige Klausel; die übrigen bleiben in Kraft. Eine leere `blocked_gates`-Liste bedeutet
„blockiert kein Gate", nicht „blockiert nie". Ein Gate-Bezeichner in `blocked_activities` (oder
umgekehrt) ist ein Validierungsfehler, kein Toleranzfall.

`blocking` wird **berechnet, nie gelesen**. Die Spalte unten zeigt das Ergebnis der Berechnung am
jeweils **eigenen** `evidence_gate` bzw. an der eigenen Leittätigkeit des Eintrags. Wer gegen ein
anderes Gate oder eine andere Tätigkeit prüft, leitet neu ab und übernimmt den Tabellenwert
nicht. Hartkodierte Werte je ID sind unzulässig.

| id | status | resolution_status | evidence_status | blocked_gates | blocked_activities | evidence_gate | blocking (berechnet, am eigenen Gate/an eigener Tätigkeit) | decision_reference | evidence_reference |
|---|---|---|---|---|---|---|---|---|---|
| CONTRA-001 | resolved | accepted | not-required | — (leer) | — (leer) | — | **false** — an jedem Gate und jeder Tätigkeit | CONTRA-001 (dieser Ledger), `CLAUDE.md`-Korrektur | — |
| CONTRA-002 | resolved | accepted | pending | `A0` | `implementation`, `release` | A0 | **true** — `A0` ∈ `blocked_gates` | DEC-005 (`user-confirmed`), CONTRA-002 (dieser Ledger), SRC-006 | ASM-103 (Bundle-Scan ohne Routing-Key + Proxy-Integrationstest), EV-034 |
| CONTRA-003 | resolved | accepted | pending | — (leer) | `documentation` | — | **false an jedem Gate** · **true** bei `current_activity = documentation` — siehe Anmerkung unten | CONTRA-003 (dieser Ledger), `docs/decisions/open-questions.md` als kanonisches Register | **MISSING** — siehe Anmerkung unten |
| CONTRA-004 | resolved | accepted | pending | `C`, `D` | `competition-release`, `territory-release` | C | **true** — `C` ∈ `blocked_gates` | DEC-011 | EV-024, EV-034 (teilweise) |
| CONTRA-005 | resolved | accepted | pending | `B` | `database-schema-finalization`, `account-release` | B | **true** — `B` ∈ `blocked_gates` | DEC-012 | EV-017, EV-027 (teilweise), **EV-042** (Trennung Identität ↔ historische Aggregate) |
| CONTRA-006 | resolved | accepted | pending | `A0` | `field-test`, `release` | A0 | **true** — `A0` ∈ `blocked_gates` | OQ-011, DEC-013, **ADR zum A0-Routing-Proxy = MISSING** | EV-006, EV-034; A0-Routing-Evidence (a)…(n) laut `docs/EVIDENCE-LEDGER.md` |

**Was die Nachrechnung ergeben hat — und was daran ein Befund ist.** Die `blocking`-Werte sind
mit dieser Änderung erstmals **nachgerechnet** statt übernommen. Unter der alten Formel hätten
CONTRA-002, -004, -005 und -006 an ihrem **eigenen** Gate `false` ergeben; die Tabelle führte sie
dennoch auf `true`. Die Werte waren also faktisch **hartkodiert** und nur deshalb inhaltlich
richtig, weil ein Mensch sie ausgelegt hat. Unter der neuen Formel ergibt die Rechnung dieselben
vier `true` — jetzt aber **maschinell reproduzierbar**. Das frühere Urteil „nicht die Daten waren
defekt, sondern das Prüfinstrument" war für die vier Ergebniswerte zutreffend, für die Aussage
„`blocking` ist abgeleitet" jedoch **nicht**: abgeleitet war es nicht, sondern gesetzt.

**CONTRA-003 blockiert kein Gate.** Sein einziger Eintrag steht in `blocked_activities`. Eine
Prüfung, die ausschließlich Gates auswertet, meldet für CONTRA-003 korrekt `false` — und übersieht
die Blockade trotzdem. Der Eintrag ist **nur** über `current_activity = documentation` sichtbar.
Das ist kein Datenfehler, sondern die Eigenschaft eines rein tätigkeitsgebundenen Blockers; ein
Prüfwerkzeug muss beide Achsen auswerten, sonst ist es blind für diese Klasse.

**`rationale` zu den drei durch die Nutzerentscheidung vorgegebenen Einträgen**

- **CONTRA-004** — Die Kollision zwischen serverseitiger Anti-Cheat-Plausibilität und der
  Datenminimierung aus REQ-034 ist durch DEC-011 entschieden: nur minimierte, abgeleitete
  Plausibilitätssignale verlassen das Gerät. Der Nachweis, dass der Server tatsächlich **nur**
  diese Signale empfängt und dass fehlende Sensoren nie automatisch zu `rejected` führen, setzt
  laufenden Code und Betrugsfixtures voraus — es existiert kein Code.
- **CONTRA-005** — Die Kollision zwischen „unveränderlicher Historie" und dem Löschanspruch ist
  durch DEC-012 entschieden. Der Nachweis der technischen Trennung von Identität und
  historischen Aggregaten ist **vor** Finalisierung des Datenbankschemas fällig; ein Schema
  existiert nicht. Für diese Trennung ist seit dem 2026-07-19 **EV-042** reserviert (zuvor
  „keine EV-ID"); der Nachweis selbst steht auf `evidence_status = blocked`, weil die
  Retentionsfristen (OQ-009) fehlen — das Schema ist ohne sie nicht belastbar entwerfbar.
- **CONTRA-006** — Die Kollision zwischen Local-first und serverseitigem Routing ist durch die
  Entscheidung für einen transienten, datenminimierten EU-Routing-Proxy gelöst; der Nachweis der
  Privacy-, Logging-, Retention- und Security-Eigenschaften steht aus.

**MISSING — `decision_reference` von CONTRA-006 unvollständig.** Die Nutzerentscheidung nennt als
Entscheidungsbeleg neben OQ-011 einen „ADR zum A0-Routing-Proxy". Ein solches Dokument existiert
im Repository **nicht** (`find docs -iname "*adr*"` am 2026-07-19: kein Treffer). Die Referenz
wird deshalb als **MISSING** geführt und **nicht** stillschweigend durch DEC-013 ersetzt — DEC-013
ist die Privacy-Baseline, nicht der Architekturentscheid über den Proxy als solchen. Das Anlegen
des ADR liegt beim Architektur-Owner.

**MISSING — `evidence_reference` von CONTRA-003.** `docs/decisions/open-questions.md` ist als
einziges kanonisches OQ-Register festgelegt; die im Ledger-Eintrag CONTRA-003 behauptete
maschinelle 1:1-Prüfung ID↔Entscheidung ist jedoch **nicht belegt**: Registry §9 hält fest, dass
im Repository überhaupt kein ausführbares Prüfwerkzeug existiert. Die Prüfung wird deshalb nicht
als erbracht geführt, und `evidence_status` bleibt `pending` bei
`blocked_activities = [documentation]`.

**GESCHLOSSEN — die frühere `blocking`-Formel war nicht maschinell auswertbar.** Der am
2026-07-19 festgehaltene Befund lautete: die letzte Klausel verglich einen **Gate-Bezeichner** mit
einer **Tätigkeitsliste**, zwei Vokabulare mit leerer Schnittmenge. Eine Prüfung, die die Klausel
als String-Enthaltensein implementierte, lieferte für **jeden** Eintrag mit echtem Gate `false` —
genau das stillschweigende Absinken auf `false`, das §3.1 verhindern will. Die Prüfung schlug für
CONTRA-002, -004, -005 und -006 an.

**Der Befund ist durch die Nutzerentscheidung C16 vom 2026-07-19 behoben, nicht weggeschrieben.**
`blocking_scope` ist ersatzlos entfallen; an seine Stelle treten `blocked_gates` und
`blocked_activities` mit abgeschlossenen, disjunkten Wertebereichen (siehe Abschnitt
„Feldwechsel" oben). Die Zuordnung Gate → Tätigkeiten, die zuvor in **keinem** Artefakt definiert
war und die Formel auf menschliche Auslegung angewiesen machte, wird dadurch **nicht mehr
gebraucht**: beide Achsen werden getrennt und wörtlich ausgewertet. Die Umstellung ist die
zweite der beiden damals vorgeschlagenen Optionen — sie wurde vom Nutzer entschieden, nicht von
der Assistenz gewählt.

**GESCHLOSSEN — Wertebereich.** Die vier Werte `competition-release`, `territory-release`,
`database-schema-finalization` und `account-release` lagen zuvor außerhalb der Basis-Liste, was
als offener Konflikt geführt wurde. C16 löst ihn auf: das Tätigkeitsvokabular ist jetzt
**abgeschlossen** und enthält alle vier ausdrücklich. Damit kehrt sich die Validator-Regel um —
ein unbekannter Wert in `blocked_gates` oder `blocked_activities` ist ab jetzt ein **Fehler**,
kein Toleranzfall.

**BLOCKER — es existiert keine gemeinsame Implementierung der Blocking-Funktion.** §3.1 verlangt,
dass **alle** Validatoren dieselbe Implementierung importieren — keine Duplikate, keine
abweichende Fassung, keine ID-spezifische Sonderbehandlung. Im Repository existiert derzeit
**überhaupt kein ausführbares Prüfwerkzeug** (Registry §9). Die Formel oben ist die normative
Spezifikation jeder späteren Implementierung; sie ist **kein** erbrachter Nachweis, dass irgendwo
korrekt gerechnet wird. In diesem Schritt wurde bewusst kein Code geschrieben.

**BLOCKER — `blocking_scope` lebt außerhalb dieser Datei weiter.** Stand 2026-07-19 (Messung des
Auftau-Schritts 2) stand das entfallene Feld noch in sechs Dateien mit zusammen 52 Fundstellen.
Diese Datei (9) und `docs/EVIDENCE-LEDGER.md` (1) sind mit dieser Änderung bereinigt. Offen
bleiben:

| Datei | Fundstellen (Stand 2026-07-19) | Owner |
|---|---|---|
| `docs/traceability.md` | 20 | Traceability-Owner |
| `docs/prd/revyr-endurance-platform.prd.md` | 14 | PRD-Owner |
| `docs/validation/validation-report.md` | 7 | Owner des Validierungsberichts |
| `docs/vision/revyr-endurance-platform.vision.md` | 1 | Vision-Owner |

**Ergänzung 2026-07-20 — auch außerhalb der Dokumente.** `nfr-audit.json` führt `blocking_scope`
weiterhin **lebend** und mischt dort zusätzlich die Vokabulare (u. a. der Wert `["none"]`, der in
keinem der beiden abgeschlossenen Wertebereiche vorkommt). Die Datei liegt nicht im Repository und
gehört nicht zu dieser Datei; der Befund wird hier verzeichnet, damit er nicht dadurch verschwindet,
dass er in keinem versionierten Artefakt steht. **Ein lebendes `blocking_scope` in einem Werkzeug
ist schwerwiegender als eines in einem Dokument** — das Dokument wird gelesen, das Werkzeug meldet
`PASS`.

**Ein reines Umbenennen des Feldes behebt den Defekt nicht.** Jeder Alt-Wert ist eine Tätigkeit
und wandert nach `blocked_activities`; `blocked_gates` ist **neu zu befüllen** und war in der
alten Struktur überhaupt nicht darstellbar. Solange ein Werkzeug die alte Formel anwendet,
liefert es für gegatete Einträge weiterhin fälschlich `false`.

**Deprecatete CAN-Referenzen in den Spalten „Widerspruch".** Die Beschreibungen von CONTRA-004
und CONTRA-006 nennen `CAN-007` und `CAN-011`. Beide wurden am 2026-07-19 durch die
Canvas-Atomisierung deprecated (Registry §6.2/§7). Der historische Wortlaut bleibt hier
absichtlich unverändert — er hält fest, was zum Zeitpunkt der Entdeckung im Canvas stand. Für
die Weiterverwendung gilt:

- `CAN-011` (Allowed Scope je Release-Stufe) → `CAN-131` … `CAN-137`; die in CONTRA-006
  gemeinte Aussage „A0 ist eine lokale Stufe ohne Backend" ist **CAN-131** (so auch Registry §8,
  offener Punkt 8).
- `CAN-007` (Constraints) → `CAN-080` … `CAN-098`. Welches **einzelne** Atom die in CONTRA-004
  gemeinte Datenminimierungs-Klausel trägt, ist aus den hier vorliegenden Artefakten nicht
  eindeutig ableitbar und bleibt **MISSING** — die Zuordnung trifft der Canvas-Owner, nicht
  dieser Schritt.

Die Spalte „Status" führt **ausschließlich** `open` | `resolved`. Alle übrigen Achsen
(`resolution_status`, `evidence_status`, `blocking`, `blocked_gates`, `blocked_activities`,
`evidence_gate`) stehen in der Tabelle oben. Ein `resolved` hier bedeutet **entschieden**, nicht **nachgewiesen**.

| ID | Widerspruch | Entdeckt | Auflösung | Status |
|---|---|---|---|---|
| CONTRA-001 | `CLAUDE.md` benannte `docs/superpowers/plans/2026-07-10-REVYR-GESAMTPLAN-FINAL.md`, `docs/REVYR-Vision-Canvas-PRD.md` und `docs/REVYR-Plan-PRD.md` als verbindlichen Plan. Keine dieser Dateien existiert im Repo. Zusätzlich schrieb sie AsyncStorage als Stack fest, was REQ-005 und DEC-003 verbieten. | 2026-07-19, Plumbline-Start | Nutzerentscheidung: `CLAUDE.md` an den echten Plumbline-Artefaktsatz angleichen. Dokumenten-Hierarchie, Stack, Backend-Absatz, Evidence-/Scope-Regeln und der `EXPO_PUBLIC`-Satz korrigiert. | resolved (2026-07-19) |
| CONTRA-002 | REQ-006/007 (Routenplanung) liegen in A0; NFR-007 verbietet Secrets im Client; `CLAUDE.md` wies `EXPO_PUBLIC_ORS_API_KEY` an. DEC-005 kannte die Extrahierbarkeit bereits, war aber nur `proposed` und zeitlich auf „Produktionsrouting" bezogen, während der Backend-Entscheid erst „vor B" fällig ist. | 2026-07-19, Plumbline-Start | Nutzerentscheidung: minimaler serverseitiger Routing-Proxy ab A0. DEC-005 auf `user-confirmed` gehoben und zeitlich auf A0 präzisiert. Der volle Backend-Entscheid bleibt offen. | resolved (2026-07-19) |
| CONTRA-003 | Dieselbe `OQ-`ID bezeichnete in Canvas/PRD, Vision und `open-questions.md` unterschiedliche Entscheidungen (z. B. OQ-003 = Karten/Routing vs. Owner/DRI vs. Min iOS/Android). Ein Auftrag „schließe OQ-003" hätte je nach gelesenem Dokument etwas anderes geschlossen. | 2026-07-19, Plumbline-Start | `docs/decisions/open-questions.md` ist einziges kanonisches Register (OQ-001…OQ-011); Canvas, PRD, Vision und Traceability referenzieren dessen IDs. Maschinell geprüft: 1:1 ID↔Entscheidung. | resolved (2026-07-19) |
| CONTRA-004 | **REQ-024 ↔ REQ-034 / CAN-007.** Serverseitige Anti-Cheat-Plausibilität setzt Rohsensordaten voraus, die REQ-034 nur „bei nachgewiesener Notwendigkeit" übertragen will und CAN-007 der Datenminimierung unterwirft. | 2026-07-19, Traceability-Gate | **DEC-011:** Rohsensorverläufe bleiben lokal; der Server erhält nur minimierte, abgeleitete Plausibilitätssignale. Fünfstufiger Verifikationsstatus. Fehlende Sensoren senken die Beweiskraft, führen aber nicht automatisch zu `rejected`. Volltext unten in §CONTRA-004. | `resolved` (Entscheidung Nutzer 2026-07-19) — Achsen siehe Statusmodell-Tabelle: `evidence_status = pending`, `blocking = true`, `evidence_gate C`, `blocked_gates [C, D]`, `blocked_activities [competition-release, territory-release]` |
| CONTRA-005 | **REQ-027 ↔ REQ-017 / NFR-006.** „Unveränderliche Historie" (Snapshots, Trophäen, Zeitreise, Vereinsheim) kollidiert mit „vollständiger In-App-Accountlöschung" und dem Löschanspruch aus NFR-006. Ungeklärt, welche Historiendaten eine Löschung überleben dürfen. | 2026-07-19, Traceability-Gate | **DEC-012:** Löschung entfernt alle personenbezogenen Daten und Identitätszuordnungen; historische Team-/Season-Daten überleben nur wirksam anonymisiert, sonst werden sie gelöscht. „Unveränderliche Historie" wird projektweit durch eine Löschungs-/Anonymisierungs-Ausnahme ersetzt. Volltext unten in §CONTRA-005. | `resolved` (Entscheidung Nutzer 2026-07-19) — Achsen siehe Statusmodell-Tabelle: `evidence_status = pending`, `blocking = true`, `evidence_gate B`, `blocked_gates [B]`, `blocked_activities [database-schema-finalization, account-release]`; Schema-Trennung Identität ↔ Aggregat nicht umgesetzt (**EV-042**, `evidence_status = blocked`) |
| CONTRA-006 | **REQ-034 ab A0.** Der bestätigte A0-Routing-Proxy verarbeitet Start- und Wegpunktkoordinaten serverseitig, während Canvas/CAN-011 A0 als lokale Stufe ohne Backend beschreibt. Die NFR-007-Lösung erzeugt eine neue Privacy-Fläche. | 2026-07-19, Traceability-Gate | **DEC-013:** A0-Privacy-Baseline für den Proxy vollständig festgelegt (transiente Verarbeitung, Retention 0, Body-Logging-Verbot, Zweckbindung, TLS-only, serverseitige Secrets, `eu-central-1`, Logs max. 7 Tage). Der **Datenfluss ist entworfen, aber nicht nachgewiesen**: Providerbedingungen, Logging-Verhalten, Retention, Transparenz und Sicherheitskontrollen sind ungeprüft. Volltext unten in §CONTRA-006. | `resolved` (Entscheidung Nutzer 2026-07-19) — Achsen siehe Statusmodell-Tabelle: `evidence_status = pending`, `blocking = true`, `blocked_gates [A0]`, `blocked_activities [field-test, release]`. Der frühere Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` ist als `status` unzulässig und wurde auf die zwei Achsen aufgeteilt |

## Auflösungen im Volltext

### CONTRA-004 — Anti-Cheat vs. Datenminimierung (DEC-011)

**Lokal, standardmäßig:** Rohsensorverläufe verbleiben auf dem Gerät.

**An den Server, für Wettbewerb, Rankings, Territory und Anti-Cheat — ausschließlich
minimierte, abgeleitete Plausibilitätssignale:** Kadenzmittel/-band, Geschwindigkeitsband,
optionales HF-Band (sofern vorhanden und freigegeben), GPS-Qualitätswert,
Accuracy-Zusammenfassung, Teleport-Indikatoren, Bewegungsplausibilität, Distanz, Dauer,
Sportart, Verifikations-Confidence.

**Nicht standardmäßig an den Server:** vollständige HF-Verläufe, vollständige Schrittverläufe,
vollständige Rohsensorserien, unnötige Health-Rohdaten, zusätzliche personenbezogene Daten.

**Verifikationsstatus (fünfstufig, nicht binär — stützt DEC-007):**
`verified-high` · `verified-standard` · `low-confidence` · `review-required` · `rejected`.

- Fehlende Sensoren allein sind **kein** Betrug. Sie dürfen die Beweiskraft senken
  (`low-confidence`), aber nicht automatisch zu `rejected` führen.
- Eindeutige Teleports, physikalisch unmögliche Geschwindigkeiten oder klar widersprüchliche
  Sensordaten dürfen zu `review-required` oder `rejected` führen.

**Weitergehende Rohdatenverarbeitung** nur nach ausdrücklichem Opt-in **oder** für eine
konkrete Einspruchs-/Betrugsprüfung — zeitlich begrenzt, mit dokumentiertem Zweck und
definierter Löschung.

Betroffen: REQ-024, REQ-034, RISK-013, RISK-022, CAN-104, CAN-109.

### CONTRA-005 — Historie vs. Accountlöschung (DEC-012)

**Accountlöschung entfernt mindestens:** Profil, E-Mail, Auth-Identitäten, Geräte-/Push-Tokens,
private Routen, rohe GPS-Verläufe, Health-Daten, Stimmungseinträge, Live-Sessions,
personenbezogene Kommentare und Medien sowie die Verknüpfungen zwischen Historieneinträgen und
der gelöschten Person.

**Historische Team- und Season-Daten dürfen nur erhalten bleiben, wenn wirksam anonymisiert**
und keine Rückführung mehr möglich ist: anonymisierte Team-Gesamtstände, nicht personenbezogene
Season-Statistiken, anonymisierte Capture-Ereignisse, aggregierte Gebiets-/Teamwerte.

> Beispiel: „Vincent eroberte Gebiet X." wird zu „Gelöschtes Mitglied eroberte Gebiet X."

**Ist wirksame Anonymisierung nicht möglich, MUSS der Datensatz gelöscht werden.**

**Sprachregelung, projektweit verbindlich.** Die Formulierung „unveränderliche Historie" wird
überall ersetzt durch:

> „Nach Finalisierung fachlich unveränderbar, außer aufgrund Löschung, Anonymisierung oder
> rechtlicher Korrektur."

**Architekturfolge:** Datenmodell und Event-Historie müssen Identität und historische Aggregate
technisch trennen. Diese Trennung ist **vor** Erstellung/Finalisierung des Datenbankschemas zu
berücksichtigen — nicht erst zu Stufe D.

Betroffen: REQ-017, REQ-027, NFR-006, EV-017, EV-027, **EV-042**.

**Nachzugsbedarf außerhalb dieser Datei (nicht von diesem Schritt geändert):** die Formulierung
„unveränderliche Historie" bzw. „Unveränderlichkeitsprüfung" ist in PRD, Vision, Canvas,
Traceability und Architektur noch unverändert vorhanden. Der jeweilige Datei-Owner zieht nach.

### CONTRA-006 — Routing-Proxy vs. Local-first (DEC-013)

`status: resolved` · `resolution_status: accepted` · `evidence_status: pending` ·
`blocked_gates: [A0]` · `blocked_activities: [field-test, release]` · `evidence_gate: A0` ·
`blocking: true` (berechnet: `A0` ∈ `blocked_gates`) ·
`decision_reference: OQ-011, DEC-013, ADR zum A0-Routing-Proxy = MISSING`

**Interpretation (Nutzerentscheidung 2026-07-19).** Dokumentation und Implementierungsplanung
dürfen fortgesetzt werden; der externe A0-Feldtest und das A0-Release bleiben bis zur
Privacy-Evidence blockiert. `documentation` und `planning` stehen ausdrücklich **nicht** in
`blocked_activities`.

Blockierend für den ersten externen Feldtest und für das Release der Routenplanung.

#### Auflösung des früheren Zielkonflikts in der Anweisung

Die Nutzeranweisung vom 2026-07-19 verlangte zunächst an einer Stelle `CONTRA-006 = RESOLVED`
als Erfolgskriterium des Validierungsberichts, an anderer Stelle ausdrücklich, dass CONTRA-006
`OPEN`/`BLOCKING` bleibt, bis Datenfluss, Providerbedingungen, Logging, Retention, Transparenz,
Sicherheitskontrollen und Evidence vollständig dokumentiert und **geprüft** sind. Beide Aussagen
waren nur deshalb unvereinbar, weil ein einziges Feld zwei Fragen tragen musste.

**Dieser Konflikt ist durch die Nutzerentscheidung zum Statusmodell aufgelöst, nicht durch die
Assistenz.** Beide Aussagen behalten recht, auf getrennten Achsen: die Grundsatzfrage ist
entschieden (`status = resolved`, `resolution_status = accepted`), der Nachweis ist nicht
erbracht (`evidence_status = pending`), und die Blockade bleibt sichtbar (`blocking = true`).

Was sich dadurch **nicht** ändert: die unter „Geforderte Evidence" in
`docs/EVIDENCE-LEDGER.md` gelisteten Nachweise (a)…(n) und (o)…(u) sind sämtlich `nicht
erbracht`. Ein Großteil davon (Tests gegen Logs, Rate-Limit-Test, Secret-Scan des Bundles) setzt
lauffähigen Code voraus, der nicht existiert. `resolved` auf der Entscheidungsachse ist **keine**
Freigabe der A0-Routing-Implementierung.

#### Datenfluss und Zweckbindung

- Der Proxy verarbeitet Start-, Ziel- und Wegpunktkoordinaten **ausschließlich transient** zur
  angeforderten Routenberechnung.
- **Keine** anwendungsseitige Persistenz von Koordinaten, berechneter Route oder vollständigen
  Request-/Response-Bodies.
- **Zweckbindung:** keine Werbung, Profilbildung, Produktanalyse, Trainingsanalyse,
  Standortstatistik, Wiederverwendung, Modelltraining, kein Verkauf/keine Weitergabe.
- **Retention Koordinaten-Payload:** Application 0, Cache 0, Analytics 0.

#### Was der Client sendet

Zulässig: `sport` (`run`|`ride`), erforderliche Koordinaten, notwendige Routingparameter,
technisch erforderliche Request-ID.

Unzulässig: Benutzername, E-Mail, Account-ID, Health-Daten, Aktivitätsverlauf, vollständiger
GPS-Track, Team-/Profildaten, Gerätekennungen (sofern nicht zwingend).

#### Logging

Request-/Response-Bodies dürfen **nicht** geloggt werden.

- **Nicht** in Logs, Traces oder Fehlermeldungen: Latitude, Longitude, Wegpunktlisten,
  vollständige Provider-URLs mit Koordinaten, Routengeometrien, Start-/Zieladressen.
- **Zulässig:** zufällige Request-ID, Zeitstempel, HTTP-Status, Verarbeitungsdauer,
  Routingprofil, Anzahl Wegpunkte, normalisierte Fehlerkategorie, Provider-Latenz,
  Rate-Limit-Ereignis.
- Technische Logs dürfen **keine Standortrekonstruktion** ermöglichen.
- Aufbewahrung technischer Logs: **max. 7 Tage**, sofern keine nachgewiesene technische oder
  gesetzliche Notwendigkeit für eine andere Frist besteht; eine Änderung braucht eine
  dokumentierte Entscheidung.

#### Transport und Secrets

Nur HTTPS/TLS, keine unverschlüsselten Endpunkte. Provider-Key ausschließlich serverseitig.
Keine Secrets in App, Repository oder Logs. Secrets über AWS Secrets Manager oder verschlüsselte
Lambda-Env, restriktive IAM, Rotation und Widerruf möglich.

#### EU-Verarbeitung — Grenze der Aussage

Lambda und API Gateway in `eu-central-1`. **Vor dem ersten externen Feldtest** ist zusätzlich zu
dokumentieren: Verarbeitungsregion des Routinganbieters, ob Daten den EWR verlassen,
Unterauftragsverarbeiter, Transfergrundlage.

Die Bezeichnung „EU-Proxy" darf **nicht** den Eindruck erwecken, die gesamte Verarbeitung liege
in der EU, wenn der nachgelagerte Anbieter außerhalb verarbeitet.

#### Provider-Voraussetzungen

Vor externem Feldtest zu dokumentieren: Rollenverteilung Controller/Processor,
Auftragsverarbeitungsvertrag, Unterauftragsverarbeiter, Verarbeitungsregion,
Provider-Retention, Ausschluss eigener Werbe-/Profiling-/Trainingszwecke, Lösch- und
Sicherheitsregeln. **Wer das nicht erfüllt, darf nicht für produktive oder externe A0-Tests
eingesetzt werden.**

#### Rechtsgrundlage und Transparenz

Vor dem ersten externen Feldtest zu klären und darzustellen: Verantwortlicher, Zweck,
Rechtsgrundlage, Empfänger/Auftragsverarbeiter, Übermittlungsregionen, Speicherdauer,
Betroffenenrechte, Datenschutzkontakt.

Die Datenschutzerklärung muss **vor Nutzung der Routenplanung** verständlich erklären:

> „Zur Berechnung deiner Route werden die ausgewählten Start-, Ziel- und Wegpunkte kurzfristig
> an unseren EU-Routing-Proxy und den eingesetzten Routinganbieter übermittelt. Die App
> speichert diese Koordinaten im Proxy nicht dauerhaft."

#### Missbrauchsschutz

Rate Limit, Size-Limit, maximale Wegpunktzahl, Timeout, Kill Switch, Koordinatenvalidierung und
normalisierte Fehler dürfen **nicht** zu dauerhafter Koordinatenspeicherung führen.
IP-Adressen nur soweit technisch erforderlich, keine dauerhafte Speicherung und keine
Verknüpfung mit Routenanfragen; separat zu dokumentieren.

#### Fehlerbehandlung

Providerfehler gelangen nie ungefiltert an den Client. Eine Fehlerantwort enthält nur internen
Fehlercode, nutzergeeignete Nachricht, Request-ID und ggf. Retry-Hinweis — keine
Provider-Secrets, internen URLs, Koordinaten, vollständigen Providerantworten oder Stack Traces.

#### Local-first — verbindliche Präzisierung

Überall dort, wo „local-first" behauptet wird, gilt der Wortlaut:

> „Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal. Für die
> Routenberechnung dürfen ausschließlich die erforderlichen Wegpunkte transient an einen
> kontrollierten Routing-Proxy übertragen werden. Der Proxy speichert keine Koordinaten oder
> Routengeometrien dauerhaft."

Betroffen: REQ-006, REQ-007, REQ-034, NFR-007, DEC-005, ASM-103, CAN-091 … CAN-097, CAN-131,
OQ-004, OQ-009, RISK-007.

**Nicht gebaut.** `infra/routing-proxy/` ist ausschließlich dokumentiert. In diesem Lauf wurden
kein Verzeichnis, keine Quelldatei und keine AWS-Ressource angelegt.

## Nachzugsbedarf außerhalb dieser Datei — unzulässiger `status`-Wert noch vorhanden

Der Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` ist nach Registry §3.1 als `status`
**unzulässig**. In dieser Datei, in `docs/EVIDENCE-LEDGER.md` und — **seit dem 2026-07-20** — in
`docs/implementation/revyr-delivery-plan.md` ist er beseitigt. Er steht **weiterhin** in den
folgenden Dateien, die dieser Schritt nicht besitzt und daher nicht ändert. Der jeweilige
Datei-Owner zieht nach; bis dahin besteht dort eine Statusdivergenz gegenüber
`docs/ID-REGISTRY.md` §6.11.1 und dieser Datei:

| Datei | Fundstellen (Zeile, Stand 2026-07-19) | Stand |
|---|---|---|
| `docs/traceability.md` | 1530, 1593, 1679 (sowie 1139 als Befundtext) | offen |
| `docs/prd/revyr-endurance-platform.prd.md` | 217, 231, 252, 253, 254 | offen |
| `docs/architecture/revyr-target-architecture.md` | 155, 369, 569 | offen |
| ~~`docs/implementation/revyr-delivery-plan.md`~~ | ~~85, 171, 329~~ | **erledigt 2026-07-20** — alle drei auf `status = resolved` / `evidence_status = pending` / `blocked_gates [A0]` / `blocked_activities [field-test, release]` aufgelöst. Die vier verbliebenen Fundstellen der Zeichenfolge zitieren den Wert ausdrücklich als **historisch und unzulässig** |
| `docs/validation/validation-report.md` | 374, 405, 411 | offen |

Zulässig bleiben die Fundstellen in `docs/ID-REGISTRY.md` (74, 85, 711, 930) und
`docs/vision/revyr-endurance-platform.vision.md` (131): sie zitieren den Wert ausdrücklich als
**historisch und unzulässig** und verwenden ihn nicht als Status.

**Kein Selbstverdikt.** Die Divergenz C6b in `docs/validation/validation-report.md` ist durch
diese Änderung auf der Seite von Ledger und Registry ausgeräumt. Ob C6b damit auf `PASS` geht,
entscheidet der Owner des Validierungsberichts — nicht dieser Schritt. Der Gesamtstatus bleibt
`BLOCKED_TRACEABILITY`, bis der Nutzer die offenen Canvas-Items bestätigt hat.
