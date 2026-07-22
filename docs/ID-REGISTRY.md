# ID-Registry

Status: `ready-for-user-confirmation` — diese Registry bestätigt nichts.  
Feature Slug: `revyr-endurance-platform`  
Angelegt: 2026-07-19 (Phase 1)  
Registry-Zustand: **kontrolliert aufgetaut für genau vier serialisierte Schritte — zwei am
2026-07-19 und zwei am 2026-07-20 (Runde 4 und Runde 5), jeweils Phase 1, Owner
requirements-analyst** — danach wieder eingefroren.

**Auftau-Schritt 1** hatte genau vier Gegenstände: (1) Verankerung des Statusmodells aus der
Nutzerentscheidung vom 2026-07-19, (2) Reparatur des semantisch falschen Vision-Ankers von
REQ-014, (3) Nachzug der Titel von REQ-027 und EV-027, (4) Fortschreibung von §10/§11.

**Auftau-Schritt 2** (dieser Schritt) setzt die Nutzerentscheidungen vom 2026-07-19 zu CAN-130,
CAN-099, CAN-071, CAN-022, GPX-Export, NFR-008 und zum Blocking-Statusmodell (C16) in den
ID-Raum um. Er (1) ersetzt `blocking_scope` durch die zwei disjunkten Felder `blocked_gates` und
`blocked_activities` mit einer einzigen kanonischen Blocking-Formel, (2) atomisiert die
Composite-Items CAN-071 und REQ-014, (3) vergibt eigene IDs für GPX-Export, Streckenvergleich,
monochromes Designsystem, die Wearable-Persona und drei neue offene Entscheidungen, (4) nimmt die
Präfixe `USER-` und `NFR-` in die Registry auf, (5) verankert die Regel, dass die Gesamtzahl
aktiver Requirements **abgeleitet** und nie hartkodiert wird.

**Runde 4 (2026-07-20)** — dritter kontrolliert aufgetauter Schritt, gleicher Owner
(requirements-analyst), gleiche Serialisierung. Gegenstände: (1) drei **kanonische Anker**
(Accessibility, monochromes Designsystem, Datenportabilität/GPX) auf ihren verbindlichen
Nutzerwortlaut gezogen — **ohne neue IDs**, weil für alle drei bereits aktive Items dieselbe
Aussage tragen (§6.3.3, Abweichung von der wörtlichen Anweisung dort ausdrücklich gemeldet);
(2) **Auflösung der doppelt geführten Farbregel** zugunsten von CAN-099; (3) **Teilung von
CAN-140** in Planungs- und Auswertungsfunktion mit vollständiger Nachfolgekette; (4) **Entfernung
semantisch falscher Vision-Anker** (VIS-008 an vier Community-Requirements) und der in §6.1.1
verbotenen Schlusskette; (5) **kanonische Trennung EV-008 / EV-039**; (6) Entscheidung, dass der
`NFR-`Raum **kein `blocking`** führt (§6.13.2); (7) Zählregel auf **alle** Präfixe ausgedehnt,
Statusklassen getrennt, **weder 36 noch 39** als Literal zulässig (§10.2); (8) Angleichung von
§7.3 an §7.4.1 und Behebung der Leerzeile, die VIS-012/VIS-013 mechanisch aus der
Definitionstabelle geworfen hatte.

**Runde 5 (2026-07-20)** — vierter kontrolliert aufgetauter Schritt, gleicher Owner, gleiche
Serialisierung. Gegenstände, alle aus dem Nutzerauftrag vom 2026-07-20: (1) **Herabstufung des
Source Type** von **CAN-119, CAN-109 und CAN-024** auf `ASSUMPTION` und **Teil-Herabstufung von
VIS-003** (Schritte 2 des Auftrags); (2) **Entfernung der Web-Erstreckung aus dem kanonischen
Wortlaut von CAN-099** bei unverändertem `ASSUMPTION`-Status der vier nicht belegten
Accessibility-Details (Schritt 3); (3) **Bestätigung von REQ-007 als `ASSUMPTION`** auf der
Anforderungsebene bei ausdrücklich unverändertem `MISSING` auf der Zielwertebene (Schritt 4);
(4) **Aufnahme der Wesentlichkeitsprüfung bei Teilbelegung** als reine Berichtsregel (§3.3,
Schritt 5). **Kein Wortlaut wurde verengt, wo die Verengungsrichtung zwischen den
Gegenprüfungen strittig ist** — dort steht die Herabstufung ohne Titeländerung und die
Aufteilung ist als Nutzerentscheidung ausgewiesen (§7.6, §8 Punkte 45–50).

In **keinem** der vier Schritte wurde ein Statuswert inhaltlich uminterpretiert, eine Evidence
als erbracht markiert oder ein Zielwert erfunden. Es wurde **keine** Metamodell-Erweiterung
vorgenommen — die NFR-Frage ist innerhalb des eingefrorenen Modells gelöst, und §3.3 führt
**kein** neues Feld, **kein** neues Vokabular und **keinen** neuen Eingang der Blocking-Formel
ein (Nachweis dort). Der Gesamtstatus bleibt `BLOCKED_TRACEABILITY`; `true-line-status` ist
`pending-watcher`, `wired-in-prod` ist `no`, `evidence-class` ist `none`.

## 1. Geltung

Diese Datei ist die **einzige kanonische Quelle** für die ID-Räume `VIS-`, `CAN-`, `REQ-`,
`AC-`, `TRC-`, `EV-`, `RISK-`, `ASM-`, `OQ-` und `CONTRA-`. Bei jeder Abweichung zwischen
dieser Registry und einem referenzierenden Dokument gilt die Registry.

Der Grund ist ein bereits eingetretener Defekt: In einem früheren Schritt dieses Laufs haben
zwei parallel arbeitende Agenten OQ-IDs gleichzeitig gelesen und umnummeriert. Sechs Referenzen
wurden dadurch falsch und lasen sich trotzdem plausibel. Derselbe Defekt liegt bei den ASM-IDs
bis heute vor (siehe Abschnitt 5).

## 2. Regeln (verbindlich)

1. **Keine stillschweigende Umnummerierung.** Eine bestehende ID behält ihre Nummer. Wird sie
   ersetzt, bleibt der alte Eintrag mit `status = deprecated`, `deprecated_at` und
   `replacement_id` erhalten.
2. **Erst reservieren, dann verwenden.** Eine neue ID wird zuerst hier eingetragen (auch mit
   `status = reserved`), bevor irgendein Dokument sie referenziert.
3. **Nur Phase 1 vergibt IDs.** Ab Phase 2 ist die Registry eingefroren. Kein Agent außerhalb
   von Phase 1 vergibt, benennt oder deprecated eine ID. Wer eine fehlende ID braucht, meldet
   das als **BLOCKER** zurück und erfindet keine.
4. **Keine unabhängige Parallelvergabe.** Zwei Agenten dürfen nicht gleichzeitig IDs desselben
   Raums vergeben. Vergabe ist ein serialisierter Schritt mit genau einem Owner.
5. **Eine ID hat genau eine Bedeutung** — projektweit, dateiübergreifend. Zwei Dateien dürfen
   dieselbe ID nicht für unterschiedliche Sachverhalte verwenden.
6. **Gelöschte IDs werden nicht wiederverwendet.** Eine `deprecated` ID bleibt für immer belegt.
7. **Umbenennungen brauchen eine Alias-/Migrationstabelle** (Abschnitt 7), alt → neu, je Datei.
8. **Traceability referenziert ausschließlich Registry-IDs.** Kein Verweis auf Prosaabschnitte,
   Ad-hoc-Facetten oder Dokumentüberschriften.
9. **Doppelte, unbekannte und verwaiste IDs sind Validierungsfehler**, keine Schönheitsfehler:
   *doppelt* = eine ID mit zwei Bedeutungen; *unbekannt* = eine referenzierte ID ohne
   Registry-Eintrag; *verwaist* = ein `active` Registry-Eintrag, den kein Dokument referenziert.
10. **Nachzugsfenster.** Regel 2 verlangt, dass eine ID **zuerst** hier steht und **danach** in
    einem Dokument erscheint. Zwischen beiden Zeitpunkten ist der Eintrag zwangsläufig eine
    Waise im Sinne von Regel 9. Das ist eine **Folge** von Regel 2, kein Defekt. Solche IDs
    stehen abschließend in §7.4 und §7.5 sowie in `scratchpad/id-migration.json` und
    `scratchpad/id-migration-r4.json` (jeweils `pending_document_nachzug`). Ein Validator behandelt
    ausschließlich die dort gelisteten IDs als zulässige Waisen — jede andere Waise bleibt ein
    Fehler. Fällt eine ID aus der Liste, ohne dass ein Dokument sie referenziert, ist das ein
    Befund.
11. **Zählstände werden abgeleitet, nie hartkodiert.** Die Gesamtzahl aktiver Requirements ist
    das Ergebnis der Abfrage „alle Einträge mit Präfix `REQ-`, `status = active`, ohne
    `template-placeholder`" **gegen diese Datei**. Sie ist eine Momentaufnahme, keine Konstante.
    Keine Prüfung, kein Bericht und kein Werkzeug darf eine feste Zahl als Bestehens- oder
    Fehlschlagsbedingung verwenden — **und keine feste Zahl verbieten**. Das gilt namentlich für
    die Altstände **36** und **39**: ein Werkzeug, das „36" auf eine Verbotsliste setzt, ist an
    einen Zählstand gebunden wie eines, das „36" erwartet. Dasselbe gilt für `AC-`, `EV-`,
    `TRC-`, `CAN-`, `VIS-`, `RISK-`, `ASM-`, `OQ-`, `CONTRA-`, `NFR-` und `USER-`. **Aktive,
    deprecatete und reservierte Einträge werden immer getrennt gezählt und getrennt
    ausgewiesen**; reservierte zählen nie als erfüllte Referenz. Wer eine Zahl nennt, nennt Datum
    und Ableitungsweg dazu (§10.2).

## 3. Feld- und Statuskonventionen

| Feld | Bedeutung |
|---|---|
| `id` | Die ID selbst. Format `<PREFIX>-<3 Ziffern>`. |
| `type` | Fachlicher Typ. Bei `CAN-` zusätzlich die atomare Aussageart. |
| `title` | Kurztitel, wörtlich aus der `canonical_file` übernommen und bei Bedarf mit `…` gekürzt. Nicht neu formuliert. |
| `canonical_file` | Die eine Datei, die den Inhalt definiert. Andere Dateien referenzieren nur. |
| `status` | siehe unten |
| `created_at` | Datum der Entstehung. Ableitungsregel siehe unten. |
| `deprecated_at` | Datum der Ausmusterung, sonst `—`. |
| `replacement_id` | Nachfolge-ID(s), sonst `—`. |
| `notes` | Befunde, Kollisionen, Blocker, Herkunft. |

| `status` | Bedeutung |
|---|---|
| `active` | Gültig und referenzierbar. |
| `deprecated` | Ersetzt. Nicht löschen, nicht wiederverwenden, nicht neu referenzieren. |
| `reserved` | ID vergeben, Inhalt aber noch **MISSING** — braucht eine Nutzerentscheidung. Darf noch nicht als erfüllte Referenz gezählt werden. |
| `template-placeholder` | Kein echtes Item, sondern Platzhalter in einer Vorlage. Von der Referenzprüfung auszuschließen. |
| `open` / `resolved` | Nur für `OQ-` und `CONTRA-`: Entscheidungsstand. |

### 3.1 Statusmodell für `OQ-` und `CONTRA-` (Nutzerentscheidung 2026-07-19)

**Der Defekt, den dieses Modell behebt.** Bis zu dieser Änderung trug ein einziges Feld
`status` zwei unabhängige Fragen gleichzeitig: „Ist der Widerspruch entschieden?" und „Ist die
Erfüllung nachgewiesen?". Dadurch entstanden Werte wie `DESIGN-RESOLVED / EVIDENCE-PENDING`,
die weder `open` noch `resolved` sind und in keiner Prüfung sauber ausgewertet werden konnten —
sowie die Divergenz C6b (`docs/validation/validation-report.md`, FAIL): die Registry führte
CONTRA-004/005 als `open`, der Ledger als `resolved (Entscheidung Nutzer)`. Beide hatten recht,
weil sie unterschiedliche Fragen beantworteten. Ab jetzt hat jede Frage ihr eigenes Feld.

**Das kanonische Feld `status` behält ausschließlich `open` | `resolved`** und beschreibt
**nur**, ob der fachliche/architektonische Widerspruch **entschieden** wurde. Ein Widerspruch
erhält `resolved`, sobald die Entscheidung getroffen ist — **nicht** erst, wenn die Evidence
vorliegt. Die Evidence lebt auf der Achse `evidence_status`.

**Unzulässig als `status`-Wert:** `DESIGN-RESOLVED`, `EVIDENCE-PENDING`, `pending`, `closed`,
`mitigated`. Wer einen dieser Werte in `status` findet, hat einen Validierungsfehler gefunden.

| Feld | Zulässige Werte | Bedeutung |
|---|---|---|
| `status` | `open` \| `resolved` | Ist die Grundsatzfrage entschieden? |
| `resolution_status` | `undecided` \| `decision-documented` \| `accepted` | Reifegrad der Entscheidung. `decision-documented` = niedergeschrieben, aber noch nicht als verbindlich angenommen; `accepted` = als verbindliche Projektentscheidung angenommen. |
| `evidence_status` | `not-required` \| `not-planned` \| `planned` \| `pending` \| `verified` \| `failed` \| `blocked` | Ist die Erfüllung nachgewiesen? |
| `blocking` | `true` \| `false` | **Abgeleitet, nie hartkodiert** — siehe Formel unten. |
| `blocked_gates` | Liste aus `P0` \| `A0` \| `A1` \| `A2` \| `B` \| `C` \| `D` \| `E`, sonst leer | Welche **Release-Gates** die Blockade trifft. |
| `blocked_activities` | Liste aus `documentation` \| `planning` \| `implementation` \| `field-test` \| `release` \| `store-submission` \| `database-schema-finalization` \| `account-release` \| `competition-release` \| `territory-release`, sonst leer | Welche **Tätigkeiten** die Blockade trifft. |
| `evidence_gate` | Gate-Bezeichner oder `—` | Das Gate, an dem der Nachweis fällig ist. |
| `decision_reference` | ID-Liste oder `MISSING` | Wo die Entscheidung steht. |
| `evidence_reference` | ID-Liste oder `MISSING` | Wo der Nachweis steht bzw. stehen wird. |
| `rationale` | Freitext | Warum diese Kombination. |

`source_type` und `evidence_status` dürfen **nicht** vermischt werden. `source_type` beantwortet
„Woher stammt die Anforderung bzw. der Zielwert?", `evidence_status` beantwortet „Ist die
Erfüllung nachgewiesen?". `EXPLICIT` + `pending` ist eine **gültige** Kombination.

#### Der Defekt, den `blocked_gates` / `blocked_activities` behebt (C16, Nutzerentscheidung 2026-07-19)

Das frühere Feld `blocking_scope` mischte **Release-Gates** und **Tätigkeiten** in einer einzigen
Liste. Die Vokabulare sind disjunkt: kein Gate-Bezeichner (`A0`, `B`, `C` …) ist jemals ein
Tätigkeitsbezeichner (`field-test`, `release` …) und umgekehrt. Die Formel verlangte aber, das
„aktuell geprüfte Gate" in `blocking_scope` zu suchen. Für jeden Eintrag, dessen `blocking_scope`
nur Tätigkeiten enthielt — also für **jeden gegateten Eintrag** —, lieferte die wörtliche Lesart
damit zwangsläufig `false`. Die Blockade, die das Feld sichtbar machen sollte, verschwand genau
dann, wenn sie gegen ein Gate geprüft wurde.

Zusätzlich schrieb die Nutzerentscheidung für CONTRA-004/005 vier Werte vor, die außerhalb des
damaligen Basis-Wertebereichs lagen. Beides ist mit der Trennung erledigt: Gates und Tätigkeiten
haben jetzt je ein eigenes Feld mit je einem eigenen, **abschließenden** Wertebereich, und die
vier Werte sind reguläre Mitglieder von `blocked_activities`. Der frühere §8-Punkt 16
(„Wertebereich von `blocking_scope`") ist damit **geschlossen**.

#### Kanonische Ableitungsformel für `blocking` (verbindlich)

```
blocking = status        NOT IN [resolved]
           OR resolution_status NOT IN [accepted]
           OR evidence_status   IN     [failed, blocked]
           OR current_gate      IN     blocked_gates
           OR current_activity  IN     blocked_activities
```

Dabei sind `current_gate` und `current_activity` die **Auswertungsparameter** des jeweiligen
Prüflaufs. Ist einer von beiden nicht gesetzt, entfällt ausschließlich die zugehörige Klausel;
die übrigen bleiben in Kraft.

**Wortlautbindung (Runde 4, 2026-07-20).** Die erste Klausel lautet `status NOT IN [resolved]` —
gleichbedeutend mit `status != resolved`, aber **nicht** mit `status == open`. Für die zwei
gültigen Werte sind beide Formulierungen äquivalent; für einen **fehlenden, leeren oder
ungültigen** `status` sind sie es nicht: `status == open` liefert dann `false` (nicht blockierend),
`status NOT IN [resolved]` liefert `true`. Ein Bericht, der die Formel als `status == open`
zitiert, beschreibt ein **anderes und schwächeres** Verhalten als die normative Quelle. Verbindlich
ist die Fassung oben; sie ist **fail-closed**. Ein fehlender oder ungültiger `status` ist
**zusätzlich** ein Validierungsfehler und darf nicht durch die Formel stillschweigend geheilt
werden. Text und Implementierung sind auf diesen Wortlaut anzugleichen — nicht umgekehrt.

**Geltungsbereich der Achsen (verbindlich, Runde 4).** Die Felder `status` (`open`/`resolved`),
`resolution_status`, `blocking`, `blocked_gates` und `blocked_activities` gelten **ausschließlich
für `OQ-` und `CONTRA-`**. **Kein `NFR-`Eintrag führt `blocking`** — Begründung in §6.13.2. Nur
`evidence_status` gilt projektweit (§3.2). Ein Werkzeug, das `blocking` für ein `NFR-`, `REQ-`,
`CAN-` oder `VIS-`Item liest oder berechnet, wertet ein Feld aus, das es dort nicht gibt.

**Niemals Gate-Bezeichnungen mit Tätigkeitsbezeichnungen vergleichen.** `current_gate` wird
ausschließlich gegen `blocked_gates` geprüft, `current_activity` ausschließlich gegen
`blocked_activities`. Ein Werkzeug, das ein Gate in `blocked_activities` sucht (oder umgekehrt),
reproduziert exakt den behobenen Defekt.

**Bei `evidence_status` = `planned` oder `pending`** entsteht ein *aktueller* Blocker **nur**
dann, wenn das gerade geprüfte Gate in `blocked_gates` oder die gerade geprüfte Tätigkeit in
`blocked_activities` steht. `planned`/`pending` allein blockiert nichts.

**Eine einzige Implementierung.** Alle Validatoren importieren **dieselbe** kanonische
Blocking-Funktion. Duplizierte oder abweichende Implementierungen sind unzulässig, ebenso jede
hartkodierte Sonderbehandlung einzelner `CONTRA-`IDs. Ein Prüfwerkzeug, das `blocking` für eine
bestimmte ID fest verdrahtet, ist selbst der Defekt. Die maschinenlesbare Fassung der Formel und
der beiden Wertebereiche steht in `scratchpad/id-migration.json` unter `blocking_model` und ist
für diese Datei normativ.

**Auswertungskonvention.** `blocking` ist auswertungsrelativ: dieselbe ID kann an einem Gate
blockieren und an einem anderen nicht. Der in §6.11.1 eingetragene Wert ist die Auswertung **am
jeweils eigenen `evidence_gate` des Eintrags**. Wer gegen ein anderes Gate oder eine andere
Tätigkeit prüft, leitet neu ab und übernimmt den Tabellenwert nicht.

**Sonderfall `evidence_gate = —`.** Ein Eintrag ohne eigenes Gate wird über
`blocked_activities` wirksam. Beispiel: CONTRA-003 hat `blocked_gates = []` und
`blocked_activities = [documentation]` — solange dokumentiert wird, ist die Klausel erfüllt und
`blocking = true`. Ein leeres `blocked_gates` bedeutet **nicht** „blockiert nie", sondern
„blockiert kein Gate"; die Tätigkeitsachse bleibt davon unberührt.

**Ableitungsregel für `created_at`** (kein Artefakt trägt ein ID-Anlagedatum, deshalb
abgeleitet und hier offengelegt):

- `2026-07-18` für alle IDs, deren Bestand durch `docs/validation/validation-report.md`
  (Datum 2026-07-18, Zählstand 36/36/36/36) und `docs/risks/revyr-risk-register.md`
  ("Stand: 2026-07-18") belegt ist.
- `2026-07-19` für alles, was ausdrücklich mit diesem Datum in `open-questions.md` bzw.
  `decision-log.md` entstanden ist (OQ-011, CONTRA-001…006), sowie für alle in diesem Lauf
  neu vergebenen IDs.

Das Datum ist damit eine belegte Ableitung, kein geschätzter Wert. Ein exaktes Anlagedatum je
ID ist **MISSING** und aus den Artefakten nicht rekonstruierbar.

### 3.2 Semantik von `evidence_status` (Nutzerentscheidung 2026-07-19, projektweit)

Diese vier Werte gelten **projektweit** und für **alle** ID-Räume, nicht nur für `CONTRA-`.
Widersprüchliche Vorkommen sind für den **aktuellen Zustand** entsprechend zu ersetzen.

| Wert | Bedeutung |
|---|---|
| `not-planned` | Es existiert noch **kein Messkonzept**. |
| `planned` | Metrik, Berechnung und zuständiges Gate sind **definiert**, die Instrumentierung fehlt. |
| `pending` | Die Instrumentierung ist **implementiert**, aber Messdaten oder Messfenster fehlen noch. |
| `verified` | Der Zielwert ist mit ausreichender, **dokumentierter** Evidenz geprüft. |
| `not-required` | Requirement-spezifisch begründete Nichtanwendbarkeit. **Nie pauschal** vergeben. |
| `failed` / `blocked` | Nachweis versucht und gescheitert bzw. durch einen anderen offenen Punkt versperrt. |

Die Grenze zwischen `planned` und `pending` ist die **Instrumentierung**, nicht die Absicht.
Solange kein Code existiert, kann nichts instrumentiert sein — ein Eintrag ohne Code steht
deshalb höchstens auf `planned`. `pending` zu vergeben, wo nur ein Vorsatz existiert, behauptet
eine Instrumentierung, die es nicht gibt.

### 3.3 Wesentlichkeitsprüfung bei Teilbelegung (Nutzerentscheidung 2026-07-20, Berichtsstufe)

**Abweichung von der Platzierungsempfehlung, ausdrücklich gemeldet.** Der Regelvorschlag wollte
diesen Text in §3.2 aufnehmen, weil §3.2 der einzige projektweit geltende Abschnitt ist. Er steht
stattdessen in einem **eigenen** §3.3: §3.2 definiert ausschließlich das Vokabular von
`evidence_status`; eine Wesentlichkeitsregel dort einzuhängen würde eine Achse mit einer
Berichtsregel vermischen. Die Geltung ist dieselbe — projektweit. Der Nutzer kann die Platzierung
überstimmen; der Regeltext bliebe davon unberührt.

**Was diese Regel nicht ist.** Sie ist **kein** Eingang der kanonischen Blocking-Formel aus §3.1.
Deren Achsen gelten unverändert **ausschließlich** für `OQ-` und `CONTRA-` (§3.1,
Geltungsbereich). Die Prüfung, die dem Regelvorschlag zugrunde liegt, hat das belegt: von den 17
`TEILBELEGT`-Fällen ist repo-seitig genau **einer** als BLOCKER geführt (CAN-051,
`docs/SOURCE-MAP.md`), zwei als Nachzug, dreizehn überhaupt nicht — weil keine der Kennungen
`CAN-`, `REQ-`, `VIS-` das Feld `blocking` führt. Die Regel kann die Blocking-Formel deshalb
weder entlasten noch verschärfen. Sie steuert **nur**, ob ein Teilbefund als **BLOCKER** oder als
**Nachzug** in die §5-Listen und in §8 wandert. Sie ändert **keinen** Statuswert, führt **kein**
neues Vokabular ein und stuft **nichts** hoch. Der Zeilenstatus `linked-partial`
(`docs/traceability.md`, 3 Fälle) und die Ankerstufe `trägt-teilweise` der manuellen Ankerreview
(23 von 40 Fällen) bleiben **unberührt** — die Regel gilt allein für die **Zellenachse** der
Belegprüfung.

Ein teilbelegter Befund wird als **BLOCKER** geführt, wenn mindestens eine Bedingung erfüllt ist:

| # | Bedingung | Prüfweg |
|---|---|---|
| **W1** | Der nicht getragene Teil erscheint im **Wortlaut des Akzeptanzkriteriums** des tragenden Requirements. | Textsuche im AC-Wortlaut |
| **W1b** | Hilfsweise für Items **ohne eigenes AC**: er erscheint im AC eines Requirements, das das Item ausdrücklich als **Anker** führt. | Textsuche über den Ankereintrag |
| **W2** | Er ist selbst eine **Vorbedingung** („erst nach…", „nur wenn…", „MUSS vor…") oder begründet eine **Nachweispflicht** mit `EV-`Eintrag. | grammatische Form der Klausel; Vorhandensein eines EV-Eintrags |
| **W3** | Er erweitert den **Geltungsbereich** auf eine **Plattform, Nutzergruppe, Datenart oder Artefaktklasse**, die sonst nicht umfasst wäre. | Vergleich der Gegenstandsbereiche |

**W1b ist die schwächste Bedingung** und bei jeder Anwendung als solche zu kennzeichnen: sie
nutzt ein Zwischenglied, wenn auch ein dokumentiertes. Sie ist der einzige Punkt, an dem die
Regel vom Beweismaßstab der wortnahen Deckung abweicht. Wird sie gestrichen, fallen VIS-007 und
VIS-008 aus der BLOCKER-Führung; die Bilanz lautet dann 11 statt 13.

**W3 ist eng gefasst.** Eine Erweiterung des bloßen **Funktionsbereichs** genügt **nicht**. Die
vier genannten Kategorien bestimmen Scope; „Funktionsbereich" wäre so weit, dass jeder
Teilbefund hineinfiele und die Regel wirkungslos machte.

**Ausschluss (Nullifikator).** Ist der Teil in **irgendeiner** der vier Quellen wortnah belegt
und nur die `SRC-`Angabe falsch, ist der Fall **unabhängig von W1–W3** ein **Quellennachzug**,
kein Wesentlichkeitsbefund. Muster: CAN-113 — „nicht schwach belegt, sondern falsch adressiert"
(`docs/SOURCE-MAP.md`).

**Zwingende Nebenpflicht (Kettenregel).** Trifft die Regel mehrere Zellen **derselben
fortgepflanzten Lücke** ungleich, ist die Lücke **als Kette** weiterzuführen, auch wenn einzelne
Glieder herabgestuft werden. Belegter Anlass: die Lücke „**versionierte** Faktoren" läuft durch
VIS-008, REQ-023 und REQ-001; die Regel hält REQ-023 (AC-023 nennt „Version") und entlässt
REQ-001 (AC-001 nennt sie nicht). Dasselbe beim Cluster „Unsicherheit/Confidence": CAN-052
bleibt, REQ-012 fällt. Eine Kette darf **nicht** dadurch verschwinden, dass ihre Glieder einzeln
unwesentlich sind. Dies ist der bewusst in Kauf genommene Preis der Regel und wird nicht
weggeschrieben.

**Vorbehalt (Zirkularität).** Die Regel macht AC-Wortlaute zum Maßstab, obwohl mehrere AC selbst
`TEILBELEGT` sind. Ein nicht vollständig belegtes AC entscheidet dann über die Wesentlichkeit
einer nicht vollständig belegten Zelle. Die Regel **heilt das nicht** und darf **nicht** als
Beleg für ein AC gelesen werden.

**Bekannte Lücke, nicht durch die Regel gedeckt.** W1–W3 erfassen **keine Rollenfehler**. Muster:
CAN-044 — die Quelle führt Vereine als Zielgruppe, der Canvas als „Current Alternative". Das ist
kein Deckungs-, sondern ein Einordnungsdefekt; die Regel würde ihn stillschweigend fallen
lassen. Solche Fälle sind **getrennt** zu führen (§8 Punkt 50).

**Probeanwendung (Stand 2026-07-20).** 13 der 17 `TEILBELEGT`-Fälle bleiben BLOCKER, 4 sinken auf
Nachzug (CAN-044 Rollenfehler, CAN-113 Nullifikator, REQ-001 und REQ-012 ohne Treffer, beide
kettenpflichtig). Ohne W1b: 11 zu 6. Die Aufstellung im Einzelnen steht im Regelvorschlag zu
Schritt 5 und ist **nicht** in diese Registry kopiert — sie ist eine Momentaufnahme, kein
Registerinhalt (Regel 11).

## 4. Template-Platzhalter (keine echten IDs)

`docs/EVIDENCE-LEDGER.md` enthält eine leere Eintragsvorlage, die `REQ-000`, `AC-000` und
`EV-000` als Beispielwerte führt. Das sind **keine** Requirements, Akzeptanzkriterien oder
Evidence-Einträge. Ohne diesen Eintrag hier würde jede Referenzprüfung drei Fehlalarme
erzeugen ("unbekannte ID") oder — schlimmer — drei Phantom-Requirements zählen.

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| REQ-000 | requirement | Platzhalter in der Eintragsvorlage des Evidence Ledgers | `docs/EVIDENCE-LEDGER.md` | template-placeholder | 2026-07-18 | — | — | Kein echtes Item. Von Referenz- und Abdeckungsprüfungen auszuschließen. EMPFEHLUNG an den Owner von docs/EVIDENCE-LEDGER.md (Phase 3): die Vorlage auf eine Nicht-ID-Notation umstellen (z. B. <REQ-ID>), dann entfällt dieser Sonderfall. Diese Registry ändert das Evidence Ledger nicht. |
| AC-000 | acceptance-criterion | Platzhalter in der Eintragsvorlage des Evidence Ledgers | `docs/EVIDENCE-LEDGER.md` | template-placeholder | 2026-07-18 | — | — | Kein echtes Item. Von Referenz- und Abdeckungsprüfungen auszuschließen. EMPFEHLUNG an den Owner von docs/EVIDENCE-LEDGER.md (Phase 3): die Vorlage auf eine Nicht-ID-Notation umstellen (z. B. <REQ-ID>), dann entfällt dieser Sonderfall. Diese Registry ändert das Evidence Ledger nicht. |
| EV-000 | evidence | Platzhalter in der Eintragsvorlage des Evidence Ledgers | `docs/EVIDENCE-LEDGER.md` | template-placeholder | 2026-07-18 | — | — | Kein echtes Item. Von Referenz- und Abdeckungsprüfungen auszuschließen. EMPFEHLUNG an den Owner von docs/EVIDENCE-LEDGER.md (Phase 3): die Vorlage auf eine Nicht-ID-Notation umstellen (z. B. <REQ-ID>), dann entfällt dieser Sonderfall. Diese Registry ändert das Evidence Ledger nicht. |

## 5. Verwaltungsumfang der Registry

### 5.1 Erweiterung um `USER-` und `NFR-` (Auftau-Schritt 2, 2026-07-19)

Die Registry verwaltete ursprünglich zehn Präfixe. Zwei kommen hinzu:

| Präfix | Warum jetzt aufgenommen |
|---|---|
| `USER-` | Die Nutzerentscheidung vom 2026-07-19 verlangt eine **neue Persona-ID** für „Ambitionierte Ausdauersportler:innen mit Wearables oder externen Sensoren". Eine ID zu vergeben, ohne den Raum zu verwalten, wäre genau die Ad-hoc-Vergabe, die Regel 3 verbietet. |
| `NFR-` | Die Nutzerentscheidung vom 2026-07-19 verlangt eine Entscheidung über **NFR-008** (definieren oder deprecaten). Beides sind Registry-Operationen und setzen Verwaltung voraus. `docs/prd/…prd.md` (XC-5) führt die fehlende Kollisionssicherung des `NFR-`Raums bereits als OPEN QUESTION; NFR-007 wird von DEC-005, ASM-103 und CAN-092 referenziert. |

Die Aufnahme ist **eng gefasst**: sie erfasst die bestehenden IDs vollständig (§6.12, §6.13),
deutet **keine** von ihnen um und vergibt außer der beauftragten Persona-ID keine neue. Die
übrigen vier Präfixe bleiben unverwaltet (§5.2); §8 Punkt 11 bleibt für sie offen.

### 5.2 ID-Räume, die diese Registry weiterhin **nicht** verwaltet

Diese ID-Räume existieren im Repository, sind hier aber weiterhin **nicht** erfasst. Sie sind
damit ungeschützt gegen genau den Kollisionsdefekt, den diese Registry für die anderen Räume
behebt.

| Präfix | Vorkommen | Anzahl | Bewertung |
|---|---|---|---|
| `DEC-` | `docs/decisions/decision-log.md` | 13 | **OPEN QUESTION**: Aufnahme nicht beauftragt. DEC-IDs werden von Canvas und PRD referenziert (DEC-005, DEC-011…013) und sind damit kollisionsgefährdet. |
| `SRC-` | `docs/SOURCE-MAP.md` | 8 | **OPEN QUESTION**: nicht beauftragt. |
| `VC-` | `docs/traceability.md` (Spalte `value-check-id`) | 36 | **OPEN QUESTION**: nicht beauftragt. VC-001…VC-036 haben keine Definitionsdatei — ihr Inhalt ist **MISSING**. |
| `GATE-` | `docs/prd/…prd.md`, `docs/EVIDENCE-LEDGER.md` | 7 | **OPEN QUESTION**: nicht beauftragt. |

Eine Erweiterung der Registry auf diese vier Räume ist eine Nutzerentscheidung und wird hier
nicht vorweggenommen. **Hinweis:** `VC-` zählt 36 Einträge, weil die Matrix historisch 36
Requirements führte. Diese Zahl ist nach Regel 11 **kein** Zielwert — sie ist der Altstand und
zieht der REQ-Zahl nach, nicht umgekehrt (§8 Punkt 12).

## 6. Registrierte IDs

### 6.1 VIS — Vision Items

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| VIS-001 | vision-item | Product Vision Statement: Eine Health-first Ausdauerplattform für Läufer:innen und Radfahrer:innen, die Training verständlich macht, reale lokale Gemeinsch… | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | — |
| VIS-002 | vision-item | Target Group: Primär Freizeit-Läufer:innen und Radfahrer:innen von 20–45 Jahren mit 1–4 Aktivitäten pro Woche; sekundär ambitionierte Sportler:… | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | — |
| VIS-003 | vision-item | User Need: Nutzer benötigen verlässliches Tracking, verständliche statt abstrakte Health-Auswertung, konkrete Fortschrittssignale und einen… | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | **TEIL-HERABSTUFUNG 2026-07-20 (Runde 6), Nutzerauftrag Schritt 2.** Die Board-Zeile führt `EXPLICIT \| SRC-001`. Das ist für **zwei Klauseln nicht haltbar**; sie stehen ab jetzt auf **ASSUMPTION**, der übrige Bedürfniskern bleibt unverändert `EXPLICIT`. **(a) „sicher" als Attribut des Zugangs:** „Trainingspartner" und „Zugang" kommen in **keiner** der vier Quellen vor; die Verbundaussage „sicherer Zugang zu lokalen Trainingspartnern" entsteht erst durch Zusammensetzen von SRC-001:26/:51 (Anschluss) mit SRC-001:98/:196 (Schutzmechanismen **anderer** Gegenstände) — eine Ableitung über ein Zwischenglied. **(b) „verlässlich" beim Tracking:** 0 Treffer; belegt ist der Qualifizierer nur auf **NFR-Ebene** (SRC-001:250 Distanzabweichung, :252 Zuverlässigkeit), nicht auf Bedürfnisebene; SRC-001:18 bestreitet ein Aufzeichnungsdefizit sogar ausdrücklich. **DREI GEGENPRÜFUNGSEINWÄNDE, sichtbar abgebildet statt übernommen:** (1) Die Absenzbehauptung ist zu **eng** zu fassen — die Quellen führen sehr wohl eine Schutzarchitektur um den sozialen Kontakt (SRC-001:36 Profile standardmäßig privat, SRC-003:374 Follower-Anfrage mit Annehmen/Ablehnen, SRC-001:236 / SRC-003:524 Blockieren). Sie führen sie nur **nie als Nutzerbedürfnis**. Nicht belegt ≠ von der Quelle verneint. (2) **CAN-017 wird NICHT aufgelöst.** Der reservierte BLOCKER verliert seine Formulierungsgrundlage, nicht seinen Gegenstand: SRC-003:704 („Live Location = Stalking-Risiko") und SRC-003:713 tragen ein Sicherheitsproblem unabhängig von VIS-003. (3) Eine Verengung des Kerns darf **nicht** „gemeinsames Training und reale Treffen" mitschneiden — wortnah belegt in SRC-001:22, :26, :47, :136 und SRC-003:64; ohne diesen Gehalt bräche TRC-022 nach dem repo-eigenen VIS-004-Maßstab. **FOLGE, die zu tragen ist:** TRC-004 benennt „verlässliches Tracking" als **tragende Klausel** — die Zeile **bricht** und ist nicht bloß berührt; REQ-004 liegt auf GATE-A0. **Der Titel bleibt unverändert**, bis der Vision-Owner den Board-Wortlaut nachzieht; er ist nach §3 ein wörtliches Zitat der `canonical_file` und wird von dieser Registry nicht neu formuliert. Siehe §7.6 und §8 Punkte 45, 47, 49. |
| VIS-004 | vision-item | Product Value: Die Plattform verbindet erklärbare Trainingsbelastung, verdiente Progression, lokale Teams und reale ortsbezogene Spielmechaniken… | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | — |
| VIS-005 | vision-item | Project Goal: Zuerst einen belastbaren Health-Tracker etablieren; danach Accounts, Community, Teams und erst nach nachgewiesener Datenqualität… | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | — |
| VIS-006 | vision-item | Success Signal: W4-Retention >30 %, Check-in-Quote >50 %, Warum-Aufrufe >25 %; später Teambeitritt, gemeinsame Aktivitäten und Season-Teilnahme a… | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | — |
| VIS-007 | vision-item | Health-first Boundary: Health-Ausgaben sind Orientierung, keine Diagnose. Score und Empfehlungen müssen Datenbasis, Gründe und Unsicherheit erklären. | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | — |
| VIS-008 | vision-item | Fairness Boundary: Run und Bike besitzen getrennte Metriken, Ziele und interne Wertungen; sportübergreifender Effort wird nur mit simulierten und ve… | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | — |
| VIS-009 | vision-item | Privacy Boundary: Profile sind standardmäßig privat; Live-Standort ist pro Aktivität Opt-in, zeitlich begrenzt und start-/endpunktverschleiert; Hea… | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | — |
| VIS-010 | vision-item | Delivery Principle: Kein komplexes Community-, Territory- oder Safety-System wird vor dem Evidence-Gate der vorherigen Stufe veröffentlicht. | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | — |
| VIS-011 | vision-item | Accessibility Boundary: Jeder ausgelieferte Screen muss ohne Farbunterscheidung, mit vergrößerter Schrift und mit Screenreader vollständig bedienbar sein; Zugänglichkeit ist eine Schranke, keine Quote. | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-19 | — | — | **Neu vergeben im Auftau-Schritt 2026-07-19 (Reihenfolge eingehalten: erst hier reserviert, dann in die Vision eingetragen).** Grund: REQ-014 (Designsystem und Accessibility) war in `docs/traceability.md` an **VIS-009 (Privacy Boundary)** gehängt — null fachliche Überschneidung. Die ID war syntaktisch gültig, las sich plausibel und trug die falsche Bedeutung; genau der Fehlertyp, den §1 beschreibt. Prüfung VIS-001…VIS-010 ergab **kein** fachlich passendes Item (Begründung je Item in §6.1.1). **Source Type: ASSUMPTION**, nicht EXPLICIT — dies ist neue Produktsubstanz auf Vision-Ebene, inhaltlich abgeleitet aus REQ-014, AC-014 und NFR-005 im PRD, aber vom Nutzer nie als Vision-Aussage bestätigt. Das PRD führt REQ-014 als `EXPLICIT` mit Quelle SRC-003 — SRC-003 ist laut `docs/SOURCE-MAP.md` **nicht im Repository auffindbar (BLOCKER)**, taugt also nicht als Beleg für eine Höherstufung. **VIS-011 zählt bis zur ausdrücklichen Nutzerbestätigung NICHT als erfüllter Vision-Anker für REQ-014** (§8, Punkt 15). Die Umhängung in PRD und `docs/traceability.md` macht **Phase 2**, nicht diese Registry. |
| VIS-012 | vision-item | MISSING – Designprinzip auf Vision-Ebene (monochromes, tokenbasiertes Designsystem; Farbe nur mit fachlicher Bedeutung) | `docs/vision/revyr-endurance-platform.vision.md` | reserved | 2026-07-19 | — | — | **Reserviert im Auftau-Schritt 2 (2026-07-19).** Inhalt **MISSING**, BLOCKER. Grund: REQ-014 wurde in REQ-037 (Accessibility) und REQ-038 (monochromes Designsystem) zerlegt. VIS-011 deckt ausdrücklich **nur** die Accessibility-Hälfte ab (§6.1.1 prüfte VIS-001…VIS-010 gegen REQ-014 und fand für **keine** der beiden Hälften einen Anker; VIS-011 wurde nur für Accessibility angelegt). REQ-038 hat damit **keinen** Vision-Anker. Die Registry vergibt hier **keinen Inhalt** — ein Designprinzip auf Vision-Ebene wäre neue Produktsubstanz und braucht eine Nutzerentscheidung. Die ID ist reserviert, damit Phase 2/3 weder eine ID erfindet noch REQ-038 still an einen unpassenden VIS-Anker hängt (genau der Defekt VIS-009 ↔ REQ-014). |
| VIS-013 | vision-item | MISSING – Datenportabilität auf Vision-Ebene (Nutzer können ihre Aktivitätsdaten in einem offenen Format mitnehmen) | `docs/vision/revyr-endurance-platform.vision.md` | reserved | 2026-07-19 | — | — | **Reserviert im Auftau-Schritt 2 (2026-07-19).** Inhalt **MISSING**, BLOCKER. Grund: REQ-039 (GPX-Export) ist eine eigenständige Capability und braucht einen primären Vision-Anker. Prüfung aller bestehenden VIS-Items: VIS-003 (User Need) nennt Tracking, Health-Auswertung, Fortschrittssignale und Trainingspartner — **keine** Portabilität; VIS-009 (Privacy Boundary) regelt Sichtbarkeit und Werbenutzung, **nicht** Mitnahme. Der Export ist über REQ-034 nur **sekundär** als Constraint verknüpft (Nutzerkontrolle, Datenminimierung) — das trägt die Capability nicht (Nutzerentscheidung 2026-07-19). Inhalt braucht Nutzerentscheidung. |
| VIS-014 | vision-item | MISSING – Wiederverwendung geplanter Strecken auf Vision-Ebene | `docs/vision/revyr-endurance-platform.vision.md` | reserved | 2026-07-20 | — | — | **Reserviert in Runde 4 (2026-07-20).** Inhalt **MISSING**, BLOCKER. Grund: die angeordnete Teilung von CAN-140 erzeugt mit **REQ-041** (Wiederverwendung einer gespeicherten Route) eine Anforderung ohne Vision-Anker. `docs/traceability.md:1702` hält für den Vorgänger REQ-040 bereits ausdrücklich fest: „Für die **Streckenwiederverwendung** existiert kein Vision-Anker und **keine reservierte VIS-ID**." **Prüfung der bestehenden Items:** VIS-003 nennt verlässliches Tracking, Health-Auswertung, konkrete Fortschrittssignale und sicheren Zugang zu lokalen Trainingspartnern — **keine** Wiederverwendung geplanter Strecken; VIS-004 nennt Belastung, Progression, lokale Teams und ortsbezogene Spielmechaniken — ebenfalls nicht. Die naheliegende Lesart „Routenplanung hängt doch an VIS-003" stammt aus TRC-006 und ist dort selbst ungeprüft (§8 Punkt 40) — sie wird hier **nicht** übernommen. **ABWEICHUNG von der wörtlichen Auftragsliste:** die Aufgabe nannte nur neue CAN-, REQ-, AC-, EV- und TRC-IDs. Die VIS-Reservierung wird trotzdem vorgenommen, weil der Präzedenzfall VIS-012/VIS-013 genau für diese Lage geschaffen wurde („damit Phase 2/3 weder eine ID erfindet noch … still an einen unpassenden VIS-Anker hängt"). Ohne sie hätte TRC-041 eine leere Vision-Spalte ohne reservierte Zieladresse. Der Nutzer kann diese Abweichung überstimmen; dann bleibt der Anker als BLOCKER ohne ID (§8 Punkt 38). |

#### 6.1.1 Warum VIS-011 neu ist — Prüfung VIS-001 … VIS-010 gegen REQ-014

REQ-014 fordert ein tokenbasiertes monochromes Designsystem, Dynamic Type, Screenreader-Labels,
WCAG-AA-Kontraste und zusätzliche Symbole statt alleiniger Farbcodierung. Geprüft wurde, ob eines
der bestehenden Vision-Items diese Aussage **trägt** — nicht, ob es sich plausibel lesen lässt.

| Vision-Item | Aussage | Passt zu REQ-014? |
|---|---|---|
| VIS-001 | Produktvisionssatz (Health-first, lokale Gemeinschaft, faires Spielfeld) | nein — nennt keine Darstellungs- oder Bedienbarkeitseigenschaft |
| VIS-002 | Zielgruppe (Alter, Aktivitätsfrequenz, Vereine) | nein — Zielgruppendefinition, keine Produkteigenschaft |
| VIS-003 | User Need (Tracking, Health-Auswertung, Fortschritt, Trainingspartner) | **nein, trotz Anziehungskraft** — „verständliche statt abstrakte Health-**Auswertung**" meint die Verständlichkeit der Health-Aussage, nicht die Wahrnehmbarkeit der Oberfläche. Diesen Bezug zu nutzen wäre derselbe Fehler wie VIS-009: plausible Lesart, falsche Bedeutung. |
| VIS-004 | Product Value (Belastung, Progression, Teams, Territory) | nein — Wertversprechen der Fachfunktionen |
| VIS-005 | Project Goal (Reihenfolge der Stufen) | nein — Reihenfolgeprinzip |
| VIS-006 | Success Signals (Retention, Check-in-Quote, Warum-Aufrufe) | nein — und ausdrücklich **kein** geeigneter Anker: `docs/traceability.md` hält für REQ-014 fest, dass eine Nutzungsquote von Screenreader-Nutzern WCAG-Konformität weder belegen noch widerlegen kann und falsche Anreize setzt |
| VIS-007 | Health-first Boundary (Orientierung statt Diagnose; Datenbasis, Gründe, Unsicherheit erklären) | **nein, trotz Anziehungskraft** — die geforderte Erklärbarkeit betrifft den Health-**Inhalt** (Score, Empfehlung), nicht die Zugänglichkeit der Darstellung |
| VIS-008 | Fairness Boundary (getrennte Run/Bike-Metriken) | nein — Wertungsfairness, nicht Zugänglichkeit |
| VIS-009 | Privacy Boundary (private Profile, Live-Standort, Health-Daten nicht für Werbung) | **nein — der bestehende, fehlerhafte Anker.** Datenschutz und Accessibility haben keine gemeinsame Aussage |
| VIS-010 | Delivery Principle (kein System vor dem Evidence-Gate der Vorstufe) | nein — Freigabereihenfolge |

**Ergebnis: kein passendes Item vorhanden.** Der Befund deckt sich mit drei unabhängigen
Vorbefunden im Repository: `docs/prd/…prd.md:554`, `docs/traceability.md:517` und
`docs/traceability.md:1444` halten jeweils fest, dass REQ-014 an VIS-009 hängt und **kein**
VIS-Item Accessibility abdeckt. `docs/traceability.md:1444` beließ VIS-009 bewusst als Link und
vermerkte nur den Befund; dieser Schritt behebt die Ursache. Ein semantisch falscher Anker bleibt
nicht bestehen, nur weil die ID existiert.

**Abgrenzung zu CAN-099.** VIS-011 ersetzt **nicht** CAN-099 (reservierte Canvas-Constraint
„Accessibility-Verbindlichkeit"). Beide Lücken bestehen unabhängig: die Vision-Lücke schließt
VIS-011 vorbehaltlich Nutzerbestätigung, die Canvas-Lücke bleibt als BLOCKER offen (§8, Punkt 3).
REQ-014 hat zusätzlich **keinen** atomaren Canvas-Anker für das tokenbasierte monochrome
Designsystem — auch das bleibt offen.

### 6.2 CAN — Legacy-Canvas-Items (deprecated)

Alle zwölf Ursprungs-Items waren Sammelblöcke mit mehreren, unabhängig prüfbaren Aussagen in
einer Zelle. Sie sind durch atomare Items ersetzt (Abschnitt 6.3) und werden **nicht gelöscht**.
Neue Referenzen auf diese IDs sind ein Validierungsfehler.

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-001 | canvas-item (Sammelblock) | Canvas-Abschnitt „Problem“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-013 … CAN-015 | Zerlegt in 3 atomare Items plus reservierte, inhaltlich offene Lücken CAN-016 … CAN-022. |
| CAN-002 | canvas-item (Sammelblock) | Canvas-Abschnitt „Users / Customers“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-023 … CAN-027 | Zerlegt in 5 atomare Items. |
| CAN-003 | canvas-item (Sammelblock) | Canvas-Abschnitt „Value Promise“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-028 … CAN-038 | Zerlegt in 11 atomare Items. |
| CAN-004 | canvas-item (Sammelblock) | Canvas-Abschnitt „Current Alternatives“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-039 … CAN-046 | Zerlegt in 8 atomare Items. |
| CAN-005 | canvas-item (Sammelblock) | Canvas-Abschnitt „Key Capabilities“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-047 … CAN-070 | Zerlegt in 24 atomare Items plus reservierte, inhaltlich offene Lücke CAN-071. |
| CAN-006 | canvas-item (Sammelblock) | Canvas-Abschnitt „Non-Goals“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-072 … CAN-079 | Zerlegt in 8 atomare Items. |
| CAN-007 | canvas-item (Sammelblock) | Canvas-Abschnitt „Constraints“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-080 … CAN-098 | Zerlegt in 19 atomare Items plus reservierte, inhaltlich offene Lücke CAN-099. |
| CAN-008 | canvas-item (Sammelblock) | Canvas-Abschnitt „Risks“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-100 … CAN-110 | Zerlegt in 11 atomare Items. |
| CAN-009 | canvas-item (Sammelblock) | Canvas-Abschnitt „Success Signal“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-124 … CAN-129 | Zerlegt in 6 atomare Items plus reservierte, inhaltlich offene Lücke CAN-130. |
| CAN-010 | canvas-item (Sammelblock) | Canvas-Abschnitt „Evidence“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-111 … CAN-123 | Zerlegt in 13 atomare Items. |
| CAN-011 | canvas-item (Sammelblock) | Canvas-Abschnitt „Allowed Scope“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | CAN-131 … CAN-137 | Zerlegt in 7 atomare Items. |
| CAN-012 | canvas-item (Sammelblock) | Canvas-Abschnitt „Unresolved Questions“ | `docs/canvas/revyr-endurance-platform.canvas.md` | deprecated | 2026-07-18 | 2026-07-19 | OQ-001, OQ-003, OQ-004, OQ-005, OQ-006, OQ-007, OQ-008, OQ-011 | Ersatzlos aufgelöst: CAN-012 zählte offene Fragen auf, die der Canvas gar nicht definiert. Kanonisch ist docs/decisions/open-questions.md. Es entsteht KEIN atomares CAN-Item; Referenzen zeigen künftig direkt auf die OQ-IDs. |

### 6.3 CAN — Atomare Canvas-Items (neu, 2026-07-19)

Ein Item = **genau eine** kontrollierbare Aussage. `notes` nennt zuerst die Herkunft, damit
jede neue ID auf ihr Alt-Item und ihre Fundstelle zurückführbar bleibt.

#### Problem (10 Items)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-013 | canvas-item / problem | Bestehende Tracker liefern Daten ohne verständliche Bedeutung. | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-001, Tabellenzelle CAN-001 + Prosa 'Problem'. Ersetzt Facette CAN-001-a aus docs/traceability.md. |
| CAN-014 | canvas-item / problem | Soziale Interaktion findet ohne lokale Bindung statt. | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-001, Tabellenzelle CAN-001 + Prosa 'Problem'. Ersetzt Facette CAN-001-b aus docs/traceability.md. |
| CAN-015 | canvas-item / problem | Es gibt zu wenig Anlass für echte gemeinsame Aktivität. | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-001, Tabellenzelle CAN-001 + Prosa 'Problem'. Ersetzt Facette CAN-001-c aus docs/traceability.md. |
| CAN-016 | canvas-item / problem | MISSING – Fortschritts- und Motivationsproblem | `docs/canvas/revyr-endurance-platform.canvas.md` | reserved | 2026-07-19 | — | — | Herkunft: CAN-001, nicht im Canvas vorhanden. BLOCKER. REQ-015 und REQ-016 haben laut docs/traceability.md canvas-problem = MISSING, weil CAN-001 kein Fortschritts-/Motivationsproblem nennt. Inhalt ist aus keinem Artefakt ableitbar und braucht eine Nutzerentscheidung. ID reserviert, damit Phase 3 nicht selbst eine ID vergibt. |
| CAN-017 | canvas-item / problem | MISSING – Sicherheitsproblem | `docs/canvas/revyr-endurance-platform.canvas.md` | reserved | 2026-07-19 | — | — | Herkunft: CAN-001, nicht im Canvas vorhanden. BLOCKER. REQ-030 und REQ-031 haben canvas-problem = MISSING. VIS-003 nennt 'sicheren Zugang zu lokalen Trainingspartnern', der Canvas nennt kein Sicherheitsproblem – dokumentierte Canvas/Vision-Divergenz. Inhalt braucht Nutzerentscheidung. |
| CAN-018 | canvas-item / problem | MISSING – Datenschutzproblem | `docs/canvas/revyr-endurance-platform.canvas.md` | reserved | 2026-07-19 | — | — | Herkunft: CAN-001, nicht im Canvas vorhanden. BLOCKER. REQ-034 hat canvas-problem = MISSING; Datenschutz erscheint im Canvas nur als Constraint (CAN-088) und Risiko (CAN-105), nicht als Nutzerproblem. Inhalt braucht Nutzerentscheidung. |
| CAN-019 | canvas-item / problem | MISSING – Planungs- und Orientierungsproblem vor der Aktivität | `docs/canvas/revyr-endurance-platform.canvas.md` | reserved | 2026-07-19 | — | — | Herkunft: CAN-001, nicht im Canvas vorhanden. BLOCKER. REQ-006 und REQ-007 (Routenplanung, routebezogener Fortschritt) haben canvas-problem = MISSING; sie hängen aktuell nur an der Capability CAN-050/CAN-051. |
| CAN-020 | canvas-item / problem | MISSING – Fairness- und Manipulationsproblem | `docs/canvas/revyr-endurance-platform.canvas.md` | reserved | 2026-07-19 | — | — | Herkunft: CAN-001, nicht im Canvas vorhanden. BLOCKER. REQ-023 und REQ-024 haben canvas-problem = MISSING; Fairness ist im Canvas nur Wertversprechen (CAN-033/CAN-036) und Risiko (CAN-104/CAN-109). |
| CAN-021 | canvas-item / problem | MISSING – Problem hinter Einzel-Revieren und Sportplatz-Challenges | `docs/canvas/revyr-endurance-platform.canvas.md` | reserved | 2026-07-19 | — | — | Herkunft: CAN-001, nicht im Canvas vorhanden. BLOCKER. REQ-028 und REQ-029 haben canvas-problem = MISSING und laut docs/traceability.md zusätzlich weder CAN-003-Klausel noch Erfolgssignal – sie zahlen derzeit auf kein dokumentiertes Canvas-Ziel ein. |
| CAN-022 | canvas-item / problem | Ohne Anbindung bereits genutzter Sportuhren und externer Sensoren fehlen oder verschlechtern sich zentrale Trainingssignale. | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-001, nicht im Canvas vorhanden. **Inhalt entschieden durch den Nutzer am 2026-07-19** (Auftau-Schritt 2); Status daher von `reserved` auf `active`. **Wortlaut:** „Ohne Anbindung bereits genutzter Sportuhren und externer Sensoren fehlen oder verschlechtern sich zentrale Trainingssignale wie Herzfrequenz, Kadenz, Geschwindigkeit, Leistung und Höheninformationen. Dadurch werden Belastungsanalyse, sportartspezifische Auswertung und erklärbare Empfehlungen weniger vollständig und weniger zuverlässig." Item Type PROBLEM · Anker REQ-032 / AC-032 · Release Gate E · **Source Type ASSUMPTION** (bis der Wortlaut ausdrücklich nutzerbestätigt ist). **Ausdrücklich NICHT enthalten:** der Komfortaspekt „Nutzer müssen zusätzlich das Telefon mitführen" — laut Nutzerentscheidung eine separate mögliche Convenience-Aussage, die in diesem Lauf **nicht** angelegt wird und daher **keine** CAN-ID erhält. Canvas-Nachzug offen (§7.4, Nachzugsfenster nach Regel 10). |

#### Zielnutzer (5 Items)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-023 | canvas-item / target-user | Freizeit-Läufer:innen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-002, Prosa 'Users / Customers', Aufzählungspunkt 1. Zuordnung PRD: USER-001. |
| CAN-024 | canvas-item / target-user | Freizeit- und Rennradfahrer:innen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-002, Prosa 'Users / Customers', Aufzählungspunkt 1. Zuordnung PRD: USER-002. Der Canvas-Punkt nennt Laufende und Radfahrende in einem Satz; das PRD führt sie als zwei Personas, daher zwei Atome. — **HERABGESTUFT 2026-07-20 (Runde 6) auf `ASSUMPTION`, Nutzerauftrag Schritt 2.** Der Canvas führt `EXPLICIT \| SRC-001`; das trägt den Titel in seiner jetzigen Fassung nicht. Der zitierte Herkunftspunkt lautet wörtlich „Freizeit-Läufer:innen und Radfahrer:innen." und steht in SRC-001:51 unter „**Primär:**". **„Renn-" steht dort nicht** — das Wort existiert in SRC-001 ausschließlich in Zeile 52 unter „**Sekundär:**", untrennbar mit „Ambitionierte" und „mit festen Strecken und Leistungsfokus"; CAN-024 übernimmt es ohne alle drei Qualifikatoren und löscht damit eine Rangunterscheidung, die die Quelle ausdrücklich setzt. **„Freizeit-"** ist orthographisch nur an „Läufer:innen" gebunden; die Präfix-Verteilung auf „Radfahrer:innen" ist ein Zwischenglied („Freizeit" hat in SRC-002/003/004 null Treffer). **ZWEI BEFUNDSPUNKTE AUSDRÜCKLICH ZURÜCKGEWIESEN:** (1) Die Herkunftsangabe „Prosa 'Users / Customers'" ist **korrekt und am 2026-07-20 verifiziert** — `docs/canvas/…canvas.md` führt im Ursprungstext die Überschrift „## Users / Customers" mit genau vier Aufzählungspunkten; die Spalte **Herkunft** bezeichnet die canvas-interne Dekompositionsherkunft, die Spalte **Source** die Quelle. Die beiden wurden im Befund verwechselt; hier wird **nichts** geändert. (2) Eine „Doppelverwertung von SRC-001:52 durch CAN-024 und CAN-025" liegt **nicht** vor: CAN-025 stammt aus Aufzählungspunkt 2 des Ursprungstextes („Ambitionierte Ausdauersportler:innen.", buchstabengleich), nicht aus SRC-001:52. **ÜBERMASSEINWAND, sichtbar abgebildet:** ein bloßes „Radfahrer:innen" wäre **keine** Verengung, sondern begrifflich **weiter** als der Primär-Punkt — es umfasst die ambitionierten Rennradfahrenden aus SRC-001:52 mit und stellt die Verschmelzung unsichtbar wieder her, zusätzlich asymmetrisch zum Geschwisteratom CAN-023. Die Zielfassung ist deshalb **strittig** (Rangzusatz „(primär)" gegen Quellenwechsel auf `SRC-001/SRC-003`, wo SRC-003:65 „Radfahrer/Rennradfahrer" ungestuft als **eine** Zielgruppe führt und das PRD bereits `SRC-001/SRC-003` fährt) und bleibt **Nutzerentscheidung**; der Titel wird hier **nicht** geändert. **WESENTLICH:** `docs/traceability.md` führt CAN-024 für REQ-032 als „primär (Bike-Sensorik)" — Sensorik ist quellenseitig nur an der **sekundären** Persona verankert (SRC-001:137, SRC-003:65). Siehe §7.6 und §8 Punkt 46. |
| CAN-025 | canvas-item / target-user | Ambitionierte Ausdauersportler:innen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-002, Prosa 'Users / Customers', Aufzählungspunkt 2. BLOCKER: Das PRD hat für diese Zielgruppe KEINE USER-ID (nur USER-001..003). docs/traceability.md vermerkt das bei REQ-009, REQ-011 und REQ-032 als 'ambitionierte Persona MISSING im PRD'. Entweder das PRD ergänzt eine USER-ID (Phase 3, PRD-Owner) oder der Canvas streicht die Zielgruppe – beides braucht eine Nutzerentscheidung. |
| CAN-026 | canvas-item / target-user | Lauf- und Radsportgruppen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-002, Prosa 'Users / Customers', Aufzählungspunkt 3. Zuordnung PRD: USER-003. |
| CAN-027 | canvas-item / target-user | Vereine und lokale Communities | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-002, Prosa 'Users / Customers', Aufzählungspunkt 4. Zuordnung PRD: USER-003. OPEN QUESTION: Der Punkt fasst Vereine (Rechtsträger) und lokale Communities (informell) zusammen; ob das PRD zwei getrennte USER-IDs braucht, ist nicht entschieden. |

#### Value Promise (11 Items)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-028 | canvas-item / value-promise | Verlässliches Tracking | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Prosa 'Value Promise' (Blockzitat). Ersetzt Facette CAN-003-p1. Kernbefund der Atomisierung: Diese Klausel stand NUR im Prosa-Block, nicht in der CAN-003-Tabellenzeile. REQ-001..REQ-007 (sieben A0-REQs) konnten deshalb bisher nur auf Prosa zeigen. |
| CAN-029 | canvas-item / value-promise | Verstehe deine Belastung (erklärbare Trainingsorientierung) | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Tabellenzelle CAN-003 + Prosa. Ersetzt Facette CAN-003-v1. |
| CAN-030 | canvas-item / value-promise | Erkenne deinen Fortschritt | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Tabellenzelle CAN-003. Ersetzt Facette CAN-003-v2. |
| CAN-031 | canvas-item / value-promise | Trainiere sicherer | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Tabellenzelle CAN-003. Ersetzt Facette CAN-003-v3. OPEN QUESTION (aus docs/traceability.md, REQ-030): Der Canvas lässt offen, ob 'sicherer' Trainingssicherheit oder Datensicherheit meint. Die Klausel ist bis zur Klärung nicht prüfbar. |
| CAN-032 | canvas-item / value-promise | Finde reale lokale Gemeinschaft | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Tabellenzelle CAN-003 + Prosa. Ersetzt Facette CAN-003-v4. |
| CAN-033 | canvas-item / value-promise | Spielmechaniken verdrängen die Health-Grundlage nicht | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Tabellenzelle CAN-003. Ersetzt Facette CAN-003-v5. |
| CAN-034 | canvas-item / value-promise | Verdiente Progression | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Prosa 'Value Promise' (Blockzitat). Nur im Prosa-Block, nicht in der Tabellenzelle – gleiches Defektmuster wie CAN-028. |
| CAN-035 | canvas-item / value-promise | Reihenfolge: Tracking und Health zuerst, Progression, Gemeinschaft und Territory danach | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Prosa 'Value Promise' (Blockzitat). Nur im Prosa-Block. Inhaltlich deckungsgleich mit VIS-005 und den Stufen CAN-131..CAN-137. |
| CAN-036 | canvas-item / value-promise | Fairness-Gate vor späteren Stufen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Prosa 'Value Promise' (Blockzitat, 'klare Fairness-, Privacy- und Evidence-Gates'). Der Prosa-Satz nennt drei Gates in einer Aufzählung; sie werden von unterschiedlichen REQs getragen (Fairness: REQ-023/REQ-024) und sind daher getrennte Atome. |
| CAN-037 | canvas-item / value-promise | Privacy-Gate vor späteren Stufen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Prosa 'Value Promise' (Blockzitat). Getragen von REQ-018 und REQ-034. |
| CAN-038 | canvas-item / value-promise | Evidence-Gate vor späteren Stufen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-003, Prosa 'Value Promise' (Blockzitat). Getragen von REQ-035 und REQ-036. |

#### Current Alternatives (8 Items)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-039 | canvas-item / alternative | Strava | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-004, Tabellenzelle CAN-004 + Prosa-Tabelle 'Current Alternatives'. Stärke: Tracking, Segmente, Netzwerk. Adressierte Lücke: lokale Team- und Territory-Mechanik sowie erklärbarer Health-Fokus. |
| CAN-040 | canvas-item / alternative | Garmin Connect | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-004, Tabellenzelle CAN-004 + Prosa-Zeile 'Garmin/Apple/Google/Fitbit'. Stärke: Geräte- und Health-Ökosystem. Lücke: plattformübergreifende lokale Community und verdiente Progression. Die Prosa-Zeile fasst vier Anbieter zusammen; die CAN-004-Zelle nennt sie einzeln. |
| CAN-041 | canvas-item / alternative | Apple Fitness | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-004, Tabellenzelle CAN-004 + Prosa-Zeile 'Garmin/Apple/Google/Fitbit'. Stärke und Lücke wie CAN-040 (gemeinsame Prosa-Zeile). |
| CAN-042 | canvas-item / alternative | Google/Fitbit | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-004, Tabellenzelle CAN-004 + Prosa-Zeile 'Garmin/Apple/Google/Fitbit'. Stärke und Lücke wie CAN-040 (gemeinsame Prosa-Zeile). |
| CAN-043 | canvas-item / alternative | Whoop | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-004, Tabellenzelle CAN-004 + Prosa-Tabelle. Stärke: Belastungs- und Recovery-Fokus. Lücke: Transparenz, Smartphone-Basis und lokale Community. |
| CAN-044 | canvas-item / alternative | Lauf- und Radsportvereine | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-004, Tabellenzelle CAN-004 + Prosa-Zeile 'WhatsApp/Vereine'. Stärke: reale Gruppen. Lücke: strukturierte Aktivitäten, Fortschritt und sichere Auffindbarkeit. |
| CAN-045 | canvas-item / alternative | WhatsApp-Gruppen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-004, Tabellenzelle CAN-004 + Prosa-Zeile 'WhatsApp/Vereine'. Stärke und Lücke wie CAN-044 (gemeinsame Prosa-Zeile). |
| CAN-046 | canvas-item / alternative | Lokale Event-Plattformen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-004, nur Tabellenzelle CAN-004. MISSING: Die Prosa-Tabelle 'Current Alternatives' enthält für diese Alternative KEINE Zeile; Stärke und adressierte Lücke sind nicht dokumentiert. |

#### Key Capabilities (24 aktiv + CAN-071 deprecated; Nachfolger in §6.3.1)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-047 | canvas-item / capability | Run und Bike als zwei getrennte, gleichwertige Sportmodi in einer App | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 ('Robustes Run/Bike-Tracking') + Prosa 1. Trägt REQ-001 (Sportmodus als zentrale Konfiguration). |
| CAN-048 | canvas-item / capability | Robustes Foreground-Tracking | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 + Prosa 1. Trägt REQ-002. |
| CAN-049 | canvas-item / capability | Background- und Recovery-Verhalten | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 1 ('mit robustem Background- und Recovery-Verhalten'). Trägt REQ-003. Eigenes Atom, weil separat prüfbar (EV-003) und mit eigenem Risiko (CAN-108 Store-Ablehnung). |
| CAN-050 | canvas-item / capability | Routenplanung und gespeicherte Routen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 ('geplante Routen') + Prosa 2. Trägt REQ-006. |
| CAN-051 | canvas-item / capability | Echte routebezogene Restdistanz | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 2 ('echte routebezogene Restdistanz'). Trägt REQ-007. Eigenes Atom, weil DEC-004 die einfache Distanzsubtraktion ausdrücklich verbietet. |
| CAN-052 | canvas-item / capability | Erklärbarer Health-Score mit Fallback und Confidence | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 ('erklärbare Health-Auswertung') + Prosa 3. Trägt REQ-009 bis REQ-013. |
| CAN-053 | canvas-item / capability | Progression | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 + Prosa 4. |
| CAN-054 | canvas-item / capability | Rückblicke | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 4. Trägt REQ-016. |
| CAN-055 | canvas-item / capability | Verdiente Avatar-Identität | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 4. Trägt REQ-015. |
| CAN-056 | canvas-item / capability | Accounts | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 + Prosa 5. Trägt REQ-017. |
| CAN-057 | canvas-item / capability | Privacy-Einstellungen und Sichtbarkeitssteuerung | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 5. Trägt REQ-018. |
| CAN-058 | canvas-item / capability | Routenempfehlungen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 5. Trägt REQ-019. |
| CAN-059 | canvas-item / capability | Moderation | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 5. Trägt REQ-018. |
| CAN-060 | canvas-item / capability | Lokale Teams | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 + Prosa 6. Trägt REQ-020 und REQ-021. |
| CAN-061 | canvas-item / capability | Challenges | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 + Prosa 6. Trägt REQ-025. |
| CAN-062 | canvas-item / capability | Rankings | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 6. Trägt REQ-023 und REQ-025. |
| CAN-063 | canvas-item / capability | Anti-Cheat | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 6. Trägt REQ-024. |
| CAN-064 | canvas-item / capability | Team-Territory | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 ('Territory') + Prosa 7. Trägt REQ-026. |
| CAN-065 | canvas-item / capability | Einzel-Territory | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 7. Trägt REQ-028. Achtung: laut CAN-079 im ersten Release ausgeschlossen. |
| CAN-066 | canvas-item / capability | Seasons | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 7. Trägt REQ-027. |
| CAN-067 | canvas-item / capability | Lokale Events | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 7. Trägt REQ-022. |
| CAN-068 | canvas-item / capability | Live-Safety | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 + Prosa 8. Trägt REQ-030 und REQ-031. |
| CAN-069 | canvas-item / capability | Wearable-Anbindung | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Tabellenzelle CAN-005 + Prosa 8. Trägt REQ-032. |
| CAN-070 | canvas-item / capability | Erklärbare Coach-Funktionen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-005, Prosa 8. Trägt REQ-033. |
| CAN-071 | canvas-item / capability | MISSING – Verlauf, Detailansicht und GPX-Export | `docs/canvas/revyr-endurance-platform.canvas.md` | **deprecated** | 2026-07-19 | 2026-07-19 | CAN-138, CAN-139, CAN-140 | **Deprecated im Auftau-Schritt 2 (2026-07-19).** Grund (Nutzerentscheidung): CAN-071 trägt **mindestens drei fachlich getrennte Capabilities** — Verlauf/Detailansicht, GPX-Export, Streckenwiederverwendung/-vergleich — und darf nicht als **ein** atomares Item bestehen bleiben. Sie liegen zudem auf **zwei verschiedenen Release-Stufen** (A0 bzw. A2), was in einem gemeinsamen Item nicht abbildbar ist. Ersetzt durch CAN-138 (A0), CAN-139 (A2), CAN-140 (A2). Migrationstabelle: §7.4. Neue Referenzen auf CAN-071 sind ein Validierungsfehler. **TRANSITIVE NACHFOLGE (Runde 4, 2026-07-20):** CAN-140 ist seit dem 2026-07-20 **selbst deprecated** und durch CAN-142 und CAN-143 ersetzt. Die `replacement_id`-Spalte bleibt nach Regel 1 unverändert (sie hält den Stand der eigenen Ausmusterung fest), aber die **wirksame Nachfolgemenge von CAN-071 ist CAN-138, CAN-139, CAN-142, CAN-143**. Wer CAN-071 mechanisch auflöst, muss die Kette **bis zu einem aktiven Eintrag** weiterverfolgen — ein Nachzug, der auf CAN-140 stehen bleibt, landet auf einer deprecateten ID. Dieselbe Regel gilt für REQ-008 → REQ-040 → REQ-041/REQ-042. |

#### 6.3.1 Neue atomare Items aus Auftau-Schritt 2 (2026-07-19)

Vier neue Items. Drei davon lösen CAN-071 ab, eines schließt die Designsystem-Lücke, die §6.1.1
für REQ-014 ausdrücklich festgehalten hatte („REQ-014 hat **keinen** atomaren Canvas-Anker für
das tokenbasierte monochrome Designsystem").

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-138 | canvas-item / capability | Verlauf und Detailansicht lokal gespeicherter Run- und Bike-Aktivitäten | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | **Nachfolger 1 von 3 für CAN-071.** **Kanonischer Wortlaut (Runde 4, 2026-07-20):** „Nutzer können lokal gespeicherte Run- und Bike-Aktivitäten in einem Verlauf anzeigen und eine ausgewählte Aktivität mit Route, Dauer, Distanz und sportartspezifischer Kernmetrik in einer Detailansicht öffnen." (Alt: „…eine Detailansicht mit Strecke, Dauer, Distanz … öffnen." — dieselbe Aussage, präzisierter Wortlaut, **keine** neue ID.) **CAN-138 BLEIBT EIN GEMEINSAMES ITEM — es wird ausdrücklich NICHT geteilt.** Begründung nach der Atomisierungsregel: (a) beide Funktionen gehören zum selben **A0-Nutzerfluss**; (b) die Detailansicht ist die **unmittelbare Vertiefung** des Verlaufs und nicht unabhängig auslieferbar; (c) beide werden gemeinsam durch **REQ-008** ausgeliefert; (d) **gleiches Gate** (A0); (e) **gleiches lokales Aktivitätsmodell**. Damit ist kein einziges Trennkriterium der Regel erfüllt — mehrere Verben allein trennen nicht. **Release-Stufe A0.** Trägt REQ-008 in seiner **verengten** Fassung; **GPX-Export und Streckenvergleich gehören NICHT dazu** (REQ-039 bzw. REQ-041/REQ-042). Source Type **ASSUMPTION**, solange der Wortlaut nicht ausdrücklich nutzerbestätigt ist. Canvas-Nachzug offen (Regel 10, §7.5). |
| CAN-139 | canvas-item / VALUE PROMISE · CAPABILITY | Datenportabilität und GPX-Export abgeschlossener Aktivitäten | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | **Nachfolger 2 von 3 für CAN-071.** **Wortlaut in Runde 4 (2026-07-20) auf den kanonischen Text der Nutzerentscheidung gezogen; KEINE neue ID** (das vorhandene aktive Item trägt dieselbe Aussage — Begründung §6.3.3 C). **Kanonischer Wortlaut (verbindlich):** „Nutzer behalten Kontrolle über ihre aufgezeichneten Aktivitäten und können eine abgeschlossene Run- oder Bike-Aktivität als standardkonforme GPX-Datei exportieren, ohne sie veröffentlichen oder mit anderen Nutzern teilen zu müssen." **Item Type VALUE PROMISE / CAPABILITY** · **Source Type EXPLICIT** (vorher ASSUMPTION — der Nutzer hat den Wortlaut am 2026-07-20 als verbindlich gesetzt) · `measurement_type` OPERATIONAL_QUALITY. **Primäres Requirement: REQ-039.** **REQ-034 bleibt AUSSCHLIESSLICH sekundärer Security-/Privacy-/Portabilitäts-Constraint** — das GPX-Canvas-Item darf **nicht allein über REQ-034 getragen** werden. **Release-Stufe A2**, spätestens vor öffentlichem v1.0-Release. **BEFUND (§8 Punkt 36):** der kanonische Text nennt die Klausel „in einer kompatiblen Fremdanwendung öffnen" **nicht mehr**; AC-039 (d) und EV-039 verlangen sie weiterhin. Der Bezug ist über „**standardkonforme** GPX-Datei" tragbar (Interoperabilität ist die operative Probe auf Standardkonformität), aber er ist nicht mehr wörtlich belegt — das wird **offengelegt statt stillschweigend gedeckt**. Canvas-Nachzug offen. |
| CAN-140 | canvas-item / capability | Streckenwiederverwendung und Vergleich fachlich vergleichbarer Aktivitäten | `docs/canvas/revyr-endurance-platform.canvas.md` | **deprecated** | 2026-07-19 | 2026-07-20 | CAN-142, CAN-143 | **Deprecated in Runde 4 (2026-07-20) auf Nutzerentscheidung.** Grund: CAN-140 trägt **zwei** Aussagen, die nach der Atomisierungsregel zu trennen sind — eine **Planungsfunktion** (eine gespeicherte Route erneut als Grundlage einer geplanten Aktivität verwenden) und eine **Auswertungsfunktion** (vergleichbare Aktivitäten anhand sportartspezifischer Kennzahlen vergleichen). Sie sind **unabhängig auslieferbar**, haben **unterschiedliche Nutzerwerte** (Vorbereitung vs. Rückblick), brauchen **unterschiedliche Acceptance Criteria** und können **unabhängig bestehen oder scheitern**: die Wiederverwendung ist schon heute vollständig spezifizierbar, der Vergleich ist es ohne OQ-015 **nicht**. Ein gemeinsames Item ketten den lieferbaren Teil an eine offene Forschungsfrage. Ersetzt durch **CAN-142** (Planung) und **CAN-143** (Auswertung). Neue Referenzen auf CAN-140 sind ein Validierungsfehler. Migration: §7.5. |
| CAN-141 | canvas-item / DESIGN CONSTRAINT · PRODUCT PRINCIPLE | Tokenbasiertes, überwiegend monochromes Designsystem; Farbe nur mit fachlicher Bedeutung | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | **Neu vergeben im Auftau-Schritt 2 (2026-07-19); Wortlaut in Runde 4 (2026-07-20) auf den kanonischen Text gezogen, KEINE neue ID** (Begründung §6.3.3 B). **Kanonischer Wortlaut (verbindlich):** „Die Anwendung verwendet ein tokenbasiertes, überwiegend monochromes Designsystem. Farbe wird nur eingesetzt, wenn sie eine definierte fachliche Bedeutung besitzt: Health-Status, Team- und Revieridentität, Sportplatz-Gold sowie bestätigte Feiermomente. Run und Bike werden nicht ausschließlich durch Farbe unterschieden." **Item Type DESIGN CONSTRAINT / PRODUCT PRINCIPLE** · **Source Type EXPLICIT**. **Primäres Requirement: REQ-038.** **Darf NICHT mit Accessibility kombiniert werden.** **Farbregel-Bereinigung (Runde 4):** die generische Klausel „Farbe ist nie der einzige Informationsträger" ist aus CAN-141 **entfernt** und wird ausschließlich von **CAN-099** getragen (§6.3.3 C). Der frühere Registry-Vermerk, sie wirke „in CAN-099 als Accessibility-Schranke und in CAN-141 als Gestaltungsregel — dieselbe Beobachtung, zwei getrennt prüfbare Pflichten", war die belegte **doppelt geführte Pflicht** und ist damit aufgehoben. In CAN-141 verbleibt ausschließlich die **engere** Regel „Run und Bike werden nicht ausschließlich durch Farbe unterschieden" — eine Gestaltungsregel über zwei bestimmte Zustände, keine allgemeine Wahrnehmbarkeitsschranke. Canvas-Nachzug offen. |

#### 6.3.3 Runde 4 (2026-07-20) — kanonische Anker und Teilung von CAN-140

##### Vorgehensregel bei der ID-Vergabe (Abweichung von der wörtlichen Anweisung, ausdrücklich gemeldet)

Die Anweisung lautete wörtlich, für die drei kanonischen Aussagen „jeweils die nächste
tatsächlich freie CAN-ID zu reservieren". Für **alle drei** existiert jedoch bereits ein
**aktives** Item aus Runde 3. Drei neue IDs zu vergeben, hätte drei Dubletten erzeugt — exakt die
Defektklasse, gegen die Abschnitt C derselben Entscheidung die Regel aufstellt („nicht beide
aktiv lassen, eine ID als kanonisch bestimmen, die andere deprecaten"). Angewandte Regel:

- **Trägt ein vorhandenes aktives Item dieselbe Aussage** → dessen Wortlaut wird auf den
  kanonischen Text gezogen, **keine neue ID**.
- **Trägt es eine andere Aussage** → neue ID reservieren, Altitem deprecaten und migrieren.

| Aussage | Vorhandenes aktives Item | Trägt es dieselbe Aussage? | Entscheidung |
|---|---|---|---|
| **A — Accessibility** | **CAN-099** („WCAG 2.2 AA … Schriftgrößen, Screenreader, Fokusführung, Kontraste, Bedienflächen … Farbe nie einziger Informationsträger") | **Ja.** Dieselbe Pflicht, dieselbe Prüfrichtung, dieselben Gates. Der kanonische Text benennt zusätzlich die **Zielgruppe** („visuelle, motorische und assistive Anforderungen") und macht Schriftskalierung und Bedienflächen explizit — das ist eine **Präzisierung derselben Aussage**, keine neue. | **Vorhandenes Item aktualisiert. KEINE neue ID.** |
| **B — Monochromes Designsystem** | **CAN-141** (tokenbasiert, überwiegend monochrom, vier zulässige Farbbedeutungen, Run/Bike nicht nur farblich) | **Ja.** Wortgleich bis auf „nur **dort eingesetzt, wo** sie eine fachliche Bedeutung besitzt" → „nur eingesetzt, **wenn** sie eine **definierte** fachliche Bedeutung besitzt". | **Vorhandenes Item aktualisiert. KEINE neue ID.** |
| **C — Datenportabilität / GPX** | **CAN-139** („abgeschlossene Aktivität als standardkonforme GPX-Datei exportieren und in einer kompatiblen Fremdanwendung öffnen") | **Ja im Kern.** Identische Capability (abgeschlossene Run-/Bike-Aktivität → standardkonforme GPX-Datei). Der kanonische Text **ergänzt** den Kontrollgedanken und die Klausel „ohne veröffentlichen oder teilen zu müssen" und **entfernt** die Fremd-App-Klausel. Beides ändert den Item Type (CAPABILITY → VALUE PROMISE / CAPABILITY), nicht die Aussage. | **Vorhandenes Item aktualisiert. KEINE neue ID.** Die entfernte Fremd-App-Klausel ist als Befund offengelegt (§8 Punkt 36) statt stillschweigend weiterbehauptet. |

**Damit weicht dieser Schritt in drei Fällen von der wörtlichen Anweisung ab.** Die Abweichung
ist hier vollständig benannt, damit der Nutzer sie überstimmen kann. Wird sie überstimmt, sind
CAN-142/CAN-143 **nicht** die betroffenen IDs — für A/B/C müssten dann drei **weitere** freie
IDs vergeben und CAN-099/CAN-139/CAN-141 deprecatet werden.

##### Farbregel — welches Item die Klausel kanonisch trägt

Der belegte Befund war: „Farbe nie einziger Informationsträger" stand **gleichzeitig** in
CAN-099 und (als Registry-Vermerk) in CAN-141 — eine doppelt geführte Pflicht mit zwei Ownern,
zwei Nachweisen und keiner Instanz, die entscheidet, welcher gilt.

**Entscheidung: CAN-099 trägt die Klausel kanonisch.** Begründung: die Klausel schützt die
**Wahrnehmbarkeit** von Information. Ihr Ausfall trifft Menschen mit Farbfehlsichtigkeit und ist
ein **Zugänglichkeitsdefekt**, kein Gestaltungsdefekt — ein monochromes Produkt kann die Klausel
verletzen (zwei Grautöne als einziger Unterschied), ein farbiges kann sie erfüllen. Die beiden
Aussagen sind also nicht dieselbe Beobachtung aus zwei Blickwinkeln, sondern **unabhängig**.
CAN-141 behält ausschließlich die engere Regel „Run und Bike werden nicht ausschließlich durch
Farbe unterschieden": ein konkretes Unterscheidungspaar, prüfbar gegen die Design-Tokens.
**Es entsteht keine dritte Farbregel.** CAN-099 bleibt ausschließlich Accessibility.

##### Teilung von CAN-140 — Prüfung auf bestehende atomare IDs (geprüft, nicht angenommen)

| Hälfte | Kandidat | Trägt der Kandidat die Aussage? |
|---|---|---|
| **Item 1 — Planung/Wiederverwendung** | **CAN-050** „Routenplanung und gespeicherte Routen" | **Nein.** CAN-050 stammt aus der CAN-005-Zelle „geplante Routen" und trägt REQ-006 (**Gate A0**): eine Route **anlegen** und **speichern**. Die erneute Verwendung einer bereits gespeicherten Route als Grundlage einer neuen geplanten Aktivität liegt auf **Gate A2** und ist eine andere Handlung. CAN-050 dafür zu benutzen wäre die plausible Lesart mit falscher Bedeutung. **Nebenbefund:** CAN-050 ist selbst ein Composite („Planung" + „gespeicherte Routen") — §8 Punkt 39. |
| | **REQ-006 / AC-006 / EV-006** | **Nein.** REQ-006 lautet: „Nutzer MÜSSEN eine Route über Wegpunkte oder ein Distanzziel planen, das korrekte Run-/Bike-Routingprofil verwenden und den Plan vor dem Start prüfen können." Kein Wort über die Wiederverwendung einer gespeicherten Route. `prd.md:1626` hält denselben Befund für den Vorgänger REQ-040 bereits fest. |
| **Item 2 — Auswertung/Vergleich** | alle aktiven CAN-/REQ-Items | **Nein.** Die Aussage stand ausschließlich als Teilklausel im Composite REQ-008 und danach in CAN-140/REQ-040. |

**Ergebnis: für beide Hälften sind neue IDs zu vergeben.** CAN-140, REQ-040, AC-040, EV-040 und
TRC-040 werden deprecatet, nicht umgedeutet.

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-142 | canvas-item / capability | Wiederverwendung einer gespeicherten Route als Grundlage einer geplanten Aktivität | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-20 | — | — | **Nachfolger 1 von 2 für CAN-140 (Planungsfunktion).** **Kanonischer Wortlaut (Nutzerentscheidung 2026-07-20):** „Nutzer können eine gespeicherte Route erneut als Grundlage einer geplanten Run- oder Bike-Aktivität verwenden." **Release-Stufe A2.** Trägt **REQ-041**; AC-042, EV-043, TRC-041. **Source Type ASSUMPTION** — der Wortlaut stammt aus der Nutzerentscheidung, ist aber in keiner Nutzerquelle als Anforderungstext belegt (SRC-001/SRC-003 sind laut `docs/SOURCE-MAP.md` nicht auffindbar). **Vollständig spezifizierbar ohne OQ-015** — genau deshalb von CAN-143 getrennt. **Abgrenzung zu CAN-050:** CAN-050 ist das Anlegen und Speichern einer Route (A0, REQ-006), CAN-142 ist deren erneute Verwendung (A2). Canvas-Nachzug offen. |
| CAN-143 | canvas-item / capability | Vergleich fachlich vergleichbarer Aktivitäten auf derselben oder hinreichend ähnlichen Strecke | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-20 | — | — | **Nachfolger 2 von 2 für CAN-140 (Auswertungsfunktion).** **Kanonischer Wortlaut (Nutzerentscheidung 2026-07-20):** „Nutzer können fachlich vergleichbare Aktivitäten auf derselben oder hinreichend ähnlichen Strecke anhand sportartspezifischer Kennzahlen miteinander vergleichen." **Release-Stufe A2.** Trägt **REQ-042**; AC-043, EV-044, TRC-042. **Source Type ASSUMPTION.** **Benötigt zusätzliche Regeln zur Streckenähnlichkeit** — die Vergleichslogik bleibt **RESEARCH_HYPOTHESIS bzw. MISSING**, solange **OQ-015** offen ist: wann zwei Strecken als vergleichbar gelten, tolerierte Abweichung, verglichene Kennzahlen, Behandlung verkürzter/verlängerter/abgebrochener Aktivitäten, keine irreführende Bestzeit bei nicht vergleichbarer Geometrie. **Run und Bike strikt getrennt.** Canvas-Nachzug offen. |

#### Non-Goals (8 Items)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-072 | canvas-item / non-goal | Kein Medizinprodukt und keine medizinische Diagnose | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-006, Tabellenzelle CAN-006 + Prosa 'Non-Goals'. |
| CAN-073 | canvas-item / non-goal | Keine garantierte Unfallhilfe | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-006, Prosa 'Non-Goals'. Nur in der Prosa, nicht in der CAN-006-Zelle. Berührt REQ-031 unmittelbar. |
| CAN-074 | canvas-item / non-goal | Kein Chat-Messenger und kein allgemeiner Messenger | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-006, Tabellenzelle CAN-006 + Prosa. |
| CAN-075 | canvas-item / non-goal | Kein Verkauf von Leistungsstatus, Leistungs-Boosts oder Spielvorteilen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-006, Tabellenzelle CAN-006 + Prosa. |
| CAN-076 | canvas-item / non-goal | Keine Indoor-, Gym- oder Workout-Plattform | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-006, Tabellenzelle CAN-006 + Prosa. |
| CAN-077 | canvas-item / non-goal | Kein vollwertiger Web-Client | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-006, nur Tabellenzelle CAN-006. Nur in der Zelle, nicht in der Prosa-Liste. |
| CAN-078 | canvas-item / non-goal | Kein sichtbares H3- oder Raster-Gameplay | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-006, nur Prosa 'Non-Goals'. Nur in der Prosa, nicht in der CAN-006-Zelle. |
| CAN-079 | canvas-item / non-goal | Kein Territory-System im ersten Release / Tracker-MVP | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-006, Tabellenzelle CAN-006 + Prosa. |

#### Constraints (20 Items)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-080 | canvas-item / constraint | Eine gemeinsame iOS-/Android-Codebasis | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Tabellenzelle CAN-007. |
| CAN-081 | canvas-item / constraint | Expo/React Native/TypeScript als App-Basis; native Dev-Builds für Background-, Health- und Widget-Funktionen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Prosa 'Constraints', Punkt 1. |
| CAN-082 | canvas-item / constraint | Deutsche Launch-Sprache mit i18n-Vorbereitung | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Tabellenzelle CAN-007. |
| CAN-083 | canvas-item / constraint | Store-Policies sind verbindlich | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Tabellenzelle CAN-007. |
| CAN-084 | canvas-item / constraint | DSGVO ist verbindlich | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Tabellenzelle CAN-007. |
| CAN-085 | canvas-item / constraint | Background-Location erfordert eine belastbare Berechtigungsbegründung | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Tabellenzelle CAN-007. |
| CAN-086 | canvas-item / constraint | Health-Berechtigungen erfordern eine belastbare Berechtigungsbegründung | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Tabellenzelle CAN-007. |
| CAN-087 | canvas-item / constraint | Reale Gerätetests auf iOS und Android pro Gate | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Tabellenzelle CAN-007 + Prosa Punkt 2. |
| CAN-088 | canvas-item / constraint | Zweckbindung und Datenminimierung für Standort- und Health-Daten | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Prosa 'Constraints', Punkt 3. |
| CAN-089 | canvas-item / constraint | Karten-, Routing- und Backendanbieter bleiben ADR-Entscheidungen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Prosa 'Constraints', Punkt 4. |
| CAN-090 | canvas-item / constraint | Der öffentliche Name darf erst nach Markenprüfung finalisiert werden | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Prosa 'Constraints', Punkt 5. |
| CAN-091 | canvas-item / constraint | Externes Routing läuft ab Stufe A0 ausschließlich über einen minimalen serverseitigen Routing-Proxy | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Prosa 'Constraints', bestätigte Nutzerentscheidung 2026-07-19. Quelle: DEC-005 (user-confirmed), CONTRA-002 (resolved). |
| CAN-092 | canvas-item / constraint | Kein Routing-API-Key als EXPO_PUBLIC_*-Variable im App-Bundle; NFR-007 gilt ab A0 | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Prosa 'Constraints', bestätigte Nutzerentscheidung 2026-07-19. EXPO_PUBLIC_* wird ins JS-Bundle inlined und ist aus jedem Build extrahierbar. |
| CAN-093 | canvas-item / constraint | Die Mobile-App kennt nur eine konfigurierbare Proxy-Basis-URL, einen providerneutralen RoutingPort und einen RoutingClient; Providername und Providerantwort dürfen nicht in Domain- oder UI-Code gelangen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Nutzerentscheidung 2026-07-19. Neu aufgenommen aus der Nutzerentscheidung vom 2026-07-19. |
| CAN-094 | canvas-item / constraint | Der Routing-Proxy übersetzt den Sportmodus in das Providerprofil: run → foot-walking, ride → cycling-regular | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Nutzerentscheidung 2026-07-19. Die Profilnamen bleiben damit serverseitig und tauchen nicht in SportConfig-nahem App-Code als Providerbegriff auf. Hinweis: docs/architecture/revyr-target-architecture.md, Abschnitt 6, führt 'routingProfile' derzeit noch in der App-seitigen SportConfig – Klärung durch den Architektur-Owner in Phase 3. |
| CAN-095 | canvas-item / constraint | Local-first-Präzisierung: Aktivitäts-, Health- und Verlaufsdaten bleiben in A0/A1 standardmäßig lokal; für die Routenberechnung dürfen ausschließlich die erforderlichen Wegpunkte transient an einen kontrollierten Routing-Proxy übertragen werden; der Proxy speichert keine Koordinaten oder Routengeometrien dauerhaft | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Nutzerentscheidung 2026-07-19. Wörtliche Nutzerformulierung. Adressiert CONTRA-006 (offen), schließt ihn aber nicht – CONTRA-006 fragt zusätzlich, welche REQ-034-Klauseln (Rate Limits, Logging, Retention, Auftragsverarbeitung, EU-Hosting) ab A0 für den Proxy gelten. |
| CAN-096 | canvas-item / constraint | A0-Laufzeit des Routing-Proxys: AWS Lambda und API Gateway, Region eu-central-1, Provider-Key nur serverseitig, Rate Limit, Timeout und Kill Switch | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Nutzerentscheidung 2026-07-19. NUR DOKUMENTIERT. In diesem Lauf wird nichts davon gebaut, deployt oder als AWS-Ressource angelegt. |
| CAN-097 | canvas-item / constraint | Ablageort des A0-Routing-Proxys im Repository: infra/routing-proxy/ – ausdrücklich nicht backend/ | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Nutzerentscheidung 2026-07-19 (OQ-011). Begründung des Nutzers: begrenzte, austauschbare Infrastrukturkomponente; backend/ bleibt für Stufe B reserviert. |
| CAN-098 | canvas-item / constraint | Der vollständige Backend-Entscheid für Geo, Auth, Realtime und EU-Hosting bleibt offen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, Prosa 'Constraints', letzter Punkt. Verweist auf OQ-005. Der A0-Proxy präjudiziert diesen Entscheid nicht. |
| CAN-099 | canvas-item / CONSTRAINT · VALUE BOUNDARY | Die mobile Anwendung muss für Menschen mit unterschiedlichen visuellen, motorischen und assistiven Anforderungen bedienbar sein. | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-007, nicht im Canvas vorhanden. Inhalt entschieden durch den Nutzer am 2026-07-19; Wortlaut in Runde 4 (2026-07-20) auf den kanonischen Text der Nutzerentscheidung gezogen; **Web-Erstreckung in Runde 6 (2026-07-20) entfernt.** **CAN-099 ist AUSSCHLIESSLICH Accessibility.** **Kanonischer Wortlaut (verbindlich, Fassung Runde 6):** „Die mobile Anwendung muss für Menschen mit unterschiedlichen visuellen, motorischen und assistiven Anforderungen bedienbar sein. Dazu gehören WCAG 2.2 AA, Screenreader-Unterstützung, skalierbare Schrift, ausreichende Bedienflächen, nachvollziehbare Fokusführung und die Regel, dass Farbe niemals der einzige Informationsträger ist." **Item Type CONSTRAINT / VALUE BOUNDARY** · **Source Type EXPLICIT für den belegten Kern** (WCAG-AA-Kontraste, Dynamic Type / Font Scaling, Screenreader-Labels, Farbregel — SRC-001:256, SRC-002:134, SRC-003:100/:101) · `measurement_type` COMPLIANCE_CONTROL. **VIER DETAILS STEHEN AUF `ASSUMPTION`** (Nutzerauftrag Schritt 3, unverändert weitergeführt): die **Fassungsziffer „2.2"** (alle vier WCAG-Treffer nennen „WCAG AA" **ohne** Fassung), **„ausreichende Bedienflächen"**, **„nachvollziehbare Fokusführung"** und die Zielgruppenrahmung **„motorischen und assistiven Anforderungen"** — für jeden dieser Begriffe liefert die Volltextsuche über alle vier Quellen **null Treffer**. **ENTFERNT 2026-07-20: „und ihre nutzbaren Web-Auskopplungen".** Grund ist **fehlende Deckung, ausdrücklich kein Widerspruch**: SRC-003 §2.4 — der einzige Accessibility-Abschnitt aller vier Quellen — nennt Web nicht und schließt mit einer reinen iOS/Android-Zeile; die vier „Web-Auskopplung"-Treffer (alle in SRC-003) betreffen ausschließlich die CSS-Farbmischregel. Die Kette „Farbregel gilt für Web, also auch Accessibility" ist ein Zwischenglied. **GEGENPRÜFUNGSEINWAND, sichtbar abgebildet:** die Begründung „widerspricht der Quelle in der Richtung" ist **falsch** und wird hier nicht geführt — SRC-001:132 nimmt den Beschützer-Link vom Nicht-Ziel ausdrücklich **aus** („kein Web-Client (außer Beschützer-Link)"), SRC-001:238 und SRC-003:605 planen ihn als L-03 / Task 13.4 ein, SRC-003:83 benennt drei Web-Artefakte namentlich. Die Quellen **bejahen** die Existenz des Prüfgegenstands. **DER SCHNITT IST NUR SYNCHRON GÜLTIG:** dieselbe Erstreckung steht in `prd.md` (REQ-037-Text, AC-037 Given, NFR-005 `signal`), in `docs/EVIDENCE-LEDGER.md` (EV-037-Kopf) und in `docs/traceability.md` (TRC-037). Bleibt sie dort stehen, trägt REQ-037 eine Geltungsbereichsklausel **ohne Canvas-Anker** — die Fehlerklasse von §8 Punkt 41. Nachzugsaufträge in §7.6.2. **Materiell zu beachten:** die unbelegte Fassungsziffer „2.2" ist **nicht** folgenlos — sie steht in der Pass-Spalte von AC-037 und in EV-037 [ACC1] als **store-release-blockierender** Nachweis; die gegenteilige Aussage im PRD („stehen nicht in AC-037 … heute folgenlos") ist widerlegt (§8 Punkt 48). **Release-Gates:** Accessibility-Basis ab **A0**, vollständiger Audit spätestens **A2**. **Farbregel (Runde-4-Entscheidung, §6.3.3):** die Klausel „Farbe ist niemals der einzige Informationsträger" wird **kanonisch hier** geführt — sie ist eine Wahrnehmbarkeitsschranke, und ihr Ausfall ist ein Zugänglichkeitsdefekt, kein Gestaltungsdefekt. CAN-141 führt sie **nicht** mehr. Hinweis zur Belegdichte: die **generische** Fassung trägt allein SRC-001:256; SRC-003:101 sagt enger „Teamfarben nie einziger Informationsträger". **Präzisierung gegenüber NFR-005:** „WCAG AA" ohne Fassung ist nicht prüfbar; die Fassung ist **2.2** — als ASSUMPTION, siehe oben. Canvas-Nachzug offen (Regel 10, §7.5, §7.6.2). |

#### Risks (11 Items)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-100 | canvas-item / risk | GPS-Drift verfälscht Distanz und Route | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, Tabellenzelle CAN-008 + Prosa 'Risks'. Register: RISK-002. |
| CAN-101 | canvas-item / risk | Batterieverbrauch verhindert längere Nutzung | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, Tabellenzelle CAN-008 + Prosa. Register: RISK-003. |
| CAN-102 | canvas-item / risk | Falsche Health-Claims | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, Tabellenzelle CAN-008 + Prosa. Register: RISK-008. |
| CAN-103 | canvas-item / risk | Namens- und Markenkollision | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, Tabellenzelle CAN-008 + Prosa. Register: RISK-011. |
| CAN-104 | canvas-item / risk | Betrug und Manipulation von Aktivitäten | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, Tabellenzelle CAN-008. Register: RISK-013 (Gegenmaßnahme Anti-Cheat). |
| CAN-105 | canvas-item / risk | Standortmissbrauch | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, Tabellenzelle CAN-008 + Prosa. Register: RISK-015 und RISK-016. |
| CAN-106 | canvas-item / risk | Geo-Komplexität | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, Tabellenzelle CAN-008 + Prosa. Register: RISK-017. |
| CAN-107 | canvas-item / risk | OSM-Qualität | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, Tabellenzelle CAN-008. Register: RISK-018. |
| CAN-108 | canvas-item / risk | Store-Ablehnung | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, Tabellenzelle CAN-008 + Prosa. Register: RISK-010. |
| CAN-109 | canvas-item / risk | Anti-Cheat-Fehler (False Positives gegen reale Nutzer) | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, nur Prosa 'Risks'. Register: RISK-013. Eigenes Atom, weil es die Gegenrichtung zu CAN-104 ist: CAN-104 ist Betrug, CAN-109 ist die Fehlbeschuldigung. — **HERABGESTUFT 2026-07-20 (Runde 6) auf `ASSUMPTION`, Nutzerauftrag Schritt 2. Der Wortlaut bleibt unverändert; herabgestuft wird der Source Type, nicht die Aussage.** Der Canvas führt `EXPLICIT \| SRC-003`; keine der vier Quellen behauptet, dass die Anti-Cheat-Klassifikation **irren** kann. Wortnah gedeckt ist in SRC-003:265 und :559 allein eine **Urteilsregel** („fehlende Sensoren allein sind kein Betrug, senken aber die Beweiskraft" / „fehlende Sensoren allein ≠ Betrug") — eine Regel, **wie** geurteilt werden darf, ist kein Risiko, **dass** falsch geurteilt wird; SRC-003:265 nennt als Rechtsfolge fehlender Sensoren ausdrücklich die gesenkte Beweiskraft und gerade **nicht** `verified=false`. Das Risikoregister von SRC-003 (24 Zeilen) hat **keine** Zeile zur Anti-Cheat-Fehlklassifikation: Nr. 8 ist die Gegenrichtung (= CAN-104), Nr. 12 betrifft Fehlalarme der **Sturzerkennung**, Nr. 19 Schummeln, Nr. 22 den Datenschutz der Sensor-Plausibilität. Volltextsuche nach „False Positive", „fälschlich", „zu Unrecht", „beschuldig", „Einspruch", „Appeal", „Confidence": **null Treffer** im Anti-Cheat-Kontext; „Fehlalarm" nur bei der Sturzerkennung. SRC-004 trägt nichts bei. **RISK-013 kann CAN-109 nicht stützen** — es ist selbst Teil dieses Artefaktsatzes, und seine Gegenmaßnahmen (mehrstufige Confidence, Review, Appeal-Flow) kommen in **keiner** Quelle vor (Zirkelbeleg). **Kein Verengen möglich:** der einzige wortnah gedeckte Nachbarinhalt ist die Klassifikationsregel; CAN-109 darauf zu verengen wäre die Umdeutung eines Risiko-Atoms in ein Regel-Atom. **ZWEI BEFUNDSPUNKTE AUSDRÜCKLICH ZURÜCKGEWIESEN — die Herkunft bleibt unverändert:** (1) Die Angabe „nur Prosa 'Risks'" ist **korrekt und am 2026-07-20 verifiziert**: der Ursprungstext des Canvas führt einen Prosa-Abschnitt „## Risks", der „**Anti-Cheat-Fehler**" wörtlich nennt; CAN-008 ist als Sammelblock „Canvas-Abschnitt Risks" mit Zerlegung in CAN-100…CAN-110 in §6.2 belegt. Die Behauptung, dieser Prosakörper existiere nicht, beruht auf der Atom-Tabelle statt auf dem Ursprungstext. (2) Der Vorschlag, die Herkunft durch „keine Quellenzeile" zu ersetzen, hätte damit eine **belegte** Tatsache gelöscht und CAN-109 als einziges der elf Geschwisteratome ohne Abstammung zurückgelassen. **Zu unterscheiden bleibt:** die Prosa belegt die **Dekompositionsherkunft**, nicht die **Quellendeckung** — der Ursprungstext ist der Canvas selbst und keine der vier `SRC-`Quellen. Genau deshalb fällt der Source Type und nicht die Herkunft. **NICHT MIT ABGESTUFT:** AC-024 („Fehlende Sensoren allein führen nicht zur Betrugsannahme") ist die Urteilsregel und bleibt quellengedeckt und unberührt. **PRÜFBEDARF, in diesem Lauf nicht ausgeführt:** CAN-110 trägt dieselbe Annotation und dieselbe Lage (§8 Punkt 50). Siehe §7.6 und §8 Punkt 47. |
| CAN-110 | canvas-item / risk | Private oder gesperrte Sportanlagen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-008, nur Prosa 'Risks'. Register: RISK-018. |

#### Evidence-Annahmen (13 Items)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-111 | canvas-item / evidence-assumption | Unit- und Property-Tests der Domainlogik | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Tabellenzelle CAN-010 + Prosa 'Evidence'. |
| CAN-112 | canvas-item / evidence-assumption | Integrationstests | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Tabellenzelle CAN-010. |
| CAN-113 | canvas-item / evidence-assumption | Referenzstrecken | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Tabellenzelle CAN-010 + Prosa. |
| CAN-114 | canvas-item / evidence-assumption | Reale Run- und Bike-Gerätetests je Plattform | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Prosa 'Evidence'. Run und Bike werden getrennt nachgewiesen. |
| CAN-115 | canvas-item / evidence-assumption | App-Kill- und Background-Tests | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Tabellenzelle CAN-010 + Prosa. |
| CAN-116 | canvas-item / evidence-assumption | Batterietests | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Tabellenzelle CAN-010 + Prosa. |
| CAN-117 | canvas-item / evidence-assumption | Health-Gerätetests | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Tabellenzelle CAN-010. |
| CAN-118 | canvas-item / evidence-assumption | Claims-Review | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Prosa 'Evidence'. |
| CAN-119 | canvas-item / evidence-assumption | Privacy-Matrix und Privacy-Review | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Tabellenzelle CAN-010 + Prosa. — **HERABGESTUFT 2026-07-20 (Runde 6) auf `ASSUMPTION`, Nutzerauftrag Schritt 2. Der Titel bleibt unverändert.** Der Canvas führt `EXPLICIT \| SRC-003`. Das Item bündelt **zwei verschiedene Gegenstände**, von denen keiner den Titel in seiner jetzigen Fassung trägt. **(a) „Privacy-Matrix":** die Zeichenfolge kommt in **keiner** der vier Quellen vor (0 Treffer). Das Artefakt heißt dort ausnahmslos **„Sichtbarkeits-Matrix"** (SRC-003:363, :522, :683; SRC-001:192); um von dort auf „Privacy-" zu kommen, braucht es die Gleichsetzung „Sichtbarkeitsstufen sind Privacy-Einstellungen", die keine Quelle vornimmt. **Der Gegenstand selbst ist real, wortnah belegt und gate-verankert** (SRC-003:522 „Matrix als Testtabelle, jede Zeile geprüft"; SRC-003:683 GATE B) — er wird im Repository aber bereits **quellentreu und verlinkt** als **EV-018 „Sichtbarkeits-Matrix"** geführt. Durch die Herabstufung geht daher **kein belegter Inhalt verloren**; es entfällt nur ein zweiter, abweichend benannter Träger desselben Objekts. **(b) „Privacy-Review":** „Privacy-Review", „Privacy Review", „Datenschutz-Review", „Datenschutzprüfung" — 0 Treffer; das Wort „Datenschutz" kommt in keiner der vier Quellen **überhaupt** vor. **GEGENPRÜFUNGSEINWAND, sichtbar abgebildet:** eine Absolutaussage „gar nicht getragen" wäre **zu weit**. Datenschutzrechtliche **Einzelprüfungen je sensibler Datenklasse** sind belegt — SRC-003:629 („17.4 Zyklus-bewusst … eigene Privacy-Prüfung", Stufe v5.0/GATE E) und SRC-003:715 („DSGVO-Prüfung in 10.2" für serverseitige Gesundheitsdaten, Stufe C); privacy-bezogene **Abnahmen** existieren zudem als Store-Compliance (SRC-003:643, Stufe A). **Nicht belegt ist allein die Verallgemeinerung** zu einem querschnittlichen, gate-blockierenden Abnahmevorgang „je Funktionsgruppe" — und genau diese Verallgemeinerung ist im Repository zu fünf harten Gate- und Abnahmepflichten ausgebaut (AC-033-Vorbedingung, blockierender Ledger-Nachweis, Gate-D- und Gate-E-Bedingung, Gegenmaßnahme eines `critical`-Risikos). **HERKUNFT: der Befundpunkt „Tabellenzelle ist unzutreffend" wird zurückgewiesen, die Angabe bleibt unverändert** — die Spalte bezeichnet die canvas-interne Dekompositionsherkunft aus dem Sammelblock CAN-010 („Canvas-Abschnitt Evidence", §6.2), **nicht** eine Fundstelle in SRC-003. Am 2026-07-20 verifiziert: der Ursprungstext führt unter „## Evidence" den Punkt „**Claims-, Privacy- und Threat-Model-Reviews.**" — daraus stammen CAN-118, CAN-119 und CAN-120. **Damit ist die Aufteilungsrichtung geklärt und zugleich strittig:** der **Review**-Teil hat echte Canvas-Lineage, der **Matrix**-Teil hat im überlieferten Ursprungstext **keine**; welcher der beiden die ID behält, ist eine **Nutzerentscheidung** und wird hier **nicht** vorweggenommen (kein Umdeuten, keine neue ID). **KEIN HALB VOLLZOGENER ABSTIEG:** das Typfeld `canvas-item / evidence-assumption` ist die **Abschnittsklassifikation** und wird von allen dreizehn Items CAN-111…CAN-123 geteilt; es ist **kein** Source-Type-Vermerk und darf nicht als solcher gelesen werden. **PRÜFBEDARF, in diesem Lauf nicht ausgeführt:** CAN-118 („Claims-Review") und CAN-120 („Threat-Model-Review") tragen dieselbe quellenlose „-Review"-Prägung; belegt sind in den Quellen nur die Grundbegriffe (SRC-003:686 „Claims juristisch freigegeben", SRC-003:602 „Threat-Model Standortfreigabe"). Ohne ihre Prüfung bleibt die Bereinigung von CAN-119 wirkungslos (§8 Punkt 50). Siehe §7.6 und §8 Punkte 45, 50. |
| CAN-120 | canvas-item / evidence-assumption | Threat-Model-Review | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Prosa 'Evidence'. |
| CAN-121 | canvas-item / evidence-assumption | Simulationen für Effort, Territory und Rewards | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Tabellenzelle CAN-010 + Prosa. |
| CAN-122 | canvas-item / evidence-assumption | Store-Testtracks | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Tabellenzelle CAN-010 + Prosa. |
| CAN-123 | canvas-item / evidence-assumption | Evidence Ledger | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-010, Tabellenzelle CAN-010 + Prosa. Datei: docs/EVIDENCE-LEDGER.md. |

#### Success Signals (7 Items)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-124 | canvas-item / success-signal | W4-Retention aktiver Tracker-Nutzer | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-009, Tabellenzelle CAN-009 ('hält Nutzer nach vier Wochen'). Ersetzt Facette CAN-009-a. Zielwert steht in VIS-006 Zeile A: > 30 %. Der Canvas selbst nennt keinen Zielwert (MISSING im Canvas, vorhanden in der Vision). |
| CAN-125 | canvas-item / success-signal | Quote der Stimmungs-Check-ins nach einer Aktivität | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-009, Tabellenzelle CAN-009 ('Health-Erklärungen werden genutzt'). Teil-Ersatz für Facette CAN-009-b. Zielwert VIS-006 Zeile A: > 50 %. CAN-009-b bündelte zwei unterschiedlich messbare Signale in einer Aussage – daher zwei Atome (CAN-125, CAN-126). |
| CAN-126 | canvas-item / success-signal | Öffnungsrate der Score-Erklärung ('Warum'-Aufrufe) | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-009, Tabellenzelle CAN-009 ('Health-Erklärungen werden genutzt'). Teil-Ersatz für Facette CAN-009-b. Zielwert VIS-006 Zeile A: > 25 %. |
| CAN-127 | canvas-item / success-signal | Anteil Nutzer in einem Team nach 60 Tagen | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-009, Tabellenzelle CAN-009 ('spätere Community-Systeme erhöhen reale gemeinsame Aktivitäten'). Teil-Ersatz für Facette CAN-009-c. Zielwert VIS-006 Zeile C: > 25 %. CAN-009-c bündelte drei Signale. |
| CAN-128 | canvas-item / success-signal | Anteil Teams mit realer gemeinsamer Aktivität pro Woche | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-009, Tabellenzelle CAN-009. Teil-Ersatz für Facette CAN-009-c. Zielwert VIS-006 Zeile C: > 40 %. |
| CAN-129 | canvas-item / success-signal | Season-Teilnahme aktiver Teams | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-009, Tabellenzelle CAN-009. Teil-Ersatz für Facette CAN-009-c. Zielwert VIS-006 Zeile D: > 60 %. |
| CAN-130 | canvas-item / success-signal | Bestätigte Routenübernahmen je auswertbarer Routenempfehlung, getrennt für Run und Bike | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-009, nicht im Canvas vorhanden. **Inhalt entschieden durch den Nutzer am 2026-07-19** (Auftau-Schritt 2); Status daher von `reserved` auf `active`. Vollständige Spezifikation in **§6.3.2** — sie ist zu umfangreich für diese Zelle und wird dort **nicht gekürzt**, weil Nenner-Definition und Ausschlussregeln der eigentliche Inhalt der Entscheidung sind. Kurzfassung: `measurement_type` PRODUCT_OUTCOME · `source_type` EXPLICIT · `evidence_status` **planned** · `empirical_result` **MISSING** · `release_gate` **B** · Messfenster **rollierende 28 Tage** · Zielwert **> 1,0** bestätigte Routenübernahmen je auswertbarer Empfehlung. Trägt REQ-019 / AC-041. Canvas-Nachzug offen (Regel 10, §7.4). |

#### 6.3.2 CAN-130 — vollständige Spezifikation (Nutzerentscheidung 2026-07-19)

**Aussage.** „Eine veröffentlichte und für mindestens einen berechtigten Empfänger sichtbare
Routenempfehlung führt im Durchschnitt zu mehr als einer tatsächlichen Routenübernahme. Run und
Bike werden getrennt ausgewertet."

| Feld | Wert |
|---|---|
| `measurement_type` | PRODUCT_OUTCOME |
| `source_type` / `target_source_type` | EXPLICIT |
| `evidence_status` | **planned** — Metrik, Berechnung und Gate sind definiert, die Instrumentierung fehlt (§3.2). Es existiert kein Code. |
| `empirical_result` | **MISSING** |
| `release_gate` | **B** |
| `measurement_window` | rollierende 28 Tage |
| `target_or_pass_condition` | **> 1,0** bestätigte Routenübernahmen je auswertbarer Empfehlung |

**Kennzahl** = bestätigte Routenübernahmen / auswertbare Routenempfehlungen.

**„Auswertbar" nur wenn** die Empfehlung: erfolgreich veröffentlicht wurde; mindestens einen
berechtigten Empfänger hatte; im Messfenster sichtbar sein konnte; **nicht** vor möglicher
Ausspielung gelöscht, blockiert oder moderativ verborgen wurde.

**Nicht in den Nenner:** private Empfehlungen ohne berechtigten Empfänger · technisch nicht
ausgelieferte Empfehlungen · vor Ausspielung gelöschte Empfehlungen · durch Blockierung oder
Moderation vollständig unsichtbare Empfehlungen · Test- und Seed-Daten.

**Mehrere Nutzer dürfen dieselbe Empfehlung übernehmen** — der Durchschnitt kann daher
> 1,0 sein. Das ist kein Rechenfehler, sondern die Absicht der Kennzahl.

**Getrennt auszuweisen:** `run_route_adoptions_per_recommendation` und
`bike_route_adoptions_per_recommendation`. Ein Gesamtwert darf gezeigt werden, aber **nie
anstelle** der getrennten Sportwerte.

**Guardrail-Signale:** Anzahl auswertbarer Empfehlungen · Empfehlungen ohne berechtigten
Empfänger · technisch fehlgeschlagene Ausspielungen · mediane Zahl berechtigter Empfänger je
Empfehlung · Anteil Empfehlungen mit mindestens einer Übernahme · Übernahmen je 100 berechtigten
Ausspielungen (sofern datenschutzkonform messbar) · Run/Bike-Verteilung · Lösch-, Blockierungs-
und Moderationsanteil.

**Datenschutzbedingt unsichtbare Empfehlungen werden SEPARAT ausgewiesen, NICHT als Gegenprobe in
den Nenner.** Begründung der Nutzerentscheidung: sonst wird fehlender *Zugang* fälschlich als
mangelndes *Nutzerinteresse* gelesen. Das ist keine Feinheit — es ist der Unterschied zwischen
„die Funktion überzeugt nicht" und „die Funktion war nie sichtbar".

**Telemetrie (privacy-minimiert).** Zulässige Ereignisse: `route_recommendation_published` ·
`route_recommendation_eligible` · `route_recommendation_exposed` · `route_adopted` ·
`route_recommendation_deleted` · `route_recommendation_hidden`. Zulässige Felder: pseudonyme
`recommendation_id` · pseudonyme `adoption_id` · `sport` (`run`|`ride`) ·
Sichtbarkeitskategorie · grober Zeitstempel bzw. Zeitbucket · Ergebnisstatus · Event-Version.
**Nicht zulässig:** GPS-Koordinaten · Routengeometrie · Start-/Zieladresse · Health-Daten ·
Klarnamen · E-Mail · vollständige Gerätekennungen · öffentliche Analytics-Profile ·
Werbe-/Cross-Service-Tracking. **Kein paralleler Standort- oder Verhaltenstracker**; die Kennzahl
ist möglichst aus ohnehin nötigen Backend-Ereignissen zu aggregieren.

**Local-first-Abgrenzung.** A0/A1: Aktivitäts-, Health- und Verlaufsdaten bleiben standardmäßig
lokal. Ab B dürfen für die **ausdrücklich aktivierte** Social-/Empfehlungsfunktion minimierte
Metadaten verarbeitet werden. **Rohroute und GPS-Geometrie NIE für die Erfolgsmessung.** Gemessen
wird das Ereignis „Empfehlung übernommen", **nicht** die später gelaufene oder gefahrene Strecke.

**Stichprobenregel — vor endgültiger Bewertung zu definieren** (OQ-014): Mindestzahl auswertbarer
Empfehlungen · Mindestzahl berechtigter Empfänger · Mindestdauer des Messfensters · Behandlung
von Testkonten · Umgang mit Mehrfachübernahmen desselben Nutzers · Umgang mit gelöschten und
moderierten Empfehlungen · getrennte Run-/Bike-Auswertung. Bis dahin gilt: `target_source_type`
EXPLICIT, `evidence_status` planned, `empirical_result` MISSING. **Es wird keine Mindestzahl
geraten.**

#### Allowed Scope je Release-Stufe (7 Items)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CAN-131 | canvas-item / allowed-scope | Stufe A0: robustes Tracking, Planung, Verlauf, Persistenz und Designbasis; nicht erlaubt vor Gate: Health-Behauptungen, Social, Territory | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile A0. OPEN QUESTION: Die Zeile beschreibt A0 als lokale Stufe, während der bestätigte A0-Routing-Proxy (CAN-091, CAN-096) serverseitig Wegpunkte verarbeitet. CONTRA-006 ist dazu offen; CAN-095 präzisiert local-first, löst den Widerspruch aber nicht vollständig. |
| CAN-132 | canvas-item / allowed-scope | Stufe A1: Health-Basis und erklärbarer Score; nicht erlaubt vor Gate: Community- und Wettbewerbssysteme | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile A1. |
| CAN-133 | canvas-item / allowed-scope | Stufe A2 / v1.0: Rückblicke, Export, Avatarbasis, Widgets und Store-Release; nicht erlaubt vor Gate: Accounts und öffentlicher UGC | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile A2. |
| CAN-134 | canvas-item / allowed-scope | Stufe B / v2: Accounts, Profile, Empfehlungen, Feed und Moderation; nicht erlaubt vor Gate: Teams/Territory ohne Anti-Cheat | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile B. |
| CAN-135 | canvas-item / allowed-scope | Stufe C / v3: Teams, Rankings, Challenges und Anti-Cheat; nicht erlaubt vor Gate: Territory/Live ohne Simulation und Threat-Model | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile C. |
| CAN-136 | canvas-item / allowed-scope | Stufe D / v4: Territory, Seasons, Events und Live-Safety; nicht erlaubt vor Gate: Coach-/Recovery-Claims ohne Freigabe | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile D. |
| CAN-137 | canvas-item / allowed-scope | Stufe E / v5: Wearables, Coach, Recovery, Wetter und Zyklus; nicht erlaubt: nicht freigegebene medizinische Claims | `docs/canvas/revyr-endurance-platform.canvas.md` | active | 2026-07-19 | — | — | Herkunft: CAN-011, Prosa-Tabelle 'Allowed Scope', Zeile E. |

### 6.4 REQ — Requirements

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| REQ-001 | requirement | Sportmodus als zentrale Konfiguration | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0, Source Type EXPLICIT. |
| REQ-002 | requirement | Foreground-Tracking | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0, Source Type EXPLICIT. |
| REQ-003 | requirement | Background, Pause und Recovery | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0, Source Type EXPLICIT. |
| REQ-004 | requirement | Erweitertes GPS-Datenmodell und Filter | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0, Source Type ASSUMPTION. |
| REQ-005 | requirement | Robuste lokale Aktivitätsspeicherung | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0, Source Type ASSUMPTION. |
| REQ-006 | requirement | Routenplanung | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0, Source Type EXPLICIT. |
| REQ-007 | requirement | Routenbezogener Fortschritt | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0, Source Type ASSUMPTION. — **BESTÄTIGT 2026-07-20 (Runde 6), Nutzerauftrag Schritt 4: REQ-007 bleibt inhaltlich vollständig als route-aware Verbesserung erhalten und steht bis zur ausdrücklichen Nutzerbestätigung auf `ASSUMPTION`. Der Wortlaut wird nicht verengt, nicht abgeschwächt und nicht gelöscht.** Der Status ist aus einem **stärkeren** Grund als „unbelegt" richtig: die einzige Quelle, die den Rechenweg überhaupt festlegt, spezifiziert wörtlich das **Gegenteil** — SRC-004:416-418 `return Math.max(0, plannedMeters - coveredMeters);`, getestet in SRC-004:382 („subtracts covered from planned") und im Tracking-Screen gegen die zurückgelegte Gesamtdistanz verdrahtet. SRC-001, SRC-002 und SRC-003 sagen zum Rechenweg **nichts**; „routebezogen", „Projektion", „monoton", „Korridor", „Hysterese", „falsche Richtung" und „Richtungsumkehr" haben in allen vier Quellen **null Treffer**. REQ-007 ist damit eine **bewusste Abweichung von SRC-004**, kein Ableitungsfehler. Ihr alleiniger Träger ist SRC-005/DEC-004, und beide tragen schwächer als die Formulierung nahelegt: **DEC-004 steht auf `proposed`**, nicht `user-confirmed`, und **SRC-005 ist laut `docs/SOURCE-MAP.md` ein `consistency-review`**, also ein interner Befundsatz und **keine Nutzerquelle**. Genau das rechtfertigt `ASSUMPTION` bis zur Nutzerbestätigung. **KEIN SOURCE-TYPE-WIDERSPRUCH — Gegenprüfungseinwand übernommen, gegenteiliger Befundpunkt zurückgewiesen:** dass `docs/prd/…prd.md` und `docs/traceability.md` für REQ-007 an anderer Stelle **`MISSING`** führen, ist **kein** Widerspruch zu dieser Zeile, sondern eine **andere Achse**. Das PRD definiert `source_type` im Messmodell als Herkunft des **Zielwerts / der Pass-Bedingung** und führt für die Anforderungsebene eigens `requirement_source_type`; die Traceability schreibt ausdrücklich „gilt dort für den **Zielwert**, nicht für die Anforderung" und überschreibt die Liste als „**MISSING-Schwellen (13)**". Der Grund für `MISSING` ist wörtlich benannt: „Der entscheidende Zielwert (Korridorbreite und Latenz) fehlt in allen Artefakten." **Diese `MISSING`-Werte sind KORREKT und dürfen NICHT auf `ASSUMPTION` harmonisiert werden** — das wäre die Behauptung, für Korridor, Hysterese und Latenz existiere eine Quelle, und damit eine Hochstufung eines zutreffenden Abwesenheitsbefundes. Verbleibender Defekt ist allein die **Feldbenennung** (`source_type` statt `target_source_type` in den Messblöcken), §8 Punkt 49. **AC-007 und EV-007** stehen bereits auf `ASSUMPTION` und erben den Status; sie bleiben unverändert. **`docs/EVIDENCE-LEDGER.md` enthält zu REQ-007/EV-007 keinen Eintrag** — Abwesenheitsbefund, am 2026-07-20 geprüft. **TRC-007 bleibt `broken`**; diese Prüfung rehabilitiert VIS-003 nicht. Siehe §7.6 und §8 Punkte 45, 49. |
| REQ-008 | requirement | Verlauf und Detailansicht | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0. **VERENGT im Auftau-Schritt 2 (2026-07-19), nicht deprecated** — es bleibt dieselbe Anforderung, ihr Umfang wird auf ihren atomaren Kern reduziert. **Entfernt:** GPX-Export (→ REQ-039) und Streckenvergleich (→ REQ-040). **Verbleibt:** Verlauf und Detailansicht. Alttitel: „Verlauf, Wiederverwendung und Export"; Alttext (`prd.md:119`): „Abgeschlossene Aktivitäten MÜSSEN in Verlauf und Detailansicht verfügbar sein; gespeicherte Routen, Streckenvergleich und GPX-Export werden unterstützt." Canvas-Anker neu: **CAN-138** (statt des deprecateten CAN-071). **Source Type ASSUMPTION**, solange der Wortlaut nicht ausdrücklich nutzerbestätigt ist — das PRD führte `EXPLICIT` über SRC-001/SRC-003, die laut `docs/SOURCE-MAP.md` **nicht auffindbar** sind. **Acceptance Criteria müssen Run und Bike GETRENNT prüfen**, siehe AC-008. PRD-Nachzug (Titel und Text) macht Phase 2/3, nicht diese Registry. |
| REQ-009 | requirement | Herzfrequenzquellen | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A1, Source Type EXPLICIT. |
| REQ-010 | requirement | Erklärbarer Belastungs-Score mit Confidence | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A1, Source Type ASSUMPTION. |
| REQ-011 | requirement | HF-Zonen und optionale Ansage | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Should, Release A1, Source Type EXPLICIT. |
| REQ-012 | requirement | Stimmungs-Check-in und Korrelation | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Should, Release A1, Source Type EXPLICIT. |
| REQ-013 | requirement | Health-Home und Steigerungshinweis | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A1, Source Type EXPLICIT. |
| REQ-014 | requirement | Designsystem und Accessibility | `docs/prd/revyr-endurance-platform.prd.md` | **deprecated** | 2026-07-18 | 2026-07-19 | REQ-037, REQ-038 | **Deprecated im Auftau-Schritt 2 (2026-07-19).** Grund (Nutzerentscheidung): REQ-014 ist ein **Composite** aus zwei unabhängig prüfbaren Anforderungen — Zugänglichkeit (WCAG, Screenreader, Dynamic Type) und Gestaltungssprache (tokenbasiert, monochrom, Farbe nur mit fachlicher Bedeutung). Sie haben **verschiedene Prüfverfahren, verschiedene Nachweise und verschiedene Gates** und können unabhängig voneinander bestehen oder fallen. **Die Composite-Requirement wird ausdrücklich NICHT umgedeutet** — kein stilles Verengen auf eine der beiden Hälften. Ersetzt durch REQ-037 (Accessibility) und REQ-038 (Monochromes Designsystem), je mit eigener AC- und EV-ID. Migrationstabelle: §7.4. Folge: AC-014, EV-014 und TRC-014 sind ebenfalls deprecated. Neue Referenzen auf REQ-014 sind ein Validierungsfehler. |
| REQ-015 | requirement | Verdiente Avatar-Progression | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Should, Release A2-B-C, Source Type EXPLICIT. |
| REQ-016 | requirement | Recaps, Erfolgskarten und Live-Status | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Should, Release A2, Source Type EXPLICIT. |
| REQ-017 | requirement | Accounts, Auth und Datenmigration | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release B, Source Type EXPLICIT. |
| REQ-018 | requirement | Privacy, Sichtbarkeit und Moderation | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release B, Source Type EXPLICIT. |
| REQ-019 | requirement | Routenempfehlungen und Feed | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Should, Release B, Source Type EXPLICIT. |
| REQ-020 | requirement | Teamgründung und Beitritt | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release C, Source Type EXPLICIT. |
| REQ-021 | requirement | Aktive Mitglieder und Teamwachstum | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release C, Source Type EXPLICIT. |
| REQ-022 | requirement | Gemeinsame Aktivitäten und Events | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release C-D, Source Type EXPLICIT. |
| REQ-023 | requirement | Effort-Normalisierung | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release C, Source Type EXPLICIT. |
| REQ-024 | requirement | Anti-Cheat mit Confidence-Stufen | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release C, Source Type ASSUMPTION. |
| REQ-025 | requirement | Challenges, Rankings und idempotente Rewards | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release C, Source Type EXPLICIT. |
| REQ-026 | requirement | Team-Territory | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release D, Source Type EXPLICIT. |
| REQ-027 | requirement | Seasons und nach Finalisierung fachlich unveränderbare Historie | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release D, Source Type EXPLICIT. **Titel nachgezogen im Auftau-Schritt 2026-07-19.** Alttitel: „Seasons und unveränderliche Historie". Der Alttitel enthielt die durch **DEC-012 / CONTRA-005** projektweit ersetzte Formulierung „unveränderliche Historie". Der neue Titel ist **wörtlich** aus der `canonical_file` übernommen (`docs/prd/…prd.md:138`) — die Registry formuliert nicht selbst (§3, Feld `title`). Keine Umnummerierung, keine Bedeutungsänderung: dieselbe Anforderung, korrigierte Sprachregelung. |
| REQ-028 | requirement | Deterministische Einzel-Reviere | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release D, Source Type ASSUMPTION. |
| REQ-029 | requirement | Sportplatz-Challenges und Bahngold-Score | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Should, Release D, Source Type ASSUMPTION. |
| REQ-030 | requirement | Live-Map und Beschützer-Modus | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release D, Source Type EXPLICIT. |
| REQ-031 | requirement | Sturzerkennung als Assistenz | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Should, Release D, Source Type EXPLICIT. |
| REQ-032 | requirement | Wearables und Bike-Sensorik | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Should, Release E, Source Type EXPLICIT. |
| REQ-033 | requirement | Coach, Recovery, Wetter und Zyklus unter Claims-Gate | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Should, Release E, Source Type EXPLICIT. |
| REQ-034 | requirement | Security, Datenschutz und Datenminimierung | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0-E, Source Type EXPLICIT. |
| REQ-035 | requirement | Evidence Ledger und Definition of Done | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0-E, Source Type EXPLICIT. |
| REQ-036 | requirement | Store- und Release-Gates | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Priority Must, Release A0-E, Source Type EXPLICIT. |
| REQ-037 | requirement | Accessibility | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu im Auftau-Schritt 2 (2026-07-19); Nachfolger 1 von 2 für REQ-014.** Aussage: „Die mobile Anwendung und alle nutzbaren Web-Auskopplungen erfüllen WCAG 2.2 AA. Schriftgrößen, Screenreader, Fokusführung, Kontraste und Bedienflächen werden auf iOS und Android nachgewiesen. Farbe ist niemals der einzige Informationsträger." Item Type **CONSTRAINT / COMPLIANCE_CONTROL** · `measurement_type` COMPLIANCE_CONTROL. Priority Must. **Release-Gates: Accessibility-Basis ab A0, vollständiger Audit spätestens A2** vor öffentlichem Store-Release. Anker: VIS-011 (ASSUMPTION, unbestätigt — zählt nach §8 Punkt 15 **nicht** als erfüllter Vision-Anker), CAN-099, NFR-005. AC-037, EV-037, TRC-037. Source Type **ASSUMPTION** bis Nutzerbestätigung des Wortlauts; das PRD führte REQ-014 als EXPLICIT über SRC-003, das **nicht auffindbar** ist. |
| REQ-038 | requirement | Monochromes tokenbasiertes Designsystem | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu im Auftau-Schritt 2 (2026-07-19); Nachfolger 2 von 2 für REQ-014.** Aussage: „Die Anwendung verwendet ein tokenbasiertes, überwiegend monochromes Designsystem. Farbe wird nur dort eingesetzt, wo sie eine fachliche Bedeutung besitzt: Health-Status, Team- und Revieridentität, Sportplatz-Gold sowie bestätigte Feiermomente. Run und Bike werden nicht ausschließlich durch Farbe unterschieden." Priority Must, Release A0-A2. **Source Type EXPLICIT** — bereits festgelegtes Designprinzip (ausdrückliche Nutzerangabe 2026-07-19). Canvas-Anker: **CAN-141**. AC-038, EV-038, TRC-038. **Vision-Anker: VIS-012 = reserved, Inhalt MISSING → BLOCKER.** Kein bestehendes VIS-Item trägt diese Aussage; es wird ausdrücklich **keines umgedeutet**. |
| REQ-039 | requirement | GPX-Export abgeschlossener Aktivitäten | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu im Auftau-Schritt 2 (2026-07-19).** Aussage: „Nutzer können eine abgeschlossene Run- oder Bike-Aktivität als standardkonforme GPX-Datei exportieren und in einer kompatiblen Fremdanwendung öffnen." Priority Must, **Release A2**, spätestens vor öffentlichem v1.0-Release. `measurement_type` OPERATIONAL_QUALITY (bzw. FUNCTIONAL CONTROL im bestehenden Modell). Canvas-Anker **CAN-139**; AC-039, EV-039, TRC-039. **Warum eine eigene REQ-ID:** die Nutzerentscheidung stellt ausdrücklich fest, dass **REQ-034 KEIN ausreichend präziser primärer Anker** ist — die Erwähnung „Datenexport" trägt die konkrete Capability „GPX-Datei erzeugen und extern öffnen" nicht. REQ-034 bleibt **sekundäre Constraint-Verknüpfung** (Nutzerkontrolle, Datenportabilität, Datenminimierung, keine unbeabsichtigten Zusatzdaten). Es wird ausdrücklich **nicht** behauptet, REQ-034 allein erfülle den GPX-Export. **Vision-Anker: VIS-013 = reserved, Inhalt MISSING → BLOCKER.** Source Type ASSUMPTION bis Nutzerbestätigung. |
| REQ-040 | requirement | Streckenwiederverwendung und Aktivitätsvergleich | `docs/prd/revyr-endurance-platform.prd.md` | **deprecated** | 2026-07-19 | 2026-07-20 | REQ-041, REQ-042 | **Deprecated in Runde 4 (2026-07-20).** Grund: REQ-040 ist — wie zuvor REQ-014 — ein **Composite** aus zwei unabhängig prüfbaren Anforderungen: der **Wiederverwendung** einer gespeicherten Route (Planung) und dem **Vergleich** abgeschlossener Aktivitäten (Auswertung). Sie können unabhängig bestehen oder scheitern, brauchen getrennte Acceptance Criteria und sind unterschiedlich blockiert: die Wiederverwendung ist vollständig spezifizierbar, der Vergleich ist ohne **OQ-015** nicht spezifizierbar. **Die Composite-Requirement wird ausdrücklich NICHT auf eine Hälfte verengt.** Ersetzt durch **REQ-041** (Wiederverwendung) und **REQ-042** (Vergleich), je mit eigener AC-, EV- und TRC-ID. Folge-Deprecations: AC-040, EV-040, TRC-040. Neue Referenzen auf REQ-040 sind ein Validierungsfehler. Migration: §7.5. |
| REQ-041 | requirement | Wiederverwendung einer gespeicherten Route | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-20 | — | — | **Neu in Runde 4 (2026-07-20); Nachfolger 1 von 2 für REQ-040.** Aussage: „Nutzer können eine gespeicherte Route erneut als Grundlage einer geplanten Run- oder Bike-Aktivität verwenden." Priority Must, **Release A2**. Canvas-Anker **CAN-142**; AC-042, EV-043, TRC-041. `measurement_type` OPERATIONAL_QUALITY. **Warum eine eigene REQ-ID (geprüft, nicht angenommen):** REQ-006 („eine Route über Wegpunkte oder ein Distanzziel planen, das korrekte Run-/Bike-Routingprofil verwenden und den Plan vor dem Start prüfen") deckt das **Anlegen** einer Route auf Gate A0 ab, nicht die **Wiederverwendung** einer gespeicherten Route auf Gate A2; REQ-007 betrifft den Fortschritt während der Aktivität. Kein bestehendes Requirement trägt die Aussage. **Source Type ASSUMPTION.** **Vision-Anker: VIS-014 = reserved, Inhalt MISSING → BLOCKER** (§8 Punkt 38). Es wird ausdrücklich **kein** bestehendes VIS-Item umgedeutet — insbesondere **nicht** VIS-003. |
| REQ-042 | requirement | Vergleich fachlich vergleichbarer Aktivitäten | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-20 | — | — | **Neu in Runde 4 (2026-07-20); Nachfolger 2 von 2 für REQ-040.** Aussage: „Nutzer können fachlich vergleichbare Aktivitäten auf derselben oder hinreichend ähnlichen Strecke anhand sportartspezifischer Kennzahlen miteinander vergleichen." Priority Must, **Release A2**. Canvas-Anker **CAN-143**; AC-043, EV-044, TRC-042. `measurement_type` OPERATIONAL_QUALITY. **Source Type ASSUMPTION.** **Die Vergleichslogik selbst bleibt RESEARCH_HYPOTHESIS bzw. MISSING**, solange **OQ-015** offen ist; sie wird hier **nicht erfunden**. Run und Bike **strikt getrennt**. Vision-Anker **VIS-003** — übernommen aus TRC-040 und weiterhin ausdrücklich eine **zu prüfende ASSUMPTION des Traceability-Owners**, keine Feststellung dieser Registry: VIS-003 nennt „konkrete Fortschrittssignale", was einen Aktivitätsvergleich plausibel trägt; ob es ihn **trägt**, ist ungeprüft (§6.1.1 zeigt, wie eine plausible Lesart zum falschen Anker führt). Die Einstufung wird **nicht hochgestuft**. |

### 6.5 AC — Acceptance Criteria

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| AC-001 | acceptance-criterion | Zu REQ-001 — Then: Alle sportabhängigen Metriken, Schwellen, Labels und Routingprofile wechseln konsistent; Run zeigt Pace, Bike… | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-001. |
| AC-002 | acceptance-criterion | Zu REQ-002 — Then: Die Route und Live-Metriken aktualisieren sich fortlaufend und die Aktivität kann kontrolliert beendet werden. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-002. |
| AC-003 | acceptance-criterion | Zu REQ-003 — Then: Die Aktivität bleibt lückenlos, Pausenzeit verfälscht keine Metrik und die Session ist wiederherstellbar. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-003. |
| AC-004 | acceptance-criterion | Zu REQ-004 — Then: Akzeptierte, verworfene und unsichere Punkte sind deterministisch und nachvollziehbar klassifiziert. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-004. |
| AC-005 | acceptance-criterion | Zu REQ-005 — Then: Keine Aktivität geht verloren und Migrationen sowie Indexe bleiben konsistent. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-005. |
| AC-006 | acceptance-criterion | Zu REQ-006 — Then: Eine plausible Route beziehungsweise ein Ziel mit Distanz und Fehlermeldungen wird angezeigt. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-006. |
| AC-007 | acceptance-criterion | Zu REQ-007 — Then: Fortschritt bleibt monoton plausibel, Restdistanz folgt der Route und Off-Route-Zustand wird sichtbar. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-007. |
| AC-008 | acceptance-criterion | Zu REQ-008 — Then: Verlauf und Detailansicht liefern die korrekten sportbezogenen Daten und die aufgezeichnete Route. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-008. **VERENGT im Auftau-Schritt 2 (2026-07-19)** parallel zu REQ-008: die Klausel „und exportierbar" ist entfernt und liegt jetzt bei AC-039 (GPX-Export); der Vergleich liegt bei AC-040. **Run und Bike müssen GETRENNT geprüft werden** (Nutzerentscheidung): gespeicherte Aktivität erscheint nach Neustart im Verlauf · Detailansicht lädt den korrekten Track · **Run zeigt Pace** · **Bike zeigt Geschwindigkeit** · keine Aktivität geht nach regulärem Abschluss verloren · beschädigte oder unbekannte Aktivitätsdaten führen zu einem **kontrollierten Zustand**. PRD-Nachzug macht Phase 2/3. |
| AC-009 | acceptance-criterion | Zu REQ-009 — Then: Live-/Verlaufs-HF und Quelle werden korrekt dargestellt; fehlende HF blockiert Tracking nicht. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-009. |
| AC-010 | acceptance-criterion | Zu REQ-010 — Then: Nutzer sehen Score, konkrete Gründe, Datenbasis, fehlende Signale und die Unsicherheit der Aussage. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-010. |
| AC-011 | acceptance-criterion | Zu REQ-011 — Then: Zonen und Hinweise reagieren korrekt; Deaktivierung verhindert jede Ansage. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-011. |
| AC-012 | acceptance-criterion | Zu REQ-012 — Then: Der Check-in dauert unter zwei Sekunden und Trends werden ohne Kausalitätsbehauptung angezeigt. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-012. |
| AC-013 | acceptance-criterion | Zu REQ-013 — Then: Aktivitäten, Belastung und Trend sind korrekt; Hinweise verwenden freigegebene Orientierungssprache. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-013. |
| AC-014 | acceptance-criterion | Zu REQ-014 — Then: Inhalt bleibt verständlich, bedienbar und kontrastreich; Farbe ist nie der einzige Träger. | `docs/prd/revyr-endurance-platform.prd.md` | **deprecated** | 2026-07-18 | 2026-07-19 | AC-037, AC-038 | **Deprecated im Auftau-Schritt 2 (2026-07-19)**, weil REQ-014 deprecated ist. AC-014 vermischte dieselben zwei Prüfungen wie REQ-014: „verständlich, bedienbar, kontrastreich" ist Accessibility (→ AC-037), „Farbe ist nie der einzige Träger" wirkt in **beiden** Nachfolgern und wird deshalb in AC-037 **und** AC-038 mit unterschiedlicher Prüfrichtung geführt (Zugänglichkeitsschranke bzw. Gestaltungsregel). Neue Referenzen auf AC-014 sind ein Validierungsfehler. |
| AC-015 | acceptance-criterion | Zu REQ-015 — Then: Das Item wird genau einmal freigeschaltet; ohne Leistung oder Kauf ist es nicht verfügbar. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-015. |
| AC-016 | acceptance-criterion | Zu REQ-016 — Then: Metriken sind korrekt, exportierbar und sensible Standortdaten sind reduziert. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-016. |
| AC-017 | acceptance-criterion | Zu REQ-017 — Then: Daten migrieren/synchronisieren deterministisch; Löschung entfernt alle personenbezogenen Daten gemäß Retenti… | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-017. |
| AC-018 | acceptance-criterion | Zu REQ-018 — Then: Nur erlaubte Daten sind sichtbar; Blockierung wirkt beidseitig sofort und Meldungen sind bearbeitbar. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-018. |
| AC-019 | acceptance-criterion | Zu REQ-019 (**funktional**) — Then: Ein berechtigter Nutzer kann eine sichtbare Routenempfehlung übernehmen; die übernommene Route wird in seiner Planung verfügbar, ohne dass private Daten des Empfehlenden offengelegt werden. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-019. **AUFGETEILT im Auftau-Schritt 2 (2026-07-19)** nach Nutzerentscheidung. AC-019 behält das **funktionale** Kriterium (inhaltlich der Kern des Alttexts „Feed-Sichtbarkeit, Routendaten und Übernahme entsprechen den Privacy-Regeln", jetzt als prüfbarer Ablauf formuliert). Das **Messkriterium** ist nach **AC-041** ausgelagert. **Warum zwei IDs statt zweier Felder einer AC — siehe §6.5.1.** |
| AC-020 | acceptance-criterion | Zu REQ-020 — Then: Es existiert nie ein Team ohne Admin und ungültige Tokens gewähren keinen Zugang. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-020. |
| AC-021 | acceptance-criterion | Zu REQ-021 — Then: Nur Mitglieder mit Aktivität im definierten Zeitfenster zählen; Bonus folgt erst nach nachgewiesener Integrat… | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-021. |
| AC-022 | acceptance-criterion | Zu REQ-022 — Then: Echte gemeinsame Aktivität wird erkannt, nicht gemeinsame wird abgelehnt und Eventinhalte sind moderierbar. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-022. |
| AC-023 | acceptance-criterion | Zu REQ-023 — Then: Keine Sportart dominiert systematisch; verwendete Version und Faktoren sind nachvollziehbar. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-023. |
| AC-024 | acceptance-criterion | Zu REQ-024 — Then: Fehlende Sensoren allein führen nicht zur Betrugsannahme; klare Manipulation zählt nicht für Wettbewerb. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-024. |
| AC-025 | acceptance-criterion | Zu REQ-025 — Then: Fortschritt ist korrekt und kein Reward wird doppelt vergeben. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-025. |
| AC-026 | acceptance-criterion | Zu REQ-026 — Then: Eroberung folgt Formel und Quorum, reale Areale werden dargestellt und das interne Raster ist nie sichtbar. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-026. |
| AC-027 | acceptance-criterion | Zu REQ-027 — Then: Aktive Besitzstände werden zurückgesetzt und historische Records bleiben vollständig abrufbar. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-027. |
| AC-028 | acceptance-criterion | Zu REQ-028 — Then: Dasselbe Eingabeset erzeugt dieselbe Geometrie und denselben Besitzer; Linien-/Drift-Tracks werden abgelehnt. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-028. |
| AC-029 | acceptance-criterion | Zu REQ-029 — Then: Nur plausible Runden zählen; geschlossene/private Anlagen bleiben gesperrt und Bahngold verändert keine Effor… | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-029. |
| AC-030 | acceptance-criterion | Zu REQ-030 — Then: In jedem Pfad endet die Freigabe; unberechtigte und blockierte Personen sehen keinen Standort. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-030. |
| AC-031 | acceptance-criterion | Zu REQ-031 — Then: Ein sichtbarer Countdown startet, kann abgebrochen werden und nur danach wird der definierte Kontakt informie… | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-031. |
| AC-032 | acceptance-criterion | Zu REQ-032 — Then: Status und Messwerte bleiben zwischen Geräten konsistent und nicht unterstützte Kombinationen sind klar benan… | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-032. |
| AC-033 | acceptance-criterion | Zu REQ-033 — Then: Empfehlung nennt Gründe, Grenzen und Datenbasis; sensible Funktionen sind Opt-in und vollständig deaktivierba… | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-033. |
| AC-034 | acceptance-criterion | Zu REQ-034 — Then: Zugriff folgt Berechtigung und Zweckbindung; nicht benötigte sensible Daten verlassen das Gerät nicht. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-034. |
| AC-035 | acceptance-criterion | Zu REQ-035 — Then: Status wird nur bei vollständiger Evidence auf done gesetzt; fehlende Nachweise bleiben sichtbar. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-035. |
| AC-036 | acceptance-criterion | Zu REQ-036 — Then: Kein Release wird ohne vollständige Nachweise und Policy-Abnahmen veröffentlicht. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-036. |
| AC-037 | acceptance-criterion | Zu REQ-037 — Then: WCAG-2.2-AA-Audit bestanden; relevante Screens mit VoiceOver UND TalkBack geprüft; Dynamic Type bzw. Font Scaling geprüft; keine Information ausschließlich durch Farbe; dokumentierte Kontrastprüfung. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19); Nachfolger 1 von 2 für AC-014.** Gehört zu REQ-037. Fünf einzeln prüfbare Bedingungen, alle aus der Nutzerentscheidung. **VoiceOver UND TalkBack** — beide, nicht „ein Screenreader". Prüfung auf **iOS und Android getrennt**. |
| AC-038 | acceptance-criterion | Zu REQ-038 — Then: Farbe erscheint ausschließlich in den vier definierten fachlichen Bedeutungen; Run und Bike sind nicht ausschließlich durch Farbe unterscheidbar; alle Farbwerte stammen aus Design-Tokens. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19); Nachfolger 2 von 2 für AC-014.** Gehört zu REQ-038. Die vier zulässigen Bedeutungen sind abschließend: Health-Status, Team-/Revieridentität, Sportplatz-Gold, bestätigte Feiermomente (CAN-141). Prüfrichtung ist die **Gestaltungsregel** (wo darf Farbe stehen), nicht die Zugänglichkeit (AC-037). |
| AC-039 | acceptance-criterion | Zu REQ-039 — Then: Für abgeschlossene Run- und Bike-Aktivitäten wird je eine standardkonforme GPX-Datei erzeugt, die in einer definierten kompatiblen Fremd-App geöffnet werden kann. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19).** Gehört zu REQ-039. Mindestbedingungen aus der Nutzerentscheidung, **jede einzeln prüfbar**: (a) GPX für abgeschlossene **Run**-Aktivität erzeugt · (b) GPX für abgeschlossene **Bike**-Aktivität erzeugt · (c) Zeitstempel und Koordinatenreihenfolge korrekt · (d) Datei in mindestens einer **definierten** kompatiblen Fremd-App öffenbar · (e) **keine Health-Daten unbeabsichtigt exportiert** · (f) Nutzer sieht **vor** dem Export, welche Daten enthalten sind · (g) fehlende oder beschädigte Trackdaten führen zu einem **kontrollierten Fehler** · (h) Export funktioniert **ohne** Veröffentlichung oder Social-Freigabe. **MISSING:** welche Fremd-App als Referenz gilt, ist nicht festgelegt — wird nicht geraten (OQ-016). |
| AC-040 | acceptance-criterion | Zu REQ-040 — Then: Eine gespeicherte Strecke kann erneut gestartet werden; zwei als vergleichbar erkannte Aktivitäten derselben Sportart werden mit definierten Kennzahlen gegenübergestellt. | `docs/prd/revyr-endurance-platform.prd.md` | **deprecated** | 2026-07-19 | 2026-07-20 | AC-042, AC-043 | **Deprecated in Runde 4 (2026-07-20)**, weil REQ-040 deprecated ist. Der Alttext belegt die Composite-Natur wörtlich: der erste Halbsatz („erneut gestartet werden") ist die **Planungs**bedingung → AC-042, der zweite („werden mit definierten Kennzahlen gegenübergestellt") die **Auswertungs**bedingung → AC-043. Die erste ist heute erfüllbar, die zweite ist ohne OQ-015 nicht spezifizierbar — eine ID kann diese zwei Zustände nicht gleichzeitig tragen (Regel 5, vgl. §6.5.1). |
| AC-042 | acceptance-criterion | Zu REQ-041 — Then: Eine zuvor gespeicherte Route kann als Grundlage einer neuen geplanten Run- oder Bike-Aktivität ausgewählt und gestartet werden; die geladene Route entspricht der gespeicherten in Geometrie und Wegpunkten. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-20 | — | — | **Neu (2026-07-20); Nachfolger 1 von 2 für AC-040.** Gehört zu **REQ-041**. Einzeln prüfbare Bedingungen: (a) gespeicherte Route für **Run** wiederverwendbar · (b) gespeicherte Route für **Bike** wiederverwendbar · (c) geladene Geometrie und Wegpunkte stimmen mit der gespeicherten überein · (d) das sportartspezifische Routingprofil bleibt beim Laden korrekt (Abgrenzung zu REQ-001/REQ-006) · (e) eine gelöschte oder beschädigte gespeicherte Route führt zu einem **kontrollierten Fehler**, nicht zu einem stillen Leerstart. **Vollständig spezifizierbar — nicht von OQ-015 abhängig.** Das ist der operative Grund für die Teilung. |
| AC-043 | acceptance-criterion | Zu REQ-042 — Then: Zwei als fachlich vergleichbar erkannte Aktivitäten derselben Sportart werden anhand sportartspezifischer Kennzahlen gegenübergestellt. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-20 | — | — | **Neu (2026-07-20); Nachfolger 2 von 2 für AC-040.** Gehört zu **REQ-042**. **Feststehend und schon jetzt prüfbar:** (a) Run und Bike **strikt getrennt** — es wird nie sportübergreifend verglichen · (b) **keine irreführende Bestzeit bei nicht vergleichbarer Geometrie**. **MISSING (OQ-015) und hier NICHT erfunden:** Vergleichbarkeitskriterium, tolerierte Abweichung der Streckenähnlichkeit, verglichene Kennzahlen sowie die Behandlung verkürzter, verlängerter und abgebrochener Aktivitäten. **AC-043 ist bis zur Entscheidung von OQ-015 nicht vollständig prüfbar** — AC-042 ist davon unberührt. |
| AC-041 | acceptance-criterion | Zu REQ-019 (**Messkriterium**) — Then: Für Gate B kann die Zahl bestätigter Übernahmen je auswertbarer Empfehlung datenschutzkonform, sportartspezifisch und reproduzierbar berechnet werden. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19).** Zweites Acceptance Criterion zu **REQ-019**, ausgelagert aus AC-019. Bezug: CAN-130 (§6.3.2), EV-041. `evidence_status` **planned**. **Dieses Kriterium prüft die Berechenbarkeit der Kennzahl, nicht ihren Zielwert** — ob > 1,0 erreicht wird, ist eine Produktfrage und keine Abnahmebedingung. Abhängig von OQ-012 (Telemetrie) und OQ-014 (Stichprobenregel). |

#### 6.5.1 Warum AC-019 in zwei IDs zerfällt und nicht in zwei Felder einer AC

Dies war eine zu treffende Modellierungsentscheidung; hier die Begründung.

**Entscheidung: zwei getrennte AC-IDs** (AC-019 funktional, AC-041 Messkriterium).

Ausschlaggebend ist ein Satz der Nutzerentscheidung selbst: *„Das funktionale Kriterium kann
bestanden sein, während die Produktkennzahl noch keine ausreichende Stichprobe hat."* Damit haben
die beiden Kriterien **zu jedem Zeitpunkt unabhängige Zustände**. Zwei Felder derselben AC-ID
hätten genau die Konsequenz, dass eine ID zwei unabhängig wahre oder falsche Aussagen trägt —
ein Verstoß gegen **Regel 5** („Eine ID hat genau eine Bedeutung") und strukturell derselbe
Defekt, den §3.1 für `status` bereits behoben hat: **ein Feld, zwei unabhängige Fragen**.

Hinzu kommen drei praktische Unterschiede, die eine gemeinsame ID unbrauchbar machten:

| | AC-019 (funktional) | AC-041 (Messkriterium) |
|---|---|---|
| Nachweisart | E2E-Flow zwischen zwei Konten | Auswertbarkeit einer aggregierten Kennzahl |
| Fälligkeit | mit der Funktion | zu Gate B, abhängig von OQ-012 und OQ-014 |
| Blockierbarkeit | durch Implementierungsfehler | durch fehlende Telemetrie-Entscheidung |

Eine gemeinsame ID hätte den Nachweis der Funktion an die offene Telemetriefrage gekettet und
damit eine Blockade erzeugt, die die Nutzerentscheidung ausdrücklich **nicht** will
(„Blocking: NICHT für A0/A1, NICHT für die Dokumentkorrektur").

**Folge:** REQ-019 ist das erste Requirement mit **zwei** Acceptance Criteria. Die bisher
implizite 1:1-Beziehung REQ↔AC gilt damit nicht mehr. Jede Prüfung, die 1:1 voraussetzt oder
`Anzahl AC == Anzahl REQ` erwartet, ist zu korrigieren — **die Prüfung, nicht die Daten**.

### 6.6 TRC — Traceability-Zeilen

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| TRC-001 | traceability-row | VIS-008 ↔ CAN-005 ↔ REQ-001 ↔ AC-001 ↔ EV-001 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-002 | traceability-row | VIS-003 ↔ CAN-005 ↔ REQ-002 ↔ AC-002 ↔ EV-002 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-003 | traceability-row | VIS-005 ↔ CAN-007 ↔ REQ-003 ↔ AC-003 ↔ EV-003 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-007 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-004 | traceability-row | VIS-007 ↔ CAN-008 ↔ REQ-004 ↔ AC-004 ↔ EV-004 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-008 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-005 | traceability-row | VIS-005 ↔ CAN-007 ↔ REQ-005 ↔ AC-005 ↔ EV-005 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-007 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-006 | traceability-row | VIS-003 ↔ CAN-005 ↔ REQ-006 ↔ AC-006 ↔ EV-006 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-007 | traceability-row | VIS-003 ↔ CAN-005 ↔ REQ-007 ↔ AC-007 ↔ EV-007 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-008 | traceability-row | VIS-003 ↔ CAN-005 ↔ REQ-008 ↔ AC-008 ↔ EV-008 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-009 | traceability-row | VIS-007 ↔ CAN-005 ↔ REQ-009 ↔ AC-009 ↔ EV-009 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-010 | traceability-row | VIS-007 ↔ CAN-003 ↔ REQ-010 ↔ AC-010 ↔ EV-010 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-003 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-011 | traceability-row | VIS-007 ↔ CAN-005 ↔ REQ-011 ↔ AC-011 ↔ EV-011 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-012 | traceability-row | VIS-003 ↔ CAN-009 ↔ REQ-012 ↔ AC-012 ↔ EV-012 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-009 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-013 | traceability-row | VIS-007 ↔ CAN-009 ↔ REQ-013 ↔ AC-013 ↔ EV-013 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-009 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-014 | traceability-row | VIS-009 ↔ CAN-007 ↔ REQ-014 ↔ AC-014 ↔ EV-014 | `docs/traceability.md` | **deprecated** | 2026-07-18 | 2026-07-19 | TRC-037, TRC-038 | **Deprecated im Auftau-Schritt 2 (2026-07-19)**, weil REQ-014, AC-014 und EV-014 deprecated sind. Die Zeile referenzierte **drei** deprecatete IDs plus das deprecatete Sammelblock-Item CAN-007 plus den bereits am 2026-07-19 als falsch erkannten Vision-Anker VIS-009 — sie ist in keinem Feld mehr gültig und wird nicht repariert, sondern ersetzt durch TRC-037 und TRC-038. |
| TRC-015 | traceability-row | VIS-004 ↔ CAN-005 ↔ REQ-015 ↔ AC-015 ↔ EV-015 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-016 | traceability-row | VIS-004 ↔ CAN-009 ↔ REQ-016 ↔ AC-016 ↔ EV-016 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-009 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-017 | traceability-row | VIS-005 ↔ CAN-011 ↔ REQ-017 ↔ AC-017 ↔ EV-017 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-011 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-018 | traceability-row | VIS-009 ↔ CAN-007 ↔ REQ-018 ↔ AC-018 ↔ EV-018 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-007 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-019 | traceability-row | **VIS-003** ↔ CAN-058 ↔ REQ-019 ↔ AC-019, AC-041 ↔ EV-019, EV-041 | `docs/traceability.md` | active | 2026-07-18 | — | — | **Vision-Anker in Runde 4 (2026-07-20) korrigiert: VIS-008 → VIS-003** (Nutzerentscheidung). **Der alte Anker war semantisch falsch:** VIS-008 ist die *Fairness Boundary* („Run und Bike besitzen getrennte Metriken, Ziele und interne Wertungen; sportübergreifender Effort nur mit simulierten und versionierten Faktoren") und trägt **keine** Community-Aussage. Er war syntaktisch gültig, las sich plausibel und trug die falsche Bedeutung — dieselbe Defektklasse wie VIS-009 ↔ REQ-014. **Tragende Klausel von VIS-003:** „…und einen **sicheren Zugang zu lokalen Trainingspartnern**." Ein Feed lokaler Routen und Aktivitäten ist die Entdeckungsfläche für genau diesen Zugang. **Teilbefund, offengelegt:** VIS-003 nennt **keine Routenempfehlung**; die Empfehlungs-Hälfte ist damit nur mittelbar getragen. Die Nutzerentscheidung erlaubt eine weitere Verknüpfung „**nur wenn belegt**" — sie ist **nicht** belegt, deshalb wird **keine** hinzugefügt (§8 Punkt 41). ACHTUNG: Die Canvas-Spalte zeigte auf das deprecatete Sammelblock-Item CAN-005; hier auf das atomare **CAN-058** (Routenempfehlungen) gestellt. Matrix-Nachzug macht Phase 2/3. |
| TRC-020 | traceability-row | **VIS-004** ↔ CAN-060 ↔ REQ-020 ↔ AC-020 ↔ EV-020 | `docs/traceability.md` | active | 2026-07-18 | — | — | **Vision-Anker in Runde 4 (2026-07-20) korrigiert: VIS-008 → VIS-004** (Nutzerentscheidung). Begründung: VIS-008 (Fairness Boundary) trägt keine Community-Aussage. **Tragende Klausel von VIS-004:** „Die Plattform verbindet erklärbare Trainingsbelastung, verdiente Progression, **lokale Teams** und reale ortsbezogene Spielmechaniken…". Teamgründung und Beitritt sind die konstituierende Handlung von „lokale Teams" — der Bezug ist **wörtlich**, nicht interpretiert. Canvas-Spalte von CAN-005 auf das atomare **CAN-060** (Lokale Teams) gestellt. Matrix-Nachzug macht Phase 2/3. |
| TRC-021 | traceability-row | **VIS-004** ↔ CAN-060 ↔ REQ-021 ↔ AC-021 ↔ EV-021 | `docs/traceability.md` | active | 2026-07-18 | — | — | **Vision-Anker in Runde 4 (2026-07-20) korrigiert: VIS-008 → VIS-004** (Nutzerentscheidung). **Tragende Klausel:** „lokale Teams" in VIS-004. Aktive Mitglieder und Teamwachstum sind der **Fortbestand** derselben Aussage: ein Team ohne aktive Mitglieder ist kein lokales Team. Eigene Zeile trotz gleichem Anker wie TRC-020, weil Gründung (REQ-020) und Wachstum (REQ-021) unabhängig prüfbar sind. Canvas-Spalte auf **CAN-060** gestellt. Matrix-Nachzug macht Phase 2/3. |
| TRC-022 | traceability-row | **VIS-003** ↔ CAN-067 ↔ REQ-022 ↔ AC-022 ↔ EV-022 | `docs/traceability.md` | active | 2026-07-18 | — | — | **Vision-Anker in Runde 4 (2026-07-20) korrigiert: VIS-008 → VIS-003** (Nutzerentscheidung; jede Verknüpfung einzeln geprüft). **VIS-003 — JA:** die Klausel „sicherer Zugang zu lokalen Trainingspartnern" wird durch eine gemeinsame Aktivität bzw. ein Event **eingelöst**; das ist die Handlung, auf die der Zugang zielt. **VIS-004 — NEIN, geprüft und verworfen:** VIS-004 nennt „lokale Teams" (der organisatorische **Rahmen**) und „reale ortsbezogene Spielmechaniken" (Territory/Spiel, nicht gemeinsames Training). Keine der beiden Klauseln sagt etwas über **gemeinsame Aktivitäten oder Events** aus. Eine Verknüpfung wäre die plausible Lesart ohne tragende Aussage und wird deshalb **nicht** gesetzt. Canvas-Spalte von CAN-005 auf das atomare **CAN-067** (Lokale Events) gestellt. Matrix-Nachzug macht Phase 2/3. |
| TRC-023 | traceability-row | VIS-008 ↔ CAN-008 ↔ REQ-023 ↔ AC-023 ↔ EV-023 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-008 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-024 | traceability-row | VIS-008 ↔ CAN-008 ↔ REQ-024 ↔ AC-024 ↔ EV-024 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-008 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-025 | traceability-row | VIS-004 ↔ CAN-005 ↔ REQ-025 ↔ AC-025 ↔ EV-025 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-026 | traceability-row | VIS-008 ↔ CAN-011 ↔ REQ-026 ↔ AC-026 ↔ EV-026 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-011 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-027 | traceability-row | VIS-004 ↔ CAN-005 ↔ REQ-027 ↔ AC-027 ↔ EV-027 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-028 | traceability-row | VIS-008 ↔ CAN-008 ↔ REQ-028 ↔ AC-028 ↔ EV-028 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-008 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-029 | traceability-row | VIS-004 ↔ CAN-008 ↔ REQ-029 ↔ AC-029 ↔ EV-029 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-008 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-030 | traceability-row | VIS-009 ↔ CAN-008 ↔ REQ-030 ↔ AC-030 ↔ EV-030 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-008 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-031 | traceability-row | VIS-007 ↔ CAN-008 ↔ REQ-031 ↔ AC-031 ↔ EV-031 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-008 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-032 | traceability-row | VIS-005 ↔ CAN-005 ↔ REQ-032 ↔ AC-032 ↔ EV-032 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-005 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-033 | traceability-row | VIS-007 ↔ CAN-007 ↔ REQ-033 ↔ AC-033 ↔ EV-033 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-007 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-034 | traceability-row | VIS-009 ↔ CAN-007 ↔ REQ-034 ↔ AC-034 ↔ EV-034 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-007 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-035 | traceability-row | VIS-010 ↔ CAN-010 ↔ REQ-035 ↔ AC-035 ↔ EV-035 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-010 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-036 | traceability-row | VIS-010 ↔ CAN-007 ↔ REQ-036 ↔ AC-036 ↔ EV-036 | `docs/traceability.md` | active | 2026-07-18 | — | — | Zeilenstatus in der Matrix: linked. ACHTUNG: Die Canvas-Spalte zeigt noch auf das deprecated Sammelblock-Item CAN-007 und muss in Phase 3 vom Traceability-Owner auf ein atomares CAN-Item aus Abschnitt 6.3 umgestellt werden. |
| TRC-037 | traceability-row | VIS-011 ↔ CAN-099 ↔ REQ-037 ↔ AC-037 ↔ EV-037 | `docs/traceability.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19); Nachfolger 1 von 2 für TRC-014.** Accessibility. **Zeilenstatus: NICHT `linked`** — VIS-011 ist ASSUMPTION und unbestätigt und zählt nach §8 Punkt 15 **nicht** als erfüllter Vision-Anker. Der Anker ist *belegt und benannt*, aber nicht *bestätigt*. **Runde 4 (2026-07-20) — verbotene Schlusskette entfernt (Nutzerentscheidung):** die in §6.1.1 ausdrücklich untersagte Kette „**Wahrnehmbarkeit als Vorstufe von Verständlichkeit**" durfte in `docs/traceability.md` **zwei** Anker für REQ-037 tragen — `:1488` (canvas-problem → **CAN-013** „Bestehende Tracker liefern Daten ohne verständliche Bedeutung") und `:1546` (value-promise → **CAN-029** „Verstehe deine Belastung"). Beide sind zu **entfernen**. CAN-013 handelt von der **Bedeutungsarmut von Trainingsdaten**, CAN-029 von der **Erklärbarkeit der Belastung** — keines von beiden sagt etwas über die **Wahrnehmbarkeit einer Oberfläche**. Nach der Entfernung ist der canvas-problem-Anker von REQ-037 **MISSING** (§8 Punkt 37); der Canvas führt kein Zugänglichkeitsproblem. Der kanonische Anker von REQ-037 ist und bleibt **CAN-099**. Matrix-Nachzug macht Phase 2/3. |
| TRC-038 | traceability-row | **VIS-012 (reserved, MISSING)** ↔ CAN-141 ↔ REQ-038 ↔ AC-038 ↔ EV-038 | `docs/traceability.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19); Nachfolger 2 von 2 für TRC-014.** Monochromes Designsystem. **Zeilenstatus: `broken` — der Vision-Anker fehlt.** VIS-012 ist reserviert, Inhalt MISSING (BLOCKER). Die Zeile wird bewusst mit sichtbarer Lücke geführt statt an ein unpassendes VIS-Item gehängt; genau letzteres war der Defekt VIS-009 ↔ REQ-014. **Runde 4 (2026-07-20) — dieselbe verbotene Kette geprüft und ebenfalls belegt:** `docs/traceability.md:1547` hängt REQ-038 mit der Begründung „(Wahrnehmbarkeit als Vorstufe von Verstehen)" an **CAN-029**. Diese Verknüpfung ist zu **entfernen**. Der kanonische Canvas-Anker von REQ-038 ist **CAN-141**. Zusätzlicher Befund: `:1489` führt REQ-038 im canvas-problem an **CAN-013** und begründet zugleich „**kein** eigenes Problem-Item — begründete Nichtanwendbarkeit" — beides zugleich ist widersprüchlich; der Wert ist auf **MISSING (begründet)** zu setzen, nicht auf CAN-013 (§8 Punkt 37). |
| TRC-039 | traceability-row | **VIS-013 (reserved, MISSING)** ↔ CAN-139 ↔ REQ-039 ↔ AC-039 ↔ EV-039 | `docs/traceability.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19).** GPX-Export. **Zeilenstatus: `broken` — der Vision-Anker fehlt** (VIS-013 reserved, MISSING). **REQ-034 bleibt AUSSCHLIESSLICH sekundärer Security-/Privacy-/Portabilitäts-Constraint** und zählt **nicht** als primärer Anker; das GPX-Canvas-Item darf nicht allein über REQ-034 getragen werden (Nutzerentscheidung 2026-07-20). **Runde 4 — verbotene Kette geprüft:** `docs/traceability.md:1490` hängt REQ-039 im canvas-problem an **CAN-013** mit der Variante „(Daten, die man nicht mitnehmen kann, bleiben fremdbestimmt)" und vermerkt im selben Feld bereits „**schwacher Bezug, offengelegt** … der Canvas führt **kein** Portabilitäts- oder Lock-in-Problem. MISSING." Das ist **dieselbe Defektklasse** in anderer Formulierung: CAN-013 wird als Universal-Problemanker benutzt. Die Verknüpfung ist zu **entfernen**, der Wert bleibt **MISSING** (§8 Punkt 37). |
| TRC-040 | traceability-row | VIS-003 ↔ CAN-140 ↔ REQ-040 ↔ AC-040 ↔ EV-040 | `docs/traceability.md` | **deprecated** | 2026-07-19 | 2026-07-20 | TRC-041, TRC-042 | **Deprecated in Runde 4 (2026-07-20)**, weil die Zeile nach der Teilung **fünf deprecatete IDs** referenzierte (CAN-140, REQ-040, AC-040, EV-040) und weil ihr einziger Vision-Anker nur **eine** der beiden Hälften betraf — `docs/traceability.md:1702` hielt das bereits als `linked-partial` fest. Ersetzt durch TRC-041 (Wiederverwendung) und TRC-042 (Vergleich). |
| TRC-041 | traceability-row | **VIS-014 (reserved, MISSING)** ↔ CAN-142 ↔ REQ-041 ↔ AC-042 ↔ EV-043 | `docs/traceability.md` | active | 2026-07-20 | — | — | **Neu (2026-07-20); Nachfolger 1 von 2 für TRC-040.** Wiederverwendung einer gespeicherten Route. **Zeilenstatus: `broken` — der Vision-Anker fehlt.** VIS-014 ist reserviert, Inhalt MISSING (BLOCKER, §8 Punkt 38). Die Zeile wird bewusst mit sichtbarer Lücke geführt statt an VIS-003 gehängt: VIS-003 nennt Tracking, Health-Auswertung, Fortschrittssignale und Trainingspartner — **keine** Wiederverwendung geplanter Strecken. Genau diese Auffüllung war der Defekt VIS-009 ↔ REQ-014. Matrix-Nachzug macht Phase 2/3. |
| TRC-042 | traceability-row | VIS-003 ↔ CAN-143 ↔ REQ-042 ↔ AC-043 ↔ EV-044 | `docs/traceability.md` | active | 2026-07-20 | — | — | **Neu (2026-07-20); Nachfolger 2 von 2 für TRC-040.** Vergleich fachlich vergleichbarer Aktivitäten. **Vision-Anker VIS-003 unverändert aus TRC-040 übernommen und ausdrücklich weiterhin eine ASSUMPTION des Traceability-Owners, keine Feststellung dieser Registry:** VIS-003 nennt „konkrete Fortschrittssignale", was einen Aktivitätsvergleich plausibel trägt — ob es ihn **trägt**, ist ungeprüft und wird hier **nicht** hochgestuft (§6.1.1). Zeilenstatus damit **nicht `linked`**, sondern `linked-partial` wie im Vorgänger. Matrix-Nachzug macht Phase 2/3. |

### 6.7 EV — Evidence Needed

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| EV-001 | evidence | Konfigurations-Unit-Tests und Screen-Checkliste für iOS/Android. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-001. |
| EV-002 | evidence | Gerätetest je Sport und Plattform auf Referenzstrecke. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-002. |
| EV-003 | evidence | 30-Minuten-Kill-/Background-Test je Plattform und Sport. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-003. |
| EV-004 | evidence | Drift-, Tunnel-, Sprung- und Hochgeschwindigkeits-Fixtures. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-004. |
| EV-005 | evidence | SQLite-Repository-Tests, Kill-Test und Migrations-Fixtures. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-005. |
| EV-006 | evidence | Routing-Service-Tests und zehn reale Routenszenarien je Sport. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-006. |
| EV-007 | evidence | Polyline-Projektions-Fixtures und reale Abweichungstests. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-007. |
| EV-008 | evidence | Repository- und UI-Test für Verlauf und Detailansicht, **je Sportart getrennt** (Run zeigt Pace, Bike zeigt Geschwindigkeit); Neustart-Test auf Persistenz; Negativtest auf beschädigte oder unbekannte Aktivitätsdaten. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-008 / AC-008 / CAN-138. **Titel in Runde 4 (2026-07-20) an die `canonical_file` angeglichen** (`prd.md:731`) — die Registry führte weiterhin den Alttitel „Repository-, UI- und **GPX-Kompatibilitätstest**", obwohl das PRD den GPX-Anteil bereits am 2026-07-19 nach EV-039 ausgelagert hatte. Nach §1 hätte die **veraltete Registry-Definition** bei jeder Prüfung gewonnen und den ausgelagerten Nachweis doppelt geführt. **Kanonische Trennung (verbindlich): EV-008 ist AUSSCHLIESSLICH Evidence für Verlauf und Detailansicht.** Es enthält **keinen** GPX-, Export-, Portabilitäts- oder Fremd-App-Nachweis. Wer einen GPX-Nachweis unter EV-008 findet, hat einen Validierungsfehler gefunden. |
| EV-009 | evidence | Echte Geräte und BLE-Gurt je Plattform. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-009. |
| EV-010 | evidence | Formeltests mit/ohne HF und UI-Test des Warum-Sheets. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-010. |
| EV-011 | evidence | Zonen-Unit-Tests und Kopfhörer-Gerätetest. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-011. |
| EV-012 | evidence | Zeitmessung, Fixture-Korrelation und Copy-Review. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-012. |
| EV-013 | evidence | Wochen-Fixtures und Claims-Lint. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-013. |
| EV-014 | evidence | Token-Review, Accessibility- und Screenreader-Check. | `docs/prd/revyr-endurance-platform.prd.md` | **deprecated** | 2026-07-18 | 2026-07-19 | EV-037, EV-038 | **Deprecated im Auftau-Schritt 2 (2026-07-19)**, weil REQ-014 deprecated ist. Der Alttext belegt die Composite-Natur wörtlich: „**Token**-Review" ist der Designsystem-Nachweis (→ EV-038), „**Accessibility- und Screenreader-Check**" der Zugänglichkeitsnachweis (→ EV-037). Zwei Nachweise, zwei Verfahren, eine ID — genau die Vermischung, die REQ-014 auflöst. |
| EV-015 | evidence | Idempotenz- und Unlock-Fixtures. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-015. |
| EV-016 | evidence | Bildexport-, Widget- und Privacy-Snapshot-Test. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-016. |
| EV-017 | evidence | E2E-Flow, Offline-Test und Löschungsnachweis. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-017. |
| EV-018 | evidence | Sichtbarkeits-Matrix, Zwei-Account- und Moderationstest. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-018. |
| EV-019 | evidence | Zwei-Account-E2E-Flow. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-019. |
| EV-020 | evidence | Datenbanktransaktions- und Zwei-Geräte-Test. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-020. |
| EV-021 | evidence | Zeitfenster- und Integrations-Fixtures. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-021. |
| EV-022 | evidence | Pure-Function-Fixtures und Zwei-Geräte-Eventtest. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-022. |
| EV-023 | evidence | Monte-Carlo-/Szenariosimulation und Kalibrierungsbericht. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-023. |
| EV-024 | evidence | Betrugs-/Grenzfall-Fixtures und False-Positive-Review. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-024. |
| EV-025 | evidence | Deterministische Fixtures und Wiederholungs-Test. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-025. |
| EV-026 | evidence | Geo-Fixtures, Simulation und Karten-Lasttest. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-026. |
| EV-027 | evidence | Zwei-Season-Integrationstest, Prüfung der fachlichen Unveränderbarkeit nach Finalisierung sowie Nachweis, dass Löschung und Anonymisierung als zulässige Ausnahmen korrekt greifen (Löschung eines Mitglieds mit historischen Capture-Ereignissen). | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-027. **Titel nachgezogen im Auftau-Schritt 2026-07-19.** Alttitel: „Zwei-Season-Integrationstest und Unveränderlichkeitsprüfung." **Herkunft der Neuformulierung — wichtig:** `DEC-012` gibt für den Begriff „Unveränderlichkeitsprüfung" **keine** Ersatzformulierung vor; `docs/traceability.md:1524` und `docs/EVIDENCE-LEDGER.md` halten das ausdrücklich fest. Es wurde deshalb **keine** Formulierung erfunden. Übernommen ist stattdessen **wörtlich** der Text der `canonical_file` (`docs/prd/…prd.md:293`), die das PRD am 2026-07-19 bereits migriert hatte — das ist die nach §3 vorgeschriebene Quelle für das Feld `title`. **Provenienz-Vorbehalt:** dieser Wortlaut ist eine Formulierung des PRD-Owners, **nicht** durch DEC-012 vorgegeben und **nicht** vom Nutzer bestätigt. Ändert der Nutzer die Sprachregelung, ist der PRD-Text die zu ändernde Stelle und die Registry zieht nach — nicht umgekehrt. |
| EV-028 | evidence | Geo-Fixture-Suite, Property-Tests und Threat-Model. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-028. |
| EV-029 | evidence | OSM-Access-Review, realer Bahn-Test und Reward-Fixtures. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-029. |
| EV-030 | evidence | Threat-Model, Endpfad-Matrix und Penetrationstest. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-030. |
| EV-031 | evidence | Kontrollierte Falltests, Fehlalarmstatistik und Claims-Review. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-031. |
| EV-032 | evidence | Gerätematrix und reale Integrationstests. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-032. |
| EV-033 | evidence | Claims-Lint, Rechtsfreigabe und Privacy-Test. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-033. |
| EV-034 | evidence | Security-Review, RLS-Tests, Datenflussdiagramm und Löschungsnachweis. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-034. |
| EV-035 | evidence | CI-Regel, Ledger-Review und Gate-Checkliste. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-035. |
| EV-036 | evidence | TestFlight/Internal-Test-Bericht, Policy-Matrix und Gate-Sign-off. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Gehört zu REQ-036. |
| EV-037 | evidence | WCAG-2.2-AA-Audit, VoiceOver- und TalkBack-Durchlauf je Plattform, Dynamic-Type-/Font-Scaling-Prüfung, dokumentierte Kontrastprüfung. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19); Nachfolger 1 von 2 für EV-014.** Gehört zu REQ-037 / AC-037. `evidence_status` **not-planned** — es existiert kein Code, keine CI und kein beauftragter Auditor; ein Messkonzept ist damit noch nicht vorhanden (§3.2). Fällig: Basis ab A0, vollständiger Audit spätestens A2. **OWNER-BLOCKER (MISSING)** — OQ-002. **Referenzumgebung MISSING** — OQ-003 (Minimum iOS/Android, Referenzgeräte). |
| EV-038 | evidence | Design-Token-Review: Inventar aller Farbwerte gegen die vier zulässigen fachlichen Bedeutungen; Prüfung, dass Run/Bike nicht ausschließlich farblich unterschieden werden. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19); Nachfolger 2 von 2 für EV-014.** Gehört zu REQ-038 / AC-038. `evidence_status` **not-planned** — kein Code, keine Token-Datei, kein Prüfverfahren festgelegt. **OWNER-BLOCKER (MISSING)** — OQ-002. |
| EV-039 | evidence | GPX-Export-Test je Sportart: Erzeugung, Schemakonformität, Zeitstempel- und Koordinatenreihenfolge, Öffnen in einer definierten Fremd-App, Negativtest auf Health-Daten im Export, Fehlerfall bei beschädigten Trackdaten, Export ohne Veröffentlichung. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19).** Gehört zu REQ-039 / AC-039 / CAN-139. **Kanonische Trennung (verbindlich, Runde 4): EV-039 ist AUSSCHLIESSLICH der GPX-Kompatibilitäts- und Exportnachweis.** Verlauf und Detailansicht werden **nicht** hier nachgewiesen (das ist EV-008). Die frühere Überlappung lief nicht über das PRD, sondern über die veraltete EV-008-Definition **dieser Registry** — sie ist mit diesem Schritt beseitigt. **Run und Bike getrennt nachzuweisen.** `evidence_status` **not-planned**. **MISSING:** die „definierte Fremd-App" ist nicht benannt (OQ-016) — ohne sie ist Kriterium (d) aus AC-039 nicht reproduzierbar prüfbar. Es wird keine App geraten. **Zusätzlicher Befund (§8 Punkt 36):** der kanonische CAN-139-Wortlaut nennt das Öffnen in einer Fremdanwendung nicht mehr; die Fälligkeit dieses Teilnachweises ist damit vom Wortlaut nicht mehr wörtlich gedeckt. |
| EV-040 | evidence | Vergleichstest: erneuter Start einer gespeicherten Strecke; Gegenüberstellung zweier als vergleichbar erkannter Aktivitäten derselben Sportart; Negativtests gegen verkürzte, verlängerte, abgebrochene und geometrisch abweichende Aktivitäten. | `docs/prd/revyr-endurance-platform.prd.md` | **deprecated** | 2026-07-19 | 2026-07-20 | EV-043, EV-044 | **Deprecated in Runde 4 (2026-07-20)**, weil REQ-040 deprecated ist. Der Alttext belegt die Composite-Natur: „erneuter Start einer gespeicherten Strecke" ist der **Planungs**nachweis (→ EV-043), die „Gegenüberstellung … Negativtests" der **Auswertungs**nachweis (→ EV-044). Zwei Nachweise mit **unterschiedlichem Blockierungszustand** in einer ID: der erste ist heute spezifizierbar, der zweite nicht (OQ-015). |
| EV-043 | evidence | Wiederverwendungstest je Sportart: Auswahl und Start einer gespeicherten Route, Abgleich von Geometrie und Wegpunkten gegen die gespeicherte Fassung, Erhalt des sportartspezifischen Routingprofils, kontrollierter Fehlerfall bei gelöschter oder beschädigter Route. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-20 | — | — | **Neu (2026-07-20); Nachfolger 1 von 2 für EV-040.** Gehört zu **REQ-041 / AC-042 / CAN-142**. **Run und Bike getrennt nachzuweisen.** `evidence_status` **not-planned** — es existiert kein Code und kein Messkonzept (§3.2); `pending` wäre eine behauptete Instrumentierung. **Nicht von OQ-015 blockiert.** |
| EV-044 | evidence | Vergleichstest je Sportart: Gegenüberstellung zweier als fachlich vergleichbar erkannter Aktivitäten anhand sportartspezifischer Kennzahlen; Negativtests gegen verkürzte, verlängerte, abgebrochene und geometrisch abweichende Aktivitäten; Negativtest gegen sportübergreifenden Vergleich. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-20 | — | — | **Neu (2026-07-20); Nachfolger 2 von 2 für EV-040.** Gehört zu **REQ-042 / AC-043 / CAN-143**. `evidence_status` **not-planned**. **BLOCKER:** ohne die Vergleichs- und Streckenähnlichkeitsdefinition aus **OQ-015** ist kein Testfall bezifferbar — die Negativtests sind benannt, aber ohne Toleranzwert nicht ausführbar. Es wird **keine Toleranz geraten**. |
| EV-041 | evidence | Reproduzierbare, datenschutzkonforme Berechnung der Kennzahl „bestätigte Routenübernahmen je auswertbarer Empfehlung", getrennt für Run und Bike, über ein rollierendes 28-Tage-Fenster. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19).** Gehört zu **REQ-019 / AC-041 / CAN-130**. `evidence_status` **planned** — Metrik, Berechnung und Gate (B) sind definiert (§6.3.2), die Instrumentierung fehlt (§3.2). Abhängig von OQ-012 (Telemetrie) und OQ-014 (Stichprobenregel). **Dieser Nachweis belegt die Berechenbarkeit, nicht die Zielerreichung** — `empirical_result` bleibt MISSING. |
| EV-042 | evidence | Nachweis, dass das Datenmodell Identität und historische Aggregate technisch trennt (DEC-012, Marke (z) in `docs/EVIDENCE-LEDGER.md`). | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu (2026-07-19).** Schließt §8 Punkt 14 **als ID-Frage** — der Nachweis selbst bleibt offen. Bezug: CONTRA-005, REQ-017, REQ-027, DEC-012. Vorher hatte dieser Nachweis **keine EV-ID**; `docs/EVIDENCE-LEDGER.md` führte ihn nur als Marke (z), und §6.11.1 musste bei CONTRA-005 „für … existiert **keine EV-ID**" vermerken. Die Vergabe war laut §8 Punkt 14 ausdrücklich einem Phase-1-Schritt vorbehalten — dies ist ein solcher. `evidence_status` **blocked** — die von DEC-012 **vor** der Schema-Finalisierung geforderte Trennung ist ohne Retentionsfristen (OQ-009) nicht spezifizierbar. **Der Inhalt ist nicht erfunden**, sondern wörtlich aus DEC-012 und dem Ledger übernommen. |

### 6.8 RISK — Risiken

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| RISK-001 | risk | Background-GPS wird durch OS gedrosselt oder beendet | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity critical, Phase A0, Registerstatus open. |
| RISK-002 | risk | GPS-Drift verfälscht Distanz und Route | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase A0, Registerstatus open. |
| RISK-003 | risk | Batterieverbrauch verhindert längere Nutzung | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase A0, Registerstatus open. |
| RISK-004 | risk | Alte Run&Bike-Annahmen gelangen in neue Implementierung | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase P0, Registerstatus open. |
| RISK-005 | risk | Bike zeigt falsche Laufmetriken | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase A0, Registerstatus open. |
| RISK-006 | risk | Routenrest ist bei Abweichungen falsch | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase A0, Registerstatus open. |
| RISK-007 | risk | Client-API-Key wird missbraucht | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase P0/A2, Registerstatus open. |
| RISK-008 | risk | Health-Score wird als medizinische Aussage verstanden | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity critical, Phase A1/E, Registerstatus open. |
| RISK-009 | risk | Nutzer ohne HF-Hardware erhalten unbrauchbares Produkt | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase A1, Registerstatus open. |
| RISK-010 | risk | Store lehnt Background-Location/Health/UGC ab | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity critical, Phase A-D, Registerstatus open. |
| RISK-011 | risk | Namens-/Markenkollision | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity critical, Phase A2, Registerstatus open. |
| RISK-012 | risk | Backend-Fehlentscheidung erzeugt Lock-in/Kosten | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase B, Registerstatus open. |
| RISK-013 | risk | Anti-Cheat produziert False Positives | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase C, Registerstatus open. |
| RISK-014 | risk | Run/Bike-Effort ist unfair | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase C/D, Registerstatus open. |
| RISK-015 | risk | Standortfreigabe ermöglicht Stalking | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity critical, Phase D, Registerstatus open. |
| RISK-016 | risk | Einzel-Reviere verraten Wohnort und Routine | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity critical, Phase D, Registerstatus open. |
| RISK-017 | risk | Polygonoperationen sind inkonsistent oder langsam | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase D, Registerstatus open. |
| RISK-018 | risk | OSM-Sportplatz ist privat oder falsch | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase D, Registerstatus open. |
| RISK-019 | risk | Bahngold fördert gesundheitlich riskantes Grinding | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase D, Registerstatus open. |
| RISK-020 | risk | Sturzerkennung erzeugt falsche Sicherheit | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity critical, Phase D, Registerstatus open. |
| RISK-021 | risk | Moderationsaufwand skaliert nicht | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase B-D, Registerstatus open. |
| RISK-022 | risk | Sensitive Health-Daten werden unnötig serverseitig verarbeitet | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity critical, Phase C/E, Registerstatus open. |
| RISK-023 | risk | Scope wächst vor Nachweis der Kernretention | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase alle, Registerstatus open. |
| RISK-024 | risk | User Confirmation wird fälschlich als erteilt angenommen | `docs/risks/revyr-risk-register.md` | active | 2026-07-18 | — | — | Severity high, Phase planning, Registerstatus open. |

### 6.9 ASM — Annahmen (Kollision aufgelöst)

**Befund.** `ASM-001`, `ASM-002` und `ASM-003` existierten in *zwei* Dateien mit
*unterschiedlicher* Bedeutung. Das ist dasselbe Defektmuster wie zuvor bei den OQ-IDs
(CONTRA-003) und war bis zu diesem Lauf unbemerkt. Ein Auftrag „prüfe ASM-002“ hätte je nach
gelesener Datei eine andere Annahme geprüft.

Der Auftrag nannte ASM-002 und ASM-003. Die Prüfung ergab, dass **auch ASM-001 kollidiert**:
das PRD behauptet die Aufteilung als Tatsache, die Vision behauptet ihren Nutzen. Zwei
Aussagen, eine ID.

**Auflösung.** Alle kollidierenden Alt-IDs werden deprecated. Die Nummern `ASM-001` bis
`ASM-004` werden **nicht** wiederverwendet (Regel 6), auch nicht für die jeweils „eigentlich
gemeinte“ Datei — sonst bliebe genau die Zweideutigkeit bestehen, die behoben werden soll.
Stattdessen zwei disjunkte, dateigebundene Bereiche:

- `ASM-1xx` → Annahmen des PRD
- `ASM-2xx` → Annahmen der Vision

Die Alt-IDs erscheinen unten **zweimal**, einmal je Datei. Das ist beabsichtigt: der Eintrag
bildet den Defekt ab und ist über das Paar (`id`, `canonical_file`) eindeutig.

#### Neue, kollisionsfreie IDs

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| ASM-101 | assumption | Der öffentliche v1.0-Release wird intern in A0, A1 und A2 geteilt. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Ersetzt ASM-001 (PRD). Source Type ASSUMPTION, Validation: Ressourcen- und Release-Review. |
| ASM-102 | assumption | SQLite beziehungsweise eine transaktionale lokale Datenbank ersetzt die vollständige Track-Speicherung in AsyncStorage. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Ersetzt ASM-002 (PRD). Source Type ASSUMPTION, Validation: technischer Spike. Stützt DEC-003 und REQ-005. |
| ASM-103 | assumption | Externes Routing läuft ab Stufe A0 ausschließlich über einen minimalen serverseitigen Routing-Proxy; ein Routing-API-Key als EXPO_PUBLIC_*-Variable ist ausgeschlossen. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Ersetzt ASM-003 (PRD). Source Type laut PRD: CONFIRMED (A0) / ASSUMPTION (ab A1). Bestätigt durch DEC-005 (user-confirmed) und CONTRA-002 (resolved). |
| ASM-104 | assumption | Einzel-Reviere und Bahngold bleiben bis Stufe D deaktiviert. | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Ersetzt ASM-004 (PRD). Umbenennung ausschließlich zur Bereichstrennung — ASM-004 selbst kollidierte nicht, würde aber als einzige verbliebene ASM-0xx-ID im PRD einen inkonsistenten Nummernraum hinterlassen. |
| ASM-201 | assumption | Eine gestufte öffentliche v1.0 aus A0/A1/A2 reduziert Risiko gegenüber einem einzigen überladenen MVP. | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | Ersetzt ASM-001 (Vision). Validation: Release- und Ressourcenschätzung. |
| ASM-202 | assumption | Ein Health-Score mit sichtbarer Confidence ist verständlicher und rechtlich robuster als ein einzelner absoluter Score. | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | Ersetzt ASM-002 (Vision). Validation: Nutzer- und Claims-Test. Stützt DEC-006 und REQ-010. |
| ASM-203 | assumption | Der technische Slug kann vorläufig stabil bleiben, auch wenn der öffentliche Name wechselt. | `docs/vision/revyr-endurance-platform.vision.md` | active | 2026-07-18 | — | — | Ersetzt ASM-003 (Vision). Validation: Repo-/Release-Entscheidung. Stützt DEC-001. |

#### Deprecated Alt-IDs (Kollisionsnachweis)

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| ASM-001 | assumption | Der öffentliche v1.0-Release wird intern in A0, A1 und A2 geteilt. | `docs/prd/revyr-endurance-platform.prd.md` | deprecated | 2026-07-18 | 2026-07-19 | ASM-101 | KOLLISION: dieselbe ID bezeichnet in der Vision eine andere Annahme (Risikoreduktion statt Aufteilung). |
| ASM-002 | assumption | SQLite bzw. transaktionale lokale Datenbank statt AsyncStorage. | `docs/prd/revyr-endurance-platform.prd.md` | deprecated | 2026-07-18 | 2026-07-19 | ASM-102 | KOLLISION: dieselbe ID bezeichnet in der Vision den Health-Score mit Confidence — fachlich völlig unverwandt. |
| ASM-003 | assumption | A0-Routing über serverseitigen Proxy, kein EXPO_PUBLIC_*-Key. | `docs/prd/revyr-endurance-platform.prd.md` | deprecated | 2026-07-18 | 2026-07-19 | ASM-103 | KOLLISION: dieselbe ID bezeichnet in der Vision die Stabilität des technischen Slugs. |
| ASM-004 | assumption | Einzel-Reviere und Bahngold bleiben bis Stufe D deaktiviert. | `docs/prd/revyr-endurance-platform.prd.md` | deprecated | 2026-07-18 | 2026-07-19 | ASM-104 | Keine Kollision (die Vision hat kein ASM-004). Umbenannt zur Bereichstrennung, siehe ASM-104. |
| ASM-001 | assumption | Eine gestufte öffentliche v1.0 aus A0/A1/A2 reduziert Risiko gegenüber einem überladenen MVP. | `docs/vision/revyr-endurance-platform.vision.md` | deprecated | 2026-07-18 | 2026-07-19 | ASM-201 | KOLLISION: siehe ASM-001 (PRD). |
| ASM-002 | assumption | Health-Score mit sichtbarer Confidence ist verständlicher und rechtlich robuster. | `docs/vision/revyr-endurance-platform.vision.md` | deprecated | 2026-07-18 | 2026-07-19 | ASM-202 | KOLLISION: siehe ASM-002 (PRD). |
| ASM-003 | assumption | Der technische Slug kann vorläufig stabil bleiben. | `docs/vision/revyr-endurance-platform.vision.md` | deprecated | 2026-07-18 | 2026-07-19 | ASM-203 | KOLLISION: siehe ASM-003 (PRD). |

### 6.10 OQ — Offene Fragen

Inhaltlich kanonisch bleibt `docs/decisions/open-questions.md` (CONTRA-003). Diese Registry
führt die IDs und ihren Entscheidungsstand.

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| OQ-001 | open-question | finaler öffentlicher Produktname | `docs/decisions/open-questions.md` | open | 2026-07-18 | — | — | Owner Product/Legal, fällig vor Gate A2. |
| OQ-002 | open-question | finaler Repository-Owner/DRI | `docs/decisions/open-questions.md` | open | 2026-07-18 | — | — | Owner Product, fällig vor P0 Start. |
| OQ-003 | open-question | Minimum iOS/Android und Referenzgeräte | `docs/decisions/open-questions.md` | open | 2026-07-18 | — | — | Owner Engineering/QA, fällig vor A0 Feldtest. |
| OQ-004 | open-question | Karten-/Routinganbieter | `docs/decisions/open-questions.md` | open | 2026-07-18 | — | — | Owner Engineering/Product, fällig vor A2/B. |
| OQ-005 | open-question | Backend | `docs/decisions/open-questions.md` | open | 2026-07-18 | — | — | Owner Engineering, fällig vor B. |
| OQ-006 | open-question | Claims-Whitelist | `docs/decisions/open-questions.md` | open | 2026-07-18 | — | — | Owner Product/Legal, fällig vor A1 Public Beta. |
| OQ-007 | open-question | Geschäftsmodell | `docs/decisions/open-questions.md` | open | 2026-07-18 | — | — | Owner Product/Business, fällig vor C. |
| OQ-008 | open-question | Effort-/Territory-/Bahngold-Startwerte | `docs/decisions/open-questions.md` | open | 2026-07-18 | — | — | Owner Product/Data, fällig vor C/D. |
| OQ-009 | open-question | Datenretention für GPS, Health und Live | `docs/decisions/open-questions.md` | open | 2026-07-18 | — | — | Owner Privacy/Product, fällig vor B/D. |
| OQ-010 | open-question | Moderations-SLA und Betrieb | `docs/decisions/open-questions.md` | open | 2026-07-18 | — | — | Owner Operations, fällig vor B Public. |
| OQ-012 | open-question | Privacy-minimierte Telemetrie für Routenempfehlungen | `docs/decisions/open-questions.md` | **open** | 2026-07-19 | — | — | **Neu reserviert im Auftau-Schritt 2 (2026-07-19)** auf ausdrückliche Nutzervorgabe. `source_type` **MISSING**. **Vor Gate B zu klären:** wird `exposed` client- oder serverseitig erhoben · welche Event-Metadaten sind nötig · welche Daten dürfen gespeichert werden · Aufbewahrung der Rohereignisse · ab wann nur noch Aggregate · ist eine **separate Einwilligung** nötig · Wirkung von Profil-Privacy, Blockierungen und Löschungen auf die Messung · Entfernung bzw. Anonymisierung gelöschter Accounts aus den Messdaten · Owner der Instrumentierung · verwendete Analytics-/Event-Lösung. `blocked_gates` **[B]** · `blocked_activities` **[]**. **Ausdrücklich NICHT blockierend** für A0, A1 oder die Dokumentkorrektur. **Blockierend** für den externen Gate-B-Erfolgsnachweis von REQ-019 und für **jede Behauptung, CAN-130 sei empirisch validiert**. Owner: MISSING (OQ-002). |
| OQ-013 | open-question | Messdefinition, Zielwert und Gate-Zuordnung für NFR-008 (Wartbarkeit) | `docs/decisions/open-questions.md` | **open** | 2026-07-19 | — | — | **Neu reserviert im Auftau-Schritt 2 (2026-07-19).** Ergibt sich zwingend aus der Entscheidung, NFR-008 **nicht** zu deprecaten (§6.13.1). **Zu klären:** welche Metrik (Testabdeckung, Typfehler, Anteil abhängigkeitsfreier Domainmodule, Anzahl unversionierter Schemas — **keine ist gewählt**) · Einheit · Schwellwert · Messfenster (je Commit, je Build) · Testmethode · zuständiges Gate · Owner. `blocked_gates` **[]** · `blocked_activities` **[]** — NFR-008 blockiert derzeit **nichts**, und genau das ist der Befund (§6.13.1). Owner: MISSING (OQ-002). |
| OQ-014 | open-question | Stichproben- und Auswertungsregel für CAN-130 / AC-041 | `docs/decisions/open-questions.md` | **open** | 2026-07-19 | — | — | **Neu reserviert im Auftau-Schritt 2 (2026-07-19).** Die Nutzerentscheidung zu CAN-130 zählt diese Punkte ausdrücklich als „vor endgültiger Bewertung zu definieren" auf: Mindestzahl auswertbarer Empfehlungen · Mindestzahl berechtigter Empfänger · Mindestdauer des Messfensters · Behandlung von Testkonten · Umgang mit Mehrfachübernahmen desselben Nutzers · Umgang mit gelöschten und moderierten Empfehlungen · getrennte Run-/Bike-Auswertung. **Es wird keine Mindestzahl geraten.** `blocked_gates` **[B]** · `blocked_activities` **[]**. Owner: MISSING (OQ-002). |
| OQ-015 | open-question | Vergleichbarkeitsdefinition für den Aktivitätsvergleich (REQ-040) | `docs/decisions/open-questions.md` | **open** | 2026-07-19 | — | — | **Neu reserviert im Auftau-Schritt 2 (2026-07-19).** Die Nutzerentscheidung verlangt, dass der Vergleich definiert: wann zwei Strecken als **vergleichbar** gelten · tolerierte Abweichung · welche Kennzahlen verglichen werden · Behandlung verkürzter, verlängerter oder abgebrochener Aktivitäten · **keine irreführende Bestzeit bei nicht vergleichbarer Geometrie**. Run und Bike strikt getrennt. Bis zur Entscheidung bleibt die Vergleichslogik **RESEARCH_HYPOTHESIS bzw. MISSING**; AC-040 und EV-040 sind ohne sie nicht vollständig spezifizierbar. `blocked_gates` **[A2]** · `blocked_activities` **[implementation]**. Owner: MISSING (OQ-002). |
| OQ-016 | open-question | Referenz-Fremdanwendung für den GPX-Kompatibilitätsnachweis (REQ-039) | `docs/decisions/open-questions.md` | **open** | 2026-07-19 | — | — | **Neu reserviert im Auftau-Schritt 2 (2026-07-19).** AC-039 verlangt, dass die exportierte Datei „in **mindestens einer definierten** kompatiblen Fremd-App" geöffnet werden kann. Welche App das ist, legt **kein Artefakt** fest — ohne Festlegung ist das Kriterium nicht reproduzierbar prüfbar. Es wird **keine App geraten**. `blocked_gates` **[A2]** · `blocked_activities` **[field-test]**. Owner: MISSING (OQ-002). |
| OQ-011 | open-question | Ablageort und Deployment-Ziel des A0-Routing-Proxys im Repository | `docs/decisions/open-questions.md` | resolved | 2026-07-19 | — | — | ENTSCHIEDEN durch den Nutzer am 2026-07-19: Ablageort ist `infra/routing-proxy/`, ausdrücklich NICHT `backend/` (begrenzte, austauschbare Infrastrukturkomponente; `backend/` bleibt für Stufe B reserviert). Laufzeit A0: AWS Lambda + API Gateway, Region eu-central-1, Provider-Key nur serverseitig, Rate Limit, Timeout, Kill Switch — nur dokumentiert, nicht gebaut. Abgebildet in CAN-096 und CAN-097. NACHZUG ERFORDERLICH (Phase 3, Owner von docs/decisions/open-questions.md): Das Register führt OQ-011 noch als offen mit Source Type OPEN QUESTION; diese Registry ändert das Register nicht. |

### 6.11 CONTRA — Widerspruchs-Ledger

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| CONTRA-001 | contradiction | `CLAUDE.md` benannte `docs/superpowers/plans/2026-07-10-REVYR-GESAMTPLAN-FINAL.md`, `docs/REVYR-Vision-Canvas-PRD.md` und `docs/REVYR-Plan-PRD.md` al… | `docs/decisions/decision-log.md` | resolved | 2026-07-19 | — | — | Ledger-Status: resolved (2026-07-19). Ein Widerspruch wird nur durch eine vom Nutzer bestätigte Auflösung geschlossen, nicht durch Agent-Konsens. |
| CONTRA-002 | contradiction | REQ-006/007 (Routenplanung) liegen in A0; NFR-007 verbietet Secrets im Client; `CLAUDE.md` wies `EXPO_PUBLIC_ORS_API_KEY` an. DEC-005 kannte die Extr… | `docs/decisions/decision-log.md` | resolved | 2026-07-19 | — | — | Ledger-Status: resolved (2026-07-19). Ein Widerspruch wird nur durch eine vom Nutzer bestätigte Auflösung geschlossen, nicht durch Agent-Konsens. |
| CONTRA-003 | contradiction | Dieselbe `OQ-`ID bezeichnete in Canvas/PRD, Vision und `open-questions.md` unterschiedliche Entscheidungen (z. B. OQ-003 = Karten/Routing vs. Owner/D… | `docs/decisions/decision-log.md` | resolved | 2026-07-19 | — | — | Ledger-Status: resolved (2026-07-19). Ein Widerspruch wird nur durch eine vom Nutzer bestätigte Auflösung geschlossen, nicht durch Agent-Konsens. |
| CONTRA-004 | contradiction | **REQ-024 ↔ REQ-034 / CAN-007.** Serverseitige Anti-Cheat-Plausibilität setzt Rohsensordaten voraus, die REQ-034 nur „bei nachgewiesener Notwendigkei… | `docs/decisions/decision-log.md` | resolved | 2026-07-19 | — | — | Status auf `resolved` gesetzt am 2026-07-19 (Auftau-Schritt): entschieden durch **DEC-011** (Nutzerentscheidung 2026-07-19). `resolved` bezeichnet die **entschiedene Grundsatzfrage**, nicht den erbrachten Nachweis — dieser läuft auf `evidence_status`, siehe §6.11.1. Damit ist die Divergenz C6b gegenüber `docs/decisions/decision-log.md` aufgelöst. Keine Selbstbestätigung: die Entscheidung stammt vom Nutzer, nicht von der Assistenz. |
| CONTRA-005 | contradiction | **REQ-027 ↔ REQ-017 / NFR-006.** „Unveränderliche Historie" (Snapshots, Trophäen, Zeitreise, Vereinsheim) kollidiert mit „vollständiger In-App-Accoun… | `docs/decisions/decision-log.md` | resolved | 2026-07-19 | — | — | Status auf `resolved` gesetzt am 2026-07-19 (Auftau-Schritt): entschieden durch **DEC-012** (Nutzerentscheidung 2026-07-19). `resolved` = Grundsatzfrage entschieden, nicht Nachweis erbracht; siehe §6.11.1. Divergenz C6b gegenüber dem Ledger aufgelöst. |
| CONTRA-006 | contradiction | **REQ-034 ab A0.** Der bestätigte A0-Routing-Proxy verarbeitet Start- und Wegpunktkoordinaten serverseitig, während Canvas/CAN-011 A0 als lokale Stuf… | `docs/decisions/decision-log.md` | resolved | 2026-07-19 | — | — | Status auf `resolved` gesetzt am 2026-07-19 (Auftau-Schritt): entschieden durch **DEC-013** und die Nutzerentscheidung zu OQ-011. Der frühere Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` ist als `status` **unzulässig** (§3.1) und wurde auf die beiden Achsen aufgeteilt: `status = resolved`, `evidence_status = pending`, `blocking = true`. Siehe §6.11.1. |

#### 6.11.1 Statusmodell je CONTRA-ID (Felder nach §3.1)

`blocking` ist **abgeleitet** nach der Formel in §3.1 und am jeweils eigenen `evidence_gate`
ausgewertet. Der Wert ist nicht hartkodiert und darf nicht als ID-spezifische Sonderregel in ein
Prüfwerkzeug übernommen werden.

**Feldwechsel im Auftau-Schritt 2 (2026-07-19):** `blocking_scope` ist ersatzlos entfallen und
durch die zwei disjunkten Felder `blocked_gates` und `blocked_activities` ersetzt (§3.1, C16).
Die Werte sind **verlustfrei** übernommen: jeder Alt-Wert war eine Tätigkeit und steht jetzt in
`blocked_activities`; `blocked_gates` ist **neu befüllt** und war vorher überhaupt nicht
darstellbar — das ist exakt der behobene Defekt. `none` ist als Wert entfallen und wird durch die
leere Liste `[]` ausgedrückt.

| id | status | resolution_status | evidence_status | blocking (abgeleitet) | blocked_gates | blocked_activities | evidence_gate | decision_reference | evidence_reference |
|---|---|---|---|---|---|---|---|---|---|
| CONTRA-001 | resolved | accepted | not-required | **false** | `[]` | `[]` | — | CONTRA-001 (Ledger), `CLAUDE.md`-Korrektur | — |
| CONTRA-002 | resolved | accepted | pending | **true** | `[A0]` | `[implementation, release]` | A0 | DEC-005 (`user-confirmed`), CONTRA-002 (Ledger), SRC-006 | ASM-103 (Bundle-Scan ohne Routing-Key + Proxy-Integrationstest), EV-034 |
| CONTRA-003 | resolved | accepted | pending | **true** | `[]` | `[documentation]` | — | CONTRA-003 (Ledger), `docs/decisions/open-questions.md` als kanonisches Register | **MISSING** — siehe Begründung unten |
| CONTRA-004 | resolved | accepted | pending | **true** | `[C, D]` | `[competition-release, territory-release]` | C | DEC-011 | EV-024, EV-034 (teilweise) |
| CONTRA-005 | resolved | accepted | pending | **true** | `[B]` | `[database-schema-finalization, account-release]` | B | DEC-012 | EV-017, EV-027 (teilweise), **EV-042** (neu 2026-07-19, für „Datenmodell trennt Identität und historische Aggregate") |
| CONTRA-006 | resolved | accepted | pending | **true** | `[A0]` | `[field-test, release]` | A0 | OQ-011, DEC-013, **ADR zum A0-Routing-Proxy = MISSING** | EV-006, EV-034; A0-Routing-Evidence (a)…(n) laut `docs/EVIDENCE-LEDGER.md` |

**Nachrechnung der `blocking`-Werte** (kanonische Formel aus §3.1, ausgewertet am jeweils eigenen
`evidence_gate`, ohne laufende Tätigkeit):

| id | `status != resolved` | `resolution_status != accepted` | `evidence_status IN [failed, blocked]` | `current_gate IN blocked_gates` | Ergebnis |
|---|---|---|---|---|---|
| CONTRA-001 | false | false | false | `—` nicht auswertbar | **false** |
| CONTRA-002 | false | false | false | `A0 ∈ [A0]` → **true** | **true** |
| CONTRA-003 | false | false | false | `—` nicht auswertbar; Tätigkeitsklausel `documentation` greift bei laufender Dokumentation | **true** |
| CONTRA-004 | false | false | false | `C ∈ [C, D]` → **true** | **true** |
| CONTRA-005 | false | false | false | `B ∈ [B]` → **true** | **true** |
| CONTRA-006 | false | false | false | `A0 ∈ [A0]` → **true** | **true** |

**Der Unterschied zur alten Formel ist nicht kosmetisch.** Unter `blocking_scope` hätte die
Gate-Klausel für CONTRA-002/004/005/006 gelautet „ist `A0` in `[implementation, release]`?" —
und damit **false** ergeben. Vier von sechs Widersprüchen wären am eigenen Gate als
nicht-blockierend erschienen. Die Werte in der Tabelle standen zwar schon vorher auf `true`,
waren aber **nicht** aus der Formel ableitbar; sie waren faktisch hartkodiert. Erst mit
`blocked_gates` stimmen Tabelle und Formel überein.

**`rationale` je Eintrag**

- **CONTRA-001** — Der Widerspruch war eine reine Dokumentinkonsistenz: `CLAUDE.md` benannte drei
  nicht existierende Plandateien und schrieb AsyncStorage fest. Die Auflösung *ist* die Korrektur
  des Dokuments; es gibt keine Laufzeit- oder Produkteigenschaft, die zusätzlich nachzuweisen
  wäre. Deshalb `evidence_status = not-required` — requirement-spezifisch begründet, nicht
  pauschal „nicht relevant".
- **CONTRA-002** — Die Kollision zwischen A0-Routenplanung und dem Secrets-Verbot aus NFR-007 ist
  durch die Entscheidung für einen serverseitigen Routing-Proxy ab A0 gelöst (DEC-005,
  `user-confirmed`). Der Nachweis „0 Routing-Provider-Keys im App-Bundle" setzt einen Build
  voraus; **es existiert kein Code**, also kann der Bundle-Scan nicht gelaufen sein.
- **CONTRA-003** — Die OQ-ID-Kollision ist durch die Festlegung eines einzigen kanonischen
  Registers gelöst. `evidence_reference` ist **MISSING**: `docs/decisions/decision-log.md`
  behauptet für diese Auflösung „maschinell geprüft: 1:1 ID↔Entscheidung", aber §9 dieser
  Registry hält fest, dass **kein ausführbares Prüfwerkzeug im Repository existiert**. Die
  behauptete maschinelle Prüfung hat damit kein reproduzierbares Artefakt. Der Nachweis wird
  hier **nicht** als erbracht geführt, nur weil ein Dokument ihn behauptet.
- **CONTRA-004** — Der Konflikt zwischen serverseitiger Anti-Cheat-Plausibilität und
  Datenminimierung ist durch DEC-011 gelöst: Rohsensorverläufe bleiben lokal, serverseitig
  laufen ausschließlich die in REQ-024 abschließend aufgezählten abgeleiteten
  Plausibilitätssignale. Ausstehend ist der Nachweis, dass der real gesendete Payload diesen
  Umfang einhält, und dass fehlende Sensoren nie automatisch zu `rejected` führen.
- **CONTRA-005** — Der Konflikt zwischen Historienerhalt und Accountlöschung ist durch DEC-012
  gelöst. Ausstehend ist der Nachweis wirksamer Anonymisierung **und** die technische Trennung
  von Identität und historischen Aggregaten. Letztere ist laut DEC-012 **vor** Finalisierung des
  Datenbankschemas herzustellen — daher `blocked_activities = [database-schema-finalization,
  account-release]`, obwohl REQ-027 selbst erst in Stufe D liegt. `blocked_gates = [B]` bildet
  ab, dass die Accountlöschung mit Gate B öffentlich wird. **Zusatzbefund erledigt:** für den
  Nachweis (z) „Datenmodell trennt Identität und historische Aggregate" führte
  `docs/EVIDENCE-LEDGER.md` ausdrücklich *keine* EV-ID. Im Auftau-Schritt 2 ist dafür **EV-042**
  vergeben (§6.7). Damit ist §8 Punkt 14 **als ID-Frage geschlossen**; der Nachweis selbst bleibt
  `blocked` (Retentionsfristen MISSING, OQ-009).
- **CONTRA-006** — Die Kollision zwischen Local-first und serverseitigem Routing ist durch die
  Entscheidung für einen transienten, datenminimierten EU-Routing-Proxy gelöst; der Nachweis der
  Privacy-, Logging-, Retention- und Security-Eigenschaften steht aus. `decision_reference`
  nennt laut Nutzervorgabe einen „ADR zum A0-Routing-Proxy" — **ein solches Artefakt existiert im
  Repository nicht** (`find docs -iname "*adr*"` liefert am 2026-07-19 nichts; ADR erscheint nur
  als Absichtserklärung in CAN-089, DEC-005 und dem Delivery-Plan). Der Verweis wird als
  **MISSING** geführt und **nicht** durch ein erfundenes Dokument ersetzt.

**Was dieser Schritt ausdrücklich nicht tut.** Kein Eintrag wird auf `verified` gesetzt. Kein
Eintrag wird von der Assistenz bestätigt. `resolution_status = accepted` bildet ab, dass die
**Nutzerentscheidung vom 2026-07-19** vorliegt (protokolliert in `docs/decisions/decision-log.md`
und `docs/SOURCE-MAP.md` als SRC-006) — es ist **keine** Selbstbestätigung durch einen Agenten.
Der Gesamtstatus des Laufs bleibt `BLOCKED_TRACEABILITY`, bis der Nutzer die Canvas-Items
bestätigt hat.

**Wirkung auf Prüfkriterium C6b.** `docs/validation/validation-report.md` führt C6b
(Statusgleichlauf Registry ↔ Widerspruchs-Ledger) als **FAIL**, weil die Registry CONTRA-004/005
als `open` führte, während der Ledger sie als entschieden führte. Nach dieser Änderung besteht
zwischen beiden Dateien **keine Statusdivergenz** mehr: alle sechs CONTRA-IDs stehen in Registry
und Ledger auf „entschieden", und der zuvor vermischte Nachweisstand steht getrennt auf
`evidence_status`. Den Ledger und den Validierungsbericht zieht **Phase 2** nach; diese Registry
ändert sie nicht. **Der Bericht darf C6b nicht selbst auf PASS setzen** — das ist Sache des
Owners von `docs/validation/validation-report.md` nach erneuter Prüfung beider Dateien.

### 6.12 USER — Personas (neu aufgenommen 2026-07-19, §5.1)

Bestand aus `docs/prd/revyr-endurance-platform.prd.md:32-34`, unverändert übernommen. **Keine
bestehende Persona wird umgedeutet.**

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| USER-001 | persona | Freizeit-Läufer:in | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Bedarf: zuverlässiges Tracking, verständlicher Fortschritt, lokale Trainingspartner. Source Type EXPLICIT via SRC-001 — **SRC-001 ist laut `docs/SOURCE-MAP.md` nicht auffindbar**; die Einstufung wird hier nur wiedergegeben, nicht bestätigt. Canvas-Anker CAN-023. |
| USER-002 | persona | Freizeit-/Rennradfahrer:in | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Bedarf: Geschwindigkeit, Höhen-/Sensordaten, Routen und faire Bike-Wertung. Source Type EXPLICIT via SRC-001/SRC-003 — beide **nicht auffindbar**. Canvas-Anker CAN-024. |
| USER-003 | persona | Lokale Sportgruppe oder Verein | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | Bedarf: Mitglieder, gemeinsame Aktivitäten, Organisation und langfristige Identität. Source Type EXPLICIT via SRC-001 — **nicht auffindbar**. Canvas-Anker CAN-026 und CAN-027. OPEN QUESTION (aus CAN-027): ob Vereine (Rechtsträger) und lokale Communities (informell) zwei getrennte Personas brauchen, ist nicht entschieden. |
| USER-004 | persona | Ambitionierte Ausdauersportler:innen mit Wearables oder externen Sensoren | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-19 | — | — | **Neu vergeben im Auftau-Schritt 2 (2026-07-19).** **Die ID USER-004 wurde vor der Vergabe geprüft und ist frei** — das PRD führte nur USER-001…003, und `USER-004` kam im gesamten Repository nicht vor. Sie wurde **nicht** ungeprüft aus der Anweisung übernommen. **Beschreibung:** „Läufer:innen und Radfahrer:innen, die regelmäßig trainieren, bereits eine Sportuhr, einen Herzfrequenzgurt oder Fahrradsensoren verwenden und erwarten, dass vorhandene Trainingssignale ohne Medienbruch in ihre Aktivitäts- und Belastungsauswertung einfließen." **Source Type ASSUMPTION** bis die Persona bestätigt ist. Schließt §8 Punkt 5 (Canvas-Zielgruppe CAN-025 ohne PRD-USER-ID) **als ID-Frage**. Canvas-Anker **CAN-025**. **REQ-032 wird primär verankert an:** USER-004, CAN-022 und ein Vision-Item zu vollständigen und erklärbaren Trainingsdaten (**MISSING** — kein VIS-Item trägt diese Aussage, siehe §8). **REQ-009 und REQ-011 werden semantisch auf eine mögliche Verknüpfung mit USER-004 geprüft — KEINE automatische Universalverknüpfung.** Die Prüfung ist Phase 2/3 und wird hier nicht vorweggenommen; `docs/traceability.md` vermerkt für beide bisher nur „ambitionierte Persona MISSING im PRD". PRD-Nachzug offen (Regel 10, §7.4). |

### 6.13 NFR — Nicht-funktionale Anforderungen (neu aufgenommen 2026-07-19, §5.1)

Bestand aus `docs/prd/revyr-endurance-platform.prd.md:215-222`, unverändert übernommen. **Keine
NFR wird umgedeutet, keine neue vergeben.** Die Spalten `source_type` und `evidence_status`
geben die Einstufung aus `docs/traceability.md` §6.7 wieder.

| id | type | title | canonical_file | status | created_at | deprecated_at | replacement_id | notes |
|---|---|---|---|---|---|---|---|---|
| NFR-001 | non-functional-requirement | Distanzgenauigkeit | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | `source_type` ASSUMPTION · `evidence_status` pending · OPERATIONAL_QUALITY · GATE-A0. |
| NFR-002 | non-functional-requirement | Batterie | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | `source_type` ASSUMPTION · `evidence_status` pending · OPERATIONAL_QUALITY · GATE-A0. **CONTRADICTION (DIV-5):** das PRD führt NFR-002 als EXPLICIT und bezeichnet denselben Wert an anderer Stelle als „nicht empirisch belegt". |
| NFR-003 | non-functional-requirement | Zuverlässigkeit | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | `source_type` ASSUMPTION · `evidence_status` pending · OPERATIONAL_QUALITY · GATE-A0. |
| NFR-004 | non-functional-requirement | Performance | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | `source_type` **BLOCKER** · `evidence_status` blocked · OPERATIONAL_QUALITY · GATE-A0 / GATE-D. **Es existiert kein Zielwert** — keine Millisekunden-, Bildraten- oder Perzentilschwelle. Schwächster der acht. |
| NFR-005 | non-functional-requirement | Accessibility | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | `source_type` ASSUMPTION · `evidence_status` pending · COMPLIANCE_CONTROL · GATE-A0 bis GATE-A2. Trägt REQ-037. **Teilweise präzisiert:** die WCAG-Fassung fehlte („WCAG AA" ohne Version); die Nutzerentscheidung vom 2026-07-19 beziffert sie in CAN-099/REQ-037 als **2.2**. Der PRD-Nachzug ist Phase 2/3. |
| NFR-006 | non-functional-requirement | Datenschutz | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | `source_type` **BLOCKER** · `evidence_status` blocked · COMPLIANCE_CONTROL · GATE-A0 bis GATE-E. Kern durch DEC-012/DEC-013 belegt; Retentionsfristen MISSING (OQ-009); „EU-orientiertes Hosting" als Zielwert nicht prüfbar (DIV-6). |
| NFR-007 | non-functional-requirement | Sicherheit | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | `source_type` **EXPLICIT (klauselbeschränkt)** · `evidence_status` pending · COMPLIANCE_CONTROL · GATE-A0 bis GATE-E. Einziger belegter EXPLICIT-Zielwert im NFR-Bestand, und zwar **nur** für die Klausel „keine Secrets im Client" (DEC-005 `user-confirmed`, CAN-092, SRC-006). Referenziert von DEC-005, ASM-103, CAN-092. |
| NFR-008 | non-functional-requirement | Wartbarkeit | `docs/prd/revyr-endurance-platform.prd.md` | active | 2026-07-18 | — | — | `source_type` **MISSING** · `evidence_status` **not-planned** · PROCESS_CONTROL · `evidence_gate` **MISSING**. **Kein `blocking`, kein `blocked_gates`, kein `blocked_activities`** — der `NFR-`Raum führt diese Felder nicht (§3.1, §6.13.2). Aussage: „TypeScript strict, reine Domainmodule, versionierte Schemas, automatisierte Tests." **NICHT deprecated** — Begründung in §6.13.1. Offene Messdefinition: **OQ-013**. **DIVERGENZ (§8 Punkt 42):** `prd.md:311` führt für NFR-008 `source_type` **EXPLICIT**; diese Registry führt **MISSING**. Nach §1 gilt die Registry; der PRD-Nachzug ist Phase 2/3. |

#### 6.13.1 NFR-008 — Entscheidung: definieren statt deprecaten

Die Nutzervorgabe verlangte eine der beiden Auflösungen und nannte drei Vorfragen. Sie sind
einzeln beantwortet:

| Vorfrage | Befund |
|---|---|
| Fachlich notwendige NFR? | **Ja.** Die vier Zusagen — TypeScript strict, reine Domainmodule, versionierte Schemas, automatisierte Tests — sind in `CLAUDE.md` und im Gesamtplan **projektweit verbindliche Arbeitsregeln** (u. a. „TDD ist mandatory", „TypeScript strict", `src/domain/` als „pure, dependency-free logic"). Die Substanz existiert und wird gelebt; ihr fehlt nur die Messdefinition. |
| Durch ein anderes NFR dupliziert? | **Nein.** NFR-001…003 messen Betriebsqualität (Genauigkeit, Batterie, Zuverlässigkeit), NFR-004 Performance, NFR-005 Zugänglichkeit, NFR-006 Datenschutz, NFR-007 Sicherheit. **Keines** trifft eine Aussage über Codestruktur, Typsicherheit, Schemaversionierung oder Testautomatisierung. |
| Nur reservierte, nie definierte ID? | **Nein.** NFR-008 ist in `prd.md:222` mit vier konkreten inhaltlichen Zusagen **definiert**. Reserviert und leer ist etwas anderes. |

**Entscheidung: NFR-008 wird NICHT deprecated.** Eine Anforderung mit realem, nicht dupliziertem
Inhalt zu deprecaten, weil ihre *Messung* fehlt, würde vorhandene Projektsubstanz löschen und die
vier Zusagen aus der Nachweispflicht entfernen. Das wäre die schlechtere der beiden Optionen.

**Was dieser Schritt NICHT tut:** Metrik, Einheit, Schwellwert, Messfenster, Testmethode, Owner
und Gate werden **nicht** vergeben. Alle sieben sind aus keinem Artefakt ableitbar. Insbesondere
wird **keine Testabdeckungsquote gesetzt** — die in `CLAUDE.md` genannten 80 % sind eine globale
Arbeitsregel des Nutzers, kein für dieses Produkt beschlossener NFR-Zielwert, und die Beweislatte
für `EXPLICIT` (§ PRD) verbietet, eine qualitative Absicht in einen quantitativen Zielwert
umzudeuten. Diese sieben Punkte sind **OQ-013**.

**Verwaisung.** Der Auftrag verlangt, dass NFR-008 nicht gleichzeitig verwaist ist und als aktive
Anforderung gezählt wird. Beides ist adressiert:

1. **Nicht mehr verwaist.** NFR-008 wird ab jetzt von dieser Registry (§6.13), von OQ-013 und von
   den Migrationstabellen §7.4/§7.5 referenziert. Die Zeichenfolge kam vorher im gesamten
   Repository **genau einmal** vor — in ihrer eigenen Definitionszeile.
2. **Nicht als erfüllte Anforderung gezählt.** NFR-008 zählt in §10 in der `NFR-`Zeile, **nicht**
   in der Zahl aktiver Requirements (das sind ausschließlich `REQ-`IDs, Regel 11). Sie steht auf
   `evidence_status = not-planned` und hat **kein** Gate (`evidence_gate = MISSING`).

**Die Entscheidung „nicht deprecaten" bleibt in Runde 4 unverändert bestehen.** Alle drei
Vorfragen wurden erneut geprüft; keine Antwort hat sich geändert. Was sich ändert, ist
ausschließlich die **Statusdarstellung** — siehe §6.13.2.

#### 6.13.2 NFR-008 — Runde 4 (2026-07-20): der `NFR-`Raum führt kein `blocking`

**Der Befund.** Die Nutzervorgabe verlangte, dass NFR-008 kein `blocking` trägt, das gesetzt oder
aus einem Tabellenwert übernommen wird, und stellte zwei Auflösungen zur Wahl: die kanonischen
Achsen für `NFR-` aufnehmen **oder** `NFR-`Einträge gar kein `blocking` führen lassen. Der Anlass
ist belegt: `prd.md:302-311` führt eine Spalte `blocking` mit **acht** hartkodierten Werten
(sieben `true`, für NFR-008 `false`). Zusammen mit den sechs `CONTRA-`Werten sind das 14
`blocking`-Werte im Projekt, von denen die **acht NFR-Werte niemand nachrechnet** — es gibt für
sie keine Formel, keine Eingabe und keinen Wertebereich. §6.13.1 selbst schrieb NFR-008
zusätzlich `blocked_gates = []` / `blocked_activities = []` und ein `blocking = false` zu, obwohl
§3.1 diese Achsen ausdrücklich nur für `OQ-` und `CONTRA-` definiert.

**Entscheidung: `NFR-`Einträge führen kein `blocking`.** Die Achsen werden **nicht** auf `NFR-`
ausgedehnt.

| Prüfung | Ergebnis |
|---|---|
| Passt die Achse `status` (`open`/`resolved`) auf ein NFR? | **Nein.** Sie beantwortet „Ist die Grundsatzfrage **entschieden**?" — eine Frage, die nur ein Widerspruch oder eine offene Frage hat. Ein NFR ist keine Entscheidung, sondern eine Anforderung; es benutzt die §3-Achse `active`/`deprecated`/`reserved`. |
| Was liefert die Formel, wenn man sie trotzdem anwendet? | **Für alle acht NFRs `blocking = true`** — denn `active NOT IN [resolved]` ist immer wahr. Das Ergebnis wäre syntaktisch gültig, mechanisch reproduzierbar und **fachlich bedeutungslos**: genau das Muster, gegen das §1 und §9 warnen. |
| Passt `resolution_status` (`undecided`/`decision-documented`/`accepted`)? | **Nein.** Ein Reifegrad einer Entscheidung; für ein NFR ohne Entscheidungsvorgang nicht besetzbar, ohne einen Wert zu **erfinden**. |
| Braucht es eine Metamodell-Erweiterung? | **Nein** — und deshalb wird keine vorgenommen. Die tragende Information ist bereits im eingefrorenen Modell darstellbar: **welches Gate** die Anforderung einfordert, steht in `evidence_gate`; **wie weit** der Nachweis ist, in `evidence_status` (§3.2, projektweit gültig). Für NFR-008 sind das `MISSING` und `not-planned`. |

**Folge für die Darstellung.** Aus §6.13.1 sind die Zuschreibungen `blocked_gates = []`,
`blocked_activities = []` und `blocking = false` entfernt. Der frühere Satz „`blocking = false`
ist hier kein Entwarnungssignal" fällt damit weg — er hat einen Wert erklärt, den es nicht geben
darf. **Der Befund, den er beschrieb, bleibt unverändert und wird jetzt ohne Hilfsfeld gesagt:**

> NFR-008 wird an **keiner Stelle wirksam**. `evidence_gate` ist **MISSING** — kein Gate fordert
> die Anforderung ein. `evidence_status` ist **not-planned** — es existiert kein Messkonzept.
> Es existiert keine CI, die die vier Zusagen durchsetzen könnte. Die Anforderung ist inhaltlich
> real und operativ folgenlos. Das bleibt so bis **OQ-013**.

**Folge für den PRD.** Die Spalte `blocking` in `prd.md:302-311` ist **zu entfernen**, nicht
umzurechnen: für `NFR-` gibt es keine Formel, aus der sich ein Wert ableiten ließe. Ein
verbleibender Wert wäre per Definition ein Wert, den niemand nachrechnet. Das ist ein
Nachzugsauftrag an den PRD-Owner (§7.5, §8 Punkt 34).

## 7. Alias- und Migrationstabellen

Diese Tabellen sind für Phase 3 gedacht: alt → neu, je Datei, mechanisch nachziehbar.
**Die Datei-Owner ziehen nach, nicht diese Registry.**

### 7.1 ASM-Migration (alt → neu, je Datei)

| Alt-ID | Datei | Neue ID | Bedeutung, die gemeint war |
|---|---|---|---|
| ASM-001 | `docs/prd/revyr-endurance-platform.prd.md` | **ASM-101** | Aufteilung der v1.0 in A0/A1/A2 |
| ASM-002 | `docs/prd/revyr-endurance-platform.prd.md` | **ASM-102** | SQLite statt AsyncStorage |
| ASM-003 | `docs/prd/revyr-endurance-platform.prd.md` | **ASM-103** | A0-Routing über serverseitigen Proxy |
| ASM-004 | `docs/prd/revyr-endurance-platform.prd.md` | **ASM-104** | Einzel-Reviere/Bahngold bis D deaktiviert |
| ASM-001 | `docs/vision/revyr-endurance-platform.vision.md` | **ASM-201** | Risikoreduktion durch gestufte v1.0 |
| ASM-002 | `docs/vision/revyr-endurance-platform.vision.md` | **ASM-202** | Health-Score mit sichtbarer Confidence |
| ASM-003 | `docs/vision/revyr-endurance-platform.vision.md` | **ASM-203** | Stabiler technischer Slug |

Vollständige Fundstellenliste (`grep -rn "ASM-" docs/`, ausgeführt am 2026-07-19; genau acht
Treffer in genau zwei Dateien):

| Datei | Zeile | Fundstelle | Alt-ID | Neue ID |
|---|---:|---|---|---|
| `docs/prd/revyr-endurance-platform.prd.md` | 52 | Tabelle „Assumptions“ | ASM-001 | ASM-101 |
| `docs/prd/revyr-endurance-platform.prd.md` | 53 | Tabelle „Assumptions“ | ASM-002 | ASM-102 |
| `docs/prd/revyr-endurance-platform.prd.md` | 54 | Tabelle „Assumptions“ | ASM-003 | ASM-103 |
| `docs/prd/revyr-endurance-platform.prd.md` | 55 | Tabelle „Assumptions“ | ASM-004 | ASM-104 |
| `docs/prd/revyr-endurance-platform.prd.md` | 78 | Tabelle „Open Questions“, Zeile OQ-004, Fließtextverweis | ASM-003 | ASM-103 |
| `docs/vision/revyr-endurance-platform.vision.md` | 79 | Tabelle „Assumptions“ | ASM-001 | ASM-201 |
| `docs/vision/revyr-endurance-platform.vision.md` | 80 | Tabelle „Assumptions“ | ASM-002 | ASM-202 |
| `docs/vision/revyr-endurance-platform.vision.md` | 81 | Tabelle „Assumptions“ | ASM-003 | ASM-203 |

Zeilennummern beziehen sich auf den Stand vom 2026-07-19 vor Phase 3 und sind als Hinweis
gedacht, nicht als Ersatz für einen erneuten `grep` durch den jeweiligen Datei-Owner.

### 7.2 Canvas-Facetten aus `docs/traceability.md` → atomare CAN-IDs

`docs/traceability.md` hat im Abschnitt „Feld-Definitionen und Facetten-IDs“ eigene
Facetten-Kennungen eingeführt (`CAN-001-a`, `CAN-003-v1`, …), die in keiner Registry standen —
genau die Ad-hoc-Vergabe, die Regel 3 künftig verbietet. Sie werden 1:1 abgelöst:

| Facette (alt) | Atomare CAN-ID (neu) |
|---|---|
| `CAN-001-a` | **CAN-013** |
| `CAN-001-b` | **CAN-014** |
| `CAN-001-c` | **CAN-015** |
| `CAN-003-p1` | **CAN-028** |
| `CAN-003-v1` | **CAN-029** |
| `CAN-003-v2` | **CAN-030** |
| `CAN-003-v3` | **CAN-031** |
| `CAN-003-v4` | **CAN-032** |
| `CAN-003-v5` | **CAN-033** |
| `CAN-009-a` | **CAN-124** |
| `CAN-009-b` | **CAN-125 + CAN-126** |
| `CAN-009-c` | **CAN-127 + CAN-128 + CAN-129** |

`CAN-009-b` und `CAN-009-c` bildeten je zwei bzw. drei unabhängig messbare Signale in einer
Facette ab und werden deshalb auf mehrere Atome abgebildet. Die Auswahl des richtigen Atoms je
REQ ist eine fachliche Entscheidung des Traceability-Owners in Phase 3 und wird hier **nicht**
vorweggenommen.

### 7.3 Legacy-Canvas-Items → atomare Items

**Stand 2026-07-20 (Runde 4).** Diese Tabelle war gegenüber §7.4.1 **veraltet und widersprüchlich**
und ist hier angeglichen. Behobene Abweichungen: (a) CAN-022, CAN-099 und CAN-130 standen noch als
„reservierte Lücke", obwohl sie seit dem 2026-07-19 **aktiv** sind; (b) CAN-071 stand als
„reservierte Lücke", obwohl es **deprecated mit drei Nachfolgern** ist — ein deprecatetes Item ist
keine offene Reserve; (c) die Nachfolgerspalten führten **CAN-138 … CAN-141** überhaupt nicht,
obwohl §7.4.1/§7.4.2 sie als Nachfolger bzw. Neuvergabe ausweisen. Aktueller Stand der
reservierten, inhaltlich MISSING gebliebenen Items: **sechs** (CAN-016 … CAN-021), nicht zehn.

| Alt-ID | Abschnitt | Atomare Nachfolger | Reservierte Lücke (Inhalt MISSING) |
|---|---|---|---|
| CAN-001 | Problem | **CAN-013 … CAN-015** (3) · **CAN-022** (aktiv seit 2026-07-19) | **CAN-016 … CAN-021** (6) |
| CAN-002 | Users / Customers | **CAN-023 … CAN-027** (5) | — |
| CAN-003 | Value Promise | **CAN-028 … CAN-038** (11) | — |
| CAN-004 | Current Alternatives | **CAN-039 … CAN-046** (8) | — |
| CAN-005 | Key Capabilities | **CAN-047 … CAN-070** (24) · **CAN-138, CAN-139** (2, aus CAN-071) · **CAN-142, CAN-143** (2, aus CAN-140) | — (CAN-071 ist **deprecated**, keine Reserve; CAN-140 ebenfalls) |
| CAN-006 | Non-Goals | **CAN-072 … CAN-079** (8) | — |
| CAN-007 | Constraints | **CAN-080 … CAN-098** (19) · **CAN-099** (aktiv seit 2026-07-19) · **CAN-141** (neu 2026-07-19) | — |
| CAN-008 | Risks | **CAN-100 … CAN-110** (11) | — |
| CAN-009 | Success Signal | **CAN-124 … CAN-129** (6) · **CAN-130** (aktiv seit 2026-07-19) | — |
| CAN-010 | Evidence | **CAN-111 … CAN-123** (13) | — |
| CAN-011 | Allowed Scope | **CAN-131 … CAN-137** (7) | — |
| CAN-012 | Unresolved Questions | keine — ersatzlos, Referenzen zeigen auf OQ-IDs | — |

**Zwischengeschaltete Deprecations** (Items, die selbst schon Nachfolger waren):

| Alt-ID | Herkunft | Nachfolger | Stand |
|---|---|---|---|
| CAN-071 | CAN-005 | CAN-138, CAN-139, **CAN-140** | CAN-140 seinerseits **deprecated** (Runde 4) → CAN-142, CAN-143 |
| CAN-140 | CAN-071 | **CAN-142, CAN-143** | Runde 4, 2026-07-20 |

### 7.4 Migration Auftau-Schritt 2 (2026-07-19)

Maschinenlesbare Fassung:
`scratchpad/id-migration.json`. Diese Tabelle und die JSON-Datei
müssen übereinstimmen; bei Abweichung gilt diese Registry (§1).

#### 7.4.1 Deprecations (alt → neu)

| Alt-ID | Typ | deprecated_at | replacement_id | Grund |
|---|---|---|---|---|
| CAN-071 | canvas-item / capability | 2026-07-19 | **CAN-138, CAN-139, CAN-140** | Composite aus drei Capabilities auf zwei Release-Stufen |
| REQ-014 | requirement | 2026-07-19 | **REQ-037, REQ-038** | Composite aus Accessibility und Designsystem |
| AC-014 | acceptance-criterion | 2026-07-19 | **AC-037, AC-038** | folgt REQ-014 |
| EV-014 | evidence | 2026-07-19 | **EV-037, EV-038** | folgt REQ-014; zwei Nachweisverfahren in einer ID |
| TRC-014 | traceability-row | 2026-07-19 | **TRC-037, TRC-038** | folgt REQ-014; Zeile referenzierte drei deprecatete IDs |

**Alt-IDs werden nie wiederverwendet** (Regel 6). CAN-071, REQ-014, AC-014, EV-014 und TRC-014
bleiben für immer belegt.

#### 7.4.2 Neu reservierte IDs

| Neue ID | Typ | Titel | Zweck |
|---|---|---|---|
| VIS-012 | vision-item (**reserved**, MISSING) | Designprinzip auf Vision-Ebene | Vision-Anker für REQ-038 — Inhalt braucht Nutzerentscheidung |
| VIS-013 | vision-item (**reserved**, MISSING) | Datenportabilität auf Vision-Ebene | Vision-Anker für REQ-039 — Inhalt braucht Nutzerentscheidung |
| CAN-138 | canvas-item / capability | Verlauf und Detailansicht | Nachfolger 1/3 von CAN-071; Stufe A0; trägt REQ-008 |
| CAN-139 | canvas-item / capability | GPX-Export | Nachfolger 2/3 von CAN-071; Stufe A2; trägt REQ-039 |
| CAN-140 | canvas-item / capability | Streckenwiederverwendung und Vergleich | Nachfolger 3/3 von CAN-071; Stufe A2; trägt REQ-040 |
| CAN-141 | canvas-item / constraint | Monochromes tokenbasiertes Designsystem | Canvas-Anker für REQ-038; schließt die zweite REQ-014-Canvas-Lücke |
| REQ-037 | requirement | Accessibility | Nachfolger 1/2 von REQ-014 |
| REQ-038 | requirement | Monochromes tokenbasiertes Designsystem | Nachfolger 2/2 von REQ-014 |
| REQ-039 | requirement | GPX-Export abgeschlossener Aktivitäten | eigene Capability; REQ-034 nur sekundär |
| REQ-040 | requirement | Streckenwiederverwendung und Aktivitätsvergleich | aus REQ-008 herausgelöst; keine bestehende REQ deckt sie ab |
| AC-037 | acceptance-criterion | zu REQ-037 | Nachfolger 1/2 von AC-014 |
| AC-038 | acceptance-criterion | zu REQ-038 | Nachfolger 2/2 von AC-014 |
| AC-039 | acceptance-criterion | zu REQ-039 | GPX-Abnahmebedingungen (a)–(h) |
| AC-040 | acceptance-criterion | zu REQ-040 | Vergleichs-Abnahmebedingungen |
| AC-041 | acceptance-criterion | zu **REQ-019** (Messkriterium) | Abspaltung aus AC-019; Begründung §6.5.1 |
| EV-037 | evidence | zu REQ-037 | Nachfolger 1/2 von EV-014 |
| EV-038 | evidence | zu REQ-038 | Nachfolger 2/2 von EV-014 |
| EV-039 | evidence | zu REQ-039 | GPX-Export-Test je Sportart |
| EV-040 | evidence | zu REQ-040 | Vergleichstest inkl. Negativtests |
| EV-041 | evidence | zu REQ-019 / AC-041 / CAN-130 | Berechenbarkeit der Übernahme-Kennzahl |
| EV-042 | evidence | zu CONTRA-005 / REQ-017 / REQ-027 | Trennung Identität ↔ historische Aggregate; schließt §8 Punkt 14 als ID-Frage |
| TRC-037 | traceability-row | VIS-011 ↔ CAN-099 ↔ REQ-037 ↔ AC-037 ↔ EV-037 | Nachfolger 1/2 von TRC-014 |
| TRC-038 | traceability-row | VIS-012 ↔ CAN-141 ↔ REQ-038 ↔ AC-038 ↔ EV-038 | Nachfolger 2/2 von TRC-014; **broken**, Vision-Anker MISSING |
| TRC-039 | traceability-row | VIS-013 ↔ CAN-139 ↔ REQ-039 ↔ AC-039 ↔ EV-039 | **broken**, Vision-Anker MISSING |
| TRC-040 | traceability-row | VIS-003 ↔ CAN-140 ↔ REQ-040 ↔ AC-040 ↔ EV-040 | Vision-Anker ist eine zu prüfende ASSUMPTION |
| USER-004 | persona | Ambitionierte Ausdauersportler:innen mit Wearables oder externen Sensoren | Persona für CAN-025 / REQ-032; ID vor Vergabe als frei geprüft |
| OQ-012 | open-question | Privacy-minimierte Telemetrie für Routenempfehlungen | ausdrückliche Nutzervorgabe; blockiert Gate B |
| OQ-013 | open-question | Messdefinition und Gate für NFR-008 | Folge der Entscheidung, NFR-008 nicht zu deprecaten |
| OQ-014 | open-question | Stichproben- und Auswertungsregel für CAN-130 | vom Nutzer aufgezählt; blockiert Gate B |
| OQ-015 | open-question | Vergleichbarkeitsdefinition für REQ-040 | vom Nutzer aufgezählt; blockiert A2 |
| OQ-016 | open-question | Referenz-Fremd-App für den GPX-Nachweis | AC-039 (d) sonst nicht prüfbar |

#### 7.4.3 Statusänderungen ohne neue ID

| ID | Alt | Neu | Grund |
|---|---|---|---|
| CAN-022 | `reserved`, Inhalt MISSING | `active`, Inhalt entschieden | Nutzerentscheidung 2026-07-19 (nur Datenqualitätsproblem; Komfortaspekt ausdrücklich nicht enthalten) |
| CAN-099 | `reserved`, Inhalt MISSING | `active`, Inhalt entschieden | Nutzerentscheidung 2026-07-19; **ab jetzt ausschließlich Accessibility** |
| CAN-130 | `reserved`, Inhalt MISSING | `active`, Inhalt entschieden | Nutzerentscheidung 2026-07-19; Vollspezifikation §6.3.2 |
| REQ-008 | Verlauf + Wiederverwendung + Export | **verengt** auf Verlauf und Detailansicht | Export → REQ-039, Vergleich → REQ-040 |
| AC-008 | inkl. „exportierbar" | **verengt**; Run/Bike getrennt zu prüfen | folgt REQ-008 |
| AC-019 | ein gemischtes Kriterium | **verengt** auf das funktionale Kriterium | Messkriterium → AC-041 |
| OQ-011 | `open` | `resolved` (bereits Schritt 1) | unverändert; hier nur zur Vollständigkeit |

#### 7.4.4 Nachzugsfenster (zulässige Waisen nach Regel 10)

Diese IDs stehen in der Registry, aber noch in **keinem** referenzierenden Dokument. Das ist die
von Regel 2 erzwungene Reihenfolge, kein Defekt. Ein Validator akzeptiert **ausschließlich diese**
als Waisen; jede weitere ist ein Fehler.

| ID | Nachzuziehendes Dokument | Owner |
|---|---|---|
| CAN-022, CAN-099, CAN-130, CAN-138, CAN-139, CAN-140, CAN-141 | `docs/canvas/revyr-endurance-platform.canvas.md` | Canvas-Owner, Phase 2/3 |
| REQ-037…040, AC-037…041, EV-037…042, USER-004 | `docs/prd/revyr-endurance-platform.prd.md` | PRD-Owner, Phase 2/3 |
| TRC-037…040 | `docs/traceability.md` | Traceability-Owner, Phase 2/3 |
| OQ-012…016 | `docs/decisions/open-questions.md` | Owner des Registers, Phase 2/3 |
| VIS-012, VIS-013 | `docs/vision/revyr-endurance-platform.vision.md` | **erst nach Nutzerentscheidung** — Inhalt MISSING |

**Deprecatete IDs sind aus den Dokumenten zu entfernen**, nicht nur hier: CAN-071, REQ-014,
AC-014, EV-014, TRC-014 werden von PRD, Canvas und Traceability noch referenziert. Das ist nach
Regel 3 (§9) ein Validierungsfehler, solange der Nachzug aussteht — er ist **bekannt und
terminiert**, nicht übersehen.

#### 7.4.5 Feld-Nachzug `blocking_scope` → `blocked_gates` / `blocked_activities`

Das Feld `blocking_scope` ist mit diesem Schritt **projektweit** entfallen. Es wird aber noch in
**sechs** Dateien außerhalb dieser Registry verwendet (Zählung `grep -c`, 2026-07-19):

| Datei | Vorkommen | Owner |
|---|---:|---|
| `docs/traceability.md` | 20 | Traceability-Owner |
| `docs/prd/revyr-endurance-platform.prd.md` | 14 | PRD-Owner |
| `docs/decisions/decision-log.md` | 9 | Owner Decision-Log |
| `docs/validation/validation-report.md` | 7 | Owner Validierungsbericht |
| `docs/EVIDENCE-LEDGER.md` | 1 | Owner Evidence Ledger |
| `docs/vision/revyr-endurance-platform.vision.md` | ≥ 1 | Vision-Owner |

**Diese Registry ändert keine dieser Dateien** — sie liegen außerhalb der Ownership dieses
Schritts. Der Nachzug ist **nicht kosmetisch**: solange ein Dokument `blocking_scope` führt und
ein Werkzeug die alte Formel darauf anwendet, liefert es für gegatete Einträge weiterhin
fälschlich `false` (§3.1). **Regel für den Nachzug:** jeder Alt-Wert ist eine Tätigkeit und
wandert nach `blocked_activities`; `blocked_gates` ist **neu zu befüllen** und war vorher nicht
darstellbar. Ein reines Umbenennen des Feldes behebt den Defekt **nicht**.

### 7.5 Migration Runde 4 (2026-07-20)

Maschinenlesbare Fassung: `scratchpad/id-migration-r4.json`. Diese Tabelle und die JSON-Datei
müssen übereinstimmen; bei Abweichung gilt diese Registry (§1).

#### 7.5.1 Deprecations (alt → neu)

| Alt-ID | Typ | deprecated_at | replacement_id | Grund |
|---|---|---|---|---|
| CAN-140 | canvas-item / capability | 2026-07-20 | **CAN-142, CAN-143** | Composite aus Planungs- und Auswertungsfunktion; unabhängig auslieferbar, unterschiedlich blockiert |
| REQ-040 | requirement | 2026-07-20 | **REQ-041, REQ-042** | folgt CAN-140; Composite aus Wiederverwendung und Vergleich |
| AC-040 | acceptance-criterion | 2026-07-20 | **AC-042, AC-043** | folgt REQ-040; eine Hälfte heute erfüllbar, die andere ohne OQ-015 nicht spezifizierbar |
| EV-040 | evidence | 2026-07-20 | **EV-043, EV-044** | folgt REQ-040; zwei Nachweise mit unterschiedlichem Blockierungszustand |
| TRC-040 | traceability-row | 2026-07-20 | **TRC-041, TRC-042** | folgt REQ-040; Zeile referenzierte vier deprecatete IDs, Vision-Anker galt nur für eine Hälfte |

**Alt-IDs werden nie wiederverwendet** (Regel 6). CAN-140, REQ-040, AC-040, EV-040 und TRC-040
bleiben für immer belegt.

#### 7.5.2 Neu reservierte IDs

| Neue ID | Typ | Titel | Zweck |
|---|---|---|---|
| VIS-014 | vision-item (**reserved**, MISSING) | Wiederverwendung geplanter Strecken auf Vision-Ebene | Vision-Anker für REQ-041 — Inhalt braucht Nutzerentscheidung. **Abweichung von der wörtlichen Auftragsliste**, begründet in §6.1 |
| CAN-142 | canvas-item / capability | Wiederverwendung einer gespeicherten Route | Nachfolger 1/2 von CAN-140 (Planungsfunktion); trägt REQ-041 |
| CAN-143 | canvas-item / capability | Vergleich fachlich vergleichbarer Aktivitäten | Nachfolger 2/2 von CAN-140 (Auswertungsfunktion); trägt REQ-042 |
| REQ-041 | requirement | Wiederverwendung einer gespeicherten Route | Nachfolger 1/2 von REQ-040 |
| REQ-042 | requirement | Vergleich fachlich vergleichbarer Aktivitäten | Nachfolger 2/2 von REQ-040 |
| AC-042 | acceptance-criterion | zu REQ-041 | Nachfolger 1/2 von AC-040 |
| AC-043 | acceptance-criterion | zu REQ-042 | Nachfolger 2/2 von AC-040 |
| EV-043 | evidence | zu REQ-041 / AC-042 / CAN-142 | Nachfolger 1/2 von EV-040 |
| EV-044 | evidence | zu REQ-042 / AC-043 / CAN-143 | Nachfolger 2/2 von EV-040 |
| TRC-041 | traceability-row | VIS-014 ↔ CAN-142 ↔ REQ-041 ↔ AC-042 ↔ EV-043 | Nachfolger 1/2 von TRC-040; **broken**, Vision-Anker MISSING |
| TRC-042 | traceability-row | VIS-003 ↔ CAN-143 ↔ REQ-042 ↔ AC-043 ↔ EV-044 | Nachfolger 2/2 von TRC-040; Vision-Anker ist eine zu prüfende ASSUMPTION |

**Keine neue OQ-ID.** OQ-015 (Vergleichbarkeitsdefinition) wandert vollständig auf REQ-042/CAN-143
und bleibt inhaltlich unverändert; OQ-016 (Referenz-Fremd-App) bleibt bei REQ-039. Es wurde
geprüft, ob der Befund zur entfallenen Fremd-App-Klausel (§8 Punkt 36) eine eigene OQ-ID braucht —
er wird als §8-Punkt geführt, weil er eine Scope-Frage zu einer bestehenden Entscheidung ist und
keine neue offene Entscheidung eröffnet.

#### 7.5.3 Wortlaut- und Typänderungen ohne neue ID

| ID | Alt | Neu | Grund |
|---|---|---|---|
| CAN-099 | Wortlaut Runde 3; Item Type `constraint` | **kanonischer Wortlaut A**; Item Type **CONSTRAINT / VALUE BOUNDARY**; Source Type **EXPLICIT** | Nutzerentscheidung 2026-07-20. Dasselbe Item trägt dieselbe Aussage → keine neue ID (§6.3.3) |
| CAN-141 | Wortlaut Runde 3; enthielt via Registry-Vermerk die generische Farbregel | **kanonischer Wortlaut B**; Item Type **DESIGN CONSTRAINT / PRODUCT PRINCIPLE**; generische Farbregel **entfernt** | Nutzerentscheidung 2026-07-20; Auflösung der doppelt geführten Pflicht |
| CAN-139 | „…exportieren **und in einer kompatiblen Fremdanwendung öffnen**"; Item Type `capability`; ASSUMPTION | **kanonischer Wortlaut C**; Item Type **VALUE PROMISE / CAPABILITY**; Source Type **EXPLICIT** | Nutzerentscheidung 2026-07-20; Fremd-App-Klausel entfällt aus dem Wortlaut → Befund §8 Punkt 36 |
| CAN-138 | „…eine Detailansicht mit **Strecke**, Dauer, Distanz … öffnen" | **kanonischer Wortlaut**: „…eine **ausgewählte Aktivität** mit **Route**, Dauer, Distanz … in einer Detailansicht öffnen"; **bleibt ungeteilt** | Nutzerentscheidung 2026-07-20; Teilungsprüfung negativ (fünf Gründe in §6.3) |
| EV-008 | „Repository-, UI- und **GPX-Kompatibilitätstest**." | Wortlaut **wörtlich aus `prd.md:731`**; **ausschließlich** Verlauf und Detailansicht | Die veraltete Registry-Definition hätte nach §1 gewonnen und den nach EV-039 ausgelagerten Nachweis doppelt geführt |
| EV-039 | — | **ausschließlich** GPX-Kompatibilitäts- und Exportnachweis | kanonische Trennung EV-008 / EV-039 |
| TRC-019 | VIS-**008** ↔ CAN-005 | **VIS-003** ↔ CAN-058 | semantisch falscher Vision-Anker (Fairness Boundary trägt keine Community-Aussage) |
| TRC-020 | VIS-**008** ↔ CAN-005 | **VIS-004** ↔ CAN-060 | dito; VIS-004 nennt „lokale Teams" wörtlich |
| TRC-021 | VIS-**008** ↔ CAN-005 | **VIS-004** ↔ CAN-060 | dito |
| TRC-022 | VIS-**008** ↔ CAN-005 | **VIS-003** ↔ CAN-067 | dito; VIS-004 geprüft und **verworfen** (§6.6) |
| NFR-001…008 | Feld `blocking` (8 hartkodierte Werte im PRD) | **Feld entfällt für den gesamten `NFR-`Raum** | §6.13.2 — kein Wert, den niemand nachrechnet |

#### 7.5.4 Nachzugsfenster Runde 4 (zulässige Waisen nach Regel 10)

Ergänzt §7.4.4. Ein Validator akzeptiert **ausschließlich** die dort und hier gelisteten IDs als
Waisen.

| ID | Nachzuziehendes Dokument | Owner |
|---|---|---|
| CAN-142, CAN-143 | `docs/canvas/revyr-endurance-platform.canvas.md` | Canvas-Owner, Phase 2/3 |
| REQ-041, REQ-042, AC-042, AC-043, EV-043, EV-044 | `docs/prd/revyr-endurance-platform.prd.md` | PRD-Owner, Phase 2/3 |
| TRC-041, TRC-042 | `docs/traceability.md` | Traceability-Owner, Phase 2/3 |
| VIS-014 | `docs/vision/revyr-endurance-platform.vision.md` | **erst nach Nutzerentscheidung** — Inhalt MISSING |

#### 7.5.5 Belegte Dokumentabweichungen — Nachzugsaufträge an die jeweiligen Owner

Diese Registry ändert **keine** dieser Dateien; sie liegen außerhalb der Ownership dieses
Schritts. Alle Fundstellen sind am 2026-07-20 verifiziert.

| Datei | Fundstelle | Befund | Nachzug |
|---|---|---|---|
| `docs/traceability.md` | `:1488` | REQ-037 → CAN-013 über die **verbotene Kette** „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" | Verknüpfung **entfernen**; Wert **MISSING** |
| `docs/traceability.md` | `:1546` | REQ-037 → CAN-029 über dieselbe Kette | Verknüpfung **entfernen**; Wert **MISSING** |
| `docs/traceability.md` | `:1547` | REQ-038 → CAN-029 über dieselbe Kette | Verknüpfung **entfernen**; kanonischer Anker ist CAN-141 |
| `docs/traceability.md` | `:1489` | REQ-038 → CAN-013 **und zugleich** „kein eigenes Problem-Item — begründete Nichtanwendbarkeit" | Widerspruch auflösen: Wert auf **MISSING (begründet)** |
| `docs/traceability.md` | `:1490` | REQ-039 → CAN-013 („Daten, die man nicht mitnehmen kann…") — dieselbe Defektklasse, im Feld bereits als MISSING selbst vermerkt | Verknüpfung **entfernen**, MISSING stehen lassen |
| `docs/traceability.md` | `:1491` | REQ-040 → CAN-013 („Vergleich erzeugt Bedeutung") — dieselbe Defektklasse; REQ-040 ist zusätzlich **deprecated** | Zeile auf REQ-041/REQ-042 aufteilen, CAN-013-Bezug **entfernen** |
| `docs/traceability.md` | `:465`, `:471` | REQ-008 führt **CAN-050** als Canvas-Anker; CAN-050 beansprucht in dieser Registry (§6.3) **REQ-006** | Anker auf **CAN-138** verengen, CAN-050 aus dem REQ-008-Kontext **entfernen** |
| `docs/prd/…prd.md` | `:993` | dieselbe CAN-050-Fehlzuordnung zu REQ-008 | dito |
| `docs/prd/…prd.md` | `:302-311` | Spalte `blocking` mit **acht** hartkodierten NFR-Werten | Spalte **entfernen** (§6.13.2) — nicht umrechnen |
| `docs/prd/…prd.md` | `:311` | NFR-008 `source_type` **EXPLICIT** gegen Registry **MISSING** | auf **MISSING** angleichen (§1) |
| `docs/implementation/revyr-delivery-plan.md` | `:93` **und** `:116` | das **deprecatete** REQ-014 wird an **zwei** Stellen aktiv geführt (frühere Berichte nannten nur eine) | beide auf **REQ-037** und/oder **REQ-038** auflösen — die Aufteilung ist fachlich zu entscheiden, nicht zu raten |
| `scratchpad/gen_intake.py` | `:343`, `:474` | hartkodiert „Zehn reservierte Canvas-Items (CAN-016…022, CAN-071, CAN-099, CAN-130)" und schreibt es wörtlich ins Intake-Paket. Es sind **sechs** (CAN-016…021); CAN-022/099/130 sind aktiv, CAN-071 ist deprecated | Zahl **und** Liste aus der Registry ableiten (§10.2) |
| `scratchpad/validate_intake.py` | `:766`, `:797` (C3d-Hinweis und Schlussblock) | derselbe Altstand; zusätzlich „0 ungueltige Referenzen ueber alle **zehn** verwalteten Praefixe" — es sind **zwölf** (`MANAGED_PREFIXES` führt sie bereits alle) | Text aus `len(MANAGED_PREFIXES)` ableiten, nie ausschreiben |
| `scratchpad/validate_trace.py` | `:142` | `forbidden = {"36"}` — verbietet **nur** „36" | **weder** 36 **noch** 39 verbieten oder erwarten; Zählstände ausschließlich aus der Registry (§10.2) |
| `scratchpad/nfr-audit.json` | `:144`…`:377` | führt `blocking_scope` noch **lebend** (Feld ist seit 2026-07-19 entfallen) und vokabularvermischt — `:377` enthält `["none"]`, das in **keinem** der beiden abschließenden Wertebereiche liegt | Feld auflösen; für `NFR-` entfällt die Blockierungsachse ersatzlos (§6.13.2) |
| alle Validatoren | — | Blocking-Formel wird als `status == open` zitiert, normativ ist `status NOT IN [resolved]` | Wortlaut **und** Implementierung auf die normative Fassung angleichen (§3.1) |

### 7.6 Migration Runde 6 (2026-07-20) — Herabstufungen nach Nutzerauftrag

**Keine neue ID. Keine Deprecation. Kein Item umgedeutet. Nichts hochgestuft.** Diese Runde
ändert ausschließlich Source-Type-Vermerke, einen kanonischen Wortlaut (CAN-099, ausdrücklich
beauftragt) und nimmt §3.3 auf. Alle Fundstellen sind am 2026-07-20 gegen die jetzt im
Repository liegenden Quellen `docs/sources/SRC-001…SRC-004` verifiziert.

#### 7.6.1 Herabstufungen (mit Datum, Grund und Fundstelle)

| ID | Alt | Neu | Grund und Fundstelle |
|---|---|---|---|
| CAN-119 | `EXPLICIT \| SRC-003` | **`ASSUMPTION`**, Titel unverändert | „Privacy-Matrix" 0 Treffer in allen vier Quellen; das Artefakt heißt dort ausnahmslos „Sichtbarkeits-Matrix" (SRC-003:363/:522/:683, SRC-001:192) und wird repo-seitig bereits als **EV-018** quellentreu geführt. „Privacy-Review" als **querschnittlicher** Nachweisvorgang 0 Treffer; belegt sind nur **datenklassengebundene Einzelprüfungen** (SRC-003:629, :715) und eine Store-Abnahme (SRC-003:643). Aufteilungsrichtung strittig → Nutzerentscheidung |
| CAN-109 | `EXPLICIT \| SRC-003` | **`ASSUMPTION`**, Wortlaut unverändert | Keine Quelle behauptet, die Anti-Cheat-Klassifikation könne irren. SRC-003:265/:559 tragen nur eine **Urteilsregel**; SRC-003:265 nennt als Rechtsfolge ausdrücklich die gesenkte Beweiskraft, **nicht** `verified=false`. Das SRC-003-Risikoregister (24 Zeilen) hat keine entsprechende Zeile. RISK-013 ist Zirkelbeleg |
| CAN-024 | `EXPLICIT \| SRC-001` | **`ASSUMPTION`**, Titel unverändert | „Renn-" steht nicht im zitierten Herkunftspunkt (SRC-001:51, „**Primär:**"), sondern nur in SRC-001:52 unter „**Sekundär:**" mit drei Qualifikatoren, die CAN-024 fallen lässt. „Freizeit-" ist orthographisch nur an „Läufer:innen" gebunden. Zielfassung strittig → Nutzerentscheidung |
| VIS-003 | `EXPLICIT \| SRC-001` (ganze Zeile) | **Teil-Herabstufung:** Klauseln „sicher(er Zugang)" und „verlässlich" auf **`ASSUMPTION`**, übriger Kern bleibt `EXPLICIT` | „Trainingspartner", „Zugang", „verlässlich", „Fortschrittssignal" je 0 Treffer. „verlässlich" ist nur auf **NFR-Ebene** belegt (SRC-001:250/:252), nicht auf Bedürfnisebene. Die Verbundaussage entsteht erst durch Komposition getrennter Fundstellen |
| CAN-099 | Kanonischer Wortlaut mit „**und ihre nutzbaren Web-Auskopplungen**" | Wortlaut **ohne** Web-Erstreckung; vier Details bleiben `ASSUMPTION` | Nutzerauftrag Schritt 3. SRC-003 §2.4 nennt Web nicht; die vier „Web-Auskopplung"-Treffer betreffen ausschließlich die CSS-Farbmischregel. **Fehlende Deckung, kein Widerspruch** — SRC-001:132 nimmt den Beschützer-Link aus, SRC-001:238 / SRC-003:605 planen ihn ein |
| REQ-007 | `ASSUMPTION` (bereits korrekt) | **`ASSUMPTION` bestätigt**, Wortlaut unverändert | Nutzerauftrag Schritt 4. Bewusste Abweichung von SRC-004:416-418, das die Subtraktion vorschreibt. Träger SRC-005/DEC-004: DEC-004 ist `proposed`, SRC-005 ist ein `consistency-review`, keine Nutzerquelle |

#### 7.6.2 Nachzugsaufträge an die jeweiligen Owner (diese Registry ändert die Dateien nicht)

| Datei | Befund | Nachzug |
|---|---|---|
| `docs/canvas/…canvas.md` | CAN-119, CAN-109, CAN-024 führen `EXPLICIT`; CAN-099 führt die Web-Erstreckung | Source Types auf `ASSUMPTION` angleichen; Web-Erstreckung aus dem CAN-099-Wortlaut entfernen (§1: die Registry gilt) |
| `docs/vision/…vision.md` | Board-Zeile VIS-003 und die Narrativ-Liste „User Needs" tragen „sicher"; Board-Zeile trägt „verlässlich" | Teil-Herabstufung abbilden. **Der Kern darf „gemeinsames Training und reale Treffen" nicht mitschneiden** (SRC-001:22/:26/:47/:136, SRC-003:64) |
| `docs/prd/…prd.md` | REQ-037-Text, AC-037 Given und NFR-005 `signal` tragen die Web-Erstreckung | **Synchron** mit CAN-099 entfernen, sonst trägt REQ-037 eine Klausel ohne Canvas-Anker |
| `docs/EVIDENCE-LEDGER.md` | EV-037-Kopf zitiert REQ-037 inklusive Web-Auskopplungen | dito, synchron |
| `docs/traceability.md` | TRC-037 (Web-Erstreckung); TRC-004 stützt sich auf „verlässliches Tracking" als **tragende Klausel** | Web-Erstreckung nachziehen; **TRC-004 neu bewerten — die Zeile bricht**, REQ-004 liegt auf GATE-A0 |
| `docs/SOURCE-MAP.md` | verortet `src-verification.json` noch „außerhalb des Repositories" | auf `scripts/validation/src-verification.json` nachziehen (§13.2) |

## 8. Offene Punkte, BLOCKER und MISSING

Nichts hier wird durch eine plausible Annahme ersetzt.

| # | Punkt | Art | Betroffen | Wer entscheidet |
|---|---|---|---|---|
| 1 | Inhalt der reservierten Canvas-Items CAN-016 … CAN-022 (sieben fehlende Problemaussagen) | **BLOCKER** | 14 REQs mit `canvas-problem = MISSING` | Nutzer |
| 2 | ~~Inhalt von CAN-071~~ | **GESCHLOSSEN 2026-07-19** | REQ-008 | CAN-071 deprecated, ersetzt durch CAN-138/139/140 (§7.4.1) |
| 3 | ~~Inhalt von CAN-099~~ | **GESCHLOSSEN 2026-07-19** | REQ-037, NFR-005 | Inhalt entschieden; die zweite Hälfte (Designsystem) ist jetzt CAN-141 |
| 4 | ~~Inhalt von CAN-130~~ | **GESCHLOSSEN 2026-07-19** | REQ-019, VIS-006 Zeile B | Inhalt entschieden, Vollspezifikation §6.3.2. **Achtung:** geschlossen ist die *Definition*, nicht der *Nachweis* — `evidence_status = planned`, `empirical_result = MISSING` |
| 5 | ~~Fehlende PRD-USER-ID für „ambitionierte Ausdauersportler:innen“~~ | **als ID-Frage GESCHLOSSEN 2026-07-19** | REQ-032 | USER-004 vergeben (§6.12). **Offen bleibt:** Bestätigung der Persona (ASSUMPTION) und die *semantische* Prüfung, ob REQ-009 und REQ-011 wirklich an USER-004 gehören — **keine automatische Universalverknüpfung** |
| 6 | Definition von „sicherer“ in CAN-031 (Trainings- oder Datensicherheit) | **OPEN QUESTION** | REQ-030, REQ-031, REQ-034 | Nutzer |
| 7 | Stärke und adressierte Lücke der Alternative „lokale Event-Plattformen“ (CAN-046) | **MISSING** | CAN-046 | Nutzer |
| 8 | Widerspruch A0 lokal ↔ serverseitiger Routing-Proxy (CAN-131 vs. CAN-091/CAN-096) | **OPEN QUESTION** | CONTRA-006, REQ-034 | Nutzer |
| 9 | `routingProfile` liegt in der App-seitigen SportConfig (Architektur §6), obwohl die Profilübersetzung laut CAN-094 im Proxy liegt | **OPEN QUESTION** | CAN-094, docs/architecture/revyr-target-architecture.md | Architektur-Owner, Phase 3 |
| 10 | Architektur §9 nennt weiterhin „Development darf einen eingeschränkten Public Key verwenden“ und bindet den Proxy an „Produktion“ — überholt durch DEC-005/CAN-091 | **OPEN QUESTION** | CAN-091, CAN-092 | Architektur-Owner, Phase 3 |
| 11 | Aufnahme der Präfixe DEC-, USER-, NFR-, SRC-, VC-, GATE- in die Registry | **OPEN QUESTION** | Abschnitt 5 | Nutzer |
| 12 | Inhalt von VC-001 … VC-036 (`value-check-id` ohne Definitionsdatei) | **MISSING** | alle 36 REQs | Traceability-Owner, Phase 3 |
| 13 | Kein ausführbarer Validator für die Regeln in Abschnitt 2 | **MISSING** | Abschnitt 9 | Nutzer |
| 14 | ~~Keine EV-ID für „Datenmodell trennt Identität und historische Aggregate"~~ | **als ID-Frage GESCHLOSSEN 2026-07-19** | CONTRA-005, REQ-017, REQ-027 | **EV-042** vergeben (§6.7). Der Nachweis selbst bleibt `blocked` (Retentionsfristen MISSING, OQ-009) |
| 15 | Bestätigung von **VIS-011** (Accessibility Boundary) als Vision-Aussage. Bis dahin `source_type = ASSUMPTION`; VIS-011 zählt **nicht** als erfüllter Vision-Anker für REQ-014 | **BLOCKER** | REQ-014, NFR-005, TRC-014 | Nutzer |
| 16 | ~~Wertebereich von `blocking_scope`~~ | **GESCHLOSSEN 2026-07-19** | §3.1, §6.11.1 | Nutzerentscheidung C16: `blocking_scope` ersetzt durch `blocked_gates` + `blocked_activities` mit je abschließendem Wertebereich; die vier strittigen Werte sind reguläre `blocked_activities` |
| 17 | `decision_reference` von CONTRA-006 nennt einen „ADR zum A0-Routing-Proxy"; ein solches Artefakt existiert im Repository nicht | **MISSING** | CONTRA-006, DEC-005, CAN-089 | Nutzer, danach Architektur-Owner |
| 18 | `docs/decisions/decision-log.md` behauptet für CONTRA-003 eine maschinelle Prüfung; §9 hält fest, dass kein ausführbares Prüfwerkzeug existiert — die Prüfung hat kein reproduzierbares Artefakt | **MISSING** | CONTRA-003 | Owner `docs/decisions/decision-log.md` |
| 19 | Inhalt von **VIS-012** (Designprinzip auf Vision-Ebene) — REQ-038 hat keinen Vision-Anker | **BLOCKER** | REQ-038, TRC-038 | Nutzer |
| 20 | Inhalt von **VIS-013** (Datenportabilität auf Vision-Ebene) — REQ-039 hat keinen Vision-Anker | **BLOCKER** | REQ-039, TRC-039 | Nutzer |
| 21 | Kein Vision-Item zu „vollständigen und erklärbaren Trainingsdaten" als primärer Anker für REQ-032 (von der Nutzerentscheidung ausdrücklich verlangt) | **MISSING** | REQ-032, USER-004, CAN-022 | Nutzer |
| 22 | Bestätigung von **USER-004** als Persona; Source Type bleibt bis dahin ASSUMPTION | **BLOCKER** | REQ-032, CAN-025 | Nutzer |
| 23 | Semantische Prüfung, ob **REQ-009 und REQ-011** an USER-004 gehören — ausdrücklich **keine** automatische Universalverknüpfung | **OPEN QUESTION** | REQ-009, REQ-011, USER-004 | PRD-/Traceability-Owner, Phase 2/3 |
| 24 | Wortlautbestätigung der neu inhaltlich gefüllten Items CAN-022, CAN-138, CAN-139, CAN-140 und der Requirements REQ-008 (verengt), REQ-037, REQ-039, REQ-040 — alle stehen auf **ASSUMPTION** | **BLOCKER** | die genannten IDs | Nutzer |
| 25 | Messdefinition, Zielwert, Messfenster, Testmethode, Owner und Gate für **NFR-008** (OQ-013) | **MISSING** | NFR-008 | Nutzer |
| 26 | Telemetrie-Entscheidung für CAN-130 (OQ-012); ohne sie ist AC-041 nicht erfüllbar und **keine Behauptung zulässig, CAN-130 sei empirisch validiert** | **BLOCKER** | REQ-019, AC-041, EV-041, CAN-130 | Nutzer |
| 27 | Stichprobenregel für CAN-130 (OQ-014) — Mindestzahlen werden **nicht geraten** | **MISSING** | CAN-130, AC-041 | Nutzer |
| 28 | Vergleichbarkeitsdefinition für REQ-040 (OQ-015); AC-040 und EV-040 sind ohne sie nicht spezifizierbar | **BLOCKER** | REQ-040, AC-040, EV-040, CAN-140 | Nutzer |
| 29 | Referenz-Fremdanwendung für den GPX-Nachweis (OQ-016); AC-039 Kriterium (d) sonst nicht reproduzierbar | **MISSING** | REQ-039, AC-039, EV-039 | Nutzer |
| 30 | Dokument-Nachzug des Auftau-Schritts 2: neue IDs eintragen, deprecatete IDs (CAN-071, REQ-014, AC-014, EV-014, TRC-014) aus PRD, Canvas und Traceability entfernen | **OFFEN, terminiert** | §7.4.4 | Datei-Owner, Phase 2/3 |
| 31 | Der Komfortaspekt „Nutzer müssen zusätzlich das Telefon mitführen" ist bewusst **kein** Canvas-Item und hat **keine ID** — Aufnahme nur nach eigener fachlicher Entscheidung | **OPEN QUESTION** | CAN-022 | Nutzer |
| 32 | Das entfallene Feld `blocking_scope` wird in **sechs** Dateien außerhalb dieser Registry noch verwendet (51+ Vorkommen, §7.4.5). Solange ein Werkzeug die alte Formel darauf anwendet, liefert es für gegatete Einträge weiterhin fälschlich `false` | **BLOCKER** | traceability, PRD, decision-log, validation-report, Evidence Ledger, Vision | jeweiliger Datei-Owner, Phase 2/3 |
| 33 | Es existiert **keine** gemeinsame Implementierung der kanonischen Blocking-Funktion. §3.1 verlangt, dass alle Validatoren *dieselbe* importieren — derzeit gibt es überhaupt kein ausführbares Prüfwerkzeug (§9) | **MISSING** | §3.1, §9 | Nutzer, danach Owner der Validierung |
| 34 | Die Spalte `blocking` in `prd.md:302-311` führt **acht** hartkodierte NFR-Werte, für die es keine Formel, keine Eingabe und keinen Wertebereich gibt. Sie ist zu **entfernen**, nicht umzurechnen (§6.13.2) | **BLOCKER** | NFR-001…008, `docs/prd/…prd.md` | PRD-Owner, Phase 2/3 |
| 35 | ~~NFR-008 trägt ein `blocking`, das niemand nachrechnet~~ | **GESCHLOSSEN 2026-07-20** | NFR-008, §3.1 | Entschieden: der `NFR-`Raum führt **kein** `blocking`; die Achsen bleiben auf `OQ-`/`CONTRA-` beschränkt; keine Metamodell-Erweiterung (§6.13.2). **Offen bleibt** die Messdefinition (Punkt 25 / OQ-013) |
| 36 | Der kanonische CAN-139-Wortlaut nennt „**in einer kompatiblen Fremdanwendung öffnen**" **nicht mehr**; AC-039 (d) und EV-039 verlangen den Nachweis weiterhin. Der Bezug ist über „standardkonforme GPX-Datei" tragbar, aber nicht mehr wörtlich belegt. Es wird weder die AC gestrichen noch der Wortlaut nachträglich ergänzt | **OPEN QUESTION** | CAN-139, REQ-039, AC-039, EV-039, OQ-016 | Nutzer |
| 37 | Nach Entfernung der verbotenen Schlusskette haben **REQ-037, REQ-038 und REQ-039** keinen canvas-problem-Anker mehr. Der Canvas führt weder ein Zugänglichkeits-, noch ein Gestaltungs-, noch ein Portabilitätsproblem. Es wird **kein** CAN-Item umgedeutet und **keine** neue Problem-ID vergeben (die reservierten CAN-016…021 decken keines der drei ab) | **BLOCKER** | REQ-037, REQ-038, REQ-039, CAN-013 | Nutzer |
| 38 | Inhalt von **VIS-014** (Wiederverwendung geplanter Strecken auf Vision-Ebene) — REQ-041 hat keinen Vision-Anker; TRC-041 bleibt `broken`. VIS-003 wurde geprüft und trägt die Aussage **nicht** | **BLOCKER** | REQ-041, TRC-041, CAN-142 | Nutzer |
| 39 | **CAN-050** („Routenplanung **und** gespeicherte Routen") ist selbst ein Composite und wird zusätzlich in `traceability.md:465` und `prd.md:993` als Anker für **REQ-008** geführt, während die Registry es REQ-006 zuordnet. Eine ID mit zwei Bedeutungen in zwei Requirement-Kontexten | **BLOCKER** | CAN-050, REQ-006, REQ-008 | Nutzer (Atomisierung), danach PRD-/Traceability-Owner |
| 40 | Der Vision-Anker **VIS-003 ↔ REQ-006** (TRC-006, Zeilenstatus `linked`) beruht auf derselben ungeprüften Lesart, die für REQ-041 ausdrücklich verworfen wurde: VIS-003 nennt keine Routenplanung. Er ist nach dem Muster §6.1.1 zu prüfen — **nicht** zu übernehmen, weil er existiert | **OPEN QUESTION** | REQ-006, TRC-006, VIS-003 | Traceability-Owner, Phase 2/3 |
| 41 | REQ-019 („Routenempfehlungen **und** Feed") ist von VIS-003 nur über die Klausel „sicherer Zugang zu lokalen Trainingspartnern" getragen; die **Empfehlungs-Hälfte** hat keinen belegten Vision-Bezug. Die Nutzerentscheidung erlaubt eine weitere Verknüpfung „nur wenn belegt" — sie ist es nicht, deshalb wurde **keine** gesetzt | **MISSING** | REQ-019, TRC-019, VIS-003 | Nutzer |
| 42 | `prd.md:311` führt NFR-008 mit `source_type` **EXPLICIT**, diese Registry mit **MISSING**. Nach §1 gilt die Registry; die Divergenz besteht bis zum PRD-Nachzug fort | **BLOCKER** | NFR-008 | PRD-Owner, Phase 2/3 |
| 43 | Wortlautbestätigung der in Runde 4 kanonisierten bzw. neu angelegten Items: **CAN-142, CAN-143, REQ-041, REQ-042** stehen auf **ASSUMPTION**; **CAN-099, CAN-139, CAN-141** sind auf **EXPLICIT** gesetzt, weil der Nutzer den Wortlaut am 2026-07-20 als verbindlich gesetzt hat — eine ausdrückliche Gegenbestätigung liegt nicht vor | **BLOCKER** | die genannten IDs | Nutzer |
| 44 | Dokument-Nachzug Runde 4: neue IDs eintragen, deprecatete IDs (CAN-140, REQ-040, AC-040, EV-040, TRC-040) aus PRD, Canvas, Traceability und Evidence Ledger entfernen, verbotene Ketten und Zähl-Literale bereinigen (§7.5.5) | **OFFEN, terminiert** | §7.5.4, §7.5.5 | Datei- und Werkzeug-Owner, Phase 2/3 |
| 45 | **Aufteilungsrichtung von CAN-119.** Das Item bündelt zwei Gegenstände: „Privacy-Review" hat echte Canvas-Lineage (Ursprungstext „Claims-, Privacy- und Threat-Model-Reviews."), aber keine Quellendeckung als querschnittlicher Nachweisvorgang; „Privacy-Matrix" hat weder Lineage im überlieferten Ursprungstext noch Quellendeckung, und der von ihm bezeichnete Gegenstand wird bereits als **EV-018 „Sichtbarkeits-Matrix"** geführt. Welcher Teil die ID behält, wird hier **nicht** vorweggenommen | **BLOCKER** | CAN-119, EV-018, REQ-018, REQ-033 | Nutzer |
| 46 | **Zielfassung von CAN-024.** Ein bloßes „Radfahrer:innen" ist begrifflich **weiter** als der Primär-Punkt und stellt die Verschmelzung mit der sekundären Gruppe unsichtbar wieder her; Alternativen sind ein Rangzusatz „(primär)" oder ein Quellenwechsel auf `SRC-001/SRC-003` (SRC-003:65 führt „Radfahrer/Rennradfahrer" ungestuft als **eine** Zielgruppe, das PRD fährt für USER-002 bereits beide Quellen). Folge der Verengung: REQ-032 verliert den belegten Anker für den **Sensorik**-Bedarf, der quellenseitig nur an der sekundären Persona hängt | **BLOCKER** | CAN-024, USER-002, REQ-032, CAN-025 | Nutzer |
| 47 | **Wortlautbestätigung der in Runde 6 herabgestuften Items.** CAN-119, CAN-109 und CAN-024 stehen auf **ASSUMPTION**, VIS-003 in zwei Klauseln ebenfalls. Die Herabstufung ist eine Belegfeststellung, **keine** Aussage darüber, ob die Inhalte fachlich richtig sind — die Bestätigung oder Streichung ist eine Nutzerentscheidung | **BLOCKER** | CAN-119, CAN-109, CAN-024, VIS-003 | Nutzer |
| 48 | **`prd.md` behauptet die Folgenlosigkeit der CAN-099-Überdehnung zu Unrecht.** Die Web-Erstreckung steht in der Given-Spalte von AC-037 und im `signal` von NFR-005; die unbelegte Fassungsziffer „2.2" steht in der **Pass**-Spalte von AC-037 und in EV-037 [ACC1] als **store-release-blockierender** Nachweis; Bedienflächen und Fokusführung stehen in EV-037 [ACC4]/[ACC7]. Der Absatz widerspricht sich zusätzlich binnenintern. Dieselbe Aussage steht im Validierungsbericht und im Canvas | **BLOCKER** | CAN-099, REQ-037, AC-037, EV-037, NFR-005 | PRD-, Canvas- und Validierungs-Owner, Phase 2/3 |
| 49 | **Feldbenennung `source_type` in den Messblöcken.** Dort beantwortet das Feld die Herkunft des **Zielwerts**, in der Anforderungstabelle die Herkunft der **Anforderung**. Gleicher Name, zwei Fragen — die Divergenz bei REQ-007 (`ASSUMPTION` gegen `MISSING`) ist deshalb **kein** Widerspruch und darf **nicht** harmonisiert werden. Zu vereinheitlichen ist der **Name** (`target_source_type`, wie an anderer Stelle im PRD bereits verwendet), nicht der Wert | **OPEN QUESTION** | REQ-007 und die übrigen 12 MISSING-Schwellen, `docs/prd/…prd.md`, `docs/traceability.md` | PRD-/Traceability-Owner, Phase 2/3 |
| 50 | **Gleich gelagerte Nachbaritems, in Runde 6 ausdrücklich NICHT angefasst.** CAN-118 („Claims-Review") und CAN-120 („Threat-Model-Review") tragen dieselbe quellenlose „-Review"-Prägung wie CAN-119 (belegt sind nur die Grundbegriffe SRC-003:686 und SRC-003:602); CAN-110 trägt dieselbe Annotation und Lage wie CAN-109; CAN-028 („Verlässliches Tracking") und CAN-031 („Trainiere sicherer") tragen dieselben unbelegten Qualifizierer wie VIS-003 und sind mit ihm **gemeinsam** zu entscheiden. Zusätzlich erfasst §3.3 **keine Rollenfehler** (Muster CAN-044). Eine Einzelbereinigung ohne diese Nachbarn bliebe wirkungslos | **BLOCKER** | CAN-118, CAN-120, CAN-110, CAN-028, CAN-031, CAN-044 | Nutzer |
| 51 | **`docs/decisions/decision-log.md` führt DEC-004 auf `proposed`**, während CAN-051 in dieser Registry (§6.3) und im Canvas im **Präsens** behauptet, DEC-004 „verbietet" die einfache Distanzsubtraktion. Ein `proposed`-Eintrag verbietet nichts. Die CAN-051-Zeile wurde in Runde 6 **nicht** geändert, weil CAN-051 nicht zum beauftragten Umfang gehört und die Zielfassung zwischen den Gegenprüfungen strittig ist (vollständige Herabstufung gegen Teilbelegung mit `SRC-001/SRC-003` **plus** `SRC-005/DEC-004`) | **BLOCKER** | CAN-051, REQ-007, DEC-004 | Nutzer, danach Canvas-Owner |

## 9. Validierungsregeln — Stand der Werkzeuge

Aus den Regeln in Abschnitt 2 folgen fünf maschinell prüfbare Bedingungen:

1. Jede in `docs/**` referenzierte ID der **zwölf** verwalteten Präfixe hat einen
   Registry-Eintrag.
2. Keine ID erscheint zweimal mit `status = active` bei unterschiedlicher `canonical_file`.
3. Kein Dokument referenziert eine ID mit `status = deprecated`.
4. Jeder `active` Eintrag wird von mindestens einem Dokument referenziert (keine Waisen).
5. `template-placeholder`-Einträge sind von Regel 1 und 4 ausgenommen.
6. **Nachzugsfenster (Regel 10).** Die in §7.4.4 und in `id-migration.json` unter
   `pending_document_nachzug` gelisteten IDs sind von Bedingung 4 ausgenommen — **und nur
   diese**. Jede andere Waise bleibt ein Fehler.
7. **Blocking (Regel §3.1).** `blocking` wird **berechnet**, nie gelesen. Prüfbedingungen:
   (a) `current_gate` wird ausschließlich gegen `blocked_gates` geprüft, `current_activity`
   ausschließlich gegen `blocked_activities`; (b) jeder Wert in `blocked_gates` liegt im
   Gate-Wertebereich, jeder Wert in `blocked_activities` im Tätigkeits-Wertebereich — ein
   Gate-Bezeichner in `blocked_activities` (oder umgekehrt) ist ein **Fehler**, kein
   Toleranzfall; (c) kein Werkzeug enthält eine ID-spezifische Sonderregel; (d) alle Werkzeuge
   importieren **dieselbe** Implementierung.
8. **Zählstände (Regel 11, verschärft in Runde 4).** Keine Prüfung verwendet eine hartkodierte
   Anzahl. **Kein Validator darf die Literale `36` ODER `39` verbieten oder erwarten** — beides
   sind Momentaufnahmen. Eine Prüfung, die „36" auf eine Verbotsliste setzt, ist derselbe Fehler
   wie eine, die „36" erwartet: sie bindet ein Werkzeug an einen Zählstand. Zählstände werden
   zur Laufzeit aus dieser Datei abgeleitet, **je Präfix und je Statusklasse getrennt** (§10.2).
9. **Statusfelder je ID-Raum (Runde 4).** `status` (`open`/`resolved`), `resolution_status`,
   `blocking`, `blocked_gates` und `blocked_activities` existieren **ausschließlich** für `OQ-`
   und `CONTRA-`. Ein Werkzeug, das eines dieser Felder für einen `NFR-`, `REQ-`, `CAN-`,
   `VIS-`, `AC-`, `EV-` oder `TRC-`Eintrag liest, schreibt oder berechnet, ist selbst der Defekt
   (§6.13.2). `evidence_status` gilt dagegen projektweit (§3.2).
10. **Wortlaut der Blocking-Formel (Runde 4).** Ein Werkzeug oder Bericht, der die erste Klausel
    als `status == open` formuliert, implementiert **nicht** die kanonische Formel. Normativ ist
    `status NOT IN [resolved]`; der Unterschied wird bei fehlendem oder ungültigem `status`
    wirksam (§3.1).

**Warnung aus einem eingetretenen Defekt.** In diesem Projekt hat ein Validator-Regex, der für
deutsche Bindestrich-Komposita blind war, einen **korrekten** Fremdbefund heruntergerechnet.
Schlägt eine Prüfung fehl, ist das zuerst ein **Befund**. Widerspricht die Prüfung dem eigenen
Text, wird **der Text geändert, nicht die Prüfung** — und ein Regex, der an der Sprache des
Repositories scheitert, ist selbst der Defekt.

**Ein ausführbares Werkzeug, das diese fünf Bedingungen prüft, existiert im Repository
nicht.** Vorhanden ist ausschließlich `~/.claude/bin/plumbline-scope-check`, und das prüft
etwas anderes: geänderte Dateipfade gegen den „Allowed change scope“ des Canvas. Die Regeln
oben sind daher derzeit **nur redaktionell durchgesetzt**. Ein Intake-/Schema-Validator wird
in diesem Lauf an anderer Stelle **neu verfasst**; er ist kein vorbestehender Standard und war
zum Zeitpunkt dieses Eintrags nicht verfügbar.

## 10. Bestandsabgleich

**Alle Zahlen hier sind Momentaufnahmen vom 2026-07-20 nach Runde 4** und nach Regel 11 aus dieser
Datei **abgeleitet** (Ableitungsweg in §10.2). Sie sind keine Zielwerte. **Weder 36 noch 39 ist ein
gültiger Erwartungswert** — beide sind Altstände. Jede Prüfung, die eine dieser Zahlen erwartet
**oder verbietet**, ist zu korrigieren, **nicht die Daten**.

| Präfix | Stand nach Schritt 2 (2026-07-19) | **Stand nach Runde 4 (2026-07-20)** | Abgleich |
|---|---|---|---|
| VIS | 11 aktiv + 2 reserviert | **11 aktiv · 0 deprecated · 3 reserviert** | VIS-014 reserviert (Inhalt MISSING, §8 Punkt 38) |
| CAN | 122 aktiv + 13 deprecated + 6 reserviert | **123 aktiv · 14 deprecated · 6 reserviert** | CAN-140 deprecated (−1 aktiv, +1 deprecated); CAN-142, CAN-143 neu (+2 aktiv) |
| REQ | 39 aktiv + 1 deprecated + 1 Platzhalter | **40 aktiv · 2 deprecated · 1 Platzhalter** | REQ-040 deprecated; REQ-041, REQ-042 neu. **40 = 39 − 1 + 2** |
| AC | 40 aktiv + 1 deprecated + 1 Platzhalter | **41 aktiv · 2 deprecated · 1 Platzhalter** | AC-040 deprecated; AC-042, AC-043 neu. **41 ≠ 40 ist korrekt** — REQ-019 hat zwei ACs (§6.5.1) |
| TRC | 39 aktiv + 1 deprecated | **40 aktiv · 2 deprecated** | TRC-040 deprecated; TRC-041, TRC-042 neu. **40 = Anzahl aktiver REQ** ✓ |
| EV | 41 aktiv + 1 deprecated + 1 Platzhalter | **42 aktiv · 2 deprecated · 1 Platzhalter** | EV-040 deprecated; EV-043, EV-044 neu. **42 = 40 + EV-041 (zweiter Nachweis zu REQ-019) + EV-042 (CONTRA-005)** ✓ |
| RISK | 24 aktiv | **24 aktiv** | unverändert |
| ASM | 7 aktiv + 7 deprecated | **7 aktiv · 7 deprecated** | unverändert. Die 7 deprecateten sind **Zeilen**, nicht IDs: ASM-001…003 stehen je **zweimal** (PRD und Vision) — das ist der dokumentierte Kollisionsnachweis (§6.9), kein Zähldefekt |
| OQ | 15 offen + 1 resolved | **15 offen · 1 resolved** | unverändert — Runde 4 vergibt **keine** neue OQ-ID (§7.5.2) |
| CONTRA | 6 resolved | **6 resolved** | unverändert. `blocking` wird je Auswertung abgeleitet und ist **keine Bestandszahl** — es wird hier bewusst nicht mehr mitgezählt |
| USER | 4 aktiv | **4 aktiv** | unverändert |
| NFR | 8 aktiv | **8 aktiv** | unverändert im Bestand. **Das Feld `blocking` entfällt für den gesamten Raum** (§6.13.2) — die früheren 8 Werte waren nicht ableitbar |

### 10.1 Ableitungsregel für die Zahl aktiver Requirements (Regel 11)

```
aktive_requirements = |{ e ∈ Registry : praefix(e.id) = "REQ"
                                    ∧ e.status = "active"
                                    ∧ e.status ≠ "template-placeholder" }|
```

**Stand 2026-07-20 nach Runde 4: 40.** Ausgeschlossen sind REQ-000 (`template-placeholder`, §4)
sowie REQ-014 und REQ-040 (`deprecated`).

`NFR-`IDs zählen **nicht** in diese Zahl — sie bilden einen eigenen Raum (§6.13). Wer
funktionale und nicht-funktionale Anforderungen zusammenzählen will, muss das benennen und
beide Zahlen getrennt ausweisen.

**Bekannte Folgeabweichung:** `VC-001…VC-036` (§5.2) bildet noch den Altstand von 36 ab und geht
der REQ-Zahl damit nach. Das ist ein Nachzugsbefund für den Traceability-Owner (§8 Punkt 12),
**kein** Argument gegen die 40.

### 10.2 Zählregel für **alle** Präfixe (Runde 4, verbindlich)

Regel 11 galt bisher vor allem für `REQ-`. Sie gilt gleichermaßen für **`VIS-`, `CAN-`, `AC-`,
`TRC-`, `EV-`, `RISK-`, `ASM-`, `OQ-`, `CONTRA-`, `USER-` und `NFR-`**. Ein Zählstand wird
**ausschließlich** so gebildet:

```
zaehle(praefix, status) = |{ e ∈ Registry-Definitionstabellen :
                                praefix(e.id) = praefix ∧ e.status = status }|

aktiv(p)        = zaehle(p, "active")            // bzw. "open" für OQ-/CONTRA-
deprecated(p)   = zaehle(p, "deprecated")        // NIE in aktiv() enthalten
reserviert(p)   = zaehle(p, "reserved")          // GETRENNT auszuweisen, nie zu aktiv() addiert
platzhalter(p)  = zaehle(p, "template-placeholder")   // von jeder Abdeckungsprüfung ausgenommen
```

**Vier Bindungen:**

1. **Aktive, deprecatete und reservierte Einträge werden immer getrennt ausgewiesen.** Eine
   Gesamtzahl ohne Statusaufschlüsselung ist kein gültiger Zählstand. Reservierte Einträge sind
   **nie** erfüllte Referenzen (§3) und dürfen nicht zur aktiven Zahl addiert werden.
2. **Kein Literal.** Kein Werkzeug, kein Bericht und keine Prüfbedingung nennt eine feste Anzahl
   als Erwartungs- **oder** Verbotswert. Das gilt namentlich für **36** und **39** — beide sind
   überholte Momentaufnahmen, und ein Verbot von „36" bindet ein Werkzeug genauso an einen
   Zählstand wie seine Erwartung.
3. **Quelle ist ausschließlich diese Datei**, und zwar ihre Definitionstabellen — nicht die
   Migrations-, Zähl- oder Befundtabellen. Die Definitionstabelle ist daran erkennbar, dass die
   vierte Spalte eine `canonical_file` in Backticks führt. Wer die Statusspalte aus §6.11.1
   (dort steht in derselben Position `blocking`) mitzählt, zählt sechs Phantomeinträge.
4. **Wer eine Zahl nennt, nennt Datum und Ableitungsweg** (§3, §10).

**Bekannte Zeilen-≠-ID-Ausnahme:** im `ASM-`Raum belegen ASM-001…003 **je zwei** deprecatete
Zeilen (PRD und Vision), weil genau diese Doppelbelegung der dokumentierte Kollisionsbefund ist
(§6.9). `deprecated("ASM") = 7 Zeilen = 4 verschiedene Alt-IDs`. Jede Zählung, die hier eine
Abweichung meldet, meldet den Befund korrekt — sie ist **nicht** zu unterdrücken.

## 11. Änderungsprotokoll

| Datum | Phase | Änderung |
|---|---|---|
| 2026-07-19 | 1 | Registry angelegt. Bestand VIS/REQ/AC/TRC/EV/RISK/OQ/CONTRA erfasst. |
| 2026-07-19 | 1 | REQ-000/AC-000/EV-000 als Template-Platzhalter ausgewiesen. |
| 2026-07-19 | 1 | ASM-Kollision (ASM-001…003 in zwei Dateien) aufgelöst; ASM-1xx/2xx vergeben, Alt-IDs deprecated. |
| 2026-07-19 | 1 | Canvas atomisiert: CAN-001…012 deprecated, CAN-013…CAN-137 vergeben (115 aktiv, 10 reserviert). |
| 2026-07-19 | 1 | Facetten-IDs aus `docs/traceability.md` auf atomare CAN-IDs abgebildet. |
| 2026-07-19 | 1 | OQ-011 auf `resolved` gesetzt (Ablageort `infra/routing-proxy/`). |
| 2026-07-19 | 1 (Auftau-Schritt) | Statusmodell für `OQ-`/`CONTRA-` verankert (§3.1): `status` auf `open`/`resolved` reduziert, getrennte Felder `resolution_status`, `evidence_status`, `blocking`, `blocking_scope`, `evidence_gate`, `decision_reference`, `evidence_reference`, `rationale` eingeführt; `blocking` als **abgeleitete** Größe mit verbindlicher Formel. |
| 2026-07-19 | 1 (Auftau-Schritt) | CONTRA-004, CONTRA-005 und CONTRA-006 auf `status = resolved` normalisiert und nach §3.1 vollständig ausgefüllt (§6.11.1). Der unzulässige Mischwert `DESIGN-RESOLVED / EVIDENCE-PENDING` bei CONTRA-006 auf die zwei Achsen aufgeteilt. Divergenz **C6b** gegenüber `docs/decisions/decision-log.md` damit aufgelöst; Ledger und Validierungsbericht zieht Phase 2 nach. |
| 2026-07-19 | 1 (Auftau-Schritt) | **VIS-011** (Accessibility Boundary) vergeben. Grund: REQ-014 hing an VIS-009 (Privacy Boundary) — semantisch falscher Anker. Prüfung VIS-001…VIS-010 in §6.1.1 dokumentiert; Source Type ASSUMPTION, nicht bestätigt. |
| 2026-07-19 | 1 (Auftau-Schritt) | Titel von **REQ-027** und **EV-027** an die bereits migrierte `canonical_file` (PRD) angeglichen; die Alttitel trugen die durch DEC-012 ersetzte Formulierung „unveränderliche Historie". Keine Neuformulierung durch die Registry. |
| 2026-07-19 | 1 (Auftau-Schritt) | §8 um die offenen Punkte 14–18 erweitert; §10 (VIS, CONTRA) fortgeschrieben. |
| 2026-07-19 | 1 (Auftau-Schritt **2**) | **Statusmodell C16:** `blocking_scope` ersatzlos entfallen, ersetzt durch die disjunkten Felder `blocked_gates` und `blocked_activities` mit je abschließendem Wertebereich. Kanonische Blocking-Formel neu gefasst; Gate- und Tätigkeitsachse werden **nie** gegeneinander geprüft. §6.11.1 vollständig umgestellt und die `blocking`-Werte erstmals nachgerechnet. §8 Punkt 16 geschlossen. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | **§3.2 neu:** projektweite Semantik von `evidence_status` (`not-planned` / `planned` / `pending` / `verified`) verankert; Grenze zwischen `planned` und `pending` ist die Instrumentierung. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | **Regel 10 (Nachzugsfenster)** und **Regel 11 (abgeleitete Zählstände, nie hartkodiert)** in §2 aufgenommen. §10.1 gibt die Ableitungsformel für die Zahl aktiver Requirements. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | **CAN-071 deprecated** → CAN-138 (Verlauf/Detail, A0), CAN-139 (GPX-Export, A2), CAN-140 (Streckenvergleich, A2). **CAN-141** neu für das monochrome Designsystem. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | **CAN-022, CAN-099, CAN-130** inhaltlich gefüllt (Nutzerentscheidung) und von `reserved` auf `active` gesetzt. CAN-099 ab jetzt **ausschließlich** Accessibility. CAN-130 mit Vollspezifikation in §6.3.2. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | **REQ-014 deprecated** (Composite) → REQ-037 (Accessibility), REQ-038 (Monochromes Designsystem), je mit AC- und EV-ID. Folge-Deprecations: AC-014, EV-014, TRC-014. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | **REQ-039** (GPX-Export) und **REQ-040** (Streckenwiederverwendung und Vergleich) neu vergeben; **REQ-008 und AC-008 verengt**. REQ-034 bleibt für den Export ausdrücklich nur **sekundäre** Constraint-Verknüpfung. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | **AC-019 aufgeteilt**: funktionales Kriterium bleibt bei AC-019, Messkriterium wird **AC-041**. Modellierungsbegründung in §6.5.1 (zwei IDs, nicht zwei Felder). REQ-019 ist damit das erste Requirement mit zwei ACs. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | **EV-042** vergeben für „Datenmodell trennt Identität und historische Aggregate" (DEC-012/CONTRA-005). §8 Punkt 14 als ID-Frage geschlossen. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | Präfixe **`USER-`** und **`NFR-`** in die Registry aufgenommen (§5.1, §6.12, §6.13). **USER-004** neu vergeben (ID zuvor als frei geprüft). **NFR-008 nicht deprecated** — Begründung und Verwaisungs-Auflösung in §6.13.1, offene Messdefinition als OQ-013. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | **VIS-012** und **VIS-013** reserviert (Inhalt MISSING) — REQ-038 und REQ-039 haben keinen Vision-Anker; es wird ausdrücklich **kein** bestehendes VIS-Item umgedeutet. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | **OQ-012…OQ-016** reserviert: Telemetrie, NFR-008-Messdefinition, CAN-130-Stichprobenregel, REQ-040-Vergleichsdefinition, GPX-Referenz-App. |
| 2026-07-19 | 1 (Auftau-Schritt 2) | §7.4 (Migrationstabellen, Nachzugsfenster) neu; §8 auf 31 Punkte fortgeschrieben; §10 vollständig neu abgeleitet. |
| 2026-07-20 | 1 (**Runde 4**) | **Kanonische Anker A/B/C** auf den verbindlichen Nutzerwortlaut gezogen: **CAN-099** (Accessibility, Item Type CONSTRAINT / VALUE BOUNDARY), **CAN-141** (monochromes Designsystem, DESIGN CONSTRAINT / PRODUCT PRINCIPLE), **CAN-139** (Datenportabilität/GPX, VALUE PROMISE / CAPABILITY). **Keine neuen IDs** — für alle drei existierte bereits ein aktives Item mit derselben Aussage; die **Abweichung von der wörtlichen Anweisung** ist in §6.3.3 einzeln begründet und gemeldet. |
| 2026-07-20 | 1 (Runde 4) | **Farbregel entdoppelt.** „Farbe ist niemals der einzige Informationsträger" wird kanonisch von **CAN-099** getragen und ist aus CAN-141 entfernt; dort verbleibt nur die engere Regel „Run und Bike nicht ausschließlich durch Farbe". Der frühere Registry-Vermerk „zwei getrennt prüfbare Pflichten" war die doppelt geführte Pflicht selbst. Keine dritte Farbregel. |
| 2026-07-20 | 1 (Runde 4) | **CAN-140 geteilt** → **CAN-142** (Planung/Wiederverwendung) und **CAN-143** (Auswertung/Vergleich). Vollständige Nachfolgekette: **REQ-040** → REQ-041/REQ-042, **AC-040** → AC-042/AC-043, **EV-040** → EV-043/EV-044, **TRC-040** → TRC-041/TRC-042. CAN-050, REQ-006, AC-006 und EV-006 wurden als Kandidaten **geprüft und verworfen** (§6.3.3). **VIS-014** reserviert. |
| 2026-07-20 | 1 (Runde 4) | **CAN-138 bleibt ungeteilt** — Teilungsprüfung nach der Atomisierungsregel negativ (gleicher A0-Nutzerfluss, Detailansicht als unmittelbare Vertiefung, gemeinsame Auslieferung über REQ-008, gleiches Gate, gleiches Datenmodell). Wortlaut kanonisiert. |
| 2026-07-20 | 1 (Runde 4) | **Semantisch falsche Vision-Anker entfernt:** TRC-019 → VIS-003, TRC-020 → VIS-004, TRC-021 → VIS-004, TRC-022 → VIS-003. VIS-008 (Fairness Boundary) trug **keine** Community-Aussage. Für REQ-022 wurde VIS-004 einzeln geprüft und **verworfen**; für REQ-019 wurde keine zweite Verknüpfung gesetzt, weil sie nicht belegt ist (§8 Punkt 41). Canvas-Spalten von CAN-005 auf CAN-058/CAN-060/CAN-067 gestellt. |
| 2026-07-20 | 1 (Runde 4) | **Verbotene Schlusskette** „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" als Anker untersagt und die belegten Fundstellen benannt: `traceability.md:1488` und `:1546` (REQ-037), `:1547` (REQ-038); dieselbe Defektklasse in `:1489` (REQ-038), `:1490` (REQ-039) und `:1491` (REQ-040). Folge: REQ-037/038/039 haben **keinen** canvas-problem-Anker mehr (§8 Punkt 37). |
| 2026-07-20 | 1 (Runde 4) | **EV-008 / EV-039 kanonisch getrennt.** EV-008 = ausschließlich Verlauf und Detailansicht (Titel wörtlich aus `prd.md:731` nachgezogen); EV-039 = ausschließlich GPX-Kompatibilitäts- und Exportnachweis. Die veraltete Registry-Definition von EV-008 hätte nach §1 gewonnen. |
| 2026-07-20 | 1 (Runde 4) | **NFR-008-Entscheidung (§6.13.2): der `NFR-`Raum führt kein `blocking`.** Die Achsen bleiben auf `OQ-`/`CONTRA-` beschränkt; keine Metamodell-Erweiterung. Aus §6.13.1 sind `blocked_gates = []`, `blocked_activities = []` und `blocking = false` entfernt; der Befund („wirkt an keiner Stelle") bleibt und wird über `evidence_gate = MISSING` und `evidence_status = not-planned` gesagt. NFR-008 bleibt **nicht deprecated**. Die acht hartkodierten `blocking`-Werte in `prd.md:302-311` sind zu **entfernen** (§8 Punkt 34). |
| 2026-07-20 | 1 (Runde 4) | **Blocking-Formel im Wortlaut gebunden:** `status NOT IN [resolved]`, ausdrücklich **nicht** `status == open`; fail-closed bei fehlendem oder ungültigem `status`, der zusätzlich ein Validierungsfehler ist (§3.1, §9 Punkt 10). |
| 2026-07-20 | 1 (Runde 4) | **Zählregel §10.2** für alle zwölf Präfixe: aktiv, deprecated, reserviert und Platzhalter **getrennt**; **weder 36 noch 39** als Erwartungs- oder Verbotsliteral; Quelle sind ausschließlich die Definitionstabellen. §10 vollständig neu abgeleitet (REQ aktiv: **40**). |
| 2026-07-20 | 1 (Runde 4) | **§7.3 an §7.4.1 angeglichen** (CAN-022/099/130 nicht mehr als Reserve, CAN-071/CAN-140 als deprecated statt als offene Lücke, CAN-138…143 in den Nachfolgerspalten; reservierte Lücken **sechs** statt zehn). **Leerzeile in der VIS-Definitionstabelle entfernt** — VIS-012/VIS-013 standen dadurch mechanisch außerhalb der Tabelle und zählten als nicht registriert (C3b). |
| 2026-07-20 | 1 (Runde 4) | §7.5 (Migration Runde 4) neu, inklusive **§7.5.5 mit fünfzehn belegten Dokument- und Werkzeugabweichungen**; §8 auf 44 Punkte fortgeschrieben. |
| 2026-07-20 | 1 (**Runde 6**) | **CAN-119, CAN-109 und CAN-024 auf `ASSUMPTION` herabgestuft**, Titel und Wortlaut jeweils **unverändert** (Nutzerauftrag Schritt 2). Die Verengungsrichtung ist bei CAN-119 und CAN-024 zwischen den Gegenprüfungen strittig und wird als Nutzerentscheidung geführt (§8 Punkte 45, 46), statt sie hier zu setzen. |
| 2026-07-20 | 1 (Runde 6) | **VIS-003 teil-herabgestuft:** die Klauseln „sicher(er Zugang)" und „verlässlich" stehen auf `ASSUMPTION`, der übrige Bedürfniskern bleibt `EXPLICIT`. **CAN-017 wird ausdrücklich NICHT aufgelöst** — der reservierte BLOCKER verliert seine Formulierungsgrundlage, nicht seinen Gegenstand (SRC-003:704, :713). Folge: TRC-004 **bricht** und ist neu zu bewerten (GATE-A0). |
| 2026-07-20 | 1 (Runde 6) | **Web-Erstreckung aus dem kanonischen CAN-099-Wortlaut entfernt** (Nutzerauftrag Schritt 3); die vier nicht belegten Accessibility-Details (Fassung „2.2", Bedienflächen, Fokusführung, motorisch/assistiv) bleiben `ASSUMPTION`. Begründung ist **fehlende Deckung, kein Widerspruch** — die Quellen bejahen die Existenz der Web-Artefakte. Der Schnitt ist **nur synchron** über PRD, Evidence Ledger und Traceability gültig (§7.6.2). |
| 2026-07-20 | 1 (Runde 6) | **REQ-007 als `ASSUMPTION` bestätigt** und inhaltlich vollständig erhalten (Nutzerauftrag Schritt 4). Ausdrücklich festgehalten: die `MISSING`-Werte im PRD und in der Traceability betreffen die **Zielwertachse** und sind korrekt — sie werden **nicht** auf `ASSUMPTION` harmonisiert (das wäre eine Hochstufung). Offen bleibt nur die Feldbenennung (§8 Punkt 49). |
| 2026-07-20 | 1 (Runde 6) | **§3.3 neu:** Wesentlichkeitsprüfung bei Teilbelegung als reine **Berichtsregel** mit W1/W1b/W2/W3, Nullifikator, Kettenregel, Zirkularitätsvorbehalt und der offengelegten Lücke „Rollenfehler". **Kein neues Feld, kein neues Vokabular, kein Eingang der Blocking-Formel** — belegt daran, dass `CAN-`, `REQ-` und `VIS-` das Feld `blocking` gar nicht führen (§3.1). Platzierung in eigenem §3.3 statt in §3.2, Abweichung dort gemeldet. |
| 2026-07-20 | 1 (Runde 6) | **§7.6 (Migration Runde 6)** neu mit Herabstufungstabelle und sechs Nachzugsaufträgen; **§8 auf 51 Punkte** fortgeschrieben. **§13.2 tatsächlich fortgeschrieben:** Quellen und Validatoren liegen seit Schritt 1 des Nutzerauftrags im Repository (`docs/sources/`, `scripts/validation/`) — §8 Punkte 13 und 33 werden dadurch **nicht** geschlossen. |

## 12. Bestätigung

Diese Registry ist **nicht** vom Nutzer bestätigt. Die Assistenz bestätigt sie nicht in seinem
Namen. Höchster erreichbarer Stand nach dieser Korrektur: `READY_FOR_USER_CONFIRMATION`.

## 13. Freeze-Vermerk — Metamodell und Validatoren (2026-07-20)

**Dieser Abschnitt vergibt, ändert oder deprecatet keine ID.** Er hält ausschließlich fest, was ab
Abschluss der Runde vom 2026-07-20 eingefroren ist. Der ID-Bestand selbst war bereits vorher
eingefroren und bleibt es.

### 13.1 Was eingefroren ist

| Gegenstand | Umfang |
|---|---|
| **Metamodell** | Achsen und ihre Vokabulare (`source_type`, `measurement_type`, `evidence_status`, `item_type`, Release-Stufen), die Blocking-Formel `status NOT IN [resolved]` (fail-closed, §3.1), die Beschränkung von `blocking` auf die Räume `OQ-` und `CONTRA-`, die Zählregel §10.2 |
| **Validatorkette** | `validate_intake.py`, `validate_trace.py`, `check_prd.py`, `validate_schema.py`, `selftest_validator.py`, `verify.py`, `verify_canvas.py`, `xcheck.py`, `oq_check.py`, `blocking_model.py`, `intake-package.schema.json` |
| **Ankersemantik** | wird **nicht** weiter maschinell geführt. Ab jetzt ausschließlich **review-geführt** über die manuelle Ankerreview-Tabelle. Es wird **kein** neuer Semantikvalidator gebaut. |

Letzte Änderung vor dem Freeze: `intake-package.schema.json` wurde **additiv** erweitert
(`validation.run_date`, `.run_scope`, `.delta_to_previous_run`, `.failed_check_diagnosis`,
`.other_validators`, root `tooling_freeze`), damit `intake-package.json` die **echte** Ausgabe des
Laufs vom 2026-07-20 tragen kann. Ohne diese Erweiterung wäre die Datei nur dadurch schemakonform
geblieben, dass sie den veralteten Stand `33/5` weitergeführt hätte. Keine Regel wurde gelockert,
kein Feld entfernt, kein Pflichtfeld optional gemacht. Protokolliert in
`x_schema_change_log`.

### 13.2 ⚠️ Die Werkzeuge sind KEINE Repository-Dateien — offener Punkt, kein gelöster

`blocking_model.py` und **sämtliche** oben genannten Werkzeuge liegen im **Scratchpad** der
laufenden Session:

```
/private/tmp/claude-501/-Users-vincentschnetzer-Documents-Run-Bike/
    5ad02448-3a52-4a17-affc-d652ef4b5345/scratchpad/
```

Daraus folgt, unbeschönigt:

- **Ein Freeze ändert daran nichts.** Eingefroren wird ein Stand, kein Ablageort.
- **Außerhalb dieser Session sind die Werkzeuge nicht verfügbar.** Jedes in
  `docs/validation/validation-report.md` berichtete Validatorergebnis ist dann **nicht
  reproduzierbar** — weder durch den Nutzer noch durch einen späteren Agenten.
- **§8 Punkt 13** („Kein ausführbarer Validator für die Regeln in Abschnitt 2") und
  **§8 Punkt 33** („keine gemeinsame Implementierung der kanonischen Blocking-Funktion") bleiben
  **OFFEN**. Die Scratchpad-Werkzeuge schließen sie **nicht**. Wer sie für geschlossen hielte,
  würde einen Sitzungsartefakt für einen Repository-Bestand halten.
- **§9** („Stand der Werkzeuge") beschreibt damit weiterhin einen Sollzustand, keinen Ist-Zustand
  des Repositorys.

Die Überführung ins Repository ist ein **eigener, ausdrücklich zu beauftragender Schritt**. Sie ist
in dieser Runde nicht erfolgt und wurde nicht begonnen — es wurde kein Verzeichnis angelegt und
keine Datei ins Repository kopiert.

**Fortschreibung 2026-07-20 (Runde 6): die Überführung ist inzwischen erfolgt.** Schritt 1 des
Nutzerauftrags vom 2026-07-20 hat sie beauftragt und ausgeführt. Am 2026-07-20 im Repository
verifiziert:

- `docs/sources/` führt **SRC-001 … SRC-004** als Dateien (`SRC-001-REVYR-Vision-Canvas-PRD.md`,
  `SRC-002-REVYR-Plan-PRD.md`, `SRC-003-REVYR-GESAMTPLAN-FINAL.md`,
  `SRC-004-tracking-and-planned-routes.md`).
- `scripts/validation/` führt die gesamte oben genannte Werkzeugkette **einschließlich**
  `blocking_model.py`, `intake-package.schema.json` und `src-verification.json` (131 Zellen,
  109 BELEGT / 17 TEILBELEGT / 5 UNBELEGT), dazu `HASHES.md`, `EQUIVALENCE.md` und `run_all.sh`.

Daraus folgt, ebenso unbeschönigt:

- Die Absätze oben beschreiben den Stand **vor** dieser Überführung und werden nicht gelöscht.
- **§8 Punkt 13 und Punkt 33 bleiben trotzdem OFFEN.** Ein Ablageortwechsel ist kein
  Ausführungs- und kein Äquivalenznachweis. In Runde 5 wurde **kein** Validator ausgeführt,
  **kein** Ergebnis reproduziert und **keine** Äquivalenz zum Scratchpad-Stand geprüft. Wer aus
  der bloßen Anwesenheit der Dateien schlösse, die Punkte seien geschlossen, würde genau den
  Fehlschluss begehen, den der ursprüngliche Absatz in die Gegenrichtung benennt.
- `docs/SOURCE-MAP.md` verortet `src-verification.json` weiterhin „außerhalb des Repositories".
  Diese Angabe ist **überholt**; der Nachzug steht in §7.6.2. Nach §1 gilt bis dahin diese
  Registry.
- Ein **Regelvorschlag, der die Nichtverfügbarkeit von `src-verification.json` als neuen BLOCKER
  aufnehmen wollte, wurde deshalb NICHT übernommen** — er wäre sachlich falsch gewesen. Die
  Begründung steht hier statt als Blockerzeile in §8.

### 13.3 Was ein Auftauen erfordern würde

Ein Auftauen ist **nur** durch eine ausdrückliche Nutzerentscheidung möglich, und nur bei einem
dieser Anlässe:

1. Eine **neue oder geänderte SRC-Quelle** (SRC-001…SRC-004 ändern sich, oder das Konzeptdokument
   `RUNNING_CYCLING_APP_KONZEPT_CHAT_ZUSAMMENFASSUNG.md` wird als Quelle aufgenommen).
2. Eine **neue ID-Klasse** oder ein **neues Achsenvokabular**.
3. Eine **Nutzerentscheidung, die eine bestehende Achse umdefiniert** (etwa die Blocking-Formel
   oder die Release-Stufen).
4. Die **Überführung der Werkzeuge ins Repository** (§13.2) — sie ist selbst ein Eingriff in den
   eingefrorenen Stand.

Ausdrücklich **kein** Auftaugrund: ein fehlgeschlagener Check. Ein Fehlschlag ist ein **Befund** und
wird am Dokument behoben, **nicht** am Werkzeug. Drei bekannte Werkzeug-Falschmeldungen
(`verify.py` D-Tally mit hartkodiertem Literal, `verify_canvas.py` ohne Honorierung maskierter
Pipes, `oq_check.py` mit unvollständigem Themenklassifikator) sind in dieser Runde bewusst **nicht**
korrigiert worden und in `docs/validation/validation-report.md` §1 offengelegt.

### 13.4 Was NICHT eingefroren ist

Dokumentinhalte, die Auflösung von Blockern, die Vergabe von IDs durch den Nutzer und die manuelle
Ankerreview. Der Freeze betrifft das **Prüfwerkzeug und das Metamodell**, nicht den Bestand, der
geprüft wird.
