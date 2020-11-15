找p&q最近公共祖先节点 通常有以下两种情况：
1. 当前节点的左边有一个p 右边一个q 则当前节点是祖先
2. 当前节点左边无p或q 自己等于p或q 另一个节点在右子树，
  或当前节点右边无pq 另一个在左子树
所以要先确定pq在不在左右两侧，是的话返回当前root 某侧不在的话将另一侧的查找结果返回
采用后序遍历既能先检查左右再确定当前根节点，又能从叶节点往上找，自下而上，找到第一个祖先节点，也就是所谓的“最近祖先”

一个疑问，为什么找到一个相等的节点就return他自己呢，这个相等的节点又不一定是祖先？
解答：因为当前的return只是传递给了上一层，但是在上一层并不是继续return这层的结果，而是综合考虑left right的情况，采纳新的逻辑return一个并不一定一致的结果
比如 如果当前节点==p q是p的父亲，那么当前节点return p自己，到了q，q也会return q自己，这样最后传上去的是q而非p
如果q的父亲和p是兄弟，那么到了p的父节点层，会发现pq分别在两侧，会return p的父节点

我还有一个想法，设置两个list保存找到p和q的路径，在较短的list里从后往前找到第一个在较长list的元素，就是最近公共祖先

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left
        
执行用时：68 ms, 在所有 Python3 提交中击败了98.88%的用户
内存消耗：24 MB, 在所有 Python3 提交中击败了35.31%的用户

