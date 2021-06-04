# itertools 사용
from itertools import permutations

n, f = map(int, input().split())
b = [1]*n
for i in range(1, n-1):
    b[i] = b[i-1]*(n-i)//i

for nums in permutations(range(1, n+1), 4):
    total = 0
    for i in range(n):
        total += nums[i]*b[i]
    if total == f:
        # print(*nums)
        for i in nums:
            print(i, end=' ')
        break
