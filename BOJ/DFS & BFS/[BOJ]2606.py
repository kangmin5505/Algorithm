# 바이러스

# BFS
from collections import deque


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    count = 0

    while queue:
        v = queue.popleft()
        for i in range(1, n+1):
            if not visited[i] and graph[v][i] == 1:
                visited[i] = True
                queue.append(i)
                count += 1
    return count


n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

print(bfs(1))
