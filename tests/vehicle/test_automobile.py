"""
Description: Unit tests for the Automobile class.
Author: Apurba Khan
Date: 2024.09.27
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_automobile.py
"""

import unittest
from vehicle.automobile import Automobile
class TestAutomobile(unittest.TestCase):

    def test_init_valid(self):
        """ Test case 1: for Automobile with name mangling """
        automobile = Automobile("Genesis", "G90", 9.0)
        self.assertEqual(automobile._Vehicle__make, "Genesis")
        self.assertEqual(automobile._Vehicle__model, "G90")
        self.assertEqual(automobile._Automobile__kilometers_per_litre, 9.0)

    def test_init_blank_make(self):
        """ Test case 2: for blank make (" ") """
        with self.assertRaises(ValueError):
            automobile = Automobile(" ", "G90", 9.0)

    def test_init_blank_model(self):
        """ Test case 3: for blank model (" ") """
        with self.assertRaises(ValueError):
            automobile = Automobile("Genesis", " ", 9.0)

    def test_init_none_numeric_kilometers_per_litre(self):
        """ Test case 4: for none-numeric kilometers_per_litre (None) """
        with self.assertRaises(ValueError):
            automobile = Automobile("Genesis", "G90", None)

    def test_str_method_format(self):
        """ Test case 5: for correct string format """
        automobile = Automobile("Genesis", "G90", 9.0)
        expected_str = "Make: Genesis\nModel: G90\nThis automobile can drive 9.0 kilometers per litre."
        self.assertEqual(str(automobile), expected_str)

    def test_calculate_fuel_requirements_correct(self):
        """ Test case 6: for correct fuel """
        automobile = Automobile("Genesis", "G90", 9.0)
        expected_fuel = 90.0 / 9.0 
        self.assertAlmostEqual(automobile.calculate_fuel_requirements(90.0), expected_fuel)