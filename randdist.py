from numpy import random

# generate random number based on probablity 

dist = random.choice([1,2,3,4],p=[0.6,0.2,0.1,0.1],size=100)


print(dist)