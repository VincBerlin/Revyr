// mobile/src/services/quality/geo.ts
//
// Kleine Geo-Helper. Kein Framework, keine Zusatzdependency.

export interface LatLng {
  readonly latitude: number;
  readonly longitude: number;
}

const EARTH_RADIUS_M = 6_371_000;

function toRad(deg: number): number {
  return (deg * Math.PI) / 180;
}

// Grosskreisentfernung nach Haversine-Formel. Fuer Sport-Distanzen im Kilometer-
// bereich vollkommen ausreichend; keine Ellipsoid-Korrektur noetig (Fehler < 0,5 %).
export function haversineDistanceM(a: LatLng, b: LatLng): number {
  const dLat = toRad(b.latitude - a.latitude);
  const dLng = toRad(b.longitude - a.longitude);
  const lat1 = toRad(a.latitude);
  const lat2 = toRad(b.latitude);
  const h =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLng / 2) ** 2;
  return 2 * EARTH_RADIUS_M * Math.asin(Math.min(1, Math.sqrt(h)));
}
