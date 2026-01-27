#Create a dictionary of student marks
def dictionary(n):
    student={}
    for i in range(n):
        name=input("Enter the name of the student:")
        mark=int(input("Enter the mark:"))
        student[name]=mark
    return student
n=int(input("enter the number of student:"))
result=dictionary(n)
print(result)

