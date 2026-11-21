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

city = df["Food_Category"].value_counts()
mycolors=["orange","pink","grey","blue","green","yellow"]

plt.legend()
plt.title("percentage of orders for each food category.")
plt.pie(city,labels=city.index)
plt.show()



