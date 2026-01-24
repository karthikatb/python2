#: Remove duplicates from a list
n=int(input("Enter the number of list:"))
numbers=[]
unique=[]
for i in range(n):
    num=int(input())
    numbers.append(num)
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)    