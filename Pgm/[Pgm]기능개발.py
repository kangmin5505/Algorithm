# # 걸리는 시간으로 풀었을 때
# import math

# def solution(progresses, speeds):
#     answer = []

#     # 걸리는 시간 구하기
#     work_day = list(math.ceil((100-a)/b) for a, b in zip(progresses, speeds))
    
#     # 기준점
#     base = 0

#     for idx in range(len(work_day)):
#         if work_day[idx] > work_day[base]:
#             answer.append(idx - base)
#             base = idx
#     # 마지막 남은 일 처리
#     # work_day의 갯수는 idx의 최댓값 + 1
#     answer.append(len(work_day) - base)

#     return answer
from collections import deque


def solution(progresses, speeds):
    
    answer = []
    time = 0
    count = 0 

    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        # 처리 가능한 것들을 한 번에 처리
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        else:
            # 처리할 수 없는 것을 만났을 때 count가 1개라도 있으면 추가시키고 count 초기화
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))