# visited
from collections import deque


def BFS(start, end):
    dQ = deque()
    dQ.append(start)
    visited[start] = 0

    while dQ:
        now = dQ.popleft()

        if now == end:
            break

        for x in (now+1, now-1, now+5):
            if 0 < x <= 10000 and visited[x] == 0:
                visited[x] = visited[now] + 1
                dQ.append(x)

    return visited[end]


s, e = map(int, input().split())
visited = [0] * 10001

result = BFS(s, e)
print(result)
