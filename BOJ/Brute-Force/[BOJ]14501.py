# 퇴사
# 퇴사일부터 시작

import sys
import copy
sys.stdin = open('C:\github\Algorithm\Brute-Force\input.txt', 'rt')

n = int(input())

# 가독성을 높이기 위해 인덱스 1부터 시작
time = [0]
price = [0]


for _ in range(n):
    t, c = map(int, input().split())
    time.append(t)
    price.append(c)

max_value = copy.deepcopy(price)

# 마지막 날부터 시작
for date in range(n, 0, -1):
    end_date = time[date] + date
    # date에 걸리는 시간을 더했을 때 퇴사날짜 이후면 그 날짜의 금액은 현재까지의 최댓값 대입
    if end_date > n + 1:
        max_value[date] = 0
    else:
        # 해당 date의 금액과 date + 걸리는 시간의 값을 더했을 때와 현재까지의 최댓값을 비교
        max_value[date] = price[date] + max_value[end_date]

print(max(max_value))
