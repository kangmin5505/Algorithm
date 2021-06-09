# 레이저 통신
"""
BFS

풀이 방법
- 한 방향으로 한 번에 갈 수 있는 곳까지 이동한다
- 방향을 바꿨을 때는 현재 위치(x, y) + 1 해주면 된다
"""
import sys
from collections import deque

sys.stdin = open("C:\github\Algorithm\BOJ\DFS & BFS\input.txt", "rt")
# input = sys.stdin.readline

def BFS(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    # 필요한 거울 갯수 저장하는 리스트 생성
    mirror = [[-1] * c for _ in range(r)]
    
    while q:
        x, y = q.popleft()
        for d in range(4):
            next_x = x + dx[d]
            next_y = y + dy[d]
            # 한 방향으로 한 번에 갈 수 있는 곳까지 이동
            while True:
                # 종료 조건
                if next_x < 0 or next_x >= r or next_y < 0 or next_y >= c:
                    break
                if graph[next_x][next_y] == '*':
                    break
                
                # 아직 필요한 거울 갯수를 체크하지 않은 곳이면 실행
                if mirror[next_x][next_y] == -1:
                    # 주의할 점 : 이전 좌표에서 +1 해주는 것이 아닌 while문이 실행하기 시작하는 x, y좌표의 필요한 거울 갯수에서 +1
                    #             => ex) while문이 시작하기 직전의 좌표의 필요한 거울 갯수가 1이면 그 방향의 필요한 거울 갯수는 1+1
                    # 시작점을 -1로 설정하면 처음 실행하는 행과 열들의 필요한 거울 갯수를 0개로 맞출 수 있다
                    mirror[next_x][next_y] = mirror[x][y] + 1
                    q.append((next_x, next_y))
                # 종료조건에 해당하기 전까지 진행 방향으로 계속 이동
                # while문이 종료되고 새로운 next_x, next_y가 실행된다는 건 방향을 틀었다는 것임
                next_x += dx[d]
                next_y += dy[d]
    
    return mirror[end_x][end_y]

if __name__ == "__main__":
    c, r = map(int, input().split())
    graph = [list(input().strip()) for _ in range(r)]
    
    # 레이저(lazer) 좌표 저장
    lazer = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "C":
                lazer.append((i, j))
    # 시작지점과 도착지점으로 구분
    start_x, start_y = lazer[0]
    end_x, end_y = lazer[1]
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    ans = BFS(start_x, start_y)
    print(ans)