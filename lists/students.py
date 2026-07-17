student_names = []
student_scores = []
student_remarks = []

totalstudents = int(input("Enter the number of students: "))

for i in range(totalstudents):
    name = input(f"Name of student {i+1}: ")
    score = int(input(f"Score of student {i+1}: "))
    if score >= 75:
        remark = "Passed"
    else:
        remark = "Failed"
    student_names.append(name)
    student_scores.append(score)
    student_remarks.append(remark)
    
print("\nStudent Records: ")
for i in range(len(student_names)):
    print(f"{i+1}. {student_names[i]} - {student_scores[i]} - {student_remarks[i]}")