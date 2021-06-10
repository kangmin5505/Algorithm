import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 2(Implementation)\input.txt", "rt")

tc = int(input())

ans = 0
for _ in range(tc):
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    a, b, c = data

    if a == b == c:
        temp = 10000 + a*1000
    elif a == b or b == c:
        temp = 1000 + b*100
    else:
        temp = a*100
    if ans < temp:
        ans = temp

print(ans)
