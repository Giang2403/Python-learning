#Enter a list of integers and print out double of that integers using list
#Cách 1:
n = int(input("Enter number of intergers: "))
lst = []
for i in range(n):
    lst.append(int(input("Enter number: ")))
print(lst)
new_lst = [v*2 for v in lst]
print(new_lst)

#Cách 2:
lst2 = list(map(int, input("Enter list of intergers: ").split()))
new_lst2 = [v*2 for v in lst2] 
print(new_lst2)
