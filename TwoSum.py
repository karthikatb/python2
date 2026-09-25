n=int(input("Enter the size: "))
'''
num=[]
for i in range(n):
    i=int(input())
    num.append(i)
print(num) 
result=[] 
target=int(input("Enter the target: "))  
for i in range(n):
    
    for j in range (i+1,n):
        if (num[i]+num[j]==target):
            
            result.append(i)
            result.append(j)
print(result)            

'''
nums={}
target=int(input("Enter the target: ")) 
print("Ente the key and value")
for i in range (n):
    key=int(input())
    value=int(input())
    nums[key]=i
for key in nums:
    diff=target-key
    if diff  in nums:
        print(nums[key],nums[diff])


        
        