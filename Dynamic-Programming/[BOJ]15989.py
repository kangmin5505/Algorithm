# 1, 2, 3 더하기 4
"""
dynamic programming
점화식
dp[1][i] = dp[1][i - 1]
dp[2][i] = dp[1][i - 2] + dp[2][i - 2] -> 1과 2를 조합하는 경우, 2와 2를 조합하는 경우
dp[3][i] = dp[1][i - 3] + dp[2][i  - 3] + dp[3][i - 3] -> 1과 3, 2와 3, 3과 3을 조합하는 경우
"""

maximum = 10001
dp = [[0] * maximum for _ in range(4)]

dp[1][1] = 1
dp[1][2], dp[2][2] = 1, 1
dp[1][3], dp[2][3], dp[3][3] = 1, 1, 1

for i in range(4, maximum):
    dp[1][i] = dp[1][i - 1]
    dp[2][i] = dp[1][i - 2] + dp[2][i - 2]
    dp[3][i] = dp[1][i - 3] + dp[2][i - 3] + dp[3][i - 3]


for tc in range(int(input())):
    n = int(input())
    answer = dp[1][n] + dp[2][n] + dp[3][n]
    print(answer)
