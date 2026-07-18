#Student Subject Comparison System
student1 = set()
student2 = set()

sub1 = int(input("How many favorite subjects does student 1 have? "))

for i in range(sub1):
    subject1 = input(f"Subject {i+1}: ")
    student1.add(subject1)
    
print("\nStudent 1 Subjects:")
for s1 in student1:
    print(s1)
    
sub2 = int(input("\nHow many favorite subjects does student 2 have? "))

for i in range(sub2):
    subject2 = input(f"Subject {i+1}: ")
    student2.add(subject2)
    
print("\nStudent 2 Subjects:")
for s2 in student2:
    print(s2)
    
print("\nCollection of Subjects:")
collection = student1 | student2
for union in collection:
    print(union)
    
print("\nCommon Subjects: ")
common = student1 & student2
for intersection in common:
    print(intersection)
    
print("\nOnly student 1 likes: ")
different1 = student1 - student2
for difference1 in different1:
    print(difference1)
    
print("\nOnly student 2 likes: ")
different2 = student2 - student1
for difference2 in different2:
    print(difference2)
    
print("\nSubjects they dont have in common: ")
unique = student1 ^ student2
for uniquesub in unique:
    print(uniquesub)
    
print("\nTotal unique subjects: ", len(collection))
print("Student 1 unique subjects: ", len(student1))
print("Student 2 unique subjects: ", len(student2))





