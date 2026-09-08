def grade_for(marks):
	if marks >= 90:
		return "A"
	if marks >= 80:
		return "B"
	if marks >= 70:
		return "C"
	if marks >= 60:
		return "D"
	return "F"


students = []
student_count = int(input("How many students? "))

for number in range(1, student_count + 1):
	name = input(f"Enter name for student {number}: ")
	marks = float(input(f"Enter marks for {name}: "))
	students.append({"name": name, "marks": marks, "grade": grade_for(marks)})

print("\nStudent Marks Report")
for student in students:
	print(
		f"{student['name']}: {student['marks']:.1f} "
		f"(Grade {student['grade']})"
	)

if students:
	highest_scorer = max(students, key=lambda student: student["marks"])
	average_marks = sum(student["marks"] for student in students) / len(students)
	print("Highest scorer:", highest_scorer["name"])
	print(f"Class average: {average_marks:.1f}")

