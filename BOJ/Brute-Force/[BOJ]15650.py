# N과 M(2)

def permu(num):
    if len(data) == m:
        print(' '.join(map(str, data)))
        return

    for i in range(num, n+1):
        if i in data:
            continue
        data.append(i)
        permu(i)
        data.pop()


n, m = map(int, input().split(' '))

data = []
permu(1)
