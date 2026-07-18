studInfo = {"Name": "Janelle",
            "Age": 19,
            "Course": "bsit",
            "School": "bulsu",
            "Year": "3"}

def display():
    print("\nStudent Information: ")
    for key,value in studInfo.items():
        print(f"{key.title()}: {value}")
    
display()

info = input("\nEnter the info you want to delete: ")
remove = studInfo.pop(info, None)

print("\n")
if remove is None:
    print("Information does not exist.")
else:
    print("\nThe information you deleted is: ", remove)
    print("\n")
    display()
        



