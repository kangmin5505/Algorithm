# 조합사용
# L == k 일 때 m의 배수인지 확인
# cnt
import sys
import time

sys.stdin = open(
    "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 6(Recursion&DFS)\input.txt", "rt")


def DFS(L, start, total):
    global result
    if L == k:
        if total % m == 0:
            result += 1
    else:
        for i in range(start, n):
            DFS(L+1, i+1, total+nums[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = [int(x) for x in input().split()]
    m = int(input())
    result = 0
    # start_time = time.time()
    DFS(0, 0, 0)
    # end_time = time.time() - start_time
    # print('time : ', end_time)
    print(result)
