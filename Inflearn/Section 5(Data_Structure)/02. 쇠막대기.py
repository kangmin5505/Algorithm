"""
1. '(' 면 append
2. ')'인데 그 전 것이 '('이면 pop하고 현재 리스트 길이 더하기
3. ')'인데 그 전 것이 ')'이면 pop하고 +1
"""
# import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 5(Data_Structure)\input.text", "rt")

brackets = input()
stack = []
ans = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append(brackets[i])
    else:
        stack.pop()
        if brackets[i-1] == '(':
            ans += len(stack)
        else:
            ans += 1

print(ans)