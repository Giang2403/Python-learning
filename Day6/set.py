#khoi tao
set1=set()      #empty set
set1.add(1)
set1.add(1)
set1.add(1)
print(set1)

#update
set1.update([2, 3, 4, 5])
print(set1)

#remove value
set1.remove(1)
print(set1)

#copy
set2=set1.copy
print(set1 is set2)
print(set1 == set2)
set1.clear()
print(set1)
set1 = {1, 2, 3, 4}
value = set1.pop()
print(value)
