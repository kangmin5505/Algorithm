#나의 풀이

def decoder(row):
    temp = ""
    for s in row:
        temp += s
    return temp
    
    
def convert(arr, board):
    for i in range(len(arr)):
        temp = arr[i]
        for j in range(len(arr)-1, -1, -1):
            if temp%2 == 1:
                board[i][j] = '#'
            else:
                if board[i][j] != '#':
                    board[i][j] = ' '
            temp = temp//2
    return board


def solution(n, arr1, arr2):
    # 0. 지도를 모두 0으로 선언
    # 1. 숫자 한 개가 주어지면 2진수로 변환시킨다.
        # 2진수 변환하는 방법 -> 2로 나누기
    # 2. 2진수 변환한 것을 1부분에는 #을 0부분에는 ' '를 대입한다
    # 3. 한 줄씩 answer에 추가한다.
    
    board = [[' ']*n for _ in range(n)]
    board = convert(arr1, board)
    board = convert(arr2, board)
    
    answer = []
    for i in range(n):
        answer.append(decoder(board[i]))

    return answer


# # 다른 사람 풀이
# def solution(n, arr1, arr2):
#     answer = []
#     for i, j in zip(arr1, arr2):
#         arr12 = str(bin(i|j)[2:])
#         arr12 = arr12.rjust(n, '0')
#         arr12 = arr12.replace('1', '#')
#         arr12 = arr12.replace('0', ' ')
#         answer.append(arr12)
#     return answer

# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]

# res = solution(n, arr1, arr2)
# print(res)

