import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 5(Data_Structure)\input.text", "rt")

n = int(input())

dic = dict()
for _ in range(n):
    word = input()
    dic[word] = 1

for _ in range(n-1):
    word = input()
    dic[word] = 0

for key, value in dic.items():
    if value == 1:
        print(key)
        break