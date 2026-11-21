import pandas as pd

df = pd.read_csv("annex1.csv")

print(df)
print(df["Item Name"])

# print(df["Item Name"].sum())
# print(df["Item Name"].mean())
# print(df["Item Name"].median())
# print(df["Item Name"].mode())
# print(df["Item Name"].min())
# print(df["Item Name"].max())
# print(df["Item Name"].count())
# print(df["Item Name"].std())
# print(df["Item Name"].var())
# print(df["Item Name"].prod())
# print(df["Item Name"].cumsum())
# print(df["Item Name"].cumprod())
#numeriacal operation 
import pandas as pd

df = pd.read_csv("annex1.csv")

print(df["Item Name"])              # All product names
print(df["Item Name"].count())      # Total non-empty values
print(df["Item Name"].mode())       # Most frequent product
print(df["Item Name"].min())        # Alphabetically smallest
print(df["Item Name"].max())        # Alphabetically largest
print(df["Item Name"].value_counts()) # Count of each product
print(df["Item Name"].unique())     # Unique product names
print(df["Item Name"].nunique())    # Number of unique products

# question 1 ==> dispaly the third row using iloc at 5 marks to every student and store them in a new colom named updatede marks display student whoes scroring betcween 70 and 90 marks dispaly record whoes name start with a replace missing ages with 20 create a result col containing for marks greater than or equal 40 otherwise fail 
# create a grad col A for marks >=90
# B--marks>80 but below 90
# c---> marks>=70 but below 80
# d--> marks<70
#  question 2----->>>>>dispaly only student with grad A and B 

#  question3-->> dispaly the toper name and percentage
#  question 4 ---> find the average marks of each student 
#  question 5=== save the final report to student performance.csv(df.to_csv("output.csv",index=false))
