# 테트로미노
# dfs 자료구조, ㅗ 모형은 예외처리

def mfinger(x, y):
    global result
    # ㅗ 모형 4가지 경우의 수 모두 실행
    for middlefinger in middlefingers:
        # ㅗ 모양 합
        middleSum = 0
        for mx, my in middlefinger:
            nx = x + mx
            ny = y + my
            # 하나라도 조건에 만족하지 않으면 두번째 for문 종료
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            middleSum += board[nx][ny]
        result = max(result, middleSum)
    return


def dfs(x, y, cnt, num):
    global result
    # 종료조건(4칸이 되었을 때)
    if cnt == 4:
        result = max(result, num)
        return
    else:
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 범위를 넘어갔거나, 방문했거나
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                continue
            else:
                visited[nx][ny] = True
                dfs(nx, ny, cnt+1, num+board[nx][ny])
                visited[nx][ny] = False


n, m = map(int, input().split())

board = []
# 방문처리
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    board.append(list(map(int, input().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# ㅗ 모형 처리
middlefingers = [
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)]
]

result = 0
# 모든 칸에 대해서 실행
# 최대 실행 횟수 500 * 500 * 4**4 = 4백만이므로 가능
for i in range(n):
    for j in range(m):
        # 방문처리
        visited[i][j] = True
        # x좌표, y좌표, 횟수, 칸의 수
        dfs(i, j, 1, board[i][j])
        # 방문처리 제거
        visited[i][j] = False
        # ㅗ 모양 처리
        mfinger(i, j)

print(result)
