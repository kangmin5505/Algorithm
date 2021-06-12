import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')

n = int(input())
arr_1 = list(map(int, input().split()))
m = int(input())
arr_2 = list(map(int, input().split()))

p1, p2 = 0, 0
ans = []

while (p1<n and p2<m):
    if arr_1[p1] < arr_2[p2]:
        ans.append(arr_1[p1])
        p1 += 1
    else:
        ans.append(arr_2[p2])
        p2 += 1

if p1 == n:
    ans += arr_2[p2:]
else:
    ans += arr_1[p1:]

for x in ans:
    print(x, end=' ')