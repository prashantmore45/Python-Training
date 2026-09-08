from pathlib import Path


filename = Path(__file__).with_name("student.txt")

with open(filename, "r", encoding="utf-8") as file:
    line_count = sum(1 for _ in file)

print(f"{filename.name} contains {line_count} lines.")