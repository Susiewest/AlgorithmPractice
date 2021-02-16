# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or prev == root.right:
                result.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return result

执行用时：40 ms, 在所有 Python3 提交中击败了57.75%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.41%的用户

