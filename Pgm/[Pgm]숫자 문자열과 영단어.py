# def solution(s):
#     check = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
#     result = []
#     tmp = ''
#     for i in s:
#         if i.isdigit():
#             result.append(i)
#         else:
#             tmp += i
#             if tmp in check:
#                 result.append(tmp)
#                 tmp = ''
#     for i in range(len(result)):
#         s = result[i]
#         if s in check:
#             result[i] = str(check.index(s))
#     answer = int("".join(result))
#     return answer


def solution(s):
    answer = s
    dic = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", 'seven': "7", "eight": "8", "nine": "9"
    }

    for key, val in dic.items():
        answer = answer.replace(key, val)

    answer = int(answer)
    return answer
