n=int(input("Enter the number:"))
student={}
for _ in range(n):
    name,*line=input().split()
    score=list(map(float,line))
    student[name]=score
    

query_name=input() 
result=0
count=0
for i in student[query_name]:
    result+=i
    count+=1
average=result/count 
print(f"{average}:.2f") 
    

 
