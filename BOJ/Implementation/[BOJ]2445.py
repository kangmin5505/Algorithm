# 별 찍기 - 8
n = int(input())

# for i in range(1, n+1):
#     print('*' * i + ' ' * 2*(n-i) + '*' * i)

# for i in range(n-1, 0, -1):
#     print('*' * i + ' ' * 2*(n-i) + '*' * i)

for i in range(2*n - 1):
    blank = abs((n - (i+1)))
    star = n - blank
    print('*'*star + ' '*2*blank + '*'*star)
