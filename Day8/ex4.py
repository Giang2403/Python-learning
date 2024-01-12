#Biện luận phương trình ax + b = 0
print("Phương trình ax + b = 0")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
if a == 0:
    if b == 0:
        print("Equation has infinite solutions")
    else:
        print("Equation doesn't have any solution")
else:
    print(f"Equation has 1 solution x = {round(-b/a, 2)}")