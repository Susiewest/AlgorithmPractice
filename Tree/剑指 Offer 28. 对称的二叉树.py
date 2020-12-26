是个简单题 但我一上来就做错劳quq
对称指的是当前层最左边和最右边相等，而非当前节点的左右孩子相等，想当然唠
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not (root.left and root.right): return True
        if not root.left or not root.right or root.left.val!=root.right.val:
            return False
        if root.left == root.right:
            return self.isSymmetric(root.left) and self.isSymmetric(root.right)

经过分析，一共有两种需要判断是否相等的模式，一种是两边的，左的左和右的右
一种是中间的，左的右和右的左
所以重新定义一个含两个节点参数的recur函数8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not (L and R): return True
            if not L or not R or L.val!=R.val:
                return False
            if L.val == R.val:
                return recur(L.left,R.right) and recur(L.right, R.left)
        if not root:    return True
        return recur(root.left, root.right) 
这个写法对以下测试用例输出true，预期结果是False
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(None)
e = TreeNode(3)
f = TreeNode(None)
g = TreeNode(3)
a.left = b
a.right = c
b.left =d
b.right = e
c.left = f
c.right = g
我在pycharm里跑是没问题的，输出False，在力扣编译器就是true
然后修改了一个地方就ac了，那就是把 if not（L and R)改成了 if not L and not R
? 有事吗大哥
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val!=R.val:
                return False
            if L.val == R.val:
                return recur(L.left,R.right) and recur(L.right, R.left)
        if not root:    return True
        return recur(root.left, root.right) 
        
执行用时：36 ms, 在所有 Python3 提交中击败了93.25%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.16%的用户
