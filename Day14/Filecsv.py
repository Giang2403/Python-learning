#Đọc file

"""
#Cách 1
with open("wages_by_education.csv", mode = "r") as file:
    for line in file:
        print(line.strip())     #Xóa dòng thừa

with open("market_data.csv", mode = "r") as file:
    for line in file:
        print(line)
"""

#Cách 2
import csv
import json
with open("wages_by_education.csv", mode = "r") as file:
    csv_file = csv.DictReader(file)             #list of dictionaries
    lst = list(csv_file)
    print(json.dumps(lst, indent=4))
    for item in lst:
        print(item)