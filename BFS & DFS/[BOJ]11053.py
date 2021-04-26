# 가장 긴 증가하는 부분 수열
# bisect_left 사용

from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))

sqeuence = [data[0]]

for num in data:
    if sqeuence[-1] < num:
        sqeuence.append(num)
    else:
        index = bisect_left(sqeuence, num)
        sqeuence[index] = num

print(len(sqeuence))
