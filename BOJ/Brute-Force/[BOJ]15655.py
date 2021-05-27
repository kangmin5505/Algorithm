# N과 M(6)

def make_combinations(answer, idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(idx, n):
        if data[i] in answer:
            continue
        answer.append(data[i])
        make_combinations(answer, i+1)
        answer.pop()


n, m = map(int, input().split(' '))

data = list(map(int, input().split(' ')))
data.sort()

answer = []
make_combinations(answer, 0)
