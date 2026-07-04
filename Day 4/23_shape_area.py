# Q7. Shape Area Calculator
# Create Shape parent class.
# Child classes: Circle, Rectangle, Triangle.
# Each class should implement its own area() method.
import math
class Shape:
    def __init__(self):
        pass

class Circle(Shape):
    def __init__(self,Radius):
        self.Radius = Radius
        
    def area(self):
        area = math.pi * self.Radius ** 2
        return area
    
class Rectangle(Shape):
    def __init__(self,Length,Width):
        self.Length = Length
        self.Width = Width

    def area(self):
        area = self.Length * self.Width
        return area
    
class Triangle(Shape):
    def __init__(self,Base,Height):
        self.Base = Base
        self.Height = Height

    def area(self):
        area = 0.5 * self.Base * self.Height
        return area
    
while True:

    print("Select Shape to calculate area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        radius = float(input("Enter the radius of the circle:"))
        circle = Circle(radius)
        print("Area of Circle:", circle.area())

    elif choice == 2:
        Length = float(input("Enter the length of the Rectangle:"))
        Width = float(input("Enter the width of the rectangle:"))
        Rectangle = Rectangle(Length,Width)
        print("Area of Ractangle:",Rectangle.area())

    elif choice == 3:
        Base = float(input("Enter the Base: "))
        Height = float(input("Enter the Height: "))
        Triangle = Triangle(Base, Height)
        print("Area of Triangle: ", Triangle.area())

    else:
        print("Invalid choice")

    while True:
        cont = input("Do you want to calculate area of another shape? (y/n):")
        if cont.lower() == 'y':
            break
        elif cont == 'n':
            exit()
        else:
            print("Invalid answer")