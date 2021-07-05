"""
1. n보다 1큰 수부터 차례대로 확인하며 1의 갯수가 같은 값을 출력
"""
def solution(n):
    for i in range(n+1, 1000001):
        if bin(n).count('1') == bin(i).count('1'):
            return i