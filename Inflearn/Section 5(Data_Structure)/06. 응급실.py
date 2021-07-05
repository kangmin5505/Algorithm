import sys
from collections import deque

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 5(Data_Structure)\input.text", "rt")

"""
1. enumerate로 쌍 지어서 넣기
2. any함수 쓰기
"""

n, k = map(int, input().split(' '))
patients = list(map(int, input().split()))
patients = [(n, patient) for n, patient in enumerate(patients)]
patients = deque(patients)
cnt = 0


while True:
    idx, patient = patients.popleft()
    if any(x[1] > patient for x in patients):
        patients.append((idx, patient))
    else:
        cnt += 1
        if idx == k:
            print(cnt)
            break
