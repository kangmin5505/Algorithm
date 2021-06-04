# 음수인 경우 제외

def DFS(L, total):
    if L == k:
        if 0 < total <= max_val:
            w.add(total)
    else:
        DFS(L+1, total+data[L])
        DFS(L+1, total-data[L])
        DFS(L+1, total)


if __name__ == "__main__":
    k = int(input())
    data = list(map(int, input().split()))
    max_val = sum(data)
    w = set()

    DFS(0, 0)
    print(max_val - len(w))
