# 탈출
"""
BFS
물이 먼저 이동하고 그 다음 고슴도치 이동
고슴도치는 재방문 하지 않도록 방문처리
"""
import sys
from collections import deque

# input = sys.stdin.readline
sys.stdin = open('C:\github\Algorithm\BFS & DFS\input.txt', 'rt')


def bfs():
    q = deque()
    for data in water:
        q.append(data)
    q.append(start)

    while q:
        x, y, info, time = q.popleft()

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < r and 0 <= ny < c:
                if info == '*':
                    if graph[nx][ny] == '.' or graph[nx][ny] == 'S':
                        q.append((nx, ny, '*', time + 1))
                        graph[nx][ny] = '*'
                elif info == 'S':
                    if graph[nx][ny] == 'D':
                        time += 1
                        return time
                    elif graph[nx][ny] == '.' and not visited[nx][ny]:
                        q.append((nx, ny, 'S', time + 1))
                        visited[nx][ny] = True

    return "KAKTUS"


r, c = map(int, input().split(' '))
visited = [[False] * c for _ in range(r)]

graph = []
water = []
for i in range(r):
    graph.append(list(input()))
    for j in range(c):
        if graph[i][j] == '*':
            water.append((i, j, '*', 0))
        elif graph[i][j] == 'S':
            start = (i, j, 'S', 0)
            visited[i][j] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = bfs()
print(answer)
