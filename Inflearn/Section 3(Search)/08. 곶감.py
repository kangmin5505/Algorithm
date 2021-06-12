import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    r, d, c = map(int, input().split())
    if d == 0:
        for _ in range(c):
            board[r-1].append(board[r-1].pop(0))
    else:
        for _ in range(c):
            board[r-1].insert(0, board[r-1].pop())

start = 0
end = n-1
ans = 0
for i in range(n):
    for j in range(start, end+1):
        ans += board[i][j]
    if i < n//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(ans)