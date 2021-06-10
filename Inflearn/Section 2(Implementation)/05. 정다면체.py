# 합을 저장하는 리스트 생성
# 리스트에서 최댓값을 구해서 그 값과 같은 숫자 출력

import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 2(Implementation)\input.txt", "rt")

n, m = map(int, input().split())
check = [0] * (n+m+1)

for i in range(1, n+1):
    for j in range(1, m+1):
        check[i+j] += 1

max_val = 0
for i in range(1, n+m+1):
    if check[i] > max_val:
        max_val = check[i]

for i in range(1, n+m+1):
    if check[i] == max_val:
        print(i, end=' ')