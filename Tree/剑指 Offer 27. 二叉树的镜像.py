一开始还没想到后序遍历，只是觉得要针对root.left/right调用递归
root.left = self.mirrorTree(root.right)
root.right = self.mirrorTree(root.left)
发现直接这样写会先改变了root.left，影响第二个递归函数
索性把赋值另外写
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        left = self.mirrorTree(root.right)
        right = self.mirrorTree(root.left)
        root.left, root.right = left, right
        return root
执行用时：36 ms, 在所有 Python3 提交中击败了82.62%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了13.24%的用户

