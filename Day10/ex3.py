#Cho dict như sau
import json
people = {
    "Emma": 71,
    "Jack": 45,
    "Amy": 15,
    "Ben": 29 
}

#In ra người lớn tuổi nhất
max = 0
max_name = ""
for name, age in people.items():
    if age > max:
        max = age
        max_name = name
print(max_name)

#Tạo ra dict mới với tuổi nhân đôi
new_people = {
    name2: age2*2 
    for name2, age2 in people.items()
}
print(json.dumps(new_people, indent=4))

#Enumerate các key trong people dict
lst = list(enumerate(people))
print(lst)
dict = dict(enumerate(people))
print(dict)
