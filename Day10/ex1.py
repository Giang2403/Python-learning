#Đếm số chẵn và lẻ trong [0, 1000] theo 2 cách: thông thường và list comprehension
chan = 0
le = 0
for i in range(0,1001):
    if i%2==0:
        chan+=1
    else:
        le+=1
print(f"{chan} so chan, {le} so le")


lst = list(range(0,1001))
lchan = [v for v in lst if v%2==0]
lle = [v for v in lst if v%2==1]

print(f"{len(lchan)} so chan, {len(lle)} so le")