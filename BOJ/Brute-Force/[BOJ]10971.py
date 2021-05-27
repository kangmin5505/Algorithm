# 외판원 순회2
# 방문, dfs
import sys
sys.stdin = open('C:\github\Algorithm\Brute-Force\input.txt', 'rt')


def dfs(start, now, cost):

    if all(visited):
        if graph[now][start] != 0:
            min_cost = min(min_cost, cost + graph[now][start])
        return

    for i in range(n):
        # 제한조건에 만족 하지 않는 경우
        if start == i or visited[i] or graph[now][i] == 0:
            continue
        else:
            visited[i] = True
            dfs(start, i, cost + graph[now][i])
            visited[i] = False


n = int(input())

visited = [False] * n
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split(' '))))

min_cost = int(1e9)
for i in range(n):
    visited[i] = True
    dfs(i, i, 0)  # 시작점, 현재노드, 비용
    visited[i] = False

print(min_cost)
