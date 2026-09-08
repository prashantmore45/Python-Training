python_students = {"Amit", "Neha", "Ravi", "Priya"}
data_students = {"Neha", "Priya", "Karan"}

print("All students:", python_students | data_students)
print("Students in both courses:", python_students & data_students)
print("Only in Python:", python_students - data_students)