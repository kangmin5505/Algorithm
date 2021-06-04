# itertools 사용
import time
from itertools import combinations
import sys

sys.stdin = open(
    "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 6(Recursion&DFS)\input.txt", "rt")


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = [int(x) for x in input().split()]
    m = int(input())
    cnt = 0

    # start_time = time.time()
    for num in combinations(nums, k):
        if sum(num) % m == 0:
            cnt += 1
    # end_time = time.time() - start_time
    # print('time : ', end_time)
    print(cnt)
