# 합분해
"""
Dynamic Programming

풀이 방법
- n을 0부터 n까지의 수 k개를 활용하여 만들 수 있는 방법의 수는 
  0부터 n까지 k-1개를 사용하여 만들 수 있는 수의 합과 같다
  why? 
  n이 0일 때는 n을 더하고 n이 1일 때는 n-1을 더하고 ... n이 n일 때는 0을 더하면 되기 때문이다
- 위 방법으로 해결할 경우 시간복잡도는 O(K*N**2) 이다
- 하지만 dp[k][n-1] = dp[k-1][0] + dp[k-1][1] + ... + dp[k-1][n-1]
  을 이용하면 
  dp[k][n] = dp[k][n-1] + dp[k-1][n]이 도출되는데
  위의 시간복잡도는 O(K*N)이다
"""
n, k = map(int, input().split())

div = 1000000000
dp = [[0] * (n+1) for _ in range(k+1)]
dp[0][0] = 1

for i in range(1, k+1):
    for j in range(n+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % div


print(dp[k][n] % div)
