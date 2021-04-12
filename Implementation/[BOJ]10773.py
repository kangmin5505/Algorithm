# 제로
import sys
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    num = int(input())
    if num != 0:
        data.append(num)
    else:
        data.pop()

print(sum(data))
