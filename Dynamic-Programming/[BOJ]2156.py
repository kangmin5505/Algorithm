# 포도주 시식
"""
dynamic programming
n >= 3 부터는 n번째 숫자가 첫 번째가 되는지 두 번째가 되는지 세 번째가 되는지 경우의 수로 나누어서 확인
if n >= 3:
    # n번째 숫자가 첫 번째인 경우, 두 번째인 경우, 세 번째인 경우
    dp[n] = max(data[n] + dp[n-2], data[n] + data[n-1] + dp[n-3], dp[i-1])
"""
import sys

sys.stdin = open('C:\github\Algorithm\Dynamic-Programming\input.txt', 'rt')

n = int(input())
data = [0]  # 인덱스 1부터 시작
for _ in range(n):
    data.append(int(input()))

dp = [0] * (n+1)
dp[1] = data[1]
if n >= 2:
    dp[2] = data[1] + data[2]

    for i in range(3, n+1):
        case_1 = data[i] + dp[i-2]
        case_2 = data[i] + data[i-1] + dp[i-3]
        case_3 = dp[i-1]
        dp[i] = max(case_1, case_2, case_3)

print(max(dp))
