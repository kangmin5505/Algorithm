# 퇴사2
import sys
sys.stdin = open('C:\github\Algorithm\Dynamic-Programming\input.txt', 'rt')

# 퇴사2
# 기본원리는 해당날짜에 일을 처리하면, 해당날짜 + 걸리는 시간에 price가 쌓이는 것

# import sys
# input = sys.stdin.readline

n = int(input())
# 가독성을 위해 인덱스를 1부터 설정하기 위함
time = [0]
price = [0]
# 인덱스는 1부터 시작하고, 적립금(dp)을 퇴사하는 날짜에 받아도 되기 때문에 n+2
dp = [0] * (n+2)

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

# date이전의 최대 적립금
M = 0

for date in range(1, n+1):
    end_date = date + time[date]
    M = max(M, dp[date])

    if end_date > n+1:
        continue
    dp[end_date] = max(dp[end_date], M + price[date])

print(dp)
print(max(dp))
