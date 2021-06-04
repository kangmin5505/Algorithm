# 상우하좌, visited
# result = visited[n-1][n-1]

import sys
from collections import deque

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def BFS(i, j):
    dQ = deque()
    dQ.append((i, j))
    visited[i][j] = 0

    while dQ:
        x, y = dQ.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    dQ.append((nx, ny))


if __name__ == "__main__":
    n = 7
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    visited = [[-1] * n for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    BFS(0, 0)

    print(visited[n-1][n-1])
