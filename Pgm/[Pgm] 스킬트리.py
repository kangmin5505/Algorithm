"""
- queue 활용
"""
from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    
    for skill_tree in skill_trees:
        skill_q = deque(list(skill))

        for s in skill_tree:
            if s in skill_q:
                if s != skill_q.popleft():
                    break
        else:
            answer += 1
    
    return answer


# def solution(skill, skill_trees):
#     cnt = 0
#     skill = list(skill)
    
#     for skill_tree in skill_trees:
#         flag = True
#         skill_q = deque(skill)
#         skill_tree_q = deque(skill_tree)
#         while skill_q and skill_tree_q:
#             s = skill_tree_q.popleft()
#             if s in skill_q:
#                 if s != skill_q[0]:
#                     flag = False
#                     break
#                 else:
#                     skill_q.popleft()
        
#         if flag:
#             cnt += 1
    
#     return cnt