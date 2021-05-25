# 동전 2
"""
dynamic programming

풀이방법
- 코인을 오름차순 정렬 후 dp[i] = dp[i - coin] + 1 해준다
"""
import math

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins.sort()

INF = math.inf

dp = [INF] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(1, k + 1):
        if i - coin >= 0:
            if dp[i] > dp[i - coin] + 1:
                dp[i] = dp[i - coin] + 1

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
