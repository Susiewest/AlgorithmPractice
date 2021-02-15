# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                result.append(root.val)
                root = root.left
            else:
                temp = stack.pop()
                root = temp.right
        return result
执行用时：44 ms, 在所有 Python3 提交中击败了30.05%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了17.98%的用户

