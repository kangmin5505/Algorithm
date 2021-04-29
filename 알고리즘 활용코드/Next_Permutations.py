# Next_Permutations 알고리즘
# 1. a[k] < a[k+1]가 성립하는 k의 최댓값을 찾는다.
#   - ( 만약 여기서 k값이 존재하지 않는다면 이미 내림차순으로 정렬되어 있는 것이다.)
# 2. 인덱스 k 이후의 값들 중 a[k] < a[m]이 성립하는 m의 최댓값을 찾는다.
# 3. k와 m 자리의 값을 서로 바꾸어 준다.
# 4. 인덱스 k 이후의 값들을 오름차순으로 정렬해준다.

n = 5
data = [1, 2, 3, 4]
length = len(data)

k = -1
# 1. k의 최댓값 구하기
for i in range(length-1):
    if data[i] < data[i+1]:
        k = i

# 내림차순으로 정렬되어 있는 경우
if k == -1:
    print(-1)
else:
    # 2. m의 최댓값 구하기
    for j in range(k+1, length):
        if data[k] < data[j]:
            m = j

    # 3. k와 m의 값 바꿔치기
    data[k], data[m] = data[m], data[k]

    # 4. k 이후 정렬
    temp = data[k+1:]
    temp.sort()
    answer = data[:k+1] + temp

    for num in answer:
        print(num, end=' ')
