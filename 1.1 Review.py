"""
Scenario: You're building an application for a Tire Center to model the different vehicles that are serviced
The types of Vehicles the Tire Center services include Cars, Trucks, and Cycles.
The types of Cycles the mechanic services includes bikes and motoercycles.
The mechanic care about the number or tires on each vehicle,
who owns it, and whether or not the vehicle has an engine

Create a python file that contains classes that model this.
Each class should contain a constructor and a way to print the objects specifications.
No need for getters and setters (but feel free to include them).
Repeat as little code as possible
Example for printing a Bicycle: "Type: Bicycle; Owner: Josh; Engine: False; Tires: 2"

Be prepared to share
"""

class Vehicle:
    def __init__(self, type: str, owner:str, engine:bool, tire_num=4):
        self.type = type
        self.owner = owner
        self.engine = engine
        self.tire_num = tire_num
    
    def __str__(self) -> str:
        result = ''
        result += f'Type: {self.type}, '
        result += f'Owner: {self.owner}, '
        result += f'Engine: {self.engine}, '
        result += f'Tires: {self.tire_num}'
        return result

class Car(Vehicle):
    def __init__(self, owner:str):
        Vehicle.__init__(self, "Car", owner, True, 4)
        self.owner = owner

class Truck(Vehicle):
    def __init__(self, owner:str):
        Vehicle.__init__(self, "Truck", owner, True, 4)
        self.owner = owner

class Cycle(Vehicle):
    def __init__(self, type: str, owner:str, engine:bool):
        Vehicle.__init__(self, type, owner, engine, 2)

class Bike(Cycle):
    def __init__(self, owner:str):
        Cycle.__init__(self, "Bicycle", owner, False)
        self.owner = owner

class Motorcycle(Cycle):
    def __init__(self, owner:str):
        Cycle.__init__(self, "Motorcycle", owner, True)
        self.owner = owner

joshBike = Bike("Josh")
print(joshBike)

alexMotorcycle = Motorcycle("Alex")
print(alexMotorcycle)

connorCar = Car("Connor")
print(connorCar)

tomTruck = Truck("Thomas")
print(tomTruck)

