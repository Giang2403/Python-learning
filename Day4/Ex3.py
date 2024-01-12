students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]

#a Take out the information of the first student and
#print out as ID: id, name: name, age: age
id = students[0][0]
name = students[0][1]
age = students[0][2]
print(f"ID: {id}, name: {name}, age: {age}")

#b Take out the age of 2nd student
age2 = students[1][2]
print(f"Age of the 2nd student: {age2}")

#c Take out information of the last 2 student:
print(f"The last 2 students: {students[1:]}")

#d Take out id of the 3rd student
id3 = students[2][0]
print(f"The id of 3rd student: {id3}")
