#Generate Fibonacci series
num=int(input("Number of terms:"))
a=0
b=1
for i in range(num):
    print(a,"\t")
    c=a+b
    a=b
    b=c    