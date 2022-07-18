# numbers = input().split()
# print(sum(numbers))

# int 형을 문자열과 합할 수 없다.
# map을 통해 입력받을때, int로 받는다.

numbers = map(int, input().split())
print(sum(numbers))