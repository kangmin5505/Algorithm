# 스택구조 사용
# import time

def DFS(L):
    global answer, cnt
    if L == m:
        for i in answer:
            print(i, end=' ')
        cnt += 1
        print()
    else:
        for i in range(1, n+1):
            answer.append(i)
            DFS(L+1)
            answer.pop()


n, m = map(int, input().split())

cnt = 0
answer = []
# start_time = time.time()
DFS(0)
print(cnt)
# end_time = time.time() - start_time
# print(end_time)
