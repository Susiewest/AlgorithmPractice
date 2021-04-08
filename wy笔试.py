1. 数组的子数组，和为6的倍数，最大是多少
2. 最小编辑距离，改的cost是2，其他是1，结果保留两位小数
3. 优惠券满减门限T，最少花多少钱
4. 树找存在节点大于x的路径，保存在数组中，不用构造树，因为是完全二叉，空节点在list中为null，可以直接下标2+1，下标2+2确定左右孩子节点。
import copy
import json

tree_temp = input()
tree_temp = json.loads(tree_temp)
tree = []
for i in tree_temp:
    if i!=None:
        tree.append(int(i))
    else:
        tree.append(-1)

x = input()
x = int(x)

class Solution:
    def __init__(self):
        self.result = []
    def search(self, tree, route, index, x):
        # 如果当前节点的值大于x，则为候选路径
        # 如果存在多条，则选择更短的
        # 如果多条长度相同，选择最大值最大的
        # 如果最大值相同，选最左边的
        if tree[index]>x:
            route.append(tree[index])
            if len(self.result) == 0:
                self.result = route.copy()
            else:
                # 如果存在多条，则选择更短的
                if len(route)<len(self.result):
                    self.result = route.copy()
                # 如果多条长度相同，选择最大值最大的
                elif len(route)==len(self.result):
                    if max(route)>max(self.result):
                        self.result = route.copy()
        # 如果当前节点不大于x，则继续
        else:
            route.append(tree[index])
            left_child_index = index*2 + 1
            if left_child_index<len(tree) and tree[left_child_index]!=-1:
                self.search(tree, route, left_child_index, x)
                route.pop()
            right_child_index =index*2 + 2
            if right_child_index<len(tree) and tree[right_child_index]!=None:
                self.search(tree, route, right_child_index, x)
                route.pop()
        return self.result

sol = Solution()
ans = sol.search(tree, [], 0, x)
print(ans)

# T = input()
# T = int(T)
# y = input()
# y = int(y)
# price = input()
# price = price.split()
# price = [int(i) for i in price]
# price.sort()
#
#
# #
# # if sum(price) < T:
# #     return False
#
#
# left, right = 0, len(price) - 1
# # 初始化为最大的两个价值相加
# min_combine = price[-2] + price[-1]
# while left < right:
#     current_sum = price[left] + price[right]
#     if current_sum > T and current_sum < min_combine:
#         min_combine = current_sum
#     if current_sum < T:
#         left += 1
#     else:
#         right -= 1
# print(min_combine)

# 2 ac
# s0 = input()
# s1 = input()
#
#
# def eidt_dist(first, second):
#     row = len(first)
#     col = len(second)
#     dp = [[0] * (col + 1) for _ in range(row + 1)]
#     # 初始化第一行
#     for j in range(1, col+1):
#         dp[0][j] = dp[0][j-1] + 1
#     for i in range(1, row+1):
#         dp[i][0] = dp[i-1][0] + 1
#     for i in range(1, row+1):
#         for j in range(1, col+1):
#             if first[i-1] == second[j-1]:
#                 dp[i][j] = dp[i-1][j-1]
#             else:
#                 dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
#     return dp[-1][-1]
#
#
# edit = eidt_dist(s0, s1)
# print(edit)
# sum_length = len(s1)+len(s0)
# sum_length = len(s1)+len(s0)
# result = (sum_length-edit)/sum_length
# print('%.2f'%result)
#

# no1 ac
# n = input()
# n = int(n)
# nums = input()
# nums = nums.split()
# nums = [int(i) for i in nums]
#
# def find_six(nums):
#     dp = [float('-inf')]*6
#     dp[0] = 0
#     next = [0]*6
#     for num in nums:
#         for i in range(6):
#             next[(num+i)%6] = max(dp[(num+i)%6], dp[i]+num)
#         for i in range(6):
#             dp[i] = next[i]
#             next[i] = 0
#     return dp[0] if dp[0]!=0 else -1
# print(find_six(nums))
