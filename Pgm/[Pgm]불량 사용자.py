from itertools import permutations

def is_match(permu_val, banned_id):
    # permu_val의 값들을 하나씩 꺼내서 비교
    for i in range(len(permu_val)):
        if len(permu_val[i]) != len(banned_id[i]):
            return False
        # permu_val에서 꺼낸 값을 banned_id와 하나씩 비교
        for j in range(len(permu_val[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != permu_val[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = []
    # 불량 사용자 아이디는 응모자 아이디 중 하나
    for permu_val in permutations(user_id, len(banned_id)): 
        if is_match(permu_val, banned_id):
            # permutations는 tuple로 반환
            # 중복을 제거해주기 위해 set로 변환
            permu_set = set(permu_val)
            # set 자료형은 순서가 없기 때문에 안에 담긴 내용이 순서에 상관없이 같다면 같은 값으로 인식
            if permu_set not in answer:
                answer.append(permu_set)
    return len(answer)