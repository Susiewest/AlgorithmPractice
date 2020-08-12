# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True
        return abs(self.depth(root.left)-self.depth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    #def里面套def 内部的def就不用self 递归也不用self. 
    #这种并列def都要各自self
    def depth(self,root):
        if root==None: return 0
        else: return max(self.depth(root.left),self.depth(root.right))+1
       
       
'''执行结果：
通过
执行用时：
88 ms, 在所有 Python3 提交中击败了16.75%的用户
内存消耗：
17.6 MB, 在所有 Python3 提交中击败了48.45%的用户'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#先序遍历，从下到上return的时候 如果有一个节点左右差大于1 就return-1给主函数 不然就继续return当前节点子树的层数
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True
        return self.downTotop(root)!=-1
    def downTotop(self,root):
        if root==None: return 0
        left=self.downTotop(root.left)
        #原本写的return False 但是true的时候return的是层数 二者类型不一致无法在主函数增加判断条件了
        if left==-1: return -1
        right=self.downTotop(root.right)
        if right==-1: return -1
        return max(left,right)+1 if abs(left-right)<=1 else -1
        

'''执行结果：
通过
执行用时：
64 ms, 在所有 Python3 提交中击败了73.07%的用户
内存消耗：
17.5 MB, 在所有 Python3 提交中击败了56.00%的用户'''
