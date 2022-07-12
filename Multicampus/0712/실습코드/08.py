numbers = [0, 20, 100]
first = numbers[0]
second = numbers[0]

for num in numbers:
    if num > first:
        second = first
        first = num
    if second < num and num < first:
        second = num
print(second)