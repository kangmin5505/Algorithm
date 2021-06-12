import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')

n = int(input())
board = [[0] * (n+2)]
for _ in range(n):
    board.append([0] + list(map(int, input().split())) + [0])
board.append([0] * (n+2))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(board[i][j] > board[i+dx[d]][j+dy[d]] for d in range(4)):
            ans += 1
print(ans)