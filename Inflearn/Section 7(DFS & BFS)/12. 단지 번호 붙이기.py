# 완전탐색, DFS
# 4 방향, 단지 수, 단지에 속하는 집의 수(오름차순)
# DFS return 값을 단지에 속하는 집의 수로 설정

import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def DFS(x, y):
    global cnt
    graph[x][y] = 0
    cnt += 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                DFS(nx, ny)


if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                cnt = 0
                DFS(i, j)
                result.append(cnt)

    result.sort()

    print(len(result))
    for x in result:
        print(x)
