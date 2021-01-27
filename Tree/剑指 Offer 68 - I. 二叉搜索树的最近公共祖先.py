# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
执行用时：84 ms, 在所有 Python3 提交中击败了78.08%的用户
内存消耗：18.7 MB, 在所有 Python3 提交中击败了26.64%的用户


递归转迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>q.val:
            p, q = q, p 
        while root:
            if p.val>root.val:
                root = root.right
            elif q.val<root.val:
                root = root.left
            else:
                break
        return root

执行用时：96 ms, 在所有 Python3 提交中击败了29.49%的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了13.27%的用户

