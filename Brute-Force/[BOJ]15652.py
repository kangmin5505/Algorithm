# N과 M(4)

def make_combinations_with_replacement(data, num):
    if len(data) == m:
        print(' '.join(map(str, data)))
        return

    for i in range(num, n+1):
        data.append(i)
        make_combinations_with_replacement(data, i)
        data.pop()


n, m = map(int, input().split(' '))

data = []
make_combinations_with_replacement(data, 1)
