import pandas as pd

studentInfo {
    "Name": ["Janelle", "Genniviev", "Daphnie", "Jester", "Angela"],
    "Age": [19,19,21,20,19],
    "Course": ["BSIT", "BSIT", "BSED", "BABr", "BSCS"],
    "Grade": [97,95,95,96,96]
             }

df = pd.DataFrame(studentInfo)
print(df)