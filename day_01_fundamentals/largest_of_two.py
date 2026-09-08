first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number > second_number:
    print("Largest number:", first_number)
elif second_number > first_number:
    print("Largest number:", second_number)
else:
    print("Both numbers are equal.")