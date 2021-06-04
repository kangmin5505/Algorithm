# 제한시간(m) 보다 커지면 return
# L == n 이면 확인
import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def DFS(L, score, time):
    global result

    if time > m:
        return
    if L == n:
        if result < score:
            result = score
    else:
        DFS(L+1, score+problem_score[L], time+problem_time[L])
        DFS(L+1, score, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    problem_score = list()
    problem_time = list()
    for _ in range(n):
        ps, pt = map(int, input().split())
        problem_score.append(ps)
        problem_time.append(pt)

    result = 0
    DFS(0, 0, 0)
    print(result)
