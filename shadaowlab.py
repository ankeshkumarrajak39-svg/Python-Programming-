# import matplotlib.pyplot as plt
# import numpy as np 
# import pandas as pd
# # x=[1,3,4,5]
# # y=[2,4,6,3]
# # plt.plot(x,y)
# # plt.show()

# # y=np.array([35,25,25,15])
# # mylabels=["Apple","Banana","cherries","Date"]
# # mycolors=["black","hotpink","b"]
# # myexplode=[0,0.3,0,0]
# # plt.pie(y,labels=mylabels,explode=myexplode,shadow=True)
# # plt.legend(title="four fruits") #to add list of a color
# # plt.show()


# # dataframe 

# details={
#   "Name": ["Ankesh","abhi","ballu" "abhay"],
#   "Marks":[90,77,88]
# }
# x=pd.DataFrame(details["Name"])
# y=pd.DataFrame(details["Marks"])
# plt.bar(x,y)
# plt.shadow()




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# # Data
# details = {
#     "Name": ["Ankesh", "abhi", "ballu", "abhay"],
#     "Marks": [90, 77, 88, 95]
# }

# # Create DataFrame
# df = pd.DataFrame(details)

# # Bar chart
# # plt.bar(df["Name"], df["Marks"])

# # # Labels and title
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("Student Performance")

# # # Grid
# # plt.grid(axis="y", linestyle="--", alpha=0.5)
# mycolors=["grey","green","pink"]
# # plt.bar(df["Name"], df["Marks"],color=mycolors)
# plt.scatter(df["Name"],df["Marks"])
# plt.show()


#wap using matplotlib to create a sccatter plot that compare the study hours and marks of girl and boys 
#instruction --create a scatter plot for boys using blue color and girl red color and appropiate labels to the x acces nad y acces and title gVs b performance use label to identify girl and boys 
