# performing cummulative sum of array element
import numpy as np
arr = [1,2,3]
out = []
def  fact(i):
   if i < 0:
      return 0
   else:
      return arr[i] + fact(i-1)
for i in range(len(arr)):
    out.append(fact(i))
#print(out)

sum = []

for k,j in zip(arr,out):
    sum.append(k+j)

print(np.add(arr,out))