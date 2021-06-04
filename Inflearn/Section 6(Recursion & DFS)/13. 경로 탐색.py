# 방향 그래프, visited, cnt
import sys

sys.stdin = open(
    'C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 6(Recursion&DFS)\input.txt', 'rt')


def DFS(v):
    global cnt
    # 종료 조건
    if v == n:
        cnt += 1
        # 경로 출력
        # for i in path:
        #     print(i, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if graph[v][i] == 1 and not visited[i]:
                # 경로 출력
                # path.append(i)
                visited[i] = True
                DFS(i)
                # path.pop()
                visited[i] = False


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1

    visited = [False] * (n+1)
    visited[1] = True
    # 경로 출력
    # path = []
    # path.append(1)
    cnt = 0

    DFS(1)
    print(cnt)
