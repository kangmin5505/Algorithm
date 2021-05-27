# 퇴사
# 1일부터 시작

import sys
import copy
sys.stdin = open("C:\github\Algorithm\Brute-Force\input.txt", 'rt')


n = int(input())

# 가독성을 위해 인덱스 1부터 시작하기 위함
time = [0]
price = [0]
for _ in range(n):
    t, c = map(int, input().split())
    time.append(t)
    price.append(c)
answer = copy.deepcopy(price)

# 첫째 날부터 시작
for date in range(1, n+1):
    if date + time[date] > n+1:
        answer[date] = 0
        continue

    for next_date in range(date + time[date], n+1):
        answer[next_date] = max(
            answer[next_date], answer[date] + price[next_date])

print(max(answer))
