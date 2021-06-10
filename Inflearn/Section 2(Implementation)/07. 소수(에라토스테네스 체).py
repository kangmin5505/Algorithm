# Eratosthenes

def eratosthenes():
    cnt = 0
    for i in range(2, n+1):
        if eratos[i] == True:
            cnt += 1
            for j in range(i*i, n+1, i):
                eratos[j] = False

n = int(input())

eratos = [True] * (n+1)

ans = eratosthenes()
print(ans)
