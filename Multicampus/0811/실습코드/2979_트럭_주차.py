import sys

sys.stdin = open("2979.txt", "r")

A, B, C = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(3)]
# print(matrix) # [[1, 6], [3, 5], [2, 8]]  

max_ = max(matrix[0][1], matrix[1][1], matrix[2][1])

result = [0] * (max_)

for truck in matrix:
    for j in range(truck[0], truck[1]):
        result[j] += 1

# print(result) # [0, 1, 2, 3, 3, 2, 1, 1]

sum_ = 0
for num in result:
    if num == 1: 
        sum_ += A
    elif num == 2: 
        sum_ += 2 * B
    elif num == 3: 
        sum_ += + 3 * C

print(sum_)