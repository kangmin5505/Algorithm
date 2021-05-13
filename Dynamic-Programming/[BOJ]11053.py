# 가장 긴 증가하는 부분 수열
"""
dynamic programming
현재 숫자의 이전 숫자 중 가장 큰 dp값 +1
"""

n = int(input())
data = list(map(int, input().split(' ')))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
