# 이분 그래프
"""
    인접한 정점끼리 서로 다른 색으로 칠해서 
    모든 정점을 두 가지 색으로만 칠할 수 있는 그래프
    => 인접한 정점이 두 그룹으로 나뉘어 질 수 있는 그래프
"""
# dfs
"""
    bfs의 경우 같은 계층에서는 같은 색 or 값을 같게 된다
"""

# input = sys.stdin.readline
import sys
from collections import deque
sys.stdin = open('C:\github\Algorithm\BFS & DFS\input.txt', 'rt')


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                # 상위 노드의 값과 다른 값을 대입
                visited[i] = -visited[v]
            # i를 방문했었으면
            else:
                if visited[v] == visited[i]:
                    return False
    return True


for tc in range(int(input())):
    v, e = map(int, input().split(' '))

    visited = [0] * (v+1)

    graph = [[] for _ in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split(' '))
        # 무방향성 그래프
        graph[a].append(b)
        graph[b].append(a)

     # 이분그래프 조건이 성립하지 않을 경우 반복문을 break하고 NO를 출력
    ans = True
    for i in range(1, v+1):
        # 방문하지 않았으면
        if visited[i] == 0:
            # bfs 함수의 결과가 False이면(=> 인접한 노드가 같은 값이면)
            if not bfs(i):
                ans = False
                break

    if ans:
        print("YES")
    else:
        print("NO")
