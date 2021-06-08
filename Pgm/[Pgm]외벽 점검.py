from itertools import permutations


def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    answer = len(dist) + 1
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            # 투입할 친구의 수
            count = 1
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start+1, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    # 새로운 친구를 투입
                    count += 1
                    # 더 투입이 불가능하다면 종료
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            # 최솟값 계산
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
