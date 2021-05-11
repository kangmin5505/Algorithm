from collections import deque


def bfs(start):
    clip = 0
    q = deque()
    q.append((start, clip))
    visited[(start, clip)] = 0

    while q:
        board, clip = q.popleft()

        if board == target:
            return visited[(board, clip)]

        if (board, board) not in visited.keys():
            visited[(board, board)] = visited[(board, clip)] + 1
            q.append((board, board))
        if (board - 1, clip) not in visited.keys():
            visited[(board - 1, clip)] = visited[(board, clip)] + 1
            q.append((board - 1, clip))
        if (board + clip, clip) not in visited.keys():
            visited[(board + clip, clip)] = visited[(board, clip)] + 1
            q.append((board + clip, clip))


target = int(input())
visited = dict()
start = 1

answer = bfs(start)
print(answer)
