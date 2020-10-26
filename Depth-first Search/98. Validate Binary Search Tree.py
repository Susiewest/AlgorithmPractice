#一开始写的是当前节点的右节点大于当前，左节点小于当前
#发现不行 不能单纯的只跟父节点比 父节点的父节点也起到了限制范围的作用
#改为对每个当前节点和上层限制的判断
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #result=True
        def bst(root:TreeNode,lower,upper):
            if not root:
                return True
            if root.val>=upper or root.val<=lower:
                return False
            if not bst(root.right,root.val,upper):
                return False
            if not bst(root.left,lower,root.val):
                return False
            return True

 
        return bst(root,-inf, inf)

执行用时：40 ms, 在所有 Python3 提交中击败了99.78%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了42.46%的用户
