""""
Description: A class to represent Rectangle objects.
Author: Apurba Khan
Date: 2024.09.27
"""
from shape.shape import Shape

class Rectangle(Shape):
    """
    A class for rectangle.

    Attributes:
        _color (str): Protected color of shape.
        length (int): Length of the rectangle.
        width (int): Width of the rectangle.
    """

    def __init__(self, color: str, length: int, width: int):
        """
        Initialize with color, length, and width.

        Args:
            color (str): No blank.
            length (int): Positive, Integer.
            width (int): Positive, Integer.

        Raises:
            ValueError: (length: Negative, None-int
                         width: Negative, None-int).
        """
        super().__init__(color)

        if not isinstance(length, int) or length <= 0:
            raise ValueError("Length must be a positive integer.")
        else:
            self.__length = length
            
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        else:
            self.__width = width

    def __str__(self) -> str:
        """
        Return color, lengths, and widths.

        Return:
            str: A string value returned from the superclass.
        """
        value = super().__str__()
        value += f"\nThis rectangle has four sides with the lengths of {self.__length}, {self.__width}, {self.__length}, and {self.__width} centimeters."
        return value

    def calculate_area(self) -> float:
        """
        Calculate area of rectangle.

        Return:
            float: Area of rectangle.
        """
        area = self.__length * self.__width
        return area

    def calculate_perimeter(self) -> float:
        """
        Calculate perimeter of rectangle.

        Return:
            float: Perimeter of rectangle.
        """
        perimeter = 2 * (self.__length + self.__width)
        return perimeter