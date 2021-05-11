# 1, 2, 3 더하기
"""
dynamic programming
"""

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for tc in range(int(input())):
    n = int(input())
    print(dp[n])
