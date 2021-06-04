# Cut Edge -> result보다 작으면 cutting
# 동전 단위 내림차순 정렬 -> 효율성
import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 6(Recursion&DFS)\input.txt", "rt")


def DFS(L, total):
    global result
    if L >= result:
        return
    if total > target:
        return

    if total == target:
        # if L < result:
        result = L
    else:
        for i in range(n):
            DFS(L+1, total+coins[i])


if __name__ == "__main__":
    n = int(input())
    coins = [int(x) for x in input().split()]
    target = int(input())

    coins.sort(reverse=True)

    result = 501
    DFS(0, 0)
    print(result)
