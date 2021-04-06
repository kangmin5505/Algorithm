# 숫자랑 문자랑 따로 저장하고 숫자는 합하기
s = input()

alpha = []
num = 0

for i in s:
    if i.isalpha():
        alpha.append(i)
    else:
        num += int(i)


alpha.sort()
num = str(num)
# join : 리스트를 문자열로 바꿔주는 함수
print(''.join(alpha) + num)
