# graph[n-1]에서 2인 열의 값을 찾아서 시작점으로 설정
# 좌우를 확인하고 없을 경우 위로 이동
# graph[0]에서 2인 값을 찾아서 열 값을 출력

import sys

sys.stdin = open(
    "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def DFS(x, y):
    visited[x][y] = True

    if x == 0:
        print(y)
    else:
        if y-1 >= 0 and graph[x][y-1] == 1 and visited[x][y-1] == 0:
            DFS(x, y-1)
        elif y+1 < n and graph[x][y+1] == 1 and visited[x][y+1] == 0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


n = 10
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for y in range(n):
    if graph[n-1][y] == 2:
        DFS(n-1, y)
