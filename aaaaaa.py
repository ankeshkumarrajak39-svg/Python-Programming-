import numpy as np
arr=np.array([
  [[1,3,2],[3,4,6]],
  [[5,7,6],[7,8,9]]
])
print(arr)
print(arr.ndim)

print(arr.shape)    #no of colom and rows

print(arr.size)

print(arr.dtype) 

a=np.identity(3)       #identity matrix
print(a)

x=np.array([2,4,5,67,0])
y=np.array([1,2,34,5,8])
print(x+y)
print(x-y)
print(y-x)
print(x*y)
print(x%y)
