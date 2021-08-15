data = input()
n, m = data.split()
chart = []
count = 0
while count< int(n):
    line = input()
    temp = list(map(int,line.split()))
    chart.append(temp)
    count += 1
visited = [[False for _ in range(len(chart))] for _ in range(len(chart[0]))]
def isMatch(m, chart):
    order = [1, 2]
    if m==1 or m==2:
        return order[m-1]
        #print(order[m-1])
    temp_j, temp_i = 0, 1
    visited_list = []
    for i in range(int(m)-2):
        new_pos = chart[temp_i][temp_j]-1
        if visited[temp_i][temp_j]==False:
            visited[temp_i][temp_j] = True
            visited_list.append(new_pos)
        else:
            return visited_list[(int(m)-2)%i]
        temp_j, temp_i = temp_i, new_pos
    return new_pos+1
print(isMatch(m, chart))

# no 3 ok
# data = input().split()
# milk_tea =  [int(i) for i in input().split()]
# n, m = int(data[0]), int(data[1])
# c = int(data[2])
# # 对奶茶分组，使得子数组和的最大值最小
# def check(x):
#     total, count = 0, 1
#     for num in milk_tea:
#         if total+num > x:
#             count += 1
#             total = num
#         else:
#             total += num
#     return count<=m
#
# left = max(milk_tea)
# right = sum(milk_tea)
# while left<right:
#     mid = (left+right)//2
#     if check(mid):
#         right = mid
#     else:
#         left = mid + 1
# max_sum = left
# if max_sum%c==0:
#     print(max_sum//c)
# else:
#     print(max_sum//c+1)
# print(math.ceil(max_sum//c))
# todo no 4 36ac
data = input()
n, m = data.split()
chart = []
count = 0
while count< int(n):
    line = input()
    temp = list(map(int,line.split()))
    chart.append(temp)
    count += 1
def isMatch(m, chart):
    order = [1, 2]
    if m==1 or m==2:
        return order[m-1]
        #print(order[m-1])
    temp_j, temp_i = 0, 1
    for i in range(int(m)-2):
        new_pos = chart[temp_i][temp_j]-1
        temp_j, temp_i = temp_i, new_pos
    return new_pos+1
print(isMatch(m, chart))
# todo: no 2 45ac
data = input()
data = data.split()
data = [int(i) for i in data]
n = data[0]
m = data[1]

# get a
a = input()
a = a.split()
a = [int(i) for i in a]
# 去重
a = list(set(a))

# get b
b = input()
b = b.split()
b = [int(i) for i in b]
# 去重
b = set(b)

x = 1
while True:
    new_a = [(num+x)%m for num in a]
    new_a = set(new_a)
    if new_a == b:
        print(x)
        break
    else:
        x += 1


# 第三题 18ac
# import math
# data = input().split()
# milk_tea =  [int(i) for i in input().split()]
# n, m = int(data[0]), int(data[1])
# c = int(data[2])
#
#
# # sliding_window = [float('inf'), float('inf')]
# current_window = 0
# for i in range(m):
#     current_window += milk_tea[i]
# # sliding_window.append(temp)
# min_sum = current_window
# for i in range(m,len(milk_tea)):
#     current_window = current_window-milk_tea[i-m]+milk_tea[i]
#     if current_window<min_sum:
#         min_sum = current_window
# print(math.ceil(min_sum//c))






# generate_str = input()
# target_str = input()
# index_chart = {}
# length = 26
#
# for i in range(len(generate_str)):
#     index_chart[generate_str[i]] = i
# result = length-1  #处理第一个字母
# for i in range(1, len(target_str)):
#     if index_chart[target_str[i]]>index_chart[target_str[i-1]]:
#         result -= 1
#     else:
#         result += length-1
# result -= length-index_chart[target_str[-1]]-1
# print(result)

====================================================================秋招==========================================================================


# T = int(input())
# for i in range(T):
#     n = int(input())
#     data = input().split(' ')
#     data = [int(i) for i in data]
#     # data.append(0)
#     # flag = False
#     # for j in range(len(data)):
#     #     while data[j]!=j:
#     #         if data[j] < 0 or data[j]>n:
#     #             print('No')
#     #             flag = True
#     #             break
#     #         if data[data[j]]==data[j]:
#     #                 print('No')
#     #                 flag = True
#     #                 break
#     #         else:
#     #             data[data[j]], data[j] = data[j], data[data[j]]
#     #     if flag:
#     #             break
#     # if not flag:
#     #     print('Yes')
#     hash_dict = dict()
#     flag = False
#     for i in range(len(data)):
#         if data[i]<1 or data[i]>n:
#             print('No')
#             flag = True
#             break
#         if data[i] not in hash_dict.keys():
#             hash_dict[data[i]] = 1
#         else:
#             print('No')
#             flag = True
#             break
#     if not flag:
#         print('Yes')


# data = input()
# # if data==data[::-1]:
# #     print(0)
# # else:
# #     for i in range(1,len(data)+1):
# #         new_data = data+data[:i]
# #         if new_data==new_data[::-1]:
# #             print(i)
# if data==data[::-1]:
#     print(0)
# else:
#     index = []
#     for i in range(len(data)):
#         if data[i]==data[-1]:
#             index.append(i)
#     for item in index:
#         temp_data = data[item:]
#         if temp_data==temp_data[::-1]:
#             print(item)
#             break

# data = input()
# if data==data[::-1]:
#     print(0)
# if data[-1] not in set(data[:-1]):
#     print(len(data)-1)
# else:
#     index = []
#     for i in range(len(data)):
#         if data[i]==data[-1]:
#             index.append(i)
#     for item in index:
#         temp_data = data[item:]
#         if temp_data==temp_data[::-1]:
#             print(item)
#             break
#
# data = input()
# flag = False
# if data==data[::-1]:
#     print(0)
#     flag = True
# if not flag and data[-1] not in set(data[:-1]):
#     print(len(data)-1)
#     flag = True
# if not flag:
#     index = []
#     for i in range(len(data)):
#         if data[i]==data[-1]:
#             index.append(i)
#     for item in index:
#         temp_data = data[item:]
#         if temp_data==temp_data[::-1]:
#             print(item)
#             break
# T = int(input())
# for i in range(T):
#     n = int(input())
#     data = input().strip()
#     data = data.split(' ')
#     data = [int(i) for i in data]
#     # data.append(0)
#     # flag = False
#     # for j in range(len(data)):
#     #     while data[j]!=j:
#     #         if data[j] < 0 or data[j]>n:
#     #             print('No')
#     #             flag = True
#     #             break
#     #         if data[data[j]]==data[j]:
#     #                 print('No')
#     #                 flag = True
#     #                 break
#     #         else:
#     #             data[data[j]], data[j] = data[j], data[data[j]]
#     #     if flag:
#     #             break
#     # if not flag:
#     #     print('Yes')
#     hash_dict = dict()
#     flag = False
#     for i in range(len(data)):
#         if data[i]<1 or data[i]>n:
#             print('No')
#             flag = True
#             break
#         if data[i] not in hash_dict.keys():
#             hash_dict[data[i]] = 1
#         else:
#             print('No')
#             flag = True
#             break
#     if not flag:
#         print('Yes')
import copy
n = int(input())
robots = []
for i in range(n):
    input_str = input().split(' ')
    pos = int(input_str[0])
    if input_str[1]=='L':
        direction = -1
    else:
        direction = 1
    robots.append([i,pos,direction])
robots = sorted(robots, key=(lambda  x:x[1]))
ans = [-1]*n
stack0 = []
stack1 = []
for i in range(n):
    if robots[i][1]%2==0:
        if robots[i][2]==1:
            stack0.append(copy.deepcopy(robots[i]))
        else:
            if len(stack0)>0:
                ans[robots[i][0]]=int(abs(robots[i][1]-stack0[-1][1])/2)
                ans[stack0[-1][0]] = ans[robots[i][0]]
                stack0.pop()
    else:
        if robots[i][2]==1:
            stack1.append(copy.deepcopy(robots[i]))
        else:
            if len(stack0)>0:
                ans[robots[i][0]] = int(abs(robots[i][1]-stack0[-1][1])/2)
                ans[stack0[-1][0]] = ans[robots[i][0]]
                stack1.pop()
for num in ans:
    print(num)
