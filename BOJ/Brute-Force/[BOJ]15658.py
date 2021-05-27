# 연산자 끼워넣기 2

# cnt : 숫자갯수 total : 결과값
def dfs(cnt, total):
    global add, sub, mul, div, max_value, min_value

    if cnt == n:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return

    if add > 0:
        add -= 1
        dfs(cnt+1, total + nums[cnt])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(cnt+1, total - nums[cnt])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(cnt+1, total * nums[cnt])
        mul += 1
    if div > 0:
        div -= 1
        dfs(cnt+1, int(total / nums[cnt]))
        div += 1


n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

# 숫자 갯수, 결과값
dfs(1, nums[0])

print(max_value)
print(min_value)
