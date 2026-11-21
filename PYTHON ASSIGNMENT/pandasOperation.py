import pandas as pd
#solution 1
# Load the CSV dataset using Pandas.
df=pd.read_csv("food_delivery.csv")
# print(df)

#solution 2
# Display the first five and last five records.
# print(df.head(5))
# print(df.tail(5))


# #solution 3
# # Display the number of rows and columns.
# print(df.shape)



#solution 4
# Check the data types of all columns.
# print(df.dtypes)

# solution 5
#solution 6



# # solution 7
# # Calculate the average customer rating
# print(df["Rating"].mean())


#solution 8
# # Find the most popular food category.
# maxRating = df["Rating"].max()
# print(maxRating)
# print(pd.df("Rating")==maxRating)

print(df[df["Rating"]==df["Rating"].max()])




#solution 9
# Calculate city-wise total revenue.

# print(df["Food_Category"].value_counts())
# print(df["City"].value_counts().sum())
# print(df.groupby("City")["Order_Amount"].sum())




#solution 10

# Calculate category-wise average order amount.
# print(df.groupby("Food_Category")["Order_Amount"].mean())