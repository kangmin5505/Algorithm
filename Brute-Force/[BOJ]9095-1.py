# 1, 2, 3 더하기
# 재귀함수 사용

def dfs(n):
    global cnt
    if n < 0:
        return

    if n == 0:
        cnt += 1
        return

    dfs(n-1)
    dfs(n-2)
    dfs(n-3)


for tc in range(int(input())):
    n = int(input())

    cnt = 0
    dfs(n)
    print(cnt)
