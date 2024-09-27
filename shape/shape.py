""""
Description: A class to represent generic Shape objects.
Author: Apurba Khan
Date: 2024.09.27
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    """
    A class for Shape.

    Attributes:
        _color (str): Protected color of shape.
    """
    def __init__(self, color: str):
        """
        Initialize with color.

        Args:
            color (str): No blank.

        Raises:
            ValueError: (color: blank).
        """
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank.")
        else:
            self._color = color

    def __str__(self) -> str:
        """
        Return:
            str: A string indicating the color of the Shape.
        """
        return f"The shape color is {self._color}."

    @abstractmethod
    def calculate_area(self) -> float:
        """
        Calculate area of shape.
        """
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """
        Calculate perimeter of shape.
        """
        pass