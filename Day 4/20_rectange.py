# Q4. Rectangle Operations
# Create a Rectangle class with Length and Breadth.
# Methods: area(), perimeter(), check_square().

class Rectangle:
    def __init__(self, Length, Breadth):
        self.Length = Length
        self.Breadth = Breadth
    
    def get_data(self):
        self.Length = float(input("Enter the Length : "))
        self.Breadth = float(input("Enter the Breadth : "))

    def area(self):
        self.area = self.Length * self.Breadth
        print(f"The area of rectangle is {self.area}")

    def perimeter(self):
        self.perimeter = 2 * (self.Length + self.Breadth)
        print(f"The perimeter of rectangle is {self.perimeter}")

    def check_square(self):
        if self.Length == self.Breadth:
            print("The rectangle is square")
        else:
            print("The rectangle is not a square")

R1 = Rectangle(0, 0)
R1.get_data()
R1.area()
R1.perimeter()
R1.check_square()