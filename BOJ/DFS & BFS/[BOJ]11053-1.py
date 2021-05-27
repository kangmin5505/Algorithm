# 가장 긴 증가하는 부분 수열

n = int(input())
data = list(map(int, input().split()))
# 각 부분 수열의 길이
dp = [0] * n

# 모든 숫자를 확인
for i in range(1, n):
    # i번째 숫자 이전 숫자를 확인
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)
# 부분 수열이 가장 긴 것을 출력
print(max(dp))
