# import sys

# sys.stdin = open(
#     "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")


"""
1. 좌, 우 인덱스를 설정
2. 좌가 작으면 +1 우가 작으면 -1
3. 가져온 값을 비교 값으로 저장
"""

n = int(input())
nums = list(map(int, input().split()))

lt = 0
rt = n-1
ans = ""
temp = []
last = 0
while lt <= rt:
    if nums[lt] > last:
        temp.append((nums[lt], 'L'))
    if nums[rt] > last:
        temp.append((nums[rt], 'R'))
    temp.sort()
    if len(temp) == 0:
        break
    else:
        ans += temp[0][1]
        last = temp[0][0]
        if temp[0][1] == "L":
            lt += 1
        else:
            rt -= 1
    temp.clear()
print(len(ans))
print(ans)