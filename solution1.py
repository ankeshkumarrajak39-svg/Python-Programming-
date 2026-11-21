
import pandas as pd

data = [
    {"Name": "Ankesh", "Marks": 99},
    {"Name": "abhay", "Marks": 66},
    {"Name": "ajbhi", "Marks": 404},
    {"Name": "abhhi", "Marks": 452},
    {"Name": "abfhi", "Marks": 945},
    {"Name": "prince", "Marks": 745},
    {"Name": "ballu", "Marks": 445},
    {"Name": "kush", "Marks": 435},
    {"Name": "kush" },
    {"Name": "kush", "Marks": 555}
]

df = pd.DataFrame(data)

#print(df)

# Print only the first 5 rows  solution 1
#print(df.iloc[:5])
#solutio 2 =display the last 3 row
#print(df.iloc[-3:])   #using position

#find total number of rows
#print(df.shape)
#soluton 4 dimension
#print(df.ndim)

#solutio 6 strutural information
#print(df.info)
print(df.describe())
print(df.isna())
print(df.isna().any())