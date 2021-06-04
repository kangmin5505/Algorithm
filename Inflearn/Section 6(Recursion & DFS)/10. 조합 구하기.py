# 그 다음 수 부터 시작하는 DFS
# result, cnt

def DFS(L, x):
    global cnt
    # 종료 조건
    if L == m:
        for num in result:
            print(num, end=' ')
        cnt += 1
        print()
    else:
        for i in range(x, n+1):
            result.append(i)
            DFS(L+1, i+1)
            result.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())

    cnt = 0
    result = []
    DFS(0, 1)
    print(cnt)
