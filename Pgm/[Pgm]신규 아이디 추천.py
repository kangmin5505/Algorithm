"""
제한사항
1. 길이(3~15)
2. 가능한 문자(소문자, 숫자, '-', '_', '.')
3. '.' 은 처음과 끝 x, 연속 x
"""

def solution(new_id):
    answer = ''
    
    # 소문자로 변경
    new_id = new_id.lower()
   
    # 문자 제거
    for s in new_id:
        if s.isalnum() or s in "-_.":
            answer += s
    # 중복 마침표 제거
    while '..' in answer:
        answer = answer.replace("..", ".")
    
    # 처음, 끝 '.' 제거
    answer = answer.strip('.')
    
    # 빈 문자열 처리
    if answer == '':
        answer = 'a'
    
    # 16자 이상이면 15자만 입력
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer.rstrip('.')
    
    # 2자 이하일 경우 반복
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer



# # 정규표현식 사용
# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st  