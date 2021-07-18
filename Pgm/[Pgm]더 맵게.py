import heapq


def solution(scoville, K):
    answer = -1
    heapq.heapify(scoville)

    cnt = 0
    while True:
        a = heapq.heappop(scoville)
        if a >= K:
            answer = cnt
            break
        if len(scoville) == 0:
            break
        b = heapq.heappop(scoville)
        tmp = a + b*2
        heapq.heappush(scoville, tmp)
        cnt += 1

    return answer
