# 토마토
# BFS
"""
토마토 좌표 받아서 상하좌우 확인
방문 좌표의 값이 0이면 기존 좌표의 값 + 1
해당 좌표의 값은 기존 값과 새로 입력되는 값의 최솟값
가장 큰 일수를 따로 저장 
마지막에 모든 좌표를 확인해서 0이 있으면 -1 출력
"""


import sys
from collections import deque

sys.stdin = open('C:\github\Algorithm\BFS & DFS\input.txt', 'rt')


def check():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True


def bfs():
    global ans

    q = deque()
    for i, j in tomato:
        q.append((i, j))

    while q:
        x, y = q.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif graph[nx][ny] != 0:
                continue
            else:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                ans = max(ans, graph[nx][ny] - 1)


m, n = map(int, input().split(' '))

graph = []
tomato = []
for i in range(n):
    graph.append(list(map(int, input().split(' '))))
    for j in range(m):
        if graph[i][j] == 1:
            tomato.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
bfs()

if check():
    print(ans)
else:
    print(-1)
