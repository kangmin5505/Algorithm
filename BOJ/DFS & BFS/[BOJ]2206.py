# 벽 부수고 이동하기
"""
BFS

해결 방법
- 벽을 부수고 이동하는 경우와 벽을 부수지 않고 이동하는 경우로 구분
"""
import sys
from collections import deque

sys.stdin = open('C:\github\Algorithm\BOJ\DFS & BFS\input.txt', 'rt')


def BFS():
    dQ = deque()
    # 시작 좌표와 벽을 부술 수 있는 기회
    dQ.append([0, 0, 1])
    # 벽을 부수고 이동하는 경우와 부수지 않고 이동하는 경우 따로 확인
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while dQ:
        x, y, w = dQ.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][w]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 부수지 않고 이동하는 경우
                if graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    dQ.append([nx, ny, w])
                # 벽을 부수고 이동한 경우
                if graph[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] = visited[x][y][w] + 1
                    dQ.append([nx, ny, 0])

    # graph[n-1][m-1]에 도달하지 못 한 경우
    return -1


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = BFS()
print(ans)
