#Khoi tao du lieu
import json
student = {
    "name" : "Bop",
    "age" : 23,
    "grades" : [45, 67, 90, 98, 99]
}
print(student)
print(json.dumps(student, indent = 4))

#Access to the value
value = student["name"]
print(value)
value = student["age"]
print(value)
value = student.get("name") #return value of key in dict
print(value)
value = student.get("id") #retunr default value if not have key in dict
print(value)
value = student.get("id", "SV001")
print(value)
print(student)

#Create new key
student["id"] = "SV001"
print(json.dumps(student, indent=4))

#Update value
student["name"] = "Jack"
print(json.dumps(student, indent =4))

#Update using update()
student.update(gender = "male", hobby = "sports")
print(json.dumps(student, indent = 4))

#Update using a dict
infor = {
    "class" : "7a0",
    "weight" : "80kg"
}
student.update(infor)
print(json.dumps(student, indent = 4))

#Update using a list tuple
infor2 = [("height", "170cm"), ("dream", "rich")]
student.update(infor2)
print(json.dumps(student, indent = 4))

#Delete value
value = student.pop("name") #return value and delete it
print(value)
print(json.dumps(student, indent = 4))

del student["age"]
print(json.dumps(student, indent = 4))

tup = student.popitem()
print(tup)
print(json.dumps(student, indent = 4))

#Create a list of keys
keys = list(student)
print(keys)

#Create a list of values
values = list(student.values())
print(values)

#Create a list of tuples (key, value)
items = list(student.items())
print(items)



