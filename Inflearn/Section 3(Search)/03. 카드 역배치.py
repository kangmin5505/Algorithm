import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')

n = 10
array = list(range(21))

for _ in range(n):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        array[a+i], array[b-i] = array[b-i], array[a+i]

for i in range(1, 21):
    print(array[i], end=' ')