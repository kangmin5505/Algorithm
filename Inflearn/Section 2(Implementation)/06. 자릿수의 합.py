import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 2(Implementation)\input.txt", "rt")

# def digit_sum(x):
#     total = 0
#     for i in str(x):
#         total += int(i)
#     return total

def digit_sum(num):
    total = 0
    
    while num > 0:
        total += num%10
        num = num//10

    return total


n = int(input())
data = list(map(int, input().split()))

max_val = 0
for x in data:
    temp = digit_sum(x)
    if temp > max_val:
        max_val = temp
        ans = x

print(ans)