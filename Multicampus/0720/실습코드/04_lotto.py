import random
for i in range(5):
    numbers = range(1,46)
    result = random.sample(numbers, 6)
    result.sort()
    print(result)