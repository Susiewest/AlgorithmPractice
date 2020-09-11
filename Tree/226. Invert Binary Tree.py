# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


'''执行用时：
52 ms, 在所有 Python3 提交中击败了9.77%的用户
内存消耗：
13.7 MB, 在所有 Python3 提交中击败了52.43%的用户'''
