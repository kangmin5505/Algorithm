# 이동하기
"""
dynamic programming
- 범위 내에서 오른쪽, 아래, 오른쪽 아래의 대각선으로 이동
- 이동 시 dp테이블 최대값으로 갱신
"""
import sys

sys.stdin = open('C:\github\Algorithm\Dynamic-Programming\input.txt', 'rt')


def solution():
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = board[i][j] + max(dp[i - 1][j], dp[i][j - 1])


n, m = map(int, input().split())

board = [[0] * (m+1)]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

dp = [[0] * (m + 1) for _ in range(n + 1)]

solution()

print(dp[n][m])
