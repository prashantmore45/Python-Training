from pathlib import Path

import matplotlib.pyplot as plt

subjects = ["Python", "Pandas", "NumPy", "SQL"]
marks = [85, 78, 92, 88]

figure, charts = plt.subplots(2, 2, figsize=(10, 7))
charts[0, 0].plot(subjects, marks, marker="o")
charts[0, 0].set_title("Line chart")
charts[0, 1].bar(subjects, marks)
charts[0, 1].set_title("Bar chart")
charts[1, 0].scatter([2, 4, 6, 8], marks)
charts[1, 0].set_title("Study hours vs marks")
charts[1, 1].pie(marks, labels=subjects, autopct="%1.1f%%")
charts[1, 1].set_title("Marks distribution")

figure.tight_layout()
figure.savefig(Path(__file__).with_name("student_chart_gallery.png"), dpi=150)
plt.show()