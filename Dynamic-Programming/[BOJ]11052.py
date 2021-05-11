# 카드 구매하기
"""
dynamic programming
"""


n = int(input())
data = [0] + list(map(int, input().split(' ')))
dp = [0] + [0] * n

for i in range(2, n+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + data[j]:
            dp[i] = dp[i-j] + data[j]

print(dp[n])
