#eval: return number of a string
print(eval("1+2"))
print(eval("1+2**4"))
lst = map(eval, input("Enter number: ").split())
print(*lst)
a = 2
print(eval("a"))
print(eval("a+2"))