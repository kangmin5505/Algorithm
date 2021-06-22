def solution(citations):
    answer = 0
    
    citations.sort()
    length = len(citations)
    
    for idx in range(length):
        # 오름차순으로 정렬되어 있으므로 처음 조건을 성립하는 값이 최댓값이다.
        # 그 이후는 조건 h번 이상 인용된 논문이 h개가 나올 수가 없음
        if citations[idx] >= length - idx:
            answer = length - idx
            break
        
    return answer