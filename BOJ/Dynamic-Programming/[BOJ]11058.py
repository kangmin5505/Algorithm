# 크리보드
"""
dynamic programming
- 1번 버튼만 선택할 경우를 초기화 시킨 후
- 2, 3, 4번 버튼은 한 번에 묶어서 i + 3번 째부터 실행한다고 가정
"""
n = int(input())

# dp[i] = i로 초기화 => 처음부터 1번 버튼만 선택할 경우
dp = [int(x) for x in range(n + 1)]

# i는 1 ~ (n-3) 까지 확인
for i in range(1, n - 2):
    for j in range(i + 3, n + 1):
        dp[j] = max(dp[i] * (j - 1 - i), dp[j])

print(dp[n])

# 다른 답안

# n = int(input())
# dp = [x for x in range(n + 1)]

# for i in range(7, n + 1):
#     dp[i] = max(dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4)

# print(dp[n])
