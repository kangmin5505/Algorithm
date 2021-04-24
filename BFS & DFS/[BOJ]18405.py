# 경쟁적 전염
# 낮은 숫자부터 순서대로 진행해야 함으로 BFS 구조 사용
# 종료 조건은 시간이 다 되거나 실행조건을 다 완료하거나
from collections import deque

n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    # data에 virus번호, 시간, x좌표, y좌표 넣기
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

# 번호 순서대로 정렬
data.sort()
# data를 deque에 넣기
q = deque(data)

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

target_s, target_x, target_y = map(int, input().split())

while q:
    virus, s, x, y = q.popleft()
    # 종료 조건
    if s == target_s:
        break

    # 상하좌우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안에 들어오는지 확인
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # virus가 감염이 안 된 지역인지 확인
            if graph[nx][ny] == 0:
                # 감염된 지역이라면 감염시키고 s+1해서 q에 넣기
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])
