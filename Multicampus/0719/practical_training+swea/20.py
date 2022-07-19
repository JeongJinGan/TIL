number = 123456
num = 0
while number > 0:
    num += number%10
    number //=10
print(num)


# divmod(x,y)는 x를 y로 나누고,
# 결과를 tuple로 반환
# (몫, 나머지)
# 다른방법
# answer = 0
# while number > 0:
#     number, remainder = divmod(number, 10)
#     answer += remainder
# print(answer)