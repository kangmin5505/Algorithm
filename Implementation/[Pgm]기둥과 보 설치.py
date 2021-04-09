# 작업을 기준으로 판단
# 규칙을 만족하는 지 확인하는 함수(Possible)를 통해 구조물을 기준으로 판단

def possible(answer):
    for x, y, stuff in answer:
        # 기둥, 보로 구분하여 확인
        if stuff == 0:
            # 기둥 설치 시 규칙
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            # 위의 규칙을 만족하지 않으면 False
            return False
        elif stuff == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    # 조건을 다 만족할 경우 True
    return True


def solution(n, build_frame):
    answer = []  # 리스트가 아닌 집합으로 선언하여 결과값 반환시 리스트로 변환해주면 속도가 조금 빠르다
    for frame in build_frame:
        x, y, stuff, operate = frame
        # 삭제, 설치로 구분하여 확인
        if operate == 0:
            # 삭제시키고 확인
            answer.remove([x, y, stuff])
            # 규칙을 위반할 경우 원상복구
            if not possible(answer):
                answer.append([x, y, stuff])
        elif operate == 1:
            # 설치하고 확인
            answer.append([x, y, stuff])
            # 규칙을 위반할 경우 원상복구
            if not possible(answer):
                answer.remove([x, y, stuff])

    # 정렬 후 반환(첫 번째 값이 같을 경우 두 번째 값 오름차순으로 정렬 됨)
    return sorted(answer)
