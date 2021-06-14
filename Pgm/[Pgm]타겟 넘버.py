def DFS(L, total, numbers, target):
    global answer
    if L == len(numbers):
        if total == target:
            answer += 1
    else:
        DFS(L+1, total+numbers[L], numbers, target)
        DFS(L+1, total-numbers[L], numbers, target)

answer = 0
def solution(numbers, target):

    DFS(0, 0, numbers, target)
    
    return answer