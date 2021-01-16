先序+树深 复杂度高
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getlevel(root):
            if not root: return 0
            left = getlevel(root.left)
            right = getlevel(root.right)
            return max(left,right)+1
        if not root: return True
        left = getlevel(root.left)
        right = getlevel(root.right)
        if abs(left-right)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False        
执行用时：108 ms, 在所有 Python3 提交中击败了5.34%的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了5.27%的用户

考虑剪枝 有一个不满足就一直往上return -1， 满足则return 当前节点层数
属于后序遍历，先判断左右，不满足直接return-1，满足再判断根

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            right = recur(root.right)
            if left==-1 or right==-1:
                return -1
            if abs(left-right)<=1:
                return max(left,right)+1
            else:
                return -1
        return recur(root)!=-1
执行用时：72 ms, 在所有 Python3 提交中击败了32.87%的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了6.83%的用户

       
