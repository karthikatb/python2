# Find the largest element in a list
n=int(input("Enter the length of the list:"))
numbers=[]
for i in range(n):
    num=int(input("Enter the number"))
    numbers.append(num)
largest=numbers[0]
for li in numbers:
    if li>largest:
        largest=li
print(largest)
