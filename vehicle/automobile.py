""""
Description: A class to represent Automobile objects.
Author: Sion Kim
Date: 2024.09.18
"""

from vehicle.vehicle import Vehicle

class Automobile(Vehicle):
    """
    A class for Automobile.

    Attributes:
        kilometers_per_litre (float): kilometers_per_litre of automobile.
    """

    def __init__(self, make: str, model: str, kilometers_per_litre: float):
        """
        Initializes the Automobile with a make, model, and kilometers per litre.

        Args:
            make (str): No blank.
            model (str): No blank.
            kilometers_per_litre (float): Positive, Numeric.

        Raises:
            ValueError: (kilometers_per_litre: Negative, None-numeric).
        """
        super().__init__(make, model)

        if not isinstance(kilometers_per_litre, (int, float)) or kilometers_per_litre <= 0:
            raise ValueError("Kilometers per litre must be numeric.")
        else:
            self.__kilometers_per_litre = kilometers_per_litre

    def __str__(self) -> str:
        """
        Return the string value returned from the superclass.
        """
        value = super().__str__()
        value += f"\nThis automobile can drive {self.__kilometers_per_litre} kilometers per litre."
        return value
    
    def calculate_fuel_requirements(self, distance: float) -> float:
        """
        Return the fuel needed (in litres) to move the vehicle the distance provided.

        Args:
            distance (float): distance for fuel.

        Returns:
            float: fuel litres.
        """
        fuel_requirements = distance / self.__kilometers_per_litre
        return fuel_requirements