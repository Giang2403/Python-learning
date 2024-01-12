#Nhap vao so nguyen duong n, tinh tong cac chu so
n = int(input("Enter number: "))
tong = 0
while n != 0:
    tong = tong + (n % 10)
    n = int(n/10)
print(tong)