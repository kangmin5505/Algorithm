"""
1. stack구조를 사용하고, 우선순위가 높은 연산자가 들어가 있을 경우 pop
    => '*', '/'가 들어갈 경우 안에 있는 '*', '/' pop
2. ')'가 나올 경우 '('까지 전부 연산자 pop

"""

# import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 5(Data_Structure)\input.text", "rt")

s = input()
stack = []
ans = ''
for x in s:
    if x.isdecimal():
        ans += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '/' or stack[-1] == '*'):
                ans += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(x)
        else:
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()

while stack:
    ans += stack.pop()

print(ans)