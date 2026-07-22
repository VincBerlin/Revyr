# Prüfsummen — Quelldokumente und Validatorkette

Stand: 2026-07-20. Alle Summen mit `shasum -a 256` **selbst berechnet**, nicht aus einer
Vorlage übernommen. Gesamtstatus bleibt `BLOCKED_TRACEABILITY`; dieses Dokument ist
weder Freigabe noch Gate-Verdikt.

Reproduktion:

```bash
shasum -a 256 "/Users/vincentschnetzer/Documents/Run&Bike/docs/sources/"SRC-00*.md
shasum -a 256 "/Users/vincentschnetzer/Documents/Run&Bike/scripts/validation/"*.py
```

⚠️ Der Repo-Pfad enthält ein kaufmännisches Und. Jede Pfadangabe **muss** in
Anführungszeichen stehen. Ein unquotierter Pfad hat in diesem Lauf bereits einmal eine
Fehlmessung erzeugt (siehe `README.md`, „Messfehler im eigenen Lauf").

---

## 1. Quelldokumente (SRC-001 … SRC-004)

Herkunft: `/Users/vincentschnetzer/Desktop/docs/` bzw. `.../superpowers/plans/`.
Die Originale wurden **ausschließlich gelesen und kopiert**, nicht verändert.

Soll-Hash = der in `docs/SOURCE-MAP.md` §1.1 verzeichnete Wert (Spalte SHA-256,
Tabelle „Kanonischer Stand — Desktop").

| ID | Repo-Datei | Bytes | SHA-256 Original | SHA-256 Repo-Kopie | Soll-Hash §1.1 | Vergleich |
|---|---|---:|---|---|---|---|
| SRC-001 | `docs/sources/SRC-001-REVYR-Vision-Canvas-PRD.md` | 24.585 | `d0a6adf4e1f2be843eb9e93896164755cd417bdd591c1bd415e9c8dc2874f0d3` | `d0a6adf4e1f2be843eb9e93896164755cd417bdd591c1bd415e9c8dc2874f0d3` | `d0a6adf4…74f0d3` | **identisch (3/3)** |
| SRC-002 | `docs/sources/SRC-002-REVYR-Plan-PRD.md` | 10.525 | `37e090aafac7a3c7278c61164cb342018dea7530c995f73f7f5add220fd16542` | `37e090aafac7a3c7278c61164cb342018dea7530c995f73f7f5add220fd16542` | `37e090aa…d16542` | **identisch (3/3)** |
| SRC-003 | `docs/sources/SRC-003-REVYR-GESAMTPLAN-FINAL.md` | 61.117 | `c3ceb46fa52c487530546370fc6682e6df7e7b66b35f4c6eb55a4b3e77e3764d` | `c3ceb46fa52c487530546370fc6682e6df7e7b66b35f4c6eb55a4b3e77e3764d` | `c3ceb46f…e3764d` | **identisch (3/3)** |
| SRC-004 | `docs/sources/SRC-004-tracking-and-planned-routes.md` | 78.355 | `dc18a97d9fe2299662933120391207264ecbb40d16bc98a129e545a9f37bc25f` | `dc18a97d9fe2299662933120391207264ecbb40d16bc98a129e545a9f37bc25f` | `dc18a97d…7bc25f` | **identisch (3/3)** |

„identisch (3/3)" heißt: Original = Repo-Kopie = Soll-Hash aus §1.1. Auch die
Byte-Größen decken sich mit §1.1 (24.585 / 10.525 / 61.117 / 78.355). **Keine
Abweichung.** Der Kopiervorgang hat den Inhalt nicht angetastet, und der in §1.1
verzeichnete Stand ist derselbe, der jetzt im Repository liegt.

### Nicht kopiert, bewusst

`docs/SOURCE-MAP.md` §1.1 führt zusätzlich einen **älteren Nebenstand** unter
`~/Downloads/` (SRC-001…SRC-003, abweichende Prüfsummen = abweichender Inhalt) sowie
`RUNNING_CYCLING_APP_KONZEPT_CHAT_ZUSAMMENFASSUNG.md` (ohne SRC-ID). Beides wurde
**nicht** ins Repository geholt: der Auftrag nennt die vier Desktop-Quellen, und §1.1
erklärt den Desktop-Stand als kanonisch. Die Downloads-Fassung ist damit nicht bloß
anders abgelegt, sondern ein anderes Dokument — sie mitzukopieren hätte zwei Stände
nebeneinander gestellt.

---

## 2. Werkzeuge — byte-identisch übernommen

Original: das Scratchpad-Verzeichnis der Vorsitzung
`/private/tmp/claude-501/-Users-vincentschnetzer-Documents-Run-Bike/5ad02448-3a52-4a17-affc-d652ef4b5345/scratchpad`.

| Datei | Bytes | SHA-256 Original | SHA-256 Repo-Kopie | Vergleich |
|---|---:|---|---|---|
| `blocking_model.py` | 23.599 | `88f0367db4c64f243725aa75c6ac5b4948eb495e5ed8c086472347eb5389b547` | `88f0367db4c64f243725aa75c6ac5b4948eb495e5ed8c086472347eb5389b547` | **identisch** |
| `registry_model.py` | 9.304 | `3e41be6ffac876939efd897f73485d74b28cb7a33a9c12874d47254bd53acd69` | `3e41be6ffac876939efd897f73485d74b28cb7a33a9c12874d47254bd53acd69` | **identisch** |
| `validate_intake.py` | 123.799 | `b85d3c4e5e27bd0b3a7877c063f8976487d113c8833a8b6c8f5986d0857aaa11` | `b85d3c4e5e27bd0b3a7877c063f8976487d113c8833a8b6c8f5986d0857aaa11` | **identisch** |
| `validate_trace.py` | 16.176 | `638be81fc40947b389138aa3a8c61aedead7e91a8efee4a6cc84fae69e1efe83` | `638be81fc40947b389138aa3a8c61aedead7e91a8efee4a6cc84fae69e1efe83` | **identisch** |
| `check_prd.py` | 18.163 | `d6ee4b3106185e5f6baefc49972ca5c59c243903924fc9af93e351bd715641c9` | `d6ee4b3106185e5f6baefc49972ca5c59c243903924fc9af93e351bd715641c9` | **identisch** |
| `selftest_validator.py` | 37.274 | `be17426c144cd7022d8a067d17681a57a243645997446f32940ae6f265b0714c` | `be17426c144cd7022d8a067d17681a57a243645997446f32940ae6f265b0714c` | **identisch** |
| `validate_schema.py` | 4.671 | `2bb3f0ae6ac919a58cabcfe638e7b841d1403a60b89d43f620abfc16595c7aee` | `2bb3f0ae6ac919a58cabcfe638e7b841d1403a60b89d43f620abfc16595c7aee` | **identisch** |
| `gen_intake.py` | 26.746 | `2b3f0fde670ec13b2ab5d839d6296b706901b341b280545f2aca4e7bdcaf97fe` | `2b3f0fde670ec13b2ab5d839d6296b706901b341b280545f2aca4e7bdcaf97fe` | **identisch** |
| `intake-package.schema.json` | 23.388 | `0111fb1243403229f1616e030076a578454b9354f056d627154133990c0f7fab` | `0111fb1243403229f1616e030076a578454b9354f056d627154133990c0f7fab` | **identisch** |
| `src-verification.json` | 76.857 | `1e05df0250ce7085b1fe75070fc8ca294bfe740ea83d1df33fd1072074d06682` | `1e05df0250ce7085b1fe75070fc8ca294bfe740ea83d1df33fd1072074d06682` | **identisch** |

`gen_intake.py` stand **nicht** auf der Übernahmeliste des Auftrags. Es ist trotzdem
hier, weil es zur Laufzeit gebraucht wird — Begründung in `README.md`, Abschnitt
„Nachträglich aufgenommen". Es wird von `run_all.sh` **nicht ausgeführt**.

`src-verification.json` enthält unter dem Schlüssel `zellen` **131** Einträge. Die
Angabe „131 Einzelbefunde" wurde nachgezählt, nicht übernommen.

---

## 3. Werkzeuge — Pfadauflösung geändert

Diese fünf hatten den Repo-Pfad als Literal. Geändert wurde **nur** das Pfad-Literal;
die Prüflogik ist eingefroren. Hash-Ungleichheit ist hier **beabsichtigt** und der
Grund, warum der Äquivalenzbeweis (`EQUIVALENCE.md`) geführt wurde.

| Datei | Bytes orig | Bytes Kopie | SHA-256 Original | SHA-256 Repo-Kopie | Vergleich |
|---|---:|---:|---|---|---|
| `xcheck.py` | 1.812 | 1.889 | `c00889230b9c1aa197258b8005d962af75e5f9f81ac98529cbcbf7c12b50fc2e` | `64c45acdbc39c52a51f8189b3936e02c8adb57e1c9dfc27625dbca7ad4c404fc` | abweichend (beabsichtigt) |
| `verify.py` | 5.062 | 5.139 | `2e55f34790de4145e7a7783f453bb3723308ff6739a6334c3316f58bef3b4172` | `938d62d6e81828929f25ea2dd682f1117a092fe0eb34fcde84e5037038ffb22e` | abweichend (beabsichtigt) |
| `verify_canvas.py` | 6.424 | 6.501 | `10b3ce6bb686543adc53b6646d10184be68fc315b2188fcc0b89c039af19323d` | `f4d2259d59079521732ba0a0e477f028e7cc060ab879bcdcf11c5572f858c3f1` | abweichend (beabsichtigt) |
| `oq_check.py` | 2.772 | 2.815 | `45a954a8256e19f6ec655490590e34d084ee695cc71057c0279a907804c7fcad` | `60e2232f5c025390e5671818bd40eda2f178030b1dcb56ac3b768903f64d5071` | abweichend (beabsichtigt) |
| `AUDIT_points.py` | 1.287 | 1.364 | `c0371a4c779176c3acf9687cb94c0732cd099eb138434259afdab57a4c6e8e59` | `6bce12902ffb3c3e3387d4a66a86fd98aff863919f15013289e25110c6603e94` | abweichend (beabsichtigt) |

Ausgabegleichheit trotz Hash-Ungleichheit: `EQUIVALENCE.md` (stdout, stderr und
Exit-Code byte-genau gleich, alle fünf).

---

## 4. Neu in diesem Lauf verfasst

Diese Dateien haben kein Original und deshalb keinen Vergleichshash.

| Datei | Bytes | SHA-256 |
|---|---:|---|
| `run_all.sh` | 5.563 | `c6401403b5348e06b509ec69849e931c96007979c10110ccce72b804e3a0d494` |

`HASHES.md`, `EQUIVALENCE.md` und `README.md` sind ebenfalls neu; ihre eigenen Summen
sind hier nicht geführt, weil eine Datei ihre eigene Prüfsumme nicht enthalten kann.
