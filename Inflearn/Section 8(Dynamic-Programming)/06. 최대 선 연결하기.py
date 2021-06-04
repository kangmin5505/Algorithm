# 최대 선 연결하기
"""
Dynamic Programming
- 해결 방법
증가하는 부분 수열 구하기
"""

n = int(input())
data = [0] + [int(x) for x in input().split()]
dp = [0] * (n+1)
dp[1] = 1
res = 0

for i in range(2, n+1):
    max_val = 0
    for j in range(i):
        if data[i] > data[j] and max_val < dp[j]:
            max_val = dp[j]
    dp[i] = max_val + 1

    if res < dp[i]:
        res = dp[i]

print(res)
