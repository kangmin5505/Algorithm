# 소수찾기

def cnt_primeNumber():
    cnt = 0

    for num in data:
        flag = True

        if num <= 1:
            continue

        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                flag = False
                break

        if flag:
            cnt += 1

    return cnt


n = int(input())
data = list(map(int, input().split()))

print(cnt_primeNumber())
