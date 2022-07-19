class Person:

    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age 
        self.gender = gender

    def info(self):
        return (self.name, self.age, self.gender)

hong = Person('홍길동', 100, 'M')
ko = Person('고길동', 40, 'M')

print(hong.info())
print(hong.name)
print(hong.age)
print(type(hong))


# class Person:
#     def __init__(self, name):
#         self.name = name

# person1 = Person('지민')
# print(person1.name)