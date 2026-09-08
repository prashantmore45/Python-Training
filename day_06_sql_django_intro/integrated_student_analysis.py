from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd

records = [("Python", 85), ("Python", 92), ("Data", 78), ("Data", 88)]

with sqlite3.connect(":memory:") as connection:
    connection.execute("CREATE TABLE students (department TEXT, marks INTEGER)")
    connection.executemany("INSERT INTO students VALUES (?, ?)", records)
    students = pd.read_sql_query("SELECT * FROM students", connection)

average_marks = students.groupby("department")["marks"].mean()
print(average_marks)
average_marks.plot(kind="bar", title="Average marks by department")
plt.ylabel("Average marks")
plt.tight_layout()
plt.savefig(Path(__file__).with_name("average_marks_by_department.png"), dpi=150)