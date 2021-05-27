# 암호 만들기

# 입력 받은 문자들을 오름차순 정렬 시킨다
# 문자들 중 L개를 뽑는 조합 리스트를 선언한다
# 최소 한 개의 모음과 최소 두 개의 자음으로 구성 되었는지 확인한다
# 순서대로 출력한다

from itertools import combinations

l, c = map(int, input().split())
data = list(input().split())

data.sort()
data_sets = list(combinations(data, l))

vowels = ('a', 'e', 'i', 'o', 'u')

for data_set in data_sets:
    cnt_vowels = 0
    for i in data_set:
        if i in vowels:
            cnt_vowels += 1
    if cnt_vowels >= 1 and len(data_set) - cnt_vowels >= 2:
        print(''.join(data_set))
