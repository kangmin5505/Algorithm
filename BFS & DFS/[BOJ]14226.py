# 이모티콘
"""
BFS
세 가지 조건으로 나누어서 실행하다가 답이 나오면 출력
"""
from collections import deque


def bfs(start):
    time = 0
    clip = 0
    q = deque()
    q.append((start, clip, time))

    while q:
        now, clip, time = q.popleft()
        print(now)
        if now == target:
            return time

        # 화면에서 한 개씩 제거할 경우
        if now > target:
            q.append((now - 1, clip, time + 1))
        else:
            q.append((now - 1, clip, time + 1))

            if clip < 1:
                clip = now
                q.append((now, clip, time + 1))
            else:
                # 클립보드에 저장할 경우
                q.append((now, now, time + 1))
                # 화면에 붙여넣기 할 경우
                q.append((now + clip, clip, time + 1))


target = int(input())

start = 1
answer = bfs(start)
print(answer)
