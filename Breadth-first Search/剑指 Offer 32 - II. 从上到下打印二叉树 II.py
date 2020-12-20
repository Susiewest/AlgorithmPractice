设置了工作queue，辅助工作tmp，result
每次不要忘了考虑边界 if not root 避免每次根据报错增加边界的习惯！
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)    
            result.append(tmp)       
        return result
执行用时：52 ms, 在所有 Python3 提交中击败了13.34%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.08%的用户

