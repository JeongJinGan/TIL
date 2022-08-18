import sys

sys.stdin = open("1926.txt", "r")


# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# ------------------------------------------------------------------------

def bfs(x, y):
    w = 1
    queue = [(x, y)]
    while queue:
        x, y = queue.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 1 and not visited[nx][ny]:
                    w += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return w
# ---------------------------------------------------------------------------------------------

N, M = map(int, (input().split()))

matrix = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
# ---------------------------------------------------------------------------------------------

cnt, area = 0, 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            cnt += 1
            visited[i][j] = True
            area = max(area, bfs(i, j))
# ----------------------------------------------------

print(cnt)
print(area)









