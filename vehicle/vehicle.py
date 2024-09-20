""""
Description: A class to represent generic Vehicle objects.
Author: Sion Kim
Date: 2024.09.18
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    A class for Vehicle.

    Attributes:
        make (str): Private make of vehicle.
        model (str): Private model of vehicle.
    """

    def __init__(self, make: str, model: str):
        """
        Initialize with make and model.

        Arg:
            make (str): No blank.
            model (str): No blank.

        Raise:
            ValueError: (make: blank
                         model: blank).
        """
        if len(make.strip()) == 0:
            raise ValueError("Make cannot be blank.")
        else:
            self.__make = make

        if len(model.strip()) == 0:
            raise ValueError("Model cannot be blank.")
        else:
            self.__model = model

    @property
    def make(self) -> str:
        """
        Return:
            str: make.
        """
        return self.__make

    @property
    def model(self) -> str:
        """
        Return:
            str: model.
        """
        return self.__model

    def __str__(self) -> str:
        """
        Return a string representation of the vehicle's make and model.
        """
        return f"Make: {self.__make}\nModel: {self.__model}"

    @abstractmethod
    def calculate_fuel_requirements(self, distance: float) -> float:
        """
        Return the fuel needed (in litres) to move the vehicle the distance provided.

        Args:
            distance (float): distance for fuel.

        Returns:
            float: fuel litres.
        """
        pass