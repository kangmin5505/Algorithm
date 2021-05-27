# 미로 탐색
# BFS
# 상하좌우 확인 후 칸이 1이면 실행

import sys
from collections import deque

sys.stdin = open('C:\github\Algorithm\BFS & DFS\input.txt', 'rt')


def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif graph[nx][ny] != 1:
                continue
            else:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


n, m = map(int, input().split(' '))

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0, 0)
print(graph[n-1][m-1])
