import sys
# import time

sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
# start = time.time()
for i in range(n):
    row = 0
    col = 0
    for j in range(n): 
        row += board[i][j]
        col += board[j][i]
    # ans = max(ans, row, col)

temp1 = 0
temp2 = 0
for i in range(n):
    temp1 += board[i][i]
    temp2 += board[i][n-1-i]

ans = max(ans, temp1, temp2)
print(ans)
# print(time.time()-start)