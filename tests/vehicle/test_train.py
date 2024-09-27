"""
Description: Unit tests for the Train class.
Author: Apurba Khan
Date: 2024.09.27
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/vehicle/test_train.py
"""

import unittest
from vehicle.train import Train

class TestTrain(unittest.TestCase):

    def test_init_valid(self):
        """ Test case 1: for Train with name mangling """
        train = Train("Korail", "KTX", 20, 0.05)
        self.assertEqual(train._Vehicle__make, "Korail")
        self.assertEqual(train._Vehicle__model, "KTX")
        self.assertEqual(train._Train__cars, 20)
        self.assertEqual(train._Train__base_fuel_rate, 0.05)

    def test_init_blank_make(self):
        """ Test case 2: for blank make (" ") """
        with self.assertRaises(ValueError):
            train = Train(" ", "KTX", 20, 0.05)

    def test_init_blank_model(self):
        """ Test case 3: for blank model (" ") """
        with self.assertRaises(ValueError):
            train = Train("Korail", " ", 20, 0.05)

    def test_init_none_integer_cars(self):
        """ Test case 4: for none-numeric cars (None) """
        with self.assertRaises(ValueError):
            train = Train("Korail", "KTX", None, 0.05)

    def test_init_none_numeric_base_fuel_rate(self):
        """ Test case 5: for none-numeric base_fuel_rate (None) """
        with self.assertRaises(ValueError):
            train = Train("Korail", "KTX", 20, None)

    def test_str_method_format(self):
        """ Test case 6: for correct string format """
        train = Train("Korail", "KTX", 20, 0.05)
        expected_str = "Make: Korail\nModel: KTX\nThis train has a base fuel rate of 0.05 litres/kilometer, and contains 20 cars."
        self.assertEqual(str(train), expected_str)

    def test_calculate_fuel_requirements_correct(self):
        """ Test case 7: for correct fuel """
        train = Train("Korail", "KTX", 20, 0.05)
        expected_fuel = (0.05 * (1.1 * 20)) * 300 
        self.assertAlmostEqual(train.calculate_fuel_requirements(300), expected_fuel)