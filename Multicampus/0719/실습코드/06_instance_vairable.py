class Person:
    pass 


# Person 클래스의 인스턴스 iu
iu = Person()
# iu의 인스턴스 변수 할당
iu.name = '아이유'
iu.age = 28
iu.gender = 'F'
# 인스턴스 변수 접근
print(iu)
print(iu.name)

class Person:
    def __str__(self):
        return f'<{self.name}>'

# Person 클래스의 인스턴스 iu
iu = Person()
# iu의 인스턴스 변수 할당
iu.name = '아이유'
iu.age = 28
iu.gender = 'F'
print(iu)
print(iu.name)