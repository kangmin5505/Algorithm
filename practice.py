import sys
from collections import deque

sys.stdin = open("C:\github\Algorithm\BOJ\DFS & BFS\input.txt", "rt")


w, h = map(int, input().split())
a = [list(input().strip()) for _ in range(h)]
dist = [[0]*w for _ in range(h)]
q = deque()
ex, ey = -1, 0

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x+dx, y+dy
            while 0 <= nx < h and 0 <= ny < w and a[nx][ny] != '*':
                if not dist[nx][ny]:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx, ny))
                nx, ny = nx+dx, ny+dy
    for x in dist:
        print(x)

for i in range(h):
    for j in range(w):
        if a[i][j] == 'C':
            if ex == -1:
                ex, ey = i, j
            else:
                q.append((i, j))
bfs()
print(dist[ex][ey]-1)


