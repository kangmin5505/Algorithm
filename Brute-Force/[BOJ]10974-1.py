# 모든 순열
# permutations 사용

from itertools import permutations

n = int(input())
data = [i for i in range(1, n+1)]

permuList = list(permutations(data, n))

for permu in permuList:
    for num in permu:
        print(num, end=' ')
    print()
