# 92%
# N = int(input())
# for i in range(N):
#     result = 0
#     data = input().split(' ')
#     x, y = int(data[0]), int(data[1])
#     r = int(data[2])
#     x, y = abs(x), abs(y)
#     temp = x**2+y**2
#     r_temp = r**2
#     if x-r<0 and y-r<0 and temp!=r_temp:
#         result = 4
#     if (x-r<0 and y-r<0 and temp==r_temp) or (x-r<0 and y-r==0) or (y-r<0 and x-r==0):
#         result = 3
#     if (x-r<0 and y-r>0) or (y-r<0 and x-r>0) or (x-r==0 and y-r==0) or (x-r<0 and y-r==0 and temp==r_temp) or (y-r<0 and x-r==0 and temp==r_temp):
#         result = 2
#     if (x-r==0 and y-r>0) or (y-r==0 and x-r>0):
#         result = 1
#     print(result)

# 2.
# data = input().split(' ')
# n, t = int(data[0]), int(data[1])
# c = int(data[2])
# result= 0
# candy = input()
# candy = [int(i) for i in candy.split(' ')]
# over_sweet = []
# for index, item in enumerate(candy):
#     if item>t:
#         over_sweet.append(index)
# left, right = 0, c-1
# i = 0
# while(right<n):
#     if i >= len(over_sweet):
#         result += n-left-c+1
#         break
#     if max(candy[left:right+1]) <= t:
#         result += 1
#         left += 1
#     else:
#         left = over_sweet[i]
#         i += 1
#     right = left + c - 1
# # print(count)
# # for item in candy:
# #     count = count+1 if item<=t else 0
# #     result += count
# print(result)

#2 100%
# data = input().split(' ')
# n, t = int(data[0]), int(data[1])
# c = int(data[2])
# result= 0
# candy = input()
# candy = [int(i) for i in candy.split(' ')]
# over_sweet = list()
# for index, item in enumerate(candy):
#     if item>t:
#         over_sweet.append(index)
# left, right = 0, c-1
# i = 0
# while(right<n):
#     if i >= len(over_sweet):
#         result += n-left-c+1
#         break
#     if max(candy[left:right+1]) <= t:
#         result += 1
#         left += 1
#     else:
#         left = over_sweet[i]+1
#         i += 1
#     right = left + c - 1
# print(count)
# for item in candy:
#     count = count+1 if item<=t else 0
#     result += count
#print(result)

data = input().split(' ')
N, M = int(data[0]), int(data[1])
count = 0
def backtrack(nums):


# oper = int(input())
# dict = {'(':0, ')':0}
# str_oper = input()
