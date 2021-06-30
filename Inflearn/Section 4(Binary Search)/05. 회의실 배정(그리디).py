import sys

sys.stdin = open(
    "C:\\github\\Algorithm\\Inflearn\\Section 4(Binary Search)\\input.txt", "rt")


"""
1. 끝나는 시간을 기준으로 정렬
2. 끝나는 시간(end_time) > 다음 회의 시작시간(start_time) 이면 건너뛰기
3. 끝나는 시간(end_time) <= 다음 회의 시작시간(start_time) 이면 cnt+=1 
4. end_time = 다음 회의 끝나는 시간
"""

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x:x[1])

cnt = 0
end_time = 0
for s_time, e_time in time:
    if s_time >= end_time:
        cnt += 1
        end_time = e_time

print(cnt)