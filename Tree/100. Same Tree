# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val==q.val:
           # return self.isSameTree(p.left,p.right) and self.isSameTree(q.left,q.right)
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            
            
            
'''Runtime: 52 ms, faster than 22.61% of Python3 online submissions for Same Tree.
Memory Usage: 13.7 MB, less than 86.99% of Python3 online submissions for Same Tree.'''
