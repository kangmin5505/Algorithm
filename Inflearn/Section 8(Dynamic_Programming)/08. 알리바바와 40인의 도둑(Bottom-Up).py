# 알리바바와 40인의 도둑(Bottom-Up)
"""
Dynamic Programming
- 점화식
if i == 0:
    dp[i][j] = dp[i][j-1] + board[i][j]
elif j == 0:
    dp[i][j] = dp[i-1][j] + board[i][j]
else:
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + board[i][j]
"""
import sys

# sys.stdin = open(
#     'C:\Study\Algorithm\Inflearn Algorithm(Python)\Section 8(solution)\input.txt', 'rt')

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(1, n):
    dp[0][i] = dp[0][i-1] + arr[0][i]
    dp[i][0] = dp[i-1][0] + arr[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]

print(dp[n-1][n-1])
