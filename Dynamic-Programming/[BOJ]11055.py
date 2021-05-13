# 가장 큰 증가 부분 수열
"""
dynamic programming
- 현재 숫자의 이전 숫자 중 현재 숫자 보다 작으면서 가장 큰 dp값을 가지고 있는 숫자 + 현재 숫자
"""
import sys
import copy
sys.stdin = open('C:\github\Algorithm\Dynamic-Programming\input.txt', 'rt')

n = int(input())
data = list(map(int, input().split(' ')))

dp = copy.deepcopy(data)

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + data[i])

print(max(dp))

# n = int(input())
# data = list(map(int, input().split(' ')))
# dp = [0] * n
# dp[0] = data[0]

# for i in range(1, n):
#     for j in range(i):
#         if data[i] > data[j]:
#             dp[i] = max(dp[i], dp[j] + data[i])
#         else:
#             dp[i] = max(dp[i], data[i])

# print(max(dp))
