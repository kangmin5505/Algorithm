# 2*n 타일링 2
"""
dynamic programming
"""

n = int(input())

div = 10007
dp = [0] * (n+1)
dp[1] = 1
if n > 1:
    dp[2] = 3

# 점화식 dp[i] = dp[i-1] + (2 * dp[i-2])
for i in range(3, n+1):
    dp[i] = (dp[i-1] + (2 * dp[i-2])) % 10007

print(dp[n])
