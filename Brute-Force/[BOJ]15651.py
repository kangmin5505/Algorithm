# N과 M(3)

def make_product(data):
    if len(data) == m:
        print(' '.join(map(str, data)))
        return

    for i in range(1, n+1):
        data.append(i)
        make_product(data)
        data.pop()


n, m = map(int, input().split(' '))

data = []
make_product(data)
