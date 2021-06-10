import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 2(Implementation)\input.txt", "rt")

n, k = map(int, input().split())
cards = list(map(int, input().split()))
ans = set()

for i in range(n-2):
    for j in range(i+1, n-1):
        for x in range(j+1, n):
            ans.add(cards[i]+cards[j]+cards[x])

ans = sorted(list(ans), reverse=True)
print(ans[k-1])
