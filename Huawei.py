# import collections
# class Node():
#     def __init__(self, id, val, left=None, right=None, left_flag = False):
#         self.id = id
#         self.val = val
#         self.left = left
#         self.left_flag = left_flag
#         self.right = right
# nodes_num = int(input())
# weight = input().split()
# weight = [int(i) for i in weight]
# nodes = []
# for i in range(nodes_num):
#     nodes.append(Node(i, weight[i]))
# for i in range(nodes_num-1):
#     each_relation = input()
#     if each_relation=='':
#         break
#     each_relation = each_relation.split()
#     father, child = nodes[int(each_relation[0])], nodes[int(each_relation[1])]
#     if not father.left_flag:
#         father.left = child
#         father.left_flag = True
#     else:
#         father.right = child
# # print(nodes)
# # 写一个层次遍历获得node为根的树之和
# def get_sum(node):
#     result = 0
#     queue = collections.deque()
#     queue.append(node)
#     while queue:
#         temp = queue.popleft()
#         result += temp.val
#         if temp.left != None:
#             queue.append(temp.left)
#         if temp.right != None:
#             queue.append(temp.right)
#     return result
# whole_tree_sum = sum(weight)
# min_id, max_abs = nodes_num + 1, float('-inf')
# def split_node(root, nodes_num, whole_tree_sum):
#     min_id, max_abs = nodes_num+1, float('-inf')
#     if not root:
#         return 0
#     queue = collections.deque()
#     queue.append(root)
#     while queue:
#         temp = queue.popleft()
#         if temp!=root:
#             temp_sum = get_sum(temp)
#             distance = abs(whole_tree_sum-temp_sum-temp_sum)
#             if distance>max_abs:
#                 max_abs = distance
#                 min_id = temp.id
#         if temp.left != None:
#             queue.append(temp.left)
#         if temp.right != None:
#             queue.append(temp.right)
#     return min_id
#
# ans = split_node(nodes[0], nodes_num, whole_tree_sum)
# print(ans)

# size = input.split(',')
# m, n = int(size[0]), int(size[1])
# data = input().split()
# data = [int(i) for i in data]
# matrix = []
# for i in range(m):
#     row = []
#     for j in range(n):
#         row.append(data[i*n+j])
#     matrix.append(row)

# import collections
# time = dict()
# target = input()
# num_module = int(target[-1])
# adjacent = [[] for _ in range(int(target[-1]))]
# indegrees = [0 for _ in range(int(target[-1]))]
# while True:
#     try:
#         rely = input().split(',')
#         time[rely[0]] = int(rely[1])
#         for i in range(2,len(rely)):
#             if rely[i] not in time.keys():
#                 print(-1)
#                 break
#             adjacent[int(rely[i][-1])-1].append(rely[0])
#             indegrees[int(rely[0][-1])-1] += 1
#     except:
#         break
# queue = collections.deque()
# for i in range(num_module):
#     if indegrees[i]==0:
#         queue.append(i)
# while queue:
#     cur = queue.popleft()
#     res
import sys
class Module(object):
    def __init__(self, line_data):
        self.name = line_data[0]
        self.time = line_data[1]
        if len(line_data)>2:
            self.dependency = line_data[2:]
        else:
            self.dependency = []
target_module = input()
modules = dict()

while True:
    try:
        line = input().strip()
    except:
        break

    line = line.split(',')
    line[1] = int(line[1])
    modules[line[0]] = Module(line)


def get_module_time(current_module, modules):
    total_time = current_module.time
    remain_time = 0
    for depend in current_module.dependency:
        current_depend_time = get_module_time(modules[depend], modules)
        if current_depend_time>remain_time:
            remain_time = current_depend_time
    total_time += remain_time
    return total_time

total = get_module_time(modules[target_module], modules)
print(total)

# module3
# module1,10
# module2,5
# module3,10,module1,module2
