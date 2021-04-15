# dfs 사용
def dfs(i, j):
    if i <= -1 or i >= n or j <= -1 or j >= m:
        return False
    if board[i][j] == 0:
        board[i][j] = 1
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        return True


n, m = map(int, input().split())

board = []
# 입력이 많을 경우 파일 읽기(with문 사용시 자동으로 f.close() 됨)
# with open("C:/github/Algorithm/BFS & DFS/text.txt", "r") as f:
#     for _ in range(n):
#         line = f.readline().rstrip()
#         board.append(list(map(int, line)))

# 사용자에게 입력받는 구문
for _ in range(n):
    board.append(list(map(int, input())))


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)
