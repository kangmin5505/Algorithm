# 최소공배수

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


for tc in range(int(input())):
    a, b = map(int, input().split())

    if b > a:
        a, b = b, a

    lcm = a*b // gcd(a, b)
    print(lcm)
