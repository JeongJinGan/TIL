class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age =age
        self.gpa = gpa

s1 = Student('학생1', 26, 4.5)
s1.talk()        