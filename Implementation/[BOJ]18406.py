# 점수 score을 반으로 나누어 좌와 우가 같은지 확인

score = input()

left_score = score[:len(score)//2]
right_score = score[len(score)//2:]

left_sum = 0
right_sum = 0
for num in left_score:
    left_sum += int(num)
for num in right_score:
    right_sum += int(num)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")
