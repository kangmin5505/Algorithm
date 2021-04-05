# 방향리스트 생성
# 방문리스트 생성
# 왼쪽방향으로 움직이는 함수 생성

# text_case
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1


# 입력
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
# 방문리스트 생성
visited = [[False] * m for _ in range(n)]
# 시작지점은 방문
visited[x][y] = True

# 지도 입력
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

# 방향리스트 생성
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽방향으로 움직이는 함수 생성


def turn_left():
    # 전역변수로 선언
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
turn_time = 0
count = 1
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if maps[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if maps[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0
        # 뒤가 바다로 막혀있는 경우
        else:
            break

print(count)
