# 스타트와 링크
# n은 짝수
import sys
from itertools import combinations
input = sys.stdin.readline


def ability(team):
    total = 0
    length = len(team)
    for i in range(length-1):
        for j in range(i+1, length):
            total += graph[team[i]][team[j]]

    return total


n = int(input())
graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
with open('C:\github\Algorithm\Back-Tracking\input.txt', 'r') as f:
    for _ in range(n):
        line = f.readline().rstrip()
        graph.append(list(map(int, line.split())))

for i in range(n-1):
    for j in range(i+1, n):
        graph[i][j] += graph[j][i]
print(graph)

team_list = list(combinations(range(n), n//2))
result = 1e9

for team in team_list:
    start_team = team
    link_team = tuple([x for x in range(n) if x not in team])

    start_team_ability = ability(start_team)
    link_team_ability = ability(link_team)

    result = min(result, abs(start_team_ability - link_team_ability))

print(result)
