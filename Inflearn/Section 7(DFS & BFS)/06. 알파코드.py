# 1 ~ 26까지 확인하기
# 마지막 숫자 뒤에 -1 넣어주기
# 숫자를 대문자로 변경하려면 chr(i + 64)

def DFS(L):
    global cnt
    if L == n:
        cnt += 1
        for x in result:
            print(chr(x+64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[L] == i:
                result.append(i)
                DFS(L+1)
                result.pop()
            elif i >= 10 and code[L] == i//10 and code[L+1] == i % 10:
                result.append(i)
                DFS(L+2)
                result.pop()


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.append(-1)
    cnt = 0
    result = []

    DFS(0)
    print(cnt)
