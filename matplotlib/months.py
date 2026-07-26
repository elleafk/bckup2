import matplotlib.pyplot as plt

#line chart
month = ["January", "February", "March", "April", "May"]
gpa = [1.80, 1.75, 1.70, 1.68, 1.65]

plt.plot(month, gpa, marker="o", color="violet")

plt.title("GPA Status Per Month")
plt.xlabel("Months")
plt.ylabel("GPA")
plt.show()