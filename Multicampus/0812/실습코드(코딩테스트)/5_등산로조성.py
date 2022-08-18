import sys

sys.stdin = open("_등산로조성.txt")


def dfs(x, y):
    # 방향탐색(dx, dy)
    for i in range(4):  
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위, 다음 방문이 지금보다 작은지, 방문체크
        if 0 <= nx < N and 0 <= ny < N and matrix[x][y] > matrix[nx][ny] and not visited[nx][ny]:
            print()


    return





T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_high = []
    for i in range(N):
        max_high.append(max(matrix[i]))
    max_ = max(max_high)

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문처리
    visited = [[0 for _ in range(N)] for _ in range(N)] 

    for x in range(N):
        for y in range(N):
            # matrix 순회하면서 최고 봉우리가 아니라면 넘어감
            if matrix[x][y] != max_:
                continue
            visited[x][y] = 1 # 방문체크
            dfs(x, y)