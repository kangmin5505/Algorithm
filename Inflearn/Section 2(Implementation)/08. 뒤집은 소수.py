import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 2(Implementation)\input.txt", "rt")

def reverse(num):
    res = 0
    while num > 0:
        res = res*10 + num%10
        num = num//10
    return res

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    else:
        return True

n = int(input())
data = list(map(int, input().split()))

for x in data:
    temp = reverse(x)
    if isPrime(temp):
        print(temp, end = ' ')