# 총액은 서로 달라야 함 -> set
import sys

sys.stdin = open(
    "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 7(DFS & BFS)\\test.txt", "rt")


def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            temp = set()
            for x in money:
                temp.add(x)
            if len(temp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += coins[L]
            DFS(L+1)
            money[i] -= coins[L]


if __name__ == "__main__":
    n = int(input())
    coins = []
    for _ in range(n):
        coin = int(input())
        coins.append(coin)

    money = [0] * 3
    res = int(1e9)
    DFS(0)
    print(res)
