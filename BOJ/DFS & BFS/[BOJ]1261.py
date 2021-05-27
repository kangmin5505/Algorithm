# 알고스팟
"""
BFS
0이 있는 길을 우선으로 가면서 block의 갯수를 count 해준다
* appendleft()
"""

import sys
from collections import deque

sys.stdin = open('C:\github\Algorithm\BFS & DFS\input.txt', 'rt')


def bfs(i, j):
    q = deque()
    q.append((i, j))
    block[i][j] = 0

    while q:
        x, y = q.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            elif block[nx][ny] != -1:
                continue
            else:
                if graph[nx][ny] == 0:
                    # 벽이 없으면 우선순위 처리
                    q.appendleft((nx, ny))
                    block[nx][ny] = block[x][y]
                elif graph[nx][ny] == 1:
                    # 벽이 있으면 뒤에 넣기
                    q.append((nx, ny))
                    block[nx][ny] = block[x][y] + 1


c, r = map(int, input().split(' '))

# 모든 값이 -1인 block 리스트를 생성하고, bfs함수 시작 시 시작점에 0을 넣어준다
# 시작점에는 block이 없기 때문에
block = [[-1] * c for _ in range(r)]
graph = []
for _ in range(r):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(0, 0)

print(block[r-1][c-1])
