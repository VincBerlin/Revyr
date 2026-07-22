"""spikes/p0-02/test_track_point_v1.py — T1..T6 nach Detailplan §2.3.

Aufruf: python3 -m unittest test_track_point_v1.py
"""
import json
import unittest
from pathlib import Path

SOURCE_VALUES = ('foreground', 'background', 'wearable', 'import')
QUALITY_VALUES = ('raw', 'accepted', 'low-confidence', 'rejected')


def make_full_point():
    return {'latitude': -33.9249, 'longitude': 18.4241, 'timestampMs': 1_729_000_000_000,
            'accuracyMeters': 4.2, 'altitudeMeters': -1.5, 'speedMps': 3.14,
            'headingDegrees': 359.9, 'source': 'foreground', 'isMocked': False,
            'quality': 'accepted'}


def make_null_point():
    return {'latitude': 0.0, 'longitude': 0.0, 'timestampMs': 0, 'accuracyMeters': None,
            'altitudeMeters': None, 'speedMps': None, 'headingDegrees': None,
            'source': 'foreground', 'isMocked': None, 'quality': 'raw'}


class TestTrackPointV1Serialisierung(unittest.TestCase):
    def setUp(self):
        from track_point_v1 import serialize, deserialize
        self.serialize = serialize
        self.deserialize = deserialize

    def test_T1_alle_null_felder_ueberleben_roundtrip(self):
        p = make_null_point()
        self.assertEqual(p, self.deserialize(self.serialize(p)))

    def test_T2_alle_felder_belegt_inkl_negativ(self):
        p = make_full_point()
        r = self.deserialize(self.serialize(p))
        self.assertEqual(p, r)
        self.assertLess(r['latitude'], 0.0)
        self.assertLess(r['altitudeMeters'], 0.0)

    def test_T3_jeder_source_und_jeder_quality_einzeln(self):
        base = make_full_point()
        for src in SOURCE_VALUES:
            for q in QUALITY_VALUES:
                p = dict(base); p['source'] = src; p['quality'] = q
                r = self.deserialize(self.serialize(p))
                self.assertEqual(p['source'], r['source'])
                self.assertEqual(p['quality'], r['quality'])

    def test_T4_isMocked_null_und_false_bleiben_unterscheidbar(self):
        p_null = dict(make_full_point()); p_null['isMocked'] = None
        p_false = dict(make_full_point()); p_false['isMocked'] = False
        r_null = self.deserialize(self.serialize(p_null))
        r_false = self.deserialize(self.serialize(p_false))
        self.assertIsNone(r_null['isMocked'])
        self.assertIs(r_false['isMocked'], False)
        self.assertNotEqual(r_null['isMocked'], r_false['isMocked'])

    def test_T5_real_recording_roundtrip(self):
        fixture = Path(__file__).parent / 'fixtures' / 'real_recording.jsonl'
        if not fixture.exists():
            self.skipTest("T5 uebersprungen: OQ-003 MISSING; keine reale Aufzeichnung.")
        with fixture.open() as f:
            for line in f:
                if line.strip():
                    p = json.loads(line)
                    self.assertEqual(p, self.deserialize(self.serialize(p)))

    def test_T6_unbekannter_source_oder_quality_fuehrt_zu_kontrolliertem_ergebnis(self):
        from track_point_v1 import DeserialiseError
        bad_src = dict(make_full_point()); bad_src['source'] = 'dogsled'
        with self.assertRaises(DeserialiseError):
            self.deserialize(self.serialize(bad_src))
        bad_q = dict(make_full_point()); bad_q['quality'] = 'gold'
        with self.assertRaises(DeserialiseError):
            self.deserialize(self.serialize(bad_q))


if __name__ == '__main__':
    unittest.main()
