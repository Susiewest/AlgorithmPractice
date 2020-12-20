这题奇数层从左到右，偶数层从右到左
我设置了一个flag标志位，每次操作后取反，以此来区分奇偶层
看答案有个更好的办法，if len（result）%2: 当前层是偶数层
else当前层是奇数层 不错子！学到了！
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        result = []
        queue.append(root)
        flag = -1
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if flag>0:
                tmp = tmp[::-1]
            flag = -flag
            result.append(tmp)
        return result
 
执行用时：44 ms, 在所有 Python3 提交中击败了56.50%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.06%的用户
