# 함수 내부에서 값을 쓰고 싶으면 어떻게 하냐?
# 정의할 때 이름을 지어놓고, 호출할 때 값을 넘겨준다.

class MyClass:
    class_variable = '클래스 변수'

    # 메소드들 정의
    def __init__(self) -> None:
        self.instance_variable = '인스턴스 변수'
    # 인스턴스 메소드
    def instance_method(self):
        return self, self.instance_variable
    # 클래스 메소드 정의
    @classmethod # 데코레이터 : 함수를 꾸며주는 건데 지금은 배우지 않음.
    def class_method(cls):
        return cls, cls.class_variable
    # 스태틱 메소드 정의
    @staticmethod
    def static_method():
        return ''


c1 = MyClass()
print('인스턴스 변수 호출', c1.instance_variable)
print('인스턴스 메소드 호출', c1.instance_method())
print('클래스 메소드 호출', c1.class_method())
print('스태틱 메소드 호출', c1.static_method())