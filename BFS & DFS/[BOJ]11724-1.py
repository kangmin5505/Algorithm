# 연결 요소의 개수

# cnt, BFS
import sys
from collections import deque

sys.stdin = open('C:\github\Algorithm\BFS & DFS\input.txt', 'rt')


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


n, m = map(int, input().split(' '))

visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
