# 최대 부분 증가수열
"""
Dynamic Programming
- 점화식
dp[i] = max_val + 1 
max_val = data[i] > data[j] 중 i보다 작은 인덱스 중에 가장 큰 값
"""

n = int(input())
data = [int(x) for x in input().split()]

dp = [0] * n
dp[0] = 1
res = 0

for i in range(1, n):
    max_val = 0
    for j in range(i):
        if data[i] > data[j] and max_val < dp[j]:
            max_val = dp[j]
    dp[i] = max_val + 1
    if dp[i] > res:
        res = dp[i]

print(res)
