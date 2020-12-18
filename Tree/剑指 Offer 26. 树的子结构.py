# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
这么写有问题，因为recur函数里，如果AB值相等就继续对比，进入下一层后如果不相等，就跳过这层，
在下层对比A.left.left和B.left,是不对的，应该有一个不等了就从头开始，我这个写法跳了一层依然在对比当前的点而非回到头部
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if B is None:
                return True
            if A is None:
                return False
            if A.val == B.val:
                return recur(A.left, B.left) and recur(A.right, B.right)
            else:
                return recur(A.left, B) or recur(A.right, B)
        if A is None or B is None:
            return False
        return recur(A, B)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if B is None:
                return True
            if A is None:
                return False
            if A.val!=B.val:
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)
        if A is None or B is None:
            return False
        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        
执行用时：136 ms, 在所有 Python3 提交中击败了49.59%的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了5.41%的用户

