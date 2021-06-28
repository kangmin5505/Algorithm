import sys

# sys.stdin = open(
#     "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")


k, n = map(int, input().split())
data = [int(input()) for _ in range(k)]
left = 0
right = max(data)
ans = 0

while left <= right:
    mid = (left + right) // 2
    temp_sum = 0 
    for num in data:
        temp_sum += num//mid
    
    if temp_sum >= n:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)