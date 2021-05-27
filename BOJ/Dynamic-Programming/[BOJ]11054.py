# 가장 긴 바이토닉 부분 수열
"""
dynamic programming
- 첫 번째 숫자부터 시작해서 가장 긴 부분 수열 dp 생성
- 마지막 숫자부터 시작해서 가장 긴 부분 수열 dp 생성
- 둘이 합한 후 가장 큰 값 -1
"""
import sys

sys.stdin = open('C:\github\Algorithm\Dynamic-Programming\input.txt', 'rt')

n = int(input())
data = list(map(int, input().split(' ')))

# 첫 번째 숫자부터 시작
dp1 = [1] * n
# 마지막 숫자부터 시작
dp2 = [1] * n
answer = [0] * n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n-2, -1, -1):
    for j in range(i, n):
        if data[i] > data[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(n):
    answer[i] = dp1[i] + dp2[i] - 1

print(max(answer))
