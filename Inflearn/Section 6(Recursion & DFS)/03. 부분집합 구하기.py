# 방문할지 안 할지 구분
# 전위순회
def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if visited[i] == 1:
                print(i, end=' ')
        print()
    else:
        visited[v] = 1
        DFS(v+1)
        visited[v] = 0
        DFS(v+1)


n = int(input())
visited = [0] * (n+1)
DFS(1)
