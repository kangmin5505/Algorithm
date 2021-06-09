# 0과 1
"""
BFS

풀이 방법
- n의 나머지는 0 ~ (n-1)까지다
- %(modular)의 법칙
    => (a + b) mod n = (a mod n + b mod n) mod n
    => ex) (r*10 + 0) mod n = (r*10 mod n + 0 mod n) mod n
"""
import sys
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    
    for _ in range(tc):
        n = int(input())
        # 나머지 체크 배열(0 ~ n-1까지)
        check = [False]*n
        q = deque()
        # 1부터 시작
        q.append(1)
        # 1체크
        check[1%n] = True
        # n이 1이면 바로 탈출하도록 while문을 설정
        ans = 0
        
        while q:
            x = q.popleft()
            # 종료 구문
            if x%n == 0:
                ans = x
                break
            else:
                for i in [0, 1]:
                    next_x = x*10 + i
                    if not check[next_x%n]:
                        check[next_x%n] = True
                        q.append(next_x)
        # ans가 0이면 0번 인덱스인 'BRAK'을 출력
        # ans가 0이 아니면 1번 인덱스인 ans를 출력
        print(['BRAK', ans][ans!=0])


