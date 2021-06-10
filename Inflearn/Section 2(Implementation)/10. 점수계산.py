import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 2(Implementation)\input.txt", "rt")

n = int(input())
data = list(map(int, input().split()))
score = 0
ans = 0
for x in data:
    if x == 1:
        score += 1
        ans += score
    else:
        score = 0

print(ans)