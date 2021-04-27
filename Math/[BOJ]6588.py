# 골드바흐의 추측
# import sys # 입력 데이터 갯수가 많으면 sys사용
# input = sys.stdin.readline

# 데이터 갯수가 백만개
n = 1000000
primeNumber = [True] * (n+1)
# 소수란 1보다 큰 자연수 중에서 1과 자기 자신만을 약수로 갖는 수로
# 곱셈이기 때문에 제곱근까지만 알아보면 된다
for i in range(2, int(n**0.5)+1):
    if primeNumber[i]:
        for j in range(i+i, n+1, i):
            primeNumber[j] = False

# n이하의 소수 리스트 생성
primeList = [i for i in range(2, n+1) if primeNumber[i]]


while True:
    n = int(input())
    flag = False

    if n == 0:
        break
    # 소수 리스트에서 숫자 하나씩 꺼내어 합이 n이 되는 숫자가 소수인지 확인한다
    for i in primeList:
        if primeNumber[n-i]:
            print("%d = %d + %d" % (n, i, n-i))
            flag = True
            break

    if not flag:
        print("Goldbach's conjecture is wrong.")
