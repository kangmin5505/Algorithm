# ' '와 '*'로 구분지어서 생각
num = int(input())

for i in range(num, 0, -1):
    print(' ' * (num - i) + '*' * (2 * i - 1))
for i in range(2, num+1):
    print(' ' * (num - i) + '*' * (2 * i - 1))
