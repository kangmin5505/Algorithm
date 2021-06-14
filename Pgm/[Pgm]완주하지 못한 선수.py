def solution(participant, completion):
    array = dict()
    for name in participant:
        if name not in array:
            array[name] = 1
        else:
            array[name] += 1
    
    
    for name in completion:
        array[name] -= 1
    
    for k, v in array.items():
        if v != 0:
            answer = k
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))