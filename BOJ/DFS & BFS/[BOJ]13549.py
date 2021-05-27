# 숨바꼭질 3

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
            now_1 = now * 2
            now_2 = now - 1
            now_3 = now + 1

            # 곱셈이 먼저 와야 하는 이유(반례 : start = 1, target =2)
            # 덧셈이 먼저 처리 되면 1초가 걸리지만 곱셈이 먼저 처리 되면 0초가
            if now_1 <= 100000:
                q.append((now_1, count))
            if now_2 <= 100000:
                q.append((now_2, count + 1))
            if now_3 >= 0:
                q.append((now_3, count + 1))

    return count


start, target = map(int, input().split(' '))
visited = [False] * 100001

print(bfs(start))
