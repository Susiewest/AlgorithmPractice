# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxsum = -inf
        def max_sum(root):
            if root==None:
                return 0
            left = max(max_sum(root.left), 0)
            right = max(max_sum(root.right), 0)
            self.maxsum = max(self.maxsum, left+right+root.val)
            return root.val+max(left, right)
        max_sum(root)
        return self.maxsum
执行用时：80 ms, 在所有 Python3 提交中击败了83.60%的用户
内存消耗：22.5 MB, 在所有 Python3 提交中击败了6.10%的用户

为什么非要另外定义一个函数？为什么不能直接用函数返回最大值？
因为我们需要的结果和每层函数递归之前需要传递的信息是不同的。
我们最后想要maxsum，然而父亲节点并不想要左右孩子的maxsum，父亲节点只想要孩子所在的单支路径的最大sum，也就是孩子的val+孩子的左路径/右路径中的最大值。
因此递归函数应该返回root.val+max(left, right)而非self.max_sum。所以就需要另外写一个函数，然后调用这个函数后返回self.max_sum。

Attention！函数最后想要的结果，跟每层函数递归之间需要传递的信息不一致！
