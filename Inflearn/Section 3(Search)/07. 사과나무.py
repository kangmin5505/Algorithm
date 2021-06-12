import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
start = n//2
end = n//2
for i in range(n):
    for j in range(start, end+1):
        ans += board[i][j]    
    if i < n//2:
            start -=1
            end += 1
    else:
            start += 1
            end -= 1

print(ans)