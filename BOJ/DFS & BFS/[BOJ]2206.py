# 벽 부수고 이동하기
"""
BFS
모든 값이 -1인 step 리스트를 선언하여 
시작시 시작점에 0 대입
1을 만나면 +1 해주고
조건식에 1이상일때 block을 만나면 가지 못하도록 설정
"""

import sys
from collections import deque

sys.stdin = open('C:\github\Algorithm\BFS & DFS\input.txt', 'rt')


def bfs(state, i, j):
    q = deque()
    q.append((state, i, j))
    step[i][j] = 1

    while q:
        state, x, y = q.popleft()

        if x == r-1 and y == c-1:
            return step[x][y]

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            else:
                if graph[nx][ny] == 1 and state == 1:
                    step[nx][ny] = step[x][y] + 1
                    q.append((state-1, nx, ny))
                elif graph[nx][ny] == 0 and step[nx][ny] == -1:
                    step[nx][ny] = step[x][y] + 1
                    q.append((state, nx, ny))

                # if state == 0:
                #     if graph[nx][ny] == 0:
                #         q.append((state, nx, ny))
                #         step[nx][ny] = step[x][y] + 1
                #     elif graph[nx][ny] == 1:
                #         q.append((state + 1, nx, ny))
                #         step[nx][ny] = step[x][y] + 1
                # elif state == 1:
                #     if graph[nx][ny] == 1:
                #         continue
                #     else:
                #         q.append((state, nx, ny))
                #         step[nx][ny] = step[x][y] + 1

    return -1


r, c = map(int, input().split(' '))

step = [[-1] * c for _ in range(r)]
graph = []
for _ in range(r):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(1, 0, 0))
for i in step:
    print(i)
