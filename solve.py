# import pandas as pd

# data = { 
#     "Name":["x","y","z"],
#     "Marks":[60,70,80]
# }

# df = pd.DataFrame(data)

# df["Bonus"] = 5

# df["FinalMarks"] = df["Marks"] + 5 

# print(df)

# a = df["Marks"].sum()
# print(a)
# b = df["Marks"].mean()
# print(b)
# c = df["Marks"].median()
# print(c)
# d = df["Marks"].mode()
# print(d)
# e = df["Marks"].min()
# print(e)
# f =df["Marks"].max()
# print(f)
# g = df["Marks"].count()
# print(g)
# h = df["Marks"].std()
# print(h)
# i = df["Marks"].var()
# print(i)
# j = df["Marks"].prod()
# print(j)
# k = df["Marks"].cumsum()
# print(k)
# j = df["Marks"].cumprod()
# print(j)
# k = df["Marks"].abs()
# print(k)
# l = df["Marks"].round()
# print(l)

import pandas as pd

data = {
    "Name": ["Ankesh", "Rahul", "Amit"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)


 print(df)

 #solution 1==>
 print(df.iloc[:3])