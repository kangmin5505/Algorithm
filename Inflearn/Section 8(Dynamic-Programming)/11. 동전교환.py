# 동전교환
"""
Dynamic Programming
"""
import math

n = int(input())
coins = list(map(int, input().split()))
tg = int(input())

dp = [math.inf] * (tg+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, tg+1):
        if dp[i] > dp[i-coin] + 1:
            dp[i] = dp[i-coin] + 1

print(dp[tg])
