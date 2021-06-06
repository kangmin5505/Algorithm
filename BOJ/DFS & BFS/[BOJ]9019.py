# DSLR
"""
BFS
풀이 방법
- D : n*2%10000
- S : n-1 if n-1 == 0 n=9999
- L : 왼쪽으로 한 칸씩 
- R : 오른쪽으로 한 칸씩

PyPy3 제출
"""
from collections import deque


def BFS(start):
    dQ = deque()
    res = ''
    visited[start] = True
    dQ.append((start, res))

    while dQ:
        now, res = dQ.popleft()

        if now == b:
            print(res)
            break
        else:
            D = now*2 % 10000
            S = now-1 if now != 0 else 9999
            L = (now//1000) + (now % 1000*10)
            R = (now//10) + now % 10*1000
            if not visited[D]:
                visited[D] = True
                dQ.append((D, res + 'D'))
            if not visited[S]:
                visited[S] = True
                dQ.append((S, res + 'S'))
            if not visited[L]:
                visited[L] = True
                dQ.append((L, res + 'L'))
            if not visited[R]:
                visited[R] = True
                dQ.append((R, res + 'R'))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        visited = [False] * 10001

        res = ''
        BFS(a)
