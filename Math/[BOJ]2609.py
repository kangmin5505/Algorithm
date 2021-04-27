# 최대공약수와 최소공배수
# 유클리드 호제법(gcd 구하는 법)
# a 를 b로 나누어서 b를 a에 나눈 나머지를 b 에 대입시켜서 b 가 0이 될때 까지 반복을 하면, 남는 a 값이 바로 최대 공약수 이다.
# 최소공배수 : a와 b를 곱한 뒤 최대공약수로 나눠주면 된다

a, b = map(int, input().split())

if b > a:
    a, b = b, a


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a*b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))
