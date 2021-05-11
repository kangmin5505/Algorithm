# 1, 2, 3 더하기 3
"""
dynamic programming
"""
import sys

input = sys.stdin.readline


max_size = 100001
div = 1000000009
dp = [[0] * 3 for _ in range(max_size)]
# 1로 끝나는 경우, 2로 끝나는 경우, 3으로 끝나는 경우의 수
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, max_size):
    # 1을 더해 i를 만드는 경우, 1이 마지막에 있으면 안 됌
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % div
    # 2를 더해 i를 만드는 경우, 2가 마지막에 있으면 안 됌
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % div
    # 3을 더해 i를 만드는 경우, 3이 마지막에 있으면 안 됌
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % div


for tc in range(int(input())):
    n = int(input())
    print(sum(dp[n]) % div)
