"""""
from copy import deepcopy
lst = [[1, [2, 3]], (2, 4)]
lst1 = lst.copy
lst2 = deepcopy(lst)
lst[0][1].append(100)
print(lst1)
"""

# isinstance
print(isinstance(3, int))
print(isinstance(3, float))
print(isinstance(True, int))

# ord: return ascii code of char
print(ord('1'))
print(ord('1') ^ ord('3'))

#abs: absolute
print(abs(-1))
print(abs(True))
print(abs(-True))
print(abs(1+2j))

#repr: print ""
print(repr('a'))
print(f"{'a'!r}")