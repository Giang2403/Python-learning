
def my_func(msg):
    print(msg)

my_func("Hello")

#Tham số mặc định phải để cuối cùng
def show_full_name(fname, lname = "Doe"):
    print(f"{fname} {lname}")

show_full_name("John")
show_full_name("John", "Ken")
show_full_name(lname="Allister", fname="Max") #Truyền tham số theo tên

#Hàm trả về gtri
def get_full_name(fname, lname = "Doe"):
    if fname:
        return f"{fname} {lname}"
    else:
        return f"Kenedy {lname}" 

full_name = get_full_name("John")
print(full_name)
full_name = get_full_name("")
print(full_name)

def add(x, y=40):
    return x+y

print(add(10))
print(add(10, 50))
#print(add(y=50)) lỗi vì thiếu x
print(add(y=10, x=100))

def func(lst=[]):
    lst.append(2)
    print(lst)

lst=[]
func()
func()

#Lamda function
print((lambda x,y: x+y)(1,2))
mul = lambda x,y: x*y
print(mul(1,2))

#First class function
def greet(msg):
    print("Hello " + msg)
hello = greet
hello("Jen")

#*args: tuple, tập hợp tất cả các đối số
def add(*args):
    print(type(args))
    return sum(args)

print(add(1,2,3,4))
lst=[1,2,3,4]
print(*lst)

lst = [1,2,3,4,5,6]
first, *mid, last = lst
print(first) #1
print(mid) #2, 3, 4, 5
print(last) #6
*first, last =  lst
print(first) #1,2,3,4,5
print(last) #6

def f(*lst, operation):
    return operation(lst)

print(f(1,2,3,4,operation=sum))