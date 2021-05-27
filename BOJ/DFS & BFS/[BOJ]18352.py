# 특정 거리의 도시 찾기

# bfs방법으로 각 node의 거리를 최소거리로 나타내고, 최소거리가 k인 node를 result 리스트에 append하기
from collections import deque


def bfs(k, start):
    result = list()
    visited[start] = True
    queue = deque()
    queue.append((start, 0))

    while queue:
        now, dist = queue.pop()

        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                distance = dist + 1

                if distance == k:
                    result.append(next_node)

                queue.append((next_node, distance))

    return result


n, m, k, start = map(int, input().split())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = bfs(k, start)

if len(result) < 1:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)
