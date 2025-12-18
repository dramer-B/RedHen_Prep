import numpy as np

# 1. Create a fake dataset (Matrix of 5 students, 3 exam scores)
# Random numbers between 0 and 100
data = np.random.randint(0, 100, size=(5, 3))

print("--- Raw Student Data (5 Students, 3 Exams) ---")
print(data)

# 2. Calculate the average score for each student
# axis=1 means "calculate across the row"
averages = np.mean(data, axis=1)

print("\n--- Student Averages ---")
print(averages)

# 3. Find who passed (Average > 50)
print("\n--- Pass/Fail Status ---")
print(averages > 50)
