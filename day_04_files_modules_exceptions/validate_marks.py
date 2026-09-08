class InvalidMarksError(ValueError):
    pass


def validate_marks(marks):
    if not 0 <= marks <= 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    return marks


try:
    marks = validate_marks(int(input("Enter marks: ")))
    print("Valid marks:", marks)
except (ValueError, InvalidMarksError) as error:
    print("Invalid input:", error)