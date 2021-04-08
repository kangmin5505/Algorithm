x, y = map(int, input().split())
for i in range(1, x):
    if i in [1, 3, 5, 7, 8, 10, 12]:
        y += 31
    elif i == 2:
        y += 28
    else:
        y += 30
`
day_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(day_week[y % 7])
