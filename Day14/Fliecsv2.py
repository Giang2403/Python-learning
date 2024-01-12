#Ghi file
import csv
header = ["id", "name", "age"]
student1 = ["SV001", "Bop", 23]
student2 = ["SV002", "Hihi", 30]
with open("test1.csv", mode = "w", newline='') as file:             #thêm newline='' để bỏ dòng thừa
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)
    csv_writer.writerow(student1)
    csv_writer.writerow(student2) 