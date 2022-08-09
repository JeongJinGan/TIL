from pprint import pprint
import sys

sys.stdin = open("Notion21.txt", "r")

N, M = map(int, input().split())
N += 1
list_ = [[] for _ in range(N)]
matrix = [[0] * N  for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1

    list_[u].append(v)
    list_[v].append(u)

pprint(matrix)
print(list_)