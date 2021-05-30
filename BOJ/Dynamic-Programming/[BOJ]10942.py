# 팰린드롬?
"""
Dynamic Programming

해결 방법
- 1개일 때, 2개일 때, 3개 이상일 때를 나누어서 확인
- 3개일 때는 확인하는 두 수의 값이 같고 그 사이에 있는 값들이 팰린드롬이면 팰린드롬이다
"""
n = int(input())
data = [0] + list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]

# 1개일 때
for i in range(1, n+1):
    dp[i][i] = 1

# 2개일 때
for i in range(1, n):
    if data[i] == data[i+1]:
        dp[i][i+1] = 1

# 3개일 때(숫자가 3개면 첫 번째와 마지막 사이의 거리는 2임)
for length in range(2, n):
    for i in range(1, n+1-length):
        if data[i] == data[i+length] and dp[i+1][i+length-1] == 1:
            dp[i][i+length] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])
