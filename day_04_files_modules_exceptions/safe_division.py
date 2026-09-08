try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    print("Result:", numerator / denominator)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("The denominator cannot be zero.")