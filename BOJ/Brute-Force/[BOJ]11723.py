# 집합
# set.discard(x) => 집합 안에 x가 없어도 keyerror 반환 x
# set.remove(x) => 집합 안에 x가 없으면 keyerror 반환
# 입력 갯수가 다른 경우 일괄처리하면 속도가 느려짐
# => 나누어서 처리
# 인덱스를 통해 값을 호출하면 속도가 느려짐
# => 각각 변수에 담아서 실행

import sys

sys.stdin = open('C:\github\Algorithm\Brute-Force\input.txt', 'rt')


n = int(input())
s = set()

for _ in range(n):
    operate_num = input().split()

    if len(operate_num) == 1:
        if operate_num[0] == 'all':
            s = {i for i in range(1, 21)}

        else:
            s = set()

        continue
    command, num = operate_num[0], int(operate_num[1])

    if command == 'add':
        s.add(num)

    elif command == 'remove':
        s.discard(num)

    elif command == 'check':
        if num in s:
            print(1)
        else:
            print(0)

    elif command == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)
