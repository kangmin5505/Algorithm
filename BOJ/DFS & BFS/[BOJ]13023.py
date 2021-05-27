# ABCDE

# 깊이가 4인 경우를 찾는 문제
# 문제해석이 어려움

def dfs(v, depth):
    global ans

    visited[v] = True

    if depth == 4:
        ans = True
        return

    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = False


n, m = map(int, input().split(' '))

visited = [False] * n

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

ans = False
for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if ans:
        break

print(1 if ans else 0)
