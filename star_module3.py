#increasing triangle
number=int(input("enter the number of row:"))
for i in range(number):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")
#decreasing triangle
number=int(input("enter the number of row:"))
for i in range(number,0,-1):
    for j in range(i,0,-1):
        print("*", end=" ")
    print(" ")
#hill pattern
number=int(input("enter the number of row :"))
for i in range(number):
    for j in range(number-i):
        print(" ",end=" ")
    for j in range((i*2)-1):
        print("*", end=" ")
    print(" ")
#reverse hill
number=int(input("enter the number of row :"))
for i in range(number,0,-1):
    for j in range(number-i,0,-1):
        print(" ",end=" ")
    for j in range((i*2)-1):
        print("*", end=" ")
    print("")



