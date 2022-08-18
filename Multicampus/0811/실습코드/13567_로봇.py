import sys

sys.stdin = open("13567.txt", "r")


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# ---------------------------------------------------------------------------------------------

N, M = map(int, (input().split()))

matrix = [[] for _ in range(N + 1)]

# for _ in range(M):
#     u, v = input().split()
#     matrix[u].append(v)
#     matrix[v].append(u)

print(matrix)
# ---------------------------------------------------------------------------------------------

stack = []



while len(stack) != 0:









