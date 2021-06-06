# 벽 부수고 이동하기
"""
BFS

풀이 방법
- 벽돌을 부수고 이동하는 경우와 부수지 않고 길로 이동하는 경우로 나누어서 실행
"""
import sys
from collections import deque

sys.stdin = open('C:\github\Algorithm\BOJ\DFS & BFS\input.txt', 'rt')
# input = sys.stdin.readline


def BFS():
    dQ = deque()
    # 시작 좌표와 벽을 부술 수 있는 경우
    dQ.append([0, 0, 1])
    dist = [[[0, 0] for _ in range(m)] for _ in range(n)]
    dist[0][0][1] = 1

    while dQ:
        x, y, w = dQ.popleft()

        # 종료조건
        if x == n-1 and y == m-1:
            return dist[x][y][w]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽돌을 부수지 않고 길로 이동하는 경우
                if graph[nx][ny] == 0 and dist[nx][ny][w] == 0:
                    dist[nx][ny][w] = dist[x][y][w] + 1
                    dQ.append([nx, ny, w])
                # 벽돌을 부수고 이동하는 경우
                elif graph[nx][ny] == 1 and w == 1:
                    dist[nx][ny][0] = dist[x][y][w] + 1
                    dQ.append([nx, ny, 0])

    # dist[n-1][m-1]에 도달하지 못 했을 때
    return -1


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = BFS()
print(ans)
