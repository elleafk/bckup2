import numpy as np
import matplotlib.pyplot as plt

names = []
grades = []

n = int(input("Enter the number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    grade = int(input(f"Enter grade of {name}: "))
    
    names.append(name)
    grades.append(grade)
    
print("\n")

plt.bar(names,grades, color="purple")
plt.title("Grades of the students")
plt.xlabel("Student names")
plt.ylabel("Grades")
plt.show()