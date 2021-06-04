# BFS
# 최소 일 수
# 1 익은 토마토, 0 익지 않은 토마토, -1 빈 칸
# 완전탐색 if graph[i][j] == 0: print(-1) flag 활용

from collections import deque
import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")

m, n = map(int, input().split())

dQ = deque()
visited = [[0] * m for _ in range(n)]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            dQ.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while dQ:
    x, y = dQ.popleft()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                dQ.append((nx, ny))
                graph[nx][ny] = 1
                visited[nx][ny] = visited[x][y] + 1

flag = True
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = False
            break

result = 0
if flag:
    for i in range(n):
        for j in range(m):
            if visited[i][j] > result:
                result = visited[i][j]
    print(result)
else:
    print(-1)
