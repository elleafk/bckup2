from sklearn.linear_model import LinearRegression
import numpy as np

n = int(input("Enter number of students: "))

x = []
y = []

for i in range(n):
    hours = float(input(f"Enter study hours of student {i+1}: "))
    score = float(input(f"Enter exam score of student {i+1}: "))
    x.append([hours])
    y.append(score)
    
x = np.array(x)
y = np.array(y)

model = LinearRegression()
model.fit(x, y)

new_hours = float(input("Enter your study hours to predict exam score: "))
prediction = model.predict([[new_hours]])

print("\nYour exam score will be: ", prediction[0])
