print("Hello World")

name = "John"
age = 25
price = 101.5
isTrue = True

print(type(age))
print(type(name))
print(type(price))
print(type(isTrue))


age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")


marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")