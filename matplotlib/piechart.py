import matplotlib.pyplot as plt

programs = ["BSIT", "BSBA", "BSCS", "BSHM"]
students = [40,30,20,10]
explode = [0.02, 0.02, 0.02, 0.02]

plt.pie(students, labels=programs, autopct="%1.1f%%", explode=explode)

plt.title("Students Distribution by Programs")
plt.show()