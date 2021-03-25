# 행이 증가할 때 열이 1씩 증가하는 상황에서 x의 열과 몇 번째인지 찾기
x = int(input())
row = 1

while x > row:
    x -= row
    row += 1
    
position = x
print(f'{row}열')
print(f'{position}번째')
