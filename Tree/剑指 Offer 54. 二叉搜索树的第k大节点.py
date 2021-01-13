# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 这个k要全局维护，如果不写成self.k,子节点层k==0了，退回到父节点层k还是=1，又会更新一次result
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if root is None:
                return            
            dfs(root.right)
            if self.k==0: return
            if root:
                self.k-=1
            if self.k==0:
                self.result = root.val
            dfs(root.left)
 
        self.k = k
        dfs(root)
        return self.result

执行用时：56 ms, 在所有 Python3 提交中击败了83.27%的用户
内存消耗：18.5 MB, 在所有 Python3 提交中击败了17.36%的用户
