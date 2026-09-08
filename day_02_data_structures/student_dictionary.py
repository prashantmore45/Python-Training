student = {"name": "Amit", "age": 20, "course": "Python", "marks": 85}
student["city"] = "Pune"
student["marks"] = 90

for key, value in student.items():
    print(f"{key}: {value}")