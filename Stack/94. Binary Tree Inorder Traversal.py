#递归中序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        def dfs(root:TreeNode):
            if root is None: return
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        dfs(root)
        return result
执行用时：40 ms, 在所有 Python3 提交中击败了70.96%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.46%的用户


#迭代中序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        stack=[]
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                temp=stack.pop()
                result.append(temp.val)
                root=temp.right
        return result
执行用时：44 ms, 在所有 Python3 提交中击败了45.25%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.46%的用户

