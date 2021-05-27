# 날짜 계산

E, S, M = map(int, input().split())
year = 1

while True:
    # 몫(year)에서 나머지(E or S or M)을 뺐을 때 0이 나오는 것이 조건을 만족하는 몫임
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
        print(year)
        break
    year += 1
