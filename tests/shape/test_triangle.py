"""
Description: Unit tests for the Book class.
Author: Sion Kim
Date: 2024.09.18
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/test_triangle.py
"""
import unittest
from shape.triangle import Triangle

class TestTriangle(unittest.TestCase):

    def test_init_valid(self):
        """ Test case 1: for triagle with name mangling """
        triangle = Triangle("white", 9, 8, 3)
        self.assertEqual(triangle._color, "white")
        self.assertEqual(triangle._Triangle__side_1, 9)
        self.assertEqual(triangle._Triangle__side_2, 8)
        self.assertEqual(triangle._Triangle__side_3, 3)

    def test_init_blank_color(self):
        """ Test case 2: for blank color (" ") """
        with self.assertRaises(ValueError):
            triangle = Triangle(" ", 9, 8, 3)

    def test_init_none_integer_side_1(self):
        """ Test case 3: for none numeric side 1 length (None) """
        with self.assertRaises(ValueError):
            triangle = Triangle("white", None, 8, 3)

    def test_init_none_integer_side_2(self):
        """ Test case 4: for none numeric side 2 length (None) """
        with self.assertRaises(ValueError):
            triangle = Triangle("white", 9, None, 3)

    def test_init_none_integer_side_3(self):
        """ Test case 5: for none numeric side 3 length (None) """
        with self.assertRaises(ValueError):
            triangle = Triangle("white", 9, 8, None)

    def test_str_format(self):
        """ Test case 6: for correct string format """
        triangle = Triangle("white", 9, 8, 3)
        expected_str = "The shape color is white.\nThis triangle has three sides with lengths of 9, 8, and 3 centimeters."
        self.assertEqual(str(triangle), expected_str)

    def test_calculate_area_correct(self):
        """ Test case 7: for correct area """
        triangle = Triangle("white", 9, 8, 3)
        expected_area = 11.83
        self.assertAlmostEqual(triangle.calculate_area(), expected_area, places=2)

    def test_calculate_perimeter_correct(self):
        """ Test case 8: for correct perimeter """
        triangle = Triangle("white", 9, 8, 3)
        expected_perimeter = 20
        self.assertEqual(triangle.calculate_perimeter(), expected_perimeter)