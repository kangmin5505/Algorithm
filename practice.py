flag = True
for i in range(5):
    for j in range(5):
        print('j', j)
        if i == 3:
            flag = False
            break
    print('i', i)


if flag:
    print('True')
else:
    print('False')
