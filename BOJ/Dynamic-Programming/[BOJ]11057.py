# 오르막 수
"""
dynamic programming
점화식 : dp[i][j] = sum(dp[i-1][:j+1])
"""

n = int(input())
div = 10007

dp = [[0] * 10 for _ in range(1001)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])
        # for k in range(j+1):
        #     dp[i][j] += dp[i-1][k]

print(sum(dp[n]) % div)
