# 이친수
"""
dynamic programming
0으로 끝날 경우 -> 이전 자릿수에서 0, 1로 끝나는 경우의 수의 합
1로 끝날 경우 -> 이전 자릿수에서 0으로 끝날 경우의 수

점화식 
dp[i][0] = dp[i-1][0] + dp[i-1][1]
dp[i][1] = dp[i-1][0]
"""

n = int(input())
dp = [[0] * 2 for _ in range(n+1)]
dp[1][0], dp[1][1] = 0, 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))
