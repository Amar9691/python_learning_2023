row = int(input("Enter Number of rows you want to print "))

for i in range(1,row+1) :
    # For space
    for j in range(1,row+1-i) :
        print(" ", end = " ")

    # decresing loop 
    for j in range(i,0,-1) :
        print(j , end = " ")

    for j in range(2,i+1) :
        print(j, end = " ")
    
    print()