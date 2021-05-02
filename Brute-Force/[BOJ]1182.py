# 부분수열의 합
# combinations 사용

# 조합으로 리스트를 선언한다
# 각 경우의 수마다 합이 target이 되는 지 확인해서 카운트 해준다

from itertools import combinations

n, target = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

answer = 0
for i in range(1, n+1):
    data_sets = list(combinations(data, i))
    for data_set in data_sets:
        if sum(data_set) == target:
            answer += 1


print(answer)
