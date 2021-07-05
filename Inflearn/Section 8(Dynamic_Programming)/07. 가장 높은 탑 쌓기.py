# 가장 높은 탑 쌓기
"""
Dynamic Programming
- 해결 방법
밑면의 넓이가 넓은 순서대로 정렬 시킨 후 
i번째 벽돌 이전에 있는 벽돌 중 무게가 가벼운 벽돌의 인덱스 값과 비교해서 높이를 추가해준다
"""
import sys

# sys.stdin = open('C:\Study\Algorithm\Inflearn Algorithm(Python)\Section 8(solution)\input.txt', 'rt')

n = int(input())
data = []
for _ in range(n):
    a, h, w = map(int, input().split())
    data.append((a, h, w))

data.sort(reverse=True)
dp = [0] * n
dp[0] = data[0][1]
res = 0

for i in range(1, n):
    max_h = 0
    for j in range(i):
        if data[i][2] < data[j][2] and max_h < dp[j]:
            max_h = dp[j]
    dp[i] = max_h + data[i][1]

    if res < dp[i]:
        res = dp[i]

print(res)
