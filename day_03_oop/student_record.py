class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"{self.roll_number}: {self.name} - {self.marks} marks")


students = [
    Student("Amit", 1, 85),
    Student("Neha", 2, 92),
]

for student in students:
    student.display()