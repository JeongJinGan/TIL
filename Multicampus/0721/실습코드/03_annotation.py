# 동적 타입 언어인 파이썬에서
# 정적 타입으로 바꿔주는 것이 아니라
# 그냥 힌트, 그냥 노트


# 변수 어노테이션
a: int = 3
print(a)

# 함수 어노테이션
def add(x: int, y: int) -> int:
    return x + y
    
print(add(7, 4))
print(add('hi ','hello')) # int만 가능하진 않음

# 함수 어노테이션
def add2(x, y):
    return x + y
print(add(7, 4))