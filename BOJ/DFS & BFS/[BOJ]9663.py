# N-Queen
# dfs방식에서 가로, 세로, 대각선을 가지치기 해서 해결 => BackTracking

n = int(input())
# 각 row에 1개의 퀸이 들어가야하기 때문에 board[x]가 의미하는 것은
# 퀸이 x번째 row, board[x]번째 column에 위치한다는 것이다
board = [0] * n
answer = 0


def check(x):
    # x번째 이전의 row들과 비교하는 반복문
    for i in range(x):
        # board[x] == board[i] : x번째 row가 i번째 row와 같은 column에 있다
        # abs(board[x] - board[i] == x - i) : x번째와 i번째 column의 차이가 x번째와 i번째 row의 차이와 같다면 대각선에 위치한다
        if board[x] == board[i] or abs(board[x] - board[i]) == x - i:
            return False
    return True


def recursive(x):
    global answer
    # 'x == n' 의 의미는 x개의 퀸을 board 위에 놓았다는 의미로 n개의 퀸들이 서로 공격하지 못하는 경우가 발생했다는 것이다
    if x == n:
        # 한 가지 경우를 세주고 함수를 return 시켜 종료한다
        answer += 1
        return
    # x번째 row의 모든 column을 확인
    for i in range(n):
        # x번째 row에 i번째 column에 넣는 식
        board[x] = i
        # x번째 이전의 row들과 확인해서 조건을 만족한다면 x+1번째 row를 확인
        if check(x):
            recursive(x+1)


# 0번째 column부터 시작
recursive(0)
print(answer)
