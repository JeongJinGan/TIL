# map(함수, 반복가능한 것)
# 반복 가능한 것들의 모든 요소에 함수를 적용시킨 결과를
# map object로 반환한다.

# map(int, input().split())
# int 형 변환함수를
# input으로 받은 것을 쪼갠 결과인 리스트에 각각 적용한다.


# 3의 배수만 출력

# 기본 반복/조건 코드
# numbers = [1, 2, 5, 10, 3, 9, 12]
# result = []
# for number in numbers:
#     if number % 3 == 0:
#         result.append(number)
# print(result)

# map을 이용해서 코드 작성
# 함수를 정의해야 한다.
# *3을 해서 출력
numbers = [1, 2, 5, 10, 3, 9, 12]
result = []
for number in numbers:
    result.append(number*3)
print(result)

#---------위에코드는 기본/ 아래는 map사용
def multiple_3(number):
    return number * 3

print(list(map(multiple_3, numbers)))


# 이 함수는 계속 사용되지 않고, map에서만 사용된다.
# 일시적인 함수를 만들고 싶다. => lambda

# n : input , n*3 : output , 앞에는 lambda라고 적기
# 밑에 코드를 보고도 30번째줄 def로 읽을 줄 알아야 함
print(list(map(lambda n:n*3,numbers)))















