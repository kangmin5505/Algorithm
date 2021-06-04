# 조합
import sys
from itertools import combinations

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")

# L == 깊이, s == 시작지점


def DFS(L, s):
    global res
    if L == m:
        total = 0
        for hx, hy in home:
            # for j in range(len(home)):
            # hx = home[j][0]
            # hy = home[j][1]
            temp = int(1e9)
            for i in cb:
                px = pizza[i][0]
                py = pizza[i][1]
                temp = min(temp, abs(hx-px)+abs(hy-py))
            total += temp
        if res > total:
            res = total
    else:
        for i in range(s, len(pizza)):
            cb.append(i)
            # cb[L] = i
            DFS(L+1, i+1)
            cb.pop()


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
home = []
pizza = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            pizza.append((i, j))

cb = []
# cb = [0]*m
res = int(1e9)
DFS(0, 0)

print(res)
