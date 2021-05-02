# 외판원 순회2
# 방문, dfs
import sys
sys.stdin = open("C:\github\Algorithm\Brute-Force\input.txt", "rt")


def dfs(start, now, cost):
    global min_cost

    # 모든 곳을 방문했을 경우 cost 계산
    if all(visited):
        min_cost = min(min_cost, cost+graph[now][start])
        return

    for i in range(n):
        if not visited[i] and graph[now][i] != 0 and start != i:
            visited[i] = True
            dfs(start, i, cost + graph[now][i])
            visited[i] = False


n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n


min_cost = int(1e9)
# 외판원이 출발하는 지점
for start in range(n):
    # 시작점, 지금위치, 비용
    dfs(start, start, 0)

print(min_cost)
