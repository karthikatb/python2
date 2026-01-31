#Given comma-separated numbers and an index i,write a program to print the largest number among the numbers from the given 
# index i to the end of the list
num=list(map(int,input("Enter the list").split()))
index=int(input("index:"))
largest=num[index]
for i in range(index,len(num)):
    print(num[i],end=" ")
    if num[i]>largest:
        largest=num[i]
print("Largest=",largest)        
