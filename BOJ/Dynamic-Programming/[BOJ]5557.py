# 1학년
"""
dynamic programming
"""
import sys

sys.stdin = open('C:\github\Algorithm\BOJ\Dynamic-Programming\input.txt', 'rt')

n = int(input())
*arr, target = [0] + [int(x) for x in input().split()]
max_val = 20
dp = [[0] * (max_val+1) for _ in range(n)]
dp[1][arr[1]] = 1

for i in range(2, n):
    for j in range(max_val + 1):
        if dp[i-1][j] > 0:
            if j + arr[i] <= max_val:
                dp[i][j + arr[i]] += dp[i-1][j]
            if j - arr[i] >= 0:
                dp[i][j - arr[i]] += dp[i-1][j]

print(dp[n-1][target])
