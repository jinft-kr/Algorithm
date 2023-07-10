# def solution(name, yearning, photo):
#     # score = {}
#     #
#     # for i, j in zip(name, yearning):
#     #     score[i] = j
#     score = dict(zip(name, yearning))
#
#     answer = []
#
#     for item in photo:
#         sum = 0
#         for i in item:
#             # if i in score.keys():
#             if i in score:
#                 sum += score[i]
#         answer.append(sum)
#
#     return answer
#
# name = ["may", "kein", "kain", "radi"]
# yearning = [5, 10, 1, 3]
# photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
# print(solution(name,yearning, photo))
d1= dict(a=1, b=2)
d2= dict(c=3, d=4)
d3=dict(d1,**d2)

print(d3)