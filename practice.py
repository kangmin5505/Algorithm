# 테트로미노
# dfs문제 (ㅗ 모양은 예외처리)

def mfinger(x, y):
    global result
    for middlefinger in middlefingers:
        mfingerSum = 0
        for mx, my in middlefinger:
            nx = x + mx
            ny = y + my
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            mfingerSum += board[nx][ny]
        result = max(result, mfingerSum)
    return


def dfs(x, y, cnt, num):
    global result

    if cnt == 4:
        result = max(result, num)
        return
    else:
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue
            else:
                visited[nx][ny] = True
                dfs(nx, ny, cnt+1, num+board[nx][ny])
                visited[nx][ny] = False


n, m = map(int, input().split())

visited = [[False] * m for _ in range(n)]
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

middlefingers = [
    [(0, 0), (0, 1), (0, 2), (-1, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, -1)]
]

result = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        mfinger(i, j)

print(result)
