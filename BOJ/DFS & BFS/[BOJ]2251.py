# 물통
"""
BFS

풀이 방법
- A=>B, A=>C, B=>A, B=>C, C=>A, C=>B로 물을 따르는 경우로 나눔
- 물을 따를 때는 물을 붓는 곳과 물이 담길 곳 중 작은 값으로 설정
- 체크 리스트 생성
"""
from collections import deque


def pour(x, y):

    if not check[x][y]:
        check[x][y] = True
        dQ.append((x, y))


def BFS():
    check[0][0] = True
    dQ.append((0, 0))

    while dQ:
        x, y = dQ.popleft()
        z = c - x - y

        # x가 0일 때 z에 있는 물의 양 추가
        if x == 0:
            res.append(z)

        # a에서 b로 따를 때
        if x > 0 and b > y:
            water = min(x, b-y)
            pour(x-water, y+water)
        # a에서 c로 따를 때
        if x > 0 and c > z:
            water = min(x, c-z)
            pour(x-water, y)
        # b에서 a로 따를 때
        if y > 0 and a > x:
            water = min(y, a-x)
            pour(x+water, y-water)
        # b에서 c로 따를 때
        if y > 0 and c > z:
            water = min(y, c-z)
            pour(x, y-water)
        # c에서 a로 따를 때
        if z > 0 and a > x:
            water = min(z, a-x)
            pour(x+water, y)
        # c에서 b로 따를 때
        if z > 0 and b > y:
            water = min(z, b-y)
            pour(x, y+water)


a, b, c = map(int, input().split())
check = [[False] * (c+1) for _ in range(c+1)]
dQ = deque()

res = []
BFS()

res.sort()
for x in res:
    print(x, end=' ')
