# 파일 합치기
"""
dynamic programming
"""
import math


def solve():
    n = int(input())
    data = [int(x) for x in input().split()]
    answer = [[0] * n for _ in range(n)]

    for j in range(1, n):
        for i in range(j-1, -1, -1):
            min_val = math.inf
            for k in range(j-i):
                min_val = min(min_val, answer[i][i+k] + answer[i+k+1][j])
            answer[i][j] = min_val + sum(answer[i:j+1])
    print(answer[0][n-1])


tc = int(input())

for _ in range(tc):
    solve()
