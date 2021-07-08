import heapq
import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 5(Data_Structure)\input.text", "rt")

hq = []
while True:
    n = int(input())
    
    if n == -1:
        break

    if n == 0:
        if len(hq) == 0:
            print(-1)
            break
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, n)
    