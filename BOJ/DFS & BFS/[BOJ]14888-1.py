# 연산자 끼워넣기
# permutations 사용
from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# add = 1, sub = 2, mul = 3, div = 4
operation_list = []
operation_list += [1] * add
operation_list += [2] * sub
operation_list += [3] * mul
operation_list += [4] * div

operation_list = list(permutations(operation_list, n-1))
# set은 리스트 슬라이싱이 안 됨
operation_set = list(set(operation_list))

max_value = -1e9
min_value = 1e9

for case in operation_set:
    answer = numbers[0]

    for i in range(n-1):
        if case[i] == 1:
            answer += numbers[i+1]
        elif case[i] == 2:
            answer -= numbers[i+1]
        elif case[i] == 3:
            answer *= numbers[i+1]
        elif case[i] == 4:
            if answer < 0:
                answer = -(-answer//numbers[i+1])
            else:
                answer //= numbers[i+1]

    if max_value < answer:
        max_value = answer
    if min_value > answer:
        min_value = answer

print(max_value)
print(min_value)
