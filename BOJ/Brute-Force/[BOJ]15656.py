# N과 M(7)

def make_product(answer):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for num in data:
        answer.append(num)
        make_product(answer)
        answer.pop()


n, m = map(int, input().split(' '))

data = list(map(int, input().split(' ')))
data.sort()

answer = []
make_product(answer)
