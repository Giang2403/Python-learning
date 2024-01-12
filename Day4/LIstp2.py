""""
#List in list
friends = [["Bop", 23], ["Jen", 34], ["Kenny", 56]]
print(type(friends))
print(type(friends[0]))
print(friends[1][0])
"""

""""
#Copy list
lst1 = [1, 2, 3]
lst2 = lst1
print(lst2 is lst1)
print(lst2 == lst1)
lst3 = lst1.copy()
print(lst3 is lst1)
print(lst3==lst1)
"""

#List slicing
a = [0, 1, 2, 3, 4, 5]
lst = a[0:2:1]
print(lst)
lst = a[:2]
print(lst)
lst = a[1:]
print(lst)
lst = a[:]  #copy
print(lst)
print(lst is a)
lst = a[::-1]   #reverse
print(lst)
lst = a[1:-1]   #remove 2 bound
print(lst)