# GCD합

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


for tc in range(int(input())):
    n, *data = map(int, input().split())
    data.sort(reverse=True)

    sum_gcd = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum_gcd += gcd(data[i], data[j])

    print(sum_gcd)
