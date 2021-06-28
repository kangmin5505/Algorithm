# import sys

# sys.stdin = open(
#     "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")



def count_dvd(capacity):
    temp_sum = 0
    cnt = 1
    for x in data:
        temp_sum += x
        if temp_sum > capacity:
            cnt += 1
            temp_sum = x
    return cnt




n, m = map(int, input().split())
data = list(map(int, input().split()))

ans = int(1e9)
left = min(data)
right = sum(data)

while left <= right:
    mid = (left + right) // 2
    temp_val = count_dvd(mid)

    if temp_val <= m:
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)