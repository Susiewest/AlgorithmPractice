# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        left=self.minDepth(root.left)
        right=self.minDepth(root.right)
        #当树为单边树时 return min+1会导致选择没有子树的那边 但是我们想要有叶节点的一边
        #所以有一孩子为空树的时候不能选择空树 要选择较大的一侧了
        return min(left,right)+1 if left and right else max(left,right)+1 
        
        
'''执行结果：
通过
执行用时：
60 ms, 在所有 Python3 提交中击败了49.50%的用户
内存消耗：
15.3 MB, 在所有 Python3 提交中击败了65.25%的用户'''
