# 일곱 난쟁이
# combinations를 사용하여 아홉 난쟁이 중 일곱 난쟁이를 뽑는 모든 경우의 수를 생성
from itertools import combinations

n = 9
dwarves = [int(input()) for _ in range(n)]


# 아홉 난쟁이 중 일곱 난쟁이를 뽑는 모든 경우의 수 리스트
dwarvesList = list(combinations(dwarves, 7))

for data in dwarvesList:
    # combinations의 반환 형태는 튜플이기 때문에 리스트로 변환
    # why? sum함수를 사용하기 위해
    data = list(data)
    if sum(data) == 100:
        answer = data
        break

answer.sort()
for i in answer:
    print(i)
