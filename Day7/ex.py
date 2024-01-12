"""
Given 2 set
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}
a) Find people who study both art and math
b) Find people who study art but not math
c) Find people who study math but not art
d) Find people who study only 1 subject
e) Find all the people
"""
art = {"John", "Max", "Anna", "Bob", "Obito"}
math = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

#a
a = art.intersection(math)
print(a)
print(art & math)

#b
b = art.difference(math)
print(b)
print(art - math)

#c
c = math.difference(art)
print(c)
print(math - art)

#d
d = art.symmetric_difference(math)
print(d)
print(art ^ math)

#e
e = art.union(math)
print(e)
print(art | math)