# Run&Bike — Tracking + Planned Routes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A working iOS/Android app (single Expo codebase) where a user presses Start and gets live GPS tracking with distance/time/pace and a route drawn on a map (Modus A), or first plans a route via map waypoints / a distance goal and sees planned vs. remaining kilometers while tracking (Modus B); finished activities are saved locally and browsable in a history.

**Architecture:** Expo (React Native, TypeScript) app with expo-router file-based navigation. Pure domain logic (distance, pace, progress) lives in dependency-free modules under `src/domain/` and is unit-tested first. Device APIs (GPS, storage) are wrapped in thin service modules so screens stay testable with mocks. Active-session state lives in a zustand store; finished activities are persisted as JSON via AsyncStorage. Route computation for Modus B calls the OpenRouteService directions API.

**Tech Stack:** Expo SDK (latest via `create-expo-app`), TypeScript (strict), expo-router, expo-location, react-native-maps, zustand, @react-native-async-storage/async-storage, expo-crypto, expo-keep-awake, Jest + jest-expo + @testing-library/react-native, OpenRouteService API.

## Global Constraints

- Target platforms: **iOS / Apple App Store** and **Android / Google Play Store** from one codebase (concept doc §34).
- All UI copy is **German** (matches the concept document; e.g. "Lauf starten", "Stopp", "Verbleibend").
- Sports are `'run' | 'ride'` everywhere — runners and cyclists get separate activity types (concept §2).
- **Out of scope for this plan** (later plans): accounts/backend, social/follow, teams, territory, challenges, health/recovery analysis, audio navigation, background GPS tracking, finger-sketch route interpretation. Modus B here = waypoint-tap route planning + distance goal.
- The Expo app lives in `mobile/` inside the repo root `/Users/vincentschnetzer/Documents/Run&Bike`. **The path contains `&` — always quote it in shell commands.** All `npm`/`npx` commands run from `mobile/` unless stated otherwise.
- TypeScript strict mode; files under 500 lines; functions under 50 lines; immutable state updates only (never mutate arrays/objects in place).
- No secrets in code: the OpenRouteService key is read from `EXPO_PUBLIC_ORS_API_KEY` (`.env`, gitignored; `.env.example` committed).
- Conventional commit messages (`feat:`, `test:`, `chore:` …), no attribution footer.
- Tests are colocated in `__tests__/` folders next to the code. Run with `npm test`. Target: every domain/service/store module fully covered; every screen has at least one behavior test.
- Manual on-device verification uses Expo Go (`npx expo start`, scan QR). react-native-maps and expo-location foreground tracking work in Expo Go. **Deployment note (not a task):** production Android builds need a Google Maps API key under `android.config.googleMaps.apiKey` in `app.json`.

---

## File Structure

```
Run&Bike/                              # repo root (git init here)
├── RUNNING_CYCLING_APP_KONZEPT_CHAT_ZUSAMMENFASSUNG.md   # existing concept doc
├── docs/superpowers/plans/            # this plan
└── mobile/                            # Expo app
    ├── app/                           # expo-router screens
    │   ├── _layout.tsx                # root stack navigator
    │   ├── index.tsx                  # home: start run/ride, plan, history
    │   ├── track.tsx                  # live tracking screen (Modus A + B)
    │   ├── plan.tsx                   # route planning screen (Modus B)
    │   ├── history/index.tsx          # activity list
    │   ├── history/[id].tsx           # activity detail
    │   └── __tests__/                 # screen tests
    ├── src/
    │   ├── domain/geo.ts              # haversine + track distance (pure)
    │   ├── domain/stats.ts            # duration/pace/speed formatting (pure)
    │   ├── domain/route-progress.ts   # remaining distance / progress (pure)
    │   ├── services/location.ts       # expo-location wrapper
    │   ├── services/routing.ts        # OpenRouteService client
    │   ├── db/activities-repo.ts      # AsyncStorage persistence
    │   ├── state/tracking-store.ts    # zustand: active session
    │   └── state/planned-route-store.ts # zustand: planned route / goal
    ├── jest.setup.js
    └── app.json / package.json / tsconfig.json
```

---

### Task 1: Project Scaffold + Geo Domain

Creates the repo, the Expo app with expo-router and Jest, and delivers the first tested module: geographic distance math. Everything later depends on `haversineDistanceMeters` / `totalDistanceMeters`.

**Files:**
- Create: `mobile/` (via create-expo-app), `mobile/app/_layout.tsx`, `mobile/app/index.tsx` (placeholder), `mobile/src/domain/geo.ts`
- Test: `mobile/src/domain/__tests__/geo.test.ts`
- Modify: `mobile/package.json` (main entry, scripts, jest config), `mobile/app.json` (scheme, expo-router plugin)

**Interfaces:**
- Consumes: nothing (first task).
- Produces:
  - `interface GeoPoint { latitude: number; longitude: number }`
  - `interface TrackPoint extends GeoPoint { timestampMs: number }`
  - `haversineDistanceMeters(a: GeoPoint, b: GeoPoint): number`
  - `totalDistanceMeters(points: readonly GeoPoint[]): number`

- [ ] **Step 1: Initialize repo and scaffold the Expo app**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git init
printf '.DS_Store\n' > .gitignore
npx create-expo-app@latest mobile --template blank-typescript
cd "/Users/vincentschnetzer/Documents/Run&Bike/mobile"
npx expo install expo-router react-native-safe-area-context react-native-screens expo-linking expo-constants expo-status-bar
npm install zustand
npm install --save-dev jest-expo jest @types/jest @testing-library/react-native
```

- [ ] **Step 2: Wire up expo-router and Jest**

In `mobile/package.json`, set the entry point, add scripts, and add the Jest config (top-level keys inside the existing JSON object):

```json
{
  "main": "expo-router/entry",
  "scripts": {
    "start": "expo start",
    "android": "expo run:android",
    "ios": "expo run:ios",
    "test": "jest"
  },
  "jest": {
    "preset": "jest-expo",
    "transformIgnorePatterns": [
      "node_modules/(?!((jest-)?react-native|@react-native(-community)?)|expo(nent)?|@expo(nent)?/.*|@expo-google-fonts/.*|react-navigation|@react-navigation/.*|@sentry/react-native|native-base|react-native-svg)"
    ]
  }
}
```

Delete the template's `App.tsx` (and `index.ts` if the template created one):

```bash
rm -f App.tsx index.ts
```

In `mobile/app.json`, inside the `"expo"` object add:

```json
{
  "scheme": "runandbike",
  "plugins": ["expo-router"]
}
```

Create `mobile/app/_layout.tsx`:

```tsx
import { Stack } from 'expo-router';

export default function RootLayout() {
  return <Stack screenOptions={{ headerTitleAlign: 'center' }} />;
}
```

Create `mobile/app/index.tsx` (placeholder, replaced in Task 6):

```tsx
import { Text, View } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Run&Bike</Text>
    </View>
  );
}
```

- [ ] **Step 3: Write the failing geo test**

Create `mobile/src/domain/__tests__/geo.test.ts`:

```ts
import { haversineDistanceMeters, totalDistanceMeters } from '../geo';

describe('haversineDistanceMeters', () => {
  it('returns 0 for identical points', () => {
    const p = { latitude: 48.137, longitude: 11.575 };
    expect(haversineDistanceMeters(p, p)).toBe(0);
  });

  it('returns ~111195 m for 1 degree of longitude at the equator', () => {
    const a = { latitude: 0, longitude: 0 };
    const b = { latitude: 0, longitude: 1 };
    expect(haversineDistanceMeters(a, b)).toBeGreaterThan(111100);
    expect(haversineDistanceMeters(a, b)).toBeLessThan(111300);
  });

  it('is symmetric', () => {
    const a = { latitude: 48.137, longitude: 11.575 };
    const b = { latitude: 48.2, longitude: 11.6 };
    expect(haversineDistanceMeters(a, b)).toBeCloseTo(haversineDistanceMeters(b, a), 6);
  });
});

describe('totalDistanceMeters', () => {
  it('returns 0 for fewer than 2 points', () => {
    expect(totalDistanceMeters([])).toBe(0);
    expect(totalDistanceMeters([{ latitude: 0, longitude: 0 }])).toBe(0);
  });

  it('sums segment distances', () => {
    const points = [
      { latitude: 0, longitude: 0 },
      { latitude: 0, longitude: 0.01 },
      { latitude: 0, longitude: 0.02 },
    ];
    const oneSegment = haversineDistanceMeters(points[0], points[1]);
    expect(totalDistanceMeters(points)).toBeCloseTo(2 * oneSegment, 6);
  });
});
```

- [ ] **Step 4: Run test to verify it fails**

Run: `npm test -- geo`
Expected: FAIL with `Cannot find module '../geo'`

- [ ] **Step 5: Implement the geo module**

Create `mobile/src/domain/geo.ts`:

```ts
export interface GeoPoint {
  latitude: number;
  longitude: number;
}

export interface TrackPoint extends GeoPoint {
  timestampMs: number;
}

const EARTH_RADIUS_METERS = 6371000;

const toRadians = (degrees: number): number => (degrees * Math.PI) / 180;

export function haversineDistanceMeters(a: GeoPoint, b: GeoPoint): number {
  const dLat = toRadians(b.latitude - a.latitude);
  const dLon = toRadians(b.longitude - a.longitude);
  const lat1 = toRadians(a.latitude);
  const lat2 = toRadians(b.latitude);
  const h =
    Math.sin(dLat / 2) ** 2 + Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon / 2) ** 2;
  return 2 * EARTH_RADIUS_METERS * Math.asin(Math.sqrt(h));
}

export function totalDistanceMeters(points: readonly GeoPoint[]): number {
  let sum = 0;
  for (let i = 1; i < points.length; i += 1) {
    sum += haversineDistanceMeters(points[i - 1], points[i]);
  }
  return sum;
}
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `npm test -- geo`
Expected: PASS (5 tests)

- [ ] **Step 7: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add .
git commit -m "feat: scaffold Expo app with expo-router, Jest, and geo domain module"
```

---

### Task 2: Stats + Route-Progress Domain

Pure formatting and progress math used by the tracking screen and history.

**Files:**
- Create: `mobile/src/domain/stats.ts`, `mobile/src/domain/route-progress.ts`
- Test: `mobile/src/domain/__tests__/stats.test.ts`, `mobile/src/domain/__tests__/route-progress.test.ts`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `formatDuration(ms: number): string` — `"12:34"` under 1 h, `"1:02:03"` above
  - `paceMinPerKm(distanceMeters: number, durationMs: number): number | null` — `null` below 10 m
  - `formatPace(pace: number | null): string` — `"5:30 /km"` or `"–"`
  - `formatKm(meters: number): string` — `"12.80 km"`
  - `remainingDistanceMeters(plannedMeters: number, coveredMeters: number): number` — clamped ≥ 0
  - `progressFraction(plannedMeters: number, coveredMeters: number): number` — 0..1 clamped

- [ ] **Step 1: Write the failing stats test**

Create `mobile/src/domain/__tests__/stats.test.ts`:

```ts
import { formatDuration, paceMinPerKm, formatPace, formatKm } from '../stats';

describe('formatDuration', () => {
  it('formats minutes and seconds under an hour', () => {
    expect(formatDuration(754000)).toBe('12:34');
  });

  it('formats hours above an hour', () => {
    expect(formatDuration(3723000)).toBe('1:02:03');
  });

  it('clamps negative input to 0:00', () => {
    expect(formatDuration(-5000)).toBe('0:00');
  });
});

describe('paceMinPerKm', () => {
  it('returns 5.5 min/km for 1 km in 5:30', () => {
    expect(paceMinPerKm(1000, 330000)).toBeCloseTo(5.5, 6);
  });

  it('returns null below 10 meters', () => {
    expect(paceMinPerKm(5, 60000)).toBeNull();
  });
});

describe('formatPace', () => {
  it('formats 5.5 as 5:30 /km', () => {
    expect(formatPace(5.5)).toBe('5:30 /km');
  });

  it('renders a dash for null', () => {
    expect(formatPace(null)).toBe('–');
  });

  it('rolls over 59.6 seconds to the next minute', () => {
    expect(formatPace(4.9999)).toBe('5:00 /km');
  });
});

describe('formatKm', () => {
  it('formats meters as km with two decimals', () => {
    expect(formatKm(12800)).toBe('12.80 km');
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npm test -- stats`
Expected: FAIL with `Cannot find module '../stats'`

- [ ] **Step 3: Implement the stats module**

Create `mobile/src/domain/stats.ts`:

```ts
const twoDigits = (n: number): string => String(n).padStart(2, '0');

export function formatDuration(ms: number): string {
  const totalSeconds = Math.max(0, Math.floor(ms / 1000));
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  if (hours > 0) {
    return `${hours}:${twoDigits(minutes)}:${twoDigits(seconds)}`;
  }
  return `${minutes}:${twoDigits(seconds)}`;
}

const MIN_DISTANCE_FOR_PACE_METERS = 10;

export function paceMinPerKm(distanceMeters: number, durationMs: number): number | null {
  if (distanceMeters < MIN_DISTANCE_FOR_PACE_METERS) {
    return null;
  }
  return durationMs / 60000 / (distanceMeters / 1000);
}

export function formatPace(pace: number | null): string {
  if (pace === null || !Number.isFinite(pace)) {
    return '–';
  }
  let minutes = Math.floor(pace);
  let seconds = Math.round((pace - minutes) * 60);
  if (seconds === 60) {
    minutes += 1;
    seconds = 0;
  }
  return `${minutes}:${twoDigits(seconds)} /km`;
}

export function formatKm(meters: number): string {
  return `${(meters / 1000).toFixed(2)} km`;
}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `npm test -- stats`
Expected: PASS (9 tests)

- [ ] **Step 5: Write the failing route-progress test**

Create `mobile/src/domain/__tests__/route-progress.test.ts`:

```ts
import { remainingDistanceMeters, progressFraction } from '../route-progress';

describe('remainingDistanceMeters', () => {
  it('subtracts covered from planned', () => {
    expect(remainingDistanceMeters(12800, 4300)).toBe(8500);
  });

  it('never goes below zero', () => {
    expect(remainingDistanceMeters(5000, 6000)).toBe(0);
  });
});

describe('progressFraction', () => {
  it('returns the covered fraction', () => {
    expect(progressFraction(10000, 2500)).toBeCloseTo(0.25, 6);
  });

  it('clamps to 1 when overshooting', () => {
    expect(progressFraction(5000, 9000)).toBe(1);
  });

  it('returns 0 for a zero-length plan', () => {
    expect(progressFraction(0, 100)).toBe(0);
  });
});
```

- [ ] **Step 6: Run test to verify it fails**

Run: `npm test -- route-progress`
Expected: FAIL with `Cannot find module '../route-progress'`

- [ ] **Step 7: Implement route-progress**

Create `mobile/src/domain/route-progress.ts`:

```ts
export function remainingDistanceMeters(plannedMeters: number, coveredMeters: number): number {
  return Math.max(0, plannedMeters - coveredMeters);
}

export function progressFraction(plannedMeters: number, coveredMeters: number): number {
  if (plannedMeters <= 0) {
    return 0;
  }
  return Math.min(1, coveredMeters / plannedMeters);
}
```

- [ ] **Step 8: Run all tests to verify they pass**

Run: `npm test`
Expected: PASS (all suites)

- [ ] **Step 9: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/src/domain
git commit -m "feat: add stats formatting and route progress domain modules"
```

---

### Task 3: Tracking Session Store

The zustand store holding the active session: start, incoming GPS points (distance accumulates incrementally), stop returns a completed-activity summary. Time comes in as parameters — no `Date.now()` inside the store, so tests are deterministic.

**Files:**
- Create: `mobile/src/state/tracking-store.ts`
- Test: `mobile/src/state/__tests__/tracking-store.test.ts`

**Interfaces:**
- Consumes: `TrackPoint`, `haversineDistanceMeters` from `src/domain/geo.ts` (Task 1).
- Produces:
  - `type Sport = 'run' | 'ride'`
  - `interface CompletedSession { sport: Sport; startedAtMs: number; endedAtMs: number; durationMs: number; distanceMeters: number; points: TrackPoint[] }`
  - `useTrackingStore` zustand hook with state `{ status: 'idle' | 'tracking'; sport: Sport; startedAtMs: number | null; points: TrackPoint[]; distanceMeters: number }` and actions `start(sport: Sport, nowMs: number): void`, `addPoint(point: TrackPoint): void`, `stop(nowMs: number): CompletedSession | null`, `reset(): void`

- [ ] **Step 1: Write the failing store test**

Create `mobile/src/state/__tests__/tracking-store.test.ts`:

```ts
import { useTrackingStore } from '../tracking-store';

const point = (longitude: number, timestampMs: number) => ({
  latitude: 0,
  longitude,
  timestampMs,
});

beforeEach(() => {
  useTrackingStore.getState().reset();
});

describe('tracking store', () => {
  it('starts a session with the given sport and empty track', () => {
    useTrackingStore.getState().start('ride', 1000);
    const state = useTrackingStore.getState();
    expect(state.status).toBe('tracking');
    expect(state.sport).toBe('ride');
    expect(state.startedAtMs).toBe(1000);
    expect(state.points).toEqual([]);
    expect(state.distanceMeters).toBe(0);
  });

  it('accumulates distance from incoming points', () => {
    useTrackingStore.getState().start('run', 0);
    useTrackingStore.getState().addPoint(point(0, 1000));
    useTrackingStore.getState().addPoint(point(0.01, 2000));
    const state = useTrackingStore.getState();
    expect(state.points).toHaveLength(2);
    expect(state.distanceMeters).toBeGreaterThan(1100);
    expect(state.distanceMeters).toBeLessThan(1125);
  });

  it('ignores points while idle', () => {
    useTrackingStore.getState().addPoint(point(0, 1000));
    expect(useTrackingStore.getState().points).toHaveLength(0);
  });

  it('stop returns a completed session and goes idle', () => {
    useTrackingStore.getState().start('run', 1000);
    useTrackingStore.getState().addPoint(point(0, 1500));
    const completed = useTrackingStore.getState().stop(61000);
    expect(completed).not.toBeNull();
    expect(completed?.durationMs).toBe(60000);
    expect(completed?.sport).toBe('run');
    expect(completed?.points).toHaveLength(1);
    expect(useTrackingStore.getState().status).toBe('idle');
  });

  it('stop while idle returns null', () => {
    expect(useTrackingStore.getState().stop(5000)).toBeNull();
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npm test -- tracking-store`
Expected: FAIL with `Cannot find module '../tracking-store'`

- [ ] **Step 3: Implement the store**

Create `mobile/src/state/tracking-store.ts`:

```ts
import { create } from 'zustand';
import { haversineDistanceMeters, TrackPoint } from '../domain/geo';

export type Sport = 'run' | 'ride';

export interface CompletedSession {
  sport: Sport;
  startedAtMs: number;
  endedAtMs: number;
  durationMs: number;
  distanceMeters: number;
  points: TrackPoint[];
}

interface TrackingState {
  status: 'idle' | 'tracking';
  sport: Sport;
  startedAtMs: number | null;
  points: TrackPoint[];
  distanceMeters: number;
  start: (sport: Sport, nowMs: number) => void;
  addPoint: (point: TrackPoint) => void;
  stop: (nowMs: number) => CompletedSession | null;
  reset: () => void;
}

const IDLE_STATE = {
  status: 'idle' as const,
  sport: 'run' as const,
  startedAtMs: null,
  points: [] as TrackPoint[],
  distanceMeters: 0,
};

export const useTrackingStore = create<TrackingState>((set, get) => ({
  ...IDLE_STATE,

  start: (sport, nowMs) =>
    set({ status: 'tracking', sport, startedAtMs: nowMs, points: [], distanceMeters: 0 }),

  addPoint: (point) =>
    set((state) => {
      if (state.status !== 'tracking') {
        return state;
      }
      const last = state.points[state.points.length - 1];
      const added = last ? haversineDistanceMeters(last, point) : 0;
      return {
        points: [...state.points, point],
        distanceMeters: state.distanceMeters + added,
      };
    }),

  stop: (nowMs) => {
    const state = get();
    if (state.status !== 'tracking' || state.startedAtMs === null) {
      return null;
    }
    const completed: CompletedSession = {
      sport: state.sport,
      startedAtMs: state.startedAtMs,
      endedAtMs: nowMs,
      durationMs: nowMs - state.startedAtMs,
      distanceMeters: state.distanceMeters,
      points: state.points,
    };
    set({ status: 'idle' });
    return completed;
  },

  reset: () => set({ ...IDLE_STATE }),
}));
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `npm test -- tracking-store`
Expected: PASS (5 tests)

- [ ] **Step 5: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/src/state
git commit -m "feat: add tracking session store with incremental distance"
```

---

### Task 4: Activities Repository (AsyncStorage)

Local persistence for finished activities: full activity per key, plus a summary index for the history list. Uses the official AsyncStorage Jest mock.

**Files:**
- Create: `mobile/src/db/activities-repo.ts`, `mobile/jest.setup.js`
- Test: `mobile/src/db/__tests__/activities-repo.test.ts`
- Modify: `mobile/package.json` (add `setupFiles` to jest config)

**Interfaces:**
- Consumes: `Sport` from `src/state/tracking-store.ts` (Task 3), `TrackPoint` from `src/domain/geo.ts` (Task 1).
- Produces:
  - `interface Activity { id: string; sport: Sport; startedAtMs: number; endedAtMs: number; durationMs: number; distanceMeters: number; points: TrackPoint[]; plannedDistanceMeters?: number }`
  - `interface ActivitySummary { id: string; sport: Sport; startedAtMs: number; durationMs: number; distanceMeters: number }`
  - `saveActivity(activity: Activity): Promise<void>`
  - `listActivities(): Promise<ActivitySummary[]>` — newest first
  - `getActivity(id: string): Promise<Activity | null>`

- [ ] **Step 1: Install AsyncStorage and register its Jest mock**

```bash
npx expo install @react-native-async-storage/async-storage
```

Create `mobile/jest.setup.js`:

```js
jest.mock('@react-native-async-storage/async-storage', () =>
  require('@react-native-async-storage/async-storage/jest/async-storage-mock'),
);
```

In `mobile/package.json`, extend the `"jest"` block with:

```json
"setupFiles": ["<rootDir>/jest.setup.js"]
```

- [ ] **Step 2: Write the failing repository test**

Create `mobile/src/db/__tests__/activities-repo.test.ts`:

```ts
import AsyncStorage from '@react-native-async-storage/async-storage';
import { saveActivity, listActivities, getActivity, Activity } from '../activities-repo';

const makeActivity = (id: string, startedAtMs: number): Activity => ({
  id,
  sport: 'run',
  startedAtMs,
  endedAtMs: startedAtMs + 60000,
  durationMs: 60000,
  distanceMeters: 1500,
  points: [{ latitude: 0, longitude: 0, timestampMs: startedAtMs }],
});

beforeEach(async () => {
  await AsyncStorage.clear();
});

describe('activities repo', () => {
  it('returns an empty list initially', async () => {
    expect(await listActivities()).toEqual([]);
  });

  it('round-trips a saved activity', async () => {
    const activity = makeActivity('a1', 1000);
    await saveActivity(activity);
    expect(await getActivity('a1')).toEqual(activity);
  });

  it('returns null for an unknown id', async () => {
    expect(await getActivity('missing')).toBeNull();
  });

  it('lists summaries newest-first without points', async () => {
    await saveActivity(makeActivity('old', 1000));
    await saveActivity(makeActivity('new', 2000));
    const summaries = await listActivities();
    expect(summaries.map((s) => s.id)).toEqual(['new', 'old']);
    expect(summaries[0]).not.toHaveProperty('points');
  });

  it('keeps the optional planned distance', async () => {
    await saveActivity({ ...makeActivity('p1', 1000), plannedDistanceMeters: 12800 });
    expect((await getActivity('p1'))?.plannedDistanceMeters).toBe(12800);
  });
});
```

- [ ] **Step 3: Run test to verify it fails**

Run: `npm test -- activities-repo`
Expected: FAIL with `Cannot find module '../activities-repo'`

- [ ] **Step 4: Implement the repository**

Create `mobile/src/db/activities-repo.ts`:

```ts
import AsyncStorage from '@react-native-async-storage/async-storage';
import { TrackPoint } from '../domain/geo';
import { Sport } from '../state/tracking-store';

export interface Activity {
  id: string;
  sport: Sport;
  startedAtMs: number;
  endedAtMs: number;
  durationMs: number;
  distanceMeters: number;
  points: TrackPoint[];
  plannedDistanceMeters?: number;
}

export interface ActivitySummary {
  id: string;
  sport: Sport;
  startedAtMs: number;
  durationMs: number;
  distanceMeters: number;
}

const INDEX_KEY = 'activities:index';
const activityKey = (id: string): string => `activities:${id}`;

const toSummary = (activity: Activity): ActivitySummary => ({
  id: activity.id,
  sport: activity.sport,
  startedAtMs: activity.startedAtMs,
  durationMs: activity.durationMs,
  distanceMeters: activity.distanceMeters,
});

export async function listActivities(): Promise<ActivitySummary[]> {
  const raw = await AsyncStorage.getItem(INDEX_KEY);
  if (!raw) {
    return [];
  }
  try {
    return JSON.parse(raw) as ActivitySummary[];
  } catch {
    return [];
  }
}

export async function saveActivity(activity: Activity): Promise<void> {
  const existing = await listActivities();
  const nextIndex = [
    toSummary(activity),
    ...existing.filter((summary) => summary.id !== activity.id),
  ];
  await AsyncStorage.setItem(activityKey(activity.id), JSON.stringify(activity));
  await AsyncStorage.setItem(INDEX_KEY, JSON.stringify(nextIndex));
}

export async function getActivity(id: string): Promise<Activity | null> {
  const raw = await AsyncStorage.getItem(activityKey(id));
  if (!raw) {
    return null;
  }
  try {
    return JSON.parse(raw) as Activity;
  } catch {
    return null;
  }
}
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `npm test -- activities-repo`
Expected: PASS (5 tests)

- [ ] **Step 6: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/src/db mobile/jest.setup.js mobile/package.json mobile/package-lock.json
git commit -m "feat: add local activities repository on AsyncStorage"
```

---

### Task 5: Location Service + Permission Config

Thin wrapper around expo-location: request foreground permission, subscribe to position updates as `TrackPoint`s. Also declares the permission strings in `app.json`.

**Files:**
- Create: `mobile/src/services/location.ts`
- Test: `mobile/src/services/__tests__/location.test.ts`
- Modify: `mobile/app.json` (expo-location plugin)

**Interfaces:**
- Consumes: `TrackPoint` from `src/domain/geo.ts` (Task 1).
- Produces:
  - `requestLocationPermission(): Promise<boolean>`
  - `watchLocation(onPoint: (point: TrackPoint) => void): Promise<() => void>` — resolves to an unsubscribe function

- [ ] **Step 1: Install expo-location and declare permissions**

```bash
npx expo install expo-location
```

In `mobile/app.json`, extend the `"plugins"` array to:

```json
"plugins": [
  "expo-router",
  [
    "expo-location",
    {
      "locationWhenInUsePermission": "Run&Bike verwendet deinen Standort, um deine Aktivität und Route aufzuzeichnen."
    }
  ]
]
```

- [ ] **Step 2: Write the failing service test**

Create `mobile/src/services/__tests__/location.test.ts`:

```ts
jest.mock('expo-location', () => ({
  Accuracy: { BestForNavigation: 6 },
  requestForegroundPermissionsAsync: jest.fn(),
  watchPositionAsync: jest.fn(),
}));

import * as Location from 'expo-location';
import { requestLocationPermission, watchLocation } from '../location';

const mockedLocation = Location as jest.Mocked<typeof Location>;

describe('requestLocationPermission', () => {
  it('returns true when granted', async () => {
    mockedLocation.requestForegroundPermissionsAsync.mockResolvedValue({
      status: 'granted',
    } as never);
    expect(await requestLocationPermission()).toBe(true);
  });

  it('returns false when denied', async () => {
    mockedLocation.requestForegroundPermissionsAsync.mockResolvedValue({
      status: 'denied',
    } as never);
    expect(await requestLocationPermission()).toBe(false);
  });
});

describe('watchLocation', () => {
  it('maps location updates to TrackPoints and returns an unsubscribe', async () => {
    const remove = jest.fn();
    mockedLocation.watchPositionAsync.mockImplementation(async (_options, callback) => {
      callback({
        coords: { latitude: 48.1, longitude: 11.5 },
        timestamp: 1234,
      } as never);
      return { remove } as never;
    });

    const received: unknown[] = [];
    const unsubscribe = await watchLocation((point) => received.push(point));

    expect(received).toEqual([{ latitude: 48.1, longitude: 11.5, timestampMs: 1234 }]);
    unsubscribe();
    expect(remove).toHaveBeenCalled();
  });
});
```

- [ ] **Step 3: Run test to verify it fails**

Run: `npm test -- services/__tests__/location`
Expected: FAIL with `Cannot find module '../location'`

- [ ] **Step 4: Implement the service**

Create `mobile/src/services/location.ts`:

```ts
import * as Location from 'expo-location';
import { TrackPoint } from '../domain/geo';

export async function requestLocationPermission(): Promise<boolean> {
  const { status } = await Location.requestForegroundPermissionsAsync();
  return status === 'granted';
}

export async function watchLocation(
  onPoint: (point: TrackPoint) => void,
): Promise<() => void> {
  const subscription = await Location.watchPositionAsync(
    {
      accuracy: Location.Accuracy.BestForNavigation,
      timeInterval: 2000,
      distanceInterval: 5,
    },
    (location) => {
      onPoint({
        latitude: location.coords.latitude,
        longitude: location.coords.longitude,
        timestampMs: location.timestamp,
      });
    },
  );
  return () => subscription.remove();
}
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `npm test -- services/__tests__/location`
Expected: PASS (3 tests)

- [ ] **Step 6: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/src/services mobile/app.json mobile/package.json mobile/package-lock.json
git commit -m "feat: add location service wrapper and permission config"
```

---

### Task 6: Home Screen

Replaces the placeholder with the real entry screen: start a run or ride (Modus A), plan a route (Modus B), open the history.

**Files:**
- Modify: `mobile/app/index.tsx` (replace placeholder from Task 1 entirely)
- Test: `mobile/app/__tests__/index.test.tsx`

**Interfaces:**
- Consumes: expo-router `Link`.
- Produces: navigation targets used by later tasks — `/track?sport=run`, `/track?sport=ride`, `/plan`, `/history`.

- [ ] **Step 1: Write the failing screen test**

Create `mobile/app/__tests__/index.test.tsx`:

```tsx
import React from 'react';
import { render } from '@testing-library/react-native';

jest.mock('expo-router', () => {
  const { View } = require('react-native');
  return {
    Link: ({ children }: { children: React.ReactNode }) => <View>{children}</View>,
  };
});

import HomeScreen from '../index';

describe('HomeScreen', () => {
  it('shows all four entry actions', () => {
    const { getByText } = render(<HomeScreen />);
    expect(getByText('Lauf starten')).toBeTruthy();
    expect(getByText('Fahrt starten')).toBeTruthy();
    expect(getByText('Route planen')).toBeTruthy();
    expect(getByText('Verlauf')).toBeTruthy();
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npm test -- app/__tests__/index`
Expected: FAIL — `Unable to find an element with text: Lauf starten` (placeholder only renders "Run&Bike")

- [ ] **Step 3: Implement the home screen**

Replace the entire content of `mobile/app/index.tsx`:

```tsx
import { Link } from 'expo-router';
import { StyleSheet, Text, View } from 'react-native';

const actions = [
  { href: { pathname: '/track', params: { sport: 'run' } }, label: 'Lauf starten' },
  { href: { pathname: '/track', params: { sport: 'ride' } }, label: 'Fahrt starten' },
  { href: { pathname: '/plan' }, label: 'Route planen' },
  { href: { pathname: '/history' }, label: 'Verlauf' },
] as const;

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Run&Bike</Text>
      {actions.map((action) => (
        <Link key={action.label} href={action.href} style={styles.button}>
          <Text style={styles.buttonText}>{action.label}</Text>
        </Link>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: 'center', justifyContent: 'center', gap: 16 },
  title: { fontSize: 32, fontWeight: 'bold', marginBottom: 24 },
  button: {
    backgroundColor: '#1d4ed8',
    borderRadius: 12,
    paddingHorizontal: 32,
    paddingVertical: 14,
    overflow: 'hidden',
  },
  buttonText: { color: '#ffffff', fontSize: 18, fontWeight: '600' },
});
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `npm test -- app/__tests__/index`
Expected: PASS (1 test)

- [ ] **Step 5: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/app
git commit -m "feat: add home screen with start, plan, and history actions"
```

---

### Task 7: Live Tracking Screen (Modus A complete)

The core screen: requests permission, starts the session, feeds GPS points into the store, shows map + live stats, keeps the screen awake, and on Stopp saves the activity and navigates to its detail page.

**Files:**
- Create: `mobile/app/track.tsx`
- Test: `mobile/app/__tests__/track.test.tsx`

**Interfaces:**
- Consumes: `useTrackingStore` (Task 3: `start(sport, nowMs)`, `addPoint(point)`, `stop(nowMs)`), `requestLocationPermission` / `watchLocation` (Task 5), `saveActivity` + `Activity` (Task 4), `formatDuration` / `formatPace` / `paceMinPerKm` / `formatKm` (Task 2), `Crypto.randomUUID()` (expo-crypto), `useKeepAwake` (expo-keep-awake).
- Produces: route `/track` accepting `sport` search param; navigates to `/history/<id>` after saving. Task 12 extends this file for planned-route display.

- [ ] **Step 1: Install map and device packages**

```bash
npx expo install react-native-maps expo-crypto expo-keep-awake
```

- [ ] **Step 2: Write the failing screen test**

Create `mobile/app/__tests__/track.test.tsx`:

```tsx
import React from 'react';
import { fireEvent, render, waitFor } from '@testing-library/react-native';

jest.mock('react-native-maps', () => {
  const React = require('react');
  const { View } = require('react-native');
  return {
    __esModule: true,
    default: (props: object) => React.createElement(View, { testID: 'map', ...props }),
    Marker: (props: object) => React.createElement(View, props),
    Polyline: (props: object) => React.createElement(View, props),
  };
});
jest.mock('expo-router', () => ({
  router: { replace: jest.fn(), push: jest.fn() },
  useLocalSearchParams: () => ({ sport: 'run' }),
}));
jest.mock('expo-keep-awake', () => ({ useKeepAwake: () => undefined }));
jest.mock('expo-crypto', () => ({ randomUUID: () => 'test-uuid' }));
jest.mock('../../src/services/location', () => ({
  requestLocationPermission: jest.fn().mockResolvedValue(true),
  watchLocation: jest.fn().mockResolvedValue(() => undefined),
}));
jest.mock('../../src/db/activities-repo', () => ({
  saveActivity: jest.fn().mockResolvedValue(undefined),
}));

import { router } from 'expo-router';
import TrackScreen from '../track';
import { saveActivity } from '../../src/db/activities-repo';
import { useTrackingStore } from '../../src/state/tracking-store';

beforeEach(() => {
  jest.clearAllMocks();
  useTrackingStore.getState().reset();
});

describe('TrackScreen', () => {
  it('starts tracking and shows the accumulated distance', async () => {
    const { getByText } = render(<TrackScreen />);
    await waitFor(() => expect(useTrackingStore.getState().status).toBe('tracking'));

    useTrackingStore.getState().addPoint({ latitude: 0, longitude: 0, timestampMs: 1000 });
    useTrackingStore.getState().addPoint({ latitude: 0, longitude: 0.01, timestampMs: 2000 });

    await waitFor(() => expect(getByText('1.11 km')).toBeTruthy());
  });

  it('saves the activity on Stopp and navigates to its detail page', async () => {
    const { getByText } = render(<TrackScreen />);
    await waitFor(() => expect(useTrackingStore.getState().status).toBe('tracking'));

    fireEvent.press(getByText('Stopp'));

    await waitFor(() => expect(saveActivity).toHaveBeenCalledTimes(1));
    const saved = (saveActivity as jest.Mock).mock.calls[0][0];
    expect(saved.id).toBe('test-uuid');
    expect(saved.sport).toBe('run');
    expect(router.replace).toHaveBeenCalledWith('/history/test-uuid');
  });
});
```

- [ ] **Step 3: Run test to verify it fails**

Run: `npm test -- app/__tests__/track`
Expected: FAIL with `Cannot find module '../track'`

- [ ] **Step 4: Implement the tracking screen**

Create `mobile/app/track.tsx`:

```tsx
import * as Crypto from 'expo-crypto';
import { useKeepAwake } from 'expo-keep-awake';
import { router, useLocalSearchParams } from 'expo-router';
import { useEffect, useState } from 'react';
import { Pressable, StyleSheet, Text, View } from 'react-native';
import MapView, { Polyline } from 'react-native-maps';
import { formatDuration, formatKm, formatPace, paceMinPerKm } from '../src/domain/stats';
import { saveActivity } from '../src/db/activities-repo';
import { requestLocationPermission, watchLocation } from '../src/services/location';
import { Sport, useTrackingStore } from '../src/state/tracking-store';

const DEFAULT_REGION = {
  latitude: 48.137,
  longitude: 11.575,
  latitudeDelta: 0.02,
  longitudeDelta: 0.02,
};

export default function TrackScreen() {
  useKeepAwake();
  const params = useLocalSearchParams<{ sport?: string }>();
  const sport: Sport = params.sport === 'ride' ? 'ride' : 'run';

  const status = useTrackingStore((state) => state.status);
  const points = useTrackingStore((state) => state.points);
  const distanceMeters = useTrackingStore((state) => state.distanceMeters);
  const startedAtMs = useTrackingStore((state) => state.startedAtMs);

  const [permissionDenied, setPermissionDenied] = useState(false);
  const [nowMs, setNowMs] = useState(() => Date.now());

  useEffect(() => {
    let unsubscribe: (() => void) | null = null;
    let cancelled = false;
    (async () => {
      const granted = await requestLocationPermission();
      if (cancelled) {
        return;
      }
      if (!granted) {
        setPermissionDenied(true);
        return;
      }
      useTrackingStore.getState().start(sport, Date.now());
      unsubscribe = await watchLocation((point) => {
        useTrackingStore.getState().addPoint(point);
      });
    })();
    return () => {
      cancelled = true;
      if (unsubscribe) {
        unsubscribe();
      }
    };
  }, [sport]);

  useEffect(() => {
    const timer = setInterval(() => setNowMs(Date.now()), 1000);
    return () => clearInterval(timer);
  }, []);

  const onStop = async () => {
    const completed = useTrackingStore.getState().stop(Date.now());
    if (!completed) {
      return;
    }
    const id = Crypto.randomUUID();
    await saveActivity({ id, ...completed });
    router.replace(`/history/${id}`);
  };

  if (permissionDenied) {
    return (
      <View style={styles.center}>
        <Text style={styles.message}>
          Ohne Standortberechtigung kann keine Aktivität aufgezeichnet werden.
        </Text>
      </View>
    );
  }

  const elapsedMs = status === 'tracking' && startedAtMs !== null ? nowMs - startedAtMs : 0;
  const pace = formatPace(paceMinPerKm(distanceMeters, elapsedMs));

  return (
    <View style={styles.container}>
      <MapView style={styles.map} initialRegion={DEFAULT_REGION} showsUserLocation>
        {points.length > 1 && (
          <Polyline coordinates={points} strokeColor="#1d4ed8" strokeWidth={4} />
        )}
      </MapView>
      <View style={styles.stats}>
        <Stat label="Distanz" value={formatKm(distanceMeters)} />
        <Stat label="Zeit" value={formatDuration(elapsedMs)} />
        <Stat label="Pace" value={pace} />
      </View>
      <Pressable style={styles.stopButton} onPress={onStop}>
        <Text style={styles.stopText}>Stopp</Text>
      </Pressable>
    </View>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <View style={styles.stat}>
      <Text style={styles.statLabel}>{label}</Text>
      <Text style={styles.statValue}>{value}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center', padding: 24 },
  message: { fontSize: 16, textAlign: 'center' },
  map: { flex: 1 },
  stats: { flexDirection: 'row', justifyContent: 'space-around', paddingVertical: 16 },
  stat: { alignItems: 'center' },
  statLabel: { fontSize: 13, color: '#6b7280' },
  statValue: { fontSize: 22, fontWeight: 'bold' },
  stopButton: {
    backgroundColor: '#dc2626',
    margin: 16,
    borderRadius: 12,
    alignItems: 'center',
    paddingVertical: 16,
  },
  stopText: { color: '#ffffff', fontSize: 20, fontWeight: 'bold' },
});
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `npm test -- app/__tests__/track`
Expected: PASS (2 tests)

- [ ] **Step 6: Manual smoke test in Expo Go**

Run: `npx expo start` — open in Expo Go on a phone, tap "Lauf starten", grant permission, walk a few meters. Verify distance ticks up and the polyline draws. (Stop navigates to a not-yet-existing history route — 404 screen is expected until Task 8.)

- [ ] **Step 7: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/app mobile/package.json mobile/package-lock.json
git commit -m "feat: add live tracking screen with map, stats, and activity saving"
```

---

### Task 8: History List + Detail Screens

Browse saved activities; detail shows the recorded route and stats.

**Files:**
- Create: `mobile/app/history/index.tsx`, `mobile/app/history/[id].tsx`
- Test: `mobile/app/history/__tests__/index.test.tsx`, `mobile/app/history/__tests__/detail.test.tsx`

**Interfaces:**
- Consumes: `listActivities` / `getActivity` / `ActivitySummary` / `Activity` (Task 4), `formatDuration` / `formatKm` / `formatPace` / `paceMinPerKm` (Task 2).
- Produces: routes `/history` and `/history/[id]` (the target of Task 7's `router.replace`).

- [ ] **Step 1: Write the failing list test**

Create `mobile/app/history/__tests__/index.test.tsx`:

```tsx
import React from 'react';
import { render, waitFor } from '@testing-library/react-native';

jest.mock('expo-router', () => {
  const { View } = require('react-native');
  return {
    Link: ({ children }: { children: React.ReactNode }) => <View>{children}</View>,
    useFocusEffect: (callback: () => void) => {
      const { useEffect } = require('react');
      useEffect(callback, []);
    },
  };
});
jest.mock('../../../src/db/activities-repo', () => ({
  listActivities: jest.fn().mockResolvedValue([
    { id: 'a1', sport: 'run', startedAtMs: 1000, durationMs: 1800000, distanceMeters: 5000 },
    { id: 'a2', sport: 'ride', startedAtMs: 500, durationMs: 3600000, distanceMeters: 30000 },
  ]),
}));

import HistoryScreen from '../index';

describe('HistoryScreen', () => {
  it('lists saved activities with sport, distance, and duration', async () => {
    const { getByText } = render(<HistoryScreen />);
    await waitFor(() => expect(getByText('5.00 km')).toBeTruthy());
    expect(getByText('30.00 km')).toBeTruthy();
    expect(getByText('Lauf')).toBeTruthy();
    expect(getByText('Fahrt')).toBeTruthy();
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npm test -- history/__tests__/index`
Expected: FAIL with `Cannot find module '../index'`

- [ ] **Step 3: Implement the list screen**

Create `mobile/app/history/index.tsx`:

```tsx
import { Link, useFocusEffect } from 'expo-router';
import { useCallback, useState } from 'react';
import { FlatList, StyleSheet, Text, View } from 'react-native';
import { ActivitySummary, listActivities } from '../../src/db/activities-repo';
import { formatDuration, formatKm } from '../../src/domain/stats';

const sportLabel = (sport: string): string => (sport === 'ride' ? 'Fahrt' : 'Lauf');

export default function HistoryScreen() {
  const [activities, setActivities] = useState<ActivitySummary[]>([]);

  useFocusEffect(
    useCallback(() => {
      let active = true;
      listActivities().then((items) => {
        if (active) {
          setActivities(items);
        }
      });
      return () => {
        active = false;
      };
    }, []),
  );

  if (activities.length === 0) {
    return (
      <View style={styles.center}>
        <Text style={styles.empty}>Noch keine Aktivitäten aufgezeichnet.</Text>
      </View>
    );
  }

  return (
    <FlatList
      data={activities}
      keyExtractor={(item) => item.id}
      contentContainerStyle={styles.list}
      renderItem={({ item }) => (
        <Link href={{ pathname: '/history/[id]', params: { id: item.id } }}>
          <View style={styles.row}>
            <Text style={styles.sport}>{sportLabel(item.sport)}</Text>
            <Text style={styles.date}>
              {new Date(item.startedAtMs).toLocaleDateString('de-DE')}
            </Text>
            <Text style={styles.distance}>{formatKm(item.distanceMeters)}</Text>
            <Text style={styles.duration}>{formatDuration(item.durationMs)}</Text>
          </View>
        </Link>
      )}
    />
  );
}

const styles = StyleSheet.create({
  center: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  empty: { fontSize: 16, color: '#6b7280' },
  list: { padding: 16, gap: 12 },
  row: {
    backgroundColor: '#f3f4f6',
    borderRadius: 12,
    padding: 16,
    width: '100%',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    gap: 8,
  },
  sport: { fontWeight: 'bold', fontSize: 16 },
  date: { color: '#6b7280' },
  distance: { fontSize: 16, fontWeight: '600' },
  duration: { color: '#374151' },
});
```

- [ ] **Step 4: Run list test to verify it passes**

Run: `npm test -- history/__tests__/index`
Expected: PASS (1 test)

- [ ] **Step 5: Write the failing detail test**

Create `mobile/app/history/__tests__/detail.test.tsx`:

```tsx
import React from 'react';
import { render, waitFor } from '@testing-library/react-native';

jest.mock('react-native-maps', () => {
  const React = require('react');
  const { View } = require('react-native');
  return {
    __esModule: true,
    default: (props: object) => React.createElement(View, { testID: 'map', ...props }),
    Polyline: (props: object) => React.createElement(View, props),
  };
});
jest.mock('expo-router', () => ({
  useLocalSearchParams: () => ({ id: 'a1' }),
}));
jest.mock('../../../src/db/activities-repo', () => ({
  getActivity: jest.fn().mockResolvedValue({
    id: 'a1',
    sport: 'run',
    startedAtMs: 1000,
    endedAtMs: 1801000,
    durationMs: 1800000,
    distanceMeters: 5000,
    points: [
      { latitude: 0, longitude: 0, timestampMs: 1000 },
      { latitude: 0, longitude: 0.01, timestampMs: 2000 },
    ],
  }),
}));

import DetailScreen from '../[id]';

describe('DetailScreen', () => {
  it('shows distance, duration, and pace of the activity', async () => {
    const { getByText } = render(<DetailScreen />);
    await waitFor(() => expect(getByText('5.00 km')).toBeTruthy());
    expect(getByText('30:00')).toBeTruthy();
    expect(getByText('6:00 /km')).toBeTruthy();
  });
});
```

- [ ] **Step 6: Run test to verify it fails**

Run: `npm test -- history/__tests__/detail`
Expected: FAIL with `Cannot find module '../[id]'`

- [ ] **Step 7: Implement the detail screen**

Create `mobile/app/history/[id].tsx`:

```tsx
import { useLocalSearchParams } from 'expo-router';
import { useEffect, useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import MapView, { Polyline } from 'react-native-maps';
import { Activity, getActivity } from '../../src/db/activities-repo';
import { formatDuration, formatKm, formatPace, paceMinPerKm } from '../../src/domain/stats';

export default function DetailScreen() {
  const { id } = useLocalSearchParams<{ id: string }>();
  const [activity, setActivity] = useState<Activity | null>(null);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    let active = true;
    getActivity(String(id)).then((item) => {
      if (active) {
        setActivity(item);
        setLoaded(true);
      }
    });
    return () => {
      active = false;
    };
  }, [id]);

  if (!loaded) {
    return null;
  }
  if (!activity) {
    return (
      <View style={styles.center}>
        <Text>Aktivität nicht gefunden.</Text>
      </View>
    );
  }

  const first = activity.points[0];
  const region = first
    ? { latitude: first.latitude, longitude: first.longitude, latitudeDelta: 0.02, longitudeDelta: 0.02 }
    : { latitude: 48.137, longitude: 11.575, latitudeDelta: 0.02, longitudeDelta: 0.02 };

  return (
    <View style={styles.container}>
      <MapView style={styles.map} initialRegion={region}>
        {activity.points.length > 1 && (
          <Polyline coordinates={activity.points} strokeColor="#1d4ed8" strokeWidth={4} />
        )}
      </MapView>
      <View style={styles.stats}>
        <Stat label="Distanz" value={formatKm(activity.distanceMeters)} />
        <Stat label="Zeit" value={formatDuration(activity.durationMs)} />
        <Stat
          label="Pace"
          value={formatPace(paceMinPerKm(activity.distanceMeters, activity.durationMs))}
        />
      </View>
      {activity.plannedDistanceMeters !== undefined && (
        <Text style={styles.planned}>
          Geplant: {formatKm(activity.plannedDistanceMeters)}
        </Text>
      )}
    </View>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <View style={styles.stat}>
      <Text style={styles.statLabel}>{label}</Text>
      <Text style={styles.statValue}>{value}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  map: { flex: 1 },
  stats: { flexDirection: 'row', justifyContent: 'space-around', paddingVertical: 16 },
  stat: { alignItems: 'center' },
  statLabel: { fontSize: 13, color: '#6b7280' },
  statValue: { fontSize: 22, fontWeight: 'bold' },
  planned: { textAlign: 'center', color: '#6b7280', paddingBottom: 16 },
});
```

- [ ] **Step 8: Run all tests to verify they pass**

Run: `npm test`
Expected: PASS (all suites)

- [ ] **Step 9: Manual verification**

Run: `npx expo start` — record a short activity via "Lauf starten" → "Stopp"; verify you land on the detail page and the activity appears under "Verlauf".

- [ ] **Step 10: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/app
git commit -m "feat: add activity history list and detail screens"
```

---

### Task 9: Routing Service (OpenRouteService)

Turns 2+ map waypoints into a real route with total distance, using the ORS directions API (GeoJSON response — no polyline decoding needed). Profiles: `foot-walking` for runs, `cycling-regular` for rides.

**Files:**
- Create: `mobile/src/services/routing.ts`, `mobile/.env.example`
- Test: `mobile/src/services/__tests__/routing.test.ts`
- Modify: `mobile/.gitignore` (add `.env`)

**Interfaces:**
- Consumes: `GeoPoint` (Task 1).
- Produces:
  - `type RoutingProfile = 'foot-walking' | 'cycling-regular'`
  - `interface PlannedRoute { coordinates: GeoPoint[]; distanceMeters: number }`
  - `class RoutingError extends Error`
  - `fetchRoute(waypoints: readonly GeoPoint[], profile: RoutingProfile, apiKey: string): Promise<PlannedRoute>`

- [ ] **Step 1: Add env file scaffolding**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike/mobile"
printf 'EXPO_PUBLIC_ORS_API_KEY=your-openrouteservice-api-key\n' > .env.example
printf '\n.env\n' >> .gitignore
```

(A free API key: sign up at https://openrouteservice.org, create `.env` from `.env.example` locally.)

- [ ] **Step 2: Write the failing routing test**

Create `mobile/src/services/__tests__/routing.test.ts`:

```ts
import { fetchRoute, RoutingError } from '../routing';

const waypoints = [
  { latitude: 48.1, longitude: 11.5 },
  { latitude: 48.11, longitude: 11.52 },
];

const orsResponse = {
  features: [
    {
      geometry: {
        coordinates: [
          [11.5, 48.1],
          [11.51, 48.105],
          [11.52, 48.11],
        ],
      },
      properties: { summary: { distance: 2345.6 } },
    },
  ],
};

describe('fetchRoute', () => {
  afterEach(() => {
    jest.restoreAllMocks();
  });

  it('posts waypoints as lng/lat and maps the GeoJSON response', async () => {
    const fetchMock = jest.fn().mockResolvedValue({
      ok: true,
      json: async () => orsResponse,
    });
    global.fetch = fetchMock as never;

    const route = await fetchRoute(waypoints, 'foot-walking', 'key-123');

    expect(fetchMock).toHaveBeenCalledWith(
      'https://api.openrouteservice.org/v2/directions/foot-walking/geojson',
      expect.objectContaining({
        method: 'POST',
        headers: expect.objectContaining({ Authorization: 'key-123' }),
        body: JSON.stringify({ coordinates: [[11.5, 48.1], [11.52, 48.11]] }),
      }),
    );
    expect(route.distanceMeters).toBeCloseTo(2345.6, 3);
    expect(route.coordinates[0]).toEqual({ latitude: 48.1, longitude: 11.5 });
    expect(route.coordinates).toHaveLength(3);
  });

  it('rejects with fewer than 2 waypoints', async () => {
    await expect(fetchRoute([waypoints[0]], 'foot-walking', 'k')).rejects.toBeInstanceOf(
      RoutingError,
    );
  });

  it('throws RoutingError on a non-ok response', async () => {
    global.fetch = jest.fn().mockResolvedValue({ ok: false, status: 403 }) as never;
    await expect(fetchRoute(waypoints, 'cycling-regular', 'bad')).rejects.toThrow(
      'HTTP 403',
    );
  });

  it('throws RoutingError when the response has no route', async () => {
    global.fetch = jest
      .fn()
      .mockResolvedValue({ ok: true, json: async () => ({ features: [] }) }) as never;
    await expect(fetchRoute(waypoints, 'foot-walking', 'k')).rejects.toBeInstanceOf(
      RoutingError,
    );
  });
});
```

- [ ] **Step 3: Run test to verify it fails**

Run: `npm test -- routing`
Expected: FAIL with `Cannot find module '../routing'`

- [ ] **Step 4: Implement the routing service**

Create `mobile/src/services/routing.ts`:

```ts
import { GeoPoint } from '../domain/geo';

export type RoutingProfile = 'foot-walking' | 'cycling-regular';

export interface PlannedRoute {
  coordinates: GeoPoint[];
  distanceMeters: number;
}

export class RoutingError extends Error {}

const BASE_URL = 'https://api.openrouteservice.org/v2/directions';

export async function fetchRoute(
  waypoints: readonly GeoPoint[],
  profile: RoutingProfile,
  apiKey: string,
): Promise<PlannedRoute> {
  if (waypoints.length < 2) {
    throw new RoutingError('Mindestens 2 Wegpunkte erforderlich.');
  }
  const response = await fetch(`${BASE_URL}/${profile}/geojson`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: apiKey,
    },
    body: JSON.stringify({
      coordinates: waypoints.map((point) => [point.longitude, point.latitude]),
    }),
  });
  if (!response.ok) {
    throw new RoutingError(`Routenberechnung fehlgeschlagen: HTTP ${response.status}`);
  }
  const data = (await response.json()) as {
    features?: Array<{
      geometry: { coordinates: [number, number][] };
      properties: { summary: { distance: number } };
    }>;
  };
  const feature = data.features?.[0];
  if (!feature) {
    throw new RoutingError('Die Antwort enthielt keine Route.');
  }
  return {
    coordinates: feature.geometry.coordinates.map(([longitude, latitude]) => ({
      latitude,
      longitude,
    })),
    distanceMeters: feature.properties.summary.distance,
  };
}
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `npm test -- routing`
Expected: PASS (4 tests)

- [ ] **Step 6: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/src/services mobile/.env.example mobile/.gitignore
git commit -m "feat: add OpenRouteService routing client"
```

---

### Task 10: Planned-Route Store

Small zustand store carrying the plan (computed route or bare distance goal) from the plan screen into the tracking screen.

**Files:**
- Create: `mobile/src/state/planned-route-store.ts`
- Test: `mobile/src/state/__tests__/planned-route-store.test.ts`

**Interfaces:**
- Consumes: `PlannedRoute` (Task 9).
- Produces:
  - `usePlannedRouteStore` with state `{ route: PlannedRoute | null; distanceGoalMeters: number | null }` and actions `setRoute(route: PlannedRoute | null): void`, `setDistanceGoal(meters: number | null): void`, `clear(): void`
  - `selectPlannedDistanceMeters(state): number | null` — route distance wins over bare goal

- [ ] **Step 1: Write the failing store test**

Create `mobile/src/state/__tests__/planned-route-store.test.ts`:

```ts
import {
  selectPlannedDistanceMeters,
  usePlannedRouteStore,
} from '../planned-route-store';

beforeEach(() => {
  usePlannedRouteStore.getState().clear();
});

describe('planned route store', () => {
  it('is empty after clear', () => {
    const state = usePlannedRouteStore.getState();
    expect(state.route).toBeNull();
    expect(state.distanceGoalMeters).toBeNull();
    expect(selectPlannedDistanceMeters(state)).toBeNull();
  });

  it('uses the distance goal when no route is set', () => {
    usePlannedRouteStore.getState().setDistanceGoal(10000);
    expect(selectPlannedDistanceMeters(usePlannedRouteStore.getState())).toBe(10000);
  });

  it('prefers the computed route distance over the goal', () => {
    usePlannedRouteStore.getState().setDistanceGoal(10000);
    usePlannedRouteStore.getState().setRoute({ coordinates: [], distanceMeters: 12800 });
    expect(selectPlannedDistanceMeters(usePlannedRouteStore.getState())).toBe(12800);
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npm test -- planned-route-store`
Expected: FAIL with `Cannot find module '../planned-route-store'`

- [ ] **Step 3: Implement the store**

Create `mobile/src/state/planned-route-store.ts`:

```ts
import { create } from 'zustand';
import { PlannedRoute } from '../services/routing';

interface PlannedRouteState {
  route: PlannedRoute | null;
  distanceGoalMeters: number | null;
  setRoute: (route: PlannedRoute | null) => void;
  setDistanceGoal: (meters: number | null) => void;
  clear: () => void;
}

export const usePlannedRouteStore = create<PlannedRouteState>((set) => ({
  route: null,
  distanceGoalMeters: null,
  setRoute: (route) => set({ route }),
  setDistanceGoal: (distanceGoalMeters) => set({ distanceGoalMeters }),
  clear: () => set({ route: null, distanceGoalMeters: null }),
}));

export function selectPlannedDistanceMeters(state: {
  route: PlannedRoute | null;
  distanceGoalMeters: number | null;
}): number | null {
  return state.route?.distanceMeters ?? state.distanceGoalMeters;
}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `npm test -- planned-route-store`
Expected: PASS (3 tests)

- [ ] **Step 5: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/src/state
git commit -m "feat: add planned route store"
```

---

### Task 11: Route Planning Screen (Modus B entry)

Tap waypoints on the map → "Route berechnen" calls the routing service and shows the total distance — or type a bare distance goal. "Start" hands the plan to the tracking screen.

**Files:**
- Create: `mobile/app/plan.tsx`
- Test: `mobile/app/__tests__/plan.test.tsx`

**Interfaces:**
- Consumes: `fetchRoute` / `RoutingProfile` / `PlannedRoute` (Task 9), `usePlannedRouteStore` (Task 10), `formatKm` (Task 2), `Sport` (Task 3), env var `EXPO_PUBLIC_ORS_API_KEY`.
- Produces: route `/plan`; on Start navigates to `/track` with `sport` param, with the plan stored in `usePlannedRouteStore`.

- [ ] **Step 1: Write the failing screen test**

Create `mobile/app/__tests__/plan.test.tsx`:

```tsx
import React from 'react';
import { fireEvent, render, waitFor } from '@testing-library/react-native';

jest.mock('react-native-maps', () => {
  const React = require('react');
  const { View } = require('react-native');
  return {
    __esModule: true,
    default: (props: object) => React.createElement(View, { testID: 'map', ...props }),
    Marker: (props: object) => React.createElement(View, props),
    Polyline: (props: object) => React.createElement(View, props),
  };
});
jest.mock('expo-router', () => ({
  router: { push: jest.fn() },
}));
jest.mock('../../src/services/routing', () => ({
  fetchRoute: jest.fn().mockResolvedValue({
    coordinates: [
      { latitude: 48.1, longitude: 11.5 },
      { latitude: 48.11, longitude: 11.52 },
    ],
    distanceMeters: 5000,
  }),
  RoutingError: class RoutingError extends Error {},
}));

import { router } from 'expo-router';
import PlanScreen from '../plan';
import { fetchRoute } from '../../src/services/routing';
import {
  selectPlannedDistanceMeters,
  usePlannedRouteStore,
} from '../../src/state/planned-route-store';

beforeEach(() => {
  jest.clearAllMocks();
  usePlannedRouteStore.getState().clear();
  process.env.EXPO_PUBLIC_ORS_API_KEY = 'test-key';
});

const tapMap = (map: unknown, latitude: number, longitude: number) => {
  fireEvent(map as never, 'press', { nativeEvent: { coordinate: { latitude, longitude } } });
};

describe('PlanScreen', () => {
  it('computes a route from two tapped waypoints and shows its distance', async () => {
    const { getByTestId, getByText } = render(<PlanScreen />);
    tapMap(getByTestId('map'), 48.1, 11.5);
    tapMap(getByTestId('map'), 48.11, 11.52);

    fireEvent.press(getByText('Route berechnen'));

    await waitFor(() => expect(getByText('Geplante Strecke: 5.00 km')).toBeTruthy());
    expect(fetchRoute).toHaveBeenCalledWith(
      [
        { latitude: 48.1, longitude: 11.5 },
        { latitude: 48.11, longitude: 11.52 },
      ],
      'foot-walking',
      'test-key',
    );
  });

  it('starts with the computed route in the planned-route store', async () => {
    const { getByTestId, getByText } = render(<PlanScreen />);
    tapMap(getByTestId('map'), 48.1, 11.5);
    tapMap(getByTestId('map'), 48.11, 11.52);
    fireEvent.press(getByText('Route berechnen'));
    await waitFor(() => expect(getByText('Geplante Strecke: 5.00 km')).toBeTruthy());

    fireEvent.press(getByText('Start'));

    expect(selectPlannedDistanceMeters(usePlannedRouteStore.getState())).toBe(5000);
    expect(router.push).toHaveBeenCalledWith({
      pathname: '/track',
      params: { sport: 'run' },
    });
  });

  it('starts with a bare distance goal', () => {
    const { getByPlaceholderText, getByText } = render(<PlanScreen />);
    fireEvent.changeText(getByPlaceholderText('Ziel in km'), '10');

    fireEvent.press(getByText('Start'));

    expect(selectPlannedDistanceMeters(usePlannedRouteStore.getState())).toBe(10000);
    expect(router.push).toHaveBeenCalled();
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npm test -- app/__tests__/plan`
Expected: FAIL with `Cannot find module '../plan'`

- [ ] **Step 3: Implement the plan screen**

Create `mobile/app/plan.tsx`:

```tsx
import { router } from 'expo-router';
import { useState } from 'react';
import { Pressable, StyleSheet, Text, TextInput, View } from 'react-native';
import MapView, { Marker, Polyline } from 'react-native-maps';
import { GeoPoint } from '../src/domain/geo';
import { formatKm } from '../src/domain/stats';
import { fetchRoute, PlannedRoute, RoutingProfile } from '../src/services/routing';
import { usePlannedRouteStore } from '../src/state/planned-route-store';
import { Sport } from '../src/state/tracking-store';

const DEFAULT_REGION = {
  latitude: 48.137,
  longitude: 11.575,
  latitudeDelta: 0.05,
  longitudeDelta: 0.05,
};

const profileForSport = (sport: Sport): RoutingProfile =>
  sport === 'ride' ? 'cycling-regular' : 'foot-walking';

export default function PlanScreen() {
  const [sport, setSport] = useState<Sport>('run');
  const [waypoints, setWaypoints] = useState<GeoPoint[]>([]);
  const [route, setRoute] = useState<PlannedRoute | null>(null);
  const [goalKmText, setGoalKmText] = useState('');
  const [error, setError] = useState<string | null>(null);

  const addWaypoint = (coordinate: GeoPoint) => {
    setWaypoints((current) => [...current, coordinate]);
    setRoute(null);
  };

  const onComputeRoute = async () => {
    const apiKey = process.env.EXPO_PUBLIC_ORS_API_KEY;
    if (!apiKey) {
      setError('Kein API-Key konfiguriert (EXPO_PUBLIC_ORS_API_KEY).');
      return;
    }
    setError(null);
    try {
      setRoute(await fetchRoute(waypoints, profileForSport(sport), apiKey));
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : 'Routenberechnung fehlgeschlagen.');
    }
  };

  const onStart = () => {
    const store = usePlannedRouteStore.getState();
    store.clear();
    if (route) {
      store.setRoute(route);
    } else {
      const goalKm = Number(goalKmText.replace(',', '.'));
      if (Number.isFinite(goalKm) && goalKm > 0) {
        store.setDistanceGoal(Math.round(goalKm * 1000));
      }
    }
    router.push({ pathname: '/track', params: { sport } });
  };

  return (
    <View style={styles.container}>
      <MapView
        style={styles.map}
        initialRegion={DEFAULT_REGION}
        onPress={(event) => addWaypoint(event.nativeEvent.coordinate)}
      >
        {waypoints.map((point, index) => (
          <Marker key={`${point.latitude}-${point.longitude}-${index}`} coordinate={point} />
        ))}
        {route && (
          <Polyline coordinates={route.coordinates} strokeColor="#1d4ed8" strokeWidth={4} />
        )}
      </MapView>

      <View style={styles.panel}>
        <View style={styles.row}>
          <Toggle label="Lauf" active={sport === 'run'} onPress={() => setSport('run')} />
          <Toggle label="Fahrt" active={sport === 'ride'} onPress={() => setSport('ride')} />
        </View>

        <Pressable
          style={[styles.secondaryButton, waypoints.length < 2 && styles.disabled]}
          disabled={waypoints.length < 2}
          onPress={onComputeRoute}
        >
          <Text style={styles.secondaryText}>Route berechnen</Text>
        </Pressable>

        {route && (
          <Text style={styles.distance}>Geplante Strecke: {formatKm(route.distanceMeters)}</Text>
        )}
        {error && <Text style={styles.error}>{error}</Text>}

        <TextInput
          style={styles.input}
          placeholder="Ziel in km"
          keyboardType="numeric"
          value={goalKmText}
          onChangeText={setGoalKmText}
        />

        <Pressable style={styles.startButton} onPress={onStart}>
          <Text style={styles.startText}>Start</Text>
        </Pressable>
      </View>
    </View>
  );
}

function Toggle({
  label,
  active,
  onPress,
}: {
  label: string;
  active: boolean;
  onPress: () => void;
}) {
  return (
    <Pressable style={[styles.toggle, active && styles.toggleActive]} onPress={onPress}>
      <Text style={active ? styles.toggleTextActive : styles.toggleText}>{label}</Text>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  map: { flex: 1 },
  panel: { padding: 16, gap: 12 },
  row: { flexDirection: 'row', gap: 8 },
  toggle: {
    flex: 1,
    borderWidth: 1,
    borderColor: '#1d4ed8',
    borderRadius: 8,
    alignItems: 'center',
    paddingVertical: 10,
  },
  toggleActive: { backgroundColor: '#1d4ed8' },
  toggleText: { color: '#1d4ed8', fontWeight: '600' },
  toggleTextActive: { color: '#ffffff', fontWeight: '600' },
  secondaryButton: {
    borderWidth: 1,
    borderColor: '#1d4ed8',
    borderRadius: 8,
    alignItems: 'center',
    paddingVertical: 12,
  },
  secondaryText: { color: '#1d4ed8', fontWeight: '600', fontSize: 16 },
  disabled: { opacity: 0.4 },
  distance: { fontSize: 16, fontWeight: '600', textAlign: 'center' },
  error: { color: '#dc2626', textAlign: 'center' },
  input: {
    borderWidth: 1,
    borderColor: '#d1d5db',
    borderRadius: 8,
    paddingHorizontal: 12,
    paddingVertical: 10,
    fontSize: 16,
  },
  startButton: {
    backgroundColor: '#16a34a',
    borderRadius: 12,
    alignItems: 'center',
    paddingVertical: 16,
  },
  startText: { color: '#ffffff', fontSize: 20, fontWeight: 'bold' },
});
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `npm test -- app/__tests__/plan`
Expected: PASS (3 tests)

- [ ] **Step 5: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/app
git commit -m "feat: add route planning screen with waypoints and distance goal"
```

---

### Task 12: Planned Mode on the Tracking Screen (Modus B complete)

Extends the tracking screen: show the planned route as a gray polyline, display "Verbleibend" (remaining km) when a plan exists, persist `plannedDistanceMeters` with the saved activity, and clear the plan afterwards.

**Files:**
- Modify: `mobile/app/track.tsx` (from Task 7 — full replacement shown below)
- Test: `mobile/app/__tests__/track.test.tsx` (add planned-mode cases)

**Interfaces:**
- Consumes: `usePlannedRouteStore` / `selectPlannedDistanceMeters` (Task 10), `remainingDistanceMeters` (Task 2). All Task 7 interfaces unchanged.
- Produces: saved `Activity` now carries `plannedDistanceMeters` when a plan was active.

- [ ] **Step 1: Add failing planned-mode tests**

Append to the `describe('TrackScreen', …)` block in `mobile/app/__tests__/track.test.tsx` (imports at top of file additionally need `usePlannedRouteStore`):

```tsx
import { usePlannedRouteStore } from '../../src/state/planned-route-store';
```

And extend `beforeEach` with `usePlannedRouteStore.getState().clear();`. Then add:

```tsx
  it('shows the remaining distance when a plan exists', async () => {
    usePlannedRouteStore.getState().setDistanceGoal(10000);
    const { getByText } = render(<TrackScreen />);
    await waitFor(() => expect(useTrackingStore.getState().status).toBe('tracking'));

    useTrackingStore.getState().addPoint({ latitude: 0, longitude: 0, timestampMs: 1000 });
    useTrackingStore.getState().addPoint({ latitude: 0, longitude: 0.01, timestampMs: 2000 });

    await waitFor(() => expect(getByText('Verbleibend')).toBeTruthy());
    expect(getByText('8.89 km')).toBeTruthy();
  });

  it('saves the planned distance with the activity and clears the plan', async () => {
    usePlannedRouteStore.getState().setDistanceGoal(10000);
    const { getByText } = render(<TrackScreen />);
    await waitFor(() => expect(useTrackingStore.getState().status).toBe('tracking'));

    fireEvent.press(getByText('Stopp'));

    await waitFor(() => expect(saveActivity).toHaveBeenCalledTimes(1));
    const saved = (saveActivity as jest.Mock).mock.calls[0][0];
    expect(saved.plannedDistanceMeters).toBe(10000);
    expect(usePlannedRouteStore.getState().distanceGoalMeters).toBeNull();
  });
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npm test -- app/__tests__/track`
Expected: FAIL — `Unable to find an element with text: Verbleibend` (2 new tests fail, 2 old tests pass)

- [ ] **Step 3: Extend the tracking screen**

Replace the entire content of `mobile/app/track.tsx` with:

```tsx
import * as Crypto from 'expo-crypto';
import { useKeepAwake } from 'expo-keep-awake';
import { router, useLocalSearchParams } from 'expo-router';
import { useEffect, useState } from 'react';
import { Pressable, StyleSheet, Text, View } from 'react-native';
import MapView, { Polyline } from 'react-native-maps';
import { remainingDistanceMeters } from '../src/domain/route-progress';
import { formatDuration, formatKm, formatPace, paceMinPerKm } from '../src/domain/stats';
import { saveActivity } from '../src/db/activities-repo';
import { requestLocationPermission, watchLocation } from '../src/services/location';
import {
  selectPlannedDistanceMeters,
  usePlannedRouteStore,
} from '../src/state/planned-route-store';
import { Sport, useTrackingStore } from '../src/state/tracking-store';

const DEFAULT_REGION = {
  latitude: 48.137,
  longitude: 11.575,
  latitudeDelta: 0.02,
  longitudeDelta: 0.02,
};

export default function TrackScreen() {
  useKeepAwake();
  const params = useLocalSearchParams<{ sport?: string }>();
  const sport: Sport = params.sport === 'ride' ? 'ride' : 'run';

  const status = useTrackingStore((state) => state.status);
  const points = useTrackingStore((state) => state.points);
  const distanceMeters = useTrackingStore((state) => state.distanceMeters);
  const startedAtMs = useTrackingStore((state) => state.startedAtMs);
  const plannedRoute = usePlannedRouteStore((state) => state.route);
  const plannedMeters = usePlannedRouteStore(selectPlannedDistanceMeters);

  const [permissionDenied, setPermissionDenied] = useState(false);
  const [nowMs, setNowMs] = useState(() => Date.now());

  useEffect(() => {
    let unsubscribe: (() => void) | null = null;
    let cancelled = false;
    (async () => {
      const granted = await requestLocationPermission();
      if (cancelled) {
        return;
      }
      if (!granted) {
        setPermissionDenied(true);
        return;
      }
      useTrackingStore.getState().start(sport, Date.now());
      unsubscribe = await watchLocation((point) => {
        useTrackingStore.getState().addPoint(point);
      });
    })();
    return () => {
      cancelled = true;
      if (unsubscribe) {
        unsubscribe();
      }
    };
  }, [sport]);

  useEffect(() => {
    const timer = setInterval(() => setNowMs(Date.now()), 1000);
    return () => clearInterval(timer);
  }, []);

  const onStop = async () => {
    const completed = useTrackingStore.getState().stop(Date.now());
    if (!completed) {
      return;
    }
    const id = Crypto.randomUUID();
    await saveActivity({
      id,
      ...completed,
      ...(plannedMeters !== null ? { plannedDistanceMeters: plannedMeters } : {}),
    });
    usePlannedRouteStore.getState().clear();
    router.replace(`/history/${id}`);
  };

  if (permissionDenied) {
    return (
      <View style={styles.center}>
        <Text style={styles.message}>
          Ohne Standortberechtigung kann keine Aktivität aufgezeichnet werden.
        </Text>
      </View>
    );
  }

  const elapsedMs = status === 'tracking' && startedAtMs !== null ? nowMs - startedAtMs : 0;
  const pace = formatPace(paceMinPerKm(distanceMeters, elapsedMs));

  return (
    <View style={styles.container}>
      <MapView style={styles.map} initialRegion={DEFAULT_REGION} showsUserLocation>
        {plannedRoute && plannedRoute.coordinates.length > 1 && (
          <Polyline
            coordinates={plannedRoute.coordinates}
            strokeColor="#9ca3af"
            strokeWidth={4}
          />
        )}
        {points.length > 1 && (
          <Polyline coordinates={points} strokeColor="#1d4ed8" strokeWidth={4} />
        )}
      </MapView>
      <View style={styles.stats}>
        <Stat label="Distanz" value={formatKm(distanceMeters)} />
        <Stat label="Zeit" value={formatDuration(elapsedMs)} />
        <Stat label="Pace" value={pace} />
        {plannedMeters !== null && (
          <Stat
            label="Verbleibend"
            value={formatKm(remainingDistanceMeters(plannedMeters, distanceMeters))}
          />
        )}
      </View>
      <Pressable style={styles.stopButton} onPress={onStop}>
        <Text style={styles.stopText}>Stopp</Text>
      </Pressable>
    </View>
  );
}

function Stat({ label, value }: { label: string; value: string }) {
  return (
    <View style={styles.stat}>
      <Text style={styles.statLabel}>{label}</Text>
      <Text style={styles.statValue}>{value}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center', padding: 24 },
  message: { fontSize: 16, textAlign: 'center' },
  map: { flex: 1 },
  stats: { flexDirection: 'row', justifyContent: 'space-around', paddingVertical: 16 },
  stat: { alignItems: 'center' },
  statLabel: { fontSize: 13, color: '#6b7280' },
  statValue: { fontSize: 22, fontWeight: 'bold' },
  stopButton: {
    backgroundColor: '#dc2626',
    margin: 16,
    borderRadius: 12,
    alignItems: 'center',
    paddingVertical: 16,
  },
  stopText: { color: '#ffffff', fontSize: 20, fontWeight: 'bold' },
});
```

- [ ] **Step 4: Run all tests to verify they pass**

Run: `npm test`
Expected: PASS (all suites, including 4 track-screen tests)

- [ ] **Step 5: Full manual verification (Modus A + B)**

Run: `npx expo start`, on a phone with a `.env` containing a real ORS key:
1. Modus A: Home → "Lauf starten" → move → distance/pace update → "Stopp" → detail page → entry in "Verlauf".
2. Modus B: Home → "Route planen" → tap 2+ points → "Route berechnen" → "Geplante Strecke: X km" appears → "Start" → gray planned line + "Verbleibend" stat → "Stopp" → detail shows "Geplant: X km".

- [ ] **Step 6: Commit**

```bash
cd "/Users/vincentschnetzer/Documents/Run&Bike"
git add mobile/app
git commit -m "feat: show planned route and remaining distance during tracking"
```

---

## Deferred to Later Plans

- **Plan 2 (candidates):** background GPS tracking (expo-task-manager + dev build), pause/resume, off-route detection, finger-sketch route interpretation (concept §4), audio announcements (§5).
- **Plan 3+:** accounts + backend, profiles (§9), follow system (§10), route sharing (§21–25), teams (§14–19), rankings (§13), challenges (§27–28), territory (§20), health/recovery analysis (§7–8), wearables (§32).
