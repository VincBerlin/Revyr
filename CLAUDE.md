# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**REVYR** (working title; German: "Revier") — a mobile health, tracking & community app for runners and cyclists. iOS + Android from one Expo/React Native/TypeScript codebase. **Current state: planning phase — no code exists yet.** The repository contains only planning documents; the Expo app will live in `mobile/` once the first A0 task runs. **The repo is not under version control yet** — that task also runs `git init`.

⚠️ **The repo path contains `&`** (`/Users/vincentschnetzer/Documents/Run&Bike`) — always quote it in shell commands.

## Document Hierarchy (read in this order)

The binding artifacts are the Plumbline product-context set. All four are **pending user confirmation** — nothing here may be treated as approved until the user has confirmed it.

1. `docs/canvas/revyr-endurance-platform.canvas.md` — Product Canvas: problem, target users, value promise, non-goals, constraints, risks, success signal, allowed change scope. The upstream value baseline every later gate re-reads.
2. `docs/prd/revyr-endurance-platform.prd.md` — PRD: REQ-001…REQ-036, acceptance criteria AC-001…AC-036, NFR-001…NFR-008, evidence per REQ, release gates A0/A1/A2/B/C/D/E.
3. `docs/vision/revyr-endurance-platform.vision.md` — Product Vision: target group, user needs, product value, success signals, boundaries.
4. `docs/traceability.md` — REQ ↔ vision ↔ canvas ↔ acceptance ↔ evidence ↔ `wired-in-prod?` ↔ `evidence-class`. **Must be updated as tasks progress.**

Supporting: `docs/implementation/revyr-delivery-plan.md`, `docs/architecture/revyr-target-architecture.md`, `docs/risks/revyr-risk-register.md`, `docs/decisions/open-questions.md` (the single canonical OQ registry), `docs/decisions/decision-log.md`, `docs/EVIDENCE-LEDGER.md`, `docs/validation/validation-report.md`.

⚠️ Earlier revisions of this file named `docs/superpowers/plans/2026-07-10-REVYR-GESAMTPLAN-FINAL.md`, `docs/REVYR-Vision-Canvas-PRD.md` and `docs/REVYR-Plan-PRD.md` as binding. **Those files do not exist in this repo.** Any surviving reference to them is stale — use the four artifacts above.

## Commands (once `mobile/` exists)

All npm/npx commands run from `mobile/`:

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike/mobile"
npm test                 # Jest (jest-expo preset)
npm test -- geo          # single test file by name pattern
npx expo start           # manual verification via Expo Go (QR scan)
```

## Architecture

- **Stack:** Expo SDK, TypeScript strict, expo-router (file-based navigation), zustand, **SQLite (transactional, versioned)** for activity storage, react-native-maps, expo-location, Jest + jest-expo + @testing-library/react-native. AsyncStorage is acceptable for small preferences only — **REQ-005 forbids** persisting tracks as a single unversioned AsyncStorage JSON. The map/routing provider is an open decision (see the OQ registry) and is reached through a server-side proxy, never a client-embedded key.
- **Module layout:**
  - `mobile/app/` — expo-router screens only
  - `mobile/src/domain/` — **pure, dependency-free logic** (distance, pace, effort, points, zones, load score, territory…). Every formula lives here so it is unit-testable and simulatable. This is the load-bearing architectural rule.
  - `mobile/src/services/` — thin wrappers for device/external APIs (GPS, routing, health, BLE, backend) so screens stay testable with mocks
  - `mobile/src/db/` — local persistence + (later) sync queue
  - `mobile/src/state/` — zustand stores (e.g. tracking session, sport mode)
  - `mobile/src/config/` — sport configuration objects and design tokens
- **Run/Bike duality:** sports are `'run' | 'ride'` everywhere. One architecture, two experiences: a global sport-mode store + per-sport config objects drive metrics, thresholds, sampling, auto-pause — **never hardcode sport-specific values, never duplicate screens.** Rankings/challenges/records are strictly sport-separated; cross-sport scoring uses effort normalization (start: Run 1.0 / Bike 0.4).
- **Backend:** no user-facing backend in v1.0 (all local, no account). **One exception, decided 2026-07-19:** a minimal server-side routing proxy exists from A0 so the routing API key never ships in the client (NFR-007). The full backend decision for social/geo/realtime/EU hosting stays open (see the OQ registry; Supabase/PostGIS is the leaning candidate).

## Working Rules (from the Canvas + PRD)

- **TDD is mandatory.** Write the failing test first; tests colocated in `__tests__/` folders next to the code. Every domain/service/store module fully covered; every screen has at least one behavior test.
- **Before implementing a release stage:** write a TDD detail plan carrying the REQ-IDs per task. After completing a task: update the row in `docs/traceability.md` (including `wired-in-prod?` and `evidence-class`) and add an Evidence Ledger entry.
- **Evidence Ledger:** no task is done without an entry in `docs/EVIDENCE-LEDGER.md` (newest on top). Real behavior on real hardware counts; **Run and Bike are verified separately.** A gate passes only when all REQs of its version are ✅.
- **UI copy is German** ("Lauf starten", "Stopp", "Verbleibend"); i18n-prepared.
- TypeScript strict; files < 500 lines; functions < 50 lines; immutable state updates only.
- **No secrets in the client.** `EXPO_PUBLIC_*` variables are inlined into the shipped JS bundle and are extractable from any build — they are **not** a secret store. The routing API key lives server-side behind the proxy (NFR-007). `.env` stays gitignored; commit `.env.example`.
- Conventional commits (`feat:`, `test:`, `chore:` …), no attribution footer.
- **Design system:** strict black & white ("Farbe muss man sich verdienen") — color only for team colors, health traffic light, and celebration moments. Design tokens in `src/config/theme.ts`; WCAG AA. In any web output (success-card renderer, guardian link): never use CSS color-mix functions — use `fill-opacity`/`rgba` instead.
- **Health claims:** all health statements are orientation, never diagnosis/instruction. Recommendation features are blocked until legal claims clearance (see the claims-whitelist entry in the OQ registry).
- **Scope guard:** the confirmed Canvas + PRD are the boundary. Never in scope: purchasable avatars/boosts, chat, AR/virtual races, indoor workouts, web client (except guardian link).
