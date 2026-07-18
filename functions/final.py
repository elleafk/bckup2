def computeAverage(math, english, science):
    total = math + english + science
    average = total/3
    return average

def displayResult(name, average):
    print(f"Student name: {name}")
    print(f"Average: {average}")
    if average >= 75:
        print(f"Status: Passed")
    elif average <= 75:
        print(f"Status: Failed")
    else:
        print("N/A")
        
print("\nStudent Record 1:")
avg = computeAverage(90,96,98)
displayResult ("Janelle", avg)