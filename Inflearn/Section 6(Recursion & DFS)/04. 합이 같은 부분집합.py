# 각각의 숫자를 포함할지 안 할지(합으로 결정) 하는 DFS 생성
# DFS의 깊이가 n이 되면 합이 같은 부분집합인지 확인

import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 6(Recursion&DFS)\input.txt", "rt")


def DFS(L, sub_total):
    # Cut Edge
    if sub_total > total//2:
        return
    if L == n:
        # main함수에서 total이 홀수인데 처리 안 할 경우
        # sub_total == total//2은 True 지만
        # sub_total == total-sub_total은 False임
        if sub_total == total-sub_total:
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sub_total+data[L])
        DFS(L+1, sub_total)


if __name__ == "__main__":
    n = int(input())
    data = [int(x) for x in input().split()]
    total = sum(data)

    # 합이 짝수가 아니면 합이 같은 부분집합이 나올 수가 없음
    if total % 2 == 0:
        DFS(0, 0)
    else:
        print("NO")
