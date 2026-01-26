# Find common elements between two lists
print("Enter the elements in first list")
list1=[]
n1=int((input("Enter the number of elements:")))
for i in range(n1):
    num=int(input())
    list1.append(num)
print("-----------------------------")    
print("Enter the elements in second list")  
list2=[]  
n2=int(input("Enter the number of elements:"))
for i in range(n2):
    n=int(input())
    list2.append(n)
print("common elements")
common=[]
for i in list1:
    for j in list2:
        if (i==j and i not in common):
            common.append(i)
for i in common:
    print(i)                




