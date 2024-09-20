""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Author: Sion Kim
Date: 2024.09.19
"""

from shape import *
from vehicle import *

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")
    # 1. Create an empty list of Shape objects.
    shapes = []

    # 2. Code a statement which creates an instance of the Triangle class.
    # Append the Triangle to the list of shapes.
    try:
        triangle_1 = Triangle("white", 9, 8, 3)
        shapes.append(triangle_1)
    except ValueError as e:
        print(e)


    # 3. Code a statement which creates an instance of the Rectangle class.
    # Append the Rectangle to the list of shapes.
    try:
        rectangle_1 = Rectangle("white", 3, 6)
        shapes.append(rectangle_1)
    except ValueError as e:
        print(e)


    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    try:
        triangle_2 = Triangle("red", 8, 3, 6)
        shapes.append(triangle_2)
    except ValueError as e:
        print(e)

    try:
        triangle_3 = Triangle("orange", 11, 12, 13)
        shapes.append(triangle_3)
    except ValueError as e:
        print(e)

    try:
        rectangle_2 = Rectangle("yellow", 8, 2)
        shapes.append(rectangle_2)
    except ValueError as e:
        print(e)

    # 4.5. Errors
    try:
        triangle_error_1 = Triangle(" ", 8, 3, 6)
        shapes.append(triangle_error_1)
    except ValueError as e:
        print(e)

    try:
        triangle_error_2 = Triangle("red", None, 3, 6)
        shapes.append(triangle_error_2)
    except ValueError as e:
        print(e)

    try:
        triangle_error_3 = Triangle("red", 8, None, 6)
        shapes.append(triangle_error_3)
    except ValueError as e:
        print(e)

    try:
        triangle_error_4 = Triangle("red", 8, 3, None)
        shapes.append(triangle_error_4)
    except ValueError as e:
        print(e)
    print("-------------Triangle Errors-------------")

    try:
        rectangle_error_1 = Rectangle(" ", 3, 6)
        shapes.append(rectangle_error_1)
    except ValueError as e:
        print(e)

    try:
        rectangle_error_2 = Rectangle("white", None, 6)
        shapes.append(rectangle_error_2)
    except ValueError as e:
        print(e)

    try:
        rectangle_error_3 = Rectangle("white", 3, None)
        shapes.append(rectangle_error_3)
    except ValueError as e:
        print(e)

    print("-------------Rectangle Errors-------------")

    # 5. Iterate through the list of shapes.  On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shape in shapes:
        print(shape)
        print(f"Area: {shape.calculate_area():.2f}")
        print(f"Perimeter: {shape.calculate_perimeter():.2f}")



    # *** END PART 1 ***

    # *** PART 2 ***
    print("*************PART 2****************")
    # 1. Create an empty list of Vehicle objects.
    vehicles = []

    # 2. Code a statement which creates an instance of the Automobile class.
    # Append the Automobile to the list of vehicles.
    try:
        automobile_1 = Automobile("Genesis", "G90", 9.0)
        vehicles.append(automobile_1)
    except ValueError as e:
        print(e)


    # 3. Code a statement which creates an instance of the Aircraft class.
    # Append the Aircraft to the list of vehicles.
    try:
        aircraft_1 = Aircraft("KAI", "KF-21", 30.0, 1500.0)
        vehicles.append(aircraft_1)
    except ValueError as e:
        print(e)


    # 4. Code 3 additional statements which creates an instance of 
    # Automobile, Aircraft or Train classes (your choice).
    # Append these instances to the list of vehicles.
    try:
        automobile_2 = Automobile("Hyundai", "IONIQ 5N", 30.0)
        vehicles.append(automobile_2)
    except ValueError as e:
        print(e)

    try:
        train_1 = Train("SNCF", "TGV", 30, 0.04)
        vehicles.append(train_1)
    except ValueError as e:
        print(e)

    try:
        aircraft_2 = Aircraft("Lockeed Martin", "SR-71", 10.0, 2000.0)
        vehicles.append(aircraft_2)
    except ValueError as e:
        print(e)

    # 4.5. Errors
    try:
        automobile_error_1 = Automobile(" ", "IONIQ 5N", 30.0)
        vehicles.append(automobile_error_1)
    except ValueError as e:
        print(e)

    try:
        automobile_error_2 = Automobile("Hyundai", " ", 30.0)
        vehicles.append(automobile_error_2)
    except ValueError as e:
        print(e)

    try:
        automobile_error_3 = Automobile("Hyundai", "IONIQ 5N", None)
        vehicles.append(automobile_error_3)
    except ValueError as e:
        print(e)
    print("-------------Automoblie Errors-------------")
    
    try:
        train_error_1 = Train(" ", "TGV", 30, 0.04)
        vehicles.append(train_error_1)
    except ValueError as e:
        print(e)

    try:
        train_error_2 = Train("SNCF", " ", 30, 0.04)
        vehicles.append(train_error_2)
    except ValueError as e:
        print(e)

    try:
        train_error_3 = Train("SNCF", "TGV", None, 0.04)
        vehicles.append(train_error_3)
    except ValueError as e:
        print(e)

    try:
        train_error_4 = Train("SNCF", "TGV", 30, None)
        vehicles.append(train_error_4)
    except ValueError as e:
        print(e)
    print("-------------Train Errors-------------")
    
    try:
        aircraft_error_1 = Aircraft(" ", "SR-71", 10.0, 2000.0)
        vehicles.append(aircraft_error_1)
    except ValueError as e:
        print(e)

    try:
        aircraft_error_2 = Aircraft("Lockeed Martin", " ", 10.0, 2000.0)
        vehicles.append(aircraft_error_2)
    except ValueError as e:
        print(e)

    try:
        aircraft_error_3 = Aircraft("Lockeed Martin", "SR-71", None, 2000.0)
        vehicles.append(aircraft_error_3)
    except ValueError as e:
        print(e)

    try:
        aircraft_error_4 = Aircraft("Lockeed Martin", "SR-71", 10.0, None)
        vehicles.append(aircraft_error_4)
    except ValueError as e:
        print(e)
    print("-------------Aircraft Errors-------------")
    
    # 5. Iterate through the list of vehicles.  On each iteration:
    # - print the vehicle
    # - print the phrase:
    # "Fuel needed for 500 kilometers: {fuel requirements} litres."
    for vehicle in vehicles:
        print(vehicle)
        fuel_needed = vehicle.calculate_fuel_requirements(500)
        print(f"Fuel needed for 500 kilometers: {fuel_needed:.2f} litres.")


if __name__ == "__main__":
    main()