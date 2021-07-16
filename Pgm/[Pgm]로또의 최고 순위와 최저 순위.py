def solution(lottos, win_nums):
    # answer = []
    # max_cor = 0
    # min_cor = 0
    # for lot in lottos:
    #     if lot in win_nums:
    #         max_cor += 1
    #         min_cor += 1
    #     elif lot == 0:
    #         max_cor += 1
    # answer = [7-max_cor if max_cor > 1 else 6, 7-min_cor if min_cor > 1 else 6]
    # return answer
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)
    cnt_cor = len([x for x in lottos if x in win_nums])
    answer = [rank[cnt_cor+cnt_0], rank[cnt_cor]]
    return answer
