直径不一定过root
首先想到dfs得到root左右子树的深度，可以获得通过当前节点的最长路径。
但是，直径不一定过root，按照上面的写法我们只能得到通过root的最长路径。
那么自底向上，探寻以每个节点为root，通过它的最长路径。
既要设置一个全局变量，保留当前最长路径，又要上传当前节点的子树深度，提供给下一个父节点

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_dia = 0
        def depth(root):
            if not root:
                return 0
            l_depth = depth(root.left)
            r_depth = depth(root.right)
            self.max_dia = max(self.max_dia,l_depth+r_depth)
            return max(l_depth,r_depth)+1
        depth(root)
        return self.max_dia
执行用时：48 ms, 在所有 Python3 提交中击败了87.91%的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了17.15%的用户

