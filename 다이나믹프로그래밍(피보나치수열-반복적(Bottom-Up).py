# Memoization 기법: 다이나믹 프로그래밍을 구현하는 방법 중 한 종류
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])