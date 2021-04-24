def bfs(x):
    if x > 11:
        return

    print(x)
    bfs(x+1)
    print(x-1 if x-1 > 0)


bfs(0)
