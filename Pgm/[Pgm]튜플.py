def solution(s):
    answer = []
    # 앞 뒤 {{}} 제거
    s = s[2:-2]
    # },{ 기준으로 나눠주기
    s = s.split("},{")
    # 길이 순서로 
    s.sort(key=len)

    for i in s:
        # , 기준으로 리스트 생성
        i = i.split(',')
        print(i)
        for j in i:
            j = int(j)
            if j not in answer:
                answer.append(j)

    return answer
