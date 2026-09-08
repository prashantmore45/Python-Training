# List in Python

# Create a list with at least 10 student names.
students = ["Amit", "Rahul", "Vishal", "Dhiraj", "Rohit", "Neha", "Priya", "Anjali", "Karan", "Sneha"]

# Print the complete list of students.
print(students)

# Print the last student using negative indexing.
print(students[-1])

# Add a new student to the end of the list.
students.append("Meera")
print(students)

# Insert a student at index 2.
students.insert(2, "Arjun")
print(students)

# Print students from index 1 through index 3.
print(students[1:4])

# Remove a student by name.
students.remove("Dhiraj")
print(students)

# Remove the student at index 3.
students.pop(3)
print(students)

# Update the student at index 1.
students[1] = "Riya"
print(students)