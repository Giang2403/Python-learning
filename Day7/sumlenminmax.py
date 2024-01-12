#len: return length of object
lst = ['a', 'b', 'c', 'd']
print(len(lst))
lst = set()
print(len(lst))

#min max: error when emtpy list, only use in list with numbers
lst = [1, 2, 3, 4]
print(min(lst))
print(max(lst))

#join: transform list -> string, list must be str
lst = ['a', 'b', 'c', 'd']
s = ''.join(lst)
print(s)
s = ' '.join(lst)
print(s)
lst2 = [1, 2, 3, 4]
s = ''.join(map(str, lst2))
print(s)
s = ' '.join(map(str, lst2))
print(s)