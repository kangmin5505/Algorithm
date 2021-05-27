# 1, 2, 3 더하기
# dp사용

n = int(input())

# 1, 2, 3 만들 수 있는 수 정의(0은 제외)
dp = [0, 1, 2, 4]
for i in range(4, 12):
    # 점화식 = dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    dp.append(dp[i-3] + dp[i-2] + dp[i-1])

for _ in range(n):
    num = int(input())
    print(dp[num])
