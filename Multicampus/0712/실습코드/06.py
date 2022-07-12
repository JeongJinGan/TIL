numbers = [-100, -60, -6]
max = numbers[0]
#max = float("-inf") 파이썬 최솟값
for a in numbers:
    if max < a:
        max = a
print(max)