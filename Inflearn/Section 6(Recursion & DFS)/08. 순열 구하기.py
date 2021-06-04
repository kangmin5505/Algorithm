# visited 리스트 생성
# DFS 체크 후 체크 제거

def DFS(L):
    global cnt
    # 완료조건
    if L == m:
        for i in result:
            print(i, end=' ')
        cnt += 1
        print()
    else:
        for i in range(1, n+1):
            if i not in result:
                result.append(i)
                DFS(L+1)
                result.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    result = []
    cnt = 0
    DFS(0)
    print(cnt)
