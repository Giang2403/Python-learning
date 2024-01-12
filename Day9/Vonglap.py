#for
for _ in range(5):
    print("Hello World!")

#list slicing
lst = list(range(0,5))      #0, 1, 2, 3, 4
print(lst)
lst = list(range(1,21,2))   #from 1 -> 20, step =2
print(lst)
lst = list(range(-4))       #from 0 -> -4, step =1 -> emtpy
print(lst)

for i in range(1,21):
    if i % 2 == 0:
        print(i, end = ' ')

#while
s = input("> ")
while s != 'q':
    print("Hello")
    s = input("> ")

#Break: exit the current loop
for i in range(1,21):
    if i>5:
        break
    print(i, end = ' ')

#Continue: skip the remaining codes and continue next loop
for i in range(1,21):
    if i%2==0:
        continue
    print(i, end = ' ')

#Else with for: when don't meet break in for
for i in range (1,21):
    if i==21:
        break
    print(i, end = ' ')
else:
    print("Don't have 21")