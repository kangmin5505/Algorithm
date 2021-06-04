# DFS 통한 완전탐색
# (a + b)**n 원리 이용(이항계수)
#   => (a+b)**2 = a**2 + 2ab + b**2
#   => (a+b)**3 = a**3 + 3a**2b + 3ab**2 + b**3
import sys


def DFS(L, total):
    # 완료 조건
    if L == n and total == f:
        for num in result:
            print(num, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                result.append(i)
                DFS(L+1, total+(b[L]*result[L]))
                visited[i] = False
                result.pop()


if __name__ == "__main__":
    n, f = map(int, input().split())
    b = [1] * n
    visited = [False] * (n+1)
    result = []
    for i in range(1, n-1):
        b[i] = b[i-1]*(n-i)//i
    DFS(0, 0)
