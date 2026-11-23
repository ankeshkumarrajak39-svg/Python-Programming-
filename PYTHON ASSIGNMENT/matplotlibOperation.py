import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
df =pd.read_csv("food_delivery.csv")



# #1====Bar Chart: Display city-wise total revenue.
# city =df.groupby("City")["Order_Amount"].sum()
# mycolors=["orange","pink","grey","blue","green","yellow"]
# plt.xlabel("City_Name")
# plt.ylabel("Order_Amount")
# plt.legend()
# plt.bar(city.index,city.values,color=mycolors)
# plt.show()




# 2===Pie Chart: Display the percentage of orders for each food category.



# Pie Chart: Percentage of orders for each food category

# city = df["Food_Category"].value_counts()

# mycolors = ["orange", "pink", "grey", "blue", "green", "yellow"]

# plt.title("Percentage of Orders for Each Food Category")

# plt.pie(
#     city,
#     labels=city.index,
#     colors=mycolors,
#     #autopct="%1.1f%%",
#     #startangle=90
# )

# plt.show()



#  3--Histogram: Show the distribution of delivery times.
# delivery_time =df["Delivery_Time"]
# plt.hist(delivery_time,bins=10,color="orange",
#  edgecolor="black")
# plt.show()




#4 Scatter Plot: Show the relationship between order amount and delivery time


# Order_Amount=df["Order_Amount"]
# delivery_time=df["Delivery_Time"]
# plt.scatter(Order_Amount, delivery_time, color="blue", marker="o")
# plt.show()



#5===5. Line Chart: Display order amounts against Order IDs.
# Order_Amount=df["Order_Amount"]
# Order_Id=df["Order_ID"]
# plt.plot(Order_Amount,Order_Id)
# plt.show()



#6 -- Horizontal Bar Chart: Compare the total number of orders in different cities.

city = df["City"].value_counts()
plt.barh(city.index, city.values, color="orange")
plt.show()