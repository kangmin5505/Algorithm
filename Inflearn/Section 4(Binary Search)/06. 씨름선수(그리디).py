# import sys

# sys.stdin = open(
#     "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")

"""
1. 키를 기준으로 내림차순으로 정렬
2. 몸무게를 순서대로 비교하며 큰 값이 나올 경우 cnt+=1 
3. 기준 몸무게를 교체

- 위에 있는 사람들 보다 몸무게가 크다면 키는 작지만 몸무게가 크고,
  아랫사람 보다는 키가 크기 때문에 조건에 성립
"""



n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
info.sort(reverse=True)

w = 0
cnt = 0
for height, weight in info:
    if weight > w:
        cnt += 1
        w = weight
    
print(cnt)