import numpy as np

sales = np.array(list(map(int, input("Enter sales separated by space: ").split())))

print("\nSales: ", sales)
print("Number of sales entered: ", len(sales))
print("Total sales: ", np.sum(sales))
print("Average sales: ", np.mean(sales))
print("Highest sale: ", np.max(sales))
print("Lowest sale: ", np.min(sales))
print("\n")