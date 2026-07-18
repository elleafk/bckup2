studInfo = {"name": "Janelle",
            "age": 19,
            "course": "bsit",
            "school": "bulsu",
            "year": "3"}

def display():
    print("Student Information:")
    print("Name: ", studInfo.get("name", "N/A"))
    print("Age: ", studInfo.get("age", "N/A"))
    print("Course: ", studInfo.get("course", "N/A"))
    print("Year: ", studInfo.get("year", "N/A"))
    print("School: ", studInfo.get("school", "N/A"))
    
display()

info = input("\nEnter the info you want to delete: ")
remove = studInfo.pop(info, None)

print("\n")
if remove is None:
    print("Information does not exist.")
else:
    print("\nThe information you deleted is: ", remove)
    display()
        



