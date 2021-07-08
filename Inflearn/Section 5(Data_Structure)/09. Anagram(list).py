import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 5(Data_Structure)\input.text", "rt")

word1 = input()
word2 = input()
n = 52
str1 = [0] * n
str2 = [0] * n
# 대문자 -65 소문자 -71

for word in word1:
    if word.isupper():
        str1[ord(word)-65] += 1
    else:
        str1[ord(word)-71] += 1

for word in word2:
    if word.isupper():
        str2[ord(word)-65] += 1
    else:
        str2[ord(word)-71] += 1

for i in range(n):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")