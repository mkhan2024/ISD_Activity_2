"""
Description: Unit tests for the Rectangle class.
Author: Apurba Khan
Date: 2024.09.27
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/test_rectangle.py
"""

import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_init_valid(self):
        """ Test case 1: for rectangle with name mangling """
        rectangle = Rectangle("white", 3, 6)
        self.assertEqual(rectangle._color, "white")
        self.assertEqual(rectangle._Rectangle__length, 3)
        self.assertEqual(rectangle._Rectangle__width, 6)

    def test_init_blank_color(self):
        """ Test case 2: for blank color (" ") """
        with self.assertRaises(ValueError):
            Rectangle(" ", 3, 6)

    def test_init_none_integer_length(self):
        """ Test case 3: for none numeric length (None) """
        with self.assertRaises(ValueError):
            Rectangle("white", None, 6)

    def test_init_none_integer_width(self):
        """ Test case 4: for none numeric width (None) """
        with self.assertRaises(ValueError):
            Rectangle("white", 3, None)

    def test_str_format(self):
        """ Test case 5: for correct string format """
        rectangle = Rectangle("white", 3, 6)
        expected_str = "The shape color is white.\nThis rectangle has four sides with the lengths of 3, 6, 3, and 6 centimeters."
        self.assertEqual(str(rectangle), expected_str)

    def test_calculate_area_correct(self):
        """ Test case 6: for correct area """
        rectangle = Rectangle("white", 3, 6)
        expected_area = 18
        self.assertEqual(rectangle.calculate_area(), expected_area)

    def test_calculate_perimeter_correct(self):
        """ Test case 7: for correct perimeter """
        rectangle = Rectangle("white", 3, 6)
        expected_perimeter = 18 
        self.assertEqual(rectangle.calculate_perimeter(), expected_perimeter)