# N과 M(9)

def solution():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    # 지역변수이므로 재귀함수의 깊이마다 값이 다름
    before_num = 0
    for idx in range(n):
        if not visited[idx] and data[idx] != before_num:
            answer.append(data[idx])
            visited[idx] = True
            before_num = data[idx]
            solution()
            visited[idx] = False
            answer.pop()


n, m = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
data.sort()
visited = [False] * n

answer = []
solution()
