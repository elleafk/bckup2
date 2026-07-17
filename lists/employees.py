employee_names = []
employee_positions = []

totalemployees = int(input("Enter the number of employees: "))

for i in range(totalemployees):
    name = input(f"Enter the name of employee {i + 1}: ")
    position = input(f"Enter the position of employee {i + 1}: ")
    
    employee_names.append(name)
    employee_positions.append(position)
    
print("\nEmployee Records:")
for i in range(len(employee_names)):
    print(f"{i+1}. {employee_names[i]} - {employee_positions[i]}")
    
    