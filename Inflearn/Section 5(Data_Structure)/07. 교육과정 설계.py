import sys
from collections import deque

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 5(Data_Structure)\input.text", "rt")

needs = list(input())
n = int(input())

for i in range(n):
    flag = True
    q_needs = deque(needs)
    subjects = list(input())
    subjects = deque(subjects)

    while q_needs and subjects:
        subject = subjects.popleft()
        if subject in q_needs:
            if subject != q_needs.popleft():
                flag = False
                break
    if q_needs:
        flag = False
    if flag:
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")
