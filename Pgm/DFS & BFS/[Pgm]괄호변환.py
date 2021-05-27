# 괄호 변환
def check(u):
    # count가 -1이 되면 올바른 괄호 문자열이 될 수 없음
    count = 0
    for i in range(len(u)):
        if u[i] == '(':
            count += 1
        else:
            # count가 0이면 그 전에 '(' 가 없어서 올바른 괄호 문자열이 아님
            if count == 0:
                return False
            count -= 1
    return True


def blancedIndex(p):
    # count가 0이 될 때 균형잡힌 괄호 문자열이 됨
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        # 균형잡힌 괄호 문자열 인덱스
        if count == 0:
            return i


def solution(p):
    answer = ""

    if p == "":
        return answer

    index = blancedIndex(p)
    u = p[:index+1]
    v = p[index+1:]

    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        # 리스트를 활용하여 문자열의 괄호 방향 뒤집기
        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)

    return answer
