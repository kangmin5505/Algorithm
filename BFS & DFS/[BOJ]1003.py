# 피보나치 함수

fibo_0 = [1, 0]
fibo_1 = [0, 1]

for i in range(2, 41):
    fibo_0.append(fibo_0[i-1] + fibo_0[i-2])
    fibo_1.append(fibo_1[i-1] + fibo_1[i-2])

for tc in range(int(input())):
    n = int(input())
    print(fibo_0[n], fibo_1[n])
