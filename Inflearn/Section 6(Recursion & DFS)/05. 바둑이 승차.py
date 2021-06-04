# c를 넘지않으면서 dogs의 부분집합을 구해 가장 큰 값 찾기
import sys

# sys.stdin = open(
#     "C:\\01. Study\Algorithm\Inflearn Algorithm(Python)\Section 6(Recursion&DFS)\input.txt", "rt")


def DFS(L, sub_total, total_sum):
    global answer
    # Cut Edge
    # 지금까지 구한 합(sub_total)에서 남은 개들의 총 무게를 더했을 때
    # answer보다 작으면 그 이상은 확인할 필요 없음
    if sub_total+(total-total_sum) < answer:
        return
    if sub_total > c:
        return
    if L == n:
        if sub_total > answer:
            answer = sub_total
    else:
        DFS(L+1, sub_total+dogs[L], total_sum+dogs[L])
        DFS(L+1, sub_total, total_sum+dogs[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    dogs = []
    for _ in range(n):
        dog = int(input())
        dogs.append(dog)

    dogs.sort(reverse=True)
    total = sum(dogs)
    answer = 0
    DFS(0, 0, 0)
    print(answer)
