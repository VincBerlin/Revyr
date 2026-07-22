# Source Map

Feature Slug: `revyr-endurance-platform`  
Stand: 2026-07-20 (**Runde 6**: Quellen und Validatorkette ins Repository überführt (§1.6); vier
zuvor als BELEGT geführte Zellen nachgeprüft und herabgestuft (§1.3.1). Vorstand: **Runde 5** —
SRC-001…SRC-004 aufgefunden, Belegbehauptungen einzeln geprüft)  
Confirmation Status: `pending-user-confirmation` — diese Datei bestätigt nichts.

> ⚠️ **Der Gesamtstatus bleibt `BLOCKED_TRACEABILITY`.** `true-line-status` `pending-watcher`,
> `wired-in-prod` `no`, `evidence-class` `none`, `self-certified` `false`. Das Auffinden der
> Quelldokumente ist **keine** Freigabe und **kein** Watcher-Verdikt. Es existiert kein Code.

## Geltung und ID-Disziplin

Diese Datei ist die Definitionsstelle des ID-Raums `SRC-`. Alle anderen Dokumente
**referenzieren** SRC-IDs nur.

⚠️ **Korrektur 2026-07-19: die Registry verwaltet zwölf ID-Räume, nicht zehn.** Die Vorfassung
dieses Abschnitts zählte `VIS-`, `CAN-`, `REQ-`, `AC-`, `TRC-`, `EV-`, `RISK-`, `ASM-`, `OQ-` und
`CONTRA-`. Im Auftau-Schritt 2 sind **`USER-` und `NFR-`** hinzugekommen (Registry §5.1, §6.12,
§6.13). Die Aussage wurde **nicht** stehen gelassen, weil sie der Registry jetzt widerspräche.

⚠️ **Grenzfall, sichtbar gemacht statt still entschieden.** `docs/ID-REGISTRY.md` ist die
kanonische Quelle dieser zwölf Räume und ab Phase 2 eingefroren. `SRC-` gehört ausdrücklich
**nicht** dazu: Registry §5.2 führt `SRC-` als nicht beauftragten, ungeschützten ID-Raum und
markiert die Aufnahme als OPEN QUESTION. Die IDs `SRC-006`…`SRC-008` sind **außerhalb der
eingefrorenen Registry** entstanden — zulässig, weil `SRC-` registryfremd und diese Datei sein
alleiniger Definitionsort ist, aber ein bewusster Grenzfall. **OPEN QUESTION an den Nutzer:** soll
`SRC-` in die ID-Registry aufgenommen werden? Bis dahin ist `SRC-` gegen genau den
Kollisionsdefekt ungeschützt, den die Registry für die anderen Räume behebt.

⚠️ **In diesem Nachzug wurde KEINE neue SRC-ID vergeben.** Der Bestand bleibt `SRC-001`…`SRC-008`.
Wo eine ID fehlt, steht unten ein **BLOCKER** (§2.1), keine erfundene Nummer. Bestehende IDs
wurden **nicht** umgedeutet und nicht umnummeriert: `SRC-001`…`SRC-008` behalten Nummer und
Bedeutung; ergänzt wurden ausschließlich Verfügbarkeits- und Messbefunde.

## 1. Upstream-Quellen der Anforderungen (`SRC-001`…`SRC-005`)

Diese Quellen sind die **Eingaben**, aus denen der Plumbline-Artefaktsatz abgeleitet wurde. Sie
sind nicht mit den Artefakten identisch.

| Source ID | Kind | Source Type | Verfügbar | Summary |
|---|---|---|---|---|
| SRC-001 | external-artifact | EXPLICIT | **ja — seit 2026-07-20 im Repository** unter `docs/sources/` (§1.6); Original außerhalb, gelesen 2026-07-20 | REVYR Vision, Product Canvas und PRD; enthält Produktvision, Zielgruppen, Core Loops, Release-Scope und Feature-Anforderungen (REQ-IDs H/T/M/A/S/G/R/L/W, NFRs). |
| SRC-002 | external-artifact | EXPLICIT | **ja — seit 2026-07-20 im Repository** unter `docs/sources/` (§1.6); Original außerhalb, gelesen 2026-07-20 | REVYR Plan-PRD; enthält die Anforderung-zu-Task- und Gate-Zuordnung. |
| SRC-003 | external-artifact | EXPLICIT | **ja — seit 2026-07-20 im Repository** unter `docs/sources/` (§1.6); Original außerhalb, gelesen 2026-07-20 | REVYR Gesamtplan FINAL; enthält Produktidentität, Design-System, Kernsystem-Spezifikationen, Release-Fahrplan, Arbeitspakete 1–17, Store-Matrix, Nachweisregeln und 24 Risiken. |
| SRC-004 | external-artifact | EXPLICIT | **ja — seit 2026-07-20 im Repository** unter `docs/sources/` (§1.6); Original außerhalb, gelesen 2026-07-20 | Run&Bike Tracking + Planned Routes Implementation Plan; TDD-Detailplan (12 Tasks) für den frühen Tracking-Prototyp, teilweise veraltet. |
| SRC-005 | consistency-review | EXPLICIT | teilweise — als Befundsatz in `docs/validation/validation-report.md` (Datum 2026-07-18) | Statische Konsistenzprüfung vom 2026-07-18: identifizierte Konflikte bei Branding, Bike-Metriken, GPS-Datenmodell, Routenfortschritt, Persistenz, API-Key-Sicherheit, Traceability und v1-Scope. |

### 1.1 Fundorte, Maße und Prüfsummen (selbst gemessen am 2026-07-20)

Die SHA-256-Summen sind mit `shasum -a 256` selbst berechnet, nicht aus einer Vorlage übernommen.

⚠️ **Korrektur vom 2026-07-20 (Runde 6) — die Vorfassung dieses Absatzes ist überholt und wird
ersetzt, nicht stehen gelassen.** Sie lautete: „Die Dateien liegen **außerhalb** des Repositories
und wurden ausschließlich **gelesen**. Sie wurden **nicht** ins Repository kopiert und **nicht**
verändert." Der zweite Satz gilt nicht mehr: die vier Dateien sind inzwischen unter
`docs/sources/` ins Repository **kopiert** worden (§1.6). Unverändert richtig bleibt, dass die
**Originale** an den unten verzeichneten Fundorten liegen, dort nur gelesen und **nicht** verändert
wurden, und dass die Kopien byte-identisch sind — selbst nachgerechnet am 2026-07-20, alle vier
Summen stimmen mit dieser Tabelle überein (§1.6).

**Kanonischer Stand — Desktop** (jeweils neuer und größer als die Nebenkopie):

| ID | Pfad | Bytes | mtime | SHA-256 |
|---|---|---:|---|---|
| SRC-001 | `/Users/vincentschnetzer/Desktop/docs/REVYR-Vision-Canvas-PRD.md` | 24.585 | 2026-07-18 02:52 | `d0a6adf4e1f2be843eb9e93896164755cd417bdd591c1bd415e9c8dc2874f0d3` |
| SRC-002 | `/Users/vincentschnetzer/Desktop/docs/REVYR-Plan-PRD.md` | 10.525 | 2026-07-16 23:51 | `37e090aafac7a3c7278c61164cb342018dea7530c995f73f7f5add220fd16542` |
| SRC-003 | `/Users/vincentschnetzer/Desktop/docs/superpowers/plans/2026-07-10-REVYR-GESAMTPLAN-FINAL.md` | 61.117 | 2026-07-18 02:52 | `c3ceb46fa52c487530546370fc6682e6df7e7b66b35f4c6eb55a4b3e77e3764d` |
| SRC-004 | `/Users/vincentschnetzer/Desktop/docs/superpowers/plans/2026-07-10-tracking-and-planned-routes.md` | 78.355 | 2026-07-10 03:19 | `dc18a97d9fe2299662933120391207264ecbb40d16bc98a129e545a9f37bc25f` |

**Älterer Nebenstand — Downloads** (nicht kanonisch, nur zur Nachvollziehbarkeit verzeichnet;
abweichende Prüfsumme = abweichender Inhalt, nicht bloß abweichender Ablageort):

| ID | Pfad | Bytes | SHA-256 |
|---|---|---:|---|
| SRC-001 | `/Users/vincentschnetzer/Downloads/REVYR-Vision-Canvas-PRD.md` | 20.916 | `30910d1b62af6d909cd392fba706c0e72bc6ec3ad0c9af92216acfb352162db4` |
| SRC-002 | `/Users/vincentschnetzer/Downloads/REVYR-Plan-PRD.md` | 9.495 | `4a92f13f7294431ac7ff28762080a9a2ab2b75f291ec34ac79f21674a7a1f627` |
| SRC-003 | `/Users/vincentschnetzer/Downloads/REVYR-GESAMTPLAN-FINAL.md` | 45.597 | `e54e62ecc830f6901ac98a30dee83d2560ff7bc5647fffc6c7c70b3510d71367` |

⚠️ **SRC-004 hat keine Nebenkopie.** Für die anderen drei existieren zwei inhaltlich
verschiedene Fassungen. Sämtliche Prüfungen dieser Runde wurden **ausschließlich gegen den
Desktop-Stand** geführt. Wer gegen die Downloads-Fassung prüft, prüft gegen ein anderes Dokument.

**Offene Beobachtung, nicht weginterpretiert: Datum.** SRC-001 und SRC-003 tragen im Fließtext
den Stand `2026-07-16`; die Desktop-Dateien haben mtime `2026-07-18`. Ein mtime ist **kein**
Autorendatum — ein Kopier-, Sync- oder Editorvorgang setzt ihn ebenfalls. Ob der Textstand
zwischen dem 16. und dem 18. inhaltlich fortgeschrieben wurde oder die Datei nur bewegt wurde,
ist **aus den Dateien nicht entscheidbar**. Es wird hier weder ein Widerspruch behauptet noch
eine Erklärung eingesetzt. Hinzu kommt die schon zuvor verzeichnete Diskrepanz zu den
Dateinamen (`2026-07-10`). **Zu klären vom Nutzer.**

**Zusätzlich aufgefunden, nicht beauftragt, KEINE ID vergeben:**
`/Users/vincentschnetzer/Downloads/RUNNING_CYCLING_APP_KONZEPT_CHAT_ZUSAMMENFASSUNG.md`
(29.451 Bytes, 2026-07-10 02:48, SHA-256
`00f898fa9c1a3a71705628b3945aa932c19b375d052885658ecb18ae1c3deb98`). Das ist das
Konzeptdokument, auf das SRC-003 und SRC-004 durchgehend mit `§`-Verweisen zitieren (z. B. §2,
§14–17, §20, §27–28, §33, §36). Es ist damit die **Referenzebene unterhalb** von SRC-003 — ein
erheblicher Teil der dortigen Paragraphenverweise ist erst mit dieser Datei auflösbar. Es wird
hier **nur gemeldet**; eine SRC-ID vergibt ausschließlich der dafür vorgesehene Schritt.

### 1.2 WIDERLEGT: die Prämisse „vier von fünf Upstream-Quellen sind nicht auffindbar"

**Die Vorfassung dieses Abschnitts ist falsch und wird ersetzt, nicht stehen gelassen.** Sie
hielt fest: „`find docs -type f` (2026-07-19) listet dreizehn Markdown-Dateien. Keine davon ist
SRC-001, SRC-002, SRC-003 oder SRC-004." Diese Messung war für **das Repository** richtig und
bleibt richtig — die Dateien liegen dort weiterhin nicht. Der daraus gezogene **Schluss** war
falsch: aus „nicht im Repository" wurde „nicht auffindbar" und daraus „nicht belegfähig". Die
Dokumente existieren, sind lesbar und wurden am 2026-07-20 vollständig gelesen (§1.1).

`CONTRA-001` (`docs/decisions/decision-log.md`, resolved) bleibt insoweit gültig, als die in
`CLAUDE.md` genannten **repo-relativen Pfade** tatsächlich nicht existieren. Der Befund war ein
**Pfadfehler in `CLAUDE.md`**, kein fehlendes Dokument. Dieser Unterschied ist nicht kosmetisch:
er entscheidet darüber, ob 131 Zellen unbelegbar sind oder nur falsch adressiert waren.

⚠️ **Was daraus ausdrücklich NICHT folgt.** Die Existenz einer Quelle belegt keine einzige
konkrete Aussage. Deshalb wurde **keine** Zelle allein deswegen hochgestuft, weil ihr
Belegdokument jetzt vorliegt. Stattdessen wurde jede der 131 Zellen **einzeln gegen den
Quelltext gelesen** (§1.3).

Folge, **neu gemessen am 2026-07-20 nach Runde 4** über die vier tragenden Artefaktdateien
(Canvas, PRD, Traceability, Vision). **Messmethode offengelegt:** gezählt werden Tabellenzellen,
deren Inhalt exakt `EXPLICIT` ist; die Zuordnung zu SRC-001/SRC-003 bzw. „ohne SRC" erfolgt über
die übrigen Zellen derselben Tabellenzeile. **Neu gemessen, nicht fortgeschrieben.**

| Befund | Anzahl | Verteilung |
|---:|---:|---|
| `EXPLICIT`-Zellen gesamt | **218** | Canvas 95, PRD 94, Traceability 12, Vision 17 |
| davon mit Berufung auf `SRC-001` oder `SRC-003` | **131** | Canvas 90, PRD 31, Vision 10 |
| davon **ohne jede** SRC-Angabe | **85** | PRD 63, Traceability 10, Canvas 5, Vision 7 |

**Veränderung gegenüber der Messung vom 2026-07-19 (222 / 131 / 87) — und warum sie erneut kein
Fortschritt beim Belegproblem ist:**

| Datei | 2026-07-19 | **2026-07-20** | Grund |
|---|---:|---:|---|
| Canvas | 93 | **95** | Runde 4 hat CAN-099, CAN-139 und CAN-141 auf `EXPLICIT` gesetzt (CAN-139 vorher ASSUMPTION). **Kein neuer Beleg:** die Grundlage ist eine **Nutzersetzung vom 2026-07-20**, die selbst **keine SRC-ID** hat (§2.1) und deren Wortlaut laut Registry §8 Punkt 43 **ohne Gegenbestätigung** ist. |
| PRD | 98 | **94** | Teilung von REQ-040 und Feldbereinigungen; **keine neue Quelle**. |
| Traceability | 14 | **12** | Entfernung semantisch falscher Anker in Runde 4. **Nicht durch neue Belege, sondern durch Wegfall.** |
| Vision | 17 | **17** | unverändert |

⚠️ **Der wichtigste Befund dieser Messung ist die Richtung, in die die Canvas-Zahl zeigt.** Sie
ist **gestiegen**, weil drei Items auf `EXPLICIT` gesetzt wurden — und zwar auf der Grundlage
einer Entscheidungstranche, die selbst **nicht referenzierbar belegt** ist (§2.1). Wer nur die
Zahl liest, sieht eine Verbesserung der Belegdichte. **Es ist keine.** Ein `EXPLICIT`, dessen
Quelle „Nutzerentscheidung 2026-07-20" im Freitext heißt, ist genauso wenig nachschlagbar wie
eines, das sich auf das fehlende SRC-003 beruft — es hat nur noch keinen Namen für sein Problem.

Die beiden Teilmengen sind **nicht mehr derselbe Befund** und werden ab hier getrennt geführt:

- Die **131** berufen sich auf `SRC-001`…`SRC-004`. Diese Dokumente liegen vor. Jede dieser
  Zellen ist gegen den Quelltext prüfbar — und wurde geprüft (§1.3).
- Die **85** tragen den Source Type `EXPLICIT`, ohne überhaupt eine Quelle zu nennen. **Für sie
  ändert sich nichts.** Sie sind nicht prüfbar, weil sie nichts benennen, wogegen zu prüfen wäre.
  Sie bleiben **BLOCKER** beim Owner PRD/Canvas/Vision. Von den drei früher angebotenen Optionen
  ist für sie keine anwendbar: es fehlt nicht das Dokument, es fehlt die Angabe.

Option 2 der Vorfassung („`SRC-001`…`SRC-004` als `external-artifact` mit dokumentiertem Fundort
führen") ist mit §1.1 **umgesetzt**.

⚠️ **Korrektur vom 2026-07-20 (Runde 6).** Die Vorfassung hielt fest: „Option 1 (Dateien ins
Repository legen) wurde **nicht** ausgeführt: die Quelldateien sind nur gelesen worden; Kopieren
läge außerhalb des zulässigen Änderungsbereichs." Das ist überholt — **Option 1 ist inzwischen
ausgeführt** (§1.6). Der damalige Grund (Kopieren nicht beauftragt) ist durch den Nutzerauftrag
vom 2026-07-20 entfallen; er war kein inhaltlicher Einwand.

Option 3 gilt nach der Nachprüfung vom 2026-07-20 für die **sechs** Zellen aus §1.3, deren
Aussage in der Quelle nachweislich **nicht** steht (fünf aus Runde 5, CAN-109 neu aus §1.3.1).

### 1.3 Einzelprüfung der 131 Zellen gegen den Quelltext (2026-07-20)

**Methode.** Die vier Quelldokumente wurden vollständig gelesen. Für jede der 131 Zellen wurde
die behauptete Aussage im beanspruchten Quelldokument gesucht. Maßstab: **wortnahe Deckung**.
Wo eine Zwischenstufe nötig gewesen wäre, um von der Quelle zur Aussage zu kommen, gilt die
Aussage **nicht** als belegt — eine Ableitung über ein Zwischenglied ist kein Beleg.
Maschinenlesbares Einzelergebnis mit Fundstelle je Zelle:
`scripts/validation/src-verification.json` (131 Einträge; **seit dem 2026-07-20 im Repository**,
zuvor `scratchpad/src-verification.json` außerhalb — §1.6).

⚠️ **Die Datei bildet den Stand VOR der Nachprüfung §1.3.1 ab.** Sie ist byte-identisch aus dem
Scratchpad übernommen worden und trägt deshalb weiterhin `ergebnis = {"BELEGT": 109,
"TEILBELEGT": 17, "UNBELEGT": 5}` sowie in `quellen[*].pfad` die **Desktop-Pfade**, nicht die
Repo-Pfade. Selbst gemessen am 2026-07-20: 133 Vorkommen der Zeichenfolge `Desktop`. Sie
widerspricht damit der Tabelle unten. **Diese Datei ändert sie nicht** — der Nachzug ist in §5
geführt. Wer die JSON als Zählstand liest, liest den Stand vor Runde 6.

| Verdikt | Anzahl | Canvas | PRD | Vision |
|---|---:|---:|---:|---:|
| **BELEGT** — Aussage steht wortnah in der beanspruchten Quelle | **105** | 74 | 24 | 7 |
| **TEILBELEGT** — ein benennbarer Teil fehlt | **20** | 10 | 7 | 3 |
| **UNBELEGT** — Aussage steht dort nicht | **6** | 6 | 0 | 0 |
| **UNGEPRÜFT** | **0** | 0 | 0 | 0 |
| Summe | **131** | 90 | 31 | 10 |

**Herabstufung protokolliert, nicht still ausgetauscht (2026-07-20, Runde 6).** Bis zum
2026-07-20 lautete diese Tabelle **109 BELEGT · 17 TEILBELEGT · 5 UNBELEGT** (Canvas 77/8/5,
PRD 24/7/0, Vision 8/2/0). Vier Zellen sind nachgeprüft worden und halten nicht:
**CAN-119**, **CAN-024** und **VIS-003** wandern von BELEGT nach TEILBELEGT, **CAN-109** von
BELEGT nach UNBELEGT. Grund, Fundstelle und wörtliches Zitat je Zelle in §1.3.1. Die
Grundgesamtheit bleibt 131; es wurde nichts hinzugefügt und nichts hochgestuft.

⚠️ **Eine Zahl dieser Tabelle ist strittig.** Bei **CAN-119** ist zwischen den Prüflinsen
umstritten, welche Hälfte des Items der Nachprüfung standhält (§1.3.1). Unter der einen Lesart
ist die Zelle TEILBELEGT, unter der anderen UNBELEGT. Hier steht die **konservative** Einstufung
TEILBELEGT — „mindestens ein benennbarer Teil fehlt" ist unter beiden Lesarten wahr, während
UNBELEGT nur unter einer wahr wäre. Fällt die Entscheidung anders aus, lauten die Zahlen
**105 / 19 / 7** (Canvas 74/9/7). **Diese Datei entscheidet den Streit nicht.**

**Die Canvas-Belegbasis trägt — mit sechs benannten Ausnahmen.** 74 von 90 Canvas-Zellen stehen
wortnah in SRC-001 bzw. SRC-003, viele davon nahezu wörtlich (Non-Goals, Risiken,
Erfolgssignale, Nachweisarten). Das ist der Befund, den die Vorfassung nicht haben konnte.

⚠️ **Und die Gegenrichtung, damit dieser Abschnitt nicht einseitig liest:** die sechs UNBELEGT
sind **keine Formfehler**, sondern Aussagen, die in **keiner** der vier Quellen vorkommen. Vier
der fünf aus Runde 5 betreffen Wettbewerbsumfeld und Nachweisarten, also genau die Stellen, an
denen branchenübliches Vorwissen leicht als Quellenaussage durchgeht. Die sechste (CAN-109,
Runde 6) betrifft das Risikoregister und ist derselbe Fehlertyp: eine Schutzregel der Quelle
wurde als Risikoaussage gelesen (§1.3.1).

| Zelle | Aussage | Befund | Herabstufung auf |
|---|---|---|---|
| **CAN-041** | „Apple Fitness" als Current Alternative | Kommt in **keiner** Quelle vor. „Apple" erscheint ausschließlich als Plattform/Dienst (Sign in with Apple, HealthKit, Apple Maps, Apple Watch). Die Wettbewerberliste der Quellen lautet abschließend: Whoop, Garmin, Strava. | ASSUMPTION oder MISSING |
| **CAN-042** | „Google/Fitbit" als Current Alternative | „Fitbit" kommt in **keiner** Quelle vor. „Google" nur als Auth-Anbieter, Play Store und Kartenanbieter. | ASSUMPTION oder MISSING |
| **CAN-046** | „Lokale Event-Plattformen" als Current Alternative | Kommt in **keiner** Quelle vor. SRC-003 führt lokale Events ausschließlich als **eigenes Feature** (Plan 14), nicht als Alternative. Der bisherige Canvas-Vermerk meldete nur fehlende Stärke/Lücke — tatsächlich fehlt die Alternative selbst. | ASSUMPTION oder MISSING |
| **CAN-109** *(neu 2026-07-20, §1.3.1)* | „Anti-Cheat-Fehler (False Positives gegen reale Nutzer)" als Risiko | Kommt in **keiner** Quelle vor. „False Positive", „fälschlich", „Einspruch", „Appeal", „Confidence" und „Datenschutz": je **0 Treffer** über alle vier Quellen (selbst gemessen 2026-07-20). SRC-003:265/:559 stellen eine **Urteilsregel** auf („Fehlende Sensoren allein sind kein Betrug, senken aber die Beweiskraft"), kein Risiko der Fehlklassifikation. Das Risikoregister SRC-003:690–717 hat keine entsprechende Zeile. | ASSUMPTION oder MISSING |
| **CAN-110** | „Private oder gesperrte Sportanlagen" als Risiko | Kommt in **keiner** Quelle vor. SRC-003 Risiko 23 betrifft die **OSM-Datenqualität** (fehlende/falsch geschnittene Plätze), nicht Zugänglichkeit oder Rechtsstatus. Zwei verschiedene Risiken. | ASSUMPTION oder MISSING |
| **CAN-112** | „Integrationstests" als Evidence-Annahme | Der Begriff kommt in **keiner** Quelle vor. SRC-003 §9 zählt abschließend auf: Unit-/Component-Tests, Smoke Test, echtes Gerät, GPS real, Run-/Bike-Modus, iOS/Android. | ASSUMPTION oder MISSING |

**Diese Datei stuft nichts herab** — der Canvas gehört einem anderen Owner. Der Nachzug ist in §5
als BLOCKER geführt.

**Ein Sonderfall unter den TEILBELEGT: CAN-113 ist nicht schwach belegt, sondern falsch
adressiert.** „Referenzstrecken" steht **nicht** in SRC-003, wohl aber wörtlich in SRC-001
(„Distanzabweichung < 3 % auf bekannter Referenzstrecke") und in SRC-002
(„Referenzstrecken-Messung, Ledger"). Die Aussage ist belegt — die SRC-Angabe ist es nicht. Die
Korrektur ist ein Quellenwechsel, **keine** inhaltliche Herabstufung.

**Wiederkehrendes Muster unter den TEILBELEGT — dreimal dieselbe Lücke.** VIS-008, REQ-023 und
REQ-001 verlangen alle **„versionierte"** Faktoren bzw. Konfigurationsobjekte. Das Wort
„versioniert" erscheint in SRC-003 ausschließlich für **Datenbank-Migrationen**, nie für
Effort-Faktoren oder Sport-Konfigurationen. Die Anforderung mag richtig sein — belegt ist sie
nicht, und sie hat sich von VIS-008 in zwei Requirements fortgepflanzt. Zweites Muster:
**„Unsicherheit"/„Confidence"** in VIS-007, CAN-052 und REQ-012 — „Confidence" kommt in keiner
der vier Quellen vor.

### 1.3.1 Nachprüfung von vier BELEGT-Verdikten (2026-07-20, Runde 6)

Vier Zellen, die §1.3 als **BELEGT** geführt hat, sind gegen die jetzt im Repository liegenden
Quellen (§1.6) einzeln nachgeprüft worden. **Keine der vier hält.** Die Verdikttabelle oben ist
entsprechend korrigiert; hier steht je Zelle, was wortnah trägt und was nicht.

⚠️ **Was hier herabgestuft wird und was nicht.** Herabgestuft wird das **Prüfverdikt dieser
Datei**, nicht der `source_type` fremder Zellen. Canvas und Vision gehören anderen Ownern; der
Nachzug ist in §5 als BLOCKER geführt. Es wurde **keine ID vergeben, kein Item umgedeutet und
nichts hochgestuft**. Alle Absenzbefunde unten sind am 2026-07-20 über alle vier Quelldateien
selbst gemessen, nicht übernommen.

| Zelle | bis 2026-07-20 | neu | trägt wortnah | trägt nicht |
|---|---|---|---|---|
| **CAN-119** (`canvas.md:301`) | BELEGT | **TEILBELEGT** *(strittig, s. u.)* | die Sichtbarkeits-Matrix als geprüfte Testtabelle und GATE-B-Bedingung | die Benennung „Privacy-"; „Privacy-Review" als eigener Nachweisvorgang |
| **VIS-003** (`vision.md:18`) | BELEGT | **TEILBELEGT** | Tracking, verständliche statt abstrakte Auswertung, Fortschritt, Anschluss an lokale Sportler und Teams | die Qualifizierer „verlässlich" und „sicher"; „Trainingspartner", „Zugang", „Fortschrittssignale" |
| **CAN-024** (`canvas.md:151`) | BELEGT | **TEILBELEGT** | „Radfahrer:innen" als primäre Zielgruppe | „Renn-" (steht nur im *sekundären* Punkt); „Freizeit-" bezogen auf Radfahrende |
| **CAN-109** (`canvas.md:286`) | BELEGT | **UNBELEGT** | — (nichts) | die gesamte Aussage; die Quelle stellt eine Urteilsregel auf, kein Risiko |

**CAN-119 — die Fundstellen sind echt, aber sie tragen einen anders benannten Gegenstand.**
Die drei Belege des Altverdikts stimmen wörtlich: SRC-003:363 „**Sichtbarkeits-Matrix
(Testtabelle in Plan 7):**", SRC-003:522 „Matrix als Testtabelle, jede Zeile geprüft",
SRC-003:683 GATE B „**Sichtbarkeits-Matrix vollständig getestet**"; zweitbelegt SRC-001:192
„Sichtbarkeits-Matrix als Testtabelle". Alle drei sagen **Sichtbarkeits-Matrix**, nicht
Privacy-Matrix. `privacy[- ]?matrix`, `privacy[- ]?review` und `datenschutz`: **je 0 Treffer**
über alle vier Quellen. Um von „Sichtbarkeits-" auf „Privacy-" zu kommen, braucht es die
Zwischenstufe „Sichtbarkeitsstufen sind Privacy-Einstellungen" — die nimmt keine Quelle vor.

⚠️ **Einwand aus der Gegenprüfung, hier nicht weggelassen — die Richtung der Aufspaltung ist
umstritten.** Eine Prüflinse hält dem Befund entgegen, dass nicht die Matrix, sondern der
**Review** das herkunftsechte Glied ist: der Ursprungstext des Canvas führt in
`canvas.md:555` wörtlich „**- Claims-, Privacy- und Threat-Model-Reviews.**" — die elliptische
Aufzählung expandiert zu Claims-Review / Privacy-Review / Threat-Model-Review, also CAN-118 /
CAN-119 / CAN-120. Eine Matrix nennt dieser Ursprungstext **nicht**. Danach wäre „Privacy-Matrix"
das Anhängsel ohne Herkunft und CAN-119 insgesamt **UNBELEGT**, während die Matrix bereits als
EV-018 („Sichtbarkeits-Matrix") quellentreu geführt wird — eine Verengung von CAN-119 auf die
Matrix erzeugte dann ein zweites Exemplar desselben Nachweises. **Dieser Streit ist hier nicht
entschieden**; die Tabelle oben führt deshalb die konservative Einstufung.

Zwei weitere Einwände sind belegt und werden mitgeführt: (a) **CAN-118 und CAN-120 tragen
dieselbe quellenlose „-Review"-Prägung** — in den Quellen stehen nur die Grundbegriffe
(SRC-003:686 „Claims juristisch freigegeben", SRC-003:626 „**Juristische Claims-Prüfung**",
SRC-003:602 „**Threat-Model Standortfreigabe** + Sicherheitsmodell"). CAN-119 isoliert zu
behandeln ließe zwei gleichartige Fälle stehen. (b) Der Satz „ein Privacy-Prüfvorgang kommt in
keiner Quelle vor" ist **zu weit**: SRC-003:629 nennt für Task 17.4 „(Opt-in, sensibelste
Datenklasse, **eigene Privacy-Prüfung**)" und SRC-003:715 „**DSGVO-Prüfung in 10.2**". Beide sind
an **eine Datenklasse und einen Plan-Task** gebunden — sie tragen keinen querschnittlichen
Nachweisvorgang, aber sie existieren. Richtig ist deshalb: *ein Privacy-Review als benannter,
gate-blockierender Abnahmevorgang* kommt in keiner Quelle vor.

**VIS-003 — das Altverdikt hat aus drei Fundstellen eine Verbundaussage gebaut.** Das
Einzelergebnis begründet das Altverdikt selbst mit einer Komposition: „sicherer Zugang zu
lokalen Trainingspartnern" wurde aus SRC-001:26 + :51 (Finden/Anschluss) **plus** :98 und :196
(Schutzmechanismen) zusammengesetzt. Genau das ist die Ableitung über ein Zwischenglied, die der
Maßstab ausschließt: SRC-001:98 („Live-Standort: Opt-in pro Aktivität …") schützt den Nutzer,
der **seinen** Standort teilt; SRC-001:196 (S-06 UGC-Sicherheit) ist eine funktionale
v2.0-Anforderung. Keine der beiden sagt etwas über die Sicherheit des **Zugangs zu Personen**.
`trainingspartner`, `zugang`, `verlässl` und `fortschrittssignal`: **je 0 Treffer** über alle
vier Quellen. SRC-001:47 zählt die Nutzerprobleme abschließend auf — „**Ich verstehe meinen
Fortschritt nicht · Ich habe niemanden · Es gibt kein Ziel außer mir selbst.**" — Sicherheit ist
keines davon.

⚠️ **Einwände aus der Gegenprüfung, sichtbar statt geglättet.** (a) Der Absolutsatz „keine Quelle
verbindet Sicherheit mit dem Kontakt zu lokalen Sportlern" **hält nicht**: die Quellen führen
sehr wohl eine Schutzarchitektur um den sozialen Kontakt — SRC-001:36 „Profile standardmäßig
privat", SRC-003:374 „privates Profil → „Follower-Anfrage" mit Annehmen/Ablehnen", SRC-003:524
„Blockierter findet Nutzer nirgends". Sie führen sie nur **nie als Nutzerbedürfnis**. Der Befund
ist auf diese engere Fassung zu bringen; sein Ergebnis ändert sich dadurch nicht.
(b) Daraus folgt **nicht**, dass `CAN-017` („MISSING – Sicherheitsproblem") seine Grundlage
verliert: SRC-003:704 „Live Location = Stalking-Risiko" und SRC-003:713 „Einzel-Reviere verraten
Wohngebiet/Lauf-Routine" tragen ein Sicherheitsproblem **unabhängig** von VIS-003. **CAN-017 ist
nicht aufzulösen**, sondern allenfalls auf eine quellenfeste Grundlage umzuhängen — Entscheidung
des Nutzers, nicht dieser Datei.
(c) Die Verengung ist **nicht folgenlos**: `traceability.md:426` benennt „verlässliches Tracking"
ausdrücklich als *tragende Klausel* von TRC-004, und REQ-004 liegt auf **GATE-A0**. Ferner tragen
`CAN-028` („Verlässliches Tracking") und `CAN-031` („Trainiere sicherer") dieselben Qualifizierer
und sind mitzuprüfen. Diese Folgen sind hier **gemeldet, nicht ausgeführt** — fremde Owner.
(d) **Gegen ein Übermaß bei der Verengung:** eine weitere Prüflinse hält fest, dass ein zu knapper
Ersatzwortlaut („Anschluss an lokale Sportler und Teams") wortnah gedeckten Gehalt mit
wegschnitte. SRC-001:22 lautet „**Echte Gemeinschaft** — Teams, die zusammen trainieren, sich
real treffen und gemeinsam ihr Revier verteidigen", SRC-001:47 „keinerlei Grund, sich real zu
treffen", SRC-003:64 „gemeinsam laufen". Gemeinsames Training und reales Treffen sind auf
Bedürfnisebene belegt und dürfen beim Verengen **nicht** entfallen. Auch das ist eine
Owner-Entscheidung; hier wird kein Wortlaut gesetzt.

**CAN-024 — die Verschmelzung löscht eine Rangaussage, die die Quelle ausdrücklich macht.**
SRC-001:51 lautet „**Primär:** Freizeit-Läufer:innen und Radfahrer:innen …", SRC-001:52
„**Sekundär:** Ambitionierte Rennradfahrer und Läufer mit festen Strecken und Leistungsfokus".
Das Wort „Rennrad" steht in SRC-001 **nur** in Zeile 52 — unter der Rangmarkierung *Sekundär*
und untrennbar mit „Ambitionierte" verbunden. Das Präfix „Freizeit-" ist orthographisch nur an
„Läufer:innen" gebunden; es auf „Radfahrer:innen" zu verteilen ist eine Zwischenstufe. Belegt
bleibt „Radfahrer:innen".

⚠️ **Einwand aus der Gegenprüfung — und er trifft, selbst nachgeprüft.** Der Befund hielt
zusätzlich die Herkunftsangabe „Prosa 'Users / Customers'" für unbelegt, weil diese Zeichenfolge
in keiner der vier Quellen vorkommt (`customers`: 0 Treffer — stimmt). **Der Schluss ist
trotzdem falsch**, weil er zwei Tabellenspalten verwechselt: die Kopfzeile `canvas.md:148` führt
`Source` und `Herkunft` als **zwei getrennte** Spalten (`ID · Aussage · Source Type · Source ·
Herkunft · Befund / Hinweis`),
und `canvas.md:474–476` erklärt ausdrücklich: „Die folgenden Abschnitte sind der **wörtliche
Ursprungstext** des Canvas. Sie belegen die Herkunft der atomaren Items". Dort steht
`canvas.md:482` „**## Users / Customers**" und `canvas.md:484` „**- Freizeit-Läufer:innen und
Radfahrer:innen.**". Die Herkunftsangabe ist damit **canvas-intern und zutreffend**; strittig ist
allein die **Source**-Spalte. Sie ist **nicht** zu löschen. — Offengelegt bleibt die Alternative:
SRC-003:65 führt „**- Radfahrer/Rennradfahrer:** längere Distanzen, feste Stammstrecken,
Sensorik, Gruppenausfahrten" als **eine** ungestufte Rad-Zielgruppe; ein Quellenwechsel auf
`SRC-001/SRC-003` deckte den Renn-Anteil wortnah, „Freizeit-" weiterhin nicht. **Nutzerentscheidung,
hier nicht getroffen.**

**CAN-109 — eine Schutzregel ist als Risiko gelesen worden.** SRC-003:265 sagt: „Fehlende
Sensoren allein sind kein Betrug, **senken aber die Beweiskraft**"; SRC-003:559 (Task 10.2)
„fehlende Sensoren allein ≠ Betrug". Das ist eine Regel, **wie** geurteilt werden darf — nicht
ein Risiko, **dass** falsch geurteilt wird. SRC-003:265 nennt als Rechtsfolge fehlender Sensoren
ausdrücklich die gesenkte Beweiskraft und gerade **nicht** `verified=false`; die Stelle schließt
den Fall, den CAN-109 als Risiko beschreibt, an dieser Stelle also aus. Das Risikoregister
SRC-003:690–717 enthält keine Zeile dazu: Nr. 8 (:701) ist die **Gegenrichtung** (= CAN-104),
Nr. 12 (:705) betrifft Fehlalarme der **Sturzerkennung**, Nr. 22 (:715) den Datenschutz der
Sensor-Plausibilität. SRC-004 trägt zu Anti-Cheat nichts bei. Damit bleibt **kein belegter Rest**
— deshalb UNBELEGT und nicht TEILBELEGT.

⚠️ **Einwand aus der Gegenprüfung — die Herkunftsangabe ist NICHT mit zu streichen.** Zwei
Prüflinsen halten fest, dass „CAN-008, nur Prosa 'Risks'" die canvas-interne Zerlegungsherkunft
bezeichnet und zutrifft; **selbst nachgeprüft und bestätigt**: der Ursprungstext-Abschnitt
`canvas.md:542` „## Risks" ist Prosa und lautet in `canvas.md:544` wörtlich „Kritisch sind
GPS-/Batterierisiken, Health-Claims, Standortmissbrauch, **Anti-Cheat-Fehler**, Geo-Komplexität,
**private Sportanlagen**, Store-Policies und Namenskollision." Die Zerlegung ist also belegt —
nur eben **gegen den Canvas selbst**, nicht gegen SRC-003. Eine dritte Prüflinse hatte behauptet,
auch dieser Canvas-Abschnitt sei prosafrei; **das ist widerlegt** — sie hat den Atom-Abschnitt
`canvas.md:273` statt den Ursprungstext `canvas.md:542` gelesen. Es fällt daher die
**Source**-Angabe (SRC-003), nicht die **Herkunft**. Nebenbefund: derselbe Satz `canvas.md:544`
nennt auch „private Sportanlagen" und erklärt damit die identische Lage bei **CAN-110**, das
bereits als UNBELEGT geführt wird.

### 1.4 Was diese Prüfung an bestehenden Befunden erschüttert (Owner: PRD, Vision, Registry)

Mehrere Herabstufungen und Blocker im Bestand sind **ausdrücklich damit begründet worden, dass
SRC-001/SRC-003 nicht auffindbar seien.** Diese Begründung ist entfallen. Das heißt **nicht**,
dass die Herabstufungen falsch waren — die meisten stehen auf **zwei** Beinen, und das zweite
Bein ist unberührt. Es heißt, dass sie **neu zu bewerten sind**, und zwar von ihren Ownern:

| Fundstelle | Wortlaut der Begründung | Status nach dieser Prüfung |
|---|---|---|
| `prd.md:921` (REQ-015) | „Anker CAN-075 trägt `EXPLICIT` via **SRC-001 = nicht auffindbar**" | Prämisse entfallen. **CAN-075 ist BELEGT** (SRC-001 §3.2 „kein Marktplatz/Kaufkosmetik", §2.9 „kaufbare Avatare/Boosts", Werte-Tabelle „niemals kaufbar"). Der zweite Grund (analytische Nullschwelle) trägt weiter. |
| `prd.md:922`, `prd.md:1263` (REQ-018) | „‚Profile standardmäßig privat' stammt aus VIS-009, Quelle SRC-001 = nicht auffindbar" | Prämisse entfallen. **VIS-009 ist BELEGT**, nahezu wörtlich (SRC-001 Werte-Tabelle: „Profile standardmäßig privat, Live-Standort Opt-in mit Zeitlimit … Health-Daten nie für Werbung"). Der analytische Grund trägt weiter. |
| `prd.md:926`, `prd.md:1613` (REQ-035) | „Anker CAN-114/CAN-123 tragen `EXPLICIT` via **SRC-003 = nicht auffindbar**" | Prämisse entfallen. **CAN-114 und CAN-123 sind BELEGT** (SRC-003 §9: „Kein Task ist fertig ohne Ledger-Eintrag"; „Run und Bike werden getrennt nachgewiesen"). Der analytische Grund trägt weiter. |
| `prd.md:958` (REQ-001), `prd.md:1076`, `prd.md:1213` | „Anker … tragen `EXPLICIT` über SRC-001/SRC-003, die laut `docs/SOURCE-MAP.md` …" | Prämisse entfallen; Ankerlage je Zeile in §1.3 nachzuschlagen. |
| `traceability.md:270`, `:526` | „… laut `docs/SOURCE-MAP.md` **nicht auffindbar**" | Prämisse entfallen. |
| `vision.md:63`, `vision.md:153` | „USER-001…003 … **nicht im Repository auffindbar (BLOCKER)**" | Prämisse entfallen. **USER-001, USER-002 und USER-003 sind BELEGT** — SRC-001 §3.3 führt genau diese drei Personas aus, „faire Bike-Wertung" steht dort wörtlich. |
| `ID-REGISTRY.md:1131–1133` | „Source Type EXPLICIT via SRC-001 — **nicht auffindbar**" | Prämisse entfallen (Registry ist eingefroren; Nachzug erst nach Auftauen). |

⚠️ **Symmetriehinweis, damit dieser Abschnitt nicht als Freigabe gelesen wird.** Kein
`source_type` wird von hier aus hochgestuft. Die Beweislatte des PRD (`prd.md:345`) verlangt für
`EXPLICIT` u. a. „der Wert steht in einer belegten Nutzerquelle" — diese Bedingung ist für die
109 BELEGT-Zellen **jetzt erfüllbar geworden**, aber die Prüfung, ob sie im Einzelfall den
**Zielwert** und nicht nur die **Anforderung** trägt, ist Sache des PRD-Owners. Die
Unterscheidung „Anforderung belegt / Zielwert unbelegt", die das PRD-Nachaudit sauber eingeführt
hat, bleibt vollständig gültig und wird durch diese Prüfung **nicht** aufgeweicht.

### 1.5 Sonderbefunde zu den fünf Punkten der Runde 5 — mit Nachträgen aus Runde 6

**REQ-007 — die Klassifikation hält, aber aus einem anderen Grund als angenommen.** REQ-007
(„‚verbleibend' MUSS entlang der geplanten Geometrie berechnet werden und darf nicht nur
Gesamtdistanz minus gelaufene Distanz sein") ist im PRD bereits `ASSUMPTION | SRC-005` und
gehört damit **nicht** zu den 131. Diese Einstufung ist **richtig — und stärker begründet als
bisher dokumentiert**: SRC-004 spezifiziert das **Gegenteil**. Wörtlich:

```
export function remainingDistanceMeters(plannedMeters: number, coveredMeters: number): number {
  return Math.max(0, plannedMeters - coveredMeters);
}
```
mit dem Test `it('subtracts covered from planned', ...)`. SRC-001 und SRC-003 sagen zum
Rechenweg **gar nichts** (nur „geplante vs. verbleibende km"). REQ-007 ist damit eine bewusste
**Abweichung von SRC-004**, getragen von SRC-005/DEC-004 — keine Ableitung aus SRC-001/SRC-003.

**Nachtrag 2026-07-20 (Runde 6): der Träger ist schwächer, als die Formulierung nahelegt — und
REQ-007 bleibt inhaltlich unangetastet.** Der Nutzerauftrag vom 2026-07-20 hält REQ-007 als
route-aware Verbesserung **vollständig aufrecht** und schreibt lediglich `ASSUMPTION` bis zur
ausdrücklichen Nutzerbestätigung fest. Diese Datei ändert das PRD nicht; sie hält nur die
Beleglage fest, die diese Einstufung stützt. Zwei nachgeprüfte Punkte kommen hinzu: **DEC-004
steht auf `proposed`** (`docs/decisions/decision-log.md:10` — „einfache Distanzsubtraktion ist
fachlich falsch | *proposed* | nach Feldtest"), verbietet also nichts; und **SRC-005 ist keine
Nutzerquelle**, sondern ein Befundsatz über dem Artefaktsatz (§1 Tabelle; §4 führt
`docs/validation/validation-report.md` ausdrücklich als „keine Eingangsquelle"). Ferner sind die
numerischen Schwellen dieser Anforderung nirgends belegt: `korridor`, `hysterese`, `projektion`,
`monoton`, `routebezogen`/`routenbezogen`, `falsche richtung`, `richtungsumkehr` ergeben **je 0
Treffer** über alle vier Quellen (selbst gemessen 2026-07-20).

⚠️ **Einwand aus der Gegenprüfung: der behauptete `source_type`-Widerspruch existiert womöglich
nicht.** Es ist beanstandet worden, dass REQ-007 im PRD als `ASSUMPTION` (`prd.md:181`) und im
Messblock als `MISSING` (`prd.md:1063`, `traceability.md:517`) geführt wird. Eine Prüflinse hält
dem entgegen, dass beide Felder **verschiedene Fragen** beantworten: `prd.md:350` definiert
`source_type` als Herkunft des **Zielwerts**, `prd.md:549` führt für die Anforderungsebene eigens
`requirement_source_type`, und `traceability.md:318` überschreibt die Liste als
„**MISSING-Schwellen (13)**". Danach wäre `MISSING` für die fehlende Korridor-/Hysterese-Schwelle
**richtig** und dürfte nicht auf `ASSUMPTION` harmonisiert werden — das wäre eine Hochstufung
eines korrekten Abwesenheitsbefundes. Eine dritte Linse zieht daraus den umgekehrten Schluss und
hält `MISSING` auch für die Anforderungszeile für richtig. **Dieser Streit ist hier nicht
entschieden und gehört dem PRD-Owner.** Festgehalten wird nur: die Abwesenheit der Schwellen ist
gemessen und bleibt Abwesenheit.

⚠️ **Daraus folgt ein neuer Befund am Canvas:** **CAN-051** („Echte routebezogene Restdistanz")
steht auf `EXPLICIT | SRC-001/SRC-003`. Der tragende Qualifier „echte routebezogene" steht in
keiner der beiden Quellen, und die einzige Quelle, die den Rechenweg überhaupt festlegt,
schreibt das Gegenteil vor. CAN-051 ist **TEILBELEGT** und trägt eine Quellenangabe, die seinen
Kern nicht deckt. Nachzug beim Canvas-Owner: Quelle auf SRC-005/DEC-004 umstellen.

⚠️ **Einwand aus der Gegenprüfung vom 2026-07-20, hier nicht unterschlagen — der Nachzug darf
kein voller Quellen*tausch* werden.** Zwei Punkte, beide selbst nachgeprüft:

1. **Der Vorwurf eines „Zirkelbelegs" trägt nicht.** Es ist eingewandt worden, die Herkunftsangabe
   „CAN-005, Prosa 2 ('echte routebezogene Restdistanz')" verweise auf `canvas.md:505` und damit
   auf den Canvas selbst. Das ist richtig, aber kein Defekt: `canvas.md:148` trennt **Source** und
   **Herkunft** als zwei Spalten, und `canvas.md:474–476` erklärt den Ursprungstext ausdrücklich
   zum Herkunftsbeleg. Die Herkunft ist canvas-intern und korrekt; strittig ist allein die
   **Source**-Spalte. Derselbe Einwand gilt für CAN-024 (§1.3.1) und CAN-109 (§1.3.1) — es ist
   ein durchgängiges Lesemuster, kein Einzelfall.
2. **Ein Teil von CAN-051 ist in SRC-001/SRC-003 sehr wohl gedeckt.** SRC-001:160 („Modus B: Route
   per Wegpunkte planen oder km-Ziel; **geplante vs. verbleibende km**") und SRC-003:682 (GATE A
   „**verbleibende km korrekt**"). Wird SRC-001/SRC-003 aus der Source-Spalte **entfernt**,
   verliert ein wörtliches GATE-A-Kriterium seinen Canvas-Anker. Ungedeckt ist nur der Qualifier
   „echte routebezogene" (`routebezogen`/`routenbezogen`: 0 Treffer) und das Verbot der
   Subtraktion. Der sachgerechte Nachzug ist deshalb **Herabstufung des Source Type plus
   Ergänzung** von SRC-005/DEC-004, nicht der Austausch der Quelle.

Der BLOCKER in §5 bleibt bestehen; er ist um diesen Einwand zu lesen, nicht ohne ihn.

**REQ-019 — der Inhalt ist belegt; das Problem sitzt ausschließlich am Vision-Anker.** REQ-019
ist **BELEGT**, und zwar nahezu wörtlich: SRC-001 T-09 („Neue-Strecke-Erkennung + Empfehlung
(Chips + Freitext) an Follower; Übernahme mit 1 Tipp") und SRC-003 §4.2 („Post an Follower …
mit einem Tipp übernehmen"). Auch der Canvas-Anker **CAN-058 ist BELEGT**. Der in Runde 4
beanstandete Defekt betrifft **nur** die Vision-Ebene: `VIS-003` nennt Tracking,
Health-Auswertung, Fortschrittssignale und Trainingspartner — **keine Routenempfehlung**. Die
Kette „Feed → Entdeckungsfläche → Zugang" bleibt eine Ableitung über ein Zwischenglied und
**trägt nicht**; sie wird hier ausdrücklich **nicht** rehabilitiert. Geprüft wurde zusätzlich,
ob ein **anderes** der elf aktiven Vision-Items REQ-019 trägt: **keines**. Das ist ein
**fehlendes Vision-Item**, kein Quellenproblem — BLOCKER, Owner Nutzer (ID-Vergabe nur durch den
ID-Owner nach Auftauen). Es wird hier **keine** VIS-ID genannt und **kein** bestehendes Item
umgedeutet.

**OQ-002 (Repository-Owner/DRI) — bleibt MISSING.** Keine der vier Quellen benennt eine
verantwortliche Person, Rolle oder Organisation. Die Quellen sind Produkt- und Planungsdokumente
ohne Owner-Angabe. **Durch die Quellen nicht schließbar.**

**OQ-003 (Minimum iOS/Android und Referenzgeräte) — bleibt MISSING, aber nicht leer.** Die
Quellen **fordern** Referenzgeräte ausdrücklich (SRC-001 NFR Batterie: „Ziel < 10 %/h auf
Referenzgeräten"; SRC-003 §9 Ledger-Zeilen „Echtes Gerät ✅ Modell + OS", „iOS geprüft ✅
Version") — sie **benennen** aber weder ein Gerätemodell noch eine Mindest-OS-Version. Der
Bedarf ist belegt, die Antwort fehlt. **Durch die Quellen nicht schließbar; es wird kein Gerät
geraten.**

**OQ-004 (Karten-/Routinganbieter) — der Status `MISSING` unterschätzt die Beleglage.** Die
Quellen enthalten sehr wohl eine Stufe-A-Festlegung, und zwar konkret:

- SRC-003 §5.4: „**Stufe A: react-native-maps** (Apple Maps iOS / Google Android) +
  **OpenRouteService** (foot-walking / cycling-regular). **Anbieter-Review vor Stufe B**
  (Kosten: Google-Preise, ORS-Limits; Alternativen **Mapbox, MapLibre+OSM**) → ADR."
- SRC-001 §3.6 Punkt 3: „Karten-/Routing-Anbieter: **Kosten-ADR vor v2.0** (Start:
  react-native-maps + OpenRouteService)."

Damit sind **Startanbieter, Prüfzeitpunkt, Prüfkriterien und Alternativen benannt**; offen ist
allein der **finale** Anbieterentscheid vor Stufe B. ⚠️ **OQ-004 wird hier nicht geschlossen** —
das ist der Entscheidung des Nutzers und dem Owner der Open Questions vorbehalten, und der
finale Entscheid ist tatsächlich offen. Der Befund lautet: die Frage ist **enger** als
verzeichnet.

**Leere VIS-Platzhalter — der Inhalt ist in den Quellen vorhanden.** `VIS-012` und `VIS-013`
werden als `Content MISSING · Source Type MISSING` geführt mit der Begründung, eine Aussage auf
Vision-Ebene wäre „neue Produktsubstanz". Diese Begründung war unter der alten Prämisse richtig
und ist es jetzt nicht mehr:

| ID | Vorgesehene Aussage | Fundstelle in den Quellen |
|---|---|---|
| **VIS-012** | Monochromes, tokenbasiertes Designsystem; Farbe nur mit fachlicher Bedeutung | SRC-003 §2 **als Designprinzip auf oberster Ebene**: „**Designprinzip: ‚Farbe muss man sich verdienen.'** Die App ist konsequent monochrom — Farbe existiert nur, wo sie Bedeutung trägt." §2.1 zählt die zulässigen Bedeutungsfarben abschließend auf (Teamfarben · Einzel-Revier · **Gold** für Sportplätze · Health-Ampel · Feier-Momente) und hält fest: „Run-/Bike-Modus … unterscheidet sich durch Ikonografie + Typo-Akzent, **nicht durch Farbe**." SRC-003 §11 führt es als **entschieden** („Design ✅"). Zusätzlich SRC-001 M-04. |
| **VIS-013** | Datenportabilität: Nutzer können ihre Aktivitätsdaten in offenem Format mitnehmen | SRC-003 §8 Store-Matrix wörtlich: „**Datenexport | A/2.8 | GPX-Export erfüllt Portabilität**". SRC-001 NFR Privacy/DSGVO: „In-App-Löschung vollständig, **Datenexport**"; T-06 „GPX-Export | **Fremd-App öffnet Datei**". |

⚠️ **Es wird hier kein Vision-Item gefüllt und keine VIS-ID vergeben.** Das ist Sache des
Vision-Owners und des Nutzers. Der Befund ist nur: die Formulierung müsste **nicht mehr erfunden
werden** — sie ließe sich aus benannten Fundstellen ableiten, statt neue Produktsubstanz zu
setzen. Das ändert die Art des Blockers von „inhaltlich nicht ableitbar" zu „noch nicht
entschieden".

**Nebenbefund zu CAN-139/AC-039/OQ-016.** Der Canvas führt als OPEN QUESTION (Registry §8
Punkt 36), der kanonische CAN-139-Wortlaut nenne „in einer kompatiblen Fremdanwendung öffnen"
nicht mehr, weshalb AC-039 (d) und EV-039 nicht mehr wörtlich belegt seien. **Die Quellen tragen
diese Klausel wörtlich:** SRC-001 T-06 „GPX-Export | **Fremd-App öffnet Datei**" und SRC-003
Task 2.8 „GPX-Export (Share Sheet) | **Fremd-App öffnet Datei**". Die Abnahmebedingung ist also
belegt. **OQ-016 bleibt davon unberührt:** keine Quelle benennt eine **konkrete**
Referenz-Fremdanwendung. Es wird keine App geraten.

**Nachtrag 2026-07-20 (Runde 6): CAN-099 — die Accessibility-Pflicht ist auf Web-Auskopplungen
erstreckt, ohne dass eine Quelle das tut.** CAN-099 (`canvas.md:263`) gehört **nicht** zu den 131
aus §1.3: seine Source-Spalte nennt keine SRC-ID, sondern „Nutzerentscheidung 2026-07-20" — es
zählt damit zu den **85** Zellen aus §1.2, die `EXPLICIT` tragen, ohne eine Quelle zu benennen
(§2.2). Der Nutzerauftrag vom 2026-07-20 verlangt, die Erstreckung „und ihre nutzbaren
Web-Auskopplungen" zu entfernen; die übrigen nicht belegten Accessibility-Details bleiben
`ASSUMPTION`. **Diese Datei ändert den Canvas nicht**; sie hält die Beleglage fest.

Gemessen am 2026-07-20 über alle vier Quellen: `Auskopplung` erscheint **ausschließlich in
SRC-003** und dort **viermal**, jedes Mal in der CSS-Farbmisch-/Transparenzregel — SRC-003:83
„Gilt für alle Web-Auskopplungen (Erfolgskarten-Renderer, Beschützer-Web-Link,
Marketing-Seiten)", SRC-003:484, SRC-003:711, SRC-003:735. **Keine** dieser vier Stellen betrifft
Accessibility. Der einzige Accessibility-Abschnitt aller vier Quellen ist SRC-003 §2.4
(„## 2.4 Accessibility & Plattformkonventionen", :98) — er nennt Web nicht und schließt mit einer
reinen iOS/Android-Zeile (:102). Die Kette „§2.1 erstreckt die Farbregel auf Web, also gilt auch
§2.4 dort" ist eine Ableitung über ein Zwischenglied. Ebenfalls je **0 Treffer**: `wcag 2` (die
Fassungsziffer „2.2" steht nirgends — die vier WCAG-Stellen SRC-001:176, SRC-001:256, SRC-002:134
und SRC-003:100 sagen alle fassungslos „WCAG AA"), `motor`, `bedienfl`, `assistiv`, `fokusf`,
`barrierefr`. Wortnah gedeckt bleibt der Kern: SRC-001:256 „WCAG AA-Kontraste, Dynamic Type/Font
Scaling, Screenreader-Labels, Farben nie einziger Informationsträger".

⚠️ **Einwand aus der Gegenprüfung — die Streichung darf nicht falsch begründet werden.** Es ist
argumentiert worden, die Web-Erstreckung widerspreche der Quelle „in der Richtung", weil
SRC-001:132 einen Web-Client als Nicht-Ziel führe. **Das hält dem Zitat nicht stand:** die Zeile
lautet vollständig „kein Web-Client (**außer Beschützer-Link**)", und SRC-001:238 führt den
Beschützer-Web-Link als Lieferitem L-03. Die Quellen **bejahen** die Existenz des
Prüfgegenstands. Der Defekt ist ein reiner **Belegmangel**, kein Widerspruch — so und nur so ist
die Streichung zu begründen. Ein zweiter Einwand ist mitzuführen: die Erstreckung steht bereits
in AC-037 und NFR-005, die Fassungsziffer „2.2" sogar in einer Pass-Bedingung und einem als
store-release-blockierend geführten Nachweis. Eine Streichung allein im Canvas ließe ein
Akzeptanzkriterium mit einer Vorbedingung ohne Upstream-Anker zurück. **Der Nachzug ist deshalb
synchron zu führen** — Owner Canvas und PRD, nicht diese Datei.

**MISSING (fortbestehend):** Datumsdiskrepanz — siehe die offene Beobachtung in §1.1.

### 1.6 Überführung der Quellen und Werkzeuge ins Repository (2026-07-20, Runde 6)

Auf Nutzerauftrag vom 2026-07-20 sind die vier Quelldokumente und die Validatorkette ins
Repository überführt worden. **Das ändert den Fundort, nicht die Beleglage.** Kein Verdikt aus
§1.3 ist dadurch besser geworden; die Nachprüfung §1.3.1 hat vier davon sogar verschlechtert.

⚠️ **Es wurde KEINE SRC-ID vergeben und KEINE umgedeutet.** `SRC-001`…`SRC-004` behalten Nummer
und Bedeutung; ergänzt ist ausschließlich ein **zweiter, repo-relativer Fundort**. Der Bestand
bleibt `SRC-001`…`SRC-008`.

#### Quelldokumente — `docs/sources/`

Selbst gemessen am 2026-07-20 mit `shasum -a 256`, nicht aus `scripts/validation/HASHES.md`
übernommen. Alle vier Summen stimmen mit der Tabelle in §1.1 überein — der Kopiervorgang hat den
Inhalt nicht angetastet.

| ID | Repo-Pfad | Bytes | SHA-256 | Vergleich mit §1.1 |
|---|---|---:|---|---|
| SRC-001 | `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md` | 24.585 | `d0a6adf4e1f2be843eb9e93896164755cd417bdd591c1bd415e9c8dc2874f0d3` | **identisch** |
| SRC-002 | `docs/sources/SRC-002-REVYR-Plan-PRD.md` | 10.525 | `37e090aafac7a3c7278c61164cb342018dea7530c995f73f7f5add220fd16542` | **identisch** |
| SRC-003 | `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md` | 61.117 | `c3ceb46fa52c487530546370fc6682e6df7e7b66b35f4c6eb55a4b3e77e3764d` | **identisch** |
| SRC-004 | `docs/sources/SRC-004-tracking-and-planned-routes.md` | 78.355 | `dc18a97d9fe2299662933120391207264ecbb40d16bc98a129e545a9f37bc25f` | **identisch** |

Die **Originale** unter `~/Desktop/docs/` bestehen unverändert fort; ihre Summen sind ebenfalls
nachgerechnet und stimmen. **Zeilennummern sind damit stabil:** jede Fundstellenangabe dieser
Datei gilt gegen beide Fundorte gleichermaßen.

#### Werkzeuge — `scripts/validation/`

20 Einträge, selbst gezählt am 2026-07-20: 16 Werkzeug- und Datendateien plus `README.md`,
`HASHES.md`, `EQUIVALENCE.md` und `__pycache__/`.
Die Kette wird über `scripts/validation/run_all.sh` aufgerufen; Prüfsummen, Ausschlussliste und
bekannte Werkzeugdefekte stehen in `scripts/validation/HASHES.md` und
`scripts/validation/README.md`. **Diese Datei wiederholt sie nicht und bestätigt sie nicht.**

Für den Beleghaushalt hier relevant ist genau ein Artefakt:
`scripts/validation/src-verification.json` (76.857 Bytes) — das maschinenlesbare Einzelergebnis
der 131 Zellprüfungen, auf das §1.3 verweist. Es lag zuvor außerhalb des Repositories und ist
damit erstmals **dauerhaft referenzierbar**.

#### Was diese Überführung erledigt

| Bisheriger Befund | Fundstelle | Stand nach der Überführung |
|---|---|---|
| „Die Dateien … wurden **nicht** ins Repository kopiert" | §1.1 | **überholt** — korrigiert in §1.1 |
| „Option 1 (Dateien ins Repository legen) wurde **nicht** ausgeführt" | §1.2 | **ausgeführt** |
| „`scratchpad/src-verification.json` (131 Einträge, **außerhalb des Repositories**)" | §1.3 | **erledigt** — jetzt `scripts/validation/src-verification.json` |
| `CLAUDE.md` nennt repo-relative Pfade, die nicht existieren | §5, `CONTRA-001` | **auflösbar geworden**, aber **nicht ausgeführt**: `CLAUDE.md` gehört einem anderen Owner. Der Nachzug bleibt offen — die dort genannten Pfade sind weiterhin falsch, jetzt aber ohne Not. |

#### Was sie ausdrücklich NICHT erledigt

Damit dieser Abschnitt nicht als Fortschritt beim Belegproblem gelesen wird:

1. **Kein Verdikt ist dadurch besser geworden.** Die Existenz einer Quelle im Repository belegt so
   wenig eine konkrete Aussage wie ihre Existenz auf dem Desktop. Es wurde **keine Zelle
   hochgestuft** (§5.2).
2. **Das Repository steht nicht unter Versionskontrolle.** Gemessen am 2026-07-20: kein
   `.git`-Verzeichnis. „Im Repository" heißt hier **nicht** „versioniert" — eine Kopie in einem
   unversionierten Verzeichnis kann spurlos geändert werden. Die einzigen Integritätsanker sind
   die SHA-256-Summen oben und in `scripts/validation/HASHES.md`. **Das ist eine echte
   Einschränkung, keine Formalie**, und sie ist der Grund, warum die Originale hier weiterhin
   mitgeführt werden.
3. **`src-verification.json` ist byte-identisch übernommen und damit inhaltlich veraltet.** Es
   trägt weiterhin `ergebnis = {"BELEGT": 109, "TEILBELEGT": 17, "UNBELEGT": 5}` — den Stand vor
   §1.3.1 — und in `quellen[*].pfad` die **Desktop-Pfade** (133 Vorkommen der Zeichenfolge
   `Desktop`, selbst gezählt). Es widerspricht der Verdikttabelle in §1.3. Nachzug in §5,
   **hier nicht ausgeführt.**
4. **Zwei Bezugsdokumente sind weiterhin nicht im Repository.** `scratchpad/semantic-review.md`
   (Ankerreview, Grundlage der 23 `trägt-teilweise`) und `scratchpad/id-migration.json` (§4)
   wurden bewusst nicht übernommen — `scripts/validation/HASHES.md` führt beide in seiner
   Ausschlussliste. Jede Regel, jeder Befund und jede Zahl, die sich auf sie stützt, bleibt
   **nicht referenzierbar belegt**. Das gilt insbesondere für eine Wesentlichkeitsregel zu
   „trägt-teilweise", falls sie auf diese Dateien aufsetzt.
5. **Das Konzeptdokument bleibt draußen.** `RUNNING_CYCLING_APP_KONZEPT_CHAT_ZUSAMMENFASSUNG.md`
   (§1.1) — Ziel der `§`-Verweise in SRC-003/SRC-004 — ist **nicht** kopiert worden und hat
   weiterhin **keine ID**. Ein erheblicher Teil der Paragraphenverweise in SRC-003 bleibt damit
   aus dem Repository heraus **nicht auflösbar**.
6. **Der ältere Nebenstand unter `~/Downloads/` besteht fort** (§1.1). Kopiert wurde ausschließlich
   der Desktop-Stand. Solange beide Fassungen existieren, bleibt „die Quelle" mehrdeutig — die
   OPEN QUESTION in §5 ist unverändert offen.
7. **Die Werkzeuge sind in diesem Vorhaben selbst verfasst.** Was §3 für `SRC-008` festhält, gilt
   sinngemäß für die Kette: ein grüner Lauf ist **kein unabhängiger Nachweis**. Der tatsächliche
   Lauf endet ohnehin mit Exit-Code 1 und vier FAILs, davon drei als Werkzeugdefekte aktenkundig
   (`scripts/validation/README.md`).
8. **Welcher Fundort kanonisch ist, ist nicht entschieden.** Repo-Kopie und Original sind heute
   byte-identisch; nichts hält sie identisch. **OPEN QUESTION an den Nutzer** (§5).

## 2. Bestätigte Nutzerentscheidungen (`SRC-006`)

| Source ID | Kind | Source Type | Im Repository vorhanden | Summary |
|---|---|---|---|---|
| SRC-006 | user-decision | CONFIRMED | ja — als Entscheidungsspur in `docs/decisions/decision-log.md` und `docs/decisions/open-questions.md` | Bestätigte Nutzerentscheidungen vom 2026-07-19, **erste Tranche**: A0-Routing-Proxy statt Client-Key (DEC-005 `user-confirmed`, CONTRA-002 resolved), Ablageort `infra/routing-proxy/` (OQ-011), Local-first-Präzisierung, Anti-Cheat-Datenminimierung (CONTRA-004), Historie vs. Accountlöschung (CONTRA-005). |

**Warum diese ID existiert.** Canvas und PRD trugen in der Spalte `Source` den Freitext
„Nutzerentscheidung 2026-07-19" statt einer SRC-ID — dieselbe Ad-hoc-Vergabe, die die ID-Registry
für andere Räume gerade abgestellt hat. `SRC-006` gibt diesen Fundstellen eine referenzierbare ID.

### 2.1 BLOCKER — die zweite Entscheidungstranche vom 2026-07-19 hat keine SRC-ID

Am 2026-07-19 ist eine **zweite, inhaltlich getrennte Tranche** von Nutzerentscheidungen getroffen
worden (Auftau-Schritt 2). Sie ist in `SRC-006` **nicht enthalten**:

| Entscheidung | Wirkung |
|---|---|
| C16 — `blocking_scope` ersatzlos entfallen, ersetzt durch `blocked_gates` + `blocked_activities` | Registry §3.1 |
| Projektweite Semantik von `evidence_status` (`not-planned` / `planned` / `pending` / `verified`) | Registry §3.2 |
| CAN-130 — Vollspezifikation des Erfolgssignals „übernommene Routen je Empfehlung" | Registry §6.3.2 |
| CAN-099 ausschließlich Accessibility (WCAG **2.2** AA) + eigenes Designsystem-Item CAN-141 | REQ-014 → REQ-037/REQ-038 |
| GPX-Export als eigene Requirement; REQ-034 nur sekundär | REQ-039 |
| Atomisierung von CAN-071 in drei Items auf zwei Release-Stufen | CAN-138/139/140, REQ-040 |
| CAN-022 ausschließlich Datenqualitätsproblem + Persona | USER-004 |
| NFR-008 definieren statt deprecaten | Registry §6.13.1 |

⚠️ **Es wurde KEINE neue SRC-ID vergeben, und `SRC-006` wurde NICHT stillschweigend erweitert.**
Beides wäre falsch:

- **`SRC-006` zu erweitern** hieße, einer bestehenden ID eine neue, größere Bedeutung zu geben.
  Jedes Dokument, das heute `SRC-006` referenziert, meinte die **erste** Tranche; die Referenz
  würde rückwirkend etwas anderes belegen. Genau diese stille Umdeutung verbietet die
  ID-Disziplin (Registry Regel 5).
- **Eine neue SRC-Nummer zu vergeben** wäre eine ID-Vergabe außerhalb des dafür vorgesehenen
  Schritts. Der Bestand ist ab Phase 2 festgeschrieben; wo eine benötigte ID fehlt, ist ein
  **BLOCKER** zu melden, nichts zu erfinden. **Es wird hier bewusst auch keine konkrete Nummer
  genannt** — ein ausgeschriebenes `SRC-0xx` im Fließtext wird von einer Textsuche als vergebene
  ID gelesen und wäre genau die Ad-hoc-Vergabe, die dieser Abschnitt ablehnt.

**Folge, neu gemessen am 2026-07-20:** der Freitext „Nutzerentscheidung 2026-07-19" steht in
`docs/canvas/…canvas.md` **20×**, in `docs/prd/…prd.md` **18×**, in `docs/ID-REGISTRY.md` **17×**,
in `docs/traceability.md` **7×** und in `docs/vision/…vision.md` **1×**. Der weit überwiegende
Teil davon gehört zur **zweiten** Tranche und ist damit **nicht** durch `SRC-006` gedeckt.

### 2.2 BLOCKER — eine **dritte** Entscheidungstranche (2026-07-20) hat ebenfalls keine SRC-ID

**Der Befund aus §2.1 hat sich nicht nur fortgesetzt, er hat sich vergrößert.** Am 2026-07-20 ist
eine **dritte, inhaltlich getrennte Tranche** von Nutzerentscheidungen getroffen worden (Runde 4).
Sie ist weder in `SRC-006` noch in der ungelösten zweiten Tranche enthalten:

| Entscheidung | Wirkung |
|---|---|
| Kanonische Wortlaute A (Accessibility), B (monochromes Designsystem), C (Datenportabilität/GPX) | CAN-099, CAN-141, CAN-139 — alle drei auf **Source Type EXPLICIT** gesetzt |
| Farbregel „Farbe ist niemals der einzige Informationsträger" wird kanonisch von CAN-099 getragen | doppelt geführte Pflicht CAN-099 ↔ CAN-141 einseitig aufgelöst |
| Teilung von CAN-140 in Planungs- und Auswertungsfunktion | CAN-142/143, REQ-041/042, AC-042/043, EV-043/044, TRC-041/042 |
| Vier semantisch falsche Vision-Anker (VIS-008 bei REQ-019…REQ-022) | TRC-019 → VIS-003, TRC-020/021 → VIS-004, TRC-022 → VIS-003 |
| Verbot der Schlusskette „Wahrnehmbarkeit als Vorstufe von Verständlichkeit" als Anker | REQ-037, REQ-038, REQ-039 ohne canvas-problem-Anker |
| Kanonische Trennung EV-008 / EV-039 | Registry §6.7, §7.5.3 |
| Der `NFR-`Raum führt **kein** `blocking` | Registry §6.13.2 |
| Zählstände ausschließlich aus der Registry, keine Literale als Erwartungs- oder Verbotswert | Registry §10.2 |

**Fundstellen des neuen Freitexts, gemessen am 2026-07-20:** „Nutzerentscheidung 2026-07-20" steht
in `docs/ID-REGISTRY.md` **7×**, in `docs/canvas/…canvas.md` **5×** und in `docs/prd/…prd.md`
**2×**.

⚠️ **Erneut wurde KEINE SRC-ID vergeben und `SRC-006` NICHT erweitert** — aus denselben zwei
Gründen wie in §2.1, die hier unverändert gelten und deshalb nicht wiederholt, sondern
**verschärft** festgehalten werden:

- Es gibt jetzt **drei** Tranchen und **eine** ID. Wer `SRC-006` referenziert, meint die **erste**.
  Zwei weitere Tranchen sind überhaupt nicht referenzierbar.
- **Der Schaden ist in Runde 4 erstmals messbar geworden:** drei Canvas-Items sind auf `EXPLICIT`
  hochgestuft worden (§1), und ihr Beleg ist die dritte Tranche — also **kein referenzierbares
  Artefakt**. Die `EXPLICIT`-Zahl des Canvas **steigt** damit, ohne dass ein einziger Beleg
  nachschlagbar geworden wäre. Registry §8 Punkt 43 führt für genau diese drei Items zusätzlich
  die fehlende **Gegenbestätigung** als BLOCKER.

**Zu entscheiden vom Nutzer:** je eine SRC-ID für die zweite **und** die dritte Tranche vergeben,
oder den Geltungsbereich von `SRC-006` ausdrücklich und **datiert** erweitern. Bis dahin ist der
Freitext in fünf Dateien **nicht referenzierbar belegt**.

**Nachzug erforderlich (nicht von hier aus geändert):** die Owner von Canvas, PRD und Registry
ersetzen den Freitext durch die jeweils zutreffende SRC-ID, sobald die obige Entscheidung
vorliegt. Diese Datei ändert Canvas, PRD und Registry nicht.

## 3. In diesem Lauf entstandene normative Artefakte (`SRC-007`, `SRC-008`)

Diese Einträge sind keine Anforderungsquellen im engeren Sinn, sondern **normative Artefakte**,
auf die sich andere Dokumente berufen. Sie erhalten SRC-IDs, damit dieser Bezug referenzierbar
statt prosaisch ist.

| Source ID | Kind | Source Type | Im Repository vorhanden | Summary |
|---|---|---|---|---|
| SRC-007 | governance-artifact | CONFIRMED | ja — `docs/ID-REGISTRY.md` (gelesen und verifiziert 2026-07-19, nach Auftau-Schritt 2) | ID-Registry: einzige kanonische Quelle für **zwölf** Präfixe — `VIS-`, `CAN-`, `REQ-`, `AC-`, `TRC-`, `EV-`, `RISK-`, `ASM-`, `OQ-`, `CONTRA-` sowie seit dem 2026-07-19 `USER-` und `NFR-` (§5.1). Enthält die Auflösung der ASM-Kollision (§6.9/§7.1), die Canvas-Atomisierung (§6.3/§7.2/§7.3), die Migration des Auftau-Schritts 2 (§7.4), die kanonische Blocking-Formel (§3.1) und die Ableitungsregel für die Zahl aktiver Requirements (§10.1). Ab Phase 2 **eingefroren**. |
| SRC-008 | intake-artifact | **CONFIRMED für die Existenz, MISSING für die Aktualität** | **ja — inzwischen vorhanden** (`intake-package.json`, Repository-Wurzel, 82.498 Bytes, gelesen 2026-07-19) | `intake-package.json`: maschinenlesbares Intake-Paket des Plumbline-Laufs. Enthält `id_counts`, `requirements`, `nfrs`, `open_questions`, `contradictions`, `validation`, `blockers`, `overall_status`. |

### SRC-008: jetzt vorhanden — **aber inhaltlich veraltet (BLOCKER)**

**Korrektur gegenüber der Vorfassung.** Sie hielt fest: „`ls intake-package.json` liefert am
2026-07-19 „No such file or directory"" und führte Inhalt und Schema als **MISSING**. Die Datei
**existiert inzwischen**. Die Aussage wurde geprüft und **ersetzt, nicht stehen gelassen**.

⚠️ **BLOCKER — der Inhalt bildet den Stand VOR dem Auftau-Schritt 2 ab.** Gelesen und gegen
`docs/ID-REGISTRY.md` §10 abgeglichen:

**Abgleich am 2026-07-20 wiederholt und neu abgeleitet** (Registry §10, §10.2 — Zählstände
ausschließlich aus den Registry-Definitionstabellen, keine Literale fortgeschrieben):

| Feld in `intake-package.json` | Stand dort | Stand der eingefrorenen Registry (2026-07-20) |
|---|---|---|
| `id_counts.REQ.active` | 36 | **40** aktiv · 2 deprecated · 1 Platzhalter |
| `id_counts.AC.active` | 36 | **41** aktiv · 2 deprecated · 1 Platzhalter |
| `id_counts.EV.active` | 36 | **42** aktiv · 2 deprecated · 1 Platzhalter |
| `id_counts.TRC.active` | 36 | **40** aktiv · 2 deprecated |
| `id_counts.CAN` | 12 deprecated / 115 active / 10 reserved | **123** aktiv · **14** deprecated · **6** reserviert |
| `id_counts.VIS` | (nicht getrennt ausgewiesen) | **11** aktiv · 0 deprecated · **3** reserviert |
| `id_counts.OQ` | 10 offen | **15** offen · 1 resolved |
| `id_counts.by_prefix` | **zehn** Präfixe | **zwölf** (`USER-`, `NFR-` fehlen) |
| `requirements` | 36 Einträge | **40** aktive |
| `overall_status.reason` | nennt „die zehn Canvas-Items (CAN-016…022, CAN-071, CAN-099, CAN-130)" als unbestätigt und „alle 36 Requirements" | CAN-022/099/130 sind `active`, CAN-071 **und CAN-140** sind `deprecated`; es sind **sechs** reservierte Items (CAN-016…021) |

⚠️ **Die Divergenz ist seit dem 2026-07-19 nicht kleiner, sondern größer geworden**, und zwar in
**jeder** Zeile — nicht weil das Paket sich geändert hätte, sondern weil die Registry
weitergelaufen ist. Ein veraltetes Intake-Paket veraltet **weiter**, solange niemand es nachzieht.

**Was daran richtig bleibt:** `confirmation.user_confirmed = false`,
`true_line_status = "pending-watcher"`, `self_certified = false`,
`max_reachable_status = "READY_FOR_USER_CONFIRMATION"` und
`overall_status.value = "BLOCKED_TRACEABILITY"` mit `gate_ready = false`. Diese Felder stimmen mit
dem aktuellen Stand überein und werden hier **nicht** als veraltet ausgewiesen.

**Was daraus folgt:** wer `SRC-008` als Beleg für den ID-Bestand referenziert, referenziert den
**Altstand**. Die dort hartkodierten Zahlen sind keine gültigen Erwartungswerte (Registry
Regel 11, §10.1). ⚠️ **Und die Gegenrichtung gilt ebenso** (Registry §10.2 Bindung 2): ein
Werkzeug, das die alten Literale **verbietet**, ist genauso an einen Zählstand gebunden wie eines,
das sie erwartet. Zählstände sind **ausschließlich** aus den Registry-Definitionstabellen
abzuleiten, mit Datum und Ableitungsweg. **Diese Datei ändert `intake-package.json` nicht** — sie
gehört einem anderen Owner. Der Nachzug ist in §5 als BLOCKER geführt.

**Zusatzbefund zum Schema, unverändert gültig und vom Paket selbst bestätigt:**
`schema_provenance` weist aus `authored_in_this_run: true` und
`is_preexisting_standard: false`. Schema **und** Validator sind in diesem Lauf neu verfasst; ein
ausführbares Intake- oder Schema-Validierungswerkzeug existierte vorher nicht (Registry §8
Punkt 13, §9). **Ein bestandener Schema-Check ist deshalb kein unabhängiger Nachweis** — das Paket
sagt das über sich selbst.

## 4. Nicht als Quelle geführt

| Artefakt | Begründung |
|---|---|
| `CLAUDE.md` (Repository-Wurzel) | Agentenanleitung, keine Anforderungsquelle. Enthielt bis `CONTRA-001` eine falsche Dokumenthierarchie und ist deshalb ausdrücklich nicht belegfähig. |
| `README.md` (Repository-Wurzel) | Einstiegsdokument, referenziert ausschließlich; definiert nichts. |
| `docs/traceability.md`, `docs/EVIDENCE-LEDGER.md`, `docs/validation/validation-report.md` | Ableitungen und Nachweisführung über dem Artefaktsatz, keine Eingangsquellen. `docs/validation/validation-report.md` trägt zusätzlich den Befundsatz zu SRC-005. |
| `infra/routing-proxy/` | Dokumentierter Ablageort (CAN-097, OQ-011). **Existiert nicht** und wurde in diesem Lauf ausdrücklich nicht angelegt. Kein Artefakt, keine Quelle. |
| `scratchpad/id-migration.json` | Maschinenlesbare Migrationsspur des Auftau-Schritts 2 (Deprecations, neue IDs, `blocking_model`, Zählregel). Liegt **außerhalb des Repositories** im Arbeitsverzeichnis des Laufs und ist damit **nicht dauerhaft referenzierbar**. Der kanonische Inhalt steht in `docs/ID-REGISTRY.md` §7.4 — **dorthin ist zu referenzieren, nicht auf den Scratchpad.** ⚠️ Registry §3.1 bezeichnet die dortige `blocking_model`-Fassung als „für diese Datei normativ"; eine normative Referenz auf einen nicht versionierten Scratchpad-Pfad ist ein **BLOCKER** für den Owner der Registry. |
| `docs/EVIDENCE-LEDGER.md`, `docs/risks/…`, `docs/decisions/…`, `docs/architecture/…`, `docs/implementation/…` | Nachweisführung, Register und Ableitungen über dem Artefaktsatz. Keine Eingangsquellen. |

## 5. Offene Punkte dieser Datei

| Punkt | Art | Adressat |
|---|---|---|
| ~~Belegdokumente zu SRC-001…SRC-004 fehlen~~ — **erledigt am 2026-07-20.** Dokumente aufgefunden (§1.1), seit demselben Tag auch im Repository (§1.6), alle **131** Zellen einzeln geprüft (§1.3). Zählstand nach der Nachprüfung §1.3.1: **105 BELEGT · 20 TEILBELEGT · 6 UNBELEGT · 0 ungeprüft** (vorher 109 / 17 / 5). | *geschlossen* | — |
| **Sechs Canvas-Zellen sind UNBELEGT** (CAN-041, CAN-042, CAN-046, **CAN-109** *(neu, §1.3.1)*, CAN-110, CAN-112): die Aussage kommt in **keiner** der vier Quellen vor. Herabstufung auf ASSUMPTION oder MISSING erforderlich. **Diese Datei hat sie nicht herabgestuft.** Bei CAN-109 gilt zusätzlich: es fällt die **Source**-Angabe (SRC-003), **nicht** die Herkunftsangabe „CAN-008, nur Prosa 'Risks'" — diese ist gegen `canvas.md:544` zutreffend (§1.3.1). | **BLOCKER** | Owner Canvas |
| **Drei weitere Zellen sind von BELEGT auf TEILBELEGT herabgestuft** (§1.3.1): **CAN-119** (Benennung „Privacy-" und „Privacy-Review" ungedeckt; Aufspaltungsrichtung strittig), **CAN-024** (Rangaussage *Primär/Sekundär* verschmolzen; „Renn-"/„Freizeit-" ungedeckt), **VIS-003** (Qualifizierer „sicher"/„verlässlich" ungedeckt; Verbundaussage aus drei Fundstellen komponiert). Wortlaut verengen oder Rest als ASSUMPTION kennzeichnen — **hier nicht ausgeführt**. Folgeprüfung mitzuführen: TRC-004 (GATE-A0), CAN-017, CAN-028, CAN-031, CAN-118, CAN-120. | **BLOCKER** | Owner Canvas / Vision |
| **CAN-099: die Erstreckung der Accessibility-Pflicht auf „nutzbare Web-Auskopplungen" ist in keiner Quelle belegt** (§1.5). Streichung ist beauftragt; sie ist **synchron** mit AC-037, NFR-005 und EV-037 zu führen, sonst bleibt ein Akzeptanzkriterium mit einer Vorbedingung ohne Upstream-Anker zurück. Begründung ist **Belegmangel**, nicht Widerspruch — SRC-001:132 nimmt den Beschützer-Link ausdrücklich aus. | **BLOCKER** | Owner Canvas / PRD |
| **CAN-113 ist falsch adressiert** — „Referenzstrecken" steht in SRC-001/SRC-002, nicht in dem beanspruchten SRC-003. Quellenangabe korrigieren, Inhalt unverändert. | Nachzug | Owner Canvas |
| **CAN-051 trägt eine Quelle, die seinen Kern nicht deckt** — „echte routebezogene Restdistanz" steht weder in SRC-001 noch in SRC-003; SRC-004 spezifiziert ausdrücklich die einfache Subtraktion (§1.5). Quelle auf SRC-005/DEC-004 umstellen. ⚠️ **Mit dem Einwand vom 2026-07-20 zu lesen** (§1.5): SRC-001:160 und SRC-003:682 decken „verbleibende km korrekt" wörtlich — SRC-001/SRC-003 sind daher zu **ergänzen**, nicht zu **ersetzen**; der „Zirkelbeleg"-Vorwurf gegen die Herkunftsspalte trägt nicht. | **BLOCKER** | Owner Canvas |
| **Herabstufungen und Blocker, die mit „SRC nicht auffindbar" begründet wurden, sind neu zu bewerten** — betroffen sind mindestens `prd.md:921/922/926/958/1076/1213/1263/1613`, `traceability.md:270/526`, `vision.md:63/153`, `ID-REGISTRY.md:1131–1133` (§1.4). Die jeweils **zweite** Begründung (analytische Nullschwelle) bleibt unberührt; es wird **nichts** automatisch hochgestuft. | **BLOCKER** | Owner PRD / Traceability / Vision / Registry |
| **Dreifach fortgepflanzte Lücke „versioniert"** — VIS-008, REQ-023 und REQ-001 verlangen versionierte Faktoren bzw. Konfigurationsobjekte; keine Quelle sagt das. Zweite Lücke gleicher Art: „Unsicherheit"/„Confidence" in VIS-007, CAN-052, REQ-012. | Nachzug | Owner Vision / PRD / Canvas |
| **VIS-012 und VIS-013 sind inhaltlich aus den Quellen ableitbar** (§1.5) — der Blocker ändert seine Art von „nicht ableitbar" zu „noch nicht entschieden". Kein Item gefüllt, keine ID vergeben. | OPEN QUESTION | Nutzer / Owner Vision |
| **REQ-019 hat keinen tragenden Vision-Anker**, und keines der elf aktiven Vision-Items trägt ihn. Inhalt und Canvas-Anker sind belegt (§1.5). Fehlende VIS-ID = BLOCKER, keine Nummer erfunden. | **BLOCKER** | Nutzer |
| **OQ-004 ist enger als verzeichnet** — Startanbieter, Prüfzeitpunkt, Kriterien und Alternativen stehen in den Quellen (§1.5); offen ist allein der finale Entscheid vor Stufe B. **Hier nicht geschlossen.** | Nachzug | Owner Open Questions / Nutzer |
| **OQ-016 / AC-039 (d):** die Klausel „Fremd-App öffnet Datei" ist in SRC-001 und SRC-003 wörtlich belegt (§1.5); die konkrete Referenz-Fremdanwendung bleibt MISSING. | Nachzug | Owner Canvas / PRD |
| **Konzeptdokument aufgefunden** (`RUNNING_CYCLING_APP_KONZEPT_CHAT_ZUSAMMENFASSUNG.md`, §1.1) — Ziel der `§`-Verweise in SRC-003/SRC-004. **Keine ID vergeben.** Soll es als Quelle geführt werden? | OPEN QUESTION | Nutzer |
| Weitere **85** `EXPLICIT`-Zellen nennen überhaupt keine Quelle. **Unverändert** — sie sind nicht prüfbar, weil sie nichts benennen. | BLOCKER | Owner PRD / Canvas / Vision |
| **Zweite Entscheidungstranche vom 2026-07-19 ohne SRC-ID** (§2.1). `SRC-006` deckt sie nicht und wurde **nicht** erweitert; eine neue ID wurde **nicht** vergeben. | **BLOCKER** | Nutzer |
| **Dritte Entscheidungstranche vom 2026-07-20 ohne SRC-ID** (§2.2) — *neu*. Drei Canvas-Items (CAN-099, CAN-139, CAN-141) sind auf ihrer Grundlage auf `EXPLICIT` hochgestuft worden; der Beleg ist **kein referenzierbares Artefakt**. Registry §8 Punkt 43 führt zusätzlich die fehlende Gegenbestätigung. | **BLOCKER** | Nutzer |
| **`intake-package.json` (SRC-008) ist vorhanden, bildet aber einen Stand vor dem Auftau-Schritt 2 ab** (§3) — und die Divergenz ist mit Runde 4 in **jeder** Zeile größer geworden: Requirements, AC, EV, TRC, CAN, VIS, OQ und die Präfixzahl. **Keine der dort hartkodierten Zahlen ist ein gültiger Erwartungswert — und keine darf als Verbotswert verwendet werden** (Registry §10.2 Bindung 2). | **BLOCKER** | Owner des Intake-Pakets |
| Aufnahme des Raums `SRC-` in `docs/ID-REGISTRY.md`. | OPEN QUESTION | Nutzer |
| Datumsdiskrepanz. Textstand `2026-07-16` (SRC-001/SRC-003) ↔ mtime `2026-07-18` (Desktop) ↔ Dateiname `2026-07-10`. Ein mtime ist kein Autorendatum; ob fortgeschrieben oder nur kopiert wurde, ist aus den Dateien nicht entscheidbar (§1.1). **Nicht als Widerspruch behauptet, nicht wegerklärt.** | offene Beobachtung / MISSING | Nutzer |
| Für SRC-001…SRC-003 existieren **zwei inhaltlich verschiedene Fassungen** (Desktop kanonisch, Downloads älter, §1.1). Soll die Downloads-Fassung entfallen? Solange beide existieren, ist „die Quelle" mehrdeutig. | OPEN QUESTION | Nutzer |
| `CLAUDE.md` nennt für SRC-001…SRC-004 **repo-relative Pfade, die nicht existieren** — das war die eigentliche Ursache des widerlegten Befunds (§1.2). Pfade auf den kanonischen Fundort umstellen. **Seit dem 2026-07-20 auflösbar:** `docs/sources/` existiert (§1.6); die in `CLAUDE.md` genannten Pfade sind dennoch weiterhin falsch. | Nachzug | Owner `CLAUDE.md` |
| **`scripts/validation/src-verification.json` ist inhaltlich veraltet** (§1.6) — byte-identisch aus dem Scratchpad übernommen; führt weiterhin `109 / 17 / 5` statt `105 / 20 / 6` und in `quellen[*].pfad` die Desktop-Pfade statt `docs/sources/`. Es **widerspricht** der Verdikttabelle in §1.3. **Diese Datei ändert es nicht.** | **BLOCKER** | Owner der Belegprüfung |
| **`scratchpad/semantic-review.md` und `scratchpad/id-migration.json` sind nicht mit ins Repository überführt worden** (§1.6, Ausschlussliste in `scripts/validation/HASHES.md`). Befunde, Zahlen und Regeln, die sich auf sie stützen — insbesondere die 23 `trägt-teilweise` einer Wesentlichkeitsregel — bleiben **nicht referenzierbar belegt**. | **BLOCKER** | Nutzer / Owner Registry |
| **Kanonischer Fundort nicht entschieden** — Repo-Kopie (`docs/sources/`) und Original (`~/Desktop/docs/`) sind heute byte-identisch (§1.6), aber nichts hält sie identisch, und das Repository steht **nicht** unter Versionskontrolle (kein `.git`, gemessen 2026-07-20). Welcher Stand ist maßgeblich? | OPEN QUESTION | Nutzer |
| Freitext „Nutzerentscheidung 2026-07-19" durch eine SRC-ID ersetzen — Canvas 20×, PRD 18×, Registry 17×, Traceability 7×, Vision 1× (gemessen 2026-07-20). **Setzt die Entscheidung aus §2.1 voraus**, ist ohne sie nicht durchführbar. | Nachzug | Owner Canvas / PRD / Registry |
| Freitext „Nutzerentscheidung 2026-07-20" durch eine SRC-ID ersetzen — Registry 7×, Canvas 5×, PRD 2× (gemessen 2026-07-20). **Setzt die Entscheidung aus §2.2 voraus.** | Nachzug | Owner Canvas / PRD / Registry |
| Registry §5.2 zählt `SRC-` mit 8 Vorkommen. **Stimmt weiterhin** — in diesem Nachzug wurde keine SRC-ID vergeben. | *kein Nachzug offen* | — |
| **`SRC-005` (Konsistenzprüfung) referenziert `docs/validation/validation-report.md`.** Dieser Bericht führt `blocking_scope` weiterhin als **lebendes Feld** samt der alten, defekten Formel — obwohl das Feld projektweit entfallen ist (C16). Ein Befundsatz, der auf einer widerlegten Formel beruht, taugt insoweit nicht als Beleg. | **BLOCKER** | Owner `validation-report.md` |
| Finaler Repository-Owner/DRI, der über die obigen Punkte entscheidet. | MISSING | `OQ-002` |

### 5.1 Was der Nachzug vom 2026-07-20 (**Runde 5**) ausdrücklich nicht getan hat

⚠️ **Dieser Abschnitt beschreibt Runde 5 und ist an einer Stelle überholt.** Der Punkt „Keine
Quelldatei kopiert" gilt seit Runde 6 nicht mehr — die vier Quellen liegen jetzt unter
`docs/sources/` (§1.6). Was Runde 6 getan und nicht getan hat, steht in §5.2.

- **Keine SRC-ID vergeben, keine deprecatet, keine umgedeutet.** Bestand unverändert
  `SRC-001`…`SRC-008`.
- **`SRC-006` nicht erweitert.** Die zweite **und** die dritte Entscheidungstranche sind als
  BLOCKER geführt (§2.1, §2.2), nicht in eine bestehende ID hineingelesen.
- **Keine Zelle hochgestuft.** Kein `source_type` wurde von hier aus von ASSUMPTION oder MISSING
  auf `EXPLICIT` gehoben — auch nicht die 109 als BELEGT geprüften. Die Existenz einer Quelle ist
  kein Beleg für eine konkrete Aussage, und die Einstufung fremder Zellen gehört ihren Ownern.
- **Keine Zelle herabgestuft.** Die fünf UNBELEGT sind als BLOCKER an den Canvas-Owner gemeldet
  (§1.3, §5), nicht selbst geändert. Diese Datei ändert Canvas, PRD, Vision, Traceability,
  Registry und `intake-package.json` nicht.
- **Keine Quelldatei kopiert, verschoben oder verändert.** SRC-001…SRC-004 wurden ausschließlich
  gelesen; sie liegen unverändert außerhalb des Repositories.
- **Keine ID vergeben.** Weder für das aufgefundene Konzeptdokument noch für die zweite und
  dritte Entscheidungstranche (§2.1, §2.2) noch für die fehlenden Vision-Anker. Wo eine ID fehlt,
  steht ein BLOCKER.
- **Keine Bewertung der Belegqualität mit einem Werkzeug automatisiert.** Die 131 Verdikte
  stammen aus manuellem Lesen des Quelltextes. Es wurde kein Validator gebaut und keiner geändert.
- **Kein Gesamtstatus gesetzt und nichts bestätigt.** Der Gesamtstatus des Vorhabens bleibt
  **BLOCKED_TRACEABILITY**; `true-line-status` bleibt `pending-watcher`, `wired-in-prod` `no`,
  `evidence-class` `none`, `self-certified` `false`. Es existiert kein Code. Das Auffinden der
  Quellen ist ein **Befund**, keine Freigabe und kein Watcher-Verdikt.

### 5.2 Was der Nachzug vom 2026-07-20 (**Runde 6**) getan und nicht getan hat

**Getan:**

- **Vier Quelldokumente ins Repository kopiert** (`docs/sources/`, §1.6). Die Originale wurden
  dabei **nicht** verändert; die Kopien sind byte-identisch, selbst nachgerechnet.
- **Die Validatorkette ins Repository überführt** (`scripts/validation/`, §1.6). Es wurde **kein
  Werkzeug gebaut und keines geändert**; die bekannten Werkzeugdefekte sind unverändert
  übernommen und in `scripts/validation/README.md` aktenkundig.
- **Vier zuvor als BELEGT geführte Zellen nachgeprüft und herabgestuft** (§1.3.1): CAN-119,
  CAN-024 und VIS-003 auf TEILBELEGT, CAN-109 auf UNBELEGT. Jede Herabstufung ist mit Datum,
  Grund, Fundstelle und wörtlichem Zitat protokolliert — **keine still ausgetauscht**.
- **Drei Passagen als überholt ersetzt statt stehen gelassen** (§1.1 „nicht ins Repository
  kopiert", §1.2 „Option 1 nicht ausgeführt", §1.3 Scratchpad-Pfad). Der alte Wortlaut ist
  jeweils wörtlich mitzitiert.
- **Einwände aus der Gegenprüfung sichtbar abgebildet**, auch wo sie dem Befund widersprechen:
  die Herkunftsspalte ist bei CAN-024, CAN-051 und CAN-109 **zutreffend** und darf nicht mit
  gestrichen werden; die Aufspaltungsrichtung bei CAN-119 ist **strittig**; der
  Richtungs-Widerspruch bei CAN-099 trägt **nicht**.

**Nicht getan:**

- **Keine SRC-ID vergeben, keine deprecatet, keine umgedeutet.** Bestand unverändert
  `SRC-001`…`SRC-008`. Die Überführung ergänzt einen Fundort, sie schafft keine Quelle.
- **Keine Zelle hochgestuft.** Weder wegen der Überführung noch sonst. Die Existenz einer Quelle
  im Repository belegt keine einzige konkrete Aussage.
- **Keine fremde Zelle selbst geändert.** Canvas, PRD, Vision, Traceability, Registry,
  `intake-package.json` und `CLAUDE.md` sind unverändert; alle Nachzüge stehen als BLOCKER in §5.
- **Keinen der bestehenden Warnhinweise oder Blocker entfernt.** Die Punkte aus Runde 5 bestehen
  fort; hinzugekommen sind vier.
- **`scripts/validation/src-verification.json` nicht nachgezogen** — es widerspricht §1.3 und ist
  als BLOCKER gemeldet (§5).
- **Keinen der drei Streitpunkte entschieden**: Aufspaltungsrichtung CAN-119, `source_type` von
  REQ-007 (`ASSUMPTION` gegen `MISSING`), kanonischer Fundort. Alle drei sind offengelegt.
- **Kein Gesamtstatus gesetzt und nichts bestätigt.** Der Gesamtstatus bleibt
  **BLOCKED_TRACEABILITY**; `true-line-status` `pending-watcher`, `wired-in-prod` `no`,
  `evidence-class` `none`, `self-certified` `false`. Es existiert kein Code. Weder die Überführung
  der Quellen noch ein Lauf der Validatorkette ist eine Freigabe oder ein Gate-Verdikt.

## Confirmation Status

`pending-user-confirmation`

Die Assistenz bestätigt diese Source Map nicht im Namen des Nutzers.
