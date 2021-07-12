 def solution(s):
    answer = True
    cnt = 0 
    for x in s:
        if cnt < 0:
            answer = False
            break
        else:
            if x == "(":
                cnt += 1
            else:
                cnt -= 1
    if cnt != 0:
        answer = False
    return answer