# 가방문제
"""
Knapsack Algorithm
"""

n, max_w = map(int, input().split())
dp = [0] * (max_w+1)

for _ in range(n):
    w, v = map(int, input().split())
    for i in range(w, max_w+1):
        if dp[i] < dp[i-w] + v:
            dp[i] = dp[i-w] + v

print(dp[max_w])
