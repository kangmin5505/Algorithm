# import sys

# sys.stdin = open(
#     "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")


"""
1. 오름차순으로 정렬 후 첫 번째 값과 마지막 값 +1, -1
2. m번 높이 조정 후 max-min을 출력
"""

n = int(input())
heights = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    heights.sort()
    heights[0] += 1
    heights[-1] -= 1

print(max(heights)-min(heights))