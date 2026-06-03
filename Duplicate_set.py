def find_first_duplicate (num):
    seen=set()
    for i in num:
        if i not in seen:
            seen.add(i)
        else:
            return i
    return None    

size=int(input("Enter the size:"))
nums=list()
print("Ente the number")
for i in range(size):
    nums.append(int(input()))
print(nums)    
duplicate = find_first_duplicate(nums)
print("The first duplicate is:", duplicate)