# 기타리스트
"""
dynamic programming
- 2차원 dp테이블을 0으로 초기화 후 dp[0][시작점] = 1을 해준다
- 시작점부터 시작하여 범위 내에서 +, -를 모두 실시한다
- 마지막 행을 뒤에서부터 확인하여 1이 있으면 그 인덱스 값을, 1이 없으면 -1을 반환한다.
"""
import sys

input = sys.stdin.readline


def volume():
    for i in range(1, n + 1):
        for j in range(m + 1):
            # i - 1 번째 열에 해당하는 볼륨이 존재하지 않는다면
            if dp[i - 1][j] == 0:
                continue

            # j번째 행에서 i번째 볼륨을 더한 것이 m보다 작거나 같다면
            if j + volumes[i] <= m:
                dp[i][j + volumes[i]] = 1

            # j번째 행에서 i번째 볼륨을 뺀 것이 0보다 크거나 같다면
            if j - volumes[i] >= 0:
                dp[i][j - volumes[i]] = 1


def search():
    for i in range(m, -1, -1):
        if dp[-1][i] == 1:
            return i
    return -1


input = sys.stdin.readline

n, s, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

volumes = [0] + [int(x) for x in input().split()]

volume()

answer = search()

print(answer)
