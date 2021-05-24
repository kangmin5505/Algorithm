# 제곱수의 합
"""
dynamic programming
1부터 n까지 확인
"""

n = int(input())

dp = [i for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        if j * j > i:
            break
        else:
            if dp[i] > dp[i - (j * j)] + 1:
                dp[i] = dp[i - (j * j)] + 1
print(dp[n])
