import unittest
from python.gate_of_ishtar import calculate_champion_health


class GateOfIshtarTest(unittest.TestCase):

    def test_invalid_champion(self):
        with self.assertRaises(ValueError):
            calculate_champion_health('hobbit', ['2018-10-10 14:30', '2018-10-10 16:30'])

    def test_holly_day(self):
        self.assertEqual(calculate_champion_health('human', ['2018-10-11 14:30', '2018-10-11 16:30']), 100)

    def test_calc_one_hour(self):
        self.assertEqual(calculate_champion_health('vampire', ['2018-10-08 11:30', '2018-10-08 12:30']), 103)

    def test_calc_multiple_hours(self):
        self.assertEqual(calculate_champion_health('giant', ['2018-10-08 06:00', '2018-10-08 09:30']), 100)
