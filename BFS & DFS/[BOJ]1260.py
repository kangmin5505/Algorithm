from collections import deque


def dfs(start):
    visited_dfs[start] = True
    print(start, end=' ')
    for i in range(1, n+1):
        if not visited_dfs[i] and graph[start][i]:
            dfs(i)


def bfs(start):
    q = deque()
    q.append(start)
    visited_bfs[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if not visited_bfs[i] and graph[v][i]:
                q.append(i)
                visited_bfs[i] = True


n, m, start = map(int, input().split(' '))
graph = [[0] * (n+1) for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a][b] = 1
    graph[b][a] = 1

dfs(start)
print()
bfs(start)
