def check_right_triangle(sides):
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        return True
    return False
sides=[]
sides.append(int(input("enter side 1:")))
sides.append(int(input("enter side 2:")))
sides.append(int(input("enter side 3:")))
if check_right_triangle(sides):
    print("the given sides are part of the right triangle")
else:
    print("the given sides are not part of right triangle")
