# 숨바꼭질
"""
BFS
모든 경우의 수를 확인
"""
from collections import deque


def bfs(start):
    count = 0
    q = deque()
    q.append((start, count))

    while q:
        now, count = q.popleft()

        if now == target:
            return count

        if not visited[now]:
            visited[now] = True
            count += 1
            next_1 = now - 1
            next_2 = now + 1
            next_3 = now * 2

            if next_1 >= 0:
                q.append((next_1, count))
            if next_2 <= 100000:
                q.append((next_2, count))
            if next_3 <= 100000:
                q.append((next_3, count))

    return count


start, target = map(int, input().split(' '))
visited = [False] * 100001
print(bfs(start))
