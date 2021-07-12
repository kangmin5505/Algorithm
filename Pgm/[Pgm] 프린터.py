from collections import deque


def solution(priorities, location):
    p_list = [(idx, p) for idx, p in enumerate(priorities)]
    cnt = 0
    p_list = deque(p_list)
    while p_list:
        idx, p = p_list.popleft()
        if any(p < priority[1] for priority  in p_list):
            p_list.append((idx, p))
        else:
            cnt += 1
            if idx == location:
                answer = cnt
                break
    return answer