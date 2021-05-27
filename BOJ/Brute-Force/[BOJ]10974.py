# 모든 순열
# next_permutation 알고리즘

def next_permutation(permu):
    length = len(permu)
    k = -1
    for i in range(length-1):
        if permu[i] < permu[i+1]:
            k = i

    if k == -1:
        return []

    for j in range(k+1, length):
        if permu[k] < permu[j]:
            m = j

    permu[k], permu[m] = permu[m], permu[k]
    temp = permu[k+1:]
    temp.sort()
    permu = permu[:k+1] + temp

    return permu


n = int(input())
data = [i for i in range(1, n+1)]

while True:
    # print(' '.join(map(str, data)))
    print(*data)
    data = next_permutation(data)
    if not data:
        break
