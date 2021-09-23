ms笔试

像素渲染 打包成tuple，sort，从小到大排序，贪心记录最多渲染多少

节点之间的权值最大，算每个点的入度出度和，大的代表参与的路径多，贡献大，为了让总权值最大，就把大的权值赋给这种节点，也相当于贪心了？

数组中切两刀成三个链，求切的cost最小，用了三个方法，一暴力，二双指针，大的一个指针挪动， 三构建大根堆，除去开头结尾 挑出来四个最小的数，两两结合验证下标是否符合相差大于1
第三题有个测试用例没过，经过我思考，应该是遗漏了处理 数组长度为5的边界情况，这样必须选第二个数和第四个数，而不能按照上面的思路构造大小为4的堆！

bst找中位数，空间复杂度O（1） 时间复杂度O（n）

class Node():
    def __init__(self, value, left, right):
        self.val = value
        self.left = left
        self.right = right
class Solution():
    def __init__(self):
        self.node_num = 0
        self.count = 0
        self.result = -1

    def inorder(self, root, target):
        if not root:
            return
        self.inorder(root.left, target)
        self.count += 1
        if self.count == target:
            self.result = root.val
        self.inorder(root.right, target)

    def bst(self, root):
        if not root:
            return False
        def dfs(root):
            if not root:
                return
            self.node_num += 1
            dfs(root.left)
            dfs(root.right)
        dfs(node1)
        if self.node_num%2:
            target = self.node_num//2 +1
        else:
            target = self.node_num//2
        self.inorder(root, target)
        return self.result

node1 = Node(4, None, None)
node2 = Node(2, None, None)
node3 = Node(6, None, None)
node4 = Node(1, None, None)
node5 = Node(3, None, None)
node6 = Node(5, None, None)
node7 = Node(7, None, None)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
sol = Solution()
ans = sol.bst(node1)
print(ans)

# 秋招笔试

 # def solution(S):
#     n = len(S)
#     temp_sum, result = 0, 0
#     result_set = set()
#     for i in range(n):
#         temp_sum += int(S[i])
#
#     for j in range(n):
#         temp_sum -= int(S[j])
#         for k in range(10):
#             if (temp_sum+k)%3 == 0:
#                 temp_num = S[:j]+str(k)+S[j+1:]
#
#                 result_set.add(int(temp_num))
#                 # 本想直接计数， 但这样会导致0081，第一个位置取0和第二个取0重复计数，干脆用集合保存结果
#                 # 返回结果set中元素的个数
#                 # result += 1
#         temp_sum += int(S[j])
#     return len(result_set)


# def solution(S):
#     # write your code in Python 3.6
#     upper = set()
#     lower = set()
#     for c in S:
#         if ord(c) >= ord('A') and ord(c) <= ord('Z'):
#             upper.add(ord(c))
#         else:
#             lower.add(ord(c)-32)
#     intersect = upper & lower
#     if len(intersect)==0:
#         return 'NO'
#     else:
#         return chr(max(intersect))

def solution(B):
    if B is None or len(B)==0:
        return False
    row, col = len(B), len(B[0])
    board =[[B[i][j] for j in range(col)] for i in range(row)]
    stop_position = {'X', '<', '>', '^', 'v'}
    def blocked_area(board, row, col):
        # x，y用于在遍历中记录刺客的位置
        x, y = 0 ,0
        for i in range(row):
            for j in range(col):
                if board[i][j]=='<':
                    for k in range(j-1, -1, -1):
                        # 从右往左验证，如果是stop position，则停止
                        if board[i][k] in stop_position:
                            break
                        # 如果是'.'，则替换为新定义的障碍'S',为了后续和'X'区分，守卫自己不换
                        if board[i][k]=='.':
                            board[i][k] = 'S'
                        if board[i][k]=='A':
                            x, y = i, k
                            board[i][k] = 'S'
                if board[i][j]=='>':
                    for k in range(j+1,col):
                        if board[i][k] in stop_position:
                            break
                        # 如果是'.'，则替换为障碍'S',守卫自己不换
                        if board[i][k]=='.':
                            board[i][k] = 'S'
                        if board[i][k]=='A':
                            x, y = i, k
                            board[i][k] = 'S'
                if board[i][j]=='^':
                    for k in range(i-1, -1, -1):
                        # 从下往上验证
                        if board[k][j] in stop_position:
                            break
                        # 如果是'.'，则替换为障碍'X',守卫自己不换成'X'
                        if board[k][j]=='.':
                            board[k][j] = 'S'
                        if board[k][j]=='A':
                            x, y = k, j
                            board[k][j] = 'S'
                if board[i][j]=='v':
                    for k in range(i+1, row):
                        # 从上往下验证
                        if board[k][j] in stop_position:
                            break
                        # 如果是'.'，则替换为障碍'X',守卫自己不换成'X'
                        if board[k][j]=='.':
                            board[k][j] = 'S'
                        if board[k][j]=='A':
                            x, y = k, j
                            board[k][j] = 'S'
                if board[i][j]=='A':
                    x, y = i, j
        return x, y

    def isSafe(board, x, y):
        return x>=0 and x<row and y>=0 and y<col and (board[x][y] not in (stop_position|{'S'})) and (visited[x][y]==False)

    def getPath(board, x, y):
        if x==row-1 and y==col-1:
            return True
        if isSafe(board, x, y):
            visited[x][y] = True
            if getPath(board, x+1, y):
                return True
            if getPath(board, x-1, y):
                return True
            if getPath(board, x, y+1):
                return True
            if getPath(board, x, y-1):
                return True
            visited[x][y] = False
            return False
        else:
            return False

    start_x, start_y = blocked_area(board, row, col)
    visited = [[False]*col for _ in range(row)]
    if board[row-1][col-1] in (stop_position|{'S'}):
        return False
    res = getPath(board, start_x, start_y)
    return res
# ["...Xv", "AX..^", ".XX.."]
result = solution(['...', '>.A'])
print(result)
