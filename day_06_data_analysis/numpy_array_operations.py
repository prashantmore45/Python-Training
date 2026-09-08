import numpy as np

marks = np.array([72, 85, 64, 91, 78])
matrix = np.arange(1, 7).reshape(2, 3)

print("Marks:", marks)
print("Shape:", marks.shape)
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("First three:", marks[:3])
print("Matrix:\n", matrix)