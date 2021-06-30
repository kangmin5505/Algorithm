import sys
from collections import deque

sys.stdin = open(
    "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")


"""
1. 좌, 우 인덱스를 설정
2. 좌가 작으면 +1 우가 작으면 -1
3. 가져온 값을 비교 값으로 저장
"""

n = int(input())
numbers = list(map(int, input().split()))

q = deque(numbers)
ans = ''
while q:
    left = q.popleft()
    right = q.pop()
    if left < right:
        ans += 'L'