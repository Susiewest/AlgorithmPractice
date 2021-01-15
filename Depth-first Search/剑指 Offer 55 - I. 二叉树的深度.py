# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1
执行用时：44 ms, 在所有 Python3 提交中击败了88.33%的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了6.74%的用户

