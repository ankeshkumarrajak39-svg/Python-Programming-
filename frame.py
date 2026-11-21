import pandas as pd 
data={
  "Name": ["Ankesh","abhi","ballu"],
  "Marks":[20,40,0],
  "age":[20,34,55]

}
df=pd.DataFrame(data)
#print(df)
#important methid od dataframe
#print(df.shape)
#print(df.ndim)  #output 2
#print(df.size)
#print(df.columns)
#print(df.index)
#print(df.dtypes)
#print(df.values)
print(df.describe())
#print(df.info())
#print(df.axes)
#print(df.T)  #conver row -->col
