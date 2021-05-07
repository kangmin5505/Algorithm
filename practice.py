import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(i, j):
    pq = []
    heappush(pq, (0, i, j))
    block[i][j] = 0

    while pq:
        cnt, x, y = heappop(pq)
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            elif block[nx][ny] != -1:
                continue
            else:
                if graph[nx][ny] == 0:
                    heappush(pq, (0, nx, ny))
                    block[nx][ny] = block[x][y]
                else:
                    heappush(pq, (1, nx, ny))
                    block[nx][ny] = block[x][y] + 1


c, r = map(int, input().split(' '))

block = [[-1] * c for _ in range(r)]
graph = []
for _ in range(r):
    graph.append(list(map(int, input().rstrip())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dijkstra(0, 0)
print()
print(block[r-1][c-1])
