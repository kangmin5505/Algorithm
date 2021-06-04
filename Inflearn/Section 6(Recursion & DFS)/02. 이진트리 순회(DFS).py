def DFS(x):
    if x > 7:
        return
    else:
        # 전위순회
        # print(x, end=' ')
        DFS(x*2)
        # 중위순회
        # print(x, end= ' ')
        DFS(x*2+1)
        # 후위순회
        # print(x, end=' ')


if __name__ == "__main__":
    DFS(1)
