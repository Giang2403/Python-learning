"""""
2. Create an empty set name "set_a"
a) Add "Anna" to set_a
b) Add a tuple ("Kenny", "Jen", "Danny")
c) Print out set_a and its length
d) Remove "Jen" from set_a
e) Clear set a
"""

set_a = set()
set_a.add("Anna")
print(set_a)
tup = "Kenny", "Jen", "Danny"
set_a.update(tup)
print(set_a)
print(f"Length of set_a: {len(set_a)}")
set_a.remove("Jen")
print(set_a)
set_a.clear()
print(set_a)
