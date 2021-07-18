from collections import deque


def solution(n, words):
    # answer = [0, 0]
    # q = deque(words)
    # tmp = [q.popleft()]
    # while q:
    #     word = q.popleft()
    #     if word in tmp or tmp[-1][-1] != word[0]:
    #         answer = [(len(tmp)%n)+1, (len(tmp)//n)+1]
    #         break
    #     tmp.append(word)
    # return answer

    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [len(words[:i]) % n + 1, len(words[:i])//n + 1]
    return [0, 0]
