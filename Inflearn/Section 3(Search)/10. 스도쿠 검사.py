import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')

def check(board):
    # 행과 열
    for i in range(n):
        check1 = [0] * (n+1)
        check2 = [0] * (n+1)
        for j in range(n):
            check1[board[i][j]] = 1
            check2[board[j][i]] = 1
        if sum(check1) != 9 or sum(check2) != 9:
            return False

    # 3*3 칸
    for i in range(3):
        for j in range(3):
            check1 = [0] * (n+1)
            for a in range(3):
                for b in range(3):
                    check1[board[i*3+a][j*3+b]] = 1
            if sum(check1) != 9:
                return False
    return True
                

if __name__ == "__main__":
    n = 9
    board = [list(map(int, input().split())) for _ in range(n)]
    if check(board):
        print("YES")
    else:
        print("NO")