# 가장 긴 증가하는 부분 수열(dynamic programming)
n = 6
array = [10, 20, 10, 30, 20, 50]
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
            
print(max(dp))

# 가장 긴 증가하는 부분 수열(Binary Search)
from bisect import bisect_left

n = 6
array = [10, 20, 10, 30, 20, 50]
dp = [array[0]]

for i in range(1, n):
    if array[i] > dp[-1]:
        dp.append(array[i])
    else:
        idx = bisect_left(dp, array[i])
        dp[idx] = array[i]
        
print(len(dp))