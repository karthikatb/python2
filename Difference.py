#Differenc between largest and smallest number.
num=list(map(int,input("Enter the elements in the list:").split()))
largest=max(num)
print("Largest=",largest)
smallest=min(num)
print("Smallest=",smallest)
print("Difference=",largest-smallest)
