import random

# n을 넣으면
# 그 횟수만큼
def generate_lotto(n):
    result = []
    for i in range(n):
        numbers = range(1,46)
        pick = random.sample(numbers, 6)
        pick.sort()
        result.append(pick)
    return result
def check(buy_numbers, result_numbers):
    return 0

#print(generate_lotto(3))    