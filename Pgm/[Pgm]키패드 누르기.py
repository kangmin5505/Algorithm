def get_distance(prev, now):
    res = 0
    for x, y in zip(prev, now):
        res += abs(x - y)
    return res


def solution(numbers, hand):
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ["*", 0, "#"]
    ]

    answer = ''
    left = (3, 0)
    right = (3, 2)
    for num in numbers:
        for x in range(len(keypad)):
            for y in range(len(keypad[0])):
                if num == keypad[x][y]:
                    now = (x, y)
                    if num in [1, 4, 7]:
                        answer += "L"
                        left = now
                    elif num in [3, 6, 9]:
                        answer += "R"
                        right = now
                    else:
                        left_distance = get_distance(left, now)
                        right_distance = get_distance(right, now)
                        if left_distance > right_distance:
                            answer += "R"
                            right = now
                        elif left_distance < right_distance:
                            answer += "L"
                            left = now
                        else:
                            if hand == "right":
                                answer += "R"
                                right = now
                            else:
                                answer += "L"
                                left = now

    return answer
