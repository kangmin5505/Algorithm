def solution(cacheSize, cities):
    answer = 0
    n = cacheSize
    q = deque()
    
    for city in cities:
        # city가 캐시에 있을 때
        if city in q:
            answer += 1
            # 캐시 공간 있을 때
            
                
            # 캐시 공간 없을 때
        # city가 캐시에 없을 때
        else:
            pass
    
    return answer

