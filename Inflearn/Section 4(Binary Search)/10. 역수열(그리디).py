import sys

sys.stdin = open(
    "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")

"""
1. ans 배열 0으로 채워서 생성
2. 차례대로 배열을 확인하며 0을 발견할 경우 cnt+=1 하면서 진행
3. 배열에는 자기 자신을 저장
"""

n = int(input())
data = list(map(int, input().split()))
ans = [0] * n

for i in range(n):
    for j in range(n):
        if data[i] == 0 and ans[j] == 0:
            ans[j] = i+1
            break
        elif ans[j] == 0:
            data[i] -= 1

print(ans)
        