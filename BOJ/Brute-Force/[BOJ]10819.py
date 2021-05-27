# 차이를 최대로

from itertools import permutations

n = int(input())
data = list(map(int, input().split()))

permuList = list(permutations(data, n))

result = 0
for permu in permuList:
    permuSum = 0
    for i in range(n-1):
        permuSum += abs(permu[i] - permu[i-1])
    result = max(result, permuSum)

print(result)

# permuList 함수 생성해보기

# import copy
# # copy.deepcopy를 해줘야 data 객체를 참조 안 해서 데이터가 변하는 일이 없음

# def next_permutation(permu):
#     length = len(permu)

#     k = -1
#     for i in range(length-1):
#         if permu[i] < permu[i+1]:
#             k = i

#     if k == -1:
#         return []

#     for j in range(k+1, length):
#         if permu[k] < permu[j]:
#             m = j

#     permu[k], permu[m] = permu[m], permu[k]

#     temp = permu[k+1:]
#     temp.sort()
#     permu = permu[:k+1] + temp

#     return permu


# data = [1, 2, 3]
# data.sort()
# permuList = []

# while True:
#     permuList.append(data)
#     data = next_permutation(copy.deepcopy(data))
#     if not data:
#         break
