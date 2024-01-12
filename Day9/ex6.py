#nhap vao so nguyen n, tinh so so chan va le trong doan [0, n]
n = int(input("Nhap so n: "))
chan = 0
le = 0
for i in range (0, n+1):
    if i%2==0:
        chan +=1
    else:
        le +=1
print(f"Số số chẵn: {chan}, số số lẻ: {le}")