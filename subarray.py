list=[1,3,-4-8-9,76,1]
sum=0
ans=0
for i in list:
  for j in range(i, len(list)):
   sum+=list[j]
   ans=max(ans,sum)
print(sum)