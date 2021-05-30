# 괄호
"""
Dynamic Programming

점화식
- dp[n] = dp[k-2]*dp[n-k] (k=2~n)
"""
tc = int(input())

max_val = 5000
div = 1000000007
dp = [0] * (max_val+1)
dp[0] = 1

for i in range(2, max_val+1, 2):
    for j in range(2, i+1, 2):
        dp[i] += (dp[j-2]*dp[i-j]) % div

for _ in range(tc):
    n = int(input())
    print(dp[n])
