# 가장 긴 증가하는 부분 수열4
"""
dynamic programming
현재 숫자의 이전 숫자들 중 가장 큰 dp값 + 1 해주고
dp리스트를 활용하여 길이에서 -1씩 해주며 저장한 후 오름차순으로 정렬시킨다
"""

n = int(input())
data = list(map(int, input().split(' ')))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

length = max(dp)
answer = []
for i in range(n-1, -1, -1):
    if length == 0:
        break

    if dp[i] == length:
        answer.append(data[i])
        length -= 1

answer.sort()
print(max(dp))
print(' '.join(map(str, answer)))
