# 팰린드롬?
"""
dynamic programming

Solution
- i번째부터 n번째까지 팰린드롬인 경우 1, 아닐 경우 0 으로 선언한 2차원 dp테이블 생성
"""
import sys

sys.stdin = open('C:\github\Algorithm\BOJ\Dynamic-Programming\input.txt', 'rt')

n = int(input())
data = [0] + [int(x) for x in input().split()]

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i, n+1):
        if data[i:j+1] == data[j:i-1:-1]:
            dp[i][j] = 1


for i in dp:
    print(i)
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])
