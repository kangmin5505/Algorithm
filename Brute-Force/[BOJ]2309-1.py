# 일곱 난쟁이
# combinations 안 쓰고 풀기

def bruteForce():
    for i in range(n-1):
        for j in range(i+1, n):
            if dataSum - data[i] - data[j] == 100:
                rm1 = data[i]
                rm2 = data[j]
                data.remove(rm1)
                data.remove(rm2)
                data.sort()
                return data


n = 9
data = [int(input()) for _ in range(n)]
dataSum = sum(data)

answer = bruteForce()

for i in answer:
    print(i)
