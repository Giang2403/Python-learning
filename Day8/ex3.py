#Enter 2 number a, b print smaller number and larger number
a, b = map(int, input("Enter a and b: ").split())
if a>b:
    print(f"Smaller number: {b}")
    print(f"Larger number: {a}")
elif a<b:
    print(f"Smaller number: {a}")
    print(f"Larger number: {b}")
else: 
    print("a and b are equal")