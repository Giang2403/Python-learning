print("List")
lst = [4,100,5,6]
for value in lst:
    print(value, end = " ")

print("\nTuple")
tup = (4,100,5,6)
for value in tup:
    print(value, end = " ")

print("\nSet")
set = {4, 100, 5, 6}
for value in set:
    print(value, end = " ")

print("\nDictionary")
d = {
    "a":1,
    "b":2,
    "c":3
}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, value)


#List comprehension
lst = [1, 2, 3, 4]
new_lst = [val*2 for val in lst]
print(new_lst)

#Set comprehension
set = {"a", "b", "c", "d"}
new_set = {s.upper() for s in set}
print(new_set)

#Dict comprehension
dict = {
    "a":1,
    "b":2,
    "c":3
}
new_d = {
    k+"1":v*2 for k, v in dict.items()
}
print(new_d)

#Zip: return tuples
lst1 = ["a", "b", "c"]
lst2 = [1, 2, 3, 4]
print(list(zip(lst1, lst2)))
lst3 = ("a1", "b1", "c1")
print(list(zip(lst1, lst2, lst3)))

#Enumerate: đánh số cho list, return tuples: (index, value)
lst = ["a", "b", "c"]
print(list(enumerate(lst)))
print(list(enumerate(lst, start = 1)))

numbers = [1, 2, 3, 4, 5, 6]
new_num = [v*2 if v%2==0 else v*3 for v in numbers]
print(new_num)
