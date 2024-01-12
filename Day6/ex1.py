#Given a list
friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]

#a: length of a list
print(f"Length of the list: {len(friends)}")

#b: pick out the first, middle, and last member
#and check their type
print(friends[0])
print(friends[1])
print(friends[-1])

print("Type: ")
print(f"{type(friends[0])}")
print(f"{type(friends[1])}")
print(f"{type(friends[-1])}")

#c: enter a new name and gender, then add to the list
name = input("Enter new name: ")
gender = input("Enter new gender: ")
tup1 = (name, gender)
friends.append(tup1)
print(friends)

