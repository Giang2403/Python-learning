#Đếm số các số nguyên tố trong khoảng 1->100
c = 0
for i in range(2,101):
    count = 0
    for j in range(1, i):
        if i%j==0:
            count+=1
    if count ==1:
        c+=1

print(c)
