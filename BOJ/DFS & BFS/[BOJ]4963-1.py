# 섬의 개수
# DFS

import sys

sys.setrecursionlimit(10000)
sys.stdin = open('C:\github\Algorithm\BFS & DFS\input.txt', 'rt')


def dfs(x, y):
    graph[x][y] = 0

    for direction in range(8):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        elif graph[nx][ny] == 0:
            continue
        else:
            dfs(nx, ny)


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
                dfs(i, j)
                cnt += 1

    print(cnt)
