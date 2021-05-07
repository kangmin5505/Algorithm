# 단지번호 붙이기

# BFS

import sys
from collections import deque

sys.stdin = open('C:\github\Algorithm\BFS & DFS\input.txt', 'rt')


def bfs(i, j):
    q = deque()
    q.append((i, j))
    board[i][j] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 0:
                continue

            board[nx][ny] = 0
            cnt += 1
            q.append((nx, ny))

    return cnt


n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input())))

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

count_home = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = bfs(i, j)
            count_home.append(cnt)

print(len(count_home))

count_home.sort()
for i in count_home:
    print(i)
