import sys
from collections import deque

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 5(Data_Structure)\input.text", "rt")

n, k = map(int, input().split(' '))

princes = list(range(1, n+1))
princes = deque(princes)

while True:
    if len(princes) == 1:
        break
    else:
        for i in range(k-1):
            princes.append(princes.popleft())
        princes.popleft()

print(princes[0])
