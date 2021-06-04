# Topological sorting(위상 정렬)
"""
1. 2차원 테이블 선언
2. 방향그래프 간선을 입력받기 + 진입차수 증가 시키기
3. 진입차수가 0인거 dQ에 넣기
4. while문 돌면서 해당 노드와 이어져있는 노드의 진입차수 -1
5. 진입차수가 0이 된 노드 dQ에 넣기
"""
import sys
from collections import deque

sys.stdin = open(
    "C:\Study\Algorithm\Inflearn Algorithm(Python)\Section 8(solution)\input.txt", "rt")

n, m = map(int, input().split())
dis = [[0] * (n+1) for _ in range(n+1)]
degree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    dis[a][b] = 1
    degree[b] += 1

dQ = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        dQ.append(i)

while dQ:
    v = dQ.popleft()
    print(v, end=" ")

    for i in range(1, n+1):
        if dis[v][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                dQ.append(i)
