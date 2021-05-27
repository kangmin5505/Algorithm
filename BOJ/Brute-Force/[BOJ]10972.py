# 다음 순열
# 순열의 순서는 오름차순에서 내림차순 순서로 간다

n = int(input())
data = list(map(int, input().split(' ')))

length = len(data)
k = -1
# 1. data[i] < data[i+1]을 만족하는 i의 최댓값을 구한다.
for i in range(length-1):
    if data[i] < data[i+1]:
        k = i

# k = -1 이면 이미 내림차순으로 정렬되어 있는 것이다.
if k == -1:
    print(-1)
else:
    # 2. 인덱스 k 이후의 숫자 중 data[k] < data[m]을 만족하는 m의 최댓값을 찾는다.
    for j in range(k+1, length):
        if data[k] < data[j]:
            m = j

    # 3. k와 m의 자릿값을 바꿔준다
    data[k], data[m] = data[m], data[k]

    # 4. k이후의 값들을 오름차순 정렬해준다.
    temp = data[k+1:]
    temp.sort()
    answer = data[:k+1] + temp

    for i in answer:
        print(i, end=' ')
