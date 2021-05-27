# 연산자 끼워넣기
# 재귀구조 사용


n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

# dfs 메서드


def cal(i, now):
    # 전역변수 설정(재귀함수 호출시 변수들을 사용할 수 있게하기위해 )
    global add, sub, mul, div, min_value, max_value

    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)

    if add > 0:
        add -= 1
        cal(i+1, now + numbers[i])
        add += 1
    if sub > 0:
        sub -= 1
        cal(i+1, now - numbers[i])
        sub += 1
    if mul > 0:
        mul -= 1
        cal(i+1, now * numbers[i])
        mul += 1
    if div > 0:
        div -= 1
        # /와 // 차이 알기
        cal(i+1, int(now / numbers[i]))
        div += 1


cal(1, numbers[0])

print(max_value)
print(min_value)
