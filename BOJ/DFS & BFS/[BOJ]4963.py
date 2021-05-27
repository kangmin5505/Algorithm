# 섬의 개수
# BFS

import sys
from collections import deque

sys.stdin = open('C:\github\Algorithm\BFS & DFS\input.txt', 'rt')


def bfs(i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0

    while q:
        x, y = q.popleft()

        for direction in range(8):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            elif graph[nx][ny] == 0:
                continue
            else:
                graph[nx][ny] = 0
                q.append((nx, ny))


# 상하좌우(4가지), 대각선(4가지)
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

while True:
    w, h = map(int, input().split(' '))

    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split(' '))))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
