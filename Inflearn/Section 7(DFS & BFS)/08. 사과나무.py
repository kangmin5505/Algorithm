# n은 항상 홀수
# 상하좌우, visited, ans

from collections import deque
import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def BFS(a, b):
    ans = 0
    dQ = deque()
    dQ.append((a, b))
    visited[a][b] = 0

    while dQ:
        x, y = dQ.popleft()
        ans += graph[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if visited[x][y] + 1 <= n//2 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                dQ.append((nx, ny))

    return ans


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[-1] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = BFS(n//2, n//2)
print(ans)
