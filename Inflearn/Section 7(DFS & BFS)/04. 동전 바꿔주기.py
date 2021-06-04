# 동전 갯수 만큼 for문을 실행
# 동전을 0개, 1개, 2개, ... , n개 사용했을 경우로 나눠서 풀이

def DFS(L, total):
    global cnt

    if total > t:
        return
    if L == k:
        if total == t:
            cnt += 1
    else:
        for i in range(n[L]+1):
            DFS(L+1, total+p[L]*i)


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    p = list()
    n = list()

    for _ in range(k):
        a, b = map(int, input().split())
        p.append(a)
        n.append(b)

    cnt = 0
    DFS(0, 0)
    print(cnt)
