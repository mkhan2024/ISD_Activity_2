""""
Description: A class to represent Triangle objects.
Author: Sion Kim
Date: 2024.09.18
"""
import math
from shape.shape import Shape

class Triangle(Shape):
    """
    A class for triangle.

    Attributes:
        _color (str): Protected color of shape.
        side_1 (int): Length of the first side of the triangle.
        side_2 (int): Length of the second side of the triangle.
        side_3 (int): Length of the third side of the triangle.
    """
    def __init__(self, color: str, side_1: int, side_2: int, side_3: int):
        """
        Initializes with color and three sides.

        Args:
            color (str): No blank.
            side_1 (int): Positive, Integer.
            side_2 (int): Positive, Integer.
            side_3 (int): Positive, Integer.

        Raises:
            ValueError: (side_1: Negative, None-int
                         side_2: Negative, None-int
                         side_3: Negative, None-int).
        """
        super().__init__(color)

        if not isinstance(side_1, int) or side_1 <= 0:
            raise ValueError("Side 1 must be a positive integer.")
        else:
            self.__side_1 = side_1

        if not isinstance(side_2, int) or side_2 <= 0:
            raise ValueError("Side 2 must be a positive integer.")
        else:
            self.__side_2 = side_2

        if not isinstance(side_3, int) or side_3 <= 0:
            raise ValueError("Side 3 must be a positive integer.")
        else:
            self.__side_3 = side_3

    def __str__(self) -> str:
        """
        Return color and side lengths.

        Return:
            str: A string value returned from the superclass.
        """
        value = super().__str__()
        value += f"\nThis triangle has three sides with lengths of {self.__side_1}, {self.__side_2}, and {self.__side_3} centimeters."
        return value


    def calculate_area(self) -> float:
        """
        Calculate area of triangle.

        Return:
            float: Area of triangle.
        """
        semi_perimeter = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.__side_1) * (semi_perimeter - self.__side_2) * (semi_perimeter - self.__side_3))
        return area

    def calculate_perimeter(self) -> float:
        """
        Calculate perimeter of triangle.

        Return:
            float: Perimeter of triangle.
        """
        perimeter = self.__side_1 + self.__side_2 + self.__side_3
        return perimeter