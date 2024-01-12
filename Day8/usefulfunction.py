"""
#nhap 2 so tren cung 1 hang
a, b = map(int, input().split())
print(a if a<b else b)
"""

#print each members of a list
lst = [1, 2, 3, 4]
print(*lst)
print(*lst, sep="%")

#format
x = 2.4567
print(format(x, ".2f"))

#round: lam tron
print(round(x))             #nearest integer
print(round(x, 2))          #2 digits after .
print(round(x, 3))          #3 digits after .

#sorted: return sorted list
lst = [10, 1, 3, -2, 15]
lst2 = sorted(lst)
print(*lst2)
lst2 = sorted(lst, reverse=True)
print(*lst2)

#chr: return character of given ascii code
ascii_code = 97
print(chr(ascii_code))
print(chr(98))

#list:
s = "abcd"
print(list(s))

#divmode(a, b): tra ve thuong va du as tuple (thuong, du)
thuong, du = divmod(11,3)
print(thuong)
print(du)
print(divmod(11,3))
