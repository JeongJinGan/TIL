import sys

sys.stdin = open("11724.txt", "r")

# -----------------------------------
# dfs로 그래프를 탐색한다.
def dfs(x):

    #해당 노드 방문체크 한다.
    visited[x] = True

    # 해당 시작점을 기준으로 계속해서 dfs로 그래프를탐색한다.
    for i in matrix[x]:
        if visited[i] != True:
            dfs(i)

# -----------------------------------
# 무방향 그래프
N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    matrix[u].append(v)
    matrix[v].append(u)

print(matrix)
# -----------------------------------
# 방문처리
visited = [False] * (N + 1)
count = 0  # 컴포넌트 그래프 개수 저장

# -------------------------------------------
# 1 ~ N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not matrix[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1  # 개수를 + 1
            visited[i] = True  # 방문 처리
        else:  # 연결된 그래프가 있다면
            dfs(i)  # dfs탐색을 돈다.
            count += 1  # 개수를 + 1

print(count)



