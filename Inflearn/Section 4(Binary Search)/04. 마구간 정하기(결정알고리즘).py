# import sys

# sys.stdin = open(
#     "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")

def count_horses(length):
    cnt = 1
    end_point = x_list[0]

    for i in range(1, n):
        if x_list[i] - end_point >= length:
            cnt += 1
            end_point = x_list[i]

    return cnt


n, horses = map(int, input().split())
x_list = [int(input()) for _ in range(n)]
x_list.sort()

left = 1
right = x_list[-1]


while left <= right:
    mid = (left + right) // 2

    if count_horses(mid) >= horses:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)