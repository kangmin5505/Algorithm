# 로또

from itertools import combinations

while True:
    n, *data = list(map(int, input().split()))

    if n == 0:
        break

    dataList = list(combinations(data, 6))

    for combi in dataList:
        print(*combi)
    print()
