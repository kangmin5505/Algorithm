# 점프 게임
"""
BFS

풀이 방법
- 1) j+1 이동, 2) j-1 이동, 3) i+1 or i-1 이후 j+k 이동
- if j > n-1 클리어 
"""
import sys
from collections import deque

sys.stdin = open("C:\github\Algorithm\BOJ\DFS & BFS\input.txt", "rt")

def BFS(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    visited = [[False] * n for _ in range(2)]
    visited[start_x][start_y] = True
    visited[start_x+1][start_y] = True
    ans = 0
    # visitable 이하로는 이동 못 함
    visitable = 0

    while q:
        # BFS의 단계별 층의 갯수 만큼만 실행
        for _ in range(len(q)):
            x, y = q.popleft()
            for d in range(4):
                next_x = x + dx[d]
                next_y = y + dy[d]
                if 0 <= next_x < 2 and visitable < next_y:
                    if next_y > n-1:
                        ans = 1
                        return ans
                    else:
                        if board[next_x][next_y] == 1 and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y))
        visitable += 1
    return ans
                    

if __name__ == "__main__":
    n, k = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(2)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, k, k]

    ans = BFS(0, 0)
    print(ans)
    