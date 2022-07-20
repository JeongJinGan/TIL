class Person:


    # 클래스 변수(속성)
    species = '사람'

    # 인스턴스 메소드
    # 인스턴스가 활용할 메소드
    def greetring(self):
        print('안녕')

iu = Person()
iu.greetring()  # () 메소드 호출

# 클래스 변수(속성)
print(Person.species)
print(type(Person))