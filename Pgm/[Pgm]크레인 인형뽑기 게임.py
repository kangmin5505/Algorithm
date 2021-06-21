def solution(board, moves):
    answer = 0
    # 열 기준으로 하나씩 내려가면서 확인
    basket = [0]
    for move in moves:
        # 인덱스 맞춰주기
        move = move - 1
        for col in range(len(board)):
            if board[col][move] != 0:
                basket.append(board[col][move])
                board[col][move] = 0
                
                # 인형이 2개 이상 들어갔을 때 확인
                if len(basket) >= 3:
                    print(basket)
                    if basket[-1] == basket[-2]:
                        # 인형 터트리기
                        basket.pop()
                        basket.pop()
                        answer += 2
                break
                            
    return answer