# 계단오르기(Top-Down)
"""
Dynamic Programming
- 점화식
dp[i] = dfs(i-1) + dfs(i-2)
"""


def dfs(i):
    if dp[i] > 0:
        return dp[i]
    if i == 1 or i == 2:
        return i
    else:
        dp[i] = dfs(i-1) + dfs(i-2)
        return dp[i]


n = int(input())

dp = [0] * (n+1)

print(dfs(n))
