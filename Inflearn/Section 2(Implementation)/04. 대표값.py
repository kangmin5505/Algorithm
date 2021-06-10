# avg, index, score
# 평균과의 차이가 더 적을 때, 같을 때

import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 2(Implementation)\input.txt", "rt")

n = int(input())
data = list(map(int, input().split()))
avg = sum(data)/n
# 소수 첫째짜리 반올림
# round()는 0.5일 경우 짝수가 되도록 설정되어 있음
avg = int(avg+0.5)

min_val = int(1e9)
for idx, num in enumerate(data, 1):
    temp = abs(num - avg)
    if temp < min_val:
        min_val = temp
        score = num
        ans = idx
    elif temp == min_val:
        if score < num:
            score = num
            ans = idx

print(avg, ans)
