# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left
执行用时：84 ms, 在所有 Python3 提交中击败了45.56%的用户
内存消耗：25.6 MB, 在所有 Python3 提交中击败了32.69%的用户

存在疑问，如果p是q的孩子，是不是找到q的时候直接就终止递归了，不会走到p
