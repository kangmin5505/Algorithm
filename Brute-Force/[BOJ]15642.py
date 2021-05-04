# N과 M(1)

def permu():

    if len(data) == m:
        print(' '.join(map(str, data)))
        return

    for i in range(1, n+1):
        if i in data:
            continue
        data.append(i)
        permu()
        data.pop()


n, m = map(int, input().split())

data = []
permu()
