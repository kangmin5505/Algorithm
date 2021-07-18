def solution(s):
    cnt = 0
    rotate = 0
    while len(s) > 1:
        rotate += 1
        cnt += s.count("0")
        s = bin(len(s.replace("0","")))[2:]
        
    answer = [rotate, cnt]  
    return answer