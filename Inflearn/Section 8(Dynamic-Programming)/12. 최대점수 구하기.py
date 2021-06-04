# 최대점수 구하기
"""
Knapsack Algorithm
"""
import sys

# sys.stdin = open(
#     'C:\Study\Algorithm\Inflearn Algorithm(Python)\Section 8(solution)\input.txt', 'rt')

n, m = map(int, input().split())

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    score, time = map(int, input().split())
    for j in range(time, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + score)

print(dp[n][m])
