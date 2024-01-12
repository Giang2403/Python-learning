#Name of class must be capitalize
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #dunder method
    def __str__(self):
        return f"Student name: {self.name}, age: {self.age}"
    
    def __gt__(self, other):
        return self.age > other.age

student_one = Student("Bop", 23)
print(student_one.name)
print(student_one.age)
print(student_one)
student_two = Student("Giang", 30)
print(student_two)

#Calling function
print(student_one.__gt__(student_two))
print(student_two.__gt__(student_one))
print(Student.__gt__(student_one, student_two))

class People:
    def __init__(self, birth_year):
        self.birth_year = birth_year
    
    @property
    def get_age(self):
        return 2023-self.birth_year
    
people1 = People(1992)
age = people1.get_age
print(age)