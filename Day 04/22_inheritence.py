# Q6. Person → Teacher → Principal
# Use multilevel inheritance.
# Person: Name, Age
# Teacher: Subject
# Principal: School Name
# Display all details using Principal object.
class Person:
    def __init__(self,Name,Age):
        self.Name = Name
        self.Age = Age

class Teacher(Person):
    def __init__(self, Name, Age,Subject):
        self.Subject = Subject
        super().__init__(Name, Age)

class Principle(Teacher):
    def __init__(self, Name, Age, Subject, School_Name):
        self.School_Name = School_Name
        super().__init__(Name, Age, Subject)

    def display(self):
        print("==========Principle Details==========")
        print(f"Name : {self.Name}")
        print(f"Age : {self.Age}")
        print(f"Subject : {self.Subject}")
        print(f"School Name : {self.School_Name}")

name = input("Enter Principle Name : ")
age = int(input("Enter Principle Age : "))
subject = input("Enter Principle Subject : ")
school_name = input("Enter Principle School Name : ")
principle = Principle(name, age, subject, school_name)
principle.display()