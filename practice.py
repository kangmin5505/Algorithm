# import sys
import math
# input = sys.stdin.readline

n = 1000000
primeNumber = [True] * (n+1)
for i in range(2, int(math.sqrt(n))+1):
    if primeNumber[i]:
        for j in range(i+i, n, i):
            primeNumber[j] = False

primeList = [i for i in range(2, n+1) if primeNumber[i]]

while True:
    a = int(input())
    flag = False

    if a == 0:
        break

    for i in primeList:
        if primeNumber[n-i]:
            print("%d = %d + %d" % (n, i, n-i))
            flag = True
            break

    if not flag:
        print("Goldbach's conjecture is wrong.")
