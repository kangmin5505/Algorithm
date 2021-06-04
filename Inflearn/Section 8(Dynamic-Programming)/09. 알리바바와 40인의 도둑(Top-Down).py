# 알리바바와 40인의 도둑(Top-Down)
"""
Dynamic Programming
Recursion
Memoization
"""
import sys

sys.stdin = open(
    'C:\Study\Algorithm\Inflearn Algorithm(Python)\Section 8(solution)\input.txt', 'rt')


def dfs(i, j):
    if dp[i][j] > 0:
        return dp[i][j]

    if i == 0:
        dp[i][j] = dfs(i, j-1) + arr[i][j]
    elif j == 0:
        dp[i][j] = dfs(i-1, j) + arr[i][j]
    else:
        dp[i][j] = min(dfs(i-1, j), dfs(i, j-1)) + arr[i][j]
    return dp[i][j]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]


print(dfs(n-1, n-1))
