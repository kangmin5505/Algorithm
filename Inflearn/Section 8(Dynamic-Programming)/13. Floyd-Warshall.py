# Floyd-Warshall Algorithm
"""
1. 모든 간선 저장
2. 자기 자신은 0으로 초기화
3. 3중 for문으로 해결
"""
import sys
import math
# sys.stdin = open(
#     'C:\Study\Algorithm\Inflearn Algorithm(Python)\Section 8(solution)\input.txt', 'rt')


n, m = map(int, input().split())


dis = [[math.inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dis[i][i] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    dis[a][b] = cost

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j] == math.inf:
            print("M", end=" ")
        else:
            print(dis[i][j], end=" ")
    print()
