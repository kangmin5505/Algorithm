# 스티커
"""
dynamic programming
점화식
dp[0][i] += max(dp[1][i-1], d[1][i-2])
dp[1][i] += max(dp[0][i-1], d[0][i-2])
"""
import sys

# sys.stdin = open('C:\github\Algorithm\Dynamic-Programming\input.txt', 'rt')

for tc in range(int(input())):
    n = int(input())

    dp = []
    for i in range(2):
        dp.append(list(map(int, input().split(' '))))

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))
