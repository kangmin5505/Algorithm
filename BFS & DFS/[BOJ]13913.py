# 숨바꼭질 4
"""
BFS
역추적
"""
from collections import deque


def path(now):
 array = []
  temp = now
   for _ in range(time[now] + 1):
        array.append(temp)
        temp = move[temp]

    return array[::-1]


def bfs(start):
    q = deque()
    q.append(start)
    time[start] = 0

    while q:
        now = q.popleft()

        if now == target:
            return time[now], path(now)

        for nxt in [now * 2, now - 1, now + 1]:
            if 0 <= nxt < max_size and time[nxt] == -1:
                q.append(nxt)
                time[nxt] = time[now] + 1
                move[nxt] = now


start, target = map(int, input().split(' '))

max_size = 100001
time = [-1] * max_size
# 역추적할 저장소 생성
# 0으로 설정 시 time[0] = time[0] + 1의 반례가 생김
move = [-1] * max_size

min_time, movelist = bfs(start)

print(min_time)
print(' '.join(map(str, movelist)))
