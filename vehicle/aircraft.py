""""
Description: A class to represent Aircraft objects.
Author: Apurba Khan
Date: 2024.09.27
"""


from vehicle.vehicle import Vehicle


class Aircraft(Vehicle):
    """
    A class for aircraft.

    Attributes:
        fuel_burn_rate (float): Rate at which Aircraft fuel is expended. the Automobile.
        speed (float): Cruising speed of the Aircraft.
    """

    def __init__(self, make: str, model: str, fuel_burn_rate: float, speed: float):
        """
        Initialize with make, model, fuel burn rate, and speed.

        Args:
            make (str): No blank.
            model (str): No blank.
            fuel_burn_rate (float): Positive, Numeric.
            speed (float): Positive, Numeric.

        Raises:
            ValueError: (cars: Negative, None-numeric
                         base_fuel_rate: Negative, None-numeric).
        """
        super().__init__(make, model)

        if not isinstance(fuel_burn_rate, (int, float)) or fuel_burn_rate <= 0:
            raise ValueError("Fuel burn rate must be numeric.")
        else:
            self.__fuel_burn_rate = fuel_burn_rate
            
        if not isinstance(speed, (int, float)) or speed <= 0:
            raise ValueError("Speed must be numeric.")
        else:
            self.__speed = speed

    def __str__(self) -> str:
        """
        Return cars and base fuel burn rate and speed.

        Return:
            str: A string value returned from the superclass.
        """
        value = super().__str__() 
        value += f"\nThis aircraft has a fuel burn rate of {self.__fuel_burn_rate} litres/hour, and a cruising speed of {self.__speed} km/hour."
        return value
    
    def calculate_fuel_requirements(self, distance: float) -> float:
        """
        Return the calculated fuel requirements.

        Args:
            distance (float): distance for fuel.

        Returns:
            float: fuel
        """
        flight_time = distance / self.__speed
        return flight_time * self.__fuel_burn_rate
