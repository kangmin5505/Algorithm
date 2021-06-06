# 탈옥
"""
0-1 BFS : 가중치가 2개인 BFS

풀이 방법
- '.'인 경우 appendleft(우선순위)
- '#'인 경우 append
- 죄수1, 죄수2, 상근이가 각자의 위치에서 문을 열고 i, j로 가는 수를 2차원 배열로 생성
    => 죄수1과 죄수2만으로 해결하려고 하는 경우, 두 죄수가 만나고나서 탈출하는 알고리즘을 작성해야 한다
    => 밖에 있는 상근이도 포함하여 해결하기 위해 감옥 밖 지역을 생성해줘야 한다
- 3명은 문이 1개라도 있다면 항상 문에서 만남(중복을 제거하기 위해 -2)
"""
from collections import deque
import sys

sys.stdin = open("C:\github\Algorithm\BOJ\DFS & BFS\input.txt", "rt")
# input = stdin.readline


def BFS(s_x, s_y):
    dist = [[-1] * (w+2) for _ in range(h+2)]
    sdQ = deque()
    sdQ.append((s_x, s_y))
    dist[s_x][s_y] = 0

    while sdQ:
        x, y = sdQ.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < h+2 and 0 <= ny < w+2:
                if dist[nx][ny] == -1 and graph[nx][ny] != '*':
                    # 빈 공간인 경우 우선순위로 실행
                    if graph[nx][ny] == '.':
                        sdQ.appendleft((nx, ny))
                        dist[nx][ny] = dist[x][y]
                    elif graph[nx][ny] == '#':
                        sdQ.append((nx, ny))
                        dist[nx][ny] = dist[x][y] + 1
    return dist


tc = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(tc):
    h, w = map(int, input().split())
    # 상근이 활동구역 생성(감옥 밖)
    graph = [['.'] * (w+2)]
    for _ in range(h):
        graph.append(list('.' + input().strip() + '.'))
    graph.append(['.'] * (w+2))

    # 죄수 위치 파악
    dQ = deque()
    for i in range(h+2):
        for j in range(w+2):
            if graph[i][j] == '$':
                graph[i][j] = '.'
                dQ.append((i, j))

    # 죄수1, 죄수2, 상근이 BFS로 탐색
    x_1, y_1 = dQ.popleft()
    prisoner_1 = BFS(x_1, y_1)
    x_2, y_2 = dQ.popleft()
    prisoner_2 = BFS(x_2, y_2)
    sanggen = BFS(0, 0)

    ans = int(1e9)
    for i in range(h+2):
        for j in range(w+2):
            # if graph[i][j] != '*':
            # 위에 것으로 하면 고립되어 있는 '.'도 포함을 시켜서 오답이 나온다
            if prisoner_1[i][j] != -1 and prisoner_2[i][j] != -1 and sanggen[i][j] != -1:
                temp = prisoner_1[i][j] + prisoner_2[i][j] + sanggen[i][j]
                # 문일 경우 중복 제거
                if graph[i][j] == '#':
                    temp -= 2
                ans = min(ans, temp)
    print(ans)
