import sys

sys.stdin = open("2669.txt", "r")

matrix = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2): # 입력 받은 x1, x2 순회
        for j in range(y1, y2): # 입력 받은 y1, y2 순회
            matrix[i][j] = 1 # 순회한 값들 1로 변환

# pythonic한 방법
print(sum(map(sum, matrix)))




