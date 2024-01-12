class Human:
    count = 0
    def __init__(self, name):
        self.name = name
        Human.count +=1     #Đếm số đối tượng
"""
#Inheritance    
class Student(Human):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name} \n Age: {self.age}"

student_one = Student("Joe",33)
print(student_one)
"""

class Student:
    def __init__(self, name = "Bop"):
        self.name = name
    
    def __repr__(self):
        return f"Name: {self.name}"
    
    #def __str__(self):
        #return f"Str: Name: {self.name}"
    
s1 = Student()          #Khởi tạo mặc định
print(s1.name)
s2 = Student("Joe")
print(s2.name)
print(s2)

#Đếm số object
human1 = Human("Giang")
print(Human.count)
human2 = Human("Bop")
print(Human.count)