# 퍼즐
"""
BFS

풀이 방법
- 문자열을 좌표로 나타내기(x = idx//3, y = idx%3)
- 문자열 => 행렬(네 방향 확인) => 문자열 
- 방문확인(2차원 행렬로 확인하기 어려움으로 dict로 확인)
"""
from collections import deque


def BFS():
    dQ = deque()
    dQ.append(graph)
    cnt[graph] = 0

    while dQ:
        s = dQ.popleft()

        if s == '123456780':
            return cnt[s]

        idx = s.find('0')
        x = idx//3
        y = idx % 3

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                nidx = nx*3 + ny
                ns = list(s)
                ns[idx], ns[nidx] = ns[nidx], ns[idx]
                ns = ''.join(ns)

                if not cnt.get(ns):
                    cnt[ns] = cnt[s] + 1
                    dQ.append(ns)


n = 3
graph = ''
for _ in range(3):
    data = input()
    data = data.replace(' ', '')
    graph += data

cnt = dict()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = BFS()
if ans == None:
    print(-1)
else:
    print(ans)
