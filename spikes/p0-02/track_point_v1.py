"""spikes/p0-02/track_point_v1.py — Wegwerf-Umsetzung.

Kein Produktionscode. Kleinstmoegliche Struktur, um T1..T4 zu bestehen und T6 zu sichern.
Details: spikes/p0-02/README.md.
"""
import json

ALLOWED_SOURCE = ('foreground', 'background', 'wearable', 'import')
ALLOWED_QUALITY = ('raw', 'accepted', 'low-confidence', 'rejected')


class DeserialiseError(ValueError):
    """Kontrollierte Fehlermeldung fuer unbekannte Enum-Werte (kein stiller Default)."""


def serialize(point: dict) -> str:
    return json.dumps(point, sort_keys=True, allow_nan=False)


def deserialize(payload: str) -> dict:
    point = json.loads(payload)
    if point.get('source') not in ALLOWED_SOURCE:
        raise DeserialiseError(f"source '{point.get('source')}' nicht in {ALLOWED_SOURCE}")
    if point.get('quality') not in ALLOWED_QUALITY:
        raise DeserialiseError(f"quality '{point.get('quality')}' nicht in {ALLOWED_QUALITY}")
    return point
