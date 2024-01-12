friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]

#a: pick the first 4 members
lst = friends[0:4]
print(f"The first 4 friends are: {lst}")

#b: pick the last 4 members
lst = friends[::-1]
print(f"The last 4 friends are: {lst[0:4]}")

#c: reverse the list
lst = friends[::-1]
print(f"The list after reverse: {lst}")

#d: take the friends from index 1 to end
lst = friends[1:]
print(f"The friends from 1 to end: {lst}")

#e: Copy to a new list
lst = friends[:]
print(f"The list after copy: {lst}")

#f: remove the 2 bound of the list
lst = friends[1:-1]
print(f"The list after remove: {lst}")