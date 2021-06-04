# 오늘 상담을 할 경우와 안 할 경우로 구분
# 날짜가 n+1이 되면 return
import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def DFS(L, total_profit):
    global max_profit
    # 종료 조건
    if L == n+1:
        if max_profit < total_profit:
            max_profit = total_profit
    else:
        # 휴가 가는 날(n+1) 전에 있는 것만 처리 가능
        if L + time[L] <= n+1:
            DFS(L+time[L], total_profit + price[L])
        DFS(L+1, total_profit)


if __name__ == "__main__":
    n = int(input())
    time = [0]
    price = [0]

    for _ in range(n):
        t, p = map(int, input().split())
        time.append(t)
        price.append(p)

    max_profit = 0
    DFS(1, 0)
    print(max_profit)
