"""
split(sep, maxsplit)
=> sep가 연속적으로 나올 경우 빈 문자열 반환
ex) example = " a  a ".split(" ") => ["", "a", "", "a", ""]
"""

def solution(s):
    answer = ''
    s = s.lower()
    words = s.split(" ")
    for word in words:
        word = word.capitalize()
        answer += word + ' '
    answer = answer[:-1]
    return answer