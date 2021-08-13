# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorderlist = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.inorderlist.append(node.val)
            inorder(node.right)
        def build_bst(nums):
            if not nums:
                return None
            left, right = 0, len(nums)-1
            mid = (left+right)>>1
            root = TreeNode(nums[mid])
            root.left = build_bst(nums[:mid])
            root.right = build_bst(nums[mid+1:])
            return root
        inorder(root)
        return build_bst(self.inorderlist)
        
执行用时：204 ms, 在所有 Python3 提交中击败了68.56%的用户
内存消耗：21.7 MB, 在所有 Python3 提交中击败了5.24%的用户
