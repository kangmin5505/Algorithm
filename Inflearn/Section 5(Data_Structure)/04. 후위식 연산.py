# import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 5(Data_Structure)\input.text", "rt")

s = input()
ans = []
for x in s:
    if x.isdigit():
        ans.append(int(x))
    else:
        pop_1 = ans.pop()
        pop_2 = ans.pop()
        if x == '+':
            ans.append(pop_2 + pop_1)
        elif x == '/':
            ans.append(pop_2 / pop_1)
        elif x == '*':
            ans.append(pop_2 * pop_1)
        else:
            ans.append(pop_2 - pop_1)

print(ans[0])
