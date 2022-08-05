import sys

sys.stdin = open("1652.txt", "r")

result =[0] * 2

T = int(input())
matrix = []
for _ in range(T):
    matrix.append(list(input()))

for i in range(T):
    cnt_row, cnt_col = 0, 0
    for j in range(T):
        if matrix[i][j] == '.':
            cnt_row += 1
        elif matrix[i][j] == 'X':
            if cnt_row >= 2:
                result[0] += 1
            cnt_row = 0

        if matrix[j][i] == '.':
            cnt_col += 1
        elif matrix[j][i] == 'X':
            if cnt_col >= 2:
                result[1] += 1
            cnt_col = 0

        if j == T-1:
            if cnt_row >= 2:
                result[0] += 1
            if cnt_col >= 2:
                result[1] += 1
        
print(*result)




