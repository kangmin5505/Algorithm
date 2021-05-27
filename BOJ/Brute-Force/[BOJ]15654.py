# N과 M(5)

def make_permutations(answer):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in data:
        if i in answer:
            continue
        answer.append(i)
        make_permutations(answer)
        answer.pop()


n, m = map(int, input().split(' '))

data = list(map(int, input().split(' ')))
data.sort()

answer = []
make_permutations(answer)
