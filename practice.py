from itertools import combinations_with_replacement

n, m = map(int, input().split())

a = combinations_with_replacement(range(1, n+1), m)
for i in a:
    print(*i)
