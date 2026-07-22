# Run&Bike — Arbeitstitel `REVYR`

Geplante mobile App für Läufer:innen und Radfahrer:innen: Aktivitäts-Tracking, erklärbare
Health-Auswertung und lokale Community. Ein iOS-/Android-Client aus einer gemeinsamen
Expo-/React-Native-/TypeScript-Codebasis.

**Dieses Repository enthält ausschließlich Planungsdokumente.** Alles Folgende beschreibt
Absichten, keine vorhandenen Eigenschaften.

## Status (2026-07-19)

| Punkt | Stand |
|---|---|
| Anwendungscode | **existiert nicht.** Kein `mobile/`, kein `infra/`, keine Build- oder Test-Konfiguration. |
| Versionskontrolle | **nicht initialisiert.** Kein `.git`-Verzeichnis; es gibt keine Historie und keine Commits. |
| Artefaktsatz | vollständig, aber `pending-user-confirmation`. |
| Freigabe | **keine.** Kein Dokument ist vom Nutzer bestätigt. |

Der Artefaktsatz trägt den Readiness-Level `READY_FOR_USER_CONFIRMATION`
(`docs/validation/validation-report.md`). Das ist der höchste Stand, den die Assistenz vergeben
darf — es ist ausdrücklich **keine** Bestätigung. Bestätigen kann nur der Nutzer.

## Namen

Zwei Namen, die nicht verwechselt werden dürfen:

- **`REVYR`** ist ein **Arbeitstitel** (von „Revier"). Der finale öffentliche Produktname ist
  offen und markenrechtlich ungeprüft — `OQ-001` in `docs/decisions/open-questions.md`, fällig vor
  Gate A2. Bis dahin darf der Arbeitstitel nicht in Bundle IDs, Domains oder Store-Metadaten
  eingebrannt werden (`CAN-090`).
- **`revyr-endurance-platform`** ist der interne technische Feature-Slug. Er bleibt stabil, auch
  wenn der öffentliche Name wechselt (`DEC-001`, `ASM-203`).

## Owner / DRI

**Offen.** Es gibt derzeit keinen benannten Repository-Owner und keinen DRI — `OQ-002`, fällig vor
P0-Start. Solange die Frage offen ist, bleibt die Umsetzung organisatorisch unzugeordnet: Es gibt
niemanden, der Gates abnimmt, offene Fragen entscheidet oder Evidence gegenzeichnet.

Das ist keine Formalie. Alle 36 Requirements tragen deshalb einen sichtbaren Owner-Blocker statt
eines Owner-Eintrags.

## Verbindliche Dokumenthierarchie

In dieser Reihenfolge lesen. Bei Abweichungen zwischen Dokumenten gilt das jeweils höherrangige.

1. **`docs/ID-REGISTRY.md`** — kanonische Quelle für die ID-Räume `VIS-`, `CAN-`, `REQ-`, `AC-`,
   `TRC-`, `EV-`, `RISK-`, `ASM-`, `OQ-`, `CONTRA-`. Bei jeder Abweichung zwischen Registry und
   referenzierendem Dokument **gilt die Registry**. Ab Phase 2 eingefroren: IDs werden nicht mehr
   vergeben, umbenannt oder deprecated. Wer eine fehlende ID braucht, meldet einen BLOCKER und
   erfindet keine.
2. **`docs/canvas/revyr-endurance-platform.canvas.md`** — Product Canvas: Problem, Zielnutzer,
   Wertversprechen, Non-Goals, Constraints, Risiken, Erfolgssignale, Allowed change scope.
3. **`docs/prd/revyr-endurance-platform.prd.md`** — PRD: `REQ-001`…`REQ-036`, Akzeptanzkriterien
   `AC-001`…`AC-036`, `NFR-001`…`NFR-008`, Evidence je REQ, Release-Gates A0/A1/A2/B/C/D/E.
4. **`docs/vision/revyr-endurance-platform.vision.md`** — Vision: Zielgruppe, Bedürfnisse,
   Produktwert, Erfolgssignale, Grenzen.
5. **`docs/traceability.md`** — REQ ↔ Vision ↔ Canvas ↔ Akzeptanz ↔ Evidence. Wird mit dem
   Fortschritt fortgeschrieben.

Ergänzend, nicht rangfrei übergeordnet:

- `docs/decisions/open-questions.md` — **einziges kanonisches OQ-Register** (`OQ-001`…`OQ-011`).
- `docs/decisions/decision-log.md` — Entscheidungen (`DEC-`) und Widerspruchs-Ledger (`CONTRA-`).
- `docs/SOURCE-MAP.md` — Herkunft der Anforderungen (`SRC-`).
- `docs/implementation/revyr-delivery-plan.md`, `docs/architecture/revyr-target-architecture.md`,
  `docs/risks/revyr-risk-register.md`, `docs/EVIDENCE-LEDGER.md`,
  `docs/validation/validation-report.md`.

`CLAUDE.md` ist Agentenanleitung, keine Anforderungsquelle.

⚠️ Ältere Fassungen von `CLAUDE.md` nannten `docs/superpowers/plans/2026-07-10-REVYR-GESAMTPLAN-FINAL.md`,
`docs/REVYR-Vision-Canvas-PRD.md` und `docs/REVYR-Plan-PRD.md` als verbindlich. **Diese Dateien
existieren in diesem Repository nicht** (`CONTRA-001`, resolved). Jede verbliebene Referenz darauf
ist veraltet.

## Bekannte offene Punkte

Diese Liste ist eine Auswahl und ersetzt die Register nicht.

- **Elf offene Fragen** in `docs/decisions/open-questions.md`, davon zehn ungelöst. `OQ-011`
  (Ablageort des A0-Routing-Proxys) ist entschieden — das Register führt ihn noch als offen; der
  Nachzug steht aus.
- **`CONTRA-004`** Anti-Cheat vs. Datenminimierung — Grundsatzentscheidung getroffen,
  Implementierungs-Evidence ausstehend.
- **`CONTRA-005`** Historie vs. Accountlöschung — Grundsatzentscheidung getroffen. Sie prägt
  Datenbankschema und Sync und muss **vor** der Schema-Finalisierung berücksichtigt werden.
- **`CONTRA-006`** Routing-Proxy vs. Local-first — Status `DESIGN-RESOLVED / EVIDENCE-PENDING`,
  **blockierend für die A0-Routing-Implementierung**. Nicht geschlossen: Der Nachweis zu Logging,
  Retention, Providerbedingungen und Sicherheitskontrollen setzt lauffähigen Code voraus, der noch
  nicht existiert.
- **Vier von fünf Upstream-Quellen** (`SRC-001`…`SRC-004`) liegen nicht im Repository, obwohl sich
  133 `EXPLICIT`-Zellen auf sie berufen. Weitere 102 `EXPLICIT`-Zellen nennen gar keine Quelle —
  siehe `docs/SOURCE-MAP.md`.
- **`infra/routing-proxy/`** ist als Ablageort dokumentiert (`CAN-097`), aber **nicht angelegt**.
  Es wurde in diesem Lauf ausdrücklich nichts gebaut, deployt oder als AWS-Ressource erzeugt.

## Hinweis zur Shell

Der Repository-Pfad enthält ein `&`:

```
/Users/vincentschnetzer/Documents/Run&Bike
```

In jedem Shell-Kommando quoten.

## Confirmation Status

`pending-user-confirmation`

Die Assistenz bestätigt weder diese Datei noch den Artefaktsatz im Namen des Nutzers.
