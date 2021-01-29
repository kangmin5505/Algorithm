def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

# Memoization 기법: 다이나믹 프로그래밍을 구현하는 방법 중 한 종류
d = [0] * 100
print(fibo(99))