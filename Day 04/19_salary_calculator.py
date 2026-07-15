# Q3. Employee Salary Calculator
# Create an Employee class with Employee ID, Name, Basic Salary.
# Methods to calculate HRA (20%), DA (10%), Gross Salary, and display details.
class Employee:
    def __init__(self, Employee_ID, Name, Basic_Salary):
        self.Employee_ID = Employee_ID
        self.Name = Name
        self.Basic_Salary = Basic_Salary
    
    def calculate_HRA(self):
        return self.Basic_Salary * (20 / 100)
    
    def calculate_DA(self):
        return self.Basic_Salary * (10 / 100)
    
    def calculate_Gross(self):
        return self.Basic_Salary + self.calculate_DA() + self.calculate_HRA()
    
    def display_details(self):
        print(f"Employee ID: {self.Employee_ID}")
        print(f"Name: {self.Name}")
        print(f"Basic Salary: {self.Basic_Salary}")
        print(f"HRA: {self.calculate_HRA()}")
        print(f"DA: {self.calculate_DA()}")
        print(f"Gross Salary: {self.calculate_Gross()}")

e1 = Employee(101, "John Doe", 50000)
e1.display_details()