# 감시 피하기
# combinations 함수를 사용하여 빈칸의 경우를 만들고
# 선생님이 상하좌우 확인할 수 있도록 방향에 따라 다르게 처리해준다
from itertools import combinations


def watch(x, y, direction):
    # 북쪽으로 가는 경우
    if direction == 0:
        # 범위 내에서
        while x >= 0:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            x -= 1
    # 동쪽으로 가는 경우
    if direction == 1:
        # 범위 내에서
        while y < n:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            y += 1
    # 남쪽으로 가는 경우
    if direction == 2:
        # 범위 내에서
        while x < n:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            x += 1
     # 서쪽으로 가는 경우
    if direction == 3:
        # 범위 내에서
        while y >= 0:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            y -= 1
    return False


def process():
    for x, y in teachers:
        for direction in range(4):
            if watch(x, y, direction):
                return True
    return False


n = int(input())
board = []
# 선생님과 빈칸의 위치를 저장해둔다
# why? 선생님의 경우 매번 선생님의 좌표를 찾지 않아도 되고,
# 빈칸의 경우 combinations를 사용해 3개의 장애물을 설치할 경우의 수를 만들수 있기 때문이다
teachers = []
blanks = []
for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'X':
            blanks.append((i, j))

# combinations을 사용하여 3개의 장애물을 설치할 경우를 리스트로 반환
blankList = list(combinations(blanks, 3))
# 찾을 수 있는 경우 True, 아니면 False
find = False

for obstacle in blankList:
    # 장애물 설치
    for i, j in obstacle:
        board[i][j] = 'O'

    # 선생님들이 학생들을 감시 못한다면
    if not process():
        # 답을 찾음
        find = True
        break

    # 장애물 제거
    for i, j in obstacle:
        board[i][j] = 'X'


if find:
    print("YES")
else:
    print("NO")
