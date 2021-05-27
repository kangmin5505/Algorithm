# 스토쿠
# 빈칸의 좌표를 모아놓은 리스트와 가능성이 있는 수들을 만드는 함수를 정의
# => 시간단축을 위함
# 빈칸의 좌표 => zeros, 가능성이 있는 수들을 만드는 함수 => promising

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def promising(x, y):
    promised_num = [i for i in range(1, 10)]

    # 행렬 확인
    for k in range(9):
        if sudoku[x][k] in promised_num:
            promised_num.remove(sudoku[x][k])
        if sudoku[k][y] in promised_num:
            promised_num.remove(sudoku[k][y])

    # 3*3 행렬 확인
    x //= 3
    y //= 3

    for p in range(x*3, (x+1)*3):
        for q in range(y*3, (y+1)*3):
            if sudoku[p][q] in promised_num:
                promised_num.remove(sudoku[p][q])

    return promised_num


flag = False


def dfs(x):
    # flag 전역변수로 설정
    global flag

    # 종료조건 설정
    if flag == True:
        return

    # 모든 빈 칸을 채웠을 때
    if x == len(zeros):
        for row in sudoku:
            print(*row)

        flag = True
        return

    # 빈 칸의 좌표 받아오기
    (i, j) = zeros[x]
    promised_num = promising(i, j)

    for num in promised_num:
        sudoku[i][j] = num
        dfs(x+1)
        sudoku[i][j] = 0


dfs(0)
