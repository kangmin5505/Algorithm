# 도착지점까지 갈 수 있는 방법의 수
# cnt, visited, 상우하좌

import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def DFS(x, y):
    global cnt
    if x == n-1 and y == n-1:
        cnt += 1
    else:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    DFS(nx, ny)
                    visited[nx][ny] = False


n = 7

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]
visited[0][0] = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
DFS(0, 0)
print(cnt)
