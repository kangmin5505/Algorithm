import sys

# sys.stdin = open("C:\github\Algorithm\Inflearn\Section 5(Data_Structure)\input.text", "rt")

words_1 = list(input())
words_2 = list(input())
dic = dict()

for word in words_1:
    dic[word] = dic.get(word, 0) + 1
for word in words_2:
    dic[word] = dic.get(word, 0) - 1

for k, v in dic.items():
    if v > 0:
        print("NO")
        break
else:
    print("YES")