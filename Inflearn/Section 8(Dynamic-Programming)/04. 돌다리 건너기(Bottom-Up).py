# 돌다리 건너기(Bottom-Up)
"""
Dynamic Programming
- 점화식
dp[i] = dp[i-1] + dp[i-2]
"""

n = int(input())

dp = [0] * (n+2)
dp[1] = 1
dp[2] = 2

for i in range(3, n+2):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n+1])
