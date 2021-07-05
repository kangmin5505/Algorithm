# 네트워크 선 자르기(Top-Down)
"""
Dynamic Programming
Top-Down 방식은 재귀와 메모이제이션을 사용
- 점화식
dp[i] = dfs(i-1) + dfs(i-2)
"""


def dfs(length):
    if dp[length] > 0:
        return dp[length]
    if length == 1 or length == 2:
        return length
    else:
        dp[length] = dfs(length-1) + dfs(length-2)
        return dp[length]


n = int(input())

dp = [0] * (n+1)
print(dfs(n))
