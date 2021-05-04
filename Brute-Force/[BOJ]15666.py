# N과 M(10)

def solution(idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    before_num = 0
    for i in range(idx, n):
        if data[i] != before_num:
            answer.append(data[i])
            before_num = data[i]
            solution(i+1)
            answer.pop()


n, m = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
data.sort()

answer = []
solution(0)
