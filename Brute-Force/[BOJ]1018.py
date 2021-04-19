# 체스판 다시 칠하기
n, m = map(int, input().split())

board = list()
with open('C:\github\Algorithm\Brute-Force\input.txt', 'r') as f:

    for _ in range(n):
        line = f.readline().rstrip()
        board.append(list(line))
# board = list()
# for i in range(n):
#     board.append(input())

repair = list()
# 모든 경우의 수를 확인
# n-7, m-7의 의미는 8*8 matrix가 움직일 수 있는 횟수
for i in range(n-7):
    for j in range(m-7):
        # 처음이 W인 경우와 B인 경우를 나누어서 계산
        first_W = 0
        first_B = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 짝수 칸은 시작점과 같은 문자
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W += 1
                    elif board[k][l] != 'B':
                        first_B += 1
                # 홀수 칸은 시작점과 다른 문자
                elif (k + l) % 2 != 0:
                    if board[k][l] != 'W':
                        first_B += 1
                    elif board[k][l] != 'B':
                        first_W += 1
        repair.append(first_B)
        repair.append(first_W)

print(min(repair))
