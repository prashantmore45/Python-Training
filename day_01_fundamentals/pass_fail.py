marks = float(input("Enter marks out of 100: "))

if 0 <= marks <= 100:
    print("Pass" if marks >= 40 else "Fail")
else:
    print("Marks must be between 0 and 100.")