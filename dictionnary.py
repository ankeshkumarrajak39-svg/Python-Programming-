
import pandas as pd

data = [
    {"Name": "Ankesh", "Marks": 99},
    {"Name": "abhay", "Marks": 66},
    {"Name": "ajbhi", "Marks": 44},
    {"Name": "abhhi", "Marks": 42},
    {"Name": "abfhi", "Marks": 45}
]

index = ["s1", "s2", "s3", "s4", "s5"]

df = pd.DataFrame(data, index=index)

print(df)
#selecting row
print(df.loc[["s1", "s2"]])   #slicing 
print(df.loc["s1","Marks"])  #another use of loc
print(df.loc["s1"])