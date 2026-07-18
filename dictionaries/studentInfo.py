student = {}

print("Enter the information below:")

student["name"] = input("Name: ")
student["course"] = input("Course: ")
student["year"] = input("Year: ")
student["school"] = input("School: ")

def displayInfo():
    print("\nStudent Information")
    print("Name: ", student["name"])
    print("Course: ", student["course"])
    print("Year: ", student["year"])
    print("School: ", student["school"])
    
displayInfo()

def updateYear():
    student["year"] = input("Update year: ")

while True:
    choice = input("\nWould you like to update your year level?(Y/N): ")
    if choice.upper() == "Y":
        updateYear()
        displayInfo()
    elif choice.upper() == "N":
        break
    else:
        print("Please enter Y or N only.")

