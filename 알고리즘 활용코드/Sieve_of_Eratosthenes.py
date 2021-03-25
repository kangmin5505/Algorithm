# 여러 개의 수가 소수인지 아닌지를 판별할 때 사용하는 알고리즘
# Sieve of Eratosthenes
import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n+1)] # 처음엔 모든 수가 소수인 것으로 초기화(0과 1은 제외)

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
