def solution(n, lost, reserve):
    answer = 0
    array = [1] * (n+1)
    for idx in lost:
        array[idx] -= 1
    for idx in reserve:
        array[idx] += 1

    for idx in range(1, n+1):
        if idx == 1 and array[idx] == 0:
            if array[idx+1] == 2:
                array[idx+1] -= 1
                array[idx] += 1
        elif idx == n and array[idx] == 0:
            if array[idx-1] == 2:
                array[idx-1] -= 1
                array[idx] += 1
        else:
            if array[idx] == 0:
                if array[idx-1] == 2:
                    array[idx-1] -= 1
                    array[idx] += 1
                elif array[idx+1] == 2:
                    array[idx+1] -= 1
                    array[idx] += 1
    for i in range(1, n+1):
        if array[i] >= 1:
            answer += 1

    return answer


n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))
