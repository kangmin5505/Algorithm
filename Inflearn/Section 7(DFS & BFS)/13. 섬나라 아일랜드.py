# 완전탐색, BFS
# 4 방향, 4 대각선, cnt

import sys
from collections import deque

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def BFS(i, j):
    dQ = deque()
    dQ.append((i, j))
    graph[i][j] = 0

    while dQ:
        x, y = dQ.popleft()

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    dQ.append((nx, ny))


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0, -1, 1, 1, -1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            BFS(i, j)

print(cnt)
