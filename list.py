import pandas as pd 
  data = [
    ["Arman",21,85],
    ["Riya",33,55],
    ["ak",99,0]
  ]
  df=pd.DataFrame(
    data,
    columns=["Name","age","Marks"]
  )
  print(df)

#from list of dictionary
