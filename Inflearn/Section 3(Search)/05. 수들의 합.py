import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
p1, p2 = 0, 1
total = arr[0]
cnt = 0

while True:
    if total == m:
        total -= arr[p1]
        p1 += 1
        cnt += 1
    elif total > m:
        total -= arr[p1]
        p1 += 1
    elif total < m:
        if p2 < n:
            total += arr[p2]
            p2 += 1
        else:
            break
    
print(cnt)
