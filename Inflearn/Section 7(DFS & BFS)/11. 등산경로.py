# 네 방향 중 더 높은 구역으로만 이동
# 출발지는 가장 작은 값, 목적지는 가장 큰 값


import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def DFS(x, y):
    global cnt
    if x == target_x and y == target_y:
        cnt += 1
    else:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > graph[x][y]:
                    visited[nx][ny] = True
                    DFS(nx, ny)
                    visited[nx][ny] = False


if __name__ == "__main__":
    n = int(input())
    graph = []
    target_x, target_y = 0, 0
    max_val = 0
    start_x, start_y = 0, 0
    min_val = int(1e9)

    for i in range(n):
        graph.append(list(map(int, input().split())))
        for j in range(n):
            if graph[i][j] > max_val:
                max_val = graph[i][j]
                target_x, target_y = i, j
            if graph[i][j] < min_val:
                min_val = graph[i][j]
                start_x, start_y = i, j

    visited = [[False] * n for _ in range(n)]
    visited[start_x][start_y] = True

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0
    DFS(start_x, start_y)
    print(cnt)
