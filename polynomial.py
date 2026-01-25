n=int(input("Enter the number of the list:"))
poly=[]
for i in range(n):
    num=int(input())
    poly.append(num)
for i in range (n):
      print(poly[i],"x^",i,end="")
      if (i!=n-1): 
       print("+",end="")

