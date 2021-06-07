# 로봇 청소기
"""
BFS

풀이 방법
- 로봇청소기와 먼지 사이의 거리를 구한다
    => 처음에 선택할 먼지와의 거리를 알기 위함
- 먼지와 먼지 사이의 거리를 구한다
    => 먼지에서 먼지로 갈 때 거리를 알기 위함
- 순열을 이용하여 최소거리를 구한다
    => 어떤 경우가 최선인지 모르기 때문에 모든 경우를 실행
"""
import sys
from collections import deque
# from itertools import permutations

sys.stdin = open("C:\github\Algorithm\BOJ\DFS & BFS\input.txt", "rt")


def DFS(L):
    if L == len(dusts):
        temp = []
        for x in pm:
            temp.append(x)
        permus.append(temp)
    else:
        for i in range(len(dusts)):
            if i not in pm:
                pm.append(i)
                DFS(L+1)
                pm.pop()


def BFS(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited = [[-1] * c for _ in range(r)]
    visited[sx][sy] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                if visited[nx][ny] == -1 and graph[nx][ny] != 'x':
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx, ny))
    return visited


if __name__ == "__main__":
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    while True:
        c, r = map(int, input().split())

        # 종료조건
        if c == 0 and r == 0:
            break

        graph = [list(input().strip()) for _ in range(r)]
        # 시작점과 먼지위치 찾기
        rx, ry = 0, 0
        dusts = []
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 'o':
                    rx, ry = i, j
                elif graph[i][j] == '*':
                    dusts.append((i, j))

        # 로봇 청소기와 먼지 사이의 거리 구하기
        # 도달할 수 없는 먼지가 있다면 종료
        robot_dust = [0] * len(dusts)
        visited = BFS(rx, ry)
        is_possible = True
        for i in range(len(dusts)):
            temp = visited[dusts[i][0]][dusts[i][1]]
            if temp == -1:
                print(-1)
                is_possible = False
                break
            else:
                robot_dust[i] = temp

        if is_possible:
            # 먼지와 먼지 사이의 거리 구하기
            dist = [[0] * len(dusts) for _ in range(len(dusts))]
            for i in range(len(dusts)-1):
                # 기준 먼지(i)
                visited = BFS(dusts[i][0], dusts[i][1])
                for j in range(i+1, len(dusts)):
                    dist[i][j] = visited[dusts[j][0]][dusts[j][1]]
                    # i에서 j로 가는 거리와 j에서 i로 가는 거리는 동일
                    dist[j][i] = dist[i][j]

            # 순열을 이용하여 최소거리를 구함
            pm = []
            permus = []
            # 순열을 구해주는 함수
            DFS(0)
            ans = int(1e9)
            # for permu in permutations(range(len(dusts))):
            for permu in permus:
                # 처음에는 로봇청소기에서 첫 번째 먼지까지의 거리를 더한다
                temp = robot_dust[permu[0]]
                # 시작지점은 첫 번째 먼지
                start = permu[0]
                for idx in range(1, len(dusts)):
                    # 도착지점
                    end = permu[idx]
                    # 거리 누적
                    temp += dist[start][end]
                    start = end
                ans = min(ans, temp)
            print(ans)
        else:
            continue
