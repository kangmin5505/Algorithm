import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')

board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for j in range(3):
        for k in range(2):
            if board[i][j+k] != board[i][j+4-k]:
                break
        else:
            cnt += 1
        for k in range(2):
            if board[j+k][i] != board[j+4-k][i]:
                break
        else:
            cnt += 1

print(cnt)
        
