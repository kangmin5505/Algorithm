# 문자열 숫자 대소비교
# 맨 앞 숫자부터 비교
# 길이가 긴 것이 더 큰 숫자

# 이 문제의 경우 3과 30 중 3이 앞에 오는 것이 더 큰 숫자임으로 x*3을 해주어 333과 303030을 비교해서 3이 앞에 오도록 하면 된다.


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
