# 점프
"""
dynamic programming
- 완전탐색을 하면서 해당 칸이 이동 가능한 칸이면 해당 칸의 숫자만큼 오른쪽, 아래로 이동
"""
import sys

sys.stdin = open('BOJ/Dynamic-Programming/input.txt', 'rt')

n = int(input())

board = []
for _ in range(n):
    board.append([int(x) for x in input().split()])

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] > 0 and board[i][j] != 0:
            # 열 이동
            if j + board[i][j] < n:
                dp[i][j + board[i][j]] += dp[i][j]
            # 행 이동
            if i + board[i][j] < n:
                dp[i + board[i][j]][j] += dp[i][j]

print(dp[n-1][n-1])


