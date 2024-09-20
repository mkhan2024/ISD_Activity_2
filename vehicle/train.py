""""
Description: A class to represent Train objects.
Author: {Student Name}
Date: {Date}
"""
"""
Description: A class to represent Train objects.
Author: Sion Kim
Date: 2024.09.18
"""



from vehicle.vehicle import Vehicle


class Train(Vehicle):
    """
    A class for train.
    
    Attribute:
        cars (int): Number of cars on the Train.
        base_fuel_rate (float): Rate at which fuel is burned by the Train.
    """
    
    def __init__(self, make: str, model: str, cars: int, base_fuel_rate: float):
        """
        Initialize with make, model, cars, and base fuel rate.

        Args:
            make (str): No blank.
            model (str): No blank.
            cars (int): Positive, Integer.
            base_fuel_rate (float): Positive, Floater.

        Raises:
            ValueError: (cars: Negative, None-int
                         base_fuel_rate: Negative, None-float).
        """
        super().__init__(make, model)

        if not isinstance(cars, int) or cars <= 0:
            raise ValueError("Cars must be numeric.")
        else:
            self.__cars = cars
            
        if not isinstance(base_fuel_rate, float) or base_fuel_rate <= 0:
            raise ValueError("Base fuel rate must be numeric.")
        else:
            self.__base_fuel_rate = base_fuel_rate
    
    def __str__(self) -> str:
        """
        Return cars and base fuel rate.

        Return:
            str: A string value returned from the superclass.
        """
        value = super().__str__()
        value += f"\nThis train has a base fuel rate of {self.__base_fuel_rate} litres/kilometer, and contains {self.__cars} cars."
        return value

    
    def calculate_fuel_requirements(self, distance: float) -> float:
        """
        Return the calculated fuel requirements.

        Args:
            distance (float): distance for fuel.

        Returns:
            float: fuel
        """
        total_fuel = self.__base_fuel_rate * (1.1 * self.__cars) 
        fuel_requirements = total_fuel * distance  
        return fuel_requirements