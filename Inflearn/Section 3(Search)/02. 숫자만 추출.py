import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')

def extract_number(s):
    res = 0
    for x in s:
        if x.isdecimal():
            res = res*10 + int(x)

    return res


s = input()

ans = extract_number(s)
cnt = 0
for i in range(1, ans+1):
    if ans%i == 0:
        cnt += 1
print(ans)
print(cnt)
