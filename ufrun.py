# create ufunc 
import numpy as np

def sum(a,b):
    return a + b

myFun = np.frompyfunc(sum,2,1)

arr1 = [1,2,3,4]
arr2 = [5,6,7,8]

print(myFun(arr1,arr2))

def Main():
    pass

print(__name__ == '__main__')


