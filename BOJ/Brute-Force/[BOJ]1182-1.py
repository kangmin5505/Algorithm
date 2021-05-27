# 부분 수열의 합
# 재귀구조 사용

# 각 숫자마다 합 or 무시의 경우로 나눈다
def dfs(idx, data_sum):
    global cnt

    # idx가 주어진 갯수를 넘어갔을 때는 함수 종료
    if idx >= n:
        return

    data_sum += data_set[idx]

    if data_sum == target:
        cnt += 1
    # 합을 더한 경우와 안 더한 경우로 나누어서 재귀함수를 실시한다
    dfs(idx + 1, data_sum)
    dfs(idx + 1, data_sum - data_set[idx])


n, target = map(int, input().split())
data_set = list(map(int, input().split()))

cnt = 0
dfs(0, 0)

print(cnt)
