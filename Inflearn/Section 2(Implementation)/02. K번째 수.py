import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 2(Implementation)\input.txt", "rt")

tc = int(input())

for i in range(tc):
    n, s, e, k = map(int, input().split())
    data = list(map(int, input().split()))
    temp = data[s-1:e]
    temp.sort()

    print(f"#{i+1} {temp[k-1]}")