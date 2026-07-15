# create a student info system
# creat a student class with attributes : name, roll, marks(3 sub)
# Methods: get_data(),display_data(),calculate_percentage()
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def get_data(self):
        self.name = input("Enter student's name:")
        self.roll_number = input("Enter student's roll number:")
        self.marks = []
        for i in range(3):
                mark = float(input(f"Enter marks for subject {i + 1}:"))
                self.marks.append(mark)

    def display_data(self):
         print(f"The name of the student is: {self.name}\nThe Roll Number of the student is: {self.roll_number}\nThe marks of the student are: {self.marks}")

    def calculate_percentage(self):
         total_marks = sum(self.marks)
         percentage = (total_marks / 300) * 100
         print(f"The percentage of the student is: {percentage}%")

student1 = Student("", "", [])
student1.get_data()
student1.display_data()
student1.calculate_percentage()