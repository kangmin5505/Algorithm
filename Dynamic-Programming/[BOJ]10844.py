# 쉬운 계단 수
"""
dynamic programming
점화식 : if 0 < j < 9: dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] elif j == 0: dp[i][j] = dp[i-1][j+1] elif j == 9: dp[i][j] = dp[i-1][j-1]
"""

n = int(input())
div = 1000000000

dp = [[0] * 10 for _ in range(101)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if 1 <= j <= 8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        elif j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]

print(sum(dp[n]) % div)
