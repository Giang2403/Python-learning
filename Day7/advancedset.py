set1 = {1, 4, 3 ,2}
set2 = {2,3,10,-10}
#intersection
set3 = set1.intersection(set2)
print(set3)
print(set1&set2)

#difference
set3 = set1.difference(set2)
print(set3)
print(set1-set2)
set3 = set2.difference(set1)
print(set3)

#union
set3 = set1.union(set2)
print(set3)
print(set1|set2)
set3 ={10, 11, 20}
set4=set1.union(set2).union(set3)
print(set4)
print(set1|set2|set3)

#symmetric_difference
set3=set1.symmetric_difference(set2)
print(set3)
print(set1^set2)
