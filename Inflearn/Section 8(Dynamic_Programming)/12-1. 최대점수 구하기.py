# 최대점수 구하기
"""
Knapsack Algorithm
뒤에서부터 확인하면 중복되지 않음
"""
import sys

sys.stdin = open(
    'C:\Study\Algorithm\Inflearn Algorithm(Python)\Section 8(solution)\input.txt', 'rt')

n, m = map(int, input().split())

dp = [0] * (m+1)

for _ in range(n):
    ps, pt = map(int, input().split())
    for i in range(m, pt-1, -1):
        dp[i] = max(dp[i], dp[i-pt] + ps)

print(dp[m])
