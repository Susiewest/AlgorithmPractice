# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        
        
 '''Runtime: 48 ms, faster than 47.13% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.4 MB, less than 28.30% of Python3 online submissions for Maximum Depth of Binary Tree.'''
