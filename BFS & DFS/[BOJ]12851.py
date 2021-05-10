# 숨바꼭질 2
"""
BFS
"""
from collections import deque


def bfs(start):
    if start >= target:
        return (start - target), 1

    q = deque()
    q.append(start)
    time[start] = 0
    count = 0

    while q:
        now = q.popleft()

        if now == target:
            count += 1
            continue

        for nxt in [now * 2, now + 1, now - 1]:
            if 0 <= nxt < max_size:
                # time[nxt] == time[now] + 1
                # 이미 nxt가 대기열에 올라가 있더라도, 같은 시간이 걸린다면 제한조건을 만족
                if time[nxt] == -1 or time[nxt] == time[now] + 1:
                    q.append(nxt)
                    time[nxt] = time[now] + 1

    return time[target], count


start, target = map(int, input().split(' '))
max_size = 100001
time = [-1] * max_size

min_time, count = bfs(start)

print(min_time)
print(count)
