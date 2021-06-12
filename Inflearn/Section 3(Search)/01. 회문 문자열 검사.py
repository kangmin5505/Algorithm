import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 3(Search)\input.txt", 'rt')


def palindrome(s):
    length = len(s)

    for i in range(length//2):
        if s[i] != s[length-1-i]:
            return False
    return True

if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        s = input()
        s = s.lower()
        
        if palindrome(s):
            ans = 'YES'
        else:
            ans = 'NO'
        print(f'#{i+1} {ans}')