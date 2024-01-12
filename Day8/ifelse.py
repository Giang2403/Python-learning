if 1>0:
    print("1>0")
else:
    print("1<0")

n = int(input("n = "))
if n>0:
    print("So duong")
elif n<0:
    print("So am")
else:
    print("So 0")

print("n chia het cho 3" if n%3==0 else "n ko chia het cho 3")
a = int(input("a = "))
b = int(input("b = "))
print(a if a>b else b)
