nums=[1, -2, 3, 4, -1, 2, 1, -5, 4]
current_sum=nums[0]
max_sum=nums[0]
for i in nums:
    current_sum=max(i,current_sum+i)
    if(current_sum>max_sum):
        max_sum=current_sum

print("largest=",max_sum)        