import pandas as pd

studentinfo = { 
               "Name": ["John", "Mary", "Peter", "Anna"],
               "Age": [20,21,19,22],
               "Course": ["BSIT", "BSCS", "BSIS", "BSIT"],
               "Grade": [90,95,88,92]
}

df = pd.DataFrame(studentinfo)
print(df)