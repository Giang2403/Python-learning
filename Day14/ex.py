"""
Tạo menu có chức năng quản lý sách
a) Thêm 1 cuốn sách
b) Hiển thị tất cả các cuốn sách
c) Xóa sách theo id
d) Tìm sách theo id
dữ liệu sách được lưu trong file json
"""
import json
user_menu = """
Choose:
    "1": Add a book
    "2": Show all book
    "3": Delete book according to ID
    "4": Find book by ID
    "5": Exit
Enter your choice: 
"""
count = 0
book_file = "book_infor.json"
prevs = set()
try:
    with open("book_infor.json", "x") as file:
        json.dump([], file)
except FileExistsError:
    pass

def Add():
    global count
    name = input("Enter book's name: ").title().strip()
    while name in prevs:
        print("This book is already in the list, enter another!")
        name = input("Enter a book' name: ").title().strip()

    prevs.add(name)
    count += 1
    book = {
        "name": name,
        "ID": count
    }
    with open("book_infor.json", mode = "r") as file:
        lst = json.load(file)
        lst.append(book)
    with open("book_infor.json", mode = "w") as file:
        json.dump(lst, file, indent=4)

Add()
Add()
Add()
