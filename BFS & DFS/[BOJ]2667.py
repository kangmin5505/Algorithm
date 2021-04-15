# 단지번호 붙이기

# BFS
# 단지내 집의 수 출력
# 1이면 bfs 돌고 갯수 반환
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
# with open('C:/github/Algorithm/BFS & DFS/test.txt', 'r') as f:
#     for _ in range(n):
#         line = f.readline().rstrip()
#         graph.append(list(map(int, line)))

count_home = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = bfs(i, j)
            count_home.append(count)

print(len(count_home))
count_home.sort()
for i in count_home:
    print(i)
