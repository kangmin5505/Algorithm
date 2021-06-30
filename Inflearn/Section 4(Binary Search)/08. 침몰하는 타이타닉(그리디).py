# import sys

# sys.stdin = open(
#     "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")

"""
1. 오름차순 정렬
2. 맨 앞과 뒤의 합과 m비교
3. m보다 크면 맨 뒤 pop 같거나 작으면 앞, 뒤 pop
"""

n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()

cnt = 0
while True:
    if len(weights) == 1:
        weights.pop()
        cnt +=1 
        break
    elif len(weights) == 0:
        break
        
    if weights[0] + weights[-1] > m:
        weights.pop()
        cnt += 1
    else:
        weights.pop(0)
        weights.pop()
        cnt += 1
        
print(cnt)