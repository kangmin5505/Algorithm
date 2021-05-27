# 좌표 압축

n = int(input())
data = list(map(int, input().split()))
# set은 중복 제거
data2 = list(sorted(set(data)))
# dictionary는 시간복잡도 O(1)이고 enumberate함수는 0부터 숫자 지정 가능.
# enumerate(리스트, start=x)로 시작 숫자 지정 가능
dic = {value: index for index, value in enumerate(data2)}

for i in data:
    print(dic[i], end=' ')
