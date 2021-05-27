# 연속합
"""
dynamic programming
dp[i - 1] + data[i]가 data[i] 보다 작으면 
data[i]부터 다시 합을 시작하는 구조
"""
import sys
sys.stdin = open('C:\github\Algorithm\Dynamic-Programming\input.txt', 'rt')


n = int(input())
data = list(map(int, input().split(' ')))

dp = [0] * n
dp[0] = data[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + data[i], data[i])

print(max(dp))
