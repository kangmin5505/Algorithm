# # 괄호
# """
# Dynamic Programming

# 점화식
# - dp[n] = dp[k-2]*dp[n-k] (k=2~n)
# """
# tc = int(input())

# max_val = 5000
# div = 1000000007
# dp = [0] * (max_val+1)
# dp[0] = 1

# for i in range(2, max_val+1, 2):
#     for j in range(2, i+1, 2):
#         dp[i] += (dp[j-2]*dp[i-j]) % div

# for _ in range(tc):
#     n = int(input())
#     print(dp[n])

# 괄호
"""
Dynamic Programming

풀이 방법
- ()는 올바른 괄호, S가 올바른 괄호면 (S)도 올바른 괄호, S와 T가 올바른 괄호면 ST도 올바른 괄호
- 위 세가지 경우를 활용
- dp[n] = dp[k-2] * dp[n-k] (k = 2~n)
    -> dp[k-2]의 의미는 올바른 괄호인 S를 괄호로 감싼 것 '(S)'
    -> dp[n-k]의 의미는 올바른 괄호인 '(S)'와 올바른 괄호인 T를 붙여 '(S)T'를 만든 것
    -> 강제로 올바른 괄호인 ()를 붙여 그 안에 든 괄호가 
       (k-2개일 때 올바른 괄호의 갯수 * 나머지 괄호가 n-k일 때의 올바른 괄호의 갯수)를 하면 
       괄호가 n개일 때 올바른 괄호의 갯수가 나온다
"""
import sys

# input = sys.stdin.readline

tc = int(input())
max_val = 5000
div = 1000000007
dp = [0] * (max_val+1)
dp[0] = 1

for i in range(2, max_val+1, 2):
    for j in range(2, i+1, 2):
        # S와 T의 갯수를 변경시키면서 누적
        dp[i] += (dp[j-2] * dp[i-j]) % div

for _ in range(tc):
    n = int(input())
    # 또 div로 나눠주는 이유는 dp[i]의 값을 누적해서 더해주다 보면 div 값을 넘어갈 수 있기 때문
    print(dp[n] % div)
