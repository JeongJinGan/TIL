import random

# 1 ~ 45 까지의 숫자
# 그중에 6개
n = int(input('몇개를 사실건가요?'))
for i in range(n):
    numbers = random.sample(range(1,46),6)
    numbers.sort()
    print(numbers, type(numbers))