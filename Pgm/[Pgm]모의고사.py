def solution(answers):
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0] * 4
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern_1[idx%len(pattern_1)]:
            score[1] += 1
        if answer == pattern_2[idx%len(pattern_2)]:
            score[2] += 1
        if answer == pattern_3[idx%len(pattern_3)]:
            score[3] += 1
        
    for i in range(1, 4):
        if score[i] == max(score):
            result.append(i)

    return result



answers = [1,3,2,4,2]
print(solution(answers))