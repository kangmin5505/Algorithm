from collections import deque


def reverse():
    graph = [[] for _ in range(n+1)]
    for a, b, c in roads:
        graph[a].append((b, c))


def solution(n, start, end, roads, traps):
    answer = 0
    q = deque()
    q.append((start, answer))

    graph = [[] for _ in range(n+1)]
    for a, b, c in roads:
        graph[a].append((b, c))

    while q:
        v, cost = q.popleft()

        if v == end:
            answer = cost
            break

        if v in traps:
            reverse()

        for b, c in graph[v]:
            print(b, c)
            q.append((b, cost + c))

    return answer


n = 3
start = 1
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]
print(solution(n, start, end, roads, traps))
