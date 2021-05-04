# N과 M(8)

def make_combinations_with_replacement(answer, idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(idx, n):
        answer.append(data[i])
        make_combinations_with_replacement(answer, i)
        answer.pop()


n, m = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
data.sort()

answer = []
make_combinations_with_replacement(answer, 0)
