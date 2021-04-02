# t = int(input())
# operations = [(100,0), (75,25), (50,50), (25,75)]
# for i in range(t):
#     initial = int(input())
#     a, b = initial, initial
#     for i in range(4):
#         if a-operations[i][0]<0:

import functools
@functools.lru_cache()
def step_sum(a,b):
    if a<0 and b>0:
        return 1
    if a==0 and b==0:
        return 0.5
    if b<0 and a>0:
        return 0
    return (step_sum(a-100,b)+step_sum(a-75,b-25)+step_sum(a-50,b-50)+step_sum(a-25,b-75))/4
t = int(input())
for i in range(t):
    initial = int(input())
    a, b = initial, initial
    print('%.8f'% step_sum(a, b))





# import collections
# t = int(input())
# for i in range(t):
#     num = int(input())
#     data = input()
#     data = data.split(' ')
#     a = [int(i) for i in data]
#     chart = collections.Counter(a)
#     result = 0
#     for item in chart.keys():
#         result += 1
#         if chart[item]>1:
#             # 如果当前元素出现次数>=2，则判断当前元素+1在不在list里，不在则result+1
#             # 在 则item+1的频次+1（这么操作，万一item+1只出现一次，也可以+1避开，如果出现两次以上，则对结果没影响）
#             if item+1 not in chart:
#                 result += 1
#             else:
#                 chart[item+1] += 1
#     print(result)
#
