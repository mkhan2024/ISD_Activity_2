"""
Description: Unit tests for the Aircrat class.
Author: Apurba Khan
Date: 2024.09.27
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_aircraft.py
"""

import unittest
from vehicle.aircraft import Aircraft

class TestAircraft(unittest.TestCase):

    def test_init_valid(self):
        """ Test case 1: for Aircraft with name mangling """
        aircraft = Aircraft("KAI", "KF-21", 30.0, 1500.0)
        self.assertEqual(aircraft._Vehicle__make, "KAI")
        self.assertEqual(aircraft._Vehicle__model, "KF-21")
        self.assertEqual(aircraft._Aircraft__fuel_burn_rate, 30.0)
        self.assertEqual(aircraft._Aircraft__speed, 1500.0)

    def test_init_blank_make(self):
        """ Test case 2: for blank make (" ") """
        with self.assertRaises(ValueError):
            aircraft = Aircraft(" ", "KF-21", 30.0, 1500.0)

    def test_init_blank_model(self):
        """ Test case 3: for blank model (" ") """
        with self.assertRaises(ValueError):
            aircraft = Aircraft("KAI", " ", 30.0, 1500.0)

    def test_init_none_numeric_fuel_burn_rate(self):
        """ Test case 4: for none-numeric fuel burn rate (None) """
        with self.assertRaises(ValueError):
            aircraft = Aircraft("KAI", "KF-21", None, 1500.0)

    def test_init_none_numeric_speed(self):
        """ Test case 5: for none-numeric speed (None) """
        with self.assertRaises(ValueError):
            aircraft = Aircraft("KAI", "KF-21", 30.0, None)

    def test_str_method_format(self):
        """ Test case 6: for correct string format """
        aircraft = Aircraft("KAI", "KF-21", 30.0, 1500.0)
        expected_str = (
            "Make: KAI\nModel: KF-21\n"
            "This aircraft has a fuel burn rate of 30.0 litres/hour, and a cruising speed of 1500.0 km/hour."
        )
        self.assertEqual(str(aircraft), expected_str)

    def test_calculate_fuel_requirements_correct(self):
        """ Test case 7: for correct fuel """
        aircraft = Aircraft("KAI", "KF-21", 30.0, 1500.0)
        expected_fuel = (2500.0 / 1500.0) * 30.0 
        self.assertAlmostEqual(aircraft.calculate_fuel_requirements(2500.0), expected_fuel)
