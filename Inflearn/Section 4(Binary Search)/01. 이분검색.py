import sys

sys.stdin = open(
    "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")


def binary_search(start, end):
    mid = (start + end) // 2

    if data[mid] == target:
        return mid+1
    elif data[mid] > target:
        return binary_search(start, mid-1)
    else:
        return binary_search(mid+1, end)


n, target = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
start = 0
end = n-1
idx = binary_search(start, end)
print(idx)