# 장마철에 물에 잠기지 않는 안전한 영역의 최대 갯수
# 0 ~ max_val 까지만 확인

from collections import deque
import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def BFS(i, j):
    dQ = deque()
    dQ.append((i, j))
    visited[i][j] = True

    while dQ:
        x, y = dQ.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > k:
                    dQ.append((nx, ny))
                    visited[nx][ny] = True


n = int(input())

max_val = 0
graph = []
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    if max_val < max(data):
        max_val = max(data)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
for k in range(max_val+1):
    cnt = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                cnt += 1
                BFS(i, j)

    if cnt > result:
        result = cnt

print(result)
