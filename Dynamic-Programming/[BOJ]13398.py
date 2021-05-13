# 연속합
"""
dynamic programming

"""
import sys
sys.stdin = open('C:\github\Algorithm\Dynamic-Programming\input.txt', 'rt')


n = int(input())
data = list(map(int, input().split(' ')))

dp = [[0] * n for _ in range(2)]
dp[0][0] = dp[1][0] = data[0]
answer = data[0]

for i in range(1, n):
    # 숫자 안 뺀 거
    dp[0][i] = max(dp[0][i - 1] + data[i], data[i])
    # 숫자 뺀 거(i번째 숫자를 제외한 것과 그 이전에 나온 숫자 중 하나를 제거한 것 + i번째 숫자를 더한 것 중 최댓값)
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + data[i])

    answer = max(answer, dp[0][i], dp[1][i])

print(answer)
