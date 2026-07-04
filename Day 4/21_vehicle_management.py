# Q5. Vehicle Management System
# Create a Vehicle base class with Brand and Model.
# Create Car (Fuel Type) and Bike (Engine Capacity) child classes.
# Override display() in child classes.
class Vehicle:
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model

    def display(self):
        print(f"Brand: {self.Brand}, Model: {self.Model}")

class Car(Vehicle):
    def __init__(self, Brand, Model, Fuel_Type):
        super().__init__(Brand, Model)
        self.Fuel_Type = Fuel_Type

    def display(self):
        print(f"Car - Brand: {self.Brand}, Model: {self.Model}, Fuel Type: {self.Fuel_Type}")

class Bike(Vehicle):
    def __init__(self, Brand, Model, Engine_Capacity):
        super().__init__(Brand, Model)
        self.Engine_Capacity = Engine_Capacity

    def display(self):
        print(f"Bike - Brand: {self.Brand}, Model: {self.Model}, Engine Capacity: {self.Engine_Capacity}")

car1 = Car("BMW", "M1", "Petrol")
car1.display()

bike1 = Bike("David Putra", "D1", "3000cc")
bike1.display()