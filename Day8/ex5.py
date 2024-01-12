#Giải và biện luận phương trình ax^2 + bx + c = 0
import math
print("Phương trình ax^2 + bx + c = 0")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a == 0:
    if b==0:
        if c ==0:
            print("Equation has infinite solutions")
        else:
            print("Equation doesn't have any solution")
    else:
        print(f"Equation has only 1 solution x = {round(-c/b, 2)}")
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("Equation doesn't have any solution")
    elif delta == 0:
        print(f"Equation has double solution: x = {round(-b/(2*a), 2)}")
    else:
        print(f"Equation has 2 solutions: {round((-b+math.sqrt(delta))/(2*a), 2)} and {round((-b-math.sqrt(delta))/(2*a), 2)}") 