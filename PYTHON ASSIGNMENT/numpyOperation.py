import numpy as np 
import pandas as pd 
df = pd.read_csv("food_delivery.csv")
# print(df )
# print(df.head())  

 #solution 1 of numpy operation 
 #convert a AMOUNT col into a array 
# order_array = df["Order_Amount"].to_numpy()
# print(order_array)


#solution 2 
# find total and average amout of order 
# ave_order_amount=np.average(df["Order_Amount"])
# print(ave_order_amount)


# #solution 3 
# print(np.max(df["Order_Amount"]))

# print(np.min(df["Order_Amount"]))



# #solution 4 
# # Calculate the standard deviation and variance.

# # Calculate variance
# variance = np.var(df["Order_Amount"])

# # Calculate standard deviation
# std_deviation = np.std(df["Order_Amount"])
# print(variance)
# print(std_deviation)



# # solution 5 
# #Calculate the average delivery time.
# delivery_time=np.average(df["Delivery_Time"])
# print(delivery_time)


#solution 6
# Count the number of orders with a rating of 4 or above.

# # rating =np.array(df["Rating"])
# # print(rating)
# count = (df["Rating"] >= 4).sum()

# print("Orders with rating 4 or above:", count)




#Solution 7
# Find all orders where the delivery time exceeds 40 minutes.

# delTime = np.array(df["Delivery_Time"])
# print(delTime)
# countOrder = (df["Delivery_Time"] > 40).sum()
# print(countOrder)


# deliveryTime=np.where(df["Delivery_Time"]>40)
# print(deliveryTime)
# print(df[df["Delivery_Time"]>40])




#solution 8
# Calculate the percentage of customers who gave a 5-star rating.
#using math

# FiveStar = np.array(df["Rating"] ==4).sum()
# print(FiveStar)
# total=np.array(df["Rating"]>-1).sum()
# print(total)
# percentage=((FiveStar/total)*100)
# print("percentage of rating 4 is ::",round(percentage,2),"%")



#solution 9
# Identify orders whose amount is greater than the average order amount.
# ave_order_amount=np.average(df["Order_Amount"])
# print(ave_order_amount)
# print(df[df["Order_Amount"]>ave_order_amount])
