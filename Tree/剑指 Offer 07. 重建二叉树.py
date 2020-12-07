和105题一样的噻 我把105分到dfs里了
相对位置的构建，每次都要重定位root在inorder里的位置
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #dic = {element:i for i, element in enumerate(inorder)}
        def dfs(preorder, inorder):
            if not preorder and not inorder:
                return None
            root = TreeNode(preorder[0])
            in_root = inorder.index(preorder[0])
            root.left = dfs(preorder[1:1+in_root], inorder[0:in_root])
            root.right = dfs(preorder[1+in_root:], inorder[in_root+1:])
            return root
        return dfs(preorder, inorder)
执行用时：192 ms, 在所有 Python3 提交中击败了45.21%的用户
内存消耗：86.6 MB, 在所有 Python3 提交中击败了5.04%的用户

绝对位置的构建
经常用的计算直接保存在一个常量里，看起来会比较舒服
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        chart = {element:i for i, element in enumerate(inorder)}
        def dfs(preleft, preright, inleft, inright):
            if preleft>preright or inleft>inright:
                return None
            root = TreeNode(preorder[preleft])
            in_root = chart[preorder[preleft]]
            left_num = in_root-inleft
            root.left = dfs(preleft+1, preleft+left_num, inleft, in_root-1)
            root.right = dfs(preleft+left_num+1, preright, in_root+1, inright)
            return root
        return dfs(0, len(preorder)-1, 0, len(inorder)-1)
执行用时：48 ms, 在所有 Python3 提交中击败了94.36%的用户
内存消耗：18.4 MB, 在所有 Python3 提交中击败了64.81%的用户
