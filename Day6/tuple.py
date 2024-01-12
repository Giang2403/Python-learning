#Khoi tao
tup1 = 1, 2, 3
tup2 = (1, 2, 3)
tup3 = 1,
tup4 = (1,)
print(type(tup1))
print(type(tup2))
print(type(tup3))
print(type(tup4))

#access value
print(tup1[0])
print(tup1[-1])

#can not modify value
# tup1[0] = 100 : error

#Update
tup1 += (4,)
print(tup1)
tup1 += (5, 6, 7, 1)
print(tup1) 