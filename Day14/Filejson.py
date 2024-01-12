import json

"""
#Chưa chạy
#Đọc
with open("test.json", mode = "r") as file:
    lst = json.load(file)                       #load: đọc dữ liệu từ file, trả về list[dict], dict
    print(lst)
    print(json.dumps(lst, indent=4))
"""

#Ghi
student = [
    {
    "name": "Bop", 
    "age": 20
}, 
    {
        "name": "An",
        "age": 19
    }

]
with open("data1.json", mode = "w") as file:
    json.dump(student,file,indent=4)

student2 = {
    "name": "Phu",
    "age": 21
}
with open("data1.json", mode = "r") as file:
    lst = json.load(file)
    lst.append(student2)
with open("data1.json", mode = "w") as file:
    json.dump(lst,file,indent=4)
