# 이전 수열

n = int(input())
data = list(map(int, input().split()))

length = len(data)
k = -1
for i in range(length-1):
    # data[i] > data[i+1]을 만족하는 수 중 가장 큰 인덱스
    if data[i] > data[i+1]:
        k = i
    
if k == -1:
    print(-1)
else:
    for j in range(k+1, length):
        # data[k] > data[j]를 만족하는 가장 큰 인덱스 
        if data[k] > data[j]:
            m = j

    data[k], data[m] = data[m], data[k]

    temp = data[k+1:]
    # 역순으로 정렬하기
    temp.sort(reverse=True)
    answer = data[:k+1] + temp

    for i in answer:
        print(i, end = ' ')