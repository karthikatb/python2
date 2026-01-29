#write a program to print the Kth largest number in the list.
num=list(map(int,input("Enter the number:").split()))
k=int(input("Enter the key:"))
rank=[]
num.sort(reverse=True)
print(num)
print(" Kth largest number in the list:",num[k-1])