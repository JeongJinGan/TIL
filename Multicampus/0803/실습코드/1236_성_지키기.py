import sys

sys.stdin = open("1236.txt", "r")

N, M = map(int, input().split())
row_cnt, col_cnt = 0 ,0
matrix = [list(input()) for _ in range(N)]

# 행 순회 하면서 x 없는 곳 찾기
for i in range(N):
    if 'X' not in matrix[i]:
        row_cnt += 1

# 열 순회 하면서 x 없는 곳 찾기
for j in range(M):
    if 'X' not in [matrix[i][j] for i in range(N)]:
        col_cnt += 1 

print(max(row_cnt, col_cnt))