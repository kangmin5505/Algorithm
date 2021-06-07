# 열쇠
"""
BFS

풀이 방법
- 상근이 활동 범위 추가(지도 밖)
- 소유하고 있는 키 리스트 생성
- 문 방문 시 키가 없으면 door queue에 추가하고 키가 생기면 기존 queue에 추가
- 1) 문서인 경우, 2) 빈 공간인 경우, 3) 키인 경우, 4) 문인 경우로 구분
"""
import sys
from collections import deque

# input = sys.stdin.readline
sys.stdin = open("C:\github\Algorithm\BOJ\DFS & BFS\input.txt", "rt")


def BFS(sx, sy):
    visited = [[False] * (c+2) for _ in range(r+2)]
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True
    # door queue 생성 : 문을 만났을 때 키가 없는 경우 door queue에 추가
    dq = [deque() for _ in range(26)]
    cnt = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r+2 and 0 <= ny < c+2:
                if not visited[nx][ny] and graph[nx][ny] != '*':
                    visited[nx][ny] = True
                    # 문서인 경우
                    if graph[nx][ny] == '$':
                        cnt += 1
                        q.append((nx, ny))
                    # 빈 공간인 경우
                    elif graph[nx][ny] == '.':
                        q.append((nx, ny))
                    # 키인 경우
                    elif graph[nx][ny].islower():
                        key = ord(graph[nx][ny]) - ord('a')
                        keys[key] = True
                        # 획득한 키로 이전에 열지 못한 문을 열 수 있는 경우
                        while dq[key]:
                            kx, ky = dq[key].popleft()
                            q.append((kx, ky))
                        q.append((nx, ny))
                    # 문인 경우
                    elif graph[nx][ny].isupper():
                        door = ord(graph[nx][ny]) - ord('A')
                        # 키가 없는 경우 door queue에 추가
                        if keys[door] == False:
                            dq[door].append((nx, ny))
                        # 키가 있는 경우 이동
                        else:
                            q.append((nx, ny))
    return cnt


if __name__ == "__main__":
    tc = int(input())

    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    for _ in range(tc):
        r, c = map(int, input().split())
        # 상근이 활동 범위 추가(지도 밖)
        graph = [list('.' + input().strip() + '.') for _ in range(r)]
        graph = [['.'] * (c+2)] + graph + [['.'] * (c+2)]
        # 소유하고 있는 키 리스트 생성
        keys = [False] * 26
        k = input().strip()
        if k != '0':
            for key in k:
                keys[ord(key) - ord('a')] = True

        # (0, 0) 출발
        ans = BFS(0, 0)
        print(ans)
