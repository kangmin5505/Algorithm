"""
stack구조 활용
- 들어가 있는 숫자가 들어갈 숫자보다 작으면 pop
- k번이 완료되면 남은 숫자를 붙이기
- k번이 완료되지 않았는데 number가 없으면 뒤에서부터 자르기
"""
def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number[i])
    answer = "".join(stack[:len(number)-k])
    return answer
    